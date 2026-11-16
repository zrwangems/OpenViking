---
type: simulink-block
title: 'To Simulink Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'tosimulinkimage'
documentation_source_path: 'ref/tosimulinkimage.html'
language: en
---

# To Simulink Image

## Ports

### Input

### **Port\_1** — Input signal matrix

Input signal to the To Simulink Image block. The input is a numerical matrix.

**Data Types:** `integer` | `single` | `double` | `Boolean`
### Output

### **Port\_1** — Output signal `Simulink.ImageType`

Output signal from the To Simulink Image block. The output is an image of
`Simulink.ImageType` data type.

**Data Types:** `Simulink.ImageType`

## Parameters

### **Output data type** — Data type of output signal values `Inherit: auto` (default) | `Simulink.ImageType(480,640,3)`

Specify the output data type of the image signal.

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

You can specify any of these options:

- Inherited data type
- Simulink image data type — Use the constructor for `Simulink.ImageType` object and specify the properties to describe the
  image. By default, the data type uses
  `Simulink.ImageType(480,640,3)` expression.
- Custom data type — Use a MATLAB® expression that represents the rows, columns, and channels of the
  image respectively.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Value:** `Inherit: auto` | `Simulink.ImageType(480,640,3)` | `<data type expression>` |
| **Default:** `Inherit: auto` |

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

Pack numeric matrix into a Simulink image

The To Simulink Image block converts matrix data to Simulink® image data.
