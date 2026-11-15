---
type: simulink-block
title: 'RTSP Video Stream Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'rtspvideostreamtransmit'
documentation_source_path: 'supportpkg/raspberrypi_ref/rtspvideostreamtransmit.html'
language: en
---

# RTSP Video Stream Transmit

## Ports

### Input

### **R** — Red component of input video matrix

Red channel signal of the RGB video to stream, specified as an *M*-by-*N* grid of pixels.
Here, *M* is the number of rows and *N* is the number of columns for the red component.

#### Dependencies

To enable this port, set **Input image format** to
`RGB`.

**Data Types:** `uint8`

### **G** — Green component of input video matrix

Green channel signal of the RGB video to stream, specified as an *M*-by-*N* grid of pixels.
Here, *M* is the number of rows and *N* is the number of columns for the green component.

#### Dependencies

To enable this port, set **Input image format** to
`RGB`.

**Data Types:** `uint8`

### **B** — Blue component of input video matrix

Blue channel signal of the RGB video to stream, specified as an *M*-by-*N* grid of pixels.
Here, *M* is the number of rows and *N* is the number of columns for the blue component.

#### Dependencies

To enable this port, set **Input image format** to
`RGB`.

**Data Types:** `uint8`

### **Y** — Luma component of input video matrix

Luminance component of the input video to stream, specified as an *M*-by-*N* grid of pixels.
Here, *M* is the number of rows and *N* is the number of columns for the luminance
component.

#### Dependencies

To enable this port, set **Input image format** to
`YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cb** — Blue difference chroma component of input video matrix

Blue difference chroma component of the input video to stream, specified as an
*M*-by-*N* grid of
pixels. Here, *M* is the number of rows and *N* is the number of columns for the blue difference chroma
component.

#### Dependencies

To enable this port, set **Input image format** to
`YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cr** — Red difference chroma component of input video matrix

Red difference chroma component of the input video to stream, specified as an
*M*-by-*N* grid of
pixels. Here, *M* is the number of rows and *N* is the number of columns for the red difference chroma
component.

#### Dependencies

To enable this port, set **Input image format** to
`YCbCr 4:2:2`.

**Data Types:** `uint8`

### **I** — Grayscale input video matrix

Grayscale input video signal to stream, specified as an *M*-by-*N* grid of pixels. Here,
*M* is the number of rows and *N* is the number of columns for the grayscale input
video.

#### Dependencies

To enable this port, set **Input image format** to
`Grayscale`.

**Data Types:** `uint8`

## Parameters

### Video parameters

### **Input image format** — Input video stream format `RGB` (default) | `YCbCr 4:2:2` | `Grayscale`

Specify the format of the input video stream.

**Tip**

To view a color video on your device, set this parameter to `YCbCr
4:2:2`. Because this format requires less bandwidth, you can stream
the video without significantly affecting the video quality.

### **Output resolution** — Image resolution `Specify` (default) | `Inherit from input image`

Select the output image resolution.

- `Specify` — Manually specify the input image
  resolution in the **Image size ([width, height])** parameter.
  Using this option, you can either increase or decrease the resolution of the
  output video stream. When you specify a higher resolution, the execution speed
  of a Simulink model decreases.
- `Inherit from input image` — The block inherits the
  resolution of the input image.

### **Image size ([width, height])** — Image resolution `[640, 480]` (default) | [`width`, `height`]

Specify the resolution of the input image, in pixels.

#### Dependencies

To enable this parameter, set **Output resolution** to
`Specify`.

### **Video stream encoding** — Encoding format for video stream `H264` (default) | `JPEG`

Select the encoding format for the real-time streaming protocol (RTSP) video
stream.

### **Frame rate (in fps)** — Frame rate of input video `24` (default) | positive integer

Specify the frame rate of the input video signal, in frames per second.

### RTSP stream connection parameters

### **Port number** — Port on Raspberry Pi board to stream video `8554` (default) | positive integer in the range [`1`,`65535`]

Specify the Raspberry Pi hardware port number from which you want to stream the video.

### **Mount point** — Video identifier `stream01` (default) | char | string

Specify a unique identifier to create an RTSP URL for a video stream.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Stream video to network over real-time streaming protocol

Use the RTSP Video Stream Transmit block to stream video to network over
real-time streaming protocol (RTSP). You can stream grayscale, RGB, or YCbCr video over a
network and view it on devices connected to the same network. You can also encode the video
stream using the H264 or JPEG standards.

**Note**

- When using this block in a Simulink® model, use a minimum of 256 MB of Raspberry Pi® GPU memory to avoid any deterioration in the video feed using the RTSP
  protocol.
- To generate C/C++ code for this block, you must have an Embedded Coder® license.
