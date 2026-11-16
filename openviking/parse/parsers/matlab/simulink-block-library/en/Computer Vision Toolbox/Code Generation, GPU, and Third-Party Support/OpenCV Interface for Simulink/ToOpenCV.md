---
type: simulink-block
title: 'ToOpenCV'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'toopencv'
documentation_source_path: 'ref/toopencv.html'
language: en
---

# ToOpenCV

## Ports

### Inputs

### **Port\_1** — Input signal scalar | vector | matrix | simulink bus | simulink image

Input signal to the ToOpenCV block. The input can be of
different data types. Each of the input data types determines the output
data type of the block.

**Data Types:** `uint8` | `uint16` | `int8` | `int16` | `int32` | `single` | `double` | `Simulink.ImageType` | `CV_DMATCH_BUS` | `CV_RECT_BUS` | `CV_ROTATEDRECT_BUS` | `CV_TERMCRITERIA_BUS` | `CV_SIZE_BUS` | `CV_RANGE_BUS` | `CV_POINT2I_BUS` | `CV_POINT2F_BUS` | `CV_POINT2D_BUS` | `CV_POINT3I_BUS` | `CV_POINT3F_BUS` | `CV_POINT3D_BUS`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | simulink bus | simulink image

Output signal from the ToOpenCV block. The output
signal supports OpenCV types. For more information, see Mapping Input and
Output Data Types.

**Data Types:** `OpenCV types`

## Parameters

### **DataType** — Data type of the Input signal of ToOpenCV block `input data type` (default)

Specifies the input data type of the ToOpenCV block. The
table lists the
one-to-one mapping of the input versus output data types of the
ToOpenCV block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Type:** character vector |
| **Value:** input data type |
| **Default:** `'Point2i'` |

## Libraries

Computer Vision Toolbox Interface for OpenCV in Simulink

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `Yes` |
| **Multidimensional Signals** | `Yes` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports C++ code generation.

## Version History

**Introduced in R2020a**

## Description

Converts Simulink data types to OpenCV data types

The ToOpenCV block converts the Simulink® data types to Simulink OpenCV data types.
