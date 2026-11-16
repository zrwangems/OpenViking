---
type: simulink-block
title: '2-D FFT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Filters, Transforms, and Enhancements'
documentation_page: '2dfft'
documentation_source_path: 'ref/2dfft.html'
language: en
---

# 2-D FFT

## Ports

### Input

### **Port\_1** — Input data vector | matrix

Input data, specified as a vector or matrix of intensity values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output data vector | matrix

Output data containing the 2-D FFT of the input, returned as a vector or matrix.
The size and data type of the output are the same as those of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main

### **FFT implementation** — FFT implementation `Auto` (default) | `Radix-2` | `FFTW`

Specify the type of implementation to use to compute the FFT as one of these options:

- `FFTW` — Select this option to support an
  arbitrary-length input signal. The block restricts generated code with the
  `FFTW` implementation to host computers capable of
  running MATLAB®.
- `Radix-2` — Select this option to support
  bit-reversed processing, fixed and floating-point data, or portable C-code
  generation using Simulink Coder. The dimensions of
  the input matrix, *M* and *N*, must be powers
  of two. To work with other input sizes, use the Image Pad block to pad or truncate
  these dimensions to powers of two, or, if possible, choose the
  `FFTW` implementation. For more information about the
  algorithms used by the `Radix-2` mode, see Radix-2 Implementation.
- `Auto` — Select this option to let the block choose
  the FFT implementation. For non-power-of-two transform lengths, the block
  restricts generated code to MATLAB host computers.

### **Output in bit-reversed order** — Bit-reversed output `off` (default) | `on`

Select this parameter to get the output data in bit-reversed order relative to the
order of the input data. If you clear this parameter, the output data appears in
linear order relative to the order of the input data. For more information on the
bit-reversed order of output, see Bit-Reversed Order.

#### Dependencies

To enable this parameter, set the **FFT implementation**
parameter to `Auto` or
`Radix-2`.

### **Scale result by FFT length** — Scale output data `off` (default) | `on`

When you select this parameter, the block divides the output by the FFT length.
This option is useful when you want the output of the FFT to stay in the same
amplitude range as its input. This is particularly useful when working with
fixed-point data types.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- When these conditions apply, the executable generated from this block relies on
  prebuilt dynamic library files (`.dll` files) included with
  MATLAB:

  - **FFT implementation** is set to
    `FFTW`.
  - **Inherit FFT length from input dimensions** is cleared,
    and the length of each dimension of the input matrix is a power of two.

  Use the `packNGo` function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another
  development environment where MATLAB is not installed.
- When the length of each dimension of the input matrix is a power of two, you can
  generate standalone C and C++ code from this block.

## Version History

**Introduced before R2006a**

## Description

Compute 2-D fast Fourier transform (FFT)

The 2-D FFT block computes the discrete Fourier transform (DFT) of a
two-dimensional input matrix using the fast Fourier transform (FFT) algorithm. The equation
for the two-dimensional DFT *F*(*m*, *n*)
of an *M*-by-*N* input matrix,
*f*(*x*, *y*), is:

F(m,n)=∑x=0M−1∑y=0N−1f(x,y)e−j2πmxMe−j2πnyN

where 0≤m≤M−1 and 0≤n≤N−1.

The block supports FFT implementation based on the FFTW library and an implementation
based on a collection of Radix-2 algorithms. You can either manually select one of these
implementations or let the block select one automatically.
