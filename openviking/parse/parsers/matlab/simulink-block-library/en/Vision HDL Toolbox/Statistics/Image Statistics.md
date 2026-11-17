---
type: simulink-block
title: 'Image Statistics'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'imagestatistics'
documentation_source_path: 'ref/imagestatistics.html'
language: en
---

# Image Statistics

## Ports
```yaml
ports:
- name: pixel
  summary: Input pixel stream scalar | vector
  direction: input
  data_types: uint8 | uint16 | fixdt(0,W,0) | double | single
- name: ctrl
  summary: Control signals associated with pixel stream pixelcontrol bus
  direction: input
  data_types: bus
- name: mean
  summary: Mean of most recent input frame completed scalar
  direction: output
  data_types: uint8 | uint16 | fixdt(0,W,0) | double | single
- name: var
  summary: Variance of most recent input frame completed scalar
  direction: output
  data_types: uint8 | uint16 | fixdt(0,W,0) | double | single
- name: stdDev
  summary: Standard deviation of most recent input frame completed scalar
  direction: output
  data_types: uint8 | uint16 | fixdt(0,W,0) | double | single
- name: validOut
  summary: Computations completed boolean
  direction: output
  data_types: Boolean
```

### Input

### **pixel** — Input pixel stream scalar | vector

For single pixel streaming, specify **pixel** as an unsigned
scalar value that represents grayscale intensity. For multipixel streaming, specify
**pixel** as a column vector of **Number of
pixels** pixel intensity values. **Number of pixels** can
be two, four, or eight.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

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

The block uses full-precision arithmetic for internal calculation. At the output ports,
intermediate data is cast back to the input type by using the following fixed-point
settings: **Rounding method** = `Nearest`, and
**Overflow action** = `Saturate`. The table shows the
output word length for each calculation, relative to the input word length
(*IWL*).

| Mean | Variance | Std. Deviation |
| --- | --- | --- |
| *IWL* | 2×*IWL* | 2×*IWL* |

### **mean** — Mean of most recent input frame completed scalar

Mean of the most recent input frame completed, returned as a scalar. The data type
of **mean** is same as the data type of
**pixel**.

**Data Types:** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **var** — Variance of most recent input frame completed scalar

Variance of the most recent input frame completed, returned as a scalar. The data
type of **var** is same as the data type of
**pixel**.

**Data Types:** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **stdDev** — Standard deviation of most recent input frame completed scalar

Standard deviation of the most recent input frame completed, returned as a scalar.
The data type of **stdDev** is same as the data type of
**pixel**.

**Data Types:** `uint8` | `uint16` | `fixdt(0,W,0)` | `double` | `single`

### **validOut** — Computations completed boolean

The block sets this output to `true` when the statistic outputs
for a frame are ready.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Enable mean output
  summary: Calculate the mean of each input frame on (default) | off
  group: ''
- name: Enable variance output
  summary: Calculate the variance of each input frame on (default) | off
  group: ''
- name: Enable std. deviation
  summary: Calculate the standard deviation of each input frame on (default) | off
  group: ''
```

### **Enable mean output** — Calculate the mean of each input frame on (default) | off

Select this parameter to enable the **mean** port and calculate the
mean of each input frame.

### **Enable variance output** — Calculate the variance of each input frame on (default) | off

Select this parameter to enable the **var** port and calculate the
variance of each input frame.

### **Enable std. deviation** — Calculate the standard deviation of each input frame on (default) | off

Select this parameter to enable the **stdDev** port and calculate
the standard deviation of each input frame.
## Libraries

Vision HDL Toolbox / Statistics

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

**Introduced in R2015a**

### R2023b: Multipixel streaming

The Image Statistics block now supports multipixel streams. For multipixel streaming, the
block supports input column vectors of 2, 4, or 8 pixels. The **ctrl** port
remains scalar, and the control signals in the `pixelcontrol` bus apply to
all pixels in the vector. The output ports that represent the statistics of the image remain
scalar.

## Description

Calculate mean, variance, and standard deviation

The Image Statistics block calculates the mean, variance, and standard
deviation of streaming video data. Each calculation is performed over all pixels in the input
region of interest (ROI). The block implements the calculations by using hardware-efficient
algorithms.
