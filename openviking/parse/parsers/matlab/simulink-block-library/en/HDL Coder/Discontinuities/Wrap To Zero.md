---
type: simulink-block
title: 'Wrap To Zero'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'wraptozero'
documentation_source_path: '../simulink/slref/wraptozero.html'
language: en
---

# Wrap To Zero

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector

Input signal, specified as a scalar or vector. Signal values equal to
or greater than the value of `Threshold` are set to
zero.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal set to the input signal value or zero. The data type of
the output is the same data type as the input.

**Tip**

If the input data type cannot represent zero, parameter overflow
occurs. To detect this overflow, go to the **Diagnostics
> Data Validity** pane of the Configuration
Parameters dialog box and set **Parameters > Detect
overflow** to `warning` or
`error`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Threshold
  summary: Threshold for outputting zero 255 (default) | scalar
  group: ''
  block_parameter: Threshold
  type: character vector
  values: scalar
  default: '''255'''
```

To edit the parameters for the Wrap to Zero block, double-click the
block icon.

### **Threshold** — Threshold for outputting zero `255` (default) | scalar

Threshold value for setting the output value to zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Threshold` |
| **Type**: character vector |
| **Values**: `scalar` |
| **Default**: `'255'` |
## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The input signal and **Threshold** parameter must have equal
size. For example, if the input is a two-dimensional vector,
**Threshold** must also be a two-dimensional vector.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Set output to zero if input is above threshold

The Wrap To Zero block sets the output to zero when the input is above the
**Threshold** value. When the input is less than or equal to the
**Threshold**, then the output is equal to the input.
