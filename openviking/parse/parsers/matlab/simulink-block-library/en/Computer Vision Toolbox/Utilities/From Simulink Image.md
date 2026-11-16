---
type: simulink-block
title: 'From Simulink Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'fromsimulinkimage'
documentation_source_path: 'ref/fromsimulinkimage.html'
language: en
---

# From Simulink Image

## Ports

### Input

### **Port\_1** — Input signal `Simulink.ImageType`

Input signal to the From Simulink Image block. The input is a Simulink image data
type.

**Data Types:** `Simulink.ImageType`
### Output

### **Port\_1** — Output signal matrix

Output signal from the From Simulink Image block. The output is a matrix or an array,
depending on the format of the input.

- *M*-by-*N* matrix — The input is a
  `Grayscale` image. *M* and
  *N* are the height and width of the image, in pixels.
- *M*-by-*N*-by-*C* matrix
  — The input is an `RGB` or `BGR` image.
  *M* and *N* are the height and width of the
  image, in pixels. *C* is the number of color channels.

**Data Types:** `integer` | `single` | `double` | `Boolean`

## Parameters

### **Output dimensions** — Dimensions of block output signal `[480 640 3]` (default)

Specify the dimensions of the output image signal. The expression must be a
three-element numeric row vector of form: `[Rows Columns
Channels]`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImageSize` |
| **Type:** character vector |
| **Value:** character vector |
| **Default:** `[480 640 3]` |

## Libraries

Computer Vision Toolbox / Utilities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` | `integer` | `Boolean` | `image` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports C++ code generation.

## Version History

**Introduced in R2022a**

## Description

Unpack numeric matrix from Simulink image

The From Simulink Image block converts Simulink® image data to matrix data.
