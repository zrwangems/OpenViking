---
type: simulink-block
title: 'Translate'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'translate'
documentation_source_path: 'ref/translate.html'
language: en
---

# Translate

## Ports

### Input

### **Image** — Input image or video matrix | array

Input image or video, specified as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array,
*M*-by-*N*-by-*C* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Offset** — Translation value vector

Translation value, specified as a two-element vector of the form
`[vertical horizontal]`. The `vertical` value in
the vector is the number of pixels to shift the image up or down in the vertical
direction. The `horizontal` element is the number of pixels to shift
the image left or right in the horizontal direction. The axes origin is the top-left
corner of the input image.

- To translate the image downward, specify positive pixel values to the
  `vertical` element.
- To translate the image upward, specify negative pixel values to the
  `vertical` element.
- To translate the image to the right, specify positive pixel values to the
  `horizontal` element.
- To translate the image to the left, specify negative pixel values to the
  `horizontal` element.

#### Dependencies

To enable this port, set the **Offset source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Output** — Translated image or video matrix | array

Translated image or video, returned as a
*P*-by-*Q* matrix,
*P*-by-*Q*-by-*T* array,
*P*-by-*Q*-by-*C* array, or
*P*-by-*Q*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Output size after translation** — Translated image size `Full` (default) | `Same as input image`

Specify the size of the translated image as `Full` or
`Same as input image`.

- `Full` — The block outputs a matrix that contains the
  entire translated image.
- `Same as input image` — The block outputs a matrix of
  the same size as the input image, which contains a portion of the translated
  image.

### **Offset source** — Source of translation value `Specify via dialog` (default) | `Input port`

Specify the source of translation value as one of these options:

- `Specify via dialog` — Specify the translation value
  using the **Offset** parameter.
- `Input port` — Specify the translation value using
  the **Offset** port.

### **Offset** — Translation value `[1.5 2.3]` (default) | two-element vector

Specify the translation value as a two-element vector of the form [`vertical
horizontal`]. The vertical element in the vector is the number of pixels to
shift the image up or down in the vertical direction. The horizontal element is the
number of pixels to shift the image left or right in the horizontal direction. The axes
origin is the top-left corner of the input image.

- To translate the image downward, specify positive pixel values to the
  `vertical` element.
- To translate the image upward, specify negative pixel values to the
  `vertical` element.
- To translate the image to the right, specify positive pixel values to the
  `horizontal` element.
- To translate the image to the left, specify negative pixel values to the
  `horizontal` element.

#### Dependencies

To enable this parameter, set the **Offset source** parameter to
`Specify via dialog`.

### **Maximum offset** — Translation value limits `[8 10]` (default) | two-element vector

Specify the maximum number of pixels to translate the input image in the vertical
and horizontal directions, as a vector of the form [`vertical
horizontal`]. The translate block uses this parameter to determine the size
of the translated image when the **Output size after translation**
parameter is set to `Full` and the **Offset
source** parameter is set to `Input port`. If either
input value to the **Offset** port is greater than the corresponding
value of the **Maximum offset** parameter, the translate block reduces
that input translation value to the corresponding maximum translation value.

#### Dependencies

To enable this parameter, set the **Offset source** parameter to
`Input port`.

### **Background fill value** — Intensity or color of background in translated image `0` (default) | scalar | RGB triplet

Specify the intensity or color of the background of the translated image as a scalar
intensity value or an RGB triplet.

### **Interpolation method** — Method for interpolating translated pixel values `Bilinear` (default) | `Nearest neighbor` | `Bicubic`

Specify the method by which to interpolate the pixel values of the translated image
as one of these options:

- `Nearest neighbor` —The Translate block uses the
  value of the nearest pixel for the interpolated pixel.
- `Bilinear` — The interpolated pixel value is the
  weighted average of the 4 nearest pixel values.
- `Bicubic` — The interpolated pixel value is the
  weighted average of the 16 nearest pixel values.

The number of pixels the block considers for interpolation affects the complexity
and accuracy of the computation. The `Nearest neighbor`
interpolation, which uses the fewest pixels, is the most computationally efficient and
least accurate, while the `Bicubic` interpolation is the least
computationally efficient and the most accurate. For more information about
interpolation methods and kernels, see the More About section and
the Create and Compare Resizing Interpolation Kernels example.

## Libraries

Computer Vision Toolbox / Geometric Transformations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Translate image or video frame

The Translate block shifts an input image or video frame by the number of pixels in the
vertical and horizontal directions specified by a two-element offset vector.
