---
type: simulink-block
title: 'Identity Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'identitymatrix'
documentation_source_path: 'slref/identitymatrix.html'
language: en
---

# Identity Matrix

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Identity matrix scalar | vector | matrix
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal used to determine dimensions of the output matrix, specified as a
scalar, vector, or matrix. When the input signal is an
*M*-by-*N* matrix, the block generates an
*M*-by-*N* matrix output with the same sample
period as the input. The values in the input matrix are ignored.

#### Dependencies

To enable this port, select the **Inherit output port attributes from
input port** check box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Identity matrix scalar | vector | matrix

Identity matrix, specified as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Inherit output port attributes from input port
  summary: Option for output port to inherit attributes from input port off (default) | on
  group: ''
  block_parameter: InheritOutputPortAttributes
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Output dimensions
  summary: Size of output matrix 5 (default) | scalar | two-element vector
  group: ''
  block_parameter: OutputDimensions
  type: character vector
  values: scalar | two-element vector
  default: '''5'''
- name: Output data type
  summary: 'Output data type double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 |
    boolean | fixdt(1,16,0) | Inherit: Inherit via back propagation | <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via back propagation'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16''
    | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''double'''
- name: Mode
  summary: Data type mode Inherit (default) | Built in | Fixed point | Expression
  group: ''
- name: Signedness
  summary: Signedness of fixed-point data Signed (default) | Unsigned
  group: ''
- name: Scaling
  summary: Method for scaling fixed-point data Best precision (default) | Binary point
  group: ''
- name: Word length
  summary: Bit size of word that holds quantized integer 16 (default) | integer from 2 to 65,535
  group: ''
- name: Fraction length
  summary: Fraction length for fixed-point data type 0 (default) | integer scalar
  group: ''
- name: Data type override
  summary: Data type override mode Inherit (default) | Off
  group: ''
- name: Sample time
  summary: Output sample period 1 (default) | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar or vector
  default: '''1'''
```

### **Inherit output port attributes from input port** — Option for output port to inherit attributes from input port off (default) | on

Select this check box for the output port to inherit its dimensions, sample period,
and data type from the input port. Otherwise, clear this check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InheritOutputPortAttributes` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Output dimensions** — Size of output matrix `5` (default) | scalar | two-element vector

The number of rows and columns in the output matrix. You can specify:

- A positive integer scalar *M* to create a square
  *M*-by-*M* output.
- A vector of positive integers, [*M*
  *N*], to create an *M*-by-*N*
  output.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputDimensions` |
| **Type:** character vector |
| **Values:** scalar | two-element vector |
| **Default:** `'5'` |

### **Output data type** — Output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

Specify the output data type for this block. You can select one of these
options:

- A rule that inherits a data type, for example, `Inherit: Inherit via
  back propagation`. When you select this option, the output data type
  and scaling matches that of the next downstream block.
- A built-in data type, such as `double`.
- An expression that evaluates to a valid data type, for example,
  `fixdt(1,16)`.

For help setting data type parameters, display the **Data Type
Assistant** by clicking the **Show data type assistant**
button .

See Control Data Types of Signals for more
information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **Default**: `'double'` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**. You can choose:

- `Inherit` — Specify a rule for inheriting a
  data type, for example, `Inherit: Same as input`.
- `Built in`— Specify a built-in data type, for
  example, `double`.
- `Fixed point` — Specify the fixed-point
  attributes of the data type.
- `Expression` — Specify an expression that
  evaluates to a valid data type, for example,
  `fixdt(1,16)`.

For more information, see Specify Data Types Using Data Type Assistant.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned.
`Signed` data can represent positive and negative values, but
`Unsigned` data represents positive values only. For more
information, see Specify Data Types Using Data Type Assistant.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow conditions
and minimize quantization errors. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`

### **Word length** — Bit size of word that holds quantized integer `16` (default) | integer from 2 to 65,535

Specify the bit size of the word that holds the quantized integer as a positive
integer from 2 to 65,535. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive or negative
integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point` and **Scaling** to `Binary
point`.

### **Data type override** — Data type override mode `Inherit` (default) | `Off`

Select the data type override mode for this signal. You can select:

- `Inherit` — Inherits the data type override setting
  specified for the model.
- `Off` — Ignores the data type override setting
  specified for the model and uses the fixed-point data type you specify.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`. For more information,
see Specify Data Types Using Data Type Assistant.

### **Sample time** — Output sample period `1` (default) | scalar

The discrete sample period of the output, specified as a real-valued scalar.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar or vector |
| **Default:** `'1'` |
## Libraries

Simulink / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2022a: Identity Matrix Block Added to Simulink Matrix Operations Library

The Identity Matrix block has been removed from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear**  > **Matrix Operations** library. For equivalent functionality, use the Identity Matrix
block in the **Simulink** > **Matrix Operations** library. All existing models continue to work.

## Description

Generate matrix with ones on main diagonal and ground values elsewhere

The Identity Matrix block outputs an identity matrix, similar to the
MATLAB®
`eye` function. The block generates a square or rectangular matrix with ones on
the main diagonal and zeros elsewhere.
