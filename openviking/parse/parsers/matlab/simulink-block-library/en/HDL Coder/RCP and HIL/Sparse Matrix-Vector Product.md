---
type: simulink-block
title: 'Sparse Matrix-Vector Product'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'sparsematrixvectorproduct'
documentation_source_path: 'ref/sparsematrixvectorproduct.html'
language: en
---

# Sparse Matrix-Vector Product

## Ports
```yaml
ports:
- name: x
  summary: Input signal scalar | vector
  direction: input
  data_types: single | double | fixed point
- name: y
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double | fixed point
```

### Input

### **x** — Input signal scalar | vector

Input signal, specified as a scalar or vector. The Sparse Matrix-Vector
Product block supports fixed-point data types. The number of input ports
depends on the dimension of **Matrix A**. For example, see Model 3-D
Matrix-Vector Multiplication.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **y** — Output signal scalar | vector

Output signal, returned as a scalar or vector. The output signal is the input
signal multiplied by the sparse matrix specified by **Matrix
A**.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Matrix A
  summary: Sparse matrix 1 (default) | real scalar, vector, or matrix
  group: Main
  block_parameter: A
  values: '"1" | real scalar, vector, or matrix'
- name: Output minimum
  summary: Minimum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMin
  values: '''[]'' (default) | scalar in quotes'
- name: Output maximum
  summary: Maximum output value for range checking [] (default) | scalar
  group: Signal Attributes
  block_parameter: OutMax
  values: '''[]'' (default) | scalar in quotes'
- name: Output data type
  summary: 'Output data type ''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling''
    | ''Inherit: Inherit via back propagation'' | ''Inherit: Same as first input'' | ''double'' | ''single'' | ''half'' |
    ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)''
    | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  group: Signal Attributes
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule'' (default) | ''Inherit: Keep MSB'' | ''Inherit: Match scaling'' | ''Inherit:
    Inherit via back propagation'' | ''Inherit: Same as first input'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8''
    | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''
    | ''<data type expression>'''
- name: Parameter minimum
  summary: Minimum value of sparse matrix [] (default) | scalar
  group: Parameter Attributes
  block_parameter: ParamMin
  values: '''[]'' (default) | scalar in quotes'
- name: Parameter maximum
  summary: Maximum value of sparse matrix [] (default) | scalar
  group: Parameter Attributes
  block_parameter: ParamMax
  values: '''[]'' (default) | scalar in quotes'
- name: Parameter data type
  summary: 'Specify the data type of the sparse matrix ''Inherit: Inherit via back propagation'' (default) | ''double'' |
    ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64''
    | '' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''Enum: <class name>'' | ''<data type expression>'''
  group: Parameter Attributes
  block_parameter: ParamDataTypeStr
  values: '''Inherit: Inherit via back propagation'' (default) | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8''
    | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)''
    | ''fixdt(1,16,2^0,0)'' | ''Enum: <class name>'' | ''<data type expression>'''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Matrix A** — Sparse matrix `1` (default) | real scalar, vector, or matrix

Specify the sparse matrix to multiply the input vector by. **Matrix
A** can be a real scalar, vector, or matrix.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `A` |
| **Values:** | `"1"` | real scalar, vector, or matrix |

### Signal Attributes

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Specify the minimum value of the output range that the software checks.

The software uses the output minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters) for
  some blocks
- Simulation range checking (see Specify Signal Ranges and Enable Simulation Range Checking)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Specify the maximum value of the output range that the software checks.

The software uses the output maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters) for
  some blocks
- Simulation range checking (see Specify Signal Ranges and Enable Simulation Range Checking)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Output data type `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

### Parameter Attributes

### **Parameter minimum** — Minimum value of sparse matrix `[]` (default) | scalar

Specify the minimum value of **Matrix A**. The default value is
`[]` (unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter maximum** — Maximum value of sparse matrix `[]` (default) | scalar

Specify the maximum value of **Matrix A**. The default value is
`[]` (unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter data type** — Specify the data type of the sparse matrix `'Inherit: Inherit via back propagation'` (default) | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'`

Specify the data type of the **Matrix A** parameter.

While tuning a parameter with this **Parameter data type**
setting, specify the **Parameter minimum** and **Parameter
maximum** parameters. These settings tell the software about the range of
values you want during the simulation and allows the software to provide a full
precision data type with sufficient range to allow safe tuning within the specified
range.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamDataTypeStr` |
| **Values:** | `'Inherit: Inherit via back propagation'` (default) | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'` |
## Libraries

HDL Coder / RCP and HIL

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy. |

| General | |
| --- | --- |
| **SharingFactor** | Specify the number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing. |

## Version History

**Introduced in R2024b**

## Description

Multiply sparse matrix with input vector

The Sparse Matrix-Vector Product block multiplies the sparse matrix
`A` with an input vector `x`.
