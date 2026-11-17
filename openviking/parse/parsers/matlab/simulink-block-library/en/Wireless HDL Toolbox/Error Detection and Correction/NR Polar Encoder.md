---
type: simulink-block
title: 'NR Polar Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrpolarencoder'
documentation_source_path: 'ref/nrpolarencoder.html'
language: en
---

# NR Polar Encoder

## Ports
```yaml
ports:
- name: data
  summary: Input data bit scalar
  direction: input
  data_types: fixdt(0,1,0) | Boolean | double | single
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: K
  summary: Length of information block in bits positive integer
  direction: input
  data_types: fixdt(0,10,0)
- name: E
  summary: Rate-matched output length in bits positive integer
  direction: input
  data_types: fixdt(0,14,0)
- name: data
  summary: Encoded data bit scalar
  direction: output
  data_types: fixdt(0,1,0) | Boolean | double | single
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: nextFrame
  summary: Ready for new inputs scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data bit scalar

Input data bit, specified as a scalar.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `fixdt(0,1,0)` | `Boolean` | `double` | `single`

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

### **K** — Length of information block in bits positive integer

Length of information block in bits, specified as a positive integer. For downlink
messages, **K** must be in the range 36 to 164. For uplink messages,
**K** must be in the range 18 to 25 or 31 to 1023.

#### Dependencies

To enable this port, set the **Configuration source** parameter
to `Input port`.

**Data Types:** `fixdt(0,10,0)`

### **E** — Rate-matched output length in bits positive integer

Rate-matched output length in bits, specified as a positive integer. Specify a
value for **E** that is greater than **K** and less
than or equal to 8192.

#### Dependencies

To enable this port, set the **Configuration source** parameter
to `Input port`.

**Data Types:** `fixdt(0,14,0)`
### Output

### **data** — Encoded data bit scalar

Encoded data bit, returned as a scalar. The block returns a message of
*N* sequential bits. *N* is a power of two
determined from the values of **K** and **E**. The
maximum output message size is 512 bits when the **Link direction**
is `Downlink` and 1024 bits when the **Link
direction** is `Uplink`.

**Data Types:** `fixdt(0,1,0)` | `Boolean` | `double` | `single`

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

### **nextFrame** — Ready for new inputs scalar

The block sets this signal to `1` when the block is ready to accept the start
of the next frame. If the block receives an input **start** signal
while **nextFrame** is `0`, the block discards the
frame in progress and begins processing the new data.

For more information, see Using the nextFrame Output Signal.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Link direction
  summary: Direction of 5G NR link Downlink (default) | Uplink
  group: ''
- name: Configuration source
  summary: Source for K and E Property (default) | Input port
  group: ''
- name: Message length (K)
  summary: Length of information block in bits 56 (default) | positive integer
  group: ''
- name: Rate-matched length (E)
  summary: Rate-matched output length in bits 864 (default) | positive integer
  group: ''
```

### **Link direction** — Direction of 5G NR link `Downlink` (default) | `Uplink`

When you select `Downlink`, the block performs
interleaving, as specified in the 5G NR standard. When you select
`Uplink`, the block omits the interleaving logic.

### **Configuration source** — Source for K and E `Property` (default) | `Input port`

Select `Input port` to enable the **K**
and **E** ports. Select `Property` to use the
**Message length (K)** and **Rate-matched length
(E)** parameters.

### **Message length (K)** — Length of information block in bits `56` (default) | positive integer

For downlink messages, **K** must be in the range 36 to 164. For
uplink messages, **K** must be in the range 18 to 25 or 31 to
1023.

#### Dependencies

To enable this parameter, set the **Configuration source**
parameter to `Property`.

### **Rate-matched length (E)** — Rate-matched output length in bits `864` (default) | positive integer

Specify a value for **E** that is greater than
**K** and less than or equal to 8192.

#### Dependencies

To enable this parameter, set the **Configuration source**
parameter to `Property`.
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

Perform polar encoding according to 5G NR standard

The NR Polar Encoder block implements a streaming polar encoder with
hardware-friendly control signals. The 5G NR standard requires polar encoding for channel
coding of the DCI, UCI, and BCH transmit channels.

The encoder implementation matches the `nrPolarEncode` (5G Toolbox) function.

You must specify the link direction because the coding scheme defined by the 5G NR standard
is different for downlink and uplink messages. Downlink messages are encoded with interleaving
and uplink messages do not use interleaving.

Because the latency of this operation can vary, the block provides an output signal,
**nextFrame**, that indicates when the block is ready to accept new inputs.
For more details, see the Latency section on this page.
