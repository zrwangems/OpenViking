---
type: simulink-block
title: 'Histogram'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'histogram'
documentation_source_path: 'ref/histogram.html'
language: en
---

# Histogram

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar | vector
  direction: input
  data_types: uint | fixdt(0,W,0) | Boolean | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: binAddr
  summary: Bin number for reading histogram values integer
  direction: input
  data_types: fixdt(0,W,0)
- name: binReset
  summary: Reset histogram bin values scalar
  direction: input
  data_types: Boolean
- name: readRdy
  summary: Indicates histogram bins available for read scalar
  direction: output
  data_types: Boolean
- name: hist
  summary: Bin value corresponding to requested address integer
  direction: output
  data_types: fixed point
- name: validOut
  summary: Indicates that histogram value is valid scalar
  direction: output
  data_types: Boolean
```

### Input

### **pixel** — Input pixel stream scalar | vector

This block supports single pixel streaming or multipixel streaming.
For single pixel streaming, specify a single input pixel as a scalar
intensity value. For multipixel streaming, specify a vector of two,
four, or eight pixel intensity values. For details of how to set up your
model for multipixel streaming, see Filter Multipixel Video Streams.

This block does not support multicomponent streaming. To process
multicomponent streams, replicate the block for each component. The
`pixelcontrol` bus for all components is identical,
so you can connect a single bus to multiple replicated blocks.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint` | `fixdt(0,W,0)` | `Boolean` | `double` | `single`

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

### **binAddr** — Bin number for reading histogram values integer

The block captures this value each cycle that the
**readRdy** output port is 1
(`true`). The data type is
`fixdt(0,W,0)`, W = 5,6,...,12. The word length
must be log2(**Number of
bins**).

**Data Types:** `fixdt(0,W,0)`

### **binReset** — Reset histogram bin values scalar

A **binReset** value of 1 (`true`)
triggers a RAM initialization sequence that resets the histogram bin
values. Reset takes `NumBins` cycles to clear all
locations. Input signals are ignored during this interval.

**Data Types:** `Boolean`
### Output

### **readRdy** — Indicates histogram bins available for read scalar

When **readRdy** is 1 (`true`), the
histogram bins are ready to read. The block returns
**readRdy** set to 1 (`true`) two
cycles after the final pixel of a frame.

**Data Types:** `Boolean`

### **hist** — Bin value corresponding to requested address integer

Histogram bin value corresponding to the requested address,
**binAddr**. The **Data type**
parameter specifies the data type for this value.

**Data Types:** `fixed point`

### **validOut** — Indicates that histogram value is valid scalar

When **validOut** is 1 (`true`), the
histogram bin value, **hist**, is valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Number of bins
  summary: Number of histogram bins 256 (default) | power of 2 between 32 and 4096
  group: ''
- name: Data type
  summary: Data type of histogram bin values Unsigned fixed point (default) | double | single
  group: ''
- name: Word length
  summary: Word length of histogram bins 16 (default) | integer
  group: ''
```

### **Number of bins** — Number of histogram bins `256` (default) | power of 2 between `32` and `4096`

Choose the number of bins depending on the input word length (WL). If the
number of bins is less than 2WL, the block
truncates the least-significant bits of each pixel. If the number of bins is
greater than 2WL, some bins are not used, and
after you synthesize your design it will use more hardware resources than
necessary.

### **Data type** — Data type of histogram bin values `Unsigned fixed point` (default) | `double` | `single`

Data type of histogram bin values.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

### **Word length** — Word length of histogram bins `16` (default) | integer

Word length of the histogram bins. If a bin overflows, the count saturates
and the block shows a warning.

#### Dependencies

This parameter applies when you set **Data type** to
`Unsigned fixed point`.
## Libraries

Vision HDL Toolbox / Statistics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2015a**

### R2022b: Two pixels-per-clock streaming

The block now supports multipixel streams that have 2 pixels per clock cycle.

### R2022a: Multipixel streaming

The Histogram block now supports multipixel streams. The HDL implementation
replicates the algorithm for each pixel in parallel.

The block supports input column vectors of *NumPixels* values,
where *NumPixels* is 4 or 8. The **ctrl** ports
remain scalar, and the control signals in the `pixelcontrol` bus
apply to all pixels in the matrix. The output interface is the same whether the
input is scalar or vector.

### R2019b: Increased histogram sizes

You can now configure the block to have 2048 or 4096 histogram bins.

## Description

Frequency distribution of pixel values in video stream

The Histogram block computes the frequency distribution of pixel values
in a video stream. You can configure the number and size of the bins. The block provides
a read interface for accessing each bin. The block keeps a running histogram until you
reset the bin values.
