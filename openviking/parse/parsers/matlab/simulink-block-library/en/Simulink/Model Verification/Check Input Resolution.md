---
type: simulink-block
title: 'Check Input Resolution'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkinputresolution'
documentation_source_path: 'slref/checkinputresolution.html'
language: en
---

# Check Input Resolution

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal checked against resolution scalar | vector
  direction: input
  data_types: double
- name: Port_1
  summary: Assertion output signal scalar
  direction: output
  data_types: double | Boolean
```

### Input

### **Port\_1** — Input signal checked against resolution scalar | vector

Input signal that the block checks against the resolution specified by
the **Resolution** parameter.

**Data Types:** `double`
### Output

### **Port\_1** — Assertion output signal scalar

Output signal that is `true (1)` if the assertion succeeds and
`false (0)` if the assertion fails. If, in the
Configuration Parameters window, in the **Math and Data
Types** section, under **Advanced
parameters**, you select **Implement logic signals
as Boolean data**, then the output data type is
`Boolean`. Otherwise, the data type of the signal
is `double`.

#### Dependencies

To enable this port, select **Output assertion signal**.

**Data Types:** `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Resolution
  summary: Resolution value to compare to input signal scalar | vector
  group: ''
  block_parameter: resolution
  type: string scalar or character vector
  default: '"1"'
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
```

### **Resolution** — Resolution value to compare to input signal scalar | vector

Specify the resolution requirement for the input signal.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `resolution` |
| **Type:** string scalar or character vector |
| **Default:** `"1"` |

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
## Libraries

Simulink / Model Verification HDL Coder / Model Verification

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
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

This block can be used to check whether the input signal has a specified resolution during
simulation, but it is not included in the generated code.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**

## Description

Check that input signal has specified resolution

The Check Input Resolution block checks whether the input signal has a
specified resolution. The block input and resolution can be either a scalar or vector.
The input and resolution must be the same data type.

If the **Resolution** parameter is a scalar, the block calculates the
modulus of the input signal over the provided scalar resolution. The calculated modulus
is then compared to a tolerance of `10e-3`, and executes an assertion
after comparison. If the modulus is less than the tolerance, the assertion is
`true (1)` and the block does nothing. If not, the block halts the
simulation and returns an error message by default. If the
**Resolution** parameter is a vector, it asserts `true
(1)` if the value of the input signal is equal to any of the resolution
vector elements.

The block compares the input to the resolution in several additional ways depending on
the dimensions of the signal and resolution.

- When comparing a scalar input signal or resolution to a vector input
  signal or resolution, the block compares the scalar to each element of the
  vector.
- When comparing a vector input signal to a vector resolution, the block
  compares the input signal to the resolution element-by-element.
- For models with an input signal and resolution that are both vectors, the
  input signal and resolution must have the same dimensions.
