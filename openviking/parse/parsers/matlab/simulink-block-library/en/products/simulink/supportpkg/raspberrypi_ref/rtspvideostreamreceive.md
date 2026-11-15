---
type: simulink-block
title: 'RTSP Video Stream Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'rtspvideostreamreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/rtspvideostreamreceive.html'
language: en
---

# RTSP Video Stream Receive

## Ports

### Output

### **Status** — Status of stream video scalar

The port outputs the status of the RTSP Video Stream Receive block
upon the video reception from the transmitter.

- `0` — Indicates a successful read operation of the video
  stream over the network.
- `1` — Indicates an interrupted stream from the transmitter
  which further results that the RTSP Video Stream Receive block
  cannot read any further data from the transmitter.
- `2` — Indicates a stream error that requires user
  intervention to fix it, for example, the Raspberry Pi® hardware fails to receive data from the transmitter.
- `3` — Indicates a GStreamer pipeline creation error that
  can occur due to misconfiguration of stream URL or image properties.
- `4` — Indicates a fatal error that prevents the further
  execution of the block, for example, an internal program failure.

**Data Types:** `int32`

### **R** — Red component of output video matrix

Red channel signal of the RGB video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the red component.

#### Dependencies

- To enable this port, set **Image format** to
  `RGB`.

**Data Types:** `uint8`

### **G** — Green component of output video matrix

Green channel signal of the RGB video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the green component.

#### Dependencies

- To enable this port, set **Image format** to
  `RGB`.

**Data Types:** `uint8`

### **B** — Blue component of output video matrix

Blue channel signal of the RGB video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the blue component.

#### Dependencies

- To enable this port, set **Image format** to
  `RGB`.

**Data Types:** `uint8`

### **Y** — Luma component of output video matrix

Luminance component of video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the luminance
component.

#### Dependencies

- To enable this port, set **Image format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cb** — Blue difference chroma component of output video matrix

Blue difference chroma component of video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the blue difference chroma
component.

#### Dependencies

- To enable this port, set **Image format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cr** — Red difference chroma component of output video matrix

Red difference chroma component of video, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the red difference chroma
component.

#### Dependencies

- To enable this port, set **Image format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **I** — Grayscale output video matrix

Grayscale video, specified as an *M*-by-*N* grid of pixels. Here, *M* is the number of rows and *N* is the
number of columns for the grayscale video.

#### Dependencies

- To enable this port, set **Image format** to
  `Grayscale`.

**Data Types:** `uint8`

## Parameters

### **RTSP URL** — RTSP stream URL `rtsp://127.0.0.1:8554/stream01` (default) | char | string

Specify a unique RTSP URL to receive the video stream in this format:
`rtsp://<raspberrypi IP address>/<mount point
identifier>`

### **Image format** — Output video stream format `RGB` (default) | `YCbCr 4:2:2` | `Grayscale`

Specify the format of the output video stream.

**Tip**

To view a color video on your device, set this parameter to `YCbCr
4:2:2`. Because this format requires less bandwidth, you can stream the
video without significantly affecting the video quality.

### **Image size** — Image resolution of video frames `640x480` (default) | `160x120` | `320x240` | `800x600` | `1280x720` | `custom`

Specify image resolution of the video frames, in pixels.

### **Image size ([width, height])** — Custom image resolution `[640, 480]` (default) | [`width`, `height`]

Specify customized resolution of the output image, in pixels.

#### Dependencies

- To enable this parameter, set **Image size** to
  `custom`.

### **Video compression** — Decoding format for video stream `H264` (default) | `JPEG`

Select decoding format for the real-time streaming protocol (RTSP) video
stream.

### **Sample time** — Time frequency at which block outputs image frame `0.1` (default) | scalar

Specify how often the block outputs an image frame from the video stream.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Receive video from network over real-time streaming protocol

Use the RTSP Video Stream Receive block to receive a real-time streaming
protocol (RTSP) video stream from a network from a streaming source. You can create a source
to stream the video over a network using either the RTSP Video Stream
Transmit block or any other RTSP streaming device. The block outputs either a
grayscale, RGB, or YCbCr video. The block can decode the video stream using the H264 or JPEG
video encoding standards.

**Note**

To generate C/C++ code for this block, you must have an Embedded Coder® license.
