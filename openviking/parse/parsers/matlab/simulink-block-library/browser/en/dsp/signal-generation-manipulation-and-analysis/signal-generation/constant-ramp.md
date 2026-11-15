---
type: simulink-block
title: 'Constant Ramp'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'constantramp'
documentation_source_path: 'ref/constantramp.html'
language: en
---

# Constant Ramp

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal used to generate ramp signal, specified as a scalar,
vector, matrix, or N-D array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal vector

Output signal, returned as an unoriented vector. The block determines the length of the
output based on the length of the input signal, and the **Ramp
length equals number of** or **Dimension**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Ramp length equals number of** — Dimension used to determine ramp length `Rows` (default) | `Columns` | `Elements in specified dimension`

Specify whether the length of the output ramp is the number of rows,
number of columns, or the length of the specified dimension of the
input.

### **Dimension** — Dimension that determines length of output ramp `1` (default) | positive integer

Specify the one-based dimension of the input array that determines the
length of the output ramp as a positive integer scalar.

#### Dependencies

To enable this parameter, set **Ramp length equals number
of** to `Elements in specified
dimension`.

### **Slope** — Slope of the ramp `1` (default) | scalar

Specify the slope of the ramp as a real-valued double-precision
scalar.

### **Offset** — *y*-intercept of the ramp `0` (default) | scalar

Specify the scalar *y*-intercept of the ramp as a
real-valued double-precision scalar.

### Data Types

### **Output data type** — Output data type `Inherit: Same as input` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type for this block. You can select one of the
following:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`.
- A built-in data type, such as `double`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16)`

For help setting data type parameters, display the **Data Type
Assistant** by clicking the **Show data type
assistant** button
.

See Control Data Types of Signals (Simulink) for more
information.

### Data Type Assistant Parameters

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output data type**. You can choose:

- `Inherit` — Lets you
  specify a rule for inheriting a data type, for example,
  `Inherit: Same as input`
- `Built in`— Lets you
  specify a built-in data type, for example,
  `double`
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type,
  for example, `fixdt(1,16)`

For more information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned.
`Signed` data can represent positive and
negative values, but `Unsigned` data represents
positive values only. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 2 to 128

Specify the bit size of the word that holds the quantized integer as
an integer scalar from 2 to 128. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Data type override** — Data type override mode `Inherit` (default) | `Off`

Select the data type override mode for this signal. You can select:

- `Inherit` — Inherits the data type override setting
  specified for the model.
- `Off` — Ignores the data type override setting
  specified for the model and uses the fixed-point data type you specify.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive
or negative integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point` and
**Scaling** to `Binary
point`.

## Libraries

DSP System Toolbox / Signal Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Generate ramp signal with length based on input dimensions

The Constant Ramp block generates the constant ramp signal

```
y = (0:L-1)*m + b
```

where *m* is the slope specified by the scalar
**Slope** parameter, and *b* is the
*y*-intercept specified by the scalar **Offset**
parameter.

For an unoriented vector input, *L* is equal to the length of the
input vector. For an N-D input array, the length *L* of the output ramp
is equal to the length of the input in the dimension specified by the **Ramp
length equals number of** or **Dimension** parameter. The
output, *y*, is always an unoriented vector.
