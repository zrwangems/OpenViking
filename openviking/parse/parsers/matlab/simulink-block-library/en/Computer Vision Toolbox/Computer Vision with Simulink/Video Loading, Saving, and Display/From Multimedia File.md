---
type: simulink-block
title: 'From Multimedia File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'frommultimediafile'
documentation_source_path: 'ref/frommultimediafile.html'
language: en
---

# From Multimedia File

## Ports

### Output

### **Image** — Color image or video frame array

Color image or video frame, returned as an
*M*-by-*N*-by-*P* array.
*M* and *N* are the number of rows and columns in
each image. *P* is the number of color channels in each image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `RGB` and **Image signal**
  parameter to `One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Simulink.ImageType`

### **I** — Grayscale image or video frame matrix

Grayscale image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the grayscale
image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `Intensity`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **R** — Red color component of image or video frame matrix

Red color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `RGB` and **Image signal**
  parameter to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — Green color component of image or video frame matrix

Green color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `RGB` and **Image signal**
  parameter to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — Blue color component of image or video frame matrix

Blue color component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `RGB` and **Image signal**
  parameter to `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Y** — Luma component of image or video frame matrix

Luma component of the image or video frame, returned as an
*M*-by-*N* matrix. *M* and
*N* are the number of rows and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — Blue-difference chrominance component of image or video frame matrix

Blue-difference chrominance component of the image or video frame, returned as an
*M*-by-*N*/2 matrix. *M* and
*N* are the number of rows and columns in the input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — Red-difference chrominance component of image or video frame matrix

Red-difference chrominance component of the image or video frame, returned as an
*M*-by-*N*/2 matrix. *M* and
*N* are the number of rows and columns in each input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to the name of a
  multimedia file that contains video or image data. If the specified file
  contains both audio and video data, set the **Multimedia
  outputs** parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Audio** — Audio signal vector | matrix

Audio signal, returned as an *M*-element vector or an
*M*-by-*N* matrix. *M* is the
number of samples in each channel and *N* is the number of
channels.

#### Dependencies

To enable this port, set the **File name** parameter to the
name of a multimedia file that contains audio data. If the specified file contains
both audio and video data, set the **Multimedia outputs** parameter
to `Audio only` or `Video and
audio`.

**Data Types:** `single` | `double` | `int16` | `uint8`

### **EOF** — End-of-file indicator scalar

End-of-file indicator, returned as a logical scalar for each video frame or audio
sample. The end-of-file indicator is `1` when the block outputs the
final video frame or audio sample from the file, and is `0`
otherwise.

#### Dependencies

To enable this port, select the **Output end-of-file
indicator** parameter.

**Data Types:** `Boolean`

## Parameters

### **Main**

### **File name** — Name of multimedia file `vipmen.avi` (default) | character vector

Specify the name of the multimedia file for the block to read. If the file is not
located on your MATLAB® path, select **Browse** and navigate to the file, or
specify the full file path.

On Microsoft®
Windows® platforms, this parameter supports URLs that point to Microsoft Media Server (MMS) streams.

### **Inherit sample time from file** — Inherit sample time from file `on` (default) | `off`

Specify whether the block inherits the sample time from the multimedia file or
uses a specified sample time. When you select this parameter, the block inherits the
sample time from the input multimedia file.

**Tip**

Select this parameter when you do not know the intended sample rate of the
multimedia file.

### **Desired sample time** — Block sample time `1/30` (default) | real positive scalar

Specify a sample time for the block.

#### Dependencies

To enable this parameter, clear the **Inherit sample time from
file** parameter.

### **Number of times to play file** — Number of times to play multimedia file `inf` (default) | real positive integer

Specify the number of times to play the input multimedia file. The default value
of `inf` specifies that the block repeats playing the multimedia file
until the simulation stop time.

### **Output end-of-file indicator** — End-of-file indicator `off` (default) | `on`

Select this parameter to enable the **EOF** port, which indicates
whether the output frame or sample is the final video frame or audio sample in the
multimedia file.

### **Multimedia outputs** — Type of media `Video only` (default) | `Audio only` | `Video and audio`

Specify the type of media to read from a file containing both video and audio
data.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains both audio and video data.

### **Output color format** — Color format of video `RGB` (default) | `Intensity` | `YCbCr 4:2:2`

Specify the output color format of the input video data. The block supports the
`RGB`, `Intensity`, and
`YCbCr 4:2:2` color formats.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains video data. If the specified file
contains both audio and video data, set the **Multimedia outputs**
parameter to `Video only` or `Video and
audio`.

### **Image signal** — Output port configuration for RGB video `One multidimensional signal` (default) | `Separate color signals` | `Simulink image signal`

Specify how the block outputs an RGB color video. If you select `One
multidimensional signal`, the block outputs the video data using only
the **Image** port. If you select `Separate color
signals`, the block outputs the video data using three separate color
channels, divided across the **R**, **G**, and
**B** ports. If you select `Simulink image
signal`, the block outputs a video in
`Simulink.ImageType` datatype.

#### Dependencies

To enable this parameter:

- Set the **File name** parameter to the name of a
  multimedia file that contains video data. If the specified file contains both
  audio and video data, set the **Multimedia outputs**
  parameter to `Video only` or `Video and
  audio`.
- Set the **Output color format** parameter to
  `RGB`.

### **Read range** — Range of audio samples `[1 Inf]` (default) | two-element row vector

Specify the range of audio samples to read from the input file as a two-element
row vector of the form `[StartSample EndSample]`.
`StartSample` is the first sample the block reads from the audio
file, and `EndSample` is the final sample the block reads from the
audio file. `StartSample` must be greater than or equal to
`1`. `EndSample` must be greater than
`StartSample`.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains audio data. If the specified file
contains both audio and video data, set the **Multimedia outputs**
parameter to `Audio only`.

### **Samples per audio channel** — Samples per audio channel `1024` (default) | real positive integer

Specify the number of samples per audio channel.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains audio data. If the specified file
contains both audio and video data, set the **Multimedia outputs**
parameter to `Audio only`.

### **Data Types**

### **Video output data type** — Video output data type `single` (default) | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit from file`

Specify the data type for the output video frames.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains video data. If the specified file
contains both audio and video data, set the **Multimedia outputs**
parameter to `Video only` or `Video and
audio`.

### **Audio output data type** — Audio output data type `int16` (default) | `double` | `single` | `uint8`

Specify the data type for the output audio samples.

#### Dependencies

To enable this parameter, set the **File name** parameter to
the name of a multimedia file that contains audio data. If the specified file
contains both audio and video data, set the **Multimedia outputs**
parameter to `Audio only` or `Video and
audio`.

## Libraries

Computer Vision Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Supports 16- and 32-bit signed and 8-bit unsigned integers. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- Host computer only. Excludes Simulink Desktop Real-Time code generation.
- The executable generated from this block relies on prebuilt dynamic library files
  (`.dll` files) included with MATLAB. Use the `packNGo` (Simulink Coder) function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another development
  environment where MATLAB is not installed.

## Version History

**Introduced before R2006a**

## Description

Read video frames and audio samples from multimedia file

The From Multimedia File block reads video frames, audio samples, or both
from a multimedia file. The block imports data from a file, of a supported file format, into a
Simulink® model. For more information about supported file formats, see Supported Platforms and File Formats.

This block enables you to read WMA or WMV streams from your system or over a network
connection. Similarly, the To Multimedia File
block enables you to write WMA or WMV streams to your system or over a network connection. If
your system does not have the codec necessary to support a file format, you must re-encode
files of that format into a file format supported by the Computer Vision Toolbox™.

If you have a Simulink
Coder™ license, you can generate code from a model containing this block. To run a
generated executable file, you may need to add precompiled shared library files to your system
path. For more information, see Simulink Shared Library Dependencies and Accelerating Simulink Models.

**Note**

This block supports code generation for a host computer that has file I/O available. You
cannot use this block with Simulink
Desktop Real-Time™ software because that product does not support file I/O.
