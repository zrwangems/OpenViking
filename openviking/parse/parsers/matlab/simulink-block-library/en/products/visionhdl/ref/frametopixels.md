---
type: simulink-block
title: 'Frame To Pixels'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'frametopixels'
documentation_source_path: 'ref/frametopixels.html'
language: en
---

# Frame To Pixels

## Ports

### Input

### **frame** — Full image frame array

Full image frame, specified as an **Active pixels per
line**-by-**Active video
lines**-by-*N* array. The first two array
dimensions are the height and width of the active image specified by the
**Video format** parameter. *N* is
the **Number of components** used to express a single
pixel. **Number of components** can be one, three, or
four.

**Data Types:** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`
### Output

### **pixel** — Image pixel or pixels scalar | vector

For single pixel streams, **pixel** is a single image
pixel returned as a scalar or a vector of 1-by-**Number of
components** values. For multipixel streams,
**pixel** is a matrix of **Number of
pixels**-by-**Number of components** pixel
intensity values.

The output data type is the same as the data type of the
**frame** port.

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

## Parameters

### **Number of components** — Number of values used to represent each pixel `1` (default) | `3` | `4`

Number of values used to represent each pixel. Each pixel can have 1, 3,
or 4 components.

- For grayscale video, set this parameter to
  `1`.
- For color video, for example, {R,G,B} or {Y,Cb,Cr}, set this
  parameter to `3`.
- For color video with an alpha channel for transparency, set
  this parameter to `4`.

To process multicomponent streams for blocks that do not support
multicomponent input, replicate the block for each component. The
`pixelcontrol` bus for all components is identical, so
you can connect the **ctrl** output of the Frame To
Pixels block to each replicated block.

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

### **Video format** — Dimensions of active and inactive regions in video frame `1080p` (default) | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

Dimensions of active and inactive regions in a video frame. To select a predefined
format, select from the **Video format** list. The actual frame
dimensions are displayed in the **Video Format Parameters** section.
For a custom format, select `Custom`, and then specify the dimensions
as integers.

The dimensions are defined in the diagram.

**Note**

The sample time of your video source must match the total number of pixels in the
frame of your Frame To Pixels block. The total number of pixels is
*Total pixels per line* × *Total video lines*,
so set the sample time to this value.

If your frame size is large, you may reach the fixed-step solver step size limit
for sample times in Simulink®, and receive an error like this.

```
The computed fixed step size (1.0) is 1000000.0 times smaller than all
the discrete sample times in the model.
```

You
can avoid this error by choosing the variable-step solver.

| `Video Format` | `Active Pixels Per Line` | `Active Video Lines` | `Total Pixels Per Line` | `Total Video Lines` | `Starting Active Line` | `Ending Active Line` | `Front Porch` | `Back Porch` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `240p` | 320 | 240 | 402 | 324 | 1 | 240 | 44 | 38 |
| `480p` | 640 | 480 | 800 | 525 | 36 | 515 | 16 | 144 |
| `480pH` | 720 | 480 | 858 | 525 | 33 | 512 | 16 | 122 |
| `576p` | 720 | 576 | 864 | 625 | 47 | 622 | 12 | 132 |
| `720p` | 1280 | 720 | 1650 | 750 | 25 | 744 | 110 | 260 |
| `768p` | 1024 | 768 | 1344 | 806 | 10 | 777 | 24 | 296 |
| `1024p` | 1280 | 1024 | 1688 | 1066 | 42 | 1065 | 48 | 360 |
| `1080p` (default) | 1920 | 1080 | 2200 | 1125 | 42 | 1121 | 88 | 192 |
| `1200p` | 1600 | 1200 | 2160 | 1250 | 50 | 1249 | 64 | 496 |
| `2KCinema` | 2048 | 1080 | 2750 | 1125 | 42 | 1121 | 639 | 63 |
| `4KUHDTV` | 3840 | 2160 | 4400 | 2250 | 42 | 2201 | 88 | 472 |
| `8KUHDTV` | 7680 | 4320 | 8800 | 4500 | 42 | 4361 | 88 | 1032 |
| `Custom` | User-  defined | User-  defined | User-  defined | User-  defined | User-  defined | User-  defined | User-  defined | User-  defined |

When using a custom format, the values you enter for the active and inactive
dimensions of the image must add up to the total frame dimensions. If you specify a
format that does not conform to these rules, the block reports an error.

- For the horizontal direction, **Total pixels per line** must
  be greater than or equal to **Front porch** + **Active
  pixels per line**. The block calculates **Back
  porch** = **Total pixels per line** −
  **Front porch** − **Active pixels per
  line**.
- For the vertical direction, **Total video lines** must be
  greater than or equal to **Starting active line** +
  **Active video lines** − 1. The block calculates
  **Ending active line** = **Starting active
  line** + **Active video lines** − 1.

When using the Line
Buffer block, or blocks that use an internal line buffer, with a custom
video format, further requirements apply:

- The horizontal blanking interval, or **Back porch** +
  **Front porch**, must meet these guidelines:

  - The total of **Back porch** + **Front
    porch** must be at least 2 times the largest kernel
    size of the algorithm in the blocks following the Frame To
    Pixel block.
  - If the kernel size is less than 4, and you are using edge padding,
    the total porch must be at least 8 pixels.
  - If you disable padding, the total porch must be at least 12
    pixels.
  - The **Back porch** must be at least 6 pixels.
    This parameter is the number of inactive pixels before the first
    valid pixel in a frame.

  For more information on blanking intervals, see Configure Blanking Intervals.

When using multipixel streaming (**Number of pixels** > 1), these
requirements apply.

- The video format must have horizontal dimensions divisible by the
  **Number of pixels** parameter value. The horizontal
  dimensions are set by these parameters: **Active pixels per
  line**, **Total pixels per line**,
  **Front porch**, and **Back porch**.
  Standard video protocols 480p, 768p, 1024p, 1080p, 1200p, 4k UHD, and 8k UHD
  support **Number of pixels** equal to 4 or 8.
- The minimum input frame size for multipixel streaming is 18 rows by 32
  columns.
- Choose your kernel size and **Active pixels per line**
  such that (**Active pixels per line**)/(**Number of
  pixels**) is at least the kernel width.

## Libraries

Vision HDL Toolbox / I/O Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for
Simulink Accelerator and Rapid Accelerator modes.

## Version History

**Introduced in R2015a**

### R2022a: Two pixels-per-clock streaming

The block can now generate multipixel streams that have 2 pixels per clock cycle.

### R2020a: Multipixel-multicomponent streaming

The block can now generate multipixel-multicomponent streams. The MultiPixel-MultiComponent Video Streaming example
shows how to use a multipixel and multicomponent pixel stream to process a
high-resolution color image.

### R2019b: Multipixel streaming

The block can now generate multipixel streams. You can set the **Number of
pixels** parameter to `4` or
`8`. With this setting, the output of the block is a
vector of 4 or 8 pixel values on each time step. For an example of how to use this
feature, see Filter Multipixel Video Streams.

Video formats for multipixel streams must have horizontal dimensions divisible by
the **Number of pixels** parameter value. These horizontal
dimensions are set by the following parameters: **Active pixels per
line**, **Total pixels per line**, **Front
porch**, and **Back porch**. Standard video protocols
480p, 720p, 1080p, and 4k UHD support either 4 or 8 pixels at a time.

## Description

Convert frame-based video to pixel stream

The Frame To Pixels block converts color or grayscale video frames to a
pixel stream and control signals. The control signals indicate the validity of each
pixel and its location in the frame. The pixel stream format can include padding pixels
around the active frame. You can configure the frame and padding dimensions by selecting
a common video format or by specifying custom dimensions. The pixel stream can support
single pixel streaming or multipixel streaming. Multipixel streaming provides 2, 4, or 8
pixels per clock cycle to support high-rate or high-resolution formats. For details of
the pixel stream format, see Streaming Pixel Interface.

This block itself does not support HDL code generation. However, you can use this
block to generate input for a separate subsystem targeted for HDL code
generation.

If your model converts frames to a pixel stream and later converts the stream back to
frames, specify the same video format for the Frame To Pixels block and
the Pixels To Frame block.
