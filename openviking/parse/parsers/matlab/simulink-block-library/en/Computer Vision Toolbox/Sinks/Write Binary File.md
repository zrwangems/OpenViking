---
type: simulink-block
title: 'Write Binary File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'writebinaryfile'
documentation_source_path: 'ref/writebinaryfile.html'
language: en
---

# Write Binary File

## Ports
```yaml
ports:
- name: Y'
  summary: Luminance component of input video stream scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cb
  summary: Blue difference component of the input video stream scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cr
  summary: Red difference component of input video stream scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: A
  summary: Alpha component of input video stream scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: T
  summary: Transparency component of input video stream scalar | vector | matrix
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
```

### Input

### **Y'** — Luminance component of input video stream scalar | vector | matrix

Luminance component of the input video stream, specified as a scalar, vector, or
matrix. The label of this port can be changed using the
**Component1** parameter when the **Video format**
parameter is set to `Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — Blue difference component of the input video stream scalar | vector | matrix

Blue difference component of the input video stream, specified as a scalar,
vector, or matrix. The label of this port can be changed using the
**Component2** parameter when the **Video format**
parameter is set to `Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — Red difference component of input video stream scalar | vector | matrix

Red difference component of the input video stream, specified as a scalar, vector,
or matrix. The label of this port can be changed using the
**Component3** parameter when the **Video format**
parameter is set to `Custom`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **A** — Alpha component of input video stream scalar | vector | matrix

Alpha component of the input video stream, specified as a scalar, vector, or
matrix. The label of this port can be changed using the
**Component4** parameter when the **Video format**
parameter is set to `Custom`.

#### Dependencies

To enable this port, use one of these options.

- Set the **Video format** parameter to `Four
  character codes`, and set the **Four character
  code** parameter to `AYUV` or
  `IF09`.
- Set the **Video format** parameter to
  `Custom`, and the **Number of
  inputs** parameter to `4`. In this case,
  the name of this port is **Alpha**.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **T** — Transparency component of input video stream scalar | vector | matrix

Transparency component of the input video stream, specified as a scalar, vector,
or matrix.

#### Dependencies

To enable this port, set the **Video format** parameter to
`Four character codes`, and set the **Four
character code** parameter to `Y41T` or
`Y42T`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## Parameters
```yaml
parameters:
- name: File name
  summary: Name of the binary file output.bin (default) | file name
  group: ''
- name: Video format
  summary: Format of the video data Four character codes (default) | Custom
  group: ''
- name: Four character code
  summary: Format of binary file I420 (default) | AYUV | CLJR | cyuv | GREY | IF09 | IMC1 | IMC2 | IMC3 | IMC4 | IUYV | IY41
    | IYU1 | IYU2 | IYUV | NV12 | NV21 | UYNV | UYNY | V210 | Y411 | Y41P | Y41T | Y422 | Y42T | Y8 | Y800 | YUNV | YUY2 |
    YUYV | YV12 | YV16 | YVU9 | YVYU | ...
  group: ''
- name: Line ordering
  summary: Binary file fill direction Top line first (default) | Bottom line first
  group: ''
- name: Bit stream format
  summary: Data format of binary file Planar (default) | Packed
  group: ''
- name: Number of inputs
  summary: Number of components in input video stream 3 (default) | 1 | 2 | 4
  group: ''
- name: Inherit size of components from input data type
  summary: All components have same number of bits on (default) | off
  group: ''
- name: Component1
  summary: Name of luminance component input port Y' (default) | component name
  group: ''
- name: Component2
  summary: Name of blue difference component Cb (default) | component name
  group: ''
- name: Component3
  summary: Name of red difference component Cr (default) | component name
  group: ''
- name: Component4
  summary: Name of alpha component Alpha (default) | component name
  group: ''
- name: Bits1
  summary: Size of luminance component 8 (default) | 0 | 16 | 24 | 32
  group: ''
- name: Bits2
  summary: Size of blue difference component 8 (default) | 0 | 16 | 24 | 32
  group: ''
- name: Bits3
  summary: Size of red difference component 8 (default) | 0 | 16 | 24 | 32
  group: ''
- name: Bits4
  summary: Size of alpha component 8 (default) | 0 | 16 | 24 | 32
  group: ''
- name: Component order in binary file
  summary: Arrangement of components in binary file [1 2 3] (default) | vector of valid component identifiers
  group: ''
- name: Interlaced video
  summary: Read video data as interlaced off (default) | on
  group: ''
- name: Write signed data to output file
  summary: Write signed data to output binary file off (default) | on
  group: ''
- name: Byte order in binary file
  summary: Byte order in output binary file Little endian (default) | Big endian
  group: ''
```

### **File name** — Name of the binary file `output.bin` (default) | file name

Specify the name of the output binary file, with a `.bin`
extension, for the video data. Click **Save As** to specify the
location for the file.

### **Video format** — Format of the video data `Four character codes` (default) | `Custom`

Specify the format of the video data as one of these options.

- Four character codes (FOURCC) — For more information about these codes, see
  `https://en.wikipedia.org/wiki/FourCC`.
- Custom — Read the video data from a binary file of a custom format.

### **Four character code** — Format of binary file `I420` (default) | `AYUV` | `CLJR` | `cyuv` | `GREY` | `IF09` | `IMC1` | `IMC2` | `IMC3` | `IMC4` | `IUYV` | `IY41` | `IYU1` | `IYU2` | `IYUV` | `NV12` | `NV21` | `UYNV` | `UYNY` | `V210` | `Y411` | `Y41P` | `Y41T` | `Y422` | `Y42T` | `Y8` | `Y800` | `YUNV` | `YUY2` | `YUYV` | `YV12` | `YV16` | `YVU9` | `YVYU` | ...

Select the four character code of the desired codec for the binary file. The value
of this parameter also determines the number of input ports on the block. For
information on which four character codes enable which input ports, see the table
below.

**Input Ports for Four Character Codes**

| Four Character Codes | Input Ports |
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

To enable this parameter, set the **Video Format** parameter to
`Four character codes`.

### **Line ordering** — Binary file fill direction `Top line first` (default) | `Bottom line first`

If you select `Top line first`, the block begins filling the
binary file with the first row of the video frame. It then fills the file with the other
rows in increasing order. If you select `Bottom line first`, the block
begins filling the binary file with the last row of the video frame. It then fills the
file with the other rows in decreasing order.

### **Bit stream format** — Data format of binary file `Planar` (default) | `Packed`

Specify the data format of the binary file as `Planar` or
`Packed`.

#### Dependencies

To enable this parameter, set the **Video Format** parameter to
**Custom**.

### **Number of inputs** — Number of components in input video stream `3` (default) | `1` | `2` | `4`

Specify the number of components in the input video stream. This parameter sets the
number of input ports.

#### Dependencies

To enable this parameter, set the **Video Format** parameter to
`Custom`.

### **Inherit size of components from input data type** — All components have same number of bits `on` (default) | `off`

Select the **Inherit size of components from input data type**
parameter to indicate that all of the components have the same number of bits as the
input data type. If you clear this parameter, you can specify the number of bits for
each enabled component using the associated **Bits** parameter.

#### Dependencies

To enable this parameter, set the **Video Format** parameter to
`Custom`.

### **Component1** — Name of luminance component input port `Y'` (default) | component name

Specify the name of the input port for the luminance component of the input video
stream.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of inputs**
parameter to `1` or greater.

### **Component2** — Name of blue difference component `Cb` (default) | component name

Specify the name of the input port for the blue difference component of the input
video stream.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of inputs**
parameter to `2` or greater.

### **Component3** — Name of red difference component `Cr` (default) | component name

Specify the name of the input port for the red difference component of the input
video stream.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of inputs**
parameter to `3` or greater.

### **Component4** — Name of alpha component `Alpha` (default) | component name

Specify the name of the input port for the alpha component of the input video
stream.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, set the **Number of inputs**
parameter to `4`.

### **Bits1** — Size of luminance component `8` (default) | `0` | `16` | `24` | `32`

Specify the size of the luminance component in the input video stream. The value of
this parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of inputs**
parameter to `1` or greater, and select the **Inherit
size of components from input data type** parameter.

### **Bits2** — Size of blue difference component `8` (default) | `0` | `16` | `24` | `32`

Specify the size of the blue difference component in the input video stream. The
value of this parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of inputs**
parameter to `2` or greater, and select the **Inherit
size of components from input data type** parameter.

### **Bits3** — Size of red difference component `8` (default) | `0` | `16` | `24` | `32`

Specify the size of the red difference component in the input video stream. The
value of this parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of inputs**
parameter to `3` or greater, and select the **Inherit
size of components from input data type** parameter.

### **Bits4** — Size of alpha component `8` (default) | `0` | `16` | `24` | `32`

Specify the size of the alpha component in the input video stream. The value of this
parameter determines the interpretation of the video stream data as
`8`-bit, `16`-bit, `24`-bit, or
`32`-bit.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`, and set the **Number of inputs**
parameter to `4`, and select the **Inherit size of
components from input data type** parameter.

### **Component order in binary file** — Arrangement of components in binary file [`1 2 3`] (default) | vector of valid component identifiers

Specify the arrangement of the components in the binary file. Identify the
components by the assigned numerals, from 1 to 4, in the desired order. You must include
all enabled components when setting this parameter.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Interlaced video** — Read video data as interlaced `off` (default) | `on`

Select this parameter when the video stream contains interlaced video data.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Write signed data to output file** — Write signed data to output binary file `off` (default) | `on`

Select this parameter when the input data is signed.

#### Dependencies

To enable this parameter, set the **Video format** parameter to
`Custom`.

### **Byte order in binary file** — Byte order in output binary file `Little endian` (default) | `Big endian`

Specify the byte order in the output binary file as either little endian or big
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

Write binary video data to file

The Write Binary File block takes the video data from a Simulink® model and exports it to a binary file.

This block produces a raw binary file with no header information. It has no encoded
information providing the data type, frame rate, or dimensionality. The video data for this
block appears in row-major format.

**Note**

This block supports code generation only for platforms that have file I/O available. The
block does not support code generation using Simulink
Desktop Real-Time™ or Simulink
Real-Time™.
