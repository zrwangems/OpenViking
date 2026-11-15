---
type: simulink-block
title: 'Find Nonzero Elements'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'findnonzeroelements'
---

# Find Nonzero Elements

Find nonzero elements in array

## Libraries

Simulink / Math Operations

## Description

The Find Nonzero Elements block locates all nonzero elements of the input
signal and returns the linear indices of those elements. If the input is a
multidimensional signal, the Find Nonzero Elements block can also return
the subscripts of the nonzero input elements. In both cases, you can show an output port
with the nonzero input values.

The Find Nonzero Elements block outputs a variable-size signal. The sample
time for any variable-size signal must be discrete. If your model does not already use a
fixed-step solver, you may need to select a fixed-step solver in the Configuration
Parameters dialog. For more information, see Compare Solvers
and Choose a Solver.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal from which the block finds all nonzero elements.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Indices of nonzero elements variable-size signal

The Find Nonzero Elements block outputs the indices of nonzero elements
as a variable-size signal. You control the data type of the output using
the **Output data type** block parameter.

#### Dependencies

By default, the block outputs linear indices from the first output port. When you
change the **Index output format** to
`Subscripts`, the block instead
provides the element indices of a two-dimension or larger signal in
a subscript form. In this mode, you must specify the
**Number of input dimensions**, and the block
creates a separate output port for each dimension.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Values of nonzero elements variable-size signal

The Find block can optionally output the values of all nonzero
elements as a variable-size signal.

#### Dependencies

To enable this port, select **Show output port for nonzero
input values**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Index output format** — Format for indices of nonzero elements `Linear indices` (default) | `Subscripts`

Select the output format for the indices of the nonzero input
values.

- Selecting `Linear indices` provides
  the element indices of any dimension signal in a vector form.
  For one dimension (vector) signals, indices correspond to the
  position of nonzero values within the vector. For signals with
  more than one dimension, the conversion of subscripts to indices
  is along the first dimension. You do not need to know the signal
  dimension of the input signal.
- Selecting `Subscripts` provides the
  element indices of a two-dimension or larger signal in a
  subscript form. Because the block shows an output port for each
  dimension, this option requires you to specify the
  **Number of input dimensions**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexOutputFormat` |
| **Type:** character vector |
| **Values:** `'Linear indices'` | `'Subscripts'` |
| **Default:** `'Linear indices'` |

### **Number of input dimensions** — Number of dimensions for the input signal `1` (default) | scalar

Specify the number of dimensions for the input signal as a positive integer value from 1
to 32.

#### Dependencies

To enable this parameter, set **Index output
format** to
`Subscripts`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfInputDimensions` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **Index mode** — Specify zero- or one-based indexing `Zero-based` (default) | `One-based`

Specify the indexing mode as `Zero-based` or
`One-based`.

- For `Zero-based` indexing, an index
  of `0` specifies the first element of the input
  vector. An index of `1` specifies the second
  element, and so on.
- For `One-based` indexing, an index of
  `1` specifies the first element of the
  input vector. An index of `2`, specifies the
  second element, and so on.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexMode` |
| **Type:** character vector |
| **Values:** `'Zero-based'` | `'One-based'` |
| **Default:** `'Zero-based'` |

### **Show output port for nonzero input values** — Enable output port for nonzero values `off` (default) | `on`

Show or hide the output port for nonzero input values.

- When you clear this check box (`off`), the
  block hides the output port for nonzero input values.
- When you select this check box (`on`), the
  block displays the output port for nonzero input values. The
  additional output port provides values of the nonzero input
  elements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPortForNonzeroInputValues` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
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

### Data Types

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

Specify the output data type.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink® that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling your fixed-point data `Integer` (default)

Specify the method for scaling your fixed-point data to avoid overflow conditions and
minimize quantization errors. Selecting
`Integer` specifies a binary point location
for fixed-point data and sets the fraction length to
`0`. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2010a**
