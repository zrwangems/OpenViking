---
type: simulink-block
title: 'Image To Matrix'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'imagetomatrix'
documentation_source_path: 'ref/imagetomatrix.html'
language: en
---

# Image To Matrix

## Ports

### Input

### **Port\_1** — Input signal `Simulink.ImageType`

Input signal to the Image To Matrix block. The input is a Simulink
image data type.

**Data Types:** `Simulink.ImageType`
### Output

### **Port\_1** — Output signal matrix

Output signal from the Image To Matrix block. The output is a
matrix or an array, depending on the format of the input.

- *M*-by-*N* matrix — The input is a
  `Grayscale` image. *M* and
  *N* are the height and width of the image, in pixels.
- *M*-by-*N*-by-*C* matrix
  — The input is an `RGB` or `BGR` image.
  *M* and *N* are the height and width of the
  image, in pixels. *C* is the number of color channels.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `single` | `double`

## Parameters

### **Rows** — Number of rows in image data `'480'` (default) | positive integer

Specify the number of rows in the image data as a positive integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Rows` |
| **Type:** `double` |
| **Value:** positive integer |
| **Default:** `'480'` |

### **Columns** — Number of columns in image data `'640'` (default) | positive integer

Specify the number of columns in the image data as a positive integer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Columns` |
| **Type:** `double` |
| **Value:** positive integer |
| **Default:** `'640'` |

### **Channels** — Number of color channels or samples for each pixel `3` (default) | `1`

Specify the number of color channels or samples for each pixel in the array as
`1` or `3`. The number of channels must correspond
to the number of color channels in the color format of the image data. These are the
values of **Channels** for the supported color formats:

| Color Format | Channels |
| --- | --- |
| `Grayscale` | `1` |
| `RGB` | `3` |
| `BGR` | `3` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Channels` |
| **Type:** `double` |
| **Value:** positive integer |
| **Default:** `'3'` |

## Libraries

Computer Vision Toolbox OpenCV Interface for Simulink

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` | `uint8` | `uint16` | `int8` | `int16` | `int32` | `image` |
| **Direct Feedthrough** | `Yes` |
| **Multidimensional Signals** | `Yes` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports C++ code generation.

## Version History

**Introduced in R2021b**

## Description

Converts Simulink image data to matrix data

The Image To Matrix block converts Simulink® image data to matrix data.
