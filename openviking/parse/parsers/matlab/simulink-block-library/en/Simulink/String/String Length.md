---
type: simulink-block
title: 'String Length'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringlength'
documentation_source_path: 'slref/stringlength.html'
language: en
---

# String Length

## Ports
```yaml
ports:
- name: Port_1
  summary: Input string scalar
  direction: input
  data_types: string
- name: Port_1
  summary: Number of characters scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
```

### Input

### **Port\_1** — Input string scalar

Input string, specified as a scalar.

**Data Types:** `string`
### Output

### **Port\_1** — Number of characters scalar

Number of characters in the input string, specified as a
scalar.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
## Parameters
```yaml
parameters:
- name: Output data type
  summary: 'Output data type Inherit: Inherit via internal rule (default) | Inherit: Inherit via back propagation | int8 |
    uint8 | int16 | uint16 | int32 | uint32 | <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Inherit via back propagation'' | ''int8'' | ''uint8'' | ''int16''
    | ''uint16'' | ''int32'' | ''uint32'' | *<data type expression>*'
  default: '''Inherit: Inherit via internal rule'''
- name: Mode
  summary: Category of data type Inherit (default) | Built in | Expression
  group: ''
```

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule` —
  Simulink® chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware.
- `Inherit: Inherit via back propagation` —
  Use data type of the driving block.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`,
`Built in`, or `Expression`. For more
information on using this parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.
## Libraries

Simulink / String

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

## Description

Output number of characters in input string

The String Length block outputs the number of characters in the input
string. For example, you can use the String Length block to move focus of
attention to a particular location in a string.
