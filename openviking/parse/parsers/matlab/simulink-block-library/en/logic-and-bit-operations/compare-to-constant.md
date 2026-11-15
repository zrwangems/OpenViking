---
type: simulink-block
title: 'Compare To Constant'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetoconstant'
language: en
---

# Compare To Constant

Determine how signal compares to specified constant

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Compare To Constant block compares an input signal to a constant. Specify the
constant in the **Constant value** parameter. Specify how the input is
compared to the constant value with the **Operator** parameter.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix, is compared
with constant. The block first converts its **Constant
value** parameter to the input data type, and then performs
the specified operation.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output signal 0 | 1 | vector | matrix

The output is `0` if the comparison is false, and
`1` if it is true.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Operator** — Logical operator <= (default) | == | ~= | < | >= | >

This parameter can have these values:

- `==` — Determine whether the input is
  equal to the specified constant.
- ~`=` — Determine whether the input is not
  equal to the specified constant.
- `<` — Determine whether the input is
  less than the specified constant.
- `<=` — Determine whether the input is
  less than or equal to the specified constant.
- `>` — Determine whether the input is
  greater than the specified constant.
- `>=` — Determine whether the input is
  greater than or equal to the specified constant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `relop` |
| **Type**: character vector |
| **Values**: `'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **Default**: `'<='` |

### **Constant value** — Constant to compare with constant

Specify the constant value to which the input is compared.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `const` |
| **Type**: character vector |
| **Value:** scalar | vector | matrix | N-D array |
| **Default**: `'3.0'` |

### **Output data type** — Data type of the output `boolean` (default) | `uint8`

Specify the data type of the output, `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**:`'boolean'` | `'uint8'` |
| **Default**: `'boolean'` |

### **Enable zero-crossing detection** — Select to enable zero-crossing detection `'on'` (default) | `'off'`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

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

## Version History

**Introduced before R2006a**
