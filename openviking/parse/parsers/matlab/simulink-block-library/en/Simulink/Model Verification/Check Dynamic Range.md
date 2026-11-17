---
type: simulink-block
title: 'Check Dynamic Range'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkdynamicrange'
documentation_source_path: 'slref/checkdynamicrange.html'
language: en
---

# Check Dynamic Range

## Ports
```yaml
ports:
- name: max
  summary: Upper bound of dynamic range check scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: min
  summary: Lower bound of dynamic range check scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: u
  summary: Input signal checked against range scalar | vector | matrix
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: Port_1
  summary: Assertion output signal scalar
  direction: output
  data_types: double | Boolean
```

### Input

### **max** — Upper bound of dynamic range check scalar | vector | matrix

Signal specifying the upper bound of the range.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **min** — Lower bound of dynamic range check scalar | vector | matrix

Signal specifying the lower bound of the range.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — Input signal checked against range scalar | vector | matrix

Signal checked against the range specified by the
**max** and **min** ports.

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

To enable this port, select the **Output assertion signal**
parameter.

**Data Types:** `double` | `Boolean`
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

Check that signal falls inside range of amplitudes that varies from time step to time step

The Check Dynamic Range block checks that a signal falls inside a range of
values at each time step and executes an assertion after comparison. The width of the
range can vary from time step to time step. The **u** port is the
tested input signal. The **min** and **max** ports are
the lower and upper bounds of the range, respectively, where both
**min** and **max** are exclusive. If
**u** is between **max** and
**min**, the assertion is `true (1)` and the block
does nothing. If not, the block halts the simulation and returns an error message by
default.

The input signals can be scalars, vectors, or matrices. All three input signals must
be the same data type. The block compares the value of **u** to the
bounds differently depending on the signal.

- When comparing scalars to vectors or matrices, the block compares the
  scalar signal to each element of the non-scalar signal.
- When comparing vectors or matrix signals to other vectors or matrices, the
  block checks the inputs element-by-element.
- For models with more than one vector or matrix input signal, the vectors
  or matrices must have the same dimensions.
