---
type: simulink-block
title: 'Contrast Adjustment'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'contrastadjustment'
documentation_source_path: 'ref/contrastadjustment.html'
language: en
---

# Contrast Adjustment

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
where *C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Adjust pixel values from
  summary: Input pixel value range definition Full input data range [min max] (default) | User-defined range | Range determined
    by saturating outlier pixels
  group: Main
- name: Range [low high]
  summary: Input pixel value range [0 255] (default) | two-element vector of nonnegative numbers
  group: Main
- name: Percentage of pixels to saturate [low high]
  summary: Maximum percentages of pixels to saturate [1 1] (default) | two-element vector of nonnegative numbers
  group: Main
- name: Specify number of histogram bins (used to calculate the range when outliers are eliminated)
  summary: Custom number of histogram bins on (default) | off
  group: Main
- name: Number of histogram bins
  summary: Number of histogram bins 256 (default) | positive integer
  group: Main
- name: Adjust pixel values to
  summary: Output pixel value range definition Full data type range (default) | User-defined range
  group: Main
- name: Range [low high]
  summary: Output pixel value range [0 255] (default) | two-element vector of nonnegative numbers
  group: Main
- name: Lock data type settings against change by the fixed-point tools
  summary: Data type override off (default) | on
  group: Data Types
```

### Main

### **Adjust pixel values from** — Input pixel value range definition `Full input data range [min max]` (default) | `User-defined range` | `Range determined by saturating outlier pixels`

Specify how the block determines the pixel value range of the input image as one
of these options:

- `Full input data range [min max]` — Range set to
  the minimum and maximum pixel values in the input image.
- `User-defined range` — Select this value to enable
  a **Range [low high]** parameter. Specify the **Range
  [low high]** parameter as a two-element vector of nonnegative values,
  in which the first element is the lower limit of the input pixel value range and
  the second element is the upper limit of the input pixel value range.
- `Range determined by saturating outlier pixels` —
  Range specified by saturating the outlier pixels. The block determines the range
  based on the **Percentage of pixels to saturate [low high]**,
  **Specify number of histogram bins (used to calculate the range when
  outliers are eliminated)**, and **Number of histogram
  bins** parameters. For more information, see Determine Contrast Adjustment Range by Saturating Outlier Pixels.

### **Range [low high]** — Input pixel value range `[0 255]` (default) | two-element vector of nonnegative numbers

Specify the input pixel value range as a two-element vector of nonnegative
numbers. The first and second elements of the vector specify the lower and upper limit
of the input pixel value range, respectively.

#### Dependencies

To enable this parameter, set the **Adjust pixel values from**
parameter to `User-defined`.

### **Percentage of pixels to saturate [low high]** — Maximum percentages of pixels to saturate `[1 1]` (default) | two-element vector of nonnegative numbers

Specify the maximum percentages of pixels to saturate as a two-element vector of
nonnegative numbers. Each element must be in the range 0 to 100. The block calculates
the lower limit of the input pixel value range such that the percentage of pixels in
the input image with values less than the lower limit is at most the value of the
first element. Similarly, the block calculates the upper limit of the input pixel
value range such that the percentage of pixels in the input image with values greater
than the upper limit is at most the value of the second element.

#### Dependencies

To enable this parameter, set the **Adjust pixel values from**
parameter to `Range determined by saturating outlier
pixels`.

### **Specify number of histogram bins (used to calculate the range when outliers are eliminated)** — Custom number of histogram bins `on` (default) | `off`

Select this parameter to enable the **Number of histogram bins**
parameter, which enables you to specify a custom number of histogram bins for the
block to use to calculate the input pixel value range after outliers are
eliminated.

#### Dependencies

To enable this parameter, set the **Adjust pixel values from**
parameter to `Range determined by saturating outlier
pixels`.

### **Number of histogram bins** — Number of histogram bins `256` (default) | positive integer

Specify the number of histogram bins to use to calculate the range for scaling the
input pixel values.

#### Dependencies

To enable this parameter, set the **Adjust pixel values from**
parameter to `Range determined by saturating outlier
pixels`, and select the **Specify number of histogram bins
(used to calculate the range when outliers are eliminated)**
parameter.

### **Adjust pixel values to** — Output pixel value range definition `Full data type range` (default) | `User-defined range`

Specify how the block determines the pixel value range of the output image as one
of these options:

- `Full data type range` — Specifies the output range
  of pixel values as from the minimum to the maximum value of the input data
  type.
- `User-defined range` — Select this value to enable
  a **Range [low high]** parameter. Specify the **Range
  [low high]** parameter as a two-element vector of nonnegative values,
  in which the first element is the lower limit of the output pixel value range
  and the second element is the upper limit of the output pixel value
  range.

### **Range [low high]** — Output pixel value range `[0 255]` (default) | two-element vector of nonnegative numbers

Specify the output pixel value range as a two-element vector of nonnegative
numbers. The first and second elements of the vector specify the lower and upper limit
of the output pixel value range, respectively.

#### Dependencies

To enable this parameter, set the **Adjust pixel values to**
parameter to `User-defined range`.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Analysis & Enhancement

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006b**

## Description

Adjust image contrast using linear scaling

The Contrast Adjustment block adjusts the contrast of an image by linearly
scaling the pixel values between specified upper and lower limits. Pixel values that are above
or below the specified range are saturated to the upper or lower limit value, respectively.
For more information, see Adjust Contrast of Image.
