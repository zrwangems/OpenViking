---
type: simulink-block
title: 'FIL Pixels To Frame'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation and Deployment'
documentation_page: 'filpixelstoframe'
documentation_source_path: 'ref/filpixelstoframe.html'
language: en
---

# FIL Pixels To Frame

## Ports

### Input

### **data1,...,dataN** — Image pixels vector | matrix

Image pixels, specified as a matrix of
*M*-by-**Number of pixels**
values, where *M* is the width of the **Output
vector format**. There are *N* data ports,
where *N* is the **Number of
components**.

When you use multipixel streaming, the FIL DUT has **Number of
pixels** data ports. You must recombine the output vectors
from each port into a *M*-by-**Number of
pixels** matrix. For details, see FPGA-in-the-Loop Simulation with Multipixel Streaming.

Similarly, when you use multipixel-multicomponent streaming, the FIL
DUT has **Number of pixels**×**Number of
components** data ports. Recombine the output vectors into
a *M*-by-**Number of pixels** matrix
for each component.

**Data Types:** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`

### **hStartIn** — First pixel in horizontal line of frame vector

First pixel in a horizontal line of a frame, specified as a
`Boolean` vector of *M* values.

For multipixel streaming, **hStartIn** applies to the
pixel with the lowest index in the corresponding column.

**Data Types:** `Boolean`

### **hEndIn** — Last pixel in horizontal line of frame vector

Last pixel in a horizontal line of a frame, specified as a
`Boolean` vector of *M*
values.

For multipixel streaming, **hEndIn** applies to the
pixel with the highest index in the corresponding column.

**Data Types:** `Boolean`

### **vStartIn** — First pixel in first (top) line of frame vector

First pixel in the first (top) line of a frame, specified as a
`Boolean` vector of *M* values.

For multipixel streaming, **vStartIn** applies to the
pixel with the lowest index in the corresponding column.

**Data Types:** `Boolean`

### **vEndIn** — Last pixel in last (bottom) line of frame vector

Last pixel in the last (bottom) line of a frame, specified as a
`Boolean` vector of *M*
values.

For multipixel streaming, **hEndIn** applies to the
pixel with the highest index in the corresponding column.

**Data Types:** `Boolean`

### **validIn** — Valid pixel indicator vector

Valid pixel indicator, specified as a `Boolean`
vector of *M* values.

For multipixel streaming, the pixels in the corresponding column are
either all valid or all invalid.

**Data Types:** `Boolean`
### Output

### **frame** — Full image frame matrix

Full image specified as a (**Active pixels per
line**)-by-(**Active video
lines**)-by-*N* matrix. Height and width
are the dimensions of the active image specified in **Video
format**. *N* is the **Number of
components** used to express a single pixel. The data type
is the same as **data1,...,dataN**.

### **validOut** — Indicates when output frame is ready scalar

A `true` (1) value indicates when output frame is
successfully recompiled from the input stream.

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

### **Number of pixels** — Number of pixels in each column of input matrix `1` (default) | `2` | `4` | `8`

Number of pixels in each column of the input matrix, specified as
`1`, `2`,
`4`, or `8`.

Each data port expects a *M*-by-**Number of
pixels** matrix. You must recombine the FIL DUT output vectors
to create this matrix. For details, see FPGA-in-the-Loop Simulation with Multipixel Streaming.

### **Input vector format** — Size of the vector used to communicate with the FPGA subsystem `Frame` (default) | `Line` | `Pixel`

Size of the vector used to communicate with the FPGA subsystem. The block
accepts input pixels and control signals in vectors of the same length. The
block calculates the length of the vectors based on the **Video
format** parameter.

- `Pixel` — Accept scalar values for
  pixel and control signals.
- `Line` — Accept input vectors
  containing **Total pixels per line**
  values.
- `Frame` — Accept input vectors
  containing **Total pixels per line** ×
  **Total video lines** values.

A larger value results in faster communication between the
FPGA board and Simulink. Choose the largest option that the I/O and memory resources
on your board can support.

For multipixel streaming, specify one of these options for input size.

- `Pixel` — Accept a
  1-by-(**Number of pixels**) vector of pixel
  values, and scalar control signals that apply to all the pixels
  in each vector.
- `Line` — Accept a (**Total
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
**Input vector format** to
`Frame`.

### **Video format** — Dimensions of active regions of a video frame `1080p` (default) | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

Dimensions of active regions of a video frame. To select a predefined
format, use the **Video format** list. For a custom format,
select `Custom`, and then specify the active frame
dimensions as integers.

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
Simulink Accelerator and Rapid Accelerator modes.

## Version History

**Introduced in R2015a**

### R2022a: Two pixels-per-clock streaming

The block can now accept multipixel streams that have 2 pixels per clock cycle.

### R2020b: Multipixel-multicomponent streaming

The block can now accept multipixel-multicomponent streams. When you use
multipixel-multicomponent streaming, the FIL DUT has **Number of
pixels**×**Number of components** data ports.
Recombine the output vectors into a *M*-by-**Number of
pixels** matrix for each component.

### R2019b: Multipixel streaming

The block can now accept multipixel streams. You can set the **Number of
pixels** parameter to `4` or
`8`. When you use multipixel streaming, the FIL DUT has
**Number of pixels** data ports. You must recombine the output
vectors from each port into a *M*-by-**Number of
pixels** matrix. For details, see FPGA-in-the-Loop Simulation with Multipixel Streaming.

## Description

Convert pixel stream from FPGA-in-the-loop to frame-based video

The FIL Pixels To Frame block performs the same pixel-to-frame
conversion as the Pixels To Frame block. In addition, you
can configure the width of the input to be a single pixel, a line, or an entire frame
per step. The block expects control signal input vectors of the same width as the pixel
data. This optimization can speed up the communication link between the FPGA board and
your Simulink® simulation when using FPGA-in-the-loop. To run FPGA-in-the-loop, you must
have an HDL Verifier™ license.

When you generate a programming file for a FIL target in Simulink, the tool creates a model to compare the FIL simulation with your
Simulink design. For Vision HDL Toolbox™ designs, the FIL block in that model replicates the pixel-streaming
interface to send one pixel at a time to the FPGA. You can modify the autogenerated
model to use the FIL Frame To Pixels and FIL Pixels To
Frame blocks to improve communication bandwidth with the FPGA board by
sending one frame at a time. For how to modify the autogenerated model, see FPGA-in-the-Loop.

Specify the same video format for the FIL Frames To Pixels block and
the FIL Pixels To Frame block.
