---
type: simulink-block
title: 'Autothreshold'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'autothreshold'
documentation_source_path: 'ref/autothreshold.html'
language: en
---

# Autothreshold

## Ports
```yaml
ports:
- name: I
  summary: Input image matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: BW
  summary: Output binary image matrix
  direction: output
  data_types: Boolean
- name: Th
  summary: Threshold value scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: EMetric
  summary: Effectiveness metric value scalar
  direction: output
  data_types: single | double
```

### Input

### **I** — Input image matrix

Input image, specified as an *M*-by-*N*
matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **BW** — Output binary image matrix

Output binary image, returned as an *M*-by-*N*
matrix.

**Data Types:** `Boolean`

### **Th** — Threshold value scalar

Threshold value used to convert the intensity image to a binary image, returned as
a scalar.

The block calculates the threshold value using Otsu's method. The block computes
this value by splitting the histogram of the input image such that the variance of
each pixel group is minimized.

#### Dependencies

To enable this port, select the **Output threshold**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **EMetric** — Effectiveness metric value scalar

Effectiveness metric value, returned as a scalar in the range [0, 1].

If all the pixel values of the input image are the same, the value of the
effectiveness metric is `0`. If the image has two unique pixels, or
if the histogram of the image is symmetric, the value of the effectiveness metric is
`1`.

#### Dependencies

To enable this port, select the **Output effectiveness metric**
parameter.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Thresholding operator
  summary: Specify thresholding operator > (default) | <=
  group: Main
- name: Output threshold
  summary: Output threshold off (default) | on
  group: Main
- name: Output effectiveness metric
  summary: Output effectiveness metric off (default) | on
  group: Main
- name: Specify data range
  summary: Specify input pixel value range off (default) | on
  group: Main
- name: Minimum value of input
  summary: Minimum input pixel value 0 (default) | scalar
  group: Main
- name: Maximum value of input
  summary: Maximum input pixel value 255 (default) | scalar
  group: Main
- name: When data range is exceeded
  summary: Operation to perform when data range is exceeded Ignore (default) | Saturate | Warn and saturate | Error
  group: Main
- name: Scale threshold
  summary: Specify scale threshold off (default) | on
  group: Main
- name: Threshold scaling factor
  summary: Scale factor for thresholding 1 (default) | scalar
  group: Main
- name: Lock data type settings against change by the fixed-point tools
  summary: Data type override off (default) | on
  group: Data Types
```

**Main**

**Data Types**

### Main

### **Thresholding operator** — Specify thresholding operator `>` (default) | `<=`

Select whether the block includes pixels from the intensity image with values
below the threshold or those with values equal to or greater than the threshold in the
output binary image.

- `>` — For pixel values of the input image greater
  than the threshold, the block outputs `1` in the binary image.
  Otherwise, the block assigns the pixel a value of `0`.
- `<=` — For pixel values of the input image less
  than or equal to the threshold, the block outputs `1`.
  Otherwise, the block assigns the pixel a value of `0`.

### **Output threshold** — Output threshold `off` (default) | `on`

Select **Output threshold** to return the threshold value the
block uses to convert the intensity image to a binary image. Selecting this parameter
enables the **Th** output port.

### **Output effectiveness metric** — Output effectiveness metric `off` (default) | `on`

Select **Output effectiveness metric** to return the
effectiveness metric value. Selecting this parameter enables the
**EMetric** output port.

### **Specify data range** — Specify input pixel value range `off` (default) | `on`

Select **Specify data range** to enable specification of minimum
and maximum input pixel values to use to determine the threshold. Selecting this
parameter enables the **Minimum value of input**, **Maximum
value of input**, and **When data range is exceeded
parameters**.

### **Minimum value of input** — Minimum input pixel value `0` (default) | scalar

Specify the minimum value of input pixels to use to determine the
threshold.

### **Maximum value of input** — Maximum input pixel value `255` (default) | scalar

Specify the maximum value of input pixels to use to determine the
threshold.

### **When data range is exceeded** — Operation to perform when data range is exceeded `Ignore` (default) | `Saturate` | `Warn and saturate` | `Error`

Specify the behavior of the block when the value of an input image pixel exceeds
the specified data range.

- `Ignore` — The block ignores all pixels with values
  outside the specified data range.
- `Saturate` — The block saturates the pixels with
  values below the data range to the specified minimum value, and those above the
  data range to the specified maximum value.
- `Warn and saturate` — The block displays a warning
  message in the MATLAB® command window and saturates the pixel values as specified for the
  `Saturate` option.
- `Error` — The block displays an error message and
  ends the simulation.

### **Scale threshold** — Specify scale threshold `off` (default) | `on`

Select **Scale threshold** to enable specification of a scale
factor for the thresholding operation. Selecting this parameter enables the
**Threshold scaling factor** parameter.

### **Threshold scaling factor** — Scale factor for thresholding `1` (default) | scalar

Specify the scaling factor for the thresholding operation as a scalar. The block
performs thresholding by multiplying the threshold value computed by Otsu's method by
the specified scale factor.

### Data Types

For details on fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Data type override `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Conversions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Convert intensity image to binary image

The Autothreshold block converts an intensity image to a binary image using a threshold
value. This block uses Otsu's method to determine the threshold.
