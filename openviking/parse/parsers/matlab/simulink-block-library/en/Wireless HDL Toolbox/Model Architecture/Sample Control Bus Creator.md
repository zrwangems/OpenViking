---
type: simulink-block
title: 'Sample Control Bus Creator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Model Architecture'
documentation_page: 'samplecontrolbuscreator'
documentation_source_path: 'ref/samplecontrolbuscreator.html'
language: en
---

# Sample Control Bus Creator

## Ports

### Input

### **start** — Start of frame scalar

Start of frame, specified as a `Boolean` scalar. This
signal is 1 (true) for one time step, corresponding to the first valid
sample of the frame.

**Data Types:** `Boolean`

### **end** — End of frame scalar

End of frame, specified as a `Boolean` scalar. This
signal is 1 (true) for one time step, corresponding to the last valid
sample of the frame.

**Data Types:** `Boolean`

### **valid** — Validity of samples scalar

Validity of samples, specified as a `Boolean` scalar.
This signal is 1 (true) on time steps that correspond to valid
samples.

**Data Types:** `Boolean`
### Output

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a `samplecontrol`
bus. The bus includes the `start`, `end`, and
`valid` control signals, which indicate the boundaries of the frame
and the validity of the samples.

- `start` — Indicates the start of the output
  frame
- `end` — Indicates the end of the output frame
- `valid` — Indicates that the data on the output
  **data** port is valid

For more details, see Sample Control Bus.

**Data Types:** `bus`

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

Create control signal bus for use with Wireless HDL Toolbox blocks

The Sample Control Bus Creator block creates a
`samplecontrol` bus for modeling streaming control signals in
communication systems for hardware. See Sample Control Bus.

The block is an implementation of the Simulink®
Bus Creator block. See Bus Creator for more
information.
