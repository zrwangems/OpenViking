---
type: simulink-block
title: 'Pixel Control Bus Creator'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'pixelcontrolbuscreator'
documentation_source_path: 'ref/pixelcontrolbuscreator.html'
language: en
---

# Pixel Control Bus Creator

## Ports

### Input

### **hStart** — First pixel in a horizontal line of a frame scalar

First pixel in a horizontal line of a frame, specified as a
`Boolean` scalar.

**Data Types:** `Boolean`

### **hEnd** — Last pixel in a horizontal line of a frame scalar

Last pixel in a horizontal line of a frame, specified as a
`Boolean` scalar.

**Data Types:** `Boolean`

### **vStart** — First pixel in the first (top) line of a frame scalar

First pixel in the first (top) line of a frame, specified as a
`Boolean` scalar.

**Data Types:** `Boolean`

### **vEnd** — Last pixel in the last (bottom) line of a frame scalar

Last pixel in the last (bottom) line of a frame, specified as a
`Boolean` scalar.

**Data Types:** `Boolean`

### **valid** — Valid pixel indicator scalar

Valid pixel indicator, specified as a `Boolean`
scalar.

**Data Types:** `Boolean`
### Output

### **ctrl** — Control signals accompanying pixel stream `pixelcontrol` bus

The `pixelcontrol` bus contains five signals.
The signals describe the validity of the pixel and its location in the frame. For more
information, see Pixel Control Bus.

**Data Types:** `bus`

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

Create control signal bus for use with Vision HDL Toolbox blocks

The Pixel Control Bus Creator block creates a
`pixelcontrol` bus. See Pixel Control Bus.

The block is an implementation of the Simulink®
Bus Creator block. See Bus Creator (Simulink) for more
information.

**Troubleshooting**

When you generate HDL code from a Simulink model that uses the `pixelcontrol` bus, you might
encounter this error.

```
Cannot resolve variable 'pixelcontrol'
```

To avoid this
issue, use the `pixelcontrolbus` function to create an instance
of the bus type in the base workspace. Then try generating HDL code again.

The Vision HDL Toolbox™ model template includes this line in the `InitFcn`
callback.

```
evalin('base','pixelcontrolbus')
```
