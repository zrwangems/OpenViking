---
type: simulink-block
title: 'Demosaic'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'demosaic'
documentation_source_path: 'ref/demosaic.html'
language: en
---

# Demosaic

## Ports
```yaml
ports:
- name: I
  summary: Image to demosaic matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: R
  summary: Red color channel of processed image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: G
  summary: Green color channel of processed image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: B
  summary: Blue color channel of processed image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Image
  summary: Multidimensional processed image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **I** — Image to demosaic matrix

Image to demosaic, specified as a 2-D numeric matrix. The size requirements for
the matrix depend on the value of the **Interpolation algorithm**
parameter.

- If the value of **Interpolation algorithm** is
  `Bilinear`, the matrix must have three or more rows and three
  or more columns.
- If the value of **Interpolation algorithm** is
  `Gradient-corrected linear`, the matrix must have five or more
  rows and five or more columns.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **R** — Red color channel of processed image matrix

Red color channel of processed image, returned as a 2-D numeric matrix of the same
size and data type as **I**.

#### Dependencies

To enable this port, set the **Output image signal** parameter
to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G** — Green color channel of processed image matrix

Green color channel of processed image, returned as a 2-D numeric matrix of the
same size and data type as **I**.

#### Dependencies

To enable this port, set the **Output image signal** parameter
to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **B** — Blue color channel of processed image matrix

Blue color channel of processed image, returned as a 2-D numeric matrix of the
same size and data type as **I**.

#### Dependencies

To enable this port, set the **Output image signal** parameter
to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Image** — Multidimensional processed image matrix

Multidimensional processed image, returned as a 3-D numeric matrix of the same
data type as **I**. If the input image **I** has the
dimensions *M*-by-*N*, then
**Image** has the dimensions
*M*-by-*N*-by-*P*, where
*P* is the number of color channels.

#### Dependencies

To enable this port, specify the **Output image signal**
parameter as `One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Interpolation algorithm
  summary: Interpolation algorithm Bilinear (default) | Gradient-corrected linear
  group: Main
- name: Sensor alignment
  summary: R,G,B pixel alignment RGGB (default) | GRBG | GBRG | BGGR
  group: Main
- name: Output image signal
  summary: Dimensions of output image One multidimensional signal (default) | Separate color signals
  group: Main
- name: Lock data type settings against change by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types
```

### Main

### **Interpolation algorithm** — Interpolation algorithm `Bilinear` (default) | `Gradient-corrected linear`

Specify the algorithm the block uses to calculate the missing color information.
If you select `Bilinear`, the block spatially averages the
values of the neighboring pixels of a missing color value to calculate its color
information.

If you select `Gradient-corrected linear`, the block uses
a Weiner approach to minimize the mean-squared error in the interpolation. This method
performs well on the edges of objects in the image. Both methods use symmetric padding
at the image boundaries. For more information, see the Image Pad block reference page.

### **Sensor alignment** — R,G,B pixel alignment `RGGB` (default) | `GRBG` | `GBRG` | `BGGR`

Specify the alignment of the input image. Select the sequence of R, G, and B
pixels that correspond to the 2-by-2 block of pixels in the top-left corner of the
image. Specify the sequence in left-to-right, top-to-bottom order. For example, for
this image, you would select `BGGR`.

Illustration of 4-by-4 image in Bayer format with each pixel labeled R, G, or B.

### **Output image signal** — Dimensions of output image `One multidimensional signal` (default) | `Separate color signals`

Specify how to output the RGB image. Given an
*M*-by-*N* input image, this parameter affects the
output of this block in these ways.

- `One multidimensional image` — The block has a single port,
  Image, that outputs an
  *M*-by-*N*-by-*P* RGB image,
  where *P* is the number of color channels.
- `Separate color signals` — The block has three ports, R, G,
  and B, that each output one *M*-by-*N* color
  channel of the RGB image.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006b**

## Description

Demosaic Bayer format images

The Demosaic block takes images in Bayer format and outputs RGB images. The block performs
this operation using a gradient-corrected linear interpolation algorithm or a bilinear
interpolation algorithm. This figure illustrates a 4-by-4 image in Bayer format with each
pixel labeled R, G, or B.

Illustration of 4-by-4 image in Bayer format with each pixel labeled R, G, or B.
