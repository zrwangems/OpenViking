---
type: simulink-block
title: 'Video Send'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine 3-D Simulation'
documentation_page: 'videosend'
documentation_source_path: 'ref/videosend.html'
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

#### Video parameters

### **Format** — Input video stream signal format `RGB` (default) | `Grayscale` | `Grayscale (16-bit)`

Specify the input video stream signal format as one of the following:

- `RGB` - RGB image (8-bit per color channel).
- `Grayscale` - Grayscale image (8-bit).
- `Grayscale (16-bit)` - Grayscale image
  (16-bit).

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

### **Compression** — Compression format for the video stream `JPEG` (default) | `VP8` | `VP9`

Specify the compression format for the video stream as one of the following:

- `JPEG` - Uses jpeg GStreamer plugin.

  - This uses the following GStreamer pipeline:

    ```
    video/x-raw,format=I420 ! jpegenc quality=<Quality> idct-method=1 ! rtpjpegpay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```
- `VP8` - Uses vpx GStreamer plugin.

  - This uses the following GStreamer pipeline:

    ```
    vp8enc deadline=<Max frame time*1000> bits-per-pixel=0.0434 target-bitrate=0 threads=8 lag-in-frames=0 ! rtpvp8pay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```
- `VP9` - Uses vpx GStreamer plugin.

  - This uses the following GStreamer pipeline:

    ```
    vp9enc deadline=<Max frame time*1000> bits-per-pixel=0.0434 target-bitrate=0 threads=8 lag-in-frames=0 ! rtpvp9pay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```

### **Quality** — Quality of the video stream 85 (default) | `0`-`100`

Specify the quality of the JPEG video stream as a positive scalar. This parameter
controls the encoding speed and compression ratio of the video stream. A higher quality
value increases the image quality at the expense of a higher network bandwidth. Specify
a lower value for low-bandwidth network connections.

#### Dependencies

The `Compression` parameter must be set to
`JPEG`.

### **Max frame time (ms)** — Maximum time per frame 30 (default) | non-negative integer

Specify the maximum frame time of the VP8 or VP9 video stream in milliseconds, as a
positive integer. This parameter controls the maximum processing time that the codec
uses to encode an image. Set this parameter based on the frame rate of the input
`Image`. A good starting point value is
`1000/fps`, where `fps` is the sample rate of the
input video signal. Set 0 if you want the encoder to take as long as it needs, which
will increase the quality at the expense of time required for compression.

#### Dependencies

The `Compression` parameter must be set to
`VP8` or `VP9`.

#### Connection parameters

### **Remote address** — Remote IP address 127.0.0.1 (default) | character vector

Specify the IP address or host name of the remote device, to which the block sends
the message, as a character vector.

### **Remote port** — Remote IP port 5004 (default) | 0-65535

Specify the IP port of the remote device, to which the block sends the message. When
streaming the video, this block picks the first available local UDP port, independent of
the remote port you specify.

## Libraries

UAV Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Send video stream to remote hardware

The Video Send block sends video streams from Simulink® to a specified remote device. For hardware-in-the-loop simulation applications,
you can send grayscale and RGB images, as well as depth and lidar point cloud data collected
from Unreal Engine® scenes to the remote device. You can also specify the compression and quality of
the video stream. To stream the video, this block picks the first available local UDP port,
independent of the remote port you specify. This block uses the Gstreamer framework to handle data
streaming.
