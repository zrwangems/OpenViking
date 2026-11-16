---
type: simulink-block
title: 'Offset'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'ALG / AlgExpression'
documentation_page: 'offset'
documentation_source_path: '../dsp/ref/offset.html'
language: en
---

# Offset

## Ports

### Input

### **In1** — First input data scalar | vector

Specify the first input data as a scalar or a vector. The inputs to
the **In** ports (**In1**,
**In2**, … ) must be of the same size and data
type.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **O1** — First offset value integer

Specify the offset value that the block uses to truncate the first input data as an
integer. The offset value determines the number of samples the block
removes or keeps at the beginning or at the end of the first
data.

The inputs to the **O** ports (**O1**,
**O2**, … ) must have the same data type. The block
rounds any offset value that is a noninteger value to the nearest
integer value. If the offset value is out of the [0
*N*] range, then the **Action for out of range
offset value** parameter determines how the block behaves.
*N* is the input vector length.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **In2** — Second input data scalar | vector

Specify the second input data as a scalar or a vector. The inputs to
the **In** ports (**In1**,
**In2**, … ) must be of the same size and data
type.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **O2** — Second offset value integer

Specify the offset value that the block uses to truncate the second input data as an
integer. The offset value determines the number of samples the block
removes or keeps at the beginning or at the end of the second
data.

The inputs to the **O** ports (**O1**,
**O2**, … ) must have the same data type. The block
rounds any offset value that is a noninteger value to the nearest
integer value. If the offset value is out of the [0
*N*] range, then the **Action for out of range
offset value** parameter determines how the block behaves.
*N* is the input vector length.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Out1** — First truncated data scalar | vector

The block returns the truncated data as a scalar or a vector. The
length of the truncated data depends on the **Output port
length** and the **Output length**
parameters. If **Output port length** is set to
`Same as input`, the truncated data has the
same size as the input data. If **Output port length**
is set to `User-defined`, then the
**Output length** parameter determines the length
of the output data.

There is one output port for each pair of **In** and
**O** ports.

The truncated output has the same data type as the input data. When
the output is fixed-point, it is signed only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **Out2** — Second truncated data scalar | vector

The block returns the truncated data as a scalar or a vector. The
length of the truncated data depends on the **Output port
length** and the **Output length**
parameters. If **Output port length** is set to
`Same as input`, the truncated data has the
same size as the input data. If **Output port length**
is set to `User-defined`, then the
**Output length** parameter determines the length
of the output data.

There is one output port for each pair of **In** and
**O** ports.

The truncated output has the same data type as the input data. When
the output is fixed-point, it is signed only.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Mode** — Specify which values to discard and which values to keep `Remove beginning samples` (default) | `Remove ending samples` | `Keep beginning samples` | `Keep ending samples`

Use this parameter to specify which values the block discards and which values the block
keeps from the input vector.

Select from the following:

- `Remove beginning samples` –– Discard
  the initial values of a vector.
- `Remove ending samples` –– Discard
  the final values of a vector.
- `Keep beginning samples` –– Retain
  the initial values of a vector.
- `Keep ending samples` –– Retain the
  final values of a vector.

### **Number of input data-offset pairs** — Number of input data-offset pairs `2` (default) | positive integer

Use the **Number of input data-offset pairs** parameter to specify the
number of inputs to the block. The number of input ports is twice the scalar
value you specify in this parameter. For example, if you enter
`3`, input ports **In1**,
**O1**, **In2**,
**O2**, **In3**, and
**O3** appear on the block.

### **Output port length** — Mode to specify output port length `Same as input` (default) | `User-defined`

Use this parameter to specify the length of the output vectors. If you select
`Same as input`, the output vectors have the
same length as the input vectors. If you select
`User-defined`, you can enter the desired
length in the **Output length** parameter.

### **Output length** — Desired length of output vectors `9` (default) | positive integer

Enter a scalar that represents the desired length of the output vectors.
If the desired output length that you specify is greater than the number of
values that the block extracts from the input vector, the block zero-pads
the end of the vector to reach the length that you specify.

#### Dependencies

This parameter is visible only if you set the **Output port
length** parameter to
`User-defined`.

### **Action for out of range offset value** — Action for out of range offset value `Clip` (default) | `Clip and warn` | `Error`

Use this parameter to determine how the block behaves when an offset value
is not in the range such that 0 ≤ offset value ≤ *N*, where *N* is the input vector length.

- `Clip` –– Offset values less than 0
  are set to 0 and offset values greater than *N*
  are set to *N*.
- `Clip and warn` –– Offset values less
  than 0 are set to 0 and offset values greater than
  *N* are set to *N*. In
  addition, the block displays a warning message.
- `Error` –– Simulation stops and the
  block displays an error when the offset values or out of
  range.

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

## Version History

**Introduced before R2006a**

## Description

Truncate vectors by removing or keeping beginning or ending values

The Offset block removes or keeps values from the beginning or end of the
input vectors. The number of values to remove or keep is determined by the offset value
that you specify through the **O** ports (**O1**,
**O2**, … ). The length of the truncated vector is determined by
the **Output port length** and **Output length**
parameters. The **Number of input data-offset pairs** parameter
determines the number of input data-offset pairs.
