---
type: simulink-block
title: 'Image Data Type Conversion'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'imagedatatypeconversion'
documentation_source_path: 'ref/imagedatatypeconversion.html'
language: en
---

# Image Data Type Conversion

## Ports
```yaml
ports:
- name: I
  summary: Input image matrix | array
  direction: input
  data_types: single | double | int8 | int16 | uint8 | uint16 | Boolean | fixed point
- name: Port_1
  summary: Output image matrix | array
  direction: output
  data_types: single | double | int8 | int16 | uint8 | uint16 | Boolean | fixed point
```

### Input

### **I** — Input image matrix | array

Input image, specified as an *M*-by-*N* matrix
or an *M*-by-*N*-by-*C* array,
where *C* is the number of color channels in the input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output image matrix | array

Output image, returned as an *M*-by-*N* matrix
or an *M*-by-*N*-by-*C* array,
where *C* is the number of color channels in the output image.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Output data type
  summary: Output data type double (default) | single | int8 | uint8 | int16 | uint16 | boolean | Fixed-point | Inherit via
    back propagation
  group: ''
- name: Signed
  summary: Signed output on (default) | off
  group: ''
- name: Word length
  summary: Word length 16 (default) | scalar
  group: ''
- name: Fraction length
  summary: Fraction length 0 (default) | scalar
  group: ''
```

### **Output data type** — Output data type `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `boolean` | `Fixed-point` | `Inherit via back propagation`

Specifies the data type of your output signal.

### **Signed** — Signed output `on` (default) | `off`

Specifies the fixed-point data type of your output signal as signed.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.

### **Word length** — Word length `16` (default) | scalar

Specifies the word length of your fixed-point output.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.

### **Fraction length** — Fraction length `0` (default) | scalar

Specifies the fraction length of your fixed-point output.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.
## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integera` | `single` |
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

Convert and scale input image to specified output data type

The Image Data Type Conversion block converts the data type of the input
image to the specified data type and scales the pixel values to the dynamic range of the
output data. To convert between data types without scaling, use the Data
Type Conversion (Simulink) block.

The behavior of the block changes depending on the input and output data types of the image.

- When converting between floating-point data types, the block casts the input values
  into the output data type and clips values below or above the range of the output data
  type to `0` or `1`, respectively.
- When converting to the `Boolean` data type, the block maps
  `0` values to `0` (`false`) and all
  other values to `1` (`true`).
- Between all other data types, the block casts and scales the input data type values
  into the dynamic range of the output data type. For double- and single-precision
  floating-point data types, the dynamic range is between `0` and
  `1`. For fixed-point data types, the dynamic range is between the
  minimum and maximum pixel values of that data type.
