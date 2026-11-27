# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Ingest tiers for MATLAB project files: location → category → redundancy → default.

Every file of an imported project is decided by the same chain, from the
strongest evidence to the weakest:

1. **Location.** Build/cache folders are never imported, ``resources/project``
   state and the ``.prj`` file only reach the aggregation table.
2. **Category.** ``RULES`` maps an extension or a name glob (``.mex*``,
   ``.slx.r*``) to a category, an action and a summary strategy.
3. **Redundancy.** A file that has a generated source in the project, or that
   repeats bytes of another file, is recorded instead of imported.
4. **Default.** An unknown extension is kept as the original file and tagged
   ``unclassified``; it is never dropped silently.
"""

from __future__ import annotations

import fnmatch
import hashlib
import posixpath
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple

from openviking.parse.parsers.matlab.ignore import project_resources_index

CATEGORY_TEXT = "可读文本"
CATEGORY_CONTAINER = "ZIP/工具容器"
CATEGORY_DATA = "数据/目标二进制"
CATEGORY_NATIVE = "Windows 原生"
CATEGORY_OPAQUE = "加密/保护"
CATEGORY_DERIVED = "派生/缓存"
CATEGORY_MEDIA = "图像/三维模型"

ACTION_IMPORT = "import"
ACTION_EXCLUDE = "exclude"
ACTION_ATTACH = "attach"
ACTION_AGGREGATE = "aggregate"

SUMMARY_PARSE = "parse"
SUMMARY_ORIGINAL = "original"
SUMMARY_ON_DEMAND = "on_demand"
SUMMARY_AGGREGATE = "aggregate"

TAG_UNCLASSIFIED = "unclassified"
TAG_POSSIBLE_REDUNDANT = "possible_redundant"

BUILD_DIR_NAMES = frozenset({"slprj", "sfprj"})
BUILD_DIR_GLOBS = ("*_rtw",)
PROJECT_BUILD_DIR_NAMES = frozenset({"codegen"})
BUILD_OUTPUT_DIR_NAMES = frozenset({"build", "output", "out", "target", "release", "debug"})
RUNTIME_DIR_NAMES = frozenset({"rsim", "raccel", "sim"})

DERIVED_EXTS = frozenset({".slxc", ".autosave"})
TARGET_OUTPUT_EXTS = frozenset({".hex", ".s19", ".elf", ".bin"})
BUILD_SCRIPT_EXTS = frozenset({".mk", ".bat", ".rsp"})
NATIVE_BUILD_EXTS = frozenset({".mexw64", ".mexw32", ".dll", ".exe", ".lib", ".obj", ".pdb"})
SLPRJ_BUILD_EXTS = frozenset({".lib", ".obj", ".pdb", ".mk", ".bat", ".rsp"})

# A file listed here is a package, not knowledge: identical bytes elsewhere in
# the project, or a model of the same name, mean the copy is generated.
DUPLICATE_CONTAINER_EXTS = frozenset({".fmu", ".ctf", ".jar", ".mltbx", ".mlproj"})
DUPLICATE_HASH_MAX_BYTES = 64 * 1024 * 1024

# Export → formats that generate it. ``.fig`` draws the ``.png``, a script or
# Live Script writes the ``.html`` report, a ``.mat`` backs the ``.csv`` dump.
EXPORT_SOURCES: Mapping[str, Tuple[str, ...]] = {
    ".png": (".fig",),
    ".html": (".m", ".mlx"),
    ".csv": (".mat",),
}
# An App screenshot next to its ``.mlapp`` is likely redundant, but a picture in
# the App's main folder is not proven to be one, so it is only flagged.
POSSIBLE_EXPORT_SOURCES: Mapping[str, Tuple[str, ...]] = {
    ".png": (".mlapp",),
}


@dataclass(frozen=True)
class Rule:
    """One row of the ingest table: category, match, action and summary strategy."""

    categories: Tuple[str, ...]
    exts: Tuple[str, ...] = ()
    globs: Tuple[str, ...] = ()
    action: str = ACTION_IMPORT
    summary: str = SUMMARY_PARSE


# Ordered: the first row that matches decides. Containers and derived files
# come before their plain-text relatives so a rule can be read on its own.
RULES: Tuple[Rule, ...] = (
    Rule(
        (CATEGORY_DERIVED,),
        exts=(".slxc", ".autosave"),
        action=ACTION_EXCLUDE,
        summary=SUMMARY_ORIGINAL,
    ),
    Rule(
        (CATEGORY_TEXT,),
        exts=(".rtw", ".tmf"),
        action=ACTION_EXCLUDE,
        summary=SUMMARY_ORIGINAL,
    ),
    # The .prj is a 107-byte shell: it names the project, it is not content.
    Rule(
        (CATEGORY_TEXT,),
        exts=(".prj",),
        action=ACTION_AGGREGATE,
        summary=SUMMARY_AGGREGATE,
    ),
    # Models, dictionaries, requirement/test/report containers.
    Rule(
        (CATEGORY_CONTAINER,),
        exts=(
            ".slx",
            ".mlx",
            ".mlapp",
            ".slreqx",
            ".slmx",
            ".mldatx",
            ".sfx",
            ".sltx",
            ".mlproj",
            ".mltbx",
            ".jar",
            ".fmu",
        ),
        summary=SUMMARY_PARSE,
    ),
    Rule(
        (CATEGORY_CONTAINER, CATEGORY_DATA),
        exts=(".sldd",),
        summary=SUMMARY_PARSE,
    ),
    Rule(
        (CATEGORY_CONTAINER, CATEGORY_OPAQUE),
        exts=(".ctf",),
        summary=SUMMARY_PARSE,
    ),
    Rule(
        (CATEGORY_TEXT,),
        exts=(".mdl",),
        summary=SUMMARY_PARSE,
    ),
    # Installers are kept as the file itself; their members are not unpacked.
    Rule(
        (CATEGORY_CONTAINER,),
        exts=(".mlappinstall", ".mlpkginstall"),
        summary=SUMMARY_ORIGINAL,
    ),
    Rule(
        (CATEGORY_DATA,),
        exts=(".fig", ".mat", ".mdf", ".mf4", ".blf"),
        summary=SUMMARY_PARSE,
    ),
    # A model backup (model.slx.r2023a) is still a model container.
    Rule(
        (CATEGORY_CONTAINER,),
        globs=("*.slx.r*",),
        summary=SUMMARY_PARSE,
    ),
    # Opaque but still read for their manifest.
    Rule(
        (CATEGORY_OPAQUE,),
        exts=(".slxp", ".mdlp", ".sscp"),
        summary=SUMMARY_PARSE,
    ),
    # Native binaries travel with the project; the original bytes are enough.
    Rule(
        (CATEGORY_NATIVE,),
        exts=(".dll", ".exe", ".lib", ".obj", ".pdb"),
        globs=("*.mex*", "*.ilk"),
        summary=SUMMARY_ORIGINAL,
    ),
    Rule(
        (CATEGORY_OPAQUE,),
        exts=(".p",),
        summary=SUMMARY_ORIGINAL,
    ),
    # Delivered firmware stays next to the project; an .elf/.map is only read
    # (ELF symbols and sections, MAP segment usage) when someone asks for it.
    Rule(
        (CATEGORY_DATA,),
        exts=(".hex", ".s19", ".bin"),
        action=ACTION_ATTACH,
        summary=SUMMARY_ORIGINAL,
    ),
    Rule(
        (CATEGORY_DATA,),
        exts=(".elf", ".map"),
        action=ACTION_ATTACH,
        summary=SUMMARY_ON_DEMAND,
    ),
    Rule(
        (CATEGORY_MEDIA,),
        exts=(".stl",),
        action=ACTION_ATTACH,
        summary=SUMMARY_ORIGINAL,
    ),
    Rule(
        (CATEGORY_MEDIA,),
        exts=(".png", ".gif", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".svg"),
        summary=SUMMARY_PARSE,
    ),
    Rule(
        (CATEGORY_MEDIA,),
        exts=(".wrl",),
        summary=SUMMARY_ORIGINAL,
    ),
    # Source, configuration and generated reports stay the file itself.
    Rule(
        (CATEGORY_TEXT,),
        exts=(
            ".m",
            ".ssc",
            ".tlc",
            ".c",
            ".h",
            ".cpp",
            ".hpp",
            ".mk",
            ".bat",
            ".rsp",
            ".html",
            ".asv",
            ".tlh",
            ".py",
            ".xml",
            ".json",
            ".yaml",
            ".yml",
            ".csv",
            ".txt",
            ".ini",
            ".arxml",
            ".dbc",
            ".ldf",
            ".a2l",
            ".md",
            ".xlsx",
            ".dmr",
            ".twm",
        ),
        summary=SUMMARY_ORIGINAL,
    ),
)

# Tags that describe the file itself, independent of where it sits.
INHERENT_TAGS: Dict[str, Tuple[str, ...]] = {
    ".slxc": ("slprj", "runtime"),
}

# A glob family has one category; only the lookup by extension needs names.
GLOB_FAMILY_MEMBERS: Mapping[str, Tuple[str, ...]] = {
    "*.mex*": (".mexw64", ".mexw32", ".mexa64", ".mexmaci64"),
    "*.ilk": (".ilk",),
    "*.slx.r*": (),
}

_EXTENSION_CATEGORY: Dict[str, Tuple[str, ...]] = {}
for _rule in RULES:
    for _ext in _rule.exts:
        _EXTENSION_CATEGORY.setdefault(_ext, _rule.categories)
    for _glob in _rule.globs:
        for _ext in GLOB_FAMILY_MEMBERS.get(_glob, ()):
            _EXTENSION_CATEGORY.setdefault(_ext, _rule.categories)
del _rule, _ext, _glob

_FILENAME_GLOBS: Tuple[Tuple[Rule, Tuple[str, ...]], ...] = tuple(
    (rule, tuple(pattern.casefold() for pattern in rule.globs)) for rule in RULES if rule.globs
)

_RESOURCE_CATEGORY = re.compile(r"FileClassCategory.*?<Label UUID=\"([^\"]+)\"", re.S)
_RESOURCE_LOCATION = re.compile(r"<Info\b[^>]*\blocation=\"([^\"]*)\"")


def categories_for(ext: str) -> Tuple[str, ...]:
    """Categories of an extension; empty when the ingest table does not know it."""
    return _EXTENSION_CATEGORY.get(ext.lower(), ())


def rule_for(name: str) -> Optional[Rule]:
    """The first table row matching a file name, by extension or glob."""
    ext = Path(name).suffix.lower()
    for rule in RULES:
        if ext in rule.exts:
            return rule
    folded = name.casefold()
    for rule, patterns in _FILENAME_GLOBS:
        if any(fnmatch.fnmatch(folded, pattern) for pattern in patterns):
            return rule
    return None


def _relative_parts(rel_path: str | Path) -> Tuple[str, ...]:
    return tuple(part for part in Path(rel_path).parts if part not in {"", "."})


def _matches(name: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(name.casefold(), pattern) for pattern in patterns)


def _build_dir(rel_parts: Sequence[str]) -> Optional[Tuple[int, str]]:
    """Return the outermost build-directory part and its index, if any."""
    for index, part in enumerate(rel_parts[:-1]):
        name = part.casefold()
        if name in BUILD_DIR_NAMES or _matches(name, BUILD_DIR_GLOBS):
            return index, name
        if name in PROJECT_BUILD_DIR_NAMES or name in BUILD_OUTPUT_DIR_NAMES:
            return index, name
    return None


def _is_runtime_location(rel_parts: Sequence[str]) -> bool:
    lowered = [part.casefold() for part in rel_parts]
    if "slprj" in lowered:
        after = lowered[lowered.index("slprj") + 1 :]
        return bool(after) and after[0] in RUNTIME_DIR_NAMES
    return False


def _build_output_location(rel_parts: Sequence[str]) -> bool:
    return any(part.casefold() in BUILD_OUTPUT_DIR_NAMES for part in rel_parts[:-1])


def _location_label(rel_parts: Sequence[str], build: Optional[Tuple[int, str]]) -> str:
    if build is not None:
        index, _ = build
        suffix = " → ".join(rel_parts[index:])
        return f"{suffix}/" if not suffix.endswith("/") else suffix
    if _build_output_location(rel_parts):
        return "构建输出目录"
    return "工程目录"


def classify_path(rel_path: str | Path) -> dict[str, object]:
    """Classify one project-relative path into categories, tags, action and summary."""
    parts = _relative_parts(rel_path)
    name = parts[-1] if parts else ""
    ext = Path(name).suffix.lower()
    build = _build_dir(parts)
    runtime = _is_runtime_location(parts)
    generated = build is not None or _build_output_location(parts)
    rule = rule_for(name)
    resources_index = project_resources_index(parts)

    tags: List[str] = list(INHERENT_TAGS.get(ext, ()))
    if build is not None:
        build_name = build[1]
        if build_name in BUILD_DIR_NAMES or build_name == "sfprj":
            tags.append("slprj")
        if _matches(build_name, BUILD_DIR_GLOBS) or build_name in PROJECT_BUILD_DIR_NAMES:
            tags.append("codegen")
        if ext in BUILD_SCRIPT_EXTS or ext in NATIVE_BUILD_EXTS or ext == ".map":
            tags.append("build")
        if ext in SLPRJ_BUILD_EXTS and "slprj" not in tags:
            tags.append("slprj")
    if runtime:
        for tag in ("runtime", "slprj"):
            if tag not in tags:
                tags.append(tag)
    if ext in TARGET_OUTPUT_EXTS and generated:
        for tag in ("codegen", "target"):
            if tag not in tags:
                tags.append(tag)

    categories = list(rule.categories) if rule else []
    action = rule.action if rule else ACTION_IMPORT
    summary = rule.summary if rule else SUMMARY_ORIGINAL
    reason = "工程目录内导入"

    # 1. Location outranks category.
    if build is not None:
        action, reason = ACTION_EXCLUDE, "matlab build/cache"
    elif resources_index is not None:
        categories = categories or [CATEGORY_TEXT]
        action, summary, reason = ACTION_AGGREGATE, SUMMARY_AGGREGATE, "工程 resources 只进聚合表"
    elif action == ACTION_AGGREGATE:
        reason = "MATLAB 工程文件只进聚合表"
    # 2. Category.
    elif action == ACTION_EXCLUDE:
        reason = "matlab derived file" if ext in DERIVED_EXTS else "构建模板副本"
    elif action == ACTION_ATTACH:
        reason = "交付附件" if summary == SUMMARY_ORIGINAL else "交付附件，按需提取"
    elif ext == ".bat":
        reason = "启动脚本"
        tags.append("startup")
    elif rule is None:
        # 4. Default: keep the original file, and say that it is a guess.
        action, summary = ACTION_IMPORT, SUMMARY_ORIGINAL
        categories = [CATEGORY_TEXT]
        tags.append(TAG_UNCLASSIFIED)
        reason = "未识别扩展名，保留原件"

    return {
        "path": Path(*parts).as_posix() if parts else "",
        "extension": ext,
        "categories": categories,
        "tags": tags,
        "location": _location_label(parts, build),
        "action": action,
        "summary": summary,
        "reason": reason,
    }


def classify_directory(rel_path: str | Path) -> dict[str, object]:
    """Labels for a directory that is pruned as build/cache before its files."""
    parts = _relative_parts(rel_path)
    lowered = [part.casefold() for part in parts]
    tags: List[str] = []
    if any(part in BUILD_DIR_NAMES or part == "sfprj" for part in lowered):
        tags.append("slprj")
    if any(_matches(part, BUILD_DIR_GLOBS) for part in lowered):
        tags.append("codegen")
    if any(part in PROJECT_BUILD_DIR_NAMES for part in lowered):
        tags.append("codegen")
    if any(part in RUNTIME_DIR_NAMES for part in lowered):
        for tag in ("runtime", "slprj"):
            if tag not in tags:
                tags.append(tag)
    if any(part in BUILD_OUTPUT_DIR_NAMES for part in lowered):
        tags.append("build")
    return {
        "path": Path(*parts).as_posix(),
        "extension": "",
        "categories": [CATEGORY_DERIVED],
        "tags": list(dict.fromkeys(tags)),
        "location": "构建/缓存目录",
        "action": ACTION_EXCLUDE,
        "summary": SUMMARY_ORIGINAL,
        "reason": "matlab build/cache",
    }


def summarize(files: Iterable[dict[str, object]]) -> dict[str, object]:
    """Count categories, tags, actions, summary strategies and extensions."""
    category_counts: dict[str, int] = {}
    tag_counts: dict[str, int] = {}
    action_counts: dict[str, int] = {}
    summary_counts: dict[str, int] = {}
    extension_counts: dict[str, int] = {}
    for item in files:
        for category in item.get("categories", []):
            category_counts[category] = category_counts.get(category, 0) + 1
        for tag in item.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        action = str(item.get("action") or "")
        if action:
            action_counts[action] = action_counts.get(action, 0) + 1
        strategy = str(item.get("summary") or "")
        if strategy:
            summary_counts[strategy] = summary_counts.get(strategy, 0) + 1
        ext = str(item.get("extension") or "")
        if ext:
            extension_counts[ext] = extension_counts.get(ext, 0) + 1
    return {
        "categories": category_counts,
        "tags": tag_counts,
        "actions": action_counts,
        "summaries": summary_counts,
        "extensions": extension_counts,
    }


# ---------------------------------------------------------------------------
# Redundancy: generated exports and repeated package bytes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Redundancy:
    """Paths that must not be imported, mapped to the file that explains why."""

    duplicates: Mapping[str, str] = field(default_factory=dict)
    redundant: Mapping[str, str] = field(default_factory=dict)
    possible: Mapping[str, str] = field(default_factory=dict)


def resolve_redundancy(root: Optional[Path], paths: Sequence[str]) -> Redundancy:
    """Find exports with a generated source and packages that repeat bytes.

    ``root`` joins a project-relative path to the file on disk; without it only
    the path-only rules run, which is what the unit tests use.
    """
    normalized = [Path(path).as_posix() for path in paths]
    by_name: Dict[Tuple[str, str], str] = {}
    models: Dict[str, str] = {}
    for path in normalized:
        # Same folder, same stem, different suffix: that is exactly a generated
        # export next to its source, so the suffix stays part of the key.
        by_name[(posixpath.dirname(path), Path(path).name.casefold())] = path
        if Path(path).suffix.lower() in {".slx", ".mdl"}:
            models.setdefault(Path(path).stem, path)

    redundant: Dict[str, str] = {}
    possible: Dict[str, str] = {}
    for path in normalized:
        name = Path(path)
        ext = name.suffix.lower()
        folder = posixpath.dirname(path)
        if ext in DUPLICATE_CONTAINER_EXTS:
            model = models.get(name.stem)
            if model is not None:
                redundant[path] = model
                continue
        source = _sibling(by_name, folder, name.stem, EXPORT_SOURCES.get(ext, ()))
        if source is not None:
            redundant[path] = source
            continue
        hint = _sibling(by_name, folder, name.stem, POSSIBLE_EXPORT_SOURCES.get(ext, ()))
        if hint is not None:
            possible[path] = hint

    duplicates: Dict[str, str] = {}
    if root is not None:
        groups: Dict[str, List[str]] = {}
        for path in normalized:
            if path in redundant or Path(path).suffix.lower() not in DUPLICATE_CONTAINER_EXTS:
                continue
            digest = _file_digest(Path(root) / path)
            if digest is not None:
                groups.setdefault(digest, []).append(path)
        for group in groups.values():
            if len(group) < 2:
                continue
            keeper = sorted(group, key=lambda item: (_in_package_dir(item), item))[0]
            for path in group:
                if path != keeper:
                    duplicates[path] = keeper

    return Redundancy(duplicates=duplicates, redundant=redundant, possible=possible)


def _sibling(
    by_name: Mapping[Tuple[str, str], str],
    folder: str,
    stem: str,
    exts: Sequence[str],
) -> Optional[str]:
    """The file next to *folder*/*stem* with one of *exts*, if there is one."""
    for ext in exts:
        path = by_name.get((folder, (stem + ext).casefold()))
        if path is not None:
            return path
    return None


def _in_package_dir(rel_path: str) -> bool:
    """A copy under a package folder is the published one, not the source."""
    folders = {"packages", "package", "release"}
    return any(part.casefold() in folders for part in Path(rel_path).parts[:-1])


def _file_digest(path: Path) -> Optional[str]:
    try:
        if path.stat().st_size > DUPLICATE_HASH_MAX_BYTES:
            return None
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in _chunks(handle):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError:
        return None


def _chunks(handle, size: int = 1024 * 1024) -> Iterator[bytes]:
    while True:
        chunk = handle.read(size)
        if not chunk:
            return
        yield chunk


# ---------------------------------------------------------------------------
# Aggregation table: one project → .prj → resources files and their category
# ---------------------------------------------------------------------------


def resource_metadata(path: Path) -> dict[str, str]:
    """Category and target of one ``resources/project`` XML, when it carries them.

    MATLAB writes one ``…d.xml`` per tracked file with a ``FileClassCategory``
    label and one ``…p.xml`` with the file's ``location``; most entries are an
    empty ``<Info/>`` shell. Both keys are optional, and reading never fails the
    import.
    """
    try:
        text = Path(path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}
    metadata: Dict[str, str] = {}
    category = _RESOURCE_CATEGORY.search(text)
    if category:
        metadata["category"] = category.group(1)
    target = _RESOURCE_LOCATION.search(text)
    if target:
        metadata["target"] = target.group(1)
    return metadata


def project_table(entries: Iterable[tuple[str, Path]]) -> List[dict]:
    """Build the aggregation table for all ``.prj`` and ``resources/project`` files.

    Each project keeps its ``.prj``, the number and size of its resources files,
    the category histogram and one ``path``/``category``/``target`` row per file,
    so nothing is lost when those files stay out of the resource tree.
    """
    projects: Dict[str, dict] = {}
    for rel_path, abs_path in entries:
        posix = Path(rel_path).as_posix()
        suffix = Path(posix).suffix.lower()
        if suffix == ".prj":
            project = _project_entry(projects, posixpath.dirname(posix) or ".")
            project["prj"] = posix
            continue
        parts = Path(posix).parts
        index = project_resources_index(parts)
        if index is None:
            continue
        project = _project_entry(projects, "/".join(parts[:index]) or ".")
        metadata = resource_metadata(abs_path)
        row: Dict[str, str] = {"path": posix}
        if metadata.get("category"):
            row["category"] = metadata["category"]
            categories = project["categories"]
            categories[metadata["category"]] = categories.get(metadata["category"], 0) + 1
        if metadata.get("target"):
            row["target"] = metadata["target"]
        project["files"].append(row)
        project["resources"] += 1
        try:
            project["bytes"] += Path(abs_path).stat().st_size
        except OSError:
            pass

    table = []
    for root in sorted(projects):
        project = projects[root]
        project["files"].sort(key=lambda row: row["path"])
        project["categories"] = dict(sorted(project["categories"].items()))
        _pair_resources_targets(project["files"])
        table.append(project)
    return table


def _pair_resources_targets(rows: List[dict]) -> None:
    """Copy the ``location`` of ``…p.xml`` onto the ``…d.xml`` that carries the category.

    MATLAB splits one tracked file into a category file and a target file with
    the same prefix; only the pair says what the file was and where it belonged.
    """
    by_path = {row["path"]: row for row in rows}
    for row in rows:
        name = posixpath.basename(row["path"])
        if not name.endswith("d.xml") or row.get("target"):
            continue
        sibling = posixpath.join(posixpath.dirname(row["path"]), name[:-5] + "p.xml")
        target = by_path.get(sibling, {}).get("target")
        if target:
            row["target"] = target


def _project_entry(projects: Dict[str, dict], root: str) -> dict:
    project = projects.get(root)
    if project is None:
        project = {
            "root": root,
            "prj": "",
            "resources": 0,
            "bytes": 0,
            "categories": {},
            "files": [],
        }
        projects[root] = project
    return project
