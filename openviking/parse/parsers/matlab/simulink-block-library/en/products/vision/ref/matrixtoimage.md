---
type: simulink-block
title: 'Matrix To Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'matrixtoimage'
documentation_source_path: 'ref/matrixtoimage.html'
language: en
---

# Matrix To Image

## Ports

### Input

### **Port\_1** — Input signal matrix

Input signal to the Matrix To Image block. The input is a numerical
matrix.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `single` | `double`
### Output

### **Port\_1** — Output signal `Simulink.ImageType`

Output signal from the Matrix To Image block. The output is an
image in `Simulink.ImageType` data type.

**Data Types:** `Simulink.ImageType`

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

### **Channels** — Number of color channels or samples for each pixel in the array `3` (default) | `1`

Specify the number of color channels or samples for each pixel in the array as
`1` or `3`. The number of channels must correspond
to the number of color channels in the color format of the image data. These are the
values of **Channels** for the supported color formats:

| Channels | Color Format |
| --- | --- |
| `1` | `Grayscale` |
| `3` | `RGB` |
| `3` | `BGR` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Columns` |
| **Type:** character vector |
| **Value:** positive integer |
| **Default:** `'3'` |

### **Underlying Datatype** — Data type of underlying image data `'uint8'` (default) | `'int8'` | `'uint16'` | `'int16'` | `'uint32'` | `'int32'` | `'single'` | `'double'` | `'logical'`

Specify the data type of the underlying image data as one of these options:

- `'uint8'`
- `'int8'`
- `'uint16'`
- `'int16'`
- `'uint32'`
- `'int32'`
- `'single'`
- `'double'`
- `'logical'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ClassUnderlying` |
| **Type:** character vector |
| **Value:** `'uint8'` | `'int8'` | `'uint16'` | `'int16'` | `'uint32'` | `'int32'` | `'single'` | `'double'` | `'logical'` |
| **Default:** `'uint8'` |

### **Array Layout** — Memory arrangement of matrix data in image `'Column-major'` (default) | `'Row-major'`

Specify the memory arrangement of the matrix data in the image as
`Column-major` or `Row-major`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layout` |
| **Type:** character vector |
| **Value:** `'Column-major'` | `'Row-major'` |
| **Default:** `'Column-major'` |

### **Color Format** — Color format of pixels in underlying image data `'RGB'` (default) | `'Grayscale'` | `'BGR'`

Specify what each color channel of a pixel represents in the underlying image data
as `Grayscale`, `RGB`, or
`BGR`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ColorFormat` |
| **Type:** character vector |
| **Value:** `'Grayscale'` | `'RGB'` | `'BGR'` |
| **Default:** `'RGB'` |

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

Converts matrix data to Simulink image data

The Matrix To Image block converts matrix data to Simulink® image data.
