---
type: simulink-block
title: 'Gamma Correction'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Color Space Formatting and Conversions'
documentation_page: 'gammacorrection'
documentation_source_path: 'ref/gammacorrection.html'
language: en
---

# Gamma Correction

## Ports

### Input

### **I** — Input image matrix | array

Input image, specified as an *M*-by-*N* matrix
or an *M*-by-*N*-by-*C* array,
where *C* is the number of color channels in the input image.

#### Dependencies

To enable this port, set the **Operation** parameter to
`Gamma`.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **I'** — Gamma-corrected input image matrix | array

Gamma-corrected input image, specified as an
*M*-by-*N* matrix or an
*M*-by-*N*-by-*C* array, where
*C* is the number of color channels in the input image.

#### Dependencies

To enable this port, set the **Operation** parameter to
`De-gamma`.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
### Output

### **I'** — Gamma-corrected output image matrix | array

Gamma-corrected output image, returned as an
*M*-by-*N* matrix or an
*M*-by-*N*-by-*C* array, where
*C* is the number of color channels.

#### Dependencies

To enable this port, set the **Operation** parameter to
`Gamma`.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **I** — Gamma-removed output image matrix | array

Gamma-removed output image, returned as an
*M*-by-*N* matrix or an
*M*-by-*N*-by-*C* array, where
*C* is the number of color channels.

#### Dependencies

To enable this port, set the **Operation** parameter to
`De-gamma`.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

## Parameters

### **Operation** — Block operation `Gamma` (default) | `De-gamma`

Specify the gamma operation the block performs.

- `Gamma` — Apply gamma correction to the input
  image.
- `De-gamma` — Remove gamma correction from the input
  image.

### **Gamma** — Gamma value `2.2` (default) | scalar

Specify the gamma as a value greater than or equal to 1. A value less than 1 encodes
luminance values in image and a value greater than 1 decodes luminance values in image,
represented as gamma compression and gamma expansion respectively.

### **Linear segment** — Linear segment `on` (default) | `off`

Select this parameter to define the gamma curve as a linear segment near the origin.
For more information, see Gamma Correction Method.

### **Break point** — Break point value `0.018` (default) | scalar

Specify a scalar break point value, which indicates the *I*-axis
value at the end of the gamma curve linear segment. For more information, see Gamma Correction Method.

#### Dependencies

To enable this parameter, select the **Linear segment**
parameter.

## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `integera` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Supports word lengths less than or equal to 16 bits. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Apply or remove gamma correction to or from image or video stream

The Gamma Correction block applies or removes gamma correction to or from
an image or video stream.
