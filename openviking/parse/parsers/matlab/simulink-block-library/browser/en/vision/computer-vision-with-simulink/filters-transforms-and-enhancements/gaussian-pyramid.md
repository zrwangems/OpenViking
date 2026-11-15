---
type: simulink-block
title: 'Gaussian Pyramid'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Filters, Transforms, and Enhancements'
documentation_page: 'gaussianpyramid'
documentation_source_path: 'ref/gaussianpyramid.html'
language: en
---

# Gaussian Pyramid

## Ports

### Input

### **I** — Input image scalar | vector | matrix | array

Input image, specified as a scalar, a vector, an
*M*-by-*N* matrix, or an
*M*-by-*N*-by-*C* array.
*C* is the number of color channels in the input image. To specify
this input as a scalar or vector, you must set the **Operation**
parameter to `Expand`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### Output

### **Port\_1** — Output image scalar | vector | matrix | array

Output image, returned as a scalar, a vector, a matrix, or an array. The
dimensions of the output image are determined by the **Operation**and
**Pyramid level** parameter values. For this port to return a
scalar or vector, you must set the **Operation** parameter to
`Reduce`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Operation** — Select operation `Reduce` (default) | `Expand`

Select the Gaussian pyramid operation as one of these methods:

- `Reduce` — The block applies a lowpass filter and
  then downsamples the input image.
- `Expand` — The block upsamples and then applies a
  lowpass filter to the input image.

### **Pyramid level** — Image scaling factor `1` (default) | positive integer

Specify the factor of 2 by which to upsample or downsample each dimension of the
image.

For an *M*-by-*N* input image, if you set the
**Operation**  parameter to `Reduce` and the
**Pyramid level** to `1`, the dimensions of
the output image are
`ceil(M/2)`-by-`ceil(N/2)`.

For an *M*-by-*N* input image, if you set the
**Operation**  parameter to `Expand`, the
dimensions of the output image are
[(M-1)2l+1]-by-[(N-1)2l+1],
where the **Pyramid level** parameter *l* must be a
positive integer.

### **Coefficient source** — Lowpass filter coefficient source `Default separable filter [1/4-a/2 1/4 a 1/4 1/4-a/2]` (default) | `Specify via dialog`

Specify the lowpass filter coefficient source as `Default separable
filter [1/4-a/2 1/4 a 1/4 1/4-a/2]` or `Specify via
dialog`.

### **Coefficients for separable filter** — Separable filter coefficient `[0.0625 0.25 0.375 0.25 0.0625]` (default) | vector

Specify the separable filter coefficients as a vector.

### **Hidden coefficients** — Hidden separable filter coefficients `[1/4-0.375/2 1/4 0.375 1/4 1/4-0.375/2]` (default) | vector

Specify the hidden separable filter coefficients as a vector.

## Libraries

Computer Vision Toolbox / Transforms

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Perform Gaussian pyramid decomposition

The Gaussian Pyramid block computes Gaussian pyramid reduction or expansion
to resize an image. The image reduction process involves lowpass filtering and then
downsampling the image pixels. The image expansion process involves upsampling and then
lowpass filtering the image pixels. You can also use this block to build a Laplacian
pyramid.
