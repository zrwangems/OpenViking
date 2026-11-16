---
type: simulink-block
title: 'Uniform Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Fixed-Point Design / Quantizers'
documentation_page: 'uniformdecoder'
documentation_source_path: 'ref/uniformdecoder.html'
language: en
---

# Uniform Decoder

## Ports

### Input

### **Input** — Input vector | matrix

Specify the integer input to be decoded as a vector or a
matrix.

The real and imaginary components of complex inputs wrap
independently.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes
### Output

### **Output** — Decoded output vector | matrix

Decoded floating-point output, returned as a vector or a
matrix.

For more information on how the block computes the output, see Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Peak** — Largest amplitude in encoded input `1` (default) | nonnegative scalar

Specify the largest amplitude represented in the encoded input as a
nonnegative scalar. To correctly decode values encoded with the
Uniform Encoder block, set the **Peak**
parameter in both blocks to the same value.

### **Bits** — Number of bits `3` (default) | integer in the range [`2`, `32`]

Specify the number of input bits *B* used to encode the
data. The number of bits *B* can be any integer value
between 2 and 32, inclusive. This value can be less than the total number of
bits supplied by the input data type. To correctly decode values encoded
with the Uniform Encoder block, set the
**Bits** parameters in both blocks to the same
value.

### **Overflow mode** — Overflow mode `Saturate` (default) | `Wrap`

Specify the block behavior when the integer input is outside the range
representable by *B* bits. Out-of-range inputs can either
saturate at the extreme value, or wrap back into range.

When you select `Saturate`,
*unsigned* input values greater than
2B−1 saturate at
2B−1 and *signed* input
values greater than 2B−1−1 or less than
−2B−1 saturate at those limits. The real and
imaginary components of complex inputs saturate independently.

When you select `Wrap`, *unsigned* input
values, `u`, greater than 2B−1
wrap back into the range [0, 2B−1] using
mod-2B arithmetic.

```
u = mod(u,2^B)
```

*Signed* input values, `u`, greater than
2B−1−1 or less than
−2B−1 wrap back into that range using
mod-2B arithmetic.

```
u = (mod(u+2^B/2,2^B)-(2^B/2))
```

The real and imaginary components of complex inputs wrap
independently.

### **Output type** — Output data type `Double` (default) | `Single`

Specify the precision of the decoded floating-point output as
`single` or `double`.
You can use either level of output precision with any of the six integer
input data types.

## Libraries

DSP System Toolbox / Quantizers

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Decode integer input into floating-point output

The Uniform Decoder block performs the inverse operation of the Uniform Encoder block, and reconstructs quantized floating-point values
from encoded integer input. The block adheres to the definition for uniform decoding
specified in ITU-T Recommendation G.701.

For more information on how the block computes the decoded floating-point output, see
Algorithms.
