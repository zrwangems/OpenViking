---
type: simulink-block
title: 'Shear'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'shear'
documentation_source_path: 'ref/shear.html'
language: en
---

# Shear

## Ports
```yaml
ports:
- name: Image
  summary: Input image or video matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: S
  summary: Shear value vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Output
  summary: Transformed image or video matrix | array
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### Input

### **Image** — Input image or video matrix | array

Input image or video, specified as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array,
*M*-by-*N*-by-*C* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **S** — Shear value vector

Shear value, specified as a two-element vector of the form, `[first
last]`.

- To horizontally shear the image, the block shifts the pixels of the first
  and last rows using the `first` and `last`
  values, respectively, specified to the **S** port.
- To vertically shear the image, the block shifts the pixels of the first and
  last columns using the `first` and `last`
  values, respectively,specified to the **S** port.

#### Dependencies

To enable this port, set the **Shear values source** parameter
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Output** — Transformed image or video matrix | array

Transformed image or video, returned as a
*P*-by-*Q* matrix,
*P*-by-*Q*-by-*T* array,
*P*-by-*Q*-by-*C* array, or
*P*-by-*Q*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## Parameters
```yaml
parameters:
- name: Shear direction
  summary: Direction of transformation Horizontal (default) | Vertical
  group: ''
- name: Output size after shear
  summary: Transformed image size Full (default) | Same as input image
  group: ''
- name: Shear values source
  summary: Source of shear value offset limits Specify via dialog (default) | Input port
  group: ''
- name: Row/column shear values [first last]
  summary: Shear value offset limits [0 3] (default) | two-element vector
  group: ''
- name: Maximum shear value
  summary: Maximum row or column shear 20 (default) | scalar
  group: ''
- name: Background fill value
  summary: Intensity value of the background in transformed image 0 (default) | scalar | three-element vector
  group: ''
- name: Interpolation method
  summary: Method for interpolating transformed pixel values Bilinear (default) | Nearest neighbor | Bicubic
  group: ''
```

### **Shear direction** — Direction of transformation `Horizontal` (default) | `Vertical`

Specify the shear direction for the input image, as one of these options:

- `Horizontal` — Shifts the rows of the input image
  with a linearly varying offset. Specify the offset limits of the first and the
  last row using the **Row/column shear values [first last]**
  parameter.
- `Vertical` — Shifts the columns of the input image
  with a linearly varying offset. Specify the offset limits of the first and the
  last column using the **Row/column shear values [first last]**
  parameter.

Illustration of the effect of horizontal and vertical shear on transforming the input image

### **Output size after shear** — Transformed image size `Full` (default) | `Same as input image`

Specify the size of the transformed image as, `Full` or
`Same as input image`.

- `Full` — The block outputs the entire sheared
  image.
- `Same as input image` — The block outputs a matrix of
  the same size as the input image. In this case, the output image contains the
  top-left portion of the sheared image, as limited by the input image
  dimensions.

### **Shear values source** — Source of shear value offset limits `Specify via dialog` (default) | `Input port`

Select the source of shear value offset limits from these options:

- `Specify via dialog` — Specify the shear value offset
  limits using the **Row/column shear values [first last]**
  parameter.
- `Input port` — Specify the shear value offset limits
  using the **S** port.

### **Row/column shear values [first last]** — Shear value offset limits `[0 3]` (default) | two-element vector

Specify the shear value offset limits as a two-element vector of the form
[`first last`]. The `first` and
`last` values represent the number of pixels to shift the first and
last rows or columns of the input image, respectively.

For example, if you set the **Shear direction** parameter to
`Horizontal` and specify the **Row/column shear
values [first last]** parameter value as `[50 150]`, the
block shifts the top row of the input image 50 pixels to the right and the bottom row
150 pixels to the right. To move either row to the left, specify a negative value for
the corresponding element of **Row/column shear values [first last]**
parameter.

Similarly, if you set the **Shear direction** parameter to
`Vertical` and specify the **Row/column shear values
[first last]** parameter value as `[10 50]`, the block
shifts the furthest left column 10 pixels down and the furthest right column 50 pixels
down. To shift either column up, specify a negative value for the corresponding element
of **Row/column shear values [first last]** parameter.

#### Dependencies

To enable this parameter, set the **Shear values source**
parameter to `Specify via dialog`.

### **Maximum shear value** — Maximum row or column shear `20` (default) | scalar

Specify the maximum number of pixels to shear any row or column of the input image.
The shear block uses this parameter to determine the size of the sheared image. If any
input to the **S** port is greater than the absolute value of the
**Maximum shear value** parameter, the shear block reduces the input
value to the maximum shear value.

#### Dependencies

To enable this parameter, set the **Shear values source**
parameter to `Input port`.

### **Background fill value** — Intensity value of the background in transformed image `0` (default) | scalar | three-element vector

Specify the intensity value of the background of the transformed image as a scalar
intensity value or a three-element vector representing an RGB triplet.

### **Interpolation method** — Method for interpolating transformed pixel values `Bilinear` (default) | `Nearest neighbor` | `Bicubic`

Specify the method by which to interpolate the pixel values of the sheared image, as
one of these options:

- `Nearest neighbor` —The Shear block uses the value of
  1 nearest pixel for the new pixel value.
- `Bilinear` — The new pixel value is the weighted
  average of the 4 nearest pixel values.
- `Bicubic` — The new pixel value is the weighted
  average of the 16 nearest pixel values.

The number of pixels the block considers for interpolation affects the complexity
and accuracy of the computation. The `Nearest neighbor`
interpolation, which uses the fewest pixels, is the most computationally efficient and
least accurate while the `Bicubic` interpolation is the least
computationally efficient and the most accurate. For more information about the
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

Shift rows or columns of an image or a video frame by linearly varying offset

The Shear block transforms an input image or a video frame by shifting the rows or
columns. The block transforms the input image using either horizontal or vertical
shear.

- Horizontal shear linearly shifts the rows in the image by gradually increasing the
  offset from left to right or right to left.
- Vertical shear linearly shifts the columns in the image by gradually increasing the
  offset from top to bottom or bottom to top.
