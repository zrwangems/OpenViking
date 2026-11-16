---
type: simulink-block
title: 'String Constant'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringconstant'
language: en
---

# String Constant

Output specified string

## Libraries

Simulink / String

## Description

The String Constant block outputs a string specified by the
**String** parameter. Use this block when you want a constant whose
type is string.

## Ports

### Output

### **Port\_1** — Output string scalar

Output string, specified as a scalar.

**Data Types:** `string`

## Parameters

### **String** — Input string "Hello!" (default) | scalar

Input string, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `String` |
| **Type:** character vector |
| **Values:** `'"Hello!"'` | scalar |
| **Default:** `'"Hello!"'` |

### **Output data type** — Output data type `string` (default) | `<data type expression>`

Output data type, specified using the string data type to specify a string
with no maximum length.

To specify a string data type with a maximum length, specify
`stringtype(N)`. For
example, `stringtype(31)` creates a string data type with a
maximum length of 31 characters.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'string'` | *`<data type expression>`* |
| **Default:** `'string'` |

### **Mode** — Category of data `string` (default) | `scalar`

Use the `stringtype` function, for example,
`stringtype(31)`.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
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
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2018a**
