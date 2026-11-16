---
type: simulink-block
title: 'CCSDS LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsldpcencoder'
documentation_source_path: 'ref/ccsdsldpcencoder.html'
language: en
---

# CCSDS LDPC Encoder

## Ports

### Input

### **data** — Input data bits scalar | column vector

Input data bits, specified as a `Boolean` scalar or an
eight-element `Boolean` column vector.

**Data Types:** `Boolean`

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

### **data** — Encoded output data bits scalar | vector

Encoded output data bits, returned as a `Boolean` scalar or an
eight-element `Boolean` column vector. The output data type is same
as the input data type.

**Data Types:** `Boolean`

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

### **nextFrame** — Block ready indicator scalar

Block ready indicator, returned as a `Boolean` scalar.

The block sets this signal to `1` when the block is ready to
accept the start of the next frame. If the block receives an input
**ctrl.start** signal while **nextFrame** is
`0`, the block discards the frame in progress and begins processing
the new data.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

## Libraries

Wireless HDL Toolbox / Error Detection and Correction

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

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2025a**

## Description

Encode data with (8160,7136) LDPC code specified in CCSDS telemetry standard

The CCSDS LDPC Encoder block encodes data with (8160,7136) low-density
parity-check (LDPC) code specified in the Consultative Committee for Space Data Systems
(CCSDS) Telemetry standard. The block accepts data bits and a stream of control signals as
inputs. The block outputs encoded bits, a stream of control signals, and a signal that
indicates when the block is ready to accept new inputs.

The block supports scalar input and vector inputs of size 8. The block provides an
architecture suitable for HDL code generation and hardware deployment. You can use this block
in a CCSDS transmitter for satellite communication. To know more about CCSDS Telemetry
standard, see [1]
