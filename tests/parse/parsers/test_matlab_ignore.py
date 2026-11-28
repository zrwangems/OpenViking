# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Tests for skipping MATLAB/Simulink build and cache artifacts on import."""

from pathlib import Path

import pytest

from openviking.parse.directory_scan import scan_directory
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab.ignore import (
    detect_build_folders,
    matlab_ignore_for,
    project_resources_index,
)

SAMPLE = Path(__file__).parents[2] / "matlab_repos" / "matlab-ingest-fixture"

DEFAULT_SCRIPT = """
cfg = Simulink.fileGenControl('getConfig');
work_dir = pwd;
cfg.CacheFolder = fullfile(work_dir,'Simulation cache folder');
cfg.CodeGenFolder  = fullfile(work_dir,'Simulation cache folder');
Simulink.fileGenControl('setConfig', 'config', cfg);
"""


def make_matlab_project(root: Path, script: str = DEFAULT_SCRIPT) -> Path:
    (root / "Plant.slx").write_bytes(b"PK\x03\x04")
    (root / "Plant.sldd").write_bytes(b"PK\x03\x04")
    (root / "run.m").write_text(script, encoding="utf-8")
    (root / "src").mkdir()
    (root / "src" / "controller.m").write_text("x = 1;", encoding="utf-8")
    return root


def write(root: Path, relative: str, content: str = "x = 1;") -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_detects_custom_cache_folder_from_file_gen_control():
    assert detect_build_folders(SAMPLE) == (("build",), ("cache",))
    rules = matlab_ignore_for(SAMPLE)
    assert rules is not None
    assert rules.is_build_dir(SAMPLE / "build")
    assert rules.is_build_dir(SAMPLE / "cache")
    assert rules.is_build_dir(SAMPLE / "model" / "build")
    assert not rules.is_build_dir(SAMPLE / "model" / "VirtualVehicle")


def test_detects_direct_set_config_arguments(tmp_path: Path):
    write(
        tmp_path,
        "setup.m",
        "Simulink.fileGenControl('setConfig','CacheFolder',fullfile(pwd,'ov cache'),"
        "'CodeGenFolder','D:\\Build\\gen code');\n",
    )
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    assert detect_build_folders(tmp_path) == (("ov cache",), ("gen code",))


def test_ignores_absolute_folder_paths_by_last_component(tmp_path: Path):
    write(
        tmp_path,
        "setup.m",
        "Simulink.fileGenControl('setConfig','CacheFolder',"
        "'D:\\Projects\\EMS\\reevsim\\reevmdl_0\\architecture\\architecture\\"
        "Simulation cache folder');\n",
    )
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    assert detect_build_folders(tmp_path) == (("simulation cache folder",),)


def test_unapplied_and_commented_settings_are_ignored(tmp_path: Path):
    write(
        tmp_path,
        "notes.m",
        "% Simulink.fileGenControl('setConfig','CacheFolder','commented out');\n"
        "cfg = Simulink.fileGenControl('getConfig');\n"
        "cfg.CacheFolder = fullfile(pwd,'never applied');\n",
    )
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    assert detect_build_folders(tmp_path) == ()


def test_unresolvable_setting_falls_back_to_defaults(tmp_path: Path):
    write(
        tmp_path,
        "setup.m",
        "cfg = Simulink.fileGenControl('getConfig');\n"
        "cfg.CodeGenFolder = getenv('OV_CODEGEN_FOLDER');\n"
        "Simulink.fileGenControl('setConfig','config',cfg);\n",
    )
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    assert detect_build_folders(tmp_path) == ()
    rules = matlab_ignore_for(tmp_path)
    assert rules is not None
    assert rules.is_build_dir(tmp_path / "slprj")
    assert rules.is_build_dir(tmp_path / "Plant_ert_rtw")


def test_reset_drops_previous_folders(tmp_path: Path):
    write(
        tmp_path,
        "setup.m",
        "Simulink.fileGenControl('setConfig','CacheFolder',fullfile(pwd,'cache one'));\n"
        "Simulink.fileGenControl('reset');\n",
    )
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    assert detect_build_folders(tmp_path) == ()


def test_declaring_matlab_is_what_turns_the_rules_on(tmp_path: Path):
    """Nothing inspects the tree: the flag decides, not the files in it."""
    write(tmp_path, "main.m")
    write(tmp_path, "notes.mat", "data")
    write(tmp_path, "slprj/ert/Plant/Plant.c")

    ordinary = scan_directory(tmp_path)
    declared = scan_directory(tmp_path, matlab_project=True)

    assert "slprj/ert/Plant/Plant.c" in [entry.rel_path for entry in ordinary.processable]
    assert [entry.rel_path for entry in declared.processable] == ["main.m", "notes.mat"]
    assert ordinary.matlab_project is False
    assert declared.matlab_project is True


def test_scan_skips_build_cache_and_custom_folders(tmp_path: Path):
    make_matlab_project(tmp_path)
    write(tmp_path, "slprj/ert/Plant/Plant.c")
    write(tmp_path, "slprj/ert/Plant/Plant.obj")
    write(tmp_path, "Plant_ert_rtw/Plant.c")
    write(tmp_path, "Plant_ert_rtw/Plant.h")
    write(tmp_path, "Plant_ert_rtw/html/report.html")
    write(tmp_path, "Simulation cache folder/slprj/ert/Plant/Plant.c")
    write(tmp_path, "Simulation cache folder/cache.slxc")
    (tmp_path / "Plant.slxc").write_bytes(b"PK\x03\x04")
    write(tmp_path, "Plant.slx.autosave")
    write(tmp_path, "old_script.asv")

    result = scan_directory(tmp_path, strict=True, matlab_project=True)

    assert [entry.rel_path for entry in result.processable] == [
        "Plant.sldd",
        "Plant.slx",
        "run.m",
        "src/controller.m",
    ]
    assert result.unsupported == []
    assert result.warnings == []
    assert {
        "slprj/ert/Plant/Plant.c",
        "slprj/ert/Plant/Plant.obj",
        "Plant_ert_rtw/Plant.c",
        "Plant_ert_rtw/Plant.h",
        "Plant_ert_rtw/html/report.html",
        "Simulation cache folder/slprj/ert/Plant/Plant.c",
        "Simulation cache folder/cache.slxc",
        "Plant.slxc",
        "Plant.slx.autosave",
        "old_script.asv",
    } == {entry_path.split(" (")[0] for entry_path in result.skipped}
    assert all("matlab build/cache" in entry for entry in result.skipped)


def test_undeclared_directory_keeps_generated_folders(tmp_path: Path):
    """Without the declaration a Simulink-shaped tree is an ordinary directory."""
    write(tmp_path, "README.md", "# project")
    write(tmp_path, "codegen/app.py", "print(1)")
    write(tmp_path, "driver_rtw/notes.md", "notes")

    result = scan_directory(tmp_path)

    assert [entry.rel_path for entry in result.processable] == [
        "README.md",
        "codegen/app.py",
        "driver_rtw/notes.md",
    ]
    assert result.skipped == []
    assert result.matlab_project is False


def test_undeclared_cache_names_are_not_skipped_at_any_depth(tmp_path: Path):
    write(tmp_path, "docs/readme.md", "# project")
    write(tmp_path, "a/b/c/slprj/ert/Plant/Plant.c")
    write(tmp_path, "a/b/c/Plant_ert_rtw/Plant.h")
    (tmp_path / "a/b/c/model.slxc").write_bytes(b"cache")

    result = scan_directory(tmp_path)

    assert [entry.rel_path for entry in result.processable] == [
        "a/b/c/Plant_ert_rtw/Plant.h",
        "a/b/c/slprj/ert/Plant/Plant.c",
        "docs/readme.md",
    ]
    # The cache file is just an unknown binary here, not a derived artifact.
    assert [entry.rel_path for entry in result.unsupported] == ["a/b/c/model.slxc"]
    assert result.skipped == []


def test_codegen_and_custom_folders_at_any_depth_in_matlab_project(tmp_path: Path):
    (tmp_path / "Plant.slx").write_bytes(b"PK\x03\x04")
    write(
        tmp_path,
        "scripts/setup.m",
        "cfg = Simulink.fileGenControl('getConfig');\n"
        "cfg.CacheFolder = fullfile(pwd,'build','cache');\n"
        "Simulink.fileGenControl('setConfig','config',cfg);\n",
    )
    write(tmp_path, "deep/a/codegen/lib/Plant/Plant.c")
    write(tmp_path, "deep/a/build/cache/slprj/ert/Plant/Plant.c")
    write(tmp_path, "deep/a/other/build/cache/model.slxc")

    result = scan_directory(tmp_path, strict=True, matlab_project=True)

    assert [entry.rel_path for entry in result.processable] == [
        "Plant.slx",
        "scripts/setup.m",
    ]
    skipped = {entry.split(" (")[0] for entry in result.skipped}
    assert skipped == {
        "deep/a/codegen/lib/Plant/Plant.c",
        "deep/a/build/cache/slprj/ert/Plant/Plant.c",
        "deep/a/other/build/cache/model.slxc",
    }


def test_scan_keeps_unrelated_folder_with_similar_name(tmp_path: Path):
    make_matlab_project(tmp_path)
    write(tmp_path, "DriveCycle/data.csv", "a,b\n1,2\n")
    write(tmp_path, "Results/summary.md", "# result")

    result = scan_directory(tmp_path, matlab_project=True)

    assert "DriveCycle/data.csv" in [entry.rel_path for entry in result.processable]
    assert "Results/summary.md" in [entry.rel_path for entry in result.processable]


def test_whole_sample_project_still_imports_every_source_file(tmp_path: Path):
    result = scan_directory(SAMPLE, strict=True, matlab_project=True)

    processable = [entry.rel_path for entry in result.processable]
    duplicates = [entry.rel_path for entry in result.duplicates]
    # 3425 files: 1146 imported, 74 build/cache skipped (the 73 from before the
    # editor-backup rule plus the .asv), 2204 project state in the aggregation
    # table (2191 resources + 13 .prj) and 1 repeated .fmu.
    assert len(processable) == 1146
    assert len(result.skipped_details) == 74
    assert len(result.aggregated) == 2204
    assert duplicates == ["packages/VvcFmuEngExl.fmu"]
    assert (
        len(processable) + len(result.skipped_details) + len(result.aggregated) + len(duplicates)
        == 3425
    )
    assert not result.unsupported
    assert "src/autoblkscheckparams.p" in processable
    assert "src/detectChangeOrbitalElements.m" in processable
    assert "bin/AddOnInstaller.exe" in processable
    assert not any(entry.endswith("(IGNORE_DIRS)") for entry in result.skipped)
    assert {entry["reason"] for entry in result.skipped_details} <= {
        "matlab build/cache",
        "matlab derived file",
        "matlab build output",
        "构建模板副本",
    }
    # Project state never enters the resource tree.
    assert "MatlabIngestFixture.prj" not in processable
    outside_state = processable + [entry["path"] for entry in result.skipped_details]
    assert not any("resources/project" in path for path in outside_state)


def test_skipped_reason_is_reported_as_ignore():
    parsed = DirectoryParser._parse_skipped(
        ["Plant_ert_rtw (matlab build/cache)", "Plant.slxc (matlab build/cache)"]
    )

    assert parsed == [
        {
            "path": "Plant_ert_rtw",
            "status": "ignore",
            "reason": "matlab build/cache",
        },
        {
            "path": "Plant.slxc",
            "status": "ignore",
            "reason": "matlab build/cache",
        },
    ]


@pytest.mark.parametrize(
    "folder",
    ["slprj", "sfprj", "codegen", "Plant_ert_rtw", "Plant_grt_rtw", "sim_target_rtw"],
)
def test_default_build_folder_names_are_skipped(tmp_path: Path, folder: str):
    make_matlab_project(tmp_path)
    write(tmp_path, f"{folder}/generated.c")

    result = scan_directory(tmp_path, matlab_project=True)

    assert f"{folder}/generated.c" not in [entry.rel_path for entry in result.processable]
    assert any(entry.startswith(f"{folder}/generated.c ") for entry in result.skipped)


def test_project_resources_state_is_recognised():
    state = ("resources", "project", "hash", "file.xml")
    assert project_resources_index(state) == 0
    assert project_resources_index(("model", "SI") + state) == 2
    assert project_resources_index(("resources", "notes.md")) is None
    assert project_resources_index(("src", "controller.m")) is None
