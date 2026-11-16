---
type: simulink-block
title: 'DVB-S2 BCH Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'dvbs2bchdecoder'
documentation_source_path: 'ref/dvbs2bchdecoder.html'
language: en
---

# DVB-S2 BCH Decoder

## Ports

### Input

### **data** — Codeword data bits scalar | vector

Codeword data bits, specified as a `Boolean` scalar or an
8-element column vector.

The length of the input data must be based on the FEC frame type and code rate
according to the DVB-S2 standard. For more information, see section 5.3 in [1].

For example, if the **FEC frame type** parameter is set to
`Normal` and the **Code rate**  parameter
is set to `3/5`, the length of the input data must be
38,880.

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

### **frameType** — Frame type scalar

*Since R2024b*

Frame type, specified as a `Boolean` scalar. If you specify
`0`, the block considers the input data as a normal frame and if
you specify `1` the block considers the input data as a short
frame.

#### Dependencies

To enable this port, set the **Frame type source** parameter to
`Input port`.

**Data Types:** `Boolean`

### **codeRateIdx** — Code rate index integer

Code rate index, specified as an integer. Code rate index values range from 0 to
10. Each code rate index value represents a specific code rate, as shown in this
table.

| codeRateIdx Value | Code Rate |
| --- | --- |
| `0` | 1/4 |
| `1` | 1/3 |
| `2` | 2/5 |
| `3` | 1/2 |
| `4` | 3/5 |
| `5` | 2/3 |
| `6` | 3/4 |
| `7` | 4/5 |
| `8` | 5/6 |
| `9` | 8/9 |
| `10` | 9/10 |

#### Dependencies

To enable this port, set the **Code rate source** parameter to
`Input port`.

**Data Types:** `fixdt(0,4,0)`
### Output

### **data** — Decoded message bits scalar | vector

Decoded message bits, returned as a `Boolean` scalar or as an
8-element column vector. The output data type and dimension are same as the
input.

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

### **numCorrErr** — Number of corrected errors scalar

Number of corrected errors, returned as a scalar.

- – 1 — Indicates that the block contains errors in its output that
  cannot be corrected
- 0 — Indicates that the block does not contain errors in its
  output
- Range from 1 to 12 — Indicates the number of errors corrected in the
  block output

#### Dependencies

To enable this port, select the **Output number of corrected symbol
errors** parameter.

**Data Types:** `fixdt(1,5,0)`

### **nextFrame** — Block ready indicator scalar

Block ready indicator, returned as a `Boolean` scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

## Parameters

### **FEC frame type source** — FEC frame type source `Property` (default) | `Input port`

*Since R2024b*

Select the FEC frame type source as `Property` or
`Input port`.

- `Property` — Select this option to enable the
  **FEC frame type** parameter.
- `Input port` — Select this option to enable the
  **frameType** port.

For more information about normal and short FEC frame types, see [1].

### **FEC frame type** — FEC frame type `Normal` (default) | `Short`

Select the FEC frame type as `Normal` or
`Short`.

For more information about normal and short FEC frame types, see [1].

### **Code rate source** — Source for code rate `Property` (default) | `Input port`

Select the code rate source as `Property` or
`Input port`.

- `Property` — Select this option to enable the
  **Code rate** parameter.
- `Input port` — Select this option to enable
  the **codeRateIdx** input port.

### **Code rate** — Code rate `1/4` (default) | `1/3` | `2/5` | `1/2` | `3/5` | `2/3` | `3/4` | `4/5` | `5/6` | `8/9` | `9/10`

Select the code rate.

#### Dependencies

To enable this parameter, set the **Code rate source** parameter
to `Property`.

### **Output number of corrected errors** — Number of corrected errors `off` (default) | `on`

Select this parameter to enable the **numCorrErr** output port.
This port outputs the number of corrected errors.

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

To obtain effective synthesis results on Intel®
Altera® devices, perform the following settings:

- For VHDL — In the Configuration Parameters dialog box, go to
  **HDL Code Generation > Global Settings > Coding style** tab and
  set the **RAM Architecture** parameter to `Generic RAM
  without clock enable`.
- For Verilog — In the Configuration Parameters dialog box, go to
  **HDL Code Generation > Global Settings > Coding style** tab and
  clear the **Initialize all RAM blocks** option.

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).

## Version History

**Introduced in R2022a**

### R2024b: Support for frame-based input data and option to specify frame type through input port

The DVB-S2 BCH Decoder block now supports frame-based inputs. The block
now offers a new parameter **FEC frame source**, which you can use to
specify the frame type through an input port or through property. The block is optimized to
minimize the use of BRAMs for both scalar and frame-based input data.

### R2023b: Improvement in resource utilization

The DVB-S2 BCH Decoder block now improves its resource utilization
values. You can see a significant decrease in the usage of Block RAMs.

| Release | Slice LUTs | Slice Registers | DSPs | Block RAM |
| --- | --- | --- | --- | --- |
| R2022a | 5586 | 5294 | 4 | 638 |
| R2023b | 9057 | 5715 | 4 | 103 |

## Description

Decode and recover message from BCH codeword according to DVB-S2 standard

The DVB-S2 BCH Decoder block decodes and recovers messages from a
Bose-Chaudhuri-Hocquenghem (BCH) codeword according to the Digital Video Broadcast Satellite
Second Generation (DVB-S2) standard [1]. The block accepts
low-density parity-check (LDPC) decoded codeword data bits and a stream of control signals. It
outputs decoded message data bits, a stream of control signals, a signal that indicates when
the block is ready to accept new input, and an optional signal that provided the number of
corrected errors in the output. The block supports either a scalar or an 8-element column
vector as input.

The block supports two forward error correction (FEC) frame types, normal and short. The
block provides an architecture suitable for HDL code generation and hardware deployment. You
can use this block in a DVB-S2 receiver for satellite communication.
