---
type: simulink-block
title: 'NR LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrldpcencoder'
documentation_source_path: 'ref/nrldpcencoder.html'
language: en
---

# NR LDPC Encoder

## Ports
```yaml
ports:
- name: data
  summary: Input data bits scalar | vector
  direction: input
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: bgn
  summary: Base graph number scalar
  direction: input
  data_types: Boolean
- name: liftingSize
  summary: Input lifting size scalar
  direction: input
  data_types: uint16
- name: data
  summary: Encoded output data bits scalar | vector
  direction: output
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: liftingSize
  summary: Output lifting size scalar
  direction: output
  data_types: uint16
- name: nextFrame
  summary: Ready for new inputs scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data bits scalar | vector

Input data bits, specified as a scalar or a column vector of size 64.

For more information on how to specify vector input data, see Specifying Vector Input.

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

### **bgn** — Base graph number scalar

Base graph number, specified as a scalar. When this value is `0`,
the block applies *bgn 1*. When this value is `1`,
the block applies *bgn 2*. For more information about *bgn
1* and *bgn 2*, see section 5.3.2, of TS 38.212 [1].

**Data Types:** `Boolean`

### **liftingSize** — Input lifting size scalar

Input lifting size, specified as a scalar.

For an invalid **liftingSize** value, the block discards the
current frame and waits for the new frame.

For more information about the supported lifting size values, see section 5.3.2,
of TS 38.212 [1].

**Data Types:** `uint16`
### Output

### **data** — Encoded output data bits scalar | vector

Encoded output data bits, returned as a scalar or a column vector of size
64.

The block outputs data bits in a similar format as the input data
bits.

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

### **liftingSize** — Output lifting size scalar

Output lifting size, returned as a scalar.

**Data Types:** `uint16`

### **nextFrame** — Ready for new inputs scalar

The block sets this signal to `1` when the block is ready to accept the start
of the next frame. If the block receives an input **start** signal
while **nextFrame** is `0`, the block discards the
frame in progress and begins processing the new data.

For more information, see Using the nextFrame Output Signal.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters: []
```

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

**Introduced in R2020a**

## Description

Perform LDPC encoding according to 5G NR standard

The NR LDPC Encoder block implements a low-density parity-check (LDPC)
encoder with hardware-friendly control signals. The block accepts data bits, a stream of
control signals, a base graph number, and lifting sizes. The block outputs encoded bits, a
stream of control signals, lifting sizes, and a signal that indicates when the block is ready
to accept new inputs.

The block functionality matches that of the function `nrLDPCEncode` (5G Toolbox). You can use this block
for channel coding of downlink and uplink shared channels and paging channel according to 5G
new radio (NR) standard TS 38.212 [1].

The block supports scalar and vector inputs. The block provides an architecture suitable
for HDL code generation and hardware deployment. For more information, see Algorithms.
