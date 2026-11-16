---
type: simulink-block
title: 'Network Video Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'networkvideoreceive'
documentation_source_path: 'nvidia/ref/networkvideoreceive.html'
language: en
---

# Network Video Receive

## Ports

### Output

### **Image** — Image signal matrix

This port outputs the image signal of each pixel.

#### Dependencies

This port appears when you select `RGB` for
**Format** and `One multidimensional
signal` for **Image signal** or when you select
`Grayscale` for **Format** in the block
parameters window.

**Data Types:** `uint8` | `uint16`

### **R** — Red component of the output video stream matrix

This port outputs the red component of each pixel.

#### Dependencies

This port appears only when you select `RGB` for
**Format** and `Separate color signal`
for **Image signal** in the block parameters window.

**Data Types:** `uint8`

### **G** — Green component of the output video stream matrix

This port outputs the green component of each pixel.

#### Dependencies

This port appears only when you select `RGB` for
**Format** and `Separate color signal`
for **Image signal** in the block parameters window.

**Data Types:** `uint8`

### **B** — Blue component of the output video stream matrix

This port outputs the blue component of each pixel.

#### Dependencies

This port appears only when you select `RGB` for
**Format** and `Separate color signal`
for **Image signal** in the block parameters window.

**Data Types:** `uint8`

## Parameters

### Video Parameters

### **Video source** — Video stream source `Network stream` (default) | `Network device`

Specify the source of the video stream.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VideoSource` |
| **Type:** character vector |
| **Values:** `'Network stream'`|`'Network device'` |
| **Default:**  `'Network stream'` |

### **Image size** — Image resolution `[320, 240]` (default) | `[width, height]`

Specify the resolution of the image to be captured, in pixels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImageSize` |
| **Type:** character vector |
| **Values:** `[width, height]`| |
| **Default:**  `'[320, 240]'` |

### **Format** — Video stream format `Grayscale (16-bit)` | `Grayscale` | `RGB`

Specify the format of the video stream. The format options are based on the value
set for **Video source**.

|  | Network stream | Network device |
| --- | --- | --- |
| Available stream formats | `'Grayscale (16-bit)'` (Default) | `'Grayscale'` |
| `'Grayscale'` | `'RGB'` (Default) |
| `'RGB'` | - |
| Block parameter name | `'ImageFormat'` | `'DeviceImageFormat'` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImageFormat`|`DeviceImageFormat` |
| **Type:** character vector |
| **Values:** `'RGB'`|`'Grayscale'`|`'Grayscale (16-bit)'` |

### **Image signal** — Output signal format `One multidimensional signal` (default) | `Separate color signal`

Specify how to output RGB color video signal. If you select `One
multidimensional signal`, the block outputs an M-by-N-by-P color video
signal, where P is the number of color planes, at the `Image` port.
If you select `Separate color signal`, additional ports
appear on the block. Each port outputs one M-by-N plane of an RGB video stream.

#### Dependencies

To enable this parameter, set **Format** to
`RGB`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ImageSignal` |
| **Type:** character vector |
| **Values:** `'One multidimensional signal'`|`'Separate color signal'`| |
| **Default:**  `'One multidimensional signal'` |

### **Compression** — Video compression algorithm `JPEG` | `VP8` | `VP9` | `H264` | `H265` | `None (uncompressed)`

Select the type of compression algorithm to use for decoding the RTP video stream.
The compression options are based on the value set for **Video
source**.

|  | Network stream | Network device |
| --- | --- | --- |
| Available compression algorithms | `'JPEG'` (Default) | `'H264'` (Default) |
| `'VP8'` | `'H265'` |
| `'VP9'` | - |
| `'H264'` | - |
| `'H265'` | - |
| `'None (uncompressed)'` | - |
| Block parameter name | `'Decoder'` | `'VideoDeviceDecoder'` |

**Note**

When selecting `H265` decoder, the receiver must be started
before the sender starts the video stream. This is because metadata required to
decode the data is emitted at the start of the stream. Alternatively, you can
configure the sender to insert this metadata at intervals within the stream. For
example, when using GStreamer, use the following
command,

```
gst-launch-1.0 -v videotestsrc is-live=true ! video/x-raw,
framerate=100/1,width=320,height=240 ! videoconvert
! x265enc tune=zerolatency ! h265parse config-interval=2
! rtph265pay ! udpsink host=127.0.0.1 port=3000
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decoder` | `VideoDeviceDecoder` |
| **Type:** character vector |
| **Values:** `'JPEG'`|`'VP8'`|`'VP9'`|`'H264'`|`'H265'`|`'None (uncompressed)'` |

### **Enable hardware acceleration** — Use graphics hardware for decoding `on` (default) | off

Select this parameter to enable use of graphics hardware on the NVIDIA® target for decoding.

**Note**

When hardware acceleration is enabled, the image resolution is automatically
scaled if the sender and receiver specifications for resolution are different. If
you disable hardware acceleration, the automatic scaling is also disabled. In such
cases, the image resolution specification at the sender and receiver must be the
same.

If the video frame size is not a multiple of 16, the hardware accelerator
libraries pads the borders of the received video frame to output the requested size.
If this behavior is not desired, disable hardware acceleration.

### Connection Parameters

### **Port** — Port on NVIDIA board to receive data `3000` | positive integer in the range `[1,65535]`

Specify the port number from which you want to receive the video packets. Match
the local port number with the remote port number of the sending host.

#### Dependencies

To enable this parameter, set **Video source** to
`Network stream`.

### **RTSP URL** — RTSP URL of the IP camera `char` | `string`

RTSP URL of the IP camera, specified as a character vector.

#### Dependencies

To enable this parameter, set **Video source** to
`Network device`.

### **Sample time** — Frequency at which a new image is captured `0.1` (default) | scalar | `vector`

Select the sample time of the video device.

Smaller values require the processor to complete the same number of instructions
in less time, which can cause task overruns.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0.1'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Receive video from a network RTP or IP camera RTSP stream

Receives video from a network RTP or an IP camera RTSP stream. When running on hardware,
the block outputs video from the network or IP camera.
