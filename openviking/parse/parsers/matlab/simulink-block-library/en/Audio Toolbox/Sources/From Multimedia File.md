---
type: simulink-block
title: 'From Multimedia File'
family: 'dsp'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'frommultimediafile'
documentation_source_path: '../dsp/ref/frommultimediafile.html'
language: en
---

# From Multimedia File

## Ports
```yaml
ports:
- name: Image
  summary: Color image or video frame array
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Simulink.ImageType
- name: I
  summary: Grayscale image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: R
  summary: Red color component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: G
  summary: Green color component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: B
  summary: Blue color component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Y
  summary: Luma component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cb
  summary: Blue-difference chrominance component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cr
  summary: Red-difference chrominance component of image or video frame matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Audio
  summary: Audio signal vector | matrix
  direction: output
  data_types: single | double | int16 | uint8
- name: EOF
  summary: End-of-file indicator scalar
  direction: output
  data_types: Boolean
```

### Output

### **Image** — Color image or video frame array

Color image or video frame, returned as an
*M*-by-*N*-by-*P*
array. *M* and *N* are the number of
rows and columns in each image. *P* is the number of
color channels in each image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `One multidimensional
  signal`.
- This port is named as **Simulink
  Image** if the **Output color
  format** parameter is set to
  `RGB` and the
  **Image signal** parameter is set
  to `Simulink image
  signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Simulink.ImageType`

### **I** — Grayscale image or video frame matrix

Grayscale image or video frame, returned as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the grayscale image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to
  `Intensity`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **R** — Red color component of image or video frame matrix

Red color component of the image or video frame, returned as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Outputs from the **R**, **G**, or
**B** ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — Green color component of image or video frame matrix

Green color component of the image or video frame, returned as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Outputs from the **R**, **G**, or
**B** ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — Blue color component of image or video frame matrix

Blue color component of the image or video frame, returned as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

Outputs from the **R**, **G**, or
**B** ports must have the same dimensions.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `RGB` and
  **Image signal** parameter to
  `Separate color
  signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Y** — Luma component of image or video frame matrix

Luma component of the image or video frame, returned as an
*M*-by-*N* matrix.
*M* and *N* are the number of rows
and columns in the image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — Blue-difference chrominance component of image or video frame matrix

Blue-difference chrominance component of the image or video frame,
returned as an *M*-by-*N*/2 matrix.
*M* and *N* are the number of rows
and columns in the input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — Red-difference chrominance component of image or video frame matrix

Red-difference chrominance component of the image or video frame,
returned as an *M*-by-*N*/2 matrix.
*M* and *N* are the number of rows
and columns in each input image.

#### Dependencies

To enable this port:

- Set the **File name** parameter to
  the name of a multimedia file that contains video or
  image data. If the specified file contains both audio
  and video data, set the **Multimedia
  outputs** parameter to `Video
  only` or `Video and
  audio`.
- Set the **Output color format**
  parameter to `YCbCr
  4:2:2`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Audio** — Audio signal vector | matrix

Audio signal, returned as an *M*-element vector or an
*M*-by-*N* matrix.
*M* is the number of samples in each channel and
*N* is the number of channels.

#### Dependencies

To enable this port, set the **File name**
parameter to the name of a multimedia file that contains audio data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Audio only` or `Video and
audio`.

**Data Types:** `single` | `double` | `int16` | `uint8`

### **EOF** — End-of-file indicator scalar

End-of-file indicator, returned as a logical scalar for each video
frame or audio sample. The end-of-file indicator is `1`
when the block outputs the final video frame or audio sample from the
file, and is `0` otherwise.

#### Dependencies

To enable this port, select the **Output end-of-file
indicator** parameter.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: File name
  summary: Name of multimedia file speech_dft.mp3 (default) | character vector
  group: Main Tab
- name: Inherit sample time from file
  summary: Inherit sample time from file on (default) | off
  group: Main Tab
- name: Desired sample time
  summary: Block sample time 1/30 (default) | real positive scalar
  group: Main Tab
- name: Number of times to play file
  summary: Number of times to play multimedia file inf (default) | positive integer
  group: Main Tab
- name: Read range
  summary: Range of audio samples [1 Inf] (default) | two-element vector
  group: Main Tab
- name: Output end-of-file indicator
  summary: End-of-file indicator off (default) | on
  group: Main Tab
- name: Multimedia outputs
  summary: Type of media Audio only (default) | Video and audio | Video only
  group: Main Tab
- name: Samples per audio channel
  summary: Samples per audio channel 1024 (default) | positive integer
  group: Main Tab
- name: Output color format
  summary: Color format of video RGB (default) | Intensity | YCbCr 4:2:2
  group: Main Tab
- name: Image signal
  summary: Output port configuration for RGB video One multidimensional signal (default) | Separate color signals | Simulink
    image signal
  group: Main Tab
- name: Audio output data type
  summary: Audio output data type double (default) | single | int16 | uint8
  group: Data Types Tab
- name: Video output data type
  summary: Video output data type single (default) | double | int8 | uint8 | int16 | uint16 | int32 | uint32 | Inherit from
    file
  group: Data Types Tab
```

### Main Tab

### **File name** — Name of multimedia file `speech_dft.mp3` (default) | character vector

Specify the name of the multimedia file for the block to read. The
block determines the type of file (audio and video, audio only, or video
only) and provides the associated parameters.

If the location of the file does not appear on the MATLAB path, use the **Browse** button to
specify the full path. If the location of the file appears on the
MATLAB path, enter only the file name.

On Windows platforms, this parameter supports URLs that point to MMS
(Microsoft Media Server) streams.

### **Inherit sample time from file** — Inherit sample time from file on (default) | off

Specify whether the block inherits the sample time from the multimedia
file or uses a specified sample time. When you select this parameter,
the block inherits the sample time from the input multimedia file. When
you clear this parameter, the block uses the sample time that you
specify in the **Desired sample time**
parameter.

**Tip**

Select this parameter when you do not know the intended sample
rate of the multimedia file.

### **Desired sample time** — Block sample time `1/30` (default) | real positive scalar

Specify the block sample time.

#### Dependencies

To enable this parameter, clear the **Inherit sample time
from file** parameter.

### **Number of times to play file** — Number of times to play multimedia file `inf` (default) | positive integer

Specify the number of times to play the input multimedia file. The
default value of `inf` specifies that the block repeats
playing the multimedia file until the simulation stop time.

### **Read range** — Range of audio samples `[1 Inf]` (default) | two-element vector

Specify the sample range from which to read as a two-element row
vector in the form of [*StartSample*
*EndSample*], where *StartSample* is
the sample at which file reading starts, and
*EndSample* is the sample at which file reading
stops.

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains audio data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Audio only`.

### **Output end-of-file indicator** — End-of-file indicator off (default) | on

Use this parameter to determine whether the output is the last video
frame or audio sample in the multimedia file. When you select this
parameter, a `Boolean` output port labeled
**EOF** appears on the block. The output from the
**EOF** port defaults to 1 when the last video
frame or audio sample is output from the block. Otherwise, the output
from the **EOF** port defaults to 0.

### **Multimedia outputs** — Type of media `Audio only` (default) | `Video and audio` | `Video only`

Specify the type of media to read from a file containing both video
and audio data.

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains both audio
and video data.

### **Samples per audio channel** — Samples per audio channel `1024` (default) | positive integer

Specify number of samples per audio channel. This parameter becomes
available for files containing audio.

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains audio data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Audio only`.

### **Output color format** — Color format of video `RGB` (default) | `Intensity` | `YCbCr 4:2:2`

Specify the output color format of the input video data. The block
supports the `RGB`,
`Intensity`, and `YCbCr
4:2:2` color formats.

If you select `RGB`, use the **Image
signal** parameter to specify how to output a color
signal.

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains video data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Video only` or `Video and
audio`.

### **Image signal** — Output port configuration for RGB video `One multidimensional signal` (default) | `Separate color signals` | `Simulink image signal`

Specify how the block outputs an RGB color video. If you select:

- `One multidimensional signal` ––
  The block outputs an
  *M*-by-*N*-by-*P*
  color video signal through the **Image**
  port, where *P* is the number of color
  planes.
- `Separate color signals` –– The
  block outputs the video data using three separate color
  channels, divided across the **R**,
  **G**, and **B**
  ports. Each port outputs one
  *M*-by-*N* plane of an
  RGB video stream.
- `Simulink image signal` –– The
  block outputs a video in
  `Simulink.ImageType` datatype.

#### Dependencies

To enable this parameter:

- Set the **File name** parameter to
  the name of a multimedia file that contains video data.
  If the specified file contains both audio and video
  data, set the **Multimedia outputs**
  parameter to `Video only` or
  `Video and audio`.
- Set the **Output color format**
  parameter to `RGB`.

### Data Types Tab

### **Audio output data type** — Audio output data type `double` (default) | `single` | `int16` | `uint8`

Specify the data type for the audio samples output at the
**Audio** port.

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains audio data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Audio only` or `Video and
audio`.

### **Video output data type** — Video output data type `single` (default) | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit from file`

Specify the data type of the video frames output at the
**R**, **G**,
**B**, or **Image** ports..

#### Dependencies

To enable this parameter, set the **File name**
parameter to the name of a multimedia file that contains video data.
If the specified file contains both audio and video data, set the
**Multimedia outputs** parameter to
`Video only` or `Video and
audio`.
## Libraries

Audio Toolbox / Sources DSP System Toolbox / Sources

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

- Host computer only. Excludes Simulink Desktop Real-Time code
  generation.
- The executable generated from this block relies on prebuilt dynamic
  library files (`.dll` files) included with MATLAB. Use the `packNGo` function to package the
  code generated from this block and all the relevant files in a compressed
  ZIP file. Using this ZIP file, you can relocate, unpack, and rebuild your
  project in another development environment where MATLAB is not installed. For more details, see How To Run a Generated Executable Outside MATLAB.

## Version History

**Introduced before R2006a**

### R2022b: Support for OPUS audio file format

The From Multimedia File block supports audio files in the OPUS
file format (`.opus`).

## Description

Stream from multimedia file

The From Multimedia File block reads audio samples, video frames, or
both from a multimedia file and generates a signal with one of the following data types
and amplitude ranges.

| Output Data Type | Output Amplitude Range |
| --- | --- |
| `double` | ±1 |
| `single` | ±1 |
| `int16` | −32768 to 32767 (−215 to 215 − 1) |
| `uint8` | 0 to 255 |

The block imports data from the file into a Simulink® model.

**Note**

This block supports code generation for a host computer that has file I/O
available. You cannot use this block with Simulink
Desktop Real-Time™ software because that product does not support file I/O. The generated
code for this block relies on prebuilt library files. For more details, see Code Generation.
