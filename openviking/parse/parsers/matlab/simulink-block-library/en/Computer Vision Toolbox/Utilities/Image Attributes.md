---
type: simulink-block
title: 'Image Attributes'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'imageattributes'
documentation_source_path: 'ref/imageattributes.html'
language: en
---

# Image Attributes

## Ports

### Input

### **Port\_1** — Input signal `Simulink.ImageType`

Input signal to the Image Attributes block. The input is a Simulink image data
type.

**Data Types:** `Simulink.ImageType`
### Output

### **rows** — Number of rows in image data scalar

Number of rows in the image data, returned as a positive integer.

**Data Types:** `uint32`

### **columns** — Number of columns in image data scalar

Number of columns in the image data, returned as a positive integer.

**Data Types:** `uint32`

### **channels** — Number of color channels or samples for each pixel in array scalar

Number of color channels or samples for each pixel in the array, returned as
`1`, `3`, or `4`. The number of
channels correspond to the number of color channels in the color format of the image
data. These are the values of `Channels` for the supported color
formats:

| Color Format | Channels |
| --- | --- |
| `Grayscale` | `1` |
| `RGB` | `3` |
| `BGR` | `3` |
| `BGRA` | `4` |

**Data Types:** `uint32`

### **class** — Data type of underlying image data string

Data type of the underlying image data, returned as one of these values:

- `'uint8'`
- `'int8'`
- `'uint16'`
- `'int16'`
- `'uint32'`
- `'int32'`
- `'single'`
- `'double'`
- `'boolean'`

**Data Types:** `string`

### **color** — Color format of underlying image data string

Color format of the underlying image data, returned as `'RGB'`,
`'Grayscale'`, `'BGR'`, or
`'BGRA'`. The color format determines what each color channel of a
pixel in the image represents.

**Data Types:** `string`

### **layout** — Array layout of image data string

Memory arrangement of the matrix data in the image, returned as
`'ColumnMajor'` or `'RowMajor'`.

**Data Types:** `string`

## Parameters

Not documented in R2025b.

## Libraries

Computer Vision Toolbox / Utilities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` | `image` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports C++ code generation.

## Version History

**Introduced in R2022b**

## Description

Output attributes of Simulink image signal

The Image Attributes block outputs attributes of Simulink image signal as numeric data. Use
Image Attributes block to:

- Display image attributes for debugging purposes.
- Use image attributes in control or data flow of an image processing
  algorithm.
