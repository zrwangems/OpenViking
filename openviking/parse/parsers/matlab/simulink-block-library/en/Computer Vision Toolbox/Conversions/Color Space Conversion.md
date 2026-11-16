---
type: simulink-block
title: 'Color Space Conversion'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'colorspaceconversion'
documentation_source_path: 'ref/colorspaceconversion.html'
language: en
---

# Color Space Conversion

## Ports

### Input

### **Port\_1** — Input image array

Input image, specified as an
*M*-by-*N*-by-*C* array, where
*C* is the number of color channels in the input image.

**Data Types:** `single` | `double` | `uint8`

### **R'** — Red color component of image matrix

Red color component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **R'**, **G'**, and
**B'** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **G'** — Green color component of image matrix

Green color component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **R'**, **G'**, and
**B'** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **B'** — Blue color component of image matrix

Blue color component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **R'**, **G'**, and
**B'** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **Y'** — Luma component of image matrix

Luma component of image, specified as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `Y'CbCr to
R'G'B'`.

**Data Types:** `single` | `double` | `uint8`

### **Cb** — Blue-difference chroma component of image matrix

Blue-difference chroma component of image, specified as an
*M*-by-*D* matrix, where *D* is
half the width of the image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `Y'CbCr to
R'G'B'`.

**Data Types:** `single` | `double` | `uint8`

### **Cr** — Red-difference chroma component of image matrix

Red-difference chroma component of image, specified as an
*M*-by-*D* matrix, where *D* is
half the width of the image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `Y'CbCr to
R'G'B'`.

**Data Types:** `single` | `double` | `uint8`

### **H** — Hue component of image matrix

Hue component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **H**, **S**, and
**V** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `HSV to
R'G'B'`.

**Data Types:** `single` | `double`

### **S** — Saturation component of image matrix

Saturation component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **H**, **S**, and
**V** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `HSV to
R'G'B'`.

**Data Types:** `single` | `double`

### **V** — Brightness component of image matrix

Brightness component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **H**, **S**, and
**V** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `HSV to
R'G'B'`.

**Data Types:** `single` | `double`

### **X** — X component of image matrix

X component of image, specified as an *M*-by-*N*
matrix.

**Note**

Inputs to the **X**, **Y**, and
**Z** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `XYZ to
sR'G'B'`.

**Data Types:** `single` | `double`

### **Y** — Y component of image matrix

Y component of image, specified as an *M*-by-*N*
matrix.

**Note**

Inputs to the **X**, **Y**, and
**Z** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `XYZ to
sR'G'B'`.

**Data Types:** `single` | `double`

### **Z** — Z component of image matrix

Z component of image, specified as an *M*-by-*N*
matrix.

**Note**

Inputs to the **X**, **Y**, and
**Z** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `XYZ to
sR'G'B'`.

**Data Types:** `single` | `double`

### **L\*** — Lightness component of image matrix

Lightness component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **L\***, **a\***, and
**b\*** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `L*a*b* to
sR'G'B'`.

**Data Types:** `single` | `double`

### **a\*** — Red-green component of image *M*-by-*N* matrix

Red-green component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **L\***, **a\***, and
**b\*** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `L*a*b* to
sR'G'B'`.

**Data Types:** `single` | `double`

### **b\*** — Yellow-blue component of image *M*-by-*N* matrix

Yellow-blue component of image, specified as an
*M*-by-*N* matrix.

**Note**

Inputs to the **L\***, **a\***, and
**b\*** ports must have the same dimensions and data type as one
another.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `L*a*b* to
sR'G'B'`.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output image array

Output image, returned as an
*M*-by-*N*-by-*P* array, where
*P* is the number of color channels in the output image. For Y'CbCr
output, the value range for the Y component differs from those of the Cb and Cr
components.

- If the input is `uint8`, then Y'CbCr is
  `uint8`. `Y'` is in the range `[16,
  235]`, and `Cb` and `Cr` are in the
  range `[16, 240]`.
- If the input is `double`, then `Y'CbCr` is
  `double`. `Y'` is in the range
  `[16/255, 235/255]`, and `Cb` and
  `Cr` are in the range `[16/255,
  240/255]`.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **R'** — Red color component of image matrix

Red color component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **G'** — Green color component of image matrix

Green color component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

**Data Types:** `single` | `double` | `int8` | `uint8`

### **B'** — Blue color component of image matrix

Blue color component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to one of these options:

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Y'** — Luma component of image matrix

Luma component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
Y'CbCr`.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Cb** — Blue-difference chroma component of image matrix

Blue-difference chroma component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
Y'CbCr`.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Cr** — Red-difference chroma component of image matrix

Red-difference chroma component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
Y'CbCr`.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **I'** — Intensity image matrix

Intensity image, returned as an *M*-by-*N*
matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
intensity`.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **H** — Hue component of image matrix

Hue component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
HSV`.

**Data Types:** `single` | `double`

### **S** — Saturation component of image matrix

Saturation component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
HSV`.

**Data Types:** `single` | `double`

### **V** — Brightness component of image matrix

Brightness component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `R'G'B' to
HSV`.

**Data Types:** `single` | `double`

### **X** — X component of image matrix

X component of image, returned as an *M*-by-*N*
matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
XYZ`.

**Data Types:** `single` | `double`

### **Y** — Y component of image matrix

Y component of image, returned as an *M*-by-*N*
matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
XYZ`.

**Data Types:** `single` | `double`

### **Z** — Z component of image matrix

Z component of image, returned as an *M*-by-*N*
matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
XYZ`.

**Data Types:** `single` | `double`

### **L\*** — Lightness component of image matrix

Lightness component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
L*a*b*`.

**Data Types:** `single` | `double`

### **a\*** — Red-green component of image matrix

Red-green component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
L*a*b*`.

**Data Types:** `single` | `double`

### **b\*** — Yellow-blue component of image matrix

Yellow-blue component of image, returned as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals` and set the
**Conversion** parameter to `sR'G'B' to
L*a*b*`.

**Data Types:** `single` | `double`

## Parameters

### **Conversion** — Color space conversion `R'G'B' to Y'CbCr` (default) | `Y'CbCr to R'G'B'` | `R'G'B' to intensity` | ...

Specify which color space to convert the image from and to using these options:

- `R'G'B' to Y'CbCr`
- `Y'CbCr to R'G'B'`
- `R'G'B' to intensity`
- `B'G'R' to intensity`
- `B'G'R' to R'G'B'`
- `R'G'B' to B'G'R'`
- `R'G'B' to HSV`
- `HSV to R'G'B'`
- `sR'G'B' to XYZ`
- `XYZ to sR'G'B'`
- `sR'G'B' to L*a*b*`
- `L*a*b* to sR'G'B'`

**Note**

The prime notation indicates that the signal is gamma corrected.

### **Use conversion specified by** — Color conversion standard `Rec. 601 (SDTV)` (default) | `Rec. 709 (HDTV)`

Specify the color conversion standard for converting the image between the R'G'B'
and Y'CbCr color spaces as either `Rec. 601 (SDTV)` or
`Rec. 709 (HDTV)`.

#### Dependencies

To enable this parameter, set the **Conversion** parameter to
`R'G'B' to Y'CbCr` or `Y'CbCr to
R'G'B'`.

### **Scanning standard** — Scanning standard `1125/60/2:1` (default) | `1250/50/2:1`

Specify the scanning standard for converting the image between the R'G'B' and Y'CbCr
color spaces as either `1125/60/2:1` or
`1250/50/2:1`.

#### Dependencies

To enable this parameter, set the **Conversion** parameter to
`R'G'B' to Y'CbCr` or `Y'CbCr to
R'G'B'` and set the **Use conversion specified by**
parameter to `Rec. 709 (HDTV)`.

### **White point** — White point `D50` (default) | `D55` | `D65`

Specify the reference white point for converting the image between the sR'G'B' and
L\*a\*b\* color spaces as `D50`, `D55`,
or `D65`.

#### Dependencies

To enable this parameter, set the **Conversion** parameter to
`sR'G'B' to L*a*b*` or `L*a*b* to
sR'G'B'`.

### **Image signal** — Image signal input `One multidimensional signal` (default) | `Separate color signals`

Specify whether to combine the color channels of the image into one signal or input
and output them individually.

- `One multidimensional signal` — The block accepts all
  color channels of the input image as a multidimensional array to a single input
  port, and outputs the converted image as a single matrix or array from a single
  output port.
- `Separate color signals` — The block accepts each
  color channel of the input image to a separate input port, and outputs each color
  channel of the converted image from a separate output port.

## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` | `image` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Convert color space of image

The Color Space Conversion block converts color information between color
spaces. Use the **Conversion** parameter to specify the color spaces you are
converting between.
