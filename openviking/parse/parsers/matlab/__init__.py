# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Deterministic parsers for MATLAB and Simulink project files.

A MATLAB import is opt-in: the caller passes ``args.matlab=true`` with the
resource (``ov add-resource ./project --args matlab:true``). Nothing else turns
it on, and no extension selects it by itself.
"""

from typing import Any

from openviking.parse.parsers.matlab.parser import MatlabParser

# Key of the ``args`` entry that declares a resource a MATLAB/Simulink import.
MATLAB_ARG = "matlab"

_TRUE_WORDS = frozenset({"true", "1", "yes", "on"})


def matlab_requested(value: Any) -> bool:
    """Whether an ``args.matlab`` value asks for the MATLAB pipeline.

    Clients send a JSON boolean, but a string form reaches the same code through
    the CLI and the SDK, so ``"false"`` must not read as true.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().casefold() in _TRUE_WORDS
    if isinstance(value, (int, float)):
        return value == 1
    return False


__all__ = ["MATLAB_ARG", "MatlabParser", "matlab_requested"]
