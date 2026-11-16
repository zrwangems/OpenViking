---
type: simulink-block
title: 'To Multimedia File'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tomultimediafile'
documentation_source_path: 'ref/tomultimediafile.html'
language: en
---

# To Multimedia File

## Ports

### Input

### **Image** — Color image or video frame array

Specify the color image or video frame as an
*M*-by-*N*-by-3 matrix RGB,
Intensity, or YCbCr 4:2:2 signal. *M* and
*N* are the number of rows and columns in each
image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `One multidimensional
  signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — Red color component of image or video frame matrix

Specify the red color component of the image or video frame as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Inputs to the **R**, **G**, or **B**
ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of image or video frame matrix

Specify the green color component of the image or video frame as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Inputs to the **R**, **G**, or **B**
ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of image or video frame matrix

Specify the blue color component of the image or video frame as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Inputs to the **R**, **G**, or **B**
ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — Luma component of image or video frame matrix

Specify the luma component of the image or video frame as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — Blue-difference chrominance component of image or video frame matrix

Specify the blue-difference chrominance component of the image or
video frame as an *M*-by-*N*/2 matrix.
*M* and *N* are the number of rows
and columns in the input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — Red-difference chrominance component of image or video frame matrix

Specify the red-difference chrominance component of the image or video
frame as an *M*-by-*N*/2 matrix.
*M* and *N* are the number of rows
and columns in each input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Write**
  parameter to `Video only` or
  `Video and audio`.
- Set the **File color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Audio** — Audio signal vector | matrix

Specify the audio signal as an *M*-element vector or
an *M*-by-*N* matrix.
*M* is the number of samples in each channel and
*N* is the number of channels.

#### Dependencies

To enable this port, set the **File name**
parameter to the name of a multimedia file that contains audio data.
If the specified file contains both audio and video data, set the
**Write** parameter to `Audio
only` or `Video and
audio`.

**Data Types:** `single` | `double` | `int16` | `int32` | `uint8`

## Parameters

### **File name** — File name `output.wav` (default) | character vector

Specify the name of the multimedia file. The block saves the file in your current folder.
To specify a different file or location, click the **Save
As** button.

### **File type** — File type of multimedia file `WAV` (default) | `AVI``MJ2000` | `WMA` | `WMV` | `MPEG4` | `FLAC` | `MP3` | `OGG` | `OPUS`

Specify the type of the multimedia file as one of these options:

- `WAV`
- `AVI`
- `MJ2000`
- `WMA`
- `WMV`
- `MPEG4`
- `FLAC`
- `MP3`
- `OGG`
- `OPUS`

### **Write** — Type of multimedia `Audio only` (default) | `Video and audio` | `Video only`

Specify whether the block writes video frames, audio samples, or both to
the multimedia file. You can select `Video and
audio`, `Video only`, or
`Audio only`.

#### Dependencies

To enable this parameter, set **File type** to
`AVI`, `MPEG4`, or
`OGG`.

### **Audio Quality (0-100)** — Quality of audio file `75` (default) | integer in range [0 100]

Specify the quality setting for variable bitrate compression as a scalar
in the range [0,100], where 0 is lower quality and higher compression, and
100 is higher quality and lower compression. The default value is
`75`.

The variable bitrate (VBR) codecs select the appropriate bit rate for each
encoded frame depending on the perceptual complexity of the signal and the
value you specify in the **Audio Quality (0-100)**
parameter.

#### Dependencies

To enable this parameter, set **File type** to
`OGG`, `OPUS`, or
`MP3`.

### **Audio Bit Rate (kb/s)** — Audio compressor `128` (default) | `64` | `96` | `160` | `192` | `256` | `320`

Specify the bit rate of compressed audio files in kilobits per second
(kb/s) as 64, 96, 128, 160, 192, 256, or 320. The default value is 128.

On a Windows system, you can set the bit rate to 192, 160,128, or
96.

In general, a larger bit rate value results in higher perceived audio
quality.

#### Dependencies

To enable this parameter, set **File type** to
`MPEG4` and **Write** to
`Audio only`.

### **Audio compressor** — Audio compressor `None (uncompressed)` (default) | character vector

Select the type of compression algorithm to use to compress the audio
data. This compression reduces the size of the multimedia file. Choose
`None (uncompressed)` to save uncompressed
audio data to the multimedia file.

**Note**

The other items available in this parameter list are the audio
compression algorithms installed on your system. For information
about a specific audio compressor, see the documentation for that
compressor.

#### Dependencies

To enable this parameter, set **Write** to
`Video and audio` or `Audio
only`.

### **Audio data type** — Audio data type `16-bit integer` (default) | `Determine from input data type` | `8-bit integer` | `24-bit integer` | `32-bit integer` | `32-bit float` | `64-bit float`

Select the audio data type. You can use the **Audio data
type** parameter only for uncompressed wave files.

#### Dependencies

To enable this parameter, set **Audio compressor** to
`None (uncompressed)`.

### **Video compressor** — Video compressor `None (uncompressed)` (default) | character vector

Select the type of compression algorithm to use to compress the video
data. This compression reduces the size of the multimedia file. Choose
`None (uncompressed)` to save uncompressed
video data to the multimedia file.

**Note**

The other items available in this parameter list are the video
compression algorithms installed on your system. For information
about a specific video compressor, see the documentation for that
compressor.

#### Dependencies

To enable this parameter, set **Write** to
`Video and audio` or `Video
only`.

### **Compression Factor (>1)** — Compression factor greater than 1) 10 (default) | integer > 1

Specify the compression factor as an integer greater than `1`. The
default value of this parameter is `10`.

#### Dependencies

To enable this parameter, set **File type** to
`MJ2000` and **Video
compressor** to `Lossy`.

### **File color format** — File color format `RGB` (default) | `YCbCr 4:2:2`

Select the color format of the data stored in the file. You can select
either `RGB` or `YCbCr
4:2:2`.

#### Dependencies

To enable this parameter, set **Write** to
`Video and audio` or `Video
only`.

### **Image signal** — Image signal `Separate color signals` (default) | `One multidimensional signal`

Specify how the block accepts a color video signal. If you select
`One multidimensional signal`, the block
accepts an
*M*-by-*N*-by-*P*
color video signal, where *P* is the number of color
planes, at one port. If you select `Separate color
signals`, additional ports appear on the block. Each port
accepts one *M*-by-*N* plane of an RGB
video stream.

#### Dependencies

To enable this parameter, set **Write** to
`Video and audio` or `Video
only`.

### **Video Quality (0-100)** — Quality of video `75` (default) | integer in range [0 100]

Specify the quality of the video as an integer in the range [`0 100`].
The default value of this parameter is `75`.

#### Dependencies

To enable this parameter, set **File type** to
`MPEG4` and **Write** to
`Video only`.

## Libraries

Audio System Toolbox / Sinks DSP System Toolbox / Sinks

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

- Host computer only. Excludes Simulink
  Desktop Real-Time code generation.
- The executable generated from this block relies on prebuilt dynamic
  library files (`.dll` files) included with MATLAB. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  zip file. Using this zip file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.

## Version History

**Introduced before R2006a**

### R2024a: New **Audio Quality (0-100)** and **Audio Bit Rate (kb/s)** parameters

You can now specify audio quality and audio bitrate in the To Multimedia
File block for these compressed audio file extensions:

- `OGG`, `OPUS`,
  `MP3` –– Audio quality
- `MPEG4` –– Audio bit rate

### R2023b: Support for writing MP3 files

The To Multimedia File block supports writing MP3 files
(`.mp3`).

### R2022b: Support for OPUS audio file format

The To Multimedia File block supports OPUS file format
(`.opus`).

## Description

Stream video frames and audio samples to multimedia file

The To Multimedia File block writes video frames, audio samples, or
both to a multimedia (`.avi`, `.wav`,
`.wma`, `.mp4`, `.ogg`,
`.flac`, `.wmv`) file.

You can compress the video frames or audio samples by selecting a compression
algorithm. You can connect as many of the input ports as you want. Therefore, you can
control the type of video and/or audio the multimedia file receives.

**Note**

This block supports code generation for platforms that have file I/O available.
You cannot use this block with Simulink®
Desktop Real-Time™ software, because that product does not support file I/O.

This block performs best on platforms with Version 11 or later of Windows Media® Player software. This block supports only uncompressed RGB24 AVI files
on Linux® and Mac platforms.

Windows® 7 UAC (User Account Control) might require administrative privileges to
encode `WMV` and `WMA` files.

The generated code for this block relies on prebuilt library files. You can run this code
outside the MATLAB® environment or redeploy it, but be sure to account for these extra library
files when doing so. The `packNGo` function creates a single zip file
containing all of the pieces required to run or rebuild this code. See `packNGo` (Simulink Coder) for more information.

To run an executable file that was generated from a model containing this block, you
may need to add precompiled shared library files to your system path. See Understanding C Code Generation in DSP System Toolbox for details.
