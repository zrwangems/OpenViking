---
type: simulink-block
title: 'Opening'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'opening'
documentation_source_path: 'ref/opening.html'
language: en
---

# Opening

## Ports
```yaml
ports:
- name: I
  summary: Input image matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Nhood
  summary: Neighborhood values vector | matrix
  direction: input
  data_types: Boolean
- name: Port_1
  summary: Opened image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Input

### **I** — Input image matrix

Specify an input image as a matrix of intensity values. This port is unnamed
unless you set the **Neighborhood or structuring element source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — Neighborhood values vector | matrix

Specify neighborhood values representing a structuring element as a vector or
matrix of `1`s and `0`s or by using the `strel` function.

#### Dependencies

To enable this port, set the **Neighborhood or structuring element
source** parameter to `Input port`.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Opened image matrix

The opened image is returned as a matrix of intensity values. The size and data
type of the opened image are the same as those of the input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Neighborhood or structuring element source
  summary: Source of neighborhood or structuring element Specify via dialog (default) | Input port
  group: ''
- name: Neighborhood or structuring element
  summary: Neighborhood or structuring element strel('disk',5) (default) | vector | matrix
  group: ''
```

### **Neighborhood or structuring element source** — Source of neighborhood or structuring element `Specify via dialog` (default) | `Input port`

Specify the source of neighborhood or structuring element as one of these options:

- `Specify via dialog` — Use the **Neighborhood
  or structuring element** parameter to specify a neighborhood or
  structuring element.
- `Input port` — Use the **Nhood**
  input port to specify neighborhood values representing a structuring
  element.

### **Neighborhood or structuring element** — Neighborhood or structuring element `strel('disk',5)` (default) | vector | matrix

Specify neighborhood or structuring element as a vector or matrix of
`1`s and `0`s, a `strel` object or an array of `strel` objects. When you specify this value as an array of `strel` objects, the block applies each object to the entire image in
turn.

If the structuring element is decomposable into smaller elements, the block executes
at higher speed due to the use of a more efficient algorithm.

#### Dependencies

To enable this parameter, set the **Neighborhood or structuring element
source** parameter, to `Specify via
dialog`.
## Libraries

Computer Vision Toolbox / Morphological Operations

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

Perform morphological opening on binary or intensity images

The Opening block performs an erosion operation followed by a dilation
operation on an intensity or binary image using a predefined neighborhood or structuring
element.

To define the structuring element that the block applies to the image, use the
**Neighborhood or structuring element** parameter. Specify this element by
entering a vector or matrix of `1`s and `0`s or by using the
`strel` function.

Below are an input image and the output image after the opening operation,
respectively.

This block uses two-dimensional flat structuring elements only.
