---
type: simulink-block
title: 'Median Filter'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: en
---

# Median Filter

## Ports
```yaml
ports:
- name: I
  summary: Input image matrix
  direction: input
  data_types: single | double | int8 | int16 | uint8 | uint16 | Boolean | fixed point
- name: PVal
  summary: Pad value scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Port_1
  summary: Output image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Input

### **I** — Input image matrix

Input image, specified as an *M*-by-*N*
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **PVal** — Pad value scalar

Pad value, specified as a scalar. The block uses this value for each element of
the rows or columns added to the input image.

#### Dependencies

To enable this port:

- Set the **Output size** parameter to `Same as
  input port I`.
- Set the **Padding options** parameter to
  `Constant`.
- Set the **Pad value source** parameter to
  `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Output image matrix

Output image, returned as a matrix. The dimensions of the median-filtered output
image are specified by the **Output size** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Neighborhood size
  summary: Neighborhood window size [3 3] (default) | positive integer | two-element vector of positive integers
  group: ''
- name: Output size
  summary: Output sizing method Same as input port I (default) | Valid
  group: ''
- name: Padding options
  summary: Padding method Symmetric (default) | Constant | Replicate | Circular
  group: ''
- name: Pad value source
  summary: Source of constant padding value Specify via dialog (default) | Input port
  group: ''
- name: Pad value
  summary: Pad value 0 (default) | scalar
  group: ''
```

### **Neighborhood size** — Neighborhood window size `[3 3]` (default) | positive integer | two-element vector of positive integers

Specify the window size of the neighborhood over which the block computes the
median. If specified as a scalar, this value creates a square neighborhood with the
specified number of rows and columns. If specified as a vector, the first element is the
number of rows in the neighborhood, and the second element is the number of columns in
the neighborhood.

### **Output size** — Output sizing method `Same as input port I` (default) | `Valid`

Specify the output sizing method as one of these options.

- `Same as input port I` — The block computes the
  neighborhood median for the entire image, using padding to compute the boundary
  pixels. The output image has the same dimensions as the input image. Selecting
  this option enables the **Padding options** parameter.
- `Valid` — The block computes the median where the
  neighborhood fits within the input image without padding. For an input image of
  size *M*-by-*N* and neighborhood of size
  *X*-by-*Y*, the output image has the
  dimensions
  (`M`–`X`+1)-by-(`N`–`Y`+1).

### **Padding options** — Padding method `Symmetric` (default) | `Constant` | `Replicate` | `Circular`

Pad the image using one of these methods:

- `Constant` — Pad image with a constant value.
  Selecting this option enables the **Pad value source** parameter.
  For more information, see Pad with Constant Value.
- `Replicate` — Pad the image by repeating the border
  values of the input image. For more information, see Pad by Repeating Border Values.
- `Symmetric` — Pad the image using a mirror image of
  the input data. For more information, see Pad with Mirror Image
- `Circular` — Pad the image using a circular
  repetition of the elements in the input image. For more information, see Pad Using Circular Repetition of Elements.

#### Dependencies

To enable this parameter, set the **Output size** parameter to
`Same as input port I`.

### **Pad value source** — Source of constant padding value `Specify via dialog` (default) | `Input port`

Specify the padding source as `Specify via dialog` or
`Input port`.

- `Specify via dialog` — Specify a padding value using
  the **Pad value** parameter.
- `Input port` — Specify a padding value using the
  **PVal** input port.

#### Dependencies

To enable this parameter, set the **Output size** parameter to
`Same as input port I`, and set the **Padding
options** parameter to `Constant`.

### **Pad value** — Pad value `0` (default) | scalar

Specify a scalar value with which to pad the image.

#### Dependencies

To enable this port:

- Set the **Output size** parameter to `Same as
  input port I`.
- Set the **Padding options** parameter to
  `Constant`.
- Set the **Pad value source** parameter to
  `Specify via dialog`.
## Libraries

Computer Vision Toolbox / Analysis & Enhancement Computer Vision Toolbox / Filtering

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Perform 2-D median filtering

The Median Filter block applies a median filter to each pixel of an input
image. For each *M*-by-*N* neighborhood, the filter replaces
the central value with the median value of the neighborhood. If the neighborhood has a center
element, the block replaces the center pixel with the median value, as shown in this
figure.

If the neighborhood does not have an exact center, then the block has a bias toward the
upper-left corner of the neighborhood. In this figure, the median value has been placed in the
top-left pixel of the four pixels that meet at the center of the neighborhood.

The block pads the edges of the input image for filtering. This causes the pixels within
*M/2* pixels of the sides and *N/2* pixels of the top or
bottom of the image to appear distorted.

The median value is less sensitive than the mean to extreme values. Thus, Median
Filter is effective for removing salt-and-pepper noise from an image without
significantly reducing the sharpness of the image.
