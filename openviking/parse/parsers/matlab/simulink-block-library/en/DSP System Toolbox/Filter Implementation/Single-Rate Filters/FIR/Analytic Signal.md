---
type: simulink-block
title: 'Analytic Signal'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Single-Rate Filters / FIR'
documentation_page: 'analyticsignal'
documentation_source_path: 'ref/analyticsignal.html'
language: en
---

# Analytic Signal

## Ports

### Input

### **Input** — Data input vector | matrix

Specify the data input *u* as a vector or a matrix of
size *M*-by-*N*.

**Data Types:** `single` | `double`
### Output

### **Output** — Analytic signal output vector | matrix

Analytic signal output *y*, returned as a vector or a
matrix.

The block computes the analytic signal for each channel. The real part of the output in
each channel is a replica of the real input in that channel. The
imaginary part of the output is the Hilbert transform of the input. In
the frequency domain, the Fourier transform of the analytic signal
doubles the positive frequency content of the original signal while
zeroing out the negative frequencies and retaining the DC
component.

The output has the same size and data type as the input.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Filter order (must be even)** — Filter order `100` (default) | even positive integer

Specify the order of the Hilbert FIR filter as an even positive integer. The FIR filter
computes the Hilbert transform of the real input signal. When the filter
order is low, the block uses an equiripple FIR filter to compute the Hilbert
transform. For higher filter orders, if the equiripple design fails, the
block uses a Kaiser window FIR filter instead.

### **Input processing** — Method to process input signals `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify how the block should process the input.

You can set this parameter to one of these options:

- `Columns as channels (frame based)`
  — The block performs frame-based processing. In this mode,
  the block treats an *M*-by-*N*
  matrix input as *N* independent channels containing
  *M* sequential time samples. The block computes
  the analytic signal for each channel over time.
- `Elements as channels (sample based)`
  — The block performs sample-based processing. In this mode,
  the block treats an *M*-by-*N*
  matrix input as *M*\**N*
  independent channels and computes the analytic signal for each
  channel (matrix element) over time.

## Libraries

DSP System Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

The Analytic Signal block supports SIMD code generation using Intel AVX2
code replacement library under these conditions:

- **Input processing** is set to `Columns as
  channels (frame based)`.
- Input signal has to be real-valued.
- Input signal has a data type of `single` or
  `double`.

The SIMD technology significantly improves the performance of the generated code.
For more information, see SIMD Code Generation. To
generate SIMD code from this block, see Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks.

## Version History

**Introduced before R2006a**

### R2025a: Support for Kaiser window FIR filter at higher filter orders

When you specify a higher filter order, the Analytic Signal block uses a
Kaiser window FIR filter to compute the Hilbert transform, resulting in a more
robust filter design at higher orders.

## Description

Compute analytic signals of discrete-time inputs

The Analytic Signal block computes the complex analytic signal
*y* corresponding to each channel of the real input
*u*.

y=u+jH{u},

where j=−1 and *H*{ } denotes the Hilbert transform.

The block computes the Hilbert transform using an equiripple FIR filter or a Kaiser
window FIR filter. When the filter order is low, the block uses an equiripple FIR
filter. For higher filter orders, if the equiripple design fails, the block uses a
Kaiser window FIR filter.

This block supports C/C++ code generation and SIMD code generation. For details, see Code Generation.
