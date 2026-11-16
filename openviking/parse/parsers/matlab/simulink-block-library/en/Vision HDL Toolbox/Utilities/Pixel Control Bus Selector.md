---
type: simulink-block
title: 'Pixel Control Bus Selector'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'pixelcontrolbusselector'
documentation_source_path: 'ref/pixelcontrolbusselector.html'
language: en
---

# Pixel Control Bus Selector

## Ports

### Input

### **Port\_1** — Control signals accompanying pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`
### Output

### **Port\_1** — First pixel in a horizontal line of a frame scalar

First pixel in a horizontal line of a frame, returned as a
`Boolean` scalar. This port returns the
`hStart` signal from the input bus.

**Data Types:** `Boolean`

### **Port\_2** — Last pixel in a horizontal line of a frame scalar

Last pixel in a horizontal line of a frame, returned as a
`Boolean` scalar. This port returns the
`hEnd` signal from the input bus.

**Data Types:** `Boolean`

### **Port\_3** — First pixel in the first (top) line of a frame scalar

First pixel in the first (top) line of a frame, returned as a
`Boolean` scalar. This port returns the
`vStart` signal from the input bus.

**Data Types:** `Boolean`

### **Port\_4** — Last pixel in the last (bottom) line of a frame scalar

Last pixel in the last (bottom) line of a frame, returned as a
`Boolean` scalar. This port returns the
`vEnd` signal from the input bus.

**Data Types:** `Boolean`

### **Port\_5** — Valid pixel indicator scalar

Valid pixel indicator, returned as a `Boolean`
scalar. This port returns the `valid` signal from the
input bus.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

## Libraries

Vision HDL Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

To learn more about using buses for HDL code generation, see Buses (HDL Coder) and Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder).

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

## Description

Select signals from control signal bus used by Vision HDL Toolbox blocks

The Pixel Control Bus Selector block selects signals from the
`pixelcontrol` bus. See Pixel Control Bus.

The block is an implementation of the Simulink®
Bus Selector block. See Bus Selector (Simulink) for more
information.
