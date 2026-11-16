---
type: simulink-block
title: 'FIL Frame To Pixels'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation and Deployment'
documentation_page: 'filframetopixels'
documentation_source_path: 'ref/filframetopixels.html'
language: en
---

# FIL Frame To Pixels

## Ports

### Input

### **frame** — Full image frame matrix

Full image specified as a (**Active pixels per
line**)-by-(**Active video
lines**)-by-*N* matrix. Height and width
are the dimensions of the active image specified in **Video
format**. *N* is the **Number of
components** used to express a single pixel.

**Data Types:** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`
### Output

### **data1,...,dataN** — Image pixels vector | matrix

Image pixels, returned as a matrix of
*M*-by-**Number of pixels**
values, where *M* is the width of the **Output
vector format**. There are *N* data ports,
where *N* is the **Number of
components**. The data type is the same as the data type of
**frame**.

When you use multipixel streaming, the FIL DUT has **Number of
pixels** data ports. You must split the output matrix into
**Number of pixels** row vectors of length
*M* for the FIL DUT input ports. For details, see
FPGA-in-the-Loop Simulation with Multipixel Streaming.

Similarly, when you use multipixel-multicomponent streaming, the FIL
DUT has **Number of pixels**×**Number of
components** data ports. Split the output matrix for each
component into **Number of pixels** row vectors of
length *M* for the FIL DUT input ports.

**Data Types:** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`

### **hStartOut** — First pixel in horizontal line of frame vector

First pixel in a horizontal line of a frame, returned as a
`Boolean` vector of *M* values.

For multipixel streaming, **hStartOut** applies to
the pixel with the lowest index in the corresponding column.

**Data Types:** `Boolean`

### **hEndOut** — Last pixel in horizontal line of frame vector

Last pixel in a horizontal line of a frame, returned as a
`Boolean` vector of *M*
values.

For multipixel streaming, **hEndOut** applies to the
pixel with the highest index in the corresponding column.

**Data Types:** `Boolean`

### **vStartOut** — First pixel in first (top) line of frame vector

First pixel in the first (top) line of a frame, returned as a
`Boolean` vector of *M* values.

For multipixel streaming, **vStartOut** applies to
the pixel with the lowest index in the corresponding column.

**Data Types:** `Boolean`

### **vEndOut** — Last pixel in last (bottom) line of frame vector

Last pixel in the last (bottom) line of a frame, returned as a
`Boolean` vector of *M*
values.

For multipixel streaming, **vEndOut** applies to the
pixel with the highest index in the corresponding column.

**Data Types:** `Boolean`

### **validOut** — Valid pixel indicator vector

Valid pixel indicator, returned as a `Boolean` vector
of *M* values.

For multipixel streaming, the pixels in the corresponding column are
either all valid or all invalid.

**Data Types:** `Boolean`

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

### **Number of pixels** — Number of pixels in each column of output matrix `1` (default) | `2` | `4` | `8`

Number of pixels in each column of the output matrix, specified as
`1`, `2`,
`4`, or `8`.

Each data port returns a *M*-by-**Number of
pixels** matrix. You must split this matrix into
**Number of pixels** row vectors of length
*M* for input to the FIL DUT. For details, see FPGA-in-the-Loop Simulation with Multipixel Streaming.

### **Output vector format** — Size of vector used to communicate with FPGA subsystem `Frame` (default) | `Line` | `Pixel`

Size of the vector used to communicate with the FPGA subsystem. The block
returns input pixels and control signals in vectors of the same length. The
block calculates the length of the vectors based on the **Video
format** parameter.

- `Pixel` — Return scalar values for
  pixel and control signals.
- `Line` — Return (**Total
  pixels per line**)-by-1 vectors.
- `Frame` — Return (**Total
  pixels per line** × **Total video
  lines**)-by-1 vectors.

A larger value results in faster communication between the
FPGA board and Simulink. Choose the largest option that the I/O and memory resources
on your board can support.

For multipixel streaming, specify one of these options for output size.

- `Pixel` — Return a
  1-by-(**Number of pixels**) vector of pixel
  values, and scalar control signals that apply to all the pixels
  in each vector.
- `Line` — Return a (**Total
  pixels per line**/**Number of
  pixels**)-by-**Number of pixels**
  matrix of pixel values, and a vector of control signals of
  length (**Total pixels per
  line**)/(**Number of pixels**).
- `Frame` — Return a (**Total
  pixels per line** × **Total video
  lines**/**Number of pixels**)-by
  **Number of pixels** matrix of pixel values
  and a vector of control signals of length (**Total
  pixels per line** × **Total video
  lines**)/**Number of
  pixels**.

#### Dependencies

When **Number of pixels** and **Number of
components** are both greater than 1, you must set
**Output vector format** to
`Frame`.

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
for sample times in Simulink, and receive an error like this.

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

### R2020b: Multipixel-multicomponent streaming

The block can now generate multipixel-multicomponent streams. When you use
multipixel-multicomponent streaming, the FIL DUT has **Number of
pixels**×**Number of components** data ports. Split
the output matrix for each component into **Number of pixels** row
vectors of length *M* for the FIL DUT input ports.

### R2019b: Multipixel streaming

The block can now generate multipixel streams. You can set the **Number of
pixels** parameter to `4` or
`8`. With this setting, the output of the block is a
vector of 4 or 8 pixel values on each time step. For an example of how to use this
feature, see FPGA-in-the-Loop Simulation with Multipixel Streaming.

Video formats for multipixel streams must have horizontal dimensions divisible by
the **Number of pixels** parameter value. These horizontal
dimensions are set by the following parameters: **Active pixels per
line**, **Total pixels per line**, **Front
porch**, and **Back porch**. Standard video protocols
480p, 720p, 1080p, and 4k UHD support either 4 or 8 pixels at a time.

## Description

Convert frame-based video to pixel stream for FPGA-in-the-loop

The FIL Frame To Pixels block performs the same frame-to-pixel
conversion as the Frame To Pixels block. In addition, you
can configure the width of the output vector to be a single pixel, a line, or an entire
frame. The block returns control signals in vectors of the same width as the pixel data.
This optimization makes more efficient use of the communication link between the FPGA
board and your Simulink® simulation when using FPGA-in-the-loop (FIL). To run FPGA-in-the-loop, you
must have an HDL Verifier™ license.

When you generate a programming file for a FIL target in Simulink, the tool creates a model to compare the FIL simulation with your
Simulink design. For Vision HDL Toolbox™ designs, the FIL block in that model replicates the pixel-streaming
interface to send one pixel at a time to the FPGA. You can modify the autogenerated
model to use the FIL Frame To Pixels and FIL Pixels To
Frame blocks to improve communication bandwidth with the FPGA board by
sending one frame at a time. For how to modify the autogenerated model, see FPGA-in-the-Loop.

Specify the same video format and vector size for the FIL Frames To
Pixels block and the FIL Pixels To Frame block.
