---
type: simulink-block
title: 'Check Static Lower Bound'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkstaticlowerbound'
documentation_source_path: '../simulink/slref/checkstaticlowerbound.html'
language: en
---

# Check Static Lower Bound

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal checked against bound scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: Port_1
  summary: Assertion output signal scalar
  direction: output
  data_types: double | Boolean
```

### Input

### **Port\_1** — Input signal checked against bound scalar | vector | matrix

Input signal checked against the lower bound specified by the
**Lower bound** parameter.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Assertion output signal scalar

Output signal that is `true (1)` if the assertion
succeeds and `false (0)` if the assertion fails. If, in
the Configuration Parameters window, in the **Math and Data
Types** section, under **Advanced
parameters**, you select **Implement logic signals
as Boolean data**, then the output data type is
`Boolean`. Otherwise, the data type of the signal
is `double`.

#### Dependencies

To enable this output port, select the **Output assertion signal**
parameter check box.

**Data Types:** `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Lower bound
  summary: Lower boundary value scalar | vector | matrix
  group: ''
  block_parameter: min
  type: string scalar or character vector
  default: '"0"'
- name: Inclusive boundary
  summary: Include the lower bound in range on (default) | off
  group: ''
  block_parameter: min_included
  type: string scalar character vector
  values: '"on" | "off"'
  default: '"on"'
- name: Enable assertion
  summary: Enable or disable check on (default) | off
  group: ''
  block_parameter: enabled
  type: string scalar or character vector
  values: '"on" | "off"'
  default: '"on"'
- name: Simulation callback when assertion fails (optional)
  summary: Expression to evaluate when assertion fails "" (default) | MATLAB expression
  group: ''
  block_parameter: callback
  type: string scalar or character vector
  default: '""'
- name: Stop simulation when assertion fails
  summary: Whether to stop simulation when check fails on (default) | off
  group: ''
  block_parameter: stopWhenAssertionFail
  type: string scalar or character vector
  values: '"on" | "off"'
  default: '"on"'
- name: Output assertion signal
  summary: Create output signal off (default) | on
  group: ''
  block_parameter: export
  type: string scalar or character vector
  values: '"on" | "off"'
  default: '"off"'
- name: Select icon type
  summary: Select icon type graphic (default) | text
  group: ''
  block_parameter: icon
  type: string scalar or character vector
  values: '"graphic" | "text"'
  default: '"graphic"'
```

### **Lower bound** — Lower boundary value scalar | vector | matrix

Specify the lower bound on the range of amplitudes that the input signal
can have.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `min` |
| **Type:** string scalar or character vector |
| **Default:** `"0"` |

### **Inclusive boundary** — Include the lower bound in range `on` (default) | `off`

Select this check box to make the range of valid input amplitudes include
the lower bound.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `min_included` |
| **Type:** string scalar character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"on"` |

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

### **Simulation callback when assertion fails (optional)** — Expression to evaluate when assertion fails `""` (default) | MATLAB expression

Specify a MATLAB® expression to evaluate when the assertion fails. Because the expression is
evaluated in the MATLAB workspace, define all variables used in the expression in that
workspace.

#### Dependencies

To enable this parameter, select **Enable assertion**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `callback` |
| **Type:** string scalar or character vector |
| **Default:** `""` |

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

### **Output assertion signal** — Create output signal `off` (default) | `on`

Select this parameter to enable the output port.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `export` |
| **Type:** string scalar or character vector |
| **Values:** `"on"` | `"off"` |
| **Default:** `"off"` |

### **Select icon type** — Select icon type `graphic` (default) | `text`

Specify the style of the block icon. The `graphic` option displays a
graphical representation of the assertion condition on the icon. The
`text` option displays a mathematical expression that represents
the assertion condition.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `icon` |
| **Type:** string scalar or character vector |
| **Values:** `"graphic"` | `"text"` |
| **Default:** `"graphic"` |
## Libraries

Simulink / Model Verification HDL Coder / Model Verification

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
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

Check that signal is greater than (or optionally equal to) static lower bound

The Check Static Lower Bound block checks if an input signal is greater than
(or optionally equal to) a specified lower bound at each time step and executes an
assertion after comparison. The **Lower bound** parameter defines the
lower bound. If the input signal is greater than the lower bound, the assertion is
`true (1)` and the block does nothing. If not, the block halts the
simulation and returns an error message by default.

The input signal and bound can be scalars, vectors, or matrices. The input and the
bound must be the same data type. The block compares the value of the input to the bound
differently depending on the signal.

- When comparing scalars to vectors or matrices, the block compares the
  scalar to each element of the non-scalar input signal or bound.
- When comparing a vector or matrix input signal to a vector or matrix
  bound, the block compares the input signal to the bound
  element-by-element.
- For models with an input signal and bound that are both vectors or
  matrices, the input signal and bound must have the same dimensions.
