# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Deterministic parsers for MATLAB and Simulink project files.

A MATLAB import is opt-in: the caller passes ``args.matlab=true`` with the
resource (``ov add-resource ./project --args matlab:true``). Nothing else turns
it on, and no extension selects it by itself.
"""

from openviking.parse.parsers.matlab.parser import MatlabParser

# Key of the ``args`` entry that declares a resource a MATLAB/Simulink import.
MATLAB_ARG = "matlab"

__all__ = ["MATLAB_ARG", "MatlabParser"]
