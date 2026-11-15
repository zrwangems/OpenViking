---
type: simulink-block
title: 'ROI Selector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'roiselector'
documentation_source_path: 'ref/roiselector.html'
language: en
---

# ROI Selector

## Ports

### Input

### **pixel** — Input pixel stream scalar | vector | matrix

For single pixel streams, specify **pixel** as a scalar or a
vector of 1-by-**Number of components** values. For multipixel
streams, specify **pixel** as a matrix of **Number of
pixels**-by-**Number of components** pixel intensity
values. **Number of pixels** can be two, four, or
eight.

Since R2025a, the software supports `single`
data type for simulation and HDL code generation. To enable HDL code generation for
`single` data types in your model, open the **HDL
Coder** app, go to the **Floating Point** pane, and
select the **Use Floating Point** checkbox.
`double` data type is supported only for simulation, not for HDL code
generation.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

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

### **region1,...,regionR** — Region of interest four-element row vector

Region of interest, specified as a row vector of four positive integers that
define the coordinates of the top-left corner and dimensions of each desired output
frame. The vector must have the form `[hPos
vPos
hSize
vSize]`. The block has *R* region
ports, where *R* is the **Number of regions**
parameter value.

For multipixel streaming the regions must meet these conditions, where
*M* is **Number of pixels**.

- `mod(hPos, M) = 1` —
  For example, if your pixel stream has four pixels per cycle,
  `129` is a valid value of *hPos*
  (`mod(129,4) = 1`), while `128` is invalid
  (`mod(128,4) = 0`).
- `mod(hSize, M) = 0` —
  For example, if your pixel stream has four pixels per cycle,
  `120` is a valid *hSize*
  (`mod(120,4) = 0`), while `118` is invalid
  (`mod(118,4) = 2`).

#### Dependencies

To enable this port, clear the **Reuse output ports for vertically
aligned regions** parameter and set the **Regions
source** parameter to `Input port`.

**Data Types:** `int` | `uint`
### Output

### **pixel1,...,pixelR** — Output pixel stream scalar | vector | matrix

Output pixel, returned as a single pixel or multipixel stream. The output
dimensions and data type match those of the input **pixel** port. By
default, the block has *R* output **pixel** ports,
where *R* is the **Number of regions** parameter, or
the number of rows in the **Regions** parameter matrix.

When you select **Reuse output ports for vertically aligned
regions**, the block has one output **pixel** port for
each column of vertically-aligned regions.

**Data Types:** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl1,...,ctrlR** — Control signals `pixelcontrol` bus

Control signals, returned as a `pixelcontrol` bus that contains
five signals. By default, the block has *R* output
**ctrl** ports, where *R* is the **Number
of regions** parameter, or the number of rows in the
**Regions** parameter matrix.

When you select **Reuse output ports for vertically aligned
regions**, the block has one output **ctrl** port for each
column of aligned regions.

**Data Types:** `bus`

## Parameters

### **Reuse output ports for vertically aligned regions** — Option to return one pixel stream for each column of regions `off` (default) | `on`

When you select this parameter, you must specify regions that have no vertical
overlap and that are aligned in columns. The block has one output pixel stream for each
column of regions. This arrangement enables parallel processing of each column, and the
reuse of downstream processing logic for each region in a column. Use the `visionhdlframetoregions` function to divide a frame into tiled regions for
vertical reuse.

#### Dependencies

To enable this parameter, set the **Regions source** parameter to
`Property`.

### **Regions source** — Location of output region definitions `Property` (default) | `Input port`

Specify the location of the output region definitions. You can set **Regions
source** to one of these values:

- `Property` — Specify the regions by using the
  **Regions** parameter.
- `Input port` — Specify the regions by using input
  ports. Each input port corresponds to one region. The block samples the
  **region** input ports when `vStart` is
  `true` in the input control bus.

#### Dependencies

To enable this parameter, clear the **Reuse output ports for vertically
aligned regions** parameter.

### **Regions** — Rectangular ROIs to select from input frame *R*-by-4 matrix

Specify rectangular ROIs to select from the input frame as an
*R*-by-4 matrix.

*R* is the number of regions. The four elements that define each
region are the top-left starting coordinates and the dimensions of the region and must
be of the form `[hPos
vPos
hSize
vSize]`. The coordinates count from the upper-left corner
of the active frame, defined as [1,1]. *hSize* must be greater than 1.

For multipixel streaming the regions must meet these conditions, where
*M* is **Number of pixels**.

- `mod(hPos, M) = 1` —
  For example, if your pixel stream has four pixels per cycle,
  `129` is a valid value of *hPos*
  (`mod(129,4) = 1`), while `128` is invalid
  (`mod(128,4) = 0`).
- **`mod(hSize, M) =
  0`** — For example, if your pixel stream has four pixels per cycle,
  `120` is a valid *hSize* (`mod(120,4)
  = 0`), while `118` is invalid (`mod(118,4) =
  2`).

When you clear the **Reuse output ports for vertically aligned
regions** parameter, the regions can overlap, and *R* must
not be greater than 16.

When you select **Reuse output ports for vertically aligned
regions**, the regions in this matrix must have no vertical overlap and be
aligned in columns. This diagram shows two examples of invalid regions outlined with a
blue dashed line. The region on the left overlaps another region vertically. The two
regions at the bottom do not align with the other regions in their columns. The regions
do not have to cover the entire frame. Pixels outside of the tiled regions are marked as
inactive pixels. The number of columns must not be greater than 16.

#### Dependencies

To enable this parameter, set the **Regions source** parameter to
`Property`.

### **Number of regions** — Number of region input ports integer in the range [1, 16]

Specify the number of region input ports as an integer in the range [1, 16].

#### Dependencies

To enable this parameter, set the **Regions source** parameter to
`Input port`.

## Libraries

Vision HDL Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2016a**

### R2025a: `single` data type supported for HDL code generation

The block now supports HDL code generation with `single` data type
pixel input.

### R2023a: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2021a: Multipixel-multicomponent streaming

The block now supports streams that are both multipixel and multicomponent. The HDL
implementation replicates the algorithm for each pixel and component in parallel.

The block supports input and output matrices of
*NumPixels*-by-*NumComponents* pixels. The
**ctrl** ports remain scalar, and the control signals in the
`pixelcontrol` bus apply to all pixels in the matrix.

### R2021a: Resource sharing

The block now provides an option to share hardware resources when you select vertically
aligned regions. Regions in the same column share the same `pixelcontrol`
bus output.

Select the **Reuse output ports for vertically aligned regions**
checkbox, and provide a set of regions that are aligned in columns and do not overlap
vertically within each column. You can specify up to 1024 regions per column. To divide a
frame into tiled regions that are compatible with vertical reuse, use the `visionhdlframetoregions` function.

## Description

Select a region of interest (ROI) from pixel stream

The ROI Selector block selects a portion of the active frame from a video
stream. The size of the inactive frame remains the same. The output control signals indicate a
new active region of the frame. You can use this block with a single pixel, multipixel, or
multipixel-multicomponent pixel stream. This diagram shows the inactive pixel regions in blue
and the requested output region outlined in orange.

Specified region of the input frame returned as a pixel stream with pixels outside of the region marked as inactive.

You can specify a fixed size and location for the ROI, or you can select the region
location dynamically by using an input port. You can select more than one region. Define each
region by specifying its upper-left corner coordinates and dimensions. By default, the block
returns one set of pixels and control signals for each region you specify. The block sets the
inactive pixels in the output frame to zero.

Regions are independent from each other, so they can overlap. If you specify a region that
includes the edge of the active frame, the block returns only the active portion of the
region. This diagram shows the output frames for three requested regions. The second output
region does not include the inactive area above the image.

Three regions (one partially falling outside of the active frame, and one overlapping another), returned as three pixel streams.

The block also provides a mode for vertical reuse. In this mode, you must specify regions
that have no vertical overlap and are aligned in columns. Each column of regions shares one
output pixel stream. The control signals define each region in the stream. This arrangement
enables parallel processing of each column, and the reuse of downstream processing logic for
each region in a column. To use this mode, select the **Reuse output ports for
vertically aligned regions** parameter. Use the `visionhdlframetoregions` function to divide a frame into tiled regions for
vertical reuse.

Eight tiled regions returned as two output pixel streams that each contain four vertically-aligned regions.
