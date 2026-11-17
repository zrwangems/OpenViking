---
type: simulink-block
title: 'Read Binary File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'readbinaryfile'
documentation_source_path: 'ref/readbinaryfile.html'
language: en
---

# Read Binary File

## Ports
```yaml
ports:
- name: Y'
  summary: Luminance component 3-D array
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cb
  summary: Blue difference component 3-D array
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cr
  summary: Red difference component 3-D array
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: A
  summary: Alpha component 3-D array
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: T
  summary: Transparency component 3-D array
  direction: output
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: EOF
  summary: Last video frame indicator scalar
  direction: output
  data_types: Boolean
```

### Output

### **Y'** — Luminance component 3-D array

Luminance component of the video read from the binary file, specified as a 3-D
array. The label of this port can be changed using the **Component1**
parameter when the **Video format** parameter is set to
`Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — Blue difference component 3-D array

Blue difference component of the video read from the binary file, specified as a
3-D array. The label of this port can be changed using the
**Component2** parameter when the **Video format**
parameter is set to `Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — Red difference component 3-D array

Red difference component of the video read from the binary file, specified as a
3-D array. The label of this port can be changed using the
**Component3** parameter when the **Video format**
parameter is set to `Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **A** — Alpha component 3-D array

Alpha component of the video read from the binary file, specified as a 3-D array.
The label of this port can be changed using the **Component4**
parameter when the **Video format** parameter is set to
`Custom`.

#### Dependencies

To enable this port, use one of these options.

- Set the **Video format** parameter to `Four
  character codes` and set the **Four character
  code** parameter to `AYUV` or
  `IF09`.
- Set the **Video format** parameter to
  `Custom` and the **Number of output
  components** parameter to `4`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **T** — Transparency component 3-D array

Transparency component of the video read from the binary file, specified as a 3-D
array.

#### Dependencies

To enable this port, set the **Video format** parameter to
`Four character codes` and set the **Four
character code** parameter to `Y41T` or
`Y42T`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **EOF** — Last video frame indicator scalar

The port outputs a `1` when the component ports output the last
video frame. For every frame before that, it outputs a `0`.

#### Dependencies

To enable this port, select the **Output end-of-file
indicator** parameter.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: File name
  summary: Name of binary file vipmen.bin (default) | file name
  group: ''
- name: Video format
  summary: Format of video data Four character codes (default) | Custom
  group: ''
- name: Four character code
  summary: Format of binary file I420 (default) | AYUV | CLJR | cyuv | GREY | IF09 | IMC1 | IMC2 | IMC3 | IMC4 | IUYV | IY41
    | IYU1 | IYU2 | IYUV | NV12 | NV21 | UYNV | UYNY | V210 | Y411 | Y41P | Y41T | Y422 | Y42T | Y8 | Y800 | YUNV | YUY2 |
    YUYV | YV12 | YV16 | YVU9 | YVYU | ...
  group: ''
- name: FrameSize Rows
  summary: Number of rows in output array 120 (default) | positive integer
  group: ''
- name: FrameSize Cols
  summary: Number of columns in output array 160 (default) | positive integer
  group: ''
- name: Line ordering
  summary: Output array fill direction Top line first (default) | Bottom line first
  group: ''
- name: Number of times to play file
  summary: Number of times to play the file 1 (default) | positive integer | inf
  group: ''
- name: Output end-of-file indicator
  summary: Indicate when block output reaches last frame off (default) | on
  group: ''
- name: Sample time
  summary: Sample period of output 1/30 (default) | positive scalar | -1
  group: ''
- name: Bit stream format
  summary: Specifies if data is planar or packed Planar (default) | Packed
  group: ''
- name: Number of output components
  summary: Number of components in binary file 3 (default) | 1 | 2 | 4
  group: ''
- name: Component1
  summary: Name for luminance component Y' (default) | component name
  group: ''
- name: Component2
  summary: Name for blue difference component Cb (default) | component name
  group: ''
- name: Component3
  summary: Name for red difference component Cr (default) | component name
  group: ''
- name: Component4
  summary: Name for alpha component Alpha (default) | component name
  group: ''
- name: Bits1
  summary: Size of luminance component 8 (default) | 16 | 24 | 32
  group: ''
- name: Bits2
  summary: Size of blue difference component 8 (default) | 16 | 24 | 32
  group: ''
- name: Bits3
  summary: Size of red difference component 8 (default) | 16 | 24 | 32
  group: ''
- name: Bits4
  summary: Size of alpha component 8 (default) | 16 | 24 | 32
  group: ''
- name: Rows1
  summary: Number of rows for luminance component 120 (default) | positive integer
  group: ''
- name: Rows2
  summary: Number of rows for blue difference component 60 (default) | positive integer
  group: ''
- name: Rows3
  summary: Number of rows for red difference component 60 (default) | positive integer
  group: ''
- name: Rows4
  summary: Number of rows for alpha component 288 (default) | positive integer
  group: ''
- name: Cols1
  summary: Number of columns for luminance component 160 (default) | positive integer
  group: ''
- name: Cols2
  summary: Number of columns for blue difference component 80 (default) | positive integer
  group: ''
- name: Cols3
  summary: Number of columns for red difference component 80 (default) | positive integer
  group: ''
- name: Cols4
  summary: Number of columns for the alpha component 352 (default) | positive integer
  group: ''
- name: Component order in binary file
  summary: Arrangement of components in binary file [1 2 3] (default) | vector of valid component identifiers
  group: ''
- name: Interlaced video
  summary: Read video data from file as interlaced off (default) | on
  group: ''
- name: Input file has signed data
  summary: File has signed integers off (default) | on
  group: ''
- name: Byte order in binary file
  summary: Byte order of binary file Little endian (default) | Big endian
  group: ''
```

### **File name** — Name of binary file `vipmen.bin` (default) | file name

Specify the name of the binary source file to read video data from.

### **Video format** — Format of video data `Four character codes` (default) | `Custom`

Specify the format of the video data as one of these options.

- Four character codes (FOURCC) — For more information about these codes, see
  `https://en.wikipedia.org/wiki/FourCC`.
- Custom — Read the video data from a binary file of a custom format.

### **Four character code** — Format of binary file `I420` (default) | `AYUV` | `CLJR` | `cyuv` | `GREY` | `IF09` | `IMC1` | `IMC2` | `IMC3` | `IMC4` | `IUYV` | `IY41` | `IYU1` | `IYU2` | `IYUV` | `NV12` | `NV21` | `UYNV` | `UYNY` | `V210` | `Y411` | `Y41P` | `Y41T` | `Y422` | `Y42T` | `Y8` | `Y800` | `YUNV` | `YUY2` | `YUYV` | `YV12` | `YV16` | `YVU9` | `YVYU` | ...

Specify the four character code of the binary file codec. The value of this
parameter also sets the number of output ports. For information on which four character
codes enable which output ports, see the table below.

**Output Ports for Four Character Codes**

| Four Character Codes | Output Ports |
| --- | --- |
| I420 | Y'|Cb|Cr |
| AYUV | Y'|Cb|Cr|A |
| CLJR | Y'|Cb|Cr |
| cyuv | Y'|Cb|Cr |
| GREY | Y' |
| IF09 | Y'|Cb|Cr|A |
| IMC1 | Y'|Cb|Cr |
| IMC2 | Y'|Cb|Cr |
| IMC3 | Y'|Cb|Cr |
| IMC4 | Y'|Cb|Cr |
| IUYV | Y'|Cb|Cr |
| IY41 | Y'|Cb|Cr |
| IYU1 | Y'|Cb|Cr |
| IYU2 | Y'|Cb|Cr |
| IYUV | Y'|Cb|Cr |
| NV12 | Y'|Cb|Cr |
| NV21 | Y'|Cb|Cr |
| UYNV | Y'|Cb|Cr |
| UYNY | Y'|Cb|Cr |
| V210 | Y'|Cb|Cr |
| Y411 | Y'|Cb|Cr |
| Y41P | Y'|Cb|Cr |
| Y41T | Y'|Cb|Cr|T |
| Y422 | Y'|Cb|Cr |
| Y42T | Y'|Cb|Cr|T |
| Y8 | Y' |
| Y800 | Y' |
| YUNV | Y'|Cb|Cr |
| YUY2 | Y'|Cb|Cr |
| YUYV | Y'|Cb|Cr |
| YV12 | Y'|Cb|Cr |
| YV16 | Y'|Cb|Cr |
| YVU9 | Y'|Cb|Cr |
| YVYU | Y'|Cb|Cr |

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Four character codes`.

### **FrameSize Rows** — Number of rows in output array `120` (default) | positive integer

Specify the number of rows in the output array as a positive integer. The value of
this parameter must match the dimensions of the data inside the file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Four character codes`.

### **FrameSize Cols** — Number of columns in output array `160` (default) | positive integer

Specify the number of columns in the output array as a positive integer. The value
of this parameter must match the dimensions of the data inside the file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Four character codes`.

### **Line ordering** — Output array fill direction `Top line first` (default) | `Bottom line first`

If you select `Top line first`, the block first fills the first row
of the output array with the corresponding contents of the binary file. It then fills
the other rows in increasing order. When you select `Bottom line
first`, the block first fills the last row of the output array with the
corresponding contents of the binary file. It then fills the other rows in decreasing
order.

### **Number of times to play file** — Number of times to play the file `1` (default) | positive integer | `inf`

Specify the number of times to repeat the binary file as a positive integer or
`inf`. For any positive integer value `n` of this
parameter, the block plays the binary file `n` times. For a value of
`inf`, the block plays the file indefinitely until the end of
simulation.

### **Output end-of-file indicator** — Indicate when block output reaches last frame `off` (default) | `on`

This parameter indicates when the block output reaches the last video frame in the
binary file. Selecting this parameter enables the **EOF** port. The
output from the **EOF** port is `1` when the block
output reaches the last video frame. For all other frames, it is
`0`.

### **Sample time** — Sample period of output `1/30` (default) | positive scalar | `-1`

Specify the sample period of the output. Sample time indicates when, during
simulation the block produces output. The value of this parameter must be a positive
scalar less than the simulation time or `-1`. It cannot be
`0`. When set to `-1`, the block inherits the sample
time from the simulink model.

### **Bit stream format** — Specifies if data is planar or packed `Planar` (default) | `Packed`

Specify the data format of the binary file as planar or packed. If the data is
packed, use the **FrameSize Rows** and **FrameSize Cols** parameters to define the size of the output
array.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Number of output components** — Number of components in binary file `3` (default) | `1` | `2` | `4`

Specify the number of output components from the binary file. This parameter sets
the number of output ports.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Component1** — Name for luminance component `Y'` (default) | component name

Specify the name for the luminance component of the output array. The luminance
component is the first component from the input binary file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of output
components** parameter to `1` or greater.

### **Component2** — Name for blue difference component `Cb` (default) | component name

Specify the name for the blue difference component of the output array. The blue
difference component is the second component from the input binary file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of output
components** parameter to `2` or greater.

### **Component3** — Name for red difference component `Cr` (default) | component name

Specify the name for the red difference component of the output array using this
parameter. The red difference component is the third component from the input binary
file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of output
components** parameter to `3` or greater.

### **Component4** — Name for alpha component `Alpha` (default) | component name

Specify the name for the alpha component of the output array. The alpha component is
the fourth component from the input binary file.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of output
components** parameter to `4`.

### **Bits1** — Size of luminance component `8` (default) | `16` | `24` | `32`

Specify the size of the luminance component in the output array. The value of this
parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `1` or greater.

### **Bits2** — Size of blue difference component `8` (default) | `16` | `24` | `32`

Specify the size of the blue difference component in the output array. The value of
this parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `2` or greater.

### **Bits3** — Size of red difference component `8` (default) | `16` | `24` | `32`

Specify the size of the red difference component in the output array. The value of
this parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `3` or greater.

### **Bits4** — Size of alpha component `8` (default) | `16` | `24` | `32`

Specify the size of the alpha component in the output array. The value of this
parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `4`.

### **Rows1** — Number of rows for luminance component `120` (default) | positive integer

Specify the number of rows for the luminance component in the output array. The
value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `1` or greater.

### **Rows2** — Number of rows for blue difference component `60` (default) | positive integer

Specify the number of rows for the blue difference component in the output array.
The value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `2` or greater.

### **Rows3** — Number of rows for red difference component `60` (default) | positive integer

Specify the number of rows for the red difference component in the output array. The
value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `3` or greater.

### **Rows4** — Number of rows for alpha component `288` (default) | positive integer

Specify the number of rows for the alpha component in the output array. The value of
this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
ports** parameter to `4`.

### **Cols1** — Number of columns for luminance component `160` (default) | positive integer

Specify the number of columns for the luminance component in the output array. The
value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `1` or greater.

### **Cols2** — Number of columns for blue difference component `80` (default) | positive integer

Specify the number of columns for the blue difference component in the output array.
The value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `2` or greater.

### **Cols3** — Number of columns for red difference component `80` (default) | positive integer

Specify the number of columns for the luminance component in the output array. The
value of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `3` or greater.

### **Cols4** — Number of columns for the alpha component `352` (default) | positive integer

Specify the number of columns for the alpha component in the output array. The value
of this parameter must be a positive integer.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of output
components** parameter to `4`.

### **Component order in binary file** — Arrangement of components in binary file `[1 2 3]` (default) | vector of valid component identifiers

Specify the arrangement of components in the binary file. Identify the components by
the assigned numerals, from 1 to 4, in desired order. You must include all the enabled
components when setting this parameter.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Interlaced video** — Read video data from file as interlaced `off` (default) | `on`

Select this parameter when the binary file contains interlaced video data.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Input file has signed data** — File has signed integers `off` (default) | `on`

Select this parameter when the binary file contains signed integers.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Byte order in binary file** — Byte order of binary file `Little endian` (default) | `Big endian`

Specify the byte order of the binary file as either little endian or big
endian.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.
## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Read video data from binary file

The Read Binary File block reads the video data from a binary file and
imports it into a Simulink® model.

The user-specified block parameters describe the format of the video data. These
parameters, along with the raw binary file, create the video data for the Simulink model.

**Note**

This block supports code generation for only those platforms that have file I/O. The
block does not support code generation using Simulink
Desktop Real-Time™ or Simulink
Real-Time™.
