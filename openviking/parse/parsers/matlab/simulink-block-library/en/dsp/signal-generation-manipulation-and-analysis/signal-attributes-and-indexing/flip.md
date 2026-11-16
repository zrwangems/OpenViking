---
type: simulink-block
title: 'Flip'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Attributes and Indexing'
documentation_page: 'flip'
documentation_source_path: 'ref/flip.html'
language: en
---

# Flip

## Ports

### Input

### **Input** — Input signal matrix

Input signal, specified as a matrix of size
*M*-by-*N*.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Output** — Flipped output matrix

Flipped output, returned as a matrix of size
*M*-by-*N*. The output always has
the same dimensionality as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Flip along** — Specify dimension to flip along `Columns` (default) | `Rows`

Specify the dimension along which to flip the input as
`Columns` or `Rows`.
When you set this parameter to `Columns`, the block
flips the input vertically. When you set this parameter to
`Rows`, the block flips the input
horizontally.

When you set this parameter to `Columns`, the
block flips the input *vertically* so the first row of
the input becomes the last row of the output.

```
y = flipud(u) % Equivalent MATLAB code
```

When flipping the input vertically, the block treats
length-*M* unoriented vector inputs as
*M*-by-1 column vectors.

When you set this parameter to `Rows`, the block
flips the input *horizontally* so the first column of the
input becomes the last column of the output.

```
y = fliplr(u) % Equivalent MATLAB code
```

When flipping the input horizontally, the block treats
length-*N* unoriented vector inputs as
1-by-*N* row vectors.

## Libraries

DSP System Toolbox / Signal Management / Indexing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Flip input vertically or horizontally

The Flip block vertically or horizontally reverses the
*M*-by-*N* input matrix, *u*. The
block determines the dimension to flip along using the **Flip along** parameter.

This block supports Simulink® virtual buses.
