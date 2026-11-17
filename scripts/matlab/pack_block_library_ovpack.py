#!/usr/bin/env python3
"""Package the R2025b block library as a downloadable OpenViking resource."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from openviking.parse.parsers.matlab.library import library_root
from openviking.parse.parsers.matlab.library_pack import DEFAULT_ROOT, build_tree, pack


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path, default=library_root())
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--root-name", default=DEFAULT_ROOT)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="simulink-block-library-") as directory:
        staging = Path(directory)
        built = build_tree(args.library, staging, args.root_name)
        result = pack(staging / args.root_name, args.output, args.root_name)
    result["directories_with_l0_l1"] = built
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
