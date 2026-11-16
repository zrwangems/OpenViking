---
type: simulink-block
title: 'To Video Display'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tovideodisplay'
documentation_source_path: 'ref/tovideodisplay.html'
language: en
---

# To Video Display

## Ports

### Input

### **Image** — Input image matrix | array

Input image or video, specified as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array, or
*M*-by-*N*-by-*C*-by-*T*
array. If the input is a 3-D array, the third dimension is the number of frames in the
video. If the input is a 4-D array, the third dimension is the number of color
channels, and the fourth dimension is the number of frames in the video.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `RGB`, and set **Image signal** to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — Red color component of image matrix | array

Red color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `RGB`, and set **Image signal** to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of image matrix | array

Green color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `RGB`, and set **Image signal** to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of image matrix | array

Blue color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `RGB`, and set **Image signal** to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — Luma component of image matrix | array

Luma component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — Blue-difference chroma component of image matrix | array

Blue-difference chroma component of the input image or video, specified as an
*M*-by-*N/2* matrix or
*M*-by-*N/2*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — Red-difference chroma component of image matrix | array

Red-difference chroma component of the input image or video, specified as an
*M*-by-*N/2* matrix or
*M*-by-*N/2*-by-*T* array. If the
input is a 3-D array, the third dimension is the number of frames in the video.

#### Dependencies

To enable this port, set the **Input Color Format** parameter
to `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### View

### **Window size** — Display window size `Normal` (default) | `Full-screen (Esc to exit)` | `True size (1:1)`

Display the video stream in various window sizes:

- `Normal` — Modify the display size at the start of
  the simulation.
- `Full-screen (Esc to exit)` — Display the video
  stream in a full-screen window. To exit the full-screen view, press
  **Esc**.
- `True size (1:1)` — Display the input image at a
  one-to-one pixel ratio, at the start of the simulation.

### **Open at Start of Simulation** — Open window at start of simulation `on` (default) | `off`

To set the **Video Display** window to open automatically and
display video frames when the simulation begins, select **Open at Start of
Simulation**. If you clear this parameter, the block is not included during
runtime, and the simulation runs in Accelerator Mode (Simulink).

### Settings

### **Input Color Format** — Input color format `RGB` (default) | `YCbCr 4:2:2`

Specify the color format of the input image:

- `RGB` — Specify the input colorspace as RGB. You
  can select whether to input the image as a single signal or as individual color
  signals using the **Image signal** parameter.
- `YCbCr 4:2:2`— Specify the input colorspace as
  YCbCr. You must input the image as separate signals to the three input ports,
  **Y**, **Cb** and
  **Cr**.

### **Image signal** — Configure input port `One multidimensional signal` (default) | `Separate color signals`

Specify whether the block accepts an RGB color input as a single signal or as
separate signals for each color channel..

- `One multidimensional signal` — The block accepts RGB
  input as a single array through one port.
- `Separate color signals` — The block accepts RGB
  input as three separate matrices or arrays, one for each color channel, to the
  **R**, **G**, and **B**
  ports.

#### Dependencies

To enable this parameter, set the **Input Color Format**
parameter to `RGB`.

## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

**Note**

This block supports code generation for platforms that have file I/O available. You
cannot use this block with Simulink®
Desktop Real-Time™ software, because that product does not support file I/O.

The generated code for this block relies on prebuilt library files. You can run this
code outside the MATLAB® environment, or redeploy it, but be sure to account for these extra library
files when doing so. The `packNGo` function creates a single ZIP file
containing all of the pieces required to run or rebuild this code. See `packNGo` (Simulink Coder) for more information.

To know the code generation process of Simulink blocks, see Simulink Coder. To run an executable file that
was generated from a model containing this block, you may need to add precompiled shared
library files to your system path. See Simulink Shared Library Dependencies and Accelerating Simulink Models for details.

Usage notes and limitations:

- Host computer only. Excludes Simulink Desktop Real-Time code generation.
- The executable generated from this block relies on prebuilt dynamic library files
  (`.dll` files) included with MATLAB. Use the `packNGo` function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another development
  environment where MATLAB is not installed. For more details, see Code Generation, GPU, and Third-Party Support.

## Version History

**Introduced before R2006a**

## Description

Display images or video frames

The To Video Display block displays RGB or YCbCr formatted images and
video frames. The display created by the block is lightweight and high performance, capable of
displaying high definition video at high frame rates.
