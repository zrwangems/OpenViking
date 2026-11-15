---
type: simulink-block
title: 'Expand Scalar'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'expandscalar'
---

# Expand Scalar

Create matrix from scalar using scalar expansion

## Libraries

Simulink / Matrix Operations

## Description

The Expand Scalar block outputs a scalar-expanded matrix where each element
in the matrix has the same value.

## Ports

### Output

### **Port\_1** — Scalar-expanded matrix scalar | vector | matrix

Scalar-expanded matrix, returned as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `bus` | `Boolean` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Element value** — Matrix element value `1` (default) | scalar

Specify the matrix element value as a scalar for the expanded matrix. Element value
can be a `struct`.

**Tunable:** Yes

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ElementValue` |
| **Values:** | 1 (default) | scalar |
| **Data Types:** | `char` |

### **Output dimensions** — Dimension of output matrix `5` (default) | scalar | two-element vector

Specify the dimension of output matrix as a scalar or vector.

- A positive integer scalar creates an unoriented vector.
- A 2-D vector creates an oriented vector.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputDimensions` |
| **Values:** | `'5'` (default) | scalar | two-element vector |
| **Data Types:** | `char` |

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

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'double'` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>` |
| **Data Types:** | `char` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**.

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
`Signed` data can represent positive and negative values.
`Unsigned` data represents positive values only. For more
information, see Specify Data Types Using Data Type Assistant.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling fixed-point data to avoid overflow conditions and
minimize quantization errors. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed
point`.

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

Specify the discrete sample period of the output as a real-valued scalar.

#### Dependencies

To enable this parameter, clear the **Inherit output port attributes from
input port** check box.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `'1'` (default) | scalar |
| **Data Types:** | `char` |

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

**Introduced in R2024a**

### R2024b: Expand Scalar block supports `struct` expansion

The Expand Scalar block now supports MATLAB®
`struct` expansion with a Simulink bus data type.
