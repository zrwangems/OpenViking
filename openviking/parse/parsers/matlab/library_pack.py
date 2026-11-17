"""Stage the R2025b block-library resource and pack it as an OVPack.

The packaged library under ``openviking/parse/parsers/matlab/simulink-block-library``
stays the single source of truth for the parser. This module copies it into a
pack root (optionally one language), drops the per-directory ``index.md``, and
writes an OVPack. It generates no summaries: L0/L1 belong to ingestion, where
OpenViking's semantic processor writes them with the VLM.
"""
from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path

from openviking.storage.ovpack.format import (
    OVPACK_FILES_DIR,
    OVPACK_FORMAT_VERSION,
    OVPACK_INDEX_RECORDS_PATH,
    OVPACK_INTERNAL_DIR,
    OVPACK_KIND,
    OVPACK_MANIFEST_ZIP_LEAF,
    get_ovpack_zip_path,
    internal_zip_path,
    jsonl_bytes,
    manifest_content_sha256,
    sha256_hex,
)
from openviking.storage.ovpack.manifest import (
    read_manifest,
    validate_manifest_root_matches_zip,
)
from openviking.storage.ovpack.validation import (
    base_name_from_entries,
    validate_manifest_content,
    validated_import_members,
)
from openviking_cli.utils.uri import VikingURI

DEFAULT_ROOT = "simulink-block-library"
RESOURCE_SCOPE = "resources"
INDEX_NAME = "index.md"
"""Per-directory navigation page. The resource keeps block documents only:
OpenViking builds directory summaries at ingestion, so a hand-written index
duplicates navigation and adds nothing an agent can search."""


def _sanitize_names(staged: Path) -> int:
    """Remove backslashes from file names; OVPack rejects them as unsafe paths."""
    renamed: dict[str, str] = {}
    for path in sorted(staged.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if "\\" not in path.name:
            continue
        safe = path.with_name(path.name.replace("\\", ""))
        if safe.exists():
            raise SystemExit(f"renaming would collide: {path} -> {safe}")
        renamed[path.name] = safe.name
        path.rename(safe)
    if renamed:
        for document in staged.rglob("*.md"):
            text = document.read_text(encoding="utf-8")
            updated = text.replace("%5C", "").replace("\\\\", "\\")
            if updated != text:
                document.write_text(updated, encoding="utf-8")
    return len(renamed)


def build_tree(
    source: Path,
    target: Path,
    root_name: str,
    language: str | None = None,
) -> int:
    """Stage the library for import: block documents only, optional language split.

    ``language`` ``"zh"``/``"en"`` stages just that language and makes it the
    resource root, so the Library Browser products sit directly under
    ``viking://resources/<root_name>/``. ``None`` keeps the two-language layout.
    Directory ``index.md`` pages are dropped for the reason described on
    ``INDEX_NAME``; L0/L1 come from OpenViking's own ingestion, never from here.
    """
    if language is not None and language not in {"zh", "en"}:
        raise ValueError(f"language must be 'zh' or 'en', got {language!r}")
    staged = target / root_name
    source_root = source if language is None else source / language
    if not source_root.is_dir():
        raise ValueError(f"library directory not found: {source_root}")
    shutil.copytree(
        source_root,
        staged,
        ignore=shutil.ignore_patterns("manifest.json", INDEX_NAME, "__pycache__", "*.pyc"),
    )
    _sanitize_names(staged)
    removed_empty = 0
    for directory in sorted((path for path in staged.rglob("*") if path.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()
            removed_empty += 1
    return removed_empty


def pack(root: Path, target: Path, root_name: str) -> dict[str, object]:
    root_uri = f"viking://{RESOURCE_SCOPE}/{root_name}"
    directories: list[str] = []
    files: list[str] = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_dir():
            directories.append(relative)
        elif path.is_file():
            files.append(relative)
        else:
            raise SystemExit(f"unsupported entry: {path}")
    file_entries = {
        relative: {
            "path": relative,
            "kind": "file",
            "size": (root / relative).stat().st_size,
            "sha256": sha256_hex((root / relative).read_bytes()),
        }
        for relative in files
    }
    entries = [{"path": "", "kind": "directory"}]
    entries.extend({"path": relative, "kind": "directory"} for relative in directories)
    entries.extend(file_entries[relative] for relative in files)
    manifest = {
        "kind": OVPACK_KIND,
        "format_version": OVPACK_FORMAT_VERSION,
        "root": {"name": root_name, "uri": root_uri, "scope": VikingURI(root_uri).scope},
        "entries": entries,
        "content_sha256": manifest_content_sha256(file_entries),
    }
    index_bytes = jsonl_bytes([])
    manifest["index"] = {
        "records": {
            "path": OVPACK_INDEX_RECORDS_PATH,
            "count": 0,
            "sha256": sha256_hex(index_bytes),
        }
    }
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr(f"{root_name}/{OVPACK_FILES_DIR}/", "")
        for relative in directories:
            archive.writestr(get_ovpack_zip_path(root_name, relative) + "/", "")
        for relative in files:
            archive.write(root / relative, get_ovpack_zip_path(root_name, relative))
        archive.writestr(f"{root_name}/{OVPACK_INTERNAL_DIR}/", "")
        archive.writestr(internal_zip_path(root_name, OVPACK_INDEX_RECORDS_PATH), index_bytes)
        archive.writestr(
            f"{root_name}/{OVPACK_MANIFEST_ZIP_LEAF}",
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8"),
        )
    with zipfile.ZipFile(target) as archive:
        infolist = archive.infolist()
        base_name = base_name_from_entries(infolist)
        parsed = read_manifest(archive, base_name)
        validate_manifest_root_matches_zip(parsed, base_name)
        validate_manifest_content(archive, parsed, infolist, base_name)
        members = validated_import_members(infolist, base_name, root_uri)
    return {
        "package": str(target),
        "bytes": target.stat().st_size,
        "root_uri": root_uri,
        "directories": len(directories) + 1,
        "files": len(files),
        "abstracts": sum(relative.endswith(".abstract.md") for relative in files),
        "overviews": sum(relative.endswith(".overview.md") for relative in files),
        "members_validated": len(members),
    }


def build_language_pack(
    source: Path,
    target: Path,
    root_name: str,
    language: str,
) -> dict[str, object]:
    """Build one single-language package whose root is the library itself."""
    import tempfile

    source = Path(source)
    target = Path(target)
    with tempfile.TemporaryDirectory(prefix="block-library-") as staging:
        build_tree(source, Path(staging), root_name, language=language)
        return pack(Path(staging) / root_name, target, root_name)


def _main(argv: list[str] | None = None) -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="packaged simulink-block-library directory")
    parser.add_argument("--out", required=True, help="OVPack path to write")
    parser.add_argument("--name", default=DEFAULT_ROOT, help="resource name inside the pack")
    parser.add_argument("--language", choices=("zh", "en"), help="single-language pack")
    args = parser.parse_args(argv)

    source = Path(args.source)
    if args.language:
        summary = build_language_pack(source, Path(args.out), args.name, args.language)
    else:
        summary = pack(source, Path(args.out), args.name)
    json.dump(summary, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
