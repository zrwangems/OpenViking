---
type: simulink-block
title: 'Video Send'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'videosend'
documentation_source_path: 'nvidia/ref/videosend.html'
language: en
---

# Video Send

## Ports

### Input

### **Image** — RGB or grayscale image signal to stream *M*-by-*N*-by-*3* matrix | *M*-by-*N* matrix

RGB or grayscale image signal to stream, specified as an
*M*-by-*N*-by-*3* matrix or
*M*-by-*N* matrix, respectively.

#### Dependencies

The `Image Signal` parameter must be set to `One
multidimensional signal`.

**Data Types:** `uint8` | `uint16`

### **R** — Red channel signal of the RGB image to stream *M*-by-*N* matrix.

Red channel signal of the RGB image to stream, specified as an
`M-by-N` matrix.

#### Dependencies

The `Image Signal` parameter must be set to
`Separate color signals`.

**Data Types:** `uint8`

### **G** — Green channel signal of the RGB image to stream *M*-by-*N* matrix

Green channel signal of the RGB image to stream, specified as an
`M-by-N` matrix.

#### Dependencies

The `Image Signal` parameter must be set to
`Separate color signals`.

**Data Types:** `uint8`

### **B** — Blue channel signal of the RGB image to stream *M*-by-*N* matrix

Blue channel signal of the RGB image to stream, specified as an
`M-by-N` matrix.

#### Dependencies

The `Image Signal` parameter must be set to
`Separate color signals`.

**Data Types:** `uint8`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Video parameters

### **Format** — Input video stream signal format `RGB` (default) | `Grayscale`

Specify the input video stream signal format as one of the following:

- `RGB` - RGB image (8-bit per color channel).
- `Grayscale` - Grayscale image (8-bit).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ImageFormat` |
| **Values:** | `'RGB'` (default) | `'Grayscale'` |

### **Image signal** — Nature of the RGB image input signal `One multidimensional signal` (default) | `Separate color signals`

Specify the nature of the RGB image input signal as one of the following:

- `One multidimensional signal` - One input port for an
  *M*-by-*N*-by-*3* color video
  signal with R, G, and B color channels.
- `Separate color signals` - Three separate input ports
  for R,G and B channels. Each port accepts one
  *M*-by-*N* matrix.

#### Dependencies

The `Format` parameter must be set to
`RGB`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `ImageSignal` |
| **Values:** | `'One multidimensional signal'` (default) | `'Separate color signal'` |

### **Compression** — Compression format for the video stream `JPEG` (default) | `H264` | `H265` | `VP8` | `VP9` | `None (uncompressed)`

Specify the compression format for the video stream.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Compression` |
| **Values:** | `'JPEG'` (default) | `'VP8'` | `'VP9'` | `'H264'` | `'H265'` | `'None (uncompressed)'` |

### **Quality** — Quality of the video stream 85 (default) | positive scalar in the range [0,100]

Specify the quality of the JPEG video stream as a positive scalar. This parameter
controls the encoding speed and compression ratio of the video stream. A higher quality
value increases the image quality at the expense of a higher network bandwidth. Specify
a lower value for low-bandwidth network connections.

#### Dependencies

The `Compression` parameter must be set to
`JPEG`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `JPEGQuality` |
| **Values:** | 85 (default) | positive scalar in the range [0,100] |

### **Enable hardware acceleration** — Use graphics hardware for encoding `on` (default) | off

Select this parameter to enable use of graphics hardware on the NVIDIA® target for encoding.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `UseHWAcceleration` |
| **Values:** | `'on'` (default) | `'off'` |

#### Connection parameters

### **Remote address** — Remote IP address 127.0.0.1 (default) | valid IP address

Specify the IP address or host name of the remote device, to which the block sends
the message, as a character vector.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RemoteAddress` |
| **Values:** | `127.0.0.1` (default) | valid IP address in quotes |

### **Remote port** — Remote IP port 3000 (default) | integer from 0 to 65535

Specify the IP port of the remote device, to which the block sends the message. When
streaming the video, this block picks the first available local UDP port, independent of
the remote port you specify.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `RemotePort` |
| **Values:** | `3000` (default) | integer from 0 to 65535 |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Send video stream to remote hardware

The Video Send block sends video streams from Simulink® to a specified remote device. You can send grayscale and RGB images to the
remote device and specify the compression and quality of the video stream. This block uses the
GStreamer framework to handle
data streaming.
