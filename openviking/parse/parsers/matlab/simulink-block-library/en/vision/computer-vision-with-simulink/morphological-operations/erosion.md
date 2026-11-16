---
type: simulink-block
title: 'Erosion'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Morphological Operations'
documentation_page: 'erosion'
documentation_source_path: 'ref/erosion.html'
language: en
---

# Erosion

## Ports

### Input

### **I** — Input image matrix

Specify an input image as a matrix of binary or intensity values. This port is unnamed
until you set the **Neighborhood or structuring element
source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — Neighborhood values vector | matrix

Specify neighborhood values, representing a structuring element, as a vector or matrix
of `1`s and `0`s.

#### Dependencies

To enable this port, set the **Neighborhood or structuring
element source** parameter to `Input
port`.

**Data Types:** `Boolean`
### Output

### **Port\_1** — Eroded image matrix

Eroded image, returned as a matrix. The size and data type of the output image are the
same as those of the input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Neighborhood or structuring element source** — Source of neighborhood or structuring element `Specify via dialog` (default) | `Input port`

Specify the source of the neighborhood or structuring element as one of
these options:

- `Specify via dialog` — Use the
  **Neighborhood or structuring element**
  parameter to specify a neighborhood or structuring
  element.
- `Input port` — Use the
  **Nhood** input port to specify
  neighborhood values representing a structuring element.

### **Neighborhood or structuring element** — Neighborhood or structuring element `strel('square',4)` (default)

Specify the neighborhood or structuring element as a vector or matrix of
`1`s and `0`s, a `strel` object, or an array
of `strel` objects. When you
specify an array of `strel` objects, the block
applies each object to the entire image in sequence.

If the structuring element is decomposable into smaller elements, the
block execution speed improves due to the more efficient algorithm.

#### Dependencies

To enable this parameter, set the **Neighborhood or
structuring element source** parameter to
`Specify via dialog`.

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

Find local minima in binary or intensity image

The Erosion block slides a neighborhood or structuring element over an image, finds the
local minima, and creates an output matrix from these minimum values. If the
neighborhood or structuring element has a center element, the block places the minima
there, as shown in this figure.

Three-by-three grid with "X" over center square, representing local minima.

If the neighborhood or structuring element does not have an exact center, the block has a
bias toward the upper-left of the central elements and places the minima there, as shown
in this figure.

Four-by-four grid with "X" over the square in the second column of the second row, representing local minima.

This block uses flat structuring elements only.
