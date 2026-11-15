---
type: simulink-block
title: 'Discrete Impulse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'discreteimpulse'
documentation_source_path: 'ref/discreteimpulse.html'
language: en
---

# Discrete Impulse

## Ports

### Output

### **Port\_1** — Discrete impulse signal scalar | vector | matrix

Output signal containing a discrete impulse at output sample
`D(i)+1`, where `D` is a scalar or
vector specified by the **Delay** parameter. For more
information, see Description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Delay (samples)** — Number of zero-valued output samples `0` (default) | scalar | vector

The number of zero-valued output samples, `D`,
preceding the impulse, specified as a scalar or vector of integer
values, greater than or equal to zero. A length-*N*
vector specifies an *N*-channel output.

### **Sample time** — Output sample period `1` (default) | positive scalar

The sample period, *Ts*, of
the output signal specified as a positive finite scalar. The output
frame period is
*M**Ts*.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

The number of samples, *M*, in each output frame,
specified as a positive integer scalar.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

Specify the output data type for this block. You can select one of the
following:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`. When you select this option, the
  output data type and scaling matches that of the next downstream
  block.
- A built-in data type, such as `double`
- An expression that evaluates to a valid data type, for
  example, `fixdt(1,16)`

For help setting data type parameters, display the **Data Type
Assistant** by clicking the **Show data type
assistant** button
.

See Control Data Types of Signals (Simulink) for more
information.

### Data Type Assistant

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

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 2 to 128

Specify the bit size of the word that holds the quantized integer as a
positive integer from 2 to 128. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive
or negative integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point` and
**Scaling** to `Binary
point`.

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

## Libraries

DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Generate discrete impulse

The Discrete Impulse block generates an impulse (the value
`1`) at output sample `D+1`, where you specify
`D` using the **Delay** parameter
(`D` ≥ `0`). All output samples preceding and
following sample `D+1` are zero.

When `D` is a length-*N* vector, the block generates
an *M*-by-*N* matrix output representing
*N* distinct channels, where you specify frame size
*M* using the **Samples per frame** parameter. The
impulse for the `i`th channel appears at sample
`D(i)+1`.

The **Sample time** parameter value,
*Ts*, specifies the output signal sample
period. The resulting frame period is
*M**Ts*.
