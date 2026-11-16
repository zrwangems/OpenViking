---
type: simulink-block
title: '2-D Variance'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dvariance'
documentation_source_path: 'ref/2dvariance.html'
language: en
---

# 2-D Variance

## Ports

### Input

### **In** — Input array vector | matrix | array

Input array, specified as a vector, matrix, or *N-D*- array. This
port is unnamed until you select the **Enable ROI processing**
parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**Complex Number Support:** Yes

### **Rst** — Reset port scalar

Reset port, specified as a scalar. This port specifies the event that causes the
block to reset the running variance. The sample time of the **Rst**
input must be a positive integer and a multiple of the input sample time.

#### Dependencies

To enable this port, select the **Running variance** parameter
and set the **Reset port** parameter to `Rising
edge`, `Falling edge`, `Either
edge`, or `Non-zero sample`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — Region of interest vector | matrix

Region of interest (ROI), specified as a four-element vector,
*m*-by-4 matrix, or *M*-by-*N*
matrix. The input value to this port depends on the **ROI type** parameter.

**Note**

You can use the `ROI` port only if the input is a 2-D
image.

#### Dependencies

To enable this port, set the **Find the variance value over**
parameter to `Entire input` and select the **Enable
ROI processing** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Label** — Label matrix matrix

Label matrix, specified as a matrix of nonnegative integers. The label matrix
represents the objects in an image. The pixels labeled 0 are the background. The
pixels labeled 1 make up one object; the pixels labeled 2 make up a second object; and
so on. The size of the label matrix must be the same size as the 2-D input.

#### Dependencies

To enable this port, select the **Enable ROI processing**
parameter and set the **ROI type** parameter to
`Label matrix`.

**Data Types:** `uint8` | `uint16` | `uint32`

### **Label Numbers** — Label values of ROIs vector

Label values of ROIs, specified as a *M*-element vector. The
value of *M* can be less than or equal to the number of objects that
are labeled in the label matrix.

#### Dependencies

To enable this port, select the **Enable ROI processing**
parameter and set the **ROI type** parameter to
`Label matrix`.

**Data Types:** `uint8` | `uint16` | `uint32`
### Output

### **Out** — Computed output variance scalar | vector | matrix | *N-D*-array

Computed output variance, returned as a scalar, vector, matrix, or
*N-D*-array. The size of the returned output variance depends on
the size of the input, and the settings for the **Running
variance** and **Find the variance value
over** parameters.

This port is unnamed until you select the **Output flag indicating if ROI
is within image bounds** and the **ROI type** parameter is
set to `Rectangles`, `Lines`, or
`Label matrix`.

#### If **Running variance** Is Cleared

You can compute variance along any specified dimension of the input or the
entire input. The output is a:

- Scalar if the input is of any size and the **Find the
  variance value over** parameter is set to `Entire
  input`.
- Vector if the input is a matrix and the **Find the
  variance value over** parameter is set to any one of
  `Each row`, `Each column`,
  and `Specified dimension`. In this case, the
  **Dimension** value for `Specified
  dimension` can be either 1 or 2.
- Matrix if the input is a 3-D array and the **Find the
  variance value over** parameter is set to `Specified
  dimension` and the **Dimension** value is
  3.
- *N-D* array if the input is an *N-D* array
  and the **Find the variance value over** parameter
  is set to an option other than `Entire input`.

  If you compute variance along the *N*th dimension of the
  input, then the returned output is an *(N-1)-D* array. In this
  case, the **Dimension** value for `Specified
  dimension` is set to *N*.

  **Example:** For a 3-D input array of size
  *M*-by-*N*-by-*P*, the
  dimension of the returned output is:

  - 1-by-*N*-by-*P* if you set the
    **Find the variance value over** parameter
    to `Entire row`.
  - *M*-by-1-by-*P* if you set the
    **Find the variance value over** parameter
    to `Entire column`.
  - *M*-by-*N* if you set the **Find the variance value over** parameter to
    `Specified dimension` and the
    **Dimension** value to 3.

#### If **Running variance** Is Selected

When you select the **Running variance** parameter,
the block computes the variance of each sample in the input with respect to all
previous samples. The output is of the same size as the input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Flag** — Validation for ROI `0` | `1`

Validation for ROI, returned as 0 or 1. The output value signifies if all of the
ROIs specified at the input lie within the image bounds. The output value depends on
the values of the **Output** and **ROI Type**
parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **ROI Type** | **Output** | **Output from Flag port** | **Description** |
| - `Rectangles` - `Lines` | `Individual statistics for each ROI` | 0 | ROI is completely outside the input image. |
| 1 | ROI is either completely or partially inside the input image. |
| `Single statistic for all ROIs` | 0 | ROI is completely outside the input image. |
| 1 | ROI is either completely or partially inside the input image. |
| `Label matrix` | `Individual statistics for each ROI` | 0 | Label number is not in the label matrix. |
| 1 | Label number is in the label matrix. |
| `Single statistic for all ROIs` | 0 | None of the label numbers are in the label matrix. |
| 1 | At least one of the label numbers is in the label matrix. |

**Note**

If the ROI is partially outside the image, the block computes the variance
values only for the portion of the ROI that lies within the image bounds.

#### Dependencies

To enable this port, select the **Output flag indicating if ROI is
within image bounds** parameter and set the value of **ROI
type** parameter to `Rectangle`,
`Lines`, or `Label
Matrix`.

## Parameters

### Main

### **Running variance** — Track running variance `off` (default) | `on`

Select to track the variance of successive inputs to the block. In this mode, the
block treats each element as a channel.

### **Reset port** — Reset event `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

Specify when the block detects a reset event. The block resets the running
variance when a reset event is detected at the optional **Rst** port. The reset sample time must be a positive integer and a
multiple of the input sample time.

Specify the reset event as:

- `None` to disable the **Rst** port.
- `Rising edge` to trigger a reset event when the
  **Rst** input does one of the following:

  - Rises from a negative value to either a positive value or zero
  - Rises from zero to a positive value, where the rise is not a continuation
    of a rise from a negative value to zero
- `Falling edge` to trigger a reset event when the
  **Rst** input does one of the following:

  - Falls from a positive value to either a negative value or zero
  - Falls from zero to a negative value, where the fall is not a continuation
    of a fall from a positive value to zero

- `Either edge` to trigger a reset event when
  the **Rst** input is a `Rising
  edge` or `Falling edge`.
- `Non-zero sample` to trigger a reset event at each
  sample time, when the **Rst** input is not
  zero.

  **Note**

  When running simulations in the Simulink® multitasking mode, reset signals have a one-sample latency.
  Therefore, when the block detects a reset event, there is a one-sample delay at
  the reset port rate before the block applies the reset.

#### Dependencies

To enable this parameter, select the **Running variance**
parameter.

### **Find the variance value over** — Dimension along which variance is computed `Entire input` (default) | `Each row` | `Each column` | `Specified dimension`

Specify the dimension of the input along which the block computes the variance.

- `Entire input` — Computes variance over the
  entire input.
- `Each row` — Computes variance over each
  row.
- `Each column` — Computes variance over each
  column.
- `Specified dimension`— Computes variance
  over the dimension specified in the **Dimension** parameter.

  - If **Dimension** is 1, the output is the same
    as when you select `Each column`.
  - If **Dimension** is 2, the output is the same
    as when you select `Each row`.

#### Dependencies

To enable this parameter, clear the **Running variance**
parameter.

### **Dimension** — Custom dimension `1` (default) | scalar

Specify the dimension of the input array over which the variance is computed as a
one-based value. The value of this parameter must be greater than 0 and less than or
equal to the number of dimensions in the input array.

#### Dependencies

To enable this parameter, set the **Find the variance value
over** parameter to `Specified
dimension`.

**ROI Processing**

### **Enable ROI processing** — Compute variance within a particular region `off` (default) | `on`

Select to calculate variance within a particular ROI in the image.

**Note**

Full ROI processing is available only if you have a Computer Vision Toolbox™ license. If you do not have a Computer Vision Toolbox license, you can still use ROI processing, but the **ROI
type** is limited to `Rectangles`.

#### Dependencies

To enable this parameter, set the **Find the variance value
over** parameter to `Entire input`.

### **ROI type** — Type of ROI `Rectangles` (default) | `Lines` | `Label matrix` | `Binary mask`

Specify the type of ROI that represents the regions in the image over which the
block computes the variance. The type of ROI can be a rectangle, line, label matrix,
or a binary mask.

|  |  |  |
| --- | --- | --- |
| **Parameters** | | **Description** |
| **ROI type** | **Inputs to the ROI port** |
| `Rectangles` | - Four-element row vector    `[x y width   height]` - *m*-by-4 matrix  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ,  where *m* is the number of rectangles. Each row   of the matrix corresponds to a different rectangle. | - `x` and `y` are the one-based   coordinates of the upper left corner of the rectangle. - `width` and `height` are the   width and height, in pixels, of the rectangle. The values of   `width` and `height` must be   greater than 0. |
| `Lines` | - Four-element row   vector    `[x1   y1 x2   y2]` - *m*-by-4 matrix    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ,  where *m* is the number of lines. Each row of the   matrix corresponds to a different line. | - `x1` and   `y1` are the coordinates   of the beginning of the line. - `x2` and   `y2` are the coordinates   of the end of the line. |
| `Label matrix` | *M*-by-*N* matrix | Matrix of the same size as the input image. The matrix contains label values that represent different objects in an image. The pixels labeled 0 are the background. The pixels labeled 1 make up one object; the pixels labeled 2 make up a second object; and so on. |
| `Binary mask` | *M*-by-*N* matrix | Matrix of the same size as the input image. The binary mask classifies image pixels as belonging to either the region of interest or the background. The mask pixel values of 1 indicate that the image pixel belongs to the ROI. The mask pixel values of 0 indicate that the image pixel is part of the background. |

#### Dependencies

To enable this parameter, select the **Enable ROI processing**
parameter.

### **ROI portion to process** — Portion of ROI in which to calculate variance `Entire ROI` (default) | `ROI perimeter`

Specify the portion of the ROI from which the block has to calculate 2-D variance.
The ROI portion is either the entire ROI or the ROI perimeter.

#### Dependencies

To enable this parameter, select the **Enable ROI processing**
parameter and set the **ROI type** parameter to
`Rectangles`.

### **Output** — Calculate variance for individual or entire ROI `Individual statistics for each ROI` (default) | `Single statistic for all ROIs`

Specify whether to calculate 2-D variance individually for each ROI or for the
entire ROI.

- If you select `Individual statistics for each ROI`,
  the block outputs a vector of variance values. The size of the output vector is
  equal to the number of ROIs.
- If you select `Single statistic for all ROIs`, the
  block outputs a scalar value. The scalar value represents the statistical value
  for all the specified ROIs.

#### Dependencies

To enable this parameter, select the **Enable ROI processing**
parameter and set the **ROI type** parameter to
`Rectangles`, `Lines`, or
`Label matrix`.

### **Output flag indicating if ROI is within image bounds** — Enable Flag port `off` (default) | `on`

Select to expose the **Flag** port. For a description
of the **Flag** port output, see Flag.

#### Dependencies

To enable this parameter, select the **Enable ROI processing**
parameter and set the **ROI type** parameter to
`Rectangles`, `Lines`, or
`Label matrix`.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Compute variance of input or sequence of inputs

The 2-D Variance block computes the unbiased variance of an input array.
The input can be a 1-D vector, 2-D matrix, or an *N-D* array. The block can
compute variance along a specified dimension of the input or the entire input. If you select
the **Running variance** parameter, the block can also track the variance in
a sequence of inputs over a time period.
