---
type: simulink-block
title: 'Compositing'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'compositing'
documentation_source_path: 'ref/compositing.html'
language: en
---

# Compositing

## Ports
```yaml
ports:
- name: Image1
  summary: Input image one matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Image2
  summary: Input image two matrix | array
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Mask
  summary: Binary mask scalar | matrix
  direction: input
  data_types: single | double | Boolean
- name: Factor
  summary: Opacity factor scalar | matrix
  direction: input
  data_types: single | double
- name: Location
  summary: Location index vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Port_1
  summary: Output image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### Input

### **Image1** — Input image one matrix | array

Input image one, specified as an *M*-by-*N*
matrix or *M*-by-*N*-by-*P* array.
If the input is a *M*-by-*N*-by-*P*
array, *P* is the number of color channels in the image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Image2** — Input image two matrix | array

Input image two, specified as an *M*-by-*N*
matrix or *M*-by-*N*-by-*P* array.
If the input is a *M*-by-*N*-by-*P*
array, *P* is the number of color channels in the image.

#### Dependencies

To enable this port, set the **Operation** parameter to
`Blend` or `Binary mask`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Mask** — Binary mask scalar | matrix

Binary mask, specified as a scalar or matrix. This mask determines which pixels
of **Image1** the block overwrites with the pixel values of
**Image2** or highlights, depending on the value of the
**Operation** parameter.

- `Binary mask` — The block overwrites the pixel
  values of **Image1**, indicated by the mask, with the
  corresponding pixel values of **Image2**. You can specify
  **Mask** as a scalar `0` or
  `1`, which the block uses for all pixels of
  **Image2**, or as binary matrix of same size as
  **Image2**.
- `Highlight selected pixels` — The block highlights
  the pixels of **Image1** indicated by the mask.

#### Dependencies

To enable this port:

- If overwriting pixel values in one image with pixel values in another image,
  set the **Operation** parameter to `Binary
  mask` and the **Mask source** parameter to
  `Input port`.
- If highlighting selected pixels in an image, set the
  **Operation** parameter to `Highlight selected
  pixels`.

**Data Types:** `single` | `double` | `Boolean`

### **Factor** — Opacity factor scalar | matrix

Opacity factor, specified as a scalar or matrix. If specified as a scalar, the
value is the scale of combination for each pixel of **Image2** with
each corresponding pixel of **Image1**. If specified as a matrix, its
dimensions must match the dimensions of **Image2**. Each opacity
factor must be in the range [0, 1].

#### Dependencies

To enable this port, set the **Operation** parameter to
`Blend` and the **Opacity factor(s)
source** parameter to `Input port`.

**Data Types:** `single` | `double`

### **Location** — Location index vector

Location index, specified as a two-element vector. The first element represents
the row and the second represents the column position of the upper-left corner of
**Image2**, relative to the upper-left corner
of **Image1**. If the location of the upper-left corner of
**Image2** is such that any of its pixels would render outside the
bounds of **Image1**, the block clips **Image2** at
the final row or column or **Image1**, instead.

**Note**

When the **Image1** input has a fixed-point or boolean data
type, the **Location** input must have a built-in integer data
type.

#### Dependencies

To enable this port, set the **Location source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output image matrix

Output image, returned as an *M*-by-*N* matrix
or *M*-by-*N*-by-*P* array. If the
output is an *M*-by-*N*-by-*P*
array, *P* is the number of color channels in the image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## Parameters
```yaml
parameters:
- name: Operation
  summary: Specify operation Blend (default) | Binary mask | Highlight selected pixels
  group: Main
- name: Opacity factor(s) source
  summary: Source of opacity factor Specify via dialog (default) | Input port
  group: Main
- name: Opacity factor(s)
  summary: Opacity factor 0.75 (default) | scalar | matrix
  group: Main
- name: Location source
  summary: Source of overlay location Specify via dialog (default) | Input port
  group: Main
- name: Location [x y]
  summary: Overlay location index [1 1] (default) | two-element vector
  group: Main
- name: Mask source
  summary: Source of mask Specify via dialog (default) | Input port
  group: Main
- name: Mask
  summary: Binary mask 0 (default) | 1 | matrix
  group: Main
```

### Main

### **Operation** — Specify operation `Blend` (default) | `Binary mask` | `Highlight selected pixels`

Select the image operation for the block to perform.

- `Blend` — Linearly combines the pixel values of
  **Image1** with the pixel values of
  **Image2**, with the specified opacity factor.
- `Binary mask` — Overwrites the pixel values of
  **Image1** with the values of **Image2**
  specified by the binary mask.
- `Highlight selected pixels` — Highlights the pixels
  of **Image1** indicated by the binary mask. The highlight
  operation assign the highest intensity or color values to the pixels of
  **Image1** corresponding to the pixels with logic 1 of the
  binary mask.

### **Opacity factor(s) source** — Source of opacity factor `Specify via dialog` (default) | `Input port`

Specify the source of the opacity factor. If you set this parameter to
`Input port`, it enables the **Factor**
input port.

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`Blend`.

### **Opacity factor(s)** — Opacity factor `0.75` (default) | scalar | matrix

Defines the scale of combination for each pixel of **Image2**
with each corresponding pixel of **Image1**. When you specify the
opacity factor as matrix, its dimensions must match the dimensions of
**Image2**. If you specify it as a scalar, the block uses that
value as the opacity factor for all pixels of **Image2**. The opacity
factor must be in the range [0, 1].

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`Blend` and the **Opacity factor(s)
source** parameter to `Specify via
dialog`.

### **Location source** — Source of overlay location `Specify via dialog` (default) | `Input port`

Select the source of the overlay location. If you set this parameter to
`Input port`, it enables the **Location**
input port.

### **Location [x y]** — Overlay location index `[1 1]` (default) | two-element vector

Specify the row and column position of the upper-left corner of
**Image2**, relative to the upper-left corner of
**Image1**, as a two-element vector. If the location of the
upper-left corner of **Image2** is such that any of its pixels would
render outside the bounds of **Image1**, the block clips
**Image2** at the final row or column or
**Image1**, instead.

#### Dependencies

To enable this parameter, set the **Location source** parameter
to `Specify via dialog`.

### **Mask source** — Source of mask `Specify via dialog` (default) | `Input port`

Select the source of the binary mask. If you set this parameter to
`Input port`, it enables the **Mask**
input port.

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`Binary mask`.

### **Mask** — Binary mask `0` (default) | `1` | matrix

Binary mask, specified as a scalar or matrix, defines which pixels of
**Image1** the block overwrites with the corresponding pixel values
of **Image2** or highlights. You specify `0` or
`1`, which the block uses for all pixels in
**Image2**, or a binary matrix of the same size of as
**Image2**.

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`Binary mask` and the **Mask source**
parameter to `Specify via dialog`.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).
## Libraries

Computer Vision Toolbox / Text & Graphics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Combine two images or apply mask to image

The Compositing block combines two images, overlays one image over another,
or highlights selected pixels in an image. When combining two images, the block uses this
equation, in which the output image *O* is a linear combination of the two
images I1 and I2:

O(i,j)=(1−X)∗I1(i,j)+X∗I2(i,j).

The opacity factor *X* scales each pixel before combining the images,
where 0≤X≤1.

When overlaying one image over another image, or highlighting selected pixels in an input
image, the block uses a binary mask to specify which pixels to overwrite or highlight.

**Note**

This block supports binary, intensity, and color images.
