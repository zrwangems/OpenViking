---
type: simulink-block
title: '2-D IFFT'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2difft'
documentation_source_path: 'ref/2difft.html'
language: en
---

# 2-D IFFT

## Ports

### Input

### **Port\_1** — Input data vector | matrix

Input data, specified as a vector or matrix of intensity values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output data vector | matrix

Output data containing the 2-D IFFT of the input, returned as a vector or matrix.
The size and data type of the output are the same as those of the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main

### **FFT implementation** — FFT implementation `Auto` (default) | `Radix-2` | `FFTW`

Specify the type of implementation to compute the FFT as one of these options:

- `FFTW` — Select this option to use to support an
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

### **Input is in bit-reversed order** — Bit-reversed input `off` (default) | `on`

Specify whether the input to the block is in bit-reversed order or linear order.
Select this parameter when you specify the input in bit-reversed order. Otherwise,
clear this parameter. The block yields invalid output when you do not set this
parameter correctly. For more information on the bit-reversed order of input, see
Bit-Reversed Order.

#### Dependencies

To enable this parameter, set the **FFT implementation**
parameter to `Auto` or
`Radix-2`.

### **Input is conjugate symmetric** — Conjugate symmetric input `on` (default) | `off`

Select this parameter to specify that the block input is conjugate symmetric, and
you want real-valued outputs. Otherwise, clear this parameter.

The 2-D FFT block yields conjugate symmetric
output when you input real-valued data. Taking the 2-D IFFT of a conjugate symmetric
input matrix produces real-valued output. Therefore, if the input to the 2-D
IFFT block is conjugate symmetric, and you select this parameter, the block
produces real-valued outputs. When you select this parameter, the block optimizes its
computation method. You cannot select this parameter for fixed-point.

If you specify conjugate symmetric input data and do not select this parameter,
the block outputs complex-valued data with small imaginary parts. The block outputs
invalid data if you select this parameter with input data that is not conjugate
symmetric input data.

### **Divide output by product of FFT length in each input dimension** — Scale output data `on` (default) | `off`

Select this parameter to compute the scaled IFFT, which divides the output by the
product of the dimension lengths of the FFT input dimension, as shown in this
equation.

f(x,y)=1MN∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN,

where 0≤x≤M−1 and 0≤y≤N−1.

When you clear this parameter, the block computes the unscaled version of the
IFFT, as shown in this equation.

f(x,y)=∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN

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

Compute 2-D inverse fast Fourier transform (IFFT)

The 2-D IFFT block computes the inverse discrete Fourier transform (IDFT)
of a two-dimensional input matrix using the fast Fourier transform (FFT) algorithm. The
equation for the 2-D IDFT *f*(*x*, *y*) of
an *M*-by-*N* input matrix,
*F*(*m*, *n*), is:

f(x,y)=1MN∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN,

where 0≤x≤M−1 and 0≤y≤N−1.

The block supports FFT implementation based on the FFTW library and an implementation
based on a collection of Radix-2 algorithms. You can either manually select one of these
implementations or let the block select one automatically.
