---
type: simulink-block
title: 'Substring'
family: string
documentation_release: R2025b
official_category: 'String'
documentation_page: 'substring'
---

# Substring

Extract substring from input string signal

## Libraries

Simulink / String

## Description

The Substring block extracts a substring from the input string signal. The
block extracts the substring starting from the letter corresponding to
**idx** and includes a **len** number of
characters starting at **idx**. For example, if the input string is
`"hello 123"`, input **idx** is
`1`, and input **len** is `5`,
the output is `"hello"`. The block extracts a substring starting at
`1` and the next 4 characters for a total of 5 characters
(`hello`).

## Ports

### Input

### **str** — Input string signal scalar

Input string signal, specified as a string.

**Data Types:** `string`

### **idx** — Start of string to extract scalar

Start of string to extract, specified as a positive scalar
integer.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **len** — Length of string to extract scalar

Length of string to extract, specified as a scalar. If **len** causes
the substring to extend beyond the end of the string, the output signal
contains few than **len** characters.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **sub** — Extracted string scalar

Extracted string, specified as a scalar.

**Data Types:** `string`

## Parameters

### **Inherit maximum length from input** — Use same maximum length as input string `on` (default) | `off`

Use same maximum length as the input string source block.

on
:   Use same maximum length. The substring includes the
    characters starting from the character at
    **idx** to the end of the string.

off
:   Do not use same maximum length.

#### Dependencies

Selecting this check box enables the **Output data
type** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InheritMaximumLength` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

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

#### Dependencies

To enable this parameter, select **Inherit maximum length from
input**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'string'` | *`<data type expression>`* |
| **Default:** `'string'` |

### **Output string from 'idx' to end** — Extract string from `idx` to end `off` (default) | `on`

Extract string from `idx` to end of input string.

on
:   Extract string from `idx` to end of input
    string.

off
:   Do not extract string from `idx` to end of
    input string.

#### Dependencies

Selecting this parameter removes the third input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StringFromIdxToEnd` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
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
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2018a**
