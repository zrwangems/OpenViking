---
type: simulink-block
title: 'Check Signal Attributes'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Attributes and Indexing'
documentation_page: 'checksignalattributes'
documentation_source_path: 'ref/checksignalattributes.html'
language: en
---

# Check Signal Attributes

## Ports

### Input

### **Input** — Input signal scalar | vector | matrix | N-D array

Input signal to be checked, specified as a scalar, vector, matrix, or
N-D array. The input can be any real- or complex-valued signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Output** — Output signal scalar | vector | matrix | N-D array

Output signal, returned as a scalar, vector, matrix, or N-D array,
with the same values as the input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Error when input** — Generate error when input `Does not match attributes exactly` (default) | `Matches attributes exactly`

Specify whether the block generates an error when the input
*does* or *does not* possess
*all* of the required attributes.

When you set this parameter to `Does not match attributes
exactly`, the block generates an error when the input fails
to match *any* of the specified attributes. Only signals
that possess *all* of the specified attributes propagate
to the output unaltered and do not cause the block to generate an
error.

When you set this parameter to `Matches attributes
exactly`, the block generates an error only when the input
possesses *all* specified attributes. Signals that do not
possess *all* of the specified attributes propagate to
the output unaltered, and do not cause the block to generate an
error.

### **Complexity** — Specify complexity `Ignore` (default) | `Real` | `Complex`

Specify the complexity for which you want to check the input as
`Real` or `Complex`.
You can display this information in a model by attaching a Probe (Simulink) block with
**Probe complex signal** selected. Alternatively, in
the **Debug** tab, select **Information
Overlays** > **Port Data Type**.

When you set this parameter to `Ignore`, the
block does not check the complexity of the input.

### **Dimensionality** — Dimensionality check `Ignore` (default) | `Is...` | `Is not...`

Specify whether you want to check the input for compliance or noncompliance with the
attributes in the subordinate **Dimensions** parameter.
When you set this parameter to `Ignore`, the block
does not check the dimensionality of the input.

### **Dimensions** — Specify dimensions `1-D` (default) | `2-D` | `Scalar (1-D or 2-D)` | `Vector (1-D or 2-D)` | `Vector (1-D or 2-D) or scalar` | `Row vector (2-D)` | `Row vector (2-D) or scalar` | `Column vector (2-D)` | `Column vector (2-D) or scalar` | `Full matrix (2-D)` | `Square matrix (2-D)`

Specify the dimensions for which you want to check the input.

Check the dimensionality of the input for compliance or noncompliance with
the attributes in this parameter. See the following table.
*M* and *N* are positive integers
unless otherwise indicated.

| Dimensions | Is... | Is not... |
| --- | --- | --- |
| 1-D | 1-D vector,   1-D scalar | *M*-by-*N* matrix,   1-by-*N* matrix (row vector),   *M*-by-1 matrix (column vector),   1-by-1 matrix (2-D scalar) |
| 2-D | *M*-by-*N* matrix,   1-by-*N* matrix (row vector),   *M*-by-1 matrix (column vector),   1-by-1 matrix (2-D scalar) | 1-D vector,   1-D scalar |
| Scalar   (1-D or 2-D) | 1-D scalar,   1-by-1 matrix (2-D scalar) | 1-D vector with length>1,   *M*-by-*N* matrix with *M*>1 and/or *N*>1 |
| Vector   (1-D or 2-D) | 1-D vector,   1-D scalar,   1-by-*N* matrix (row vector),   *M*-by-1 matrix (column vector),   1-by-1 matrix (2-D scalar)   Vector (1-D or 2-D) or scalar | *M*-by-*N* matrix with *M*>1 and *N*>1 |
| Row Vector   (2-D) | 1-by-*N* matrix (row vector),   1-by-1 matrix (2-D scalar)   Row vector (2-D) or scalar | 1-D vector,   1-D scalar,   *M*-by-*N* matrix with *M*>1 |
| Column Vector   (2-D) | *M*-by-1 matrix (column vector), 1-by-1 matrix (2-D scalar)   Column vector (2-D) or scalar | 1-D vector,   1-D scalar,   *M*-by-*N* matrix with *N*>1 |
| Full matrix | *M*-by-*N* matrix with *M*>1 and *N*>1 | 1-D vector,   1-D scalar,   1-by-*N* matrix (row vector),   *M*-by-1 matrix (column vector),   1-by-1 matrix (2-D scalar) |
| Square matrix | *M*-by-*N* matrix with *M*=*N*,   1-D scalar,   1-by-1 matrix (2-D scalar | *M*-by-*N* matrix with *M*≠*N*,   1-D vector,   1-by-*N* matrix (row vector),   *M*-by-1 matrix (column vector) |

In the **Debug** tab, when you select
**Information Overlays** > **Signal
Dimensions**, Simulink® displays the size of a 1-D vector signal as an unbracketed
integer, and displays the dimension of a 2-D signal as a pair of bracketed
integers, `[MxN]`. Simulink
*does not display* any size information for a 1-D or 2-D
scalar signal. You can also display dimension information for a signal in a
model by attaching a Probe block with **Probe signal
dimensions** selected.

#### Dependencies

To enable this parameter, set **Dimensionality** to
`Is...` or `Is
not...`.

### **Data type** — Data type check `Ignore` (default) | `Is...` | `Is not...`

Specify whether you want to check the input for compliance
`Is...` or noncompliance `Is
not...` with the attributes in the subordinate
**General data type** parameter. When you set this
parameter to `Ignore`, the block does not check the
input data type.

See the following table. You can individually select any of the specific
data types listed in the `(Is...)` column from the
subordinate **Specific data type** parameter.

| General Data Type | Is... | Is not... |
| --- | --- | --- |
| Boolean | `boolean` | `single, double, uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Enumerated | A user-defined enumerated data type. See Data Types (Simulink). | `boolean, single, double, uint8, int8, uint16, int16, uint32, int32`, fixed point |
| Floating point | `single, double` | `boolean, uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Floating point or Boolean | `single, double, boolean` | `uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Fixed point | fixed point, `uint8, int8, uint16, int16, uint32, int32` | `boolean, single, double`, enumerated |
| Integer | Signed integer   `int8`, `int16`, `int32`Unsigned integer   `uint8`, `uint16`, `uint32` | `boolean, single, double`, fixed point, enumerated |

To display data type information, in the **Debug** tab,
select **Information Overlays** > **Port Data
Type**.

### **General data type** — General data type check `Boolean` (default) | `Enumerated` | `Floating-point` | `Floating-point or boolean` | `Fixed-point` | `Integer`

Specify the general data type for which you want to check the
input.

#### Dependencies

To enable this parameter, set **Data type** to
`Is...` or `Is
not...`.

### **Specific floating-point** — Specific floating-point check `Any floating-point` (default) | `Double precision` | `Single precision`

Specify the floating-point data type for which you want to check the
input.

#### Dependencies

To enable this parameter, set **General data type**
to `Floating-point` or
`Floating-point or boolean`.

### **Specific fixed-point** — Specific fixed-point check `Any fixed-point` (default) | `Signed fixed-point` | `Unsigned fixed-point`

Specify the fixed-point data type for which you want to check the
input.

#### Dependencies

To enable this parameter, set **General data type**
to `Fixed-point`.

### **Specific integer** — Specific integer check `Any integer` (default) | `Signed integer` | `Unsigned integer` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

Specify the integer data type for which you want to check the
input.

#### Dependencies

To enable this parameter, set **General data type**
to `Integer`.

### **Sample time** — Sample time check `Ignore` (default) | `Discrete` | `Continuous`

Specify the sample time for which you want to check the input as
`Discrete` or
`Continuous`. When you set this parameter to
`Ignore`, the block does not check the sample
time of the input.

The block checks whether the signal is discrete time or continuous time.
In the **Debug** tab, when you select
**Information Overlays** >
**Colors**, Simulink displays continuous-time signal lines in black or grey and
discrete-time signal lines in colors corresponding to the relative
rate.

When you attach a Probe block with **Probe sample time**
enabled to a continuous-time signal, the block icon displays `Ts:[0
To]`, where `To` is the sample time offset.
Valid values of `To` for continuous-time signals are
`0` and `1`. When
`To` is `0`, updates occur at every
major and minor time step. When `To` is
`1`, updates occur only at major time steps and the
sample time is *fixed in minor time step*.

When you attach a Probe block with **Probe sample time**
enabled to a discrete-time signal, the block icon displays `Ts:[Ts
To]` for sample-based signals, and `Tf:[Tf
To]` for frame-based signals. `Ts` and
`Tf` are the positive sample period and frame period,
respectively. `To` is the offset, such that 0 ≤ *`offset`* <
*`period`*. Frame-based signals are almost always discrete
time.

## Libraries

DSP System Toolbox / Signal Management / Signal Attributes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Error when input signal does or does not match selected attributes exactly

The Check Signal Attributes block terminates the simulation with an error when the
input characteristics differ from the characteristics you specify in the block
parameters.

The Check Signal Attributes block can test for up to five different signal attributes.
When you select `Ignore` for any parameter, the block does not
check the signal for the corresponding attribute. For example, when you set
**Complexity** to `Ignore`, neither real
nor complex inputs cause the block to generate an error.
