"""Build the downloadable R2025b block-library resource and its OVPack.

The packaged library under ``openviking/parse/parsers/matlab/simulink-block-library``
stays the single source of truth for the parser. This module stages a copy with
directory ``.abstract.md`` (L0) and ``.overview.md`` (L1) pages derived from each
directory's own ``index.md``, then writes an OVPack whose root is
``viking://resources/simulink-block-library``. No network access or LLM is used.
"""

from __future__ import annotations

import json
import re
import shutil
import zipfile
from pathlib import Path
from urllib.parse import quote

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
_ENTRY = re.compile(r"^- \[(?P<name>.+?)\]\((?P<target>[^)]+)\)\s*$")
_HEADING = re.compile(r"^#\s+(?P<title>.+?)\s*$")
_SUMMARY_SECTION = {"zh": "## 描述", "en": "## Description"}
_ENTRY_LABEL = {"zh": "目录内容", "en": "Contents"}
_COUNT_LABEL = {"zh": "条目", "en": "entries"}
_INDEX = "index.md"


def _language(relative: Path) -> str:
    top = relative.parts[0] if relative.parts else ""
    return "en" if top == "en" else "zh"


def _clean(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class Summaries:
    """One-line descriptions taken from each document's own description section."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self._cache: dict[Path, str] = {}

    def for_file(self, path: Path, language: str) -> str:
        if path in self._cache:
            return self._cache[path]
        summary = ""
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            text = ""
        marker = _SUMMARY_SECTION[language]
        start = text.find(f"\n{marker}\n")
        if start >= 0:
            body = text[start + len(marker) + 2 :]
            paragraph = body.split("\n\n", 1)[0]
            summary = _clean(paragraph)[:180]
        self._cache[path] = summary
        return summary


def _directory_entries(directory: Path) -> tuple[str, list[tuple[str, str]]]:
    index = directory / _INDEX
    title = directory.name
    entries: list[tuple[str, str]] = []
    if not index.is_file():
        readme = directory / "README.md"
        if readme.is_file():
            for line in readme.read_text(encoding="utf-8").splitlines():
                if match := _HEADING.match(line):
                    title = _clean(match.group("title"))
                    break
        entries = [
            (child.name, f"{quote(child.name)}/")
            for child in sorted(directory.iterdir(), key=lambda item: item.name)
            if child.is_dir() and not child.name.startswith(".")
        ]
        return title, entries
    for line in index.read_text(encoding="utf-8").splitlines():
        if match := _HEADING.match(line):
            title = _clean(match.group("title"))
            continue
        if match := _ENTRY.match(line.strip()):
            entries.append((_clean(match.group("name")), match.group("target")))
    return title, entries


def _front_matter(uri: str, entries: int) -> list[str]:
    return [
        "---",
        f"directory: {uri}",
        "generated_by:",
        "  component: block-library-pack",
        "  trigger: pack_build",
        "freshness:",
        f"  total_entries: {entries}",
        f"  sampled_entries: {entries}",
        "  unsampled_entries: 0",
        "  pending_child_changes: 0",
        "---",
        "",
    ]


def _abstract(title: str, entries: list[tuple[str, str]], language: str) -> str:
    names = [name for name, _ in entries]
    head = names[:6]
    listing = "、".join(head) if language == "zh" else ", ".join(head)
    more = len(names) - len(head)
    if language == "zh":
        sentence = f"{title} 收录 {len(entries)} 个条目"
        if listing:
            sentence += f"，例如 {listing}"
            sentence += " 等" if more > 0 else ""
        return f"{sentence}。目录按 Simulink Library Browser 的层级组织，可逐级进入查看块说明。"
    sentence = f"{title} lists {len(entries)} entries"
    if listing:
        sentence += f", including {listing}"
        sentence += ", among others" if more > 0 else ""
    return f"{sentence}. The directory follows the Simulink Library Browser hierarchy."


def _overview(
    title: str,
    entries: list[tuple[str, str]],
    directory: Path,
    language: str,
    summaries: Summaries,
) -> str:
    label = _ENTRY_LABEL[language]
    lines = [f"# {title}", ""]
    lines.append(_abstract(title, entries, language))
    if not entries:
        return "\n".join(lines) + "\n"
    lines.extend(["", f"## {label}", ""])
    for name, target in entries:
        decoded = target.replace("%20", " ").replace("%26", "&")
        described = ""
        candidate = (directory / decoded).resolve()
        if candidate.is_file() and candidate.suffix == ".md":
            described = summaries.for_file(candidate, language)
        line = f"- [{name}]({target})"
        if described:
            line += f" — {described}"
        lines.append(line)
    return "\n".join(lines) + "\n"


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


def build_tree(source: Path, target: Path, root_name: str) -> int:
    """Copy the library and add L0/L1 pages to every directory."""
    summaries = Summaries(source)
    staged = target / root_name
    shutil.copytree(
        source,
        staged,
        ignore=shutil.ignore_patterns("manifest.json", "__pycache__", "*.pyc"),
    )
    _sanitize_names(staged)
    written = 0
    for directory in [staged, *sorted(path for path in staged.rglob("*") if path.is_dir())]:
        if not any(directory.iterdir()) and directory != staged:
            continue
        title, entries = _directory_entries(directory)
        language = _language(directory.relative_to(staged))
        relative = directory.relative_to(staged).as_posix()
        uri = f"viking://{RESOURCE_SCOPE}/{root_name}/"
        if relative != ".":
            uri += f"{relative}/"
        front_matter = "\n".join(_front_matter(uri, len(entries))).rstrip() + "\n\n"
        (directory / ".abstract.md").write_text(
            front_matter + _abstract(title, entries, language) + "\n",
            encoding="utf-8",
        )
        (directory / ".overview.md").write_text(
            front_matter + _overview(title, entries, directory, language, summaries),
            encoding="utf-8",
        )
        written += 1
    return written


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
