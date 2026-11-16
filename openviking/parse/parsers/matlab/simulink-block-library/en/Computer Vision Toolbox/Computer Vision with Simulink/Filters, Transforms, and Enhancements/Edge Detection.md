---
type: simulink-block
title: 'Edge Detection'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'edgedetection'
documentation_source_path: 'ref/edgedetection.html'
language: en
---

# Edge Detection

## Ports

### Input

### **I** — Input image matrix

Input image, specified as a matrix of intensity values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

**Note**

The Canny method does not support 8-bit, 16-bit, or 32-bit signed fixed-point integers
or 8-bit, 16-bit, or 32-bit unsigned integers.

### **Th** — Threshold scalar | vector

Specify a threshold as a scalar or a two-element vector to detect edges from the
gradient. The data type of this value must match the input image data type. For the
Canny edge detection method, the threshold must be a two-element vector in the range
[0 1]. For the other methods, the threshold is a scalar.

#### Dependencies

To enable this port:

- Set the **Method** parameter to
  `Canny`. Alternatively, set the
  **Method** parameter to `Sobel`,
  `Prewitt`, or `Roberts`,
  and also set the **Output type** parameter to
  `Binary image` or `Binary image and
  gradient components`.
- Select the **User-defined threshold**.
- Set the **Threshold source** parameter to
  `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

**Note**

The Canny method does not support 8-bit, 16-bit, or 32-bit signed fixed-point integers
or 8-bit, 16-bit, or 32-bit unsigned integers.
### Output

### **Edge** — Edge detections matrix

Edge detections, returned as a binary image. The pixels with the value of
`1` represent the edge pixels.

#### Dependencies

This port is always enabled when you set the **Method**
parameter to `Canny`. To enable this port for the
`Sobel`, `Prewitt`, or
`Roberts` methods, set the **Output
type** parameter to `Binary image` or
`Binary image and gradient components`.

**Data Types:** `Boolean`

### **Gv** — Gradient responses to vertical edges matrix

Matrix of gradient responses to the vertical edges.

#### Dependencies

To enable this port, set these parameters:

- **Method** — `Sobel` or
  `Prewitt`
- **Output type** — `Gradient
  components` or `Binary image and gradient
  components`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Gh** — Gradient responses to horizontal edges matrix

Matrix of gradient responses to the horizontal edges.

#### Dependencies

To enable this port, set these parameters:

- **Method** — `Sobel` or
  `Prewitt`
- **Output type** — `Gradient
  components` or `Binary image and gradient
  components`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G45** — Gradient responses to edges at 45 degrees matrix

Matrix of gradient responses to edges at 45 degrees.

#### Dependencies

To enable this port, set these parameters:

- **Method** — `Roberts`
- **Output type** — `Gradient
  components` or `Binary image and gradient
  components`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G135** — Gradient responses to edges at 135 degrees matrix

Matrix of gradient responses to edges at 135 degrees.

#### Dependencies

To enable this port, set these parameters:

- **Method** — `Roberts`
- **Output type** — `Gradient
  components` or `Binary image and gradient
  components`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

**Main**

### **Method** — Edge detection method `Sobel` (default) | `Prewitt` | `Roberts` | `Canny`

Specify a method to detect edges in the input image. You can choose from
`Sobel`, `Prewitt`,
`Roberts` or `Canny`.

### **Output Type** — Output image type `Binary image` (default) | `Gradient components` | `Binary image and gradient components`

Specify the type of output image from one of these options:

- `Binary image` — The block outputs a Boolean matrix
  at the **Edge** port. The elements of the matrix labeled
  `1` represent the edge pixels.
- `Gradient components` — The block outputs the
  gradient components. For the `Sobel` and
  `Prewitt` methods, the gradient components correspond
  to the horizontal and vertical edge responses at the **Gh** and
  **Gv** ports respectively. For the
  `Roberts` method the gradient components correspond to
  45 degree and 135 degree edge responses at the **G45** and
  **G135** ports respectively.
- `Binary image and gradient components` — The block
  outputs both the binary image and the gradient components of the image

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Sobel`, `Prewitt`, or
`Roberts`.

### **User-defined threshold** — User-defined threshold off (default) | on

Specify a desired threshold value via dialog box or the **Th**
port.

#### Dependencies

This parameter is always enabled when you set the **Method**
parameter to `Canny`. To enable this parameter for the
`Sobel`, `Prewitt`, or
`Roberts` methods, set the **Output type**
parameter to `Binary image` or `Binary image and
gradient components`.

### **Threshold source** — Threshold source `Input port` (default) | `Specify via dialog`

Select the source to enter the threshold value from one of these options:

- `Input port` — Specify a threshold value using the
  **Th** port. The data type of this value must match the input
  image data type.
- `Specify via dialog` — Enter the desired threshold
  value in the dialog box.

#### Dependencies

To enable this parameter:

- Set the **Method** parameter to
  `Canny`. Alternatively set the
  **Method** parameter to `Sobel`,
  `Prewitt`, or `Roberts`, and
  also set the **Output type** parameter to `Binary
  image` or `Binary image and gradient
  components`.
- Select the **User-defined threshold**.

### **Threshold** — Threshold 20 (default) | scalar

Specify the threshold value that is within the range of your input data. This
threshold applies to Sobel, Prewitt, and Roberts edge detection methods.

#### Dependencies

To enable this parameter, set these block parameters:

- **Method** — `Sobel`,
  `Prewitt`, or
  `Roberts`
- **Output type** — `Binary image`
  or `Binary image and gradient components`
- **User-defined threshold** — `On`.
- **Threshold source** — `Specify via
  dialog`

### **Threshold, [Low High]** — Threshold for Canny edge detection [0.25 0.60] (default) | vector

Specify the threshold for the Canny edge detection as a two-element vector in the
range [0 1]. The elements of the vector specifies the low and high threshold values for
the weak and strong edges respectively.

#### Dependencies

To enable this parameter, set these block parameters:

- **Method** — `Canny`
- **User-defined threshold** — `On`.
- **Threshold source** — `Specify via
  dialog`

### **Threshold scale factor:(used to automatically calculate threshold value)** — Threshold scale factor `4` (default) | scalar

Specify the threshold scale factor to automatically calculate threshold value. The
block computes the automatic threshold using the mean of the gradient magnitude squared
image and multiplies the value of this parameter with the automatic threshold value to
determine a new threshold value.

#### Dependencies

To enable this parameter, set these block parameters:

- **Method** — `Sobel`,
  `Prewitt`, or
  `Roberts`
- **Output type** — `Binary image`
  or `Binary image and gradient components`
- **User-defined threshold** — `Off`

### **Edge Thinning** — Edge thinning `off` (default) | `on`

Select this parameter to reduce the thickness of the edges in your output images.
This option requires additional processing time and memory resources.

**Tip**

This block is most efficient in terms of memory usage and processing time when you
clear the **Edge thinning** check box and use the
**Threshold** parameter to specify a threshold value.

#### Dependencies

To enable this parameter, set these block parameters:

- **Method** — `Sobel`,
  `Prewitt`, or
  `Roberts`
- **Output type** — `Binary image`
  or `Binary image and gradient components`

### **Approximate percentage of weak edge and nonedge pixels (used to automatically calculate threshold values)** — Approximate percentage of weak edge and nonedge pixels 70 (default) | scalar

Specify the approximate percentage of weak edge and nonedge image pixels. The block
computes the automatic threshold values using this value.

#### Dependencies

To enable this parameter, set these block parameters:

- **Method** — `Canny`
- **User-defined threshold** — `Off`

### **Standard deviation of Gaussian filter** — Standard deviation of Gaussian filter 1 (default) | scalar

Specify the standard deviation of Gaussian filter used for Canny edge detection
algorithm.

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Canny`.

**Data Types**

For information about the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

When you select the **Normalized output** check box, the block input
cannot be fixed point.

## Version History

**Introduced before R2006a**

## Description

Find edges of objects in images using Sobel, Prewitt, Roberts, or Canny method

The Edge Detection block finds edges of objects in an input image. The block supports four
methods: Sobel, Prewitt, Roberts, and Canny. The first three methods find the edges by
approximating the gradient magnitude of the image. The block convolves the input matrix with
the Sobel, Prewitt, or Roberts kernel respectively, and outputs the resulting gradient
components of the image. Additionally, the block outputs a binary image of the edge detections
by thresholding the gradient magnitude.

The Canny method computes the gradient of input image using the derivative of the Gaussian
filter. It then finds edges by looking for the local maxima of the gradient. This method uses
two thresholds to detect the strong and weak edges. The weak edges are part of the output only
if they are connected to strong edges. The block outputs a binary image of the edge detections
for this method.
