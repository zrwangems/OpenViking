---
type: simulink-block
title: 'Label'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'label'
documentation_source_path: 'ref/label.html'
language: en
---

# Label

## Ports

### Input

### **BW** — Input binary image vector | matrix

The input image must be a vector or matrix of binary values, each element
representing a pixel of the image. The block categorizes pixels with a value of
`0` as background pixels, searching for connected components within
pixels with a value of `1`.

**Data Types:** `Boolean`
### Output

### **Label** — Labeled objects vector | matrix

Labeled objects in the input image, returned as a vector or matrix of nonnegative
integers. The elements of the output vector or matrix labeled `0`
represent the background, the elements labeled `1` represent the
first object, the elements labeled `2` represent the second object,
and so on. The size of this output matches the size of the **BW**
input.

#### Dependencies

To enable this port, set the **Output** parameter to either
`Label matrix` or `Label matrix and number of
labels`.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Count** — Number of labeled objects scalar

Number of labeled objects, returned as a scalar.

#### Dependencies

To enable this port, set the **Output** parameter to either
`Number of labels` or `Label matrix and
number of labels`.

**Data Types:** `uint8` | `uint16` | `uint32`

## Parameters

### **Connectivity** — Type of pixel connectivity `8` (default) | `4`

Specify how the block defines which pixels are connected to each other. If you want
to connect adjacent pixels in only the horizontal and vertical directions, select
`4`. If you want to connect adjacent pixels in the horizontal,
vertical, and diagonal directions, select `8`. These figures show how
the block defines a connected component for 4-connected and 8-connected pixels. The
block considers the white pixels marked by black circles to be connected to each other.

| Type of Connectivity | Connected Pixels |
| --- | --- |
| 4-connected pixels | Three-by-three grid, with the middle-left, center, and middle-bottom squares white with black circles in the center. The top-right square is white with no circle, and all other squares are black. |
| 8-connected pixels | Three-by-three grid, with the middle-left, center, middle-bottom, and top-right squares white with black circles in the center. All other squares are black. |

### **Output** — Block output `Label matrix and number of labels` (default) | `Label matrix` | `Number of labels`

Specify the block output as one of these options:

- `Label matrix` — The block outputs the labeled
  objects at the **Label** port.
- `Number of labels` — The block outputs the number of
  labeled objects at the **Count** port.
- `Label matrix and number of labels` — The block
  outputs both the labeled objects and number of labeled objects to the
  **Label** and **Count** ports,
  respectively.

### **Output data type** — Data type of output `Automatic` (default) | `uint8` | `uint16` | `uint32`

Specify the data type of the outputs at the **Label** and
**Count** ports. When you specify this parameter as
`Automatic`, the block calculates the maximum number of
objects that can fit inside the image based on the image size and the specified
connectivity. Using this calculation, it chooses the output data type with the minimum
value that guarantees unique region labels.

### **If label exceeds data type size, mark remaining regions using** — Overflow mode of output labels `maximum value of the output data type` (default) | `zero`

Use this parameter to specify the behavior of the block when the block finds more
objects than the maximum possible value the output data type can represent. The block
labels the remaining objects with the value determined by one of these options:

- `maximum value of the output data type` — The block
  labels the remaining objects with the maximum value of the output data
  type.
- `zero` — The block labels the remaining objects with
  `0`.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to either `uint8` or
`uint16`.

## Libraries

Computer Vision Toolbox / Morphological Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Label connected components in binary image

The Label block finds and labels the connected components or objects in a 2-D binary
image. The block ignores the background pixels in the input image and searches for connected
components within remaining pixels. The block then labels all the pixels of each connected
component with a unique number and computes the number of labeled objects.
