---
type: simulink-block
title: 'Sample Control Bus Selector'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'samplecontrolbusselector'
documentation_source_path: 'ref/samplecontrolbusselector.html'
language: en
---

# Sample Control Bus Selector

## Ports

### Input

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate the
boundaries of the frame and the validity of the samples.

- `start` — Indicates the start of the input frame
- `end` — Indicates the end of the input frame
- `valid` — Indicates that the data on the input
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`
### Output

### **start** — Start of frame scalar

Start of frame, returned as a `Boolean` scalar. This
signal is 1 (true) for one time step, corresponding to the first valid
sample of the frame.

**Data Types:** `Boolean`

### **end** — End of frame scalar

End of frame, returned as a `Boolean` scalar. This
signal is 1 (true) for one time step, corresponding to the last valid
sample of the frame.

**Data Types:** `Boolean`

### **valid** — Validity of samples scalar

Validity of samples, returned as a `Boolean` scalar.
This signal is 1 (true) on time steps that correspond to valid
samples.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

## Libraries

Wireless HDL Toolbox / Utilities

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

**Introduced in R2017b**

## Description

Select signals from the control signal bus used with Wireless HDL Toolbox blocks

The Sample Control Bus Selector block selects signals from the
`samplecontrol` bus. This bus is used for modeling streaming
control signals in communication systems for hardware. See Sample Control Bus.

The block is an implementation of the Simulink®
Bus Selector block. See Bus Selector for more
information.
