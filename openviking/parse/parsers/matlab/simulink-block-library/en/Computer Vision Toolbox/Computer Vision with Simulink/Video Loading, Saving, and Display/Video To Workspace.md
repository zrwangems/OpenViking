---
type: simulink-block
title: 'Video To Workspace'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'videotoworkspace'
documentation_source_path: 'ref/videotoworkspace.html'
language: en
---

# Video To Workspace

## Ports

### Input

### **Image** — Input video matrix | 3-D array | 4-D array

The input image or video, specified as a matrix, `3`-D array, or
`4`-D array. The type of signal determines the dimensions of the
input. Inputs are defined in terms of *M*, *N*,
*C*, and *T*. *M* and
*N* are the number of rows and columns in the signal respectively.
*C* is the number of color channels in the signal, and
*T* is the number of frames.

**Input - Output**

| Signal Type | Input Dimensions | Output Dimensions |
| --- | --- | --- |
| Grayscale image | *M*-by-*N* | *M*-by-*N*-by-2 |
| Color image | *M*-by-*N*-by-3 | *M*-by-*N*-by-3-by-2 |
| Grayscale video | *M*-by-*N*-by-*T* | *M*-by-*N*-by-*T* |
| Color video | *M*-by-*N*-by-3-by-*T* | *M*-by-*N*-by-3-by-*T* |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — Red color channel scalar | vector | matrix

Red color channel of the input image or video, specified as a scalar, vector, or
matrix.

**Note**

The port label can be changed using the `Input port labels`
parameter.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
a value greater than or equal to `2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — Green color channel scalar | vector | matrix

Green color channel of the input image or video, specified as a scalar, vector, or
matrix.

**Note**

The port label can be changed using the `Input port labels`
parameter.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
a value greater than or equal to `2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — Blue color channel scalar | vector | matrix

Blue color component of the input image or video, specified as a scalar, vector,
or matrix.

**Note**

The port label can be changed using the `Input port labels`
parameter.

#### Dependencies

To enable this port, set the **Number of inputs** parameter to
a value equal to `3`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Variable name** — MATLAB workspace variable name `vout` (default) | valid MATLAB variable name

Specify the MATLAB workspace variable name for the exported image or video.

### **Number of inputs** — Number of inputs ports `1` (default) | positive integer

Specify the number of inputs to the block. To separate the color channels in a RBG
image or video, specify the number of channels. If it is a grayscale video, enter 1. If
it is a color (R, G, B) video, enter 3.

### **Limit data points to last** — Maximum number of frames to export `10` (default) | positive integer

Specify the maximum number of frames to export to the MATLAB workspace.

### **Decimation** — Downsample video signal `1` (default) | positive integer

Enter the decimation factor by which to downsample the image or video.

### **Log fixed-point data as a fi object** — Create fixed-point numeric object `off` (default) | `on`

Select **Log fixed-point data as a fi object** to create a fi
object in the MATLAB workspace when the input signal has a fixed point data type. For
more information on `fi` objects, see `fi` (Fixed-Point Designer).

### **Input port labels** — Input port names `R|G|B` (default)

Name the input ports using the vertical bar character as a delimiter.

#### Dependencies

To enable this parameter, set the **Number of inputs** parameter
to a value greater than `1`.

## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Export image or video to MATLAB workspace

The Video To Workspace  block exports an image or video to the MATLAB® workspace. It accepts images or videos as a matrix, 3-D array, 4-D array and
converts them to a 3-D or 4-D array. The input size determines the output size.

- *M*-by-*N*, the block exports it as an
  *M*-by-*N*-by-2 array. *M* and *N* are the number of rows and
  columns, respectively, in an image frame and 2 is the number of frames in the
  image.
- *M*-by-*N*-by-3, the block exports it as a *M*-by-*N*-by-3-by-2 array.
  *M* and *N* are the number of rows and columns in a
  image or video frame, 3 is the number of color channels, and 2 is the number of frames
  in the video.
- *M*-by-*N*-by-3-by-*T*, the block
  exports it as a *M*-by-*N*-by-3-by-*T* array. *M*
  and *N* are the number of rows and columns in a video frame, 3
  represents the number of color channels, and *T* is the
  number of frames in the video.

**Note**

- Simulink®
  Coder™ does not generate code for this block.
- The block supports grayscale and color images, which are exported to the
  MATLAB workspace with an extra dimension that represents the number of
  frames. An image is always exported with a frame value of 2.
