---
type: simulink-block
title: 'Assertion'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'assertion'
documentation_source_path: 'slref/assertion.html'
language: en
---

# Assertion

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal to the assertion check.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## Parameters
```yaml
parameters:
- name: Enable assertion
  summary: Enable or disable check on (default) | off
  group: ''
  block_parameter: enabled
  type: string scalar or character vector
  values: '"on" | "off"'
  default: '"on"'
- name: Simulation callback when assertion fails
  summary: Expression to evaluate when assertion fails "" (default) | MATLAB expression
  group: ''
  block_parameter: AssertionFailFcn
  type: string scalar or character vector
  default: ''''''
- name: Stop simulation when assertion fails
  summary: Whether to stop simulation when check fails on (default) | off
  group: ''
  block_parameter: stopWhenAssertionFail
  type: string scalar or character vector
  values: '"on" | "off"'
  default: '"on"'
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: ''
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
```

### **Enable assertion** — Enable or disable check `on` (default) | `off`

Clearing this parameter disables the block and causes the model to behave as if the
block does not exist. To enable or disable all verification blocks, regardless of the
setting of this option, go to the Configuration Parameters window, click **Diagnostics** > **Data Validity**, expand the **Advanced parameters** section, and set
**Model Verification block enabling** to `Enable
all` or `Disable all`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `enabled` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

### **Simulation callback when assertion fails** — Expression to evaluate when assertion fails `""` (default) | MATLAB expression

Specify a MATLAB® expression to evaluate when the assertion fails. Because the
expression is evaluated in the MATLAB workspace, define all variables used in the expression in that
workspace.

#### Dependencies

To enable this parameter, select **Enable
assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `AssertionFailFcn` |
| **Type:** string scalar or character vector |
| **Default:** `''` |

### **Stop simulation when assertion fails** — Whether to stop simulation when check fails `on` (default) | `off`

Select this parameter to stop the simulation when the check fails. Clear this
parameter to display a warning and continue the simulation.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |
## Libraries

Simulink / Model Verification HDL Coder / Model Verification

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

For information about how Simulink®
Coder™ generated code handles Model Verification blocks, see Configure Model for Debugging (Simulink Coder).

Not recommended for production code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Check whether signal is zero

The Assertion block checks whether any of the elements of the input
signal are `0`. If all of the elements are nonzero, the assertion is
`true (1)` and the block does nothing. If not, the block halts the
simulation and returns an error message by default.
