---
type: simulink-block
title: 'To Multimedia File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'tomultimediafile'
documentation_source_path: 'ref/tomultimediafile.html'
language: en
---

# To Multimedia File

## Ports

### Input

### **Image** — Input image frame matrix | array

Specify the input image frame as a matrix or an array. To write an intensity
image frame to a multimedia file, specify it as an
*M*-by-*N* matrix. For a color image frame,
specify it as an *M*-by-*N*-by-3 array.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI`, `MJ-2000`,
  `WMV`, or `MPEG4`.
- If the **File type** parameter value is not
  `MJ-2000`, set the **Write**
  parameter to `Video and audio` or `Video
  only`.
- If the **File type** parameter value is
  `AVI` or `MPEG4`, set the
  **File color format** parameter to
  `RGB`.
- Set the **Image signal** parameter to `One
  multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — Red color component of image matrix

Specify the red color component of the input image frame as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI`, `MJ-2000`,
  `WMV`, or `MPEG4`.
- If the **File type** parameter value is not
  `MJ-2000`, set the **Write**
  parameter to `Video and audio` or `Video
  only`.
- If the **File type** parameter value is
  `AVI` or `MPEG4`, set the
  **File color format** parameter to
  `RGB`.
- Set the **Image signal** parameter to
  `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of image matrix

Specify the green color component of the input image frame as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI`, `MJ-2000`,
  `WMV`, or `MPEG4`.
- If the **File type** parameter value is not
  `MJ-2000`, set the **Write**
  parameter to `Video and audio` or `Video
  only`.
- If the **File type** parameter value is
  `AVI` or `MPEG4`, set the
  **File color format** parameter to
  `RGB`.
- Set the **Image signal** parameter to
  `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of image matrix

Specify the blue color component of the input image frame as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI`, `MJ-2000`,
  `WMV`, or `MPEG4`.
- If the **File type** parameter value is not
  `MJ-2000`, set the **Write**
  parameter to `Video and audio` or `Video
  only`.
- If the **File type** parameter value is
  `AVI` or `MPEG4`, set the
  **File color format** parameter to
  `RGB`.
- Set the **Image signal** parameter to
  `Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — Luma component of image matrix

Specify the luma component of the input image frame as an
*M*-by-*N* matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI` or `MPEG4`.
- Set the **Write** parameter to `Video and
  audio` or `Video only`.
- Set the **File color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — Blue-difference chrominance component of image matrix

Specify the blue-difference chrominance component of the input image as an
*M*-by-*N*/2 matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI` or `MPEG4`.
- Set the **Write** parameter to `Video and
  audio` or `Video only`.
- Set the **File color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — Red-difference chrominance component of image matrix

Specify the red-difference chrominance component of the input image as an
*M*-by-*N*/2 matrix.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI` or `MPEG4`.
- Set the **Write** parameter to `Video and
  audio` or `Video only`.
- Set the **File color format** parameter to
  `YCbCr 4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Audio** — Input audio signal vector | matrix

Specify the input audio signal as a vector or a matrix. When specified as a
matrix, the block treats each column as an independent channel.

#### Dependencies

To enable this port:

- Set the **File type** parameter to
  `AVI`, `WAV`,
  `WMA`, `MPEG4`,
  `FLAC`, or `OGG`.
- If the **File type** parameter value is
  `AVI`, `WMV`, or
  `MPEG4` set the **Write**
  parameter to `Video and audio` or `Audio
  only`.

**Data Types:** `single` | `double` | `int16` | `int32` | `uint8`

## Parameters

### **File name** — Name of multimedia file `output.avi` (default) | character vector

Specify the name for the multimedia file the block writes. The block appends a file
extension automatically based on the specified **File type** parameter.
If the specified file name, including the file extension, already exists, the block
overwrites the data in the existing file with the new input data.

By default, the block saves the file in the current working directory. To specify a
different file location, click the **Save As...** button.

### **File type** — Type of multimedia file `AVI` (default) | `WAV` | `MJ2000` | `WMA` | `WMV` | `MPEG4` | `FLAC` | `OGG`

Specify the type of multimedia file to write. The block supports the
`AVI`, `WAV`,
`MJ2000`, `WMA`,
`WMV`, `MPEG4`,
`FLAC`, and `OGG` file formats.

### **Write** — Type of media `Video only` (default) | `Audio only` | `Video and audio`

Specify the type of media to write. Depending on the value of the **File
type** parameter, you can select `Video only`,
`Audio only`, or `Video and audio`.

|  |  |
| --- | --- |
| **Type of file** | **Supported type of media** |
| `AVI` | - `Video only` - `Audio only` - `Video and audio` |
| `WMV` | - `Video only` - `Video and audio` |
| `MPEG4` | - `Video only` - `Audio only` |

#### Dependencies

To enable this parameter, set the **File type** parameter to
`AVI`, `WMV`, or
`MPEG4`.

### **Video compressor** — Video compression algorithm `None (uncompressed)` (default) | `DV Video Encoder` | `MJPEG Compressor` | `Lossy` | `Lossless`

Specify a video compression algorithm to reduce the size of the output file. The
available options depend on the value of the **File type** parameter.

- `AVI` — Select either the `DV Video
  Encoder` or `MJPEG Compressor` algorithm.
  If you do not want to reduce the size of the file, select `None
  (uncompressed)`.
- `MJ2000` — Select either the
  `Lossy` or `Lossless`
  algorithm.

**Note**

The options for this parameter are the video compression algorithms installed on
your system. For information about a specific video compressor, see the documentation
for that compressor.

#### Dependencies

To enable this parameter, set the **File type** parameter to
`MJ2000` or `AVI`. For the
`AVI` file type, set the **Write**
parameter to `Video only` or `Video and
audio`.

### **Compression Factor (>1)** — Compression factor `10` (default) | integer greater than `1`

Specify the compression factor as an integer greater than
`1`.

#### Dependencies

To enable this parameter, set the **File type** parameter to
`MJ2000` and the **Video compressor**
parameter to `Lossy`.

### **Video Quality (0-100)** — Quality of video `75` (default) | integer in range [0, 100]

Specify the quality of the video as an integer in the range [0, 100].

#### Dependencies

To enable this parameter, set the **File type** parameter to
`MPEG4` and the **Write** parameter to
`Video only`.

### **File color format** — Color format of output video `RGB` (default) | `YCbCr 4:2:2`

Specify the color format of the video for the output file. The block supports the
`RGB` and `YCbCr 4:2:2` color
formats.

#### Dependencies

To enable this parameter, set the **File type** parameter to
`AVI` or `MPEG4`.

### **Image signal** — Input port configuration for RGB video `One multidimensional signal` (default) | `Separate color signals`

Specify how the block accepts an RGB color video input. If you select
`One multidimensional signal`, the block accepts input using
only the **Image** port. If you select `Separate color
signals`, the block accepts an input video using three separate color
channels, divided across the **R**, **G**, and
**B** ports.

#### Dependencies

To enable this parameter:

- Set the **File type** parameter to
  `AVI`, `MJ-2000`,
  `WMV`, or `MPEG4`.
- Set the **Write** parameter to `Video and
  audio` or `Video only`.
- If the **File type** parameter value is
  `AVI` or `MPEG4`, set the
  **File color format** parameter to
  `RGB`.

### **Audio compressor** — Audio compression algorithm `None (uncompressed)` (default) | `CCITT A-Law` | `CCITT u-Law` | `GSM 6.10` | `IMA ADPCM` | `Microsoft ADPCM` | `PCM`

Specify an audio compression algorithm to reduce the size of the output file. The
block supports the `CCITT A-Law`, `CCITT
u-Law`, `GSM 6.10`, `IMA
ADPCM`, `Microsoft ADPCM`, and
`PCM` algorithms. If you do not want to reduce the size of
the file, select `None (uncompressed)`.

**Note**

The options for this parameter are the audio compression algorithms installed on
your system. For information about a specific audio compressor, see the documentation
for that compressor.

#### Dependencies

To enable this parameter, use either of these options:

- Set the **File type** parameter to
  `AVI` and set the **Write**
  parameter to `Video and audio` or `Audio
  only`.
- Set the **File type** parameter to
  `WAV`.

### **Audio data type** — Audio data type `Determine from input data type` (default) | `8-bit integer` | `16-bit integer` | `24-bit integer` | `32-bit integer` | `32-bit float` | `64-bit float`

Specify the audio data type for the output file.

#### Dependencies

To enable this parameter select, use either of these options:

- Set the **File type** parameter to
  `WAV` and the **Audio compressor**
  parameter to `None (uncompressed)`.
- Set the **File type** parameter to
  `FLAC`. This file type supports only the
  `8-bit integer`, `16-bit
  integer`, and `24-bit integer` data
  types.

## Libraries

Computer Vision Toolbox / Sinks

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
  (`.dll` files) included with MATLAB®. Use the `packNGo` (Simulink Coder) function to package the code
  generated from this block and all the relevant files in a compressed ZIP file. Using
  this ZIP file, you can relocate, unpack, and rebuild your project in another development
  environment where MATLAB is not installed. For more details, see Code Generation, GPU, and Third-Party Support.

## Version History

**Introduced before R2006a**

## Description

Write video frames and audio samples to multimedia file

The To Multimedia File block writes video frames, audio samples, or both to
a multimedia file (`.avi`, `.wav`, `.mj2`,
`.mp4`, or `.m4v` format).

You can compress the video frames or audio samples by selecting a compression algorithm.
You can also control the type of video or audio in addition to other related properties the
multimedia file receives.

If you have a Simulink®
Coder™ license, you can generate a code from a model containing this block. To run a
generated executable file, you may need to add precompiled shared library files to your system
path. See Simulink Shared Library Dependencies, and Accelerating Simulink Models for details.

**Note**

This block supports code generation for platforms that have file I/O available. You
cannot use this block with Simulink
Desktop Real-Time™ software, because that product does not support file I/O.

This block performs best on platforms with Version 11 or later of Windows Media® Player software. This block supports only uncompressed RGB24 AVI files on
Linux® and Mac platforms.
