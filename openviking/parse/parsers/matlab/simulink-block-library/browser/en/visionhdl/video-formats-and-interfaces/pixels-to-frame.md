---
type: simulink-block
title: 'Pixels To Frame'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'pixelstoframe'
documentation_source_path: 'ref/pixelstoframe.html'
language: en
---

# Pixels To Frame

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector | matrix

For single pixel streams, specify **pixel** as a
scalar or a vector of 1-by-**Number of components**
values that represent a single pixel. For multipixel streams, specify
**pixel** as a matrix of **Number of
pixels**-by-**Number of components** pixel
intensity values. **Number of pixels** can be two,
four, or eight.**Number of components** can be from one
to four.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — Control signals associated with pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

For multipixel streaming, each vector of pixel values has one set of control signals.
Because the vector has only one `valid` signal, the pixels in the
vector must be either all valid or all invalid. The `hStart` and
`vStart` signals apply to the pixel with the lowest index in the
vector. The `hEnd` and `vEnd` signals apply to the
pixel with the highest index in the vector.

**Data Types:** `bus`
### Output

### **frame** — Full image frame array

Full image frame, returned as an **Active pixels per
line**-by-**Active video
lines**-by-*N* array. The first two array
dimensions are the height and width of the active image specified by the
**Video format** parameter. *N* is
the **Number of components** used to express a single
pixel. The output data type is the same as the data type of the
**pixel** port.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **validOut** — Indicates when output frame is ready scalar

This signal is 1 (`true`) when the block has
successfully recompiled an output frame from the input stream.

**Data Types:** `Boolean`

## Parameters

### **Number of components** — Number of values used to represent each pixel `1` (default) | `2` | `3` | `4`

Number of values used to represent each pixel. Each pixel can have from 1 to 4
components.

- For grayscale video, set this parameter to `1`.
- For color video, for example, {R,G,B} or {Y,Cb,Cr}, set this parameter to
  `3`.
- For color video with an alpha channel for transparency, set this parameter
  to `4`.

To process multicomponent streams for blocks that do not support multicomponent input, replicate the block for each component. The
`pixelcontrol` bus for all components is identical, so you can
connect the **ctrl** output of the Frame To Pixels block
to each replicated block.

### **Number of pixels** — Number of pixels streamed per time step `1` (default) | `2` | `4` | `8`

Number of pixels transferred on the streaming interface for each time step, specified
as `1`, `2`,
`4`, or `8`. To enable multipixel
streaming and increase throughput for high-resolution or high-frame-rate video, set this
parameter to `2`, `4` or
`8`. Multipixel streaming processes more pixels with the
same clock frequency as a single-pixel streaming interface.

| Video Resolution | Clock Frequency Required for Single-Pixel Streaming at 60 fps | Clock Frequency Required for Multipixel Streaming at 60 fps (4 pixels) |
| --- | --- | --- |
| 1080p | 150 MHz | 37.5 MHz |
| 4k UHD | 600 MHz | 150 MHz |
| 8k UHD | 1200 MHz | 300 MHz |

### **Video format** — Dimensions of active regions in a video frame `1080p` (default) | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

Dimensions of active regions in a video frame. To select a predefined
format, use the **Video format** pull-down menu. The active
frame dimensions are set as shown in the table. For a custom format, select
`Custom`, then specify the active frame dimensions as
integers.

| `Video Format` | `Active Pixels Per Line` | `Active Video Lines` |
| --- | --- | --- |
| `240p` | 320 | 240 |
| `480p` | 640 | 480 |
| `480pH` | 720 | 480 |
| `576p` | 720 | 576 |
| `720p` | 1280 | 720 |
| `768p` | 1024 | 768 |
| `1024p` | 1280 | 1024 |
| `1080p` (default) | 1920 | 1080 |
| `1200p` | 1600 | 1200 |
| `2KCinema` | 2048 | 1080 |
| `4KUHDTV` | 3840 | 2160 |
| `8KUHDTV` | 7680 | 4320 |
| `Custom` | User-  defined | User-  defined |

## Libraries

Vision HDL Toolbox / I/O Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for
Simulink® Accelerator and Rapid Accelerator modes.

## Version History

**Introduced in R2015a**

### R2022a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2020a: Multipixel-multicomponent streaming

The block now supports multipixel-multicomponent streams. The block accepts an
input matrix of *NumPixels*-by-*NumComponents*
pixels. The **ctrl** port remains scalar, and the control signals
in the `pixelcontrol` bus apply to all pixels in the matrix. The
MultiPixel-MultiComponent Video Streaming example
shows how to use a multipixel and multicomponent pixel stream to process a
high-resolution color image.

### R2019b: Multipixel streaming

The block now accepts pixel streams that have 4 or 8 pixels per clock cycle. You
can set the **Number of pixels** parameter to
`4` or `8`. With this setting,
the block expects an input vector of 4 or 8 pixel values on each time step. For an
example of how to use this feature, see Filter Multipixel Video Streams.

## Description

Convert pixel stream to frame-based video

The Pixels To Frame block converts a color or grayscale pixel stream
and control signals to frame-based video. The control signal bus indicates the validity
of each pixel and its location within the frame. The pixel stream format can include
padding pixels around the active frame. You can configure the frame and padding
dimensions by selecting a common video format or by specifying custom dimensions. The
pixel input can support single pixel streaming, or multipixel streaming. Multipixel
streaming accepts 2, 4, or 8 pixels each clock cycle to support high-rate or
high-resolution formats. For details of the pixel stream format, see Streaming Pixel Interface.

This block itself does not support HDL code generation. However, you can use this
block to convert the output of a separate subsystem, targeted for HDL code generation,
back to frames.

If your model converts frames to a pixel stream and later converts the stream back to
frames, specify the same video format for the Frame To Pixels block and
the Pixels To Frame block.
