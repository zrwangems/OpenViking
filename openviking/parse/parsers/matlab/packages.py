# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Metadata for MATLAB packages, FMUs and Simulink project templates."""

from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Any

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _texts(root, name: str) -> list[str]:
    return [
        (element.text or "").strip()
        for element in root.iter()
        if _local(element.tag) == name and (element.text or "").strip()
    ]


def _first(root, name: str) -> str:
    values = _texts(root, name)
    return values[0] if values else ""


def _read(archive: zipfile.ZipFile, name: str):
    if name not in archive.namelist():
        return None
    try:
        return ET.fromstring(read_xml_member(archive, name))
    except (ET.ParseError, ValueError):
        return None


def _core_metadata(archive: zipfile.ZipFile) -> dict[str, str]:
    core = _read(archive, "metadata/coreProperties.xml")
    props = _read(archive, "metadata/mwcoreProperties.xml")
    release_info = _read(archive, "metadata/mwcorePropertiesReleaseInfo.xml")
    result: dict[str, str] = {}
    if core is not None:
        for key, tag in (
            ("title", "title"),
            ("creator", "creator"),
            ("description", "description"),
            ("created", "created"),
            ("modified", "modified"),
            ("category", "category"),
            ("version", "version"),
        ):
            value = _first(core, tag)
            if value:
                result[key] = value
    if props is not None:
        result["release"] = _first(props, "matlabRelease")
        result["content_type"] = _first(props, "contentType")
        result["content_type_name"] = _first(props, "contentTypeFriendlyName")
    if release_info is not None:
        result["release_version"] = _first(release_info, "version")
        result["release_description"] = _first(release_info, "description")
    return result


def _file_entries(archive: zipfile.ZipFile) -> list[dict[str, str]]:
    root = _read(archive, "metadata/filesystemManifest.xml")
    if root is None:
        return []
    entries = []
    for element in root.iter():
        if _local(element.tag) not in {"fileEntry", "entry"}:
            continue
        attrs = dict(element.attrib)
        entries.append(
            {
                "name": attrs.get("name") or _first(element, "path"),
                "source": attrs.get("content", ""),
                "type": attrs.get("type", ""),
                "date": attrs.get("date", ""),
            }
        )
    return entries


def _addon(archive: zipfile.ZipFile) -> dict[str, Any]:
    addon = _read(archive, "metadata/addonProperties.xml")
    config = _read(archive, "metadata/configuration.xml")
    result: dict[str, Any] = {}
    if addon is not None:
        for element in addon.iter():
            if _local(element.tag) == "identifier":
                result["identifier"] = (element.text or "").strip()
                result["identifier_type"] = element.get("type", "")
        description = _first(addon, "description")
        if description:
            result["description"] = description
    if config is not None:
        apps = []
        for element in config.iter():
            if _local(element.tag) != "app":
                continue
            apps.append(
                {
                    "name": _first(element, "name"),
                    "file": _first(element, "file"),
                }
            )
        if apps:
            result["apps"] = apps
        paths = _texts(config, "matlabPath")
        if paths:
            result["matlab_paths"] = paths
    return result


def _support_package(archive: zipfile.ZipFile) -> dict[str, Any]:
    root = _read(archive, "metadata/supportPackageInfo.xml")
    if root is None:
        return {}
    third_party = [
        {
            "component": _first(element, "component"),
            "license": _first(element, "license"),
        }
        for element in root.iter()
        if _local(element.tag) == "thirdParty"
    ]
    return {
        "name": _first(root, "name"),
        "version": _first(root, "version"),
        "vendor": _first(root, "vendor"),
        "hardware": _first(root, "hardware"),
        "third_party": third_party,
    }


def _system_requirements(archive: zipfile.ZipFile) -> dict[str, Any]:
    root = _read(archive, "metadata/systemRequirements.xml")
    if root is None:
        return {}
    result: dict[str, Any] = {}
    for element in root.iter():
        tag = _local(element.tag)
        if tag == "releaseCompatibility":
            result["release_compatibility"] = dict(element.attrib)
        elif tag == "platformCompatibility":
            result["platform_compatibility"] = dict(element.attrib)
        elif tag in {"dependency", "requiredProduct", "product"}:
            name = element.get("name") or (element.text or "").strip()
            if name:
                result.setdefault("dependencies", []).append(name)
    return result


def _template_properties(archive: zipfile.ZipFile) -> dict[str, Any]:
    root = _read(archive, "metadata/templateProperties.xml")
    if root is None:
        return {}
    return {
        "group": _first(root, "group"),
        "builtin": _first(root, "builtin"),
        "display_order": _first(root, "displayOrder"),
        "message_catalog": _first(root, "messageCatalogRoot"),
        "licenses": _texts(root, "license"),
    }


def _project_metadata(archive: zipfile.ZipFile) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name in archive.namelist():
        if not name.startswith("metadata/") or not name.endswith("projectProperties.xml"):
            continue
        root = _read(archive, name)
        if root is None:
            continue
        entry_points = []
        for element in root.iter():
            if _local(element.tag) != "EntryPoint":
                continue
            info = next(
                (child for child in list(element) if _local(child.tag) == "Info"),
                None,
            )
            if info is not None:
                entry_points.append(
                    {
                        "name": info.get("Name", ""),
                        "file": info.get("File", ""),
                        "group": info.get("GroupUUID", ""),
                    }
                )
        if entry_points:
            result["entry_points"] = entry_points
    return result


def _startup_files(members: list[dict[str, Any]]) -> list[str]:
    return [
        member["name"]
        for member in members
        if member["name"].rsplit("/", 1)[-1].casefold()
        in {"projectstartup.m", "startup.m", "install.m"}
    ]


def package_metadata(path: str | Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Add package-specific metadata to a generic ZIP member manifest."""
    path = Path(path)
    suffix = path.suffix.lower()
    with zipfile.ZipFile(path) as archive:
        metadata = _core_metadata(archive)
        if suffix in {".mlproj", ".sltx"}:
            metadata.update(_project_metadata(archive))
            metadata.update({"startup": _startup_files(manifest.get("members", []))})
        if suffix == ".sltx":
            metadata["template"] = _template_properties(archive)
        if suffix in {".mltbx", ".mlappinstall", ".mlpkginstall"}:
            metadata.update(_addon(archive))
        if suffix == ".mltbx":
            metadata.update(_system_requirements(archive))
        if suffix == ".mlpkginstall":
            metadata.update(_support_package(archive))
        metadata["files"] = _file_entries(archive)
    manifest["metadata"] = metadata
    if suffix == ".mlproj":
        manifest["project"] = metadata
    elif suffix == ".mltbx":
        manifest["toolbox"] = metadata
    elif suffix == ".mlappinstall":
        manifest["app"] = metadata
    elif suffix == ".sltx":
        manifest["template"] = metadata.get("template", {})
        manifest["template"]["name"] = metadata.get("title") or path.stem
        manifest["template"]["version"] = metadata.get("version", "") or metadata.get(
            "release_version", ""
        )
        manifest["template"]["required_products"] = manifest["template"].get("licenses", [])
        manifest["template"]["files"] = [
            member["name"]
            for member in manifest.get("members", [])
            if member["name"].startswith("fsroot/")
        ]
    elif suffix == ".mlpkginstall":
        manifest["support_package"] = metadata
    return manifest


def jar_metadata(path: str | Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Read a JAR manifest and list classes/resources without decompiling."""
    path = Path(path)
    manifest_mf: dict[str, str] = {}
    classes: list[str] = []
    resources: list[str] = []
    with zipfile.ZipFile(path) as archive:
        if "META-INF/MANIFEST.MF" in archive.namelist():
            text = archive.read("META-INF/MANIFEST.MF").decode("utf-8", errors="replace")
            current = ""
            for line in text.splitlines():
                if line.startswith(" ") and current:
                    manifest_mf[current] += line[1:]
                    continue
                key, separator, value = line.partition(": ")
                if separator:
                    current = key.strip()
                    manifest_mf[current] = value.strip()
        for name in archive.namelist():
            if name.endswith(".class"):
                classes.append(name)
            elif not name.endswith((".class", ".SF", ".DSA", ".RSA")):
                resources.append(name)
    manifest["java_manifest"] = manifest_mf
    manifest["classes"] = classes
    manifest["resources"] = resources
    return manifest


def fmu_metadata(path: str | Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Parse the FMI modelDescription and attach model, capabilities and variables."""
    path = Path(path)
    with zipfile.ZipFile(path) as archive:
        if "modelDescription.xml" not in archive.namelist():
            manifest["model"] = None
            manifest["variables"] = []
            return manifest
        root = ET.fromstring(read_xml_member(archive, "modelDescription.xml"))
    model = {
        "fmi_version": root.get("fmiVersion", ""),
        "name": root.get("modelName", ""),
        "guid": root.get("guid", ""),
        "generation_tool": root.get("generationTool", ""),
        "generation_time": root.get("generationDateAndTime", ""),
        "version": root.get("version", ""),
        "capabilities": {},
        "default_experiment": {},
        "units": [],
        "variables": [],
    }
    for element in root.iter():
        tag = _local(element.tag)
        if tag in {"CoSimulation", "ModelExchange", "ScheduledExecution"}:
            model["capabilities"][tag] = dict(element.attrib)
        elif tag == "DefaultExperiment":
            model["default_experiment"] = dict(element.attrib)
        elif tag == "Unit":
            name = element.get("name", "")
            if name and name not in model["units"]:
                model["units"].append(name)
        elif tag == "ScalarVariable":
            kind = next(
                (
                    _local(child.tag)
                    for child in list(element)
                    if _local(child.tag) in {"Real", "Integer", "Boolean", "String", "Enumeration"}
                ),
                "",
            )
            typed = next((child for child in list(element) if _local(child.tag) == kind), None)
            model["variables"].append(
                {
                    "name": element.get("name", ""),
                    "value_reference": element.get("valueReference", ""),
                    "causality": element.get("causality", ""),
                    "variability": element.get("variability", ""),
                    "description": element.get("description", ""),
                    "type": kind,
                    "start": typed.get("start", "") if typed is not None else "",
                    "unit": typed.get("unit", "") if typed is not None else "",
                }
            )
    manifest["model"] = model
    manifest["variables"] = model["variables"]
    manifest["modelDescription"] = "modelDescription.xml"
    manifest["capabilities"] = model["capabilities"]
    return manifest
