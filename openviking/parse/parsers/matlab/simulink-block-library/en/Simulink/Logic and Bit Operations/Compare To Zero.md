---
type: simulink-block
title: 'Compare To Zero'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetozero'
documentation_source_path: 'slref/comparetozero.html'
language: en
---

# Compare To Zero

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as scalar, vector, or matrix, is compared with
zero. If the input data type cannot represent zero, parameter overflow
occurs. To detect this overflow, go to the **Diagnostics >
Data Validity** pane of the Configuration Parameters dialog
box and set **Parameters > Detect overflow** to
`warning` or
`error`.

In this case, the block compares the input signal to the
*ground value* of the input data type. For
example, if you have an input signal of type
`fixdt(0,8,2^0,10)`, the input data type can
represent unsigned 8-bit integers from 10 to 265 due to a bias of 10.
The ground value is 10, instead of 0.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal 0 | 1 | scalar | vector | matrix

The output is `0` if the comparison is false, and
`1` if it is true.

The block output is `uint8` or
`boolean`, depending on your selection for the
**Output data type** parameter.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Operator** — Logical operator <= (default) | == | ~= | < | >= | >

This parameter can have the following values:

- `==` — Determine whether the input is
  equal to zero.
- ~`=` — Determine whether the input is not
  equal to zero.
- `<` — Determine whether the input is
  less than zero.
- `<=` — Determine whether the input is
  less than or equal to zero.
- `>` — Determine whether the input is
  greater than zero.
- `>=` — Determine whether the input is
  greater than or equal to zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `relop` |
| **Type**: character vector |
| **Values**: `'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **Default**: `'<='` |

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

### **Enable zero-crossing detection** — Select to enable zero-crossing detection on (default) | off

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
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

## Description

Determine how signal compares to zero

The Compare To Zero block compares an input signal to zero. Specify how the input is
compared to zero with the **Operator** parameter.

The output is `0` if the comparison is false, and
`1` if it is true.
