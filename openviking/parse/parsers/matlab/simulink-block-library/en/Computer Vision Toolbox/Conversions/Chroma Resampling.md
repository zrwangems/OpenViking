---
type: simulink-block
title: 'Chroma Resampling'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'chromaresampling'
documentation_source_path: 'ref/chromaresampling.html'
language: en
---

# Chroma Resampling

## Ports

### Input

### **Cb** — Blue-difference chrominance component of image matrix

Blue-difference chrominance component of the image, specified as an
*M*-by-*D* matrix. *D* is half
the width of the image.

**Data Types:** `single` | `double` | `uint8`

### **Cr** — Red-difference chrominance component of image matrix

Red-difference chrominance component of the image, specified as an
*M*-by-*D* matrix. *D* is half
the width of the image.

**Data Types:** `single` | `double` | `uint8`
### Output

### **Cb** — Blue-difference chrominance component of image matrix

Blue-difference chrominance component of image, returned as an
*M*-by-*P* matrix. *P* is half
the width of the resampled image. If you downsample the input image,
*P* is less than *D*. If you upsample the input
image, *P* is greater than *D*.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Cr** — Red-difference chrominance component of image matrix

Red-difference chrominance component of image, returned as an
*M*-by-*P* matrix. *P* is half
the width of the resampled image. If you downsample the input image,
*P* is less than *D*. If you upsample the input
image, *P* is greater than *D*

**Data Types:** `single` | `double` | `int8` | `uint8`

## Parameters

### **Resampling** — Chrominance resampling method `4:4:4 to 4:2:2` (default) | `4:4:4 to 4:2:0 (MPEG1)` | `4:4:4 to 4:2:0 (MPEG2)` | ...

Specify the resampling method to use to downsample or upsample the chrominance
components of the image.

These options specify downsampling operations:

- `4:4:4 to 4:2:2`
- `4:4:4 to 4:2:0 (MPEG1)`
- `4:4:4 to 4:2:0 (MPEG2)`
- `4:4:4 to 4:1:1`
- `4:2:2 to 4:2:0 (MPEG1)`
- `4:2:2 to 4:2:0 (MPEG2)`

These options specify upsampling operations:

- `4:2:2 to 4:4:4`
- `4:2:0 (MPEG1) to 4:2:2`
- `4:2:0 (MPEG1) to 4:4:4`
- `4:2:0 (MPEG2) to 4:2:2`
- `4:2:0 (MPEG2) to 4:4:4`
- `4:1:1 to 4:4:4`

For more information, see Chrominance Resampling Formats.

### **Antialiasing filter** — Chroma downsampling antialiasing filter `Default` (default) | `User-defined` | `None`

Specify the lowpass filter that the block uses to prevent aliasing.

- `Default` — The block uses a built-in lowpass
  filter.
- `User-defined` — Specify custom filter coefficients
  for the block. Depending on the value of the Resampling parameter, this option
  enables the **Horizontal filter coefficients** parameter, the
  **Vertical filter coefficients** parameter, or both.
- `None` — The block does not filter the input
  signal.

#### Dependencies

To enable this parameter, set the **Resampling** parameter to one
of these options:

- `4:4:4 to 4:2:2`
- `4:4:4 to 4:2:0 (MPEG1)`
- `4:4:4 to 4:2:0 (MPEG2)`
- `4:4:4 to 4:1:1`
- `4:2:2 to 4:2:0 (MPEG1)`
- `4:2:2 to 4:2:0 (MPEG2)`

.

### **Horizontal filter coefficients** — Coefficients for horizontal lowpass filter [0.2 0.6 0.2] (default) | row vector

Specify the horizontal filter coefficients as a vector of even number of elements to
apply to your input signal.

#### Dependencies

To enable this parameter, you must:

- Set the **Resampling** parameter to one of these options:

  - `4:4:4 to 4:2:2`
  - `4:4:4 to 4:2:0 (MPEG1)`
  - `4:4:4 to 4:2:0 (MPEG2)`
  - `4:4:4 to 4:1:1`
- Set the **Antialiasing filter** parameter to
  `User-defined`.

### **Vertical filter coefficients** — Coefficients for vertical lowpass filter [0.5 0.5] (default) | row vector

Specify the filter coefficients as a vector of odd number of elements to apply to
your input signal.

#### Dependencies

To enable this parameter, you must:

- Set the **Resampling** parameter to one of these options:

  - `4:4:4 to 4:2:0 (MPEG1)`
  - `4:4:4 to 4:2:0 (MPEG2)`
  - `4:2:2 to 4:2:0 (MPEG1)`
  - `4:2:2 to 4:2:0 (MPEG2)`
- Set the **Antialiasing filter** parameter to
  `User-defined`.

### **Interpolation** — Chrominance upsampling interpolation method `linear` (default) | `pixel replication`

Specify whether the block uses linear interpolation or pixel replication
interpolation to approximate the missing chrominance values when upsampling an image.

- `linear` — The block uses linear interpolation to
  calculate the missing values.
- `pixel replication` — The block replicates the
  chrominance values of the neighboring pixels to assign values to the additional
  pixels in the upsampled image.

#### Dependencies

To enable this parameter, set the **Resampling** parameter to one
of these options:

- `4:2:2 to 4:4:4`
- `4:2:0 (MPEG1) to 4:2:2`
- `4:2:0 (MPEG1) to 4:4:4`
- `4:2:0 (MPEG2) to 4:2:2`
- `4:2:0 (MPEG2) to 4:4:4`
- `4:1:1 to 4:4:4`

.

### **Input image is transposed (data order is row major)** — Read data row-wise `off` (default) | `on`

Enable this parameter to read data elements row-wise.

## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Downsample or upsample chrominance components of images

The Chroma Resampling block resamples the chrominance components of an input image. Chroma
resampling consists of these operations:

- Downsample — Reduces the bandwidth required for transmission or storage of a signal.
  You can prevent aliasing by applying a lowpass filter to bandlimit the input
  signal.
- Upsample — Expands the bandwidth of the signal. This block performs interpolation to
  approximate the missing chrominance values.
