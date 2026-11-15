---
type: simulink-block
title: 'Unary Minus'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'unaryminus'
language: en
---

# Unary Minus

## Ports

### Input

### **Port\_1** — Signal to negate scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Port\_1** — Negation of input signal scalar | vector | matrix | N-D array

Negation of the input signal. The output has the same data type and
dimensions as the input.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## Parameters

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Select to have integer overflows saturate. Otherwise, overflows
wrap.

When you select this check box, saturation applies to every internal
operation on the block, not just the output, or result. In general, the code
generation process can detect when overflow is not possible. In this case,
the code generator does not produce saturation code.

For signed-integer data types, the unary minus of the most negative value
is not representable by the data type. In this case, the **Saturate
on integer overflow** check box controls the behavior of the
block:

| Parameter Setting | Block Behavior | Examples |
| --- | --- | --- |
| **Saturate on integer overflow** = `on` | Values saturate to the most positive value of the integer data type | - For 8-bit signed integers, -128 maps to   127. - For 16-bit signed integers, -32768 maps to   32767. - For 32-bit signed integers, -2147483648 maps   to 2147483647. |
| **Saturate on integer overflow** = `off` | Values wrap to the most negative value of the integer data type | - For 8-bit signed integers, -128 remains   -128. - For 16-bit signed integers, -32768 remains   -32768. - For 32-bit signed integers, -2147483648   remains -2147483648. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed fixed-point data types. | |

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

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block only supports signed fixed-point data types.

## Version History

**Introduced before R2006a**

## Description

Negate input

The
Unary
Minus
block negates the input.
