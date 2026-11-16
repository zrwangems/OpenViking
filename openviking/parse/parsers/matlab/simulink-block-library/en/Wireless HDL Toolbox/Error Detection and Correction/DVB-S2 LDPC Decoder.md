---
type: simulink-block
title: 'DVB-S2 LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'dvbs2ldpcdecoder'
documentation_source_path: 'ref/dvbs2ldpcdecoder.html'
language: en
---

# DVB-S2 LDPC Decoder

## Ports

### Input

### **data** — LLR values scalar | column vector *(since R2025a)*

LLR values, specified as a scalar or an eight-element column vector.

For HDL code generation, specify this value in signed fixed-point format. The
input word length must be in the range from 4 to 16.

**Data Types:** `int8` | `int16` | `signed fixed point`

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

### **frameType** — Type of FEC frame scalar

Type of FEC frame, specified as a Boolean scalar.

- `0` — Indicates a normal frame
- `1` — Indicates a short frame

#### Dependencies

To enable this port, set the **FEC frame source** parameter to
`Input port`.

**Data Types:** `Boolean`

### **codeRateIdx** — Code rate index integer

Code rate index, specified as an integer. Code rate index values range from 0 to
10. Each code rate index value represents a specific code rate, as shown in this
table.

| `codeRateIdx` Value | Code Rate |
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
| `10` | 9/10 (not supported for short frame) |

You must specify this value in the `fixdt(0,4,0)` format.

#### Dependencies

To enable this port, do one of the following:

- Set the **FEC frame source** parameter to
  `Input port`.
- Set the **FEC frame source** parameter to
  `Property` and the **Code rate
  source** parameter to `Input port`.

**Data Types:** `fixdt(0,4,0)`

### **iter** — Number of iterations scalar

Number of iterations, specified as an unsigned integer in the range from 1 to
63.

If you specify an **iter** value greater than 63 or less than 1,
the block overrides your specification and sets the **iter** value to
`8` before decoding.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Max` or `Early` and
the **Source for number of iterations** parameter to
`Input port`.

**Data Types:** `uint8`

### **scalingFactorIdx** — Scaling factor index scalar

*Since R2024b*

Scaling factor index, specified as a scalar. Each scaling factor index value
represents a specific scaling factor, as shown in this table.

| `scalingFactorIdx` Value | Scaling Factor |
| --- | --- |
| `0` | 0.5 |
| `1` | 0.5625 |
| `2` | 0.6250 |
| `3` | 0.6875 |
| `4` | 0.7500 |
| `5` | 0.8125 |
| `6` | 0.8750 |
| `7` | 0.9375 |
| `8` | 1 |

You must specify this value in the `fixdt(0,4,0)` format. If you
specify a value other than one listed in this table, the block displays a warning
message and applies the scaling factor index as `4` and continues its
operation.

#### Dependencies

To enable this port, set the **Algorithm** parameter to
`Normalized min-sum` and then set the **Source
for scaling factor** parameter to `Input
port`.

**Data Types:** `uint8`
### Output

### **data** — Decoded bits scalar | column vector *(since R2025a)*

Decoded bits, returned as a scalar or a column vector of size 8.

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

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

### **parityCheck** — Parity check status indicator scalar

Parity check status indicator, returned as a Boolean scalar. The port indicates
the status of the parity check after the decoding operation.

- `0` — Indicates that the parity check failed
- `1` — Indicates that the parity check passed

#### Dependencies

To enable this port, select the **Enable parity check output
port** parameter.

**Data Types:** `Boolean`

### **actIter** — Actual number of iterations scalar

Actual number of iterations the block takes to decode the output, returned as a
scalar.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Early`.

**Data Types:** `uint8`

## Parameters

### **FEC frame source** — Source for FEC frame `Input port` (default) | `Property`

Select the FEC frame source as `Input port` or
`Property`.

- `Property` — Select this option to enable the
  **FEC frame type** parameter.
- `Input port` — Select this option to enable the
  **frameType** port.

### **FEC frame type** — FEC frame type `Normal` (default) | `Short`

Select the FEC frame type as `Normal` or
`Short`.

#### Dependencies

To enable this parameter, set the **FEC frame source** parameter
to `Property`.

### **Parallelism level** — Parallelism level `45` (default) | `180`

*Since R2024b*

Select the parallelism level as `45` or
`180`.

### **Code rate source** — Source for code rate `Property` (default) | `Input port`

Select the code rate source as `Property` or
`Input port`.

- `Property` — Select this option to enable the
  **Code rate** parameter.
- `Input port` — Select this option to enable
  the **codeRateIdx** port.

#### Dependencies

To enable this parameter, set the **FEC frame source** parameter
to `Property`.

### **Code rate** — Code rate `1/4` (default) | `1/3` | `2/5` | `1/2` | `3/5` | `2/3` | `3/4` | `4/5` | `5/6` | `8/9` | `9/10`

Select the code rate.

**Note**

Code rate of `9/10` is not supported for short
frame.

#### Dependencies

To enable this parameter, set the **FEC frame source** parameter
to `Property` and set the **Code rate
source** parameter to `Property`.

### **Algorithm** — LDPC decoding algorithm `Min-sum` (default) | `Normalized min-sum`

Select the type of LDPC decoding algorithm. For more information, see Algorithm.

- `Min-sum` — Use this option to select the layered
  belief propagation algorithm with a min-sum approximation. For more information, see
  Min-Sum Approximation.
- `Normalized min-sum` — Use this option to select the
  layered belief propagation algorithm with a normalized min-sum approximation. For
  more information, see Normalized Min-Sum Approximation.

### **Source for scaling factor** — Source for scaling factor `Property` (default) | `Input port`

*Since R2024b*

Specify the scaling factor.

- `Property` — Select this option to enable the
  **Scaling factor** parameter.
- `Input port` — Select this option to enable the
  **scalingFactorIdx** port.

#### Dependencies

To enable this parameter, set the **Algorithm** parameter to
`Normalized min-sum`.

### **Scaling factor** — Scaling factor for normalized min-sum decoding `0.75` (default) | scalar in the range 0.5 to 1, incremented by 0.0625

Specify the scaling factor as a scalar in the range 0.5 to 1, incremented by 0.0625.
For better performance, it is recommended to use scaling factors `0.75`
and `1`.

#### Dependencies

To enable this parameter, set the **Algorithm** parameter to
`Normalized min-sum` and the **Source for scaling
factor** parameter to `Property`.

### **Decoding termination criteria** — Termination criteria `Max` (default) | `Early`

Select the decoding termination criteria.

- `Max` — Terminate decoding when the block
  reaches the number of iterations specified in the block mask or through the
  **iter** input port.
- `Early` — Terminate decoding when the block
  meets all of the parity checks or when the block reaches the maximum number of
  iterations provided in the block mask.

### **Source for number of iterations** — Source selection for number of iterations `Property` (default) | `Input port`

Select the source for specifying the number of iterations.

You can set the number of iterations by using either an input port or a
parameter.

- `Property` — Select this option to enable the
  **Number of iterations** parameter.
- `Input port` — Select this option to enable the
  **iter** port.

### **Number of iterations** — Number of decoding iterations `8` (default) | integer in the range from 1 to 63

Specify the number of decoding iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Max` and the
**Source for number of iterations** parameter to
`Property`.

### **Maximum number of iterations** — Maximum number of decoding iterations `8` (default) | integer in the range from 1 to 63

Specify the maximum number of decoding iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Early` and set the
**Source for number of iterations** parameter to
`Property`.

### **Enable parity check output port** — Parity check status `off` (default) | `on`

Select this parameter to enable the **parityCheck** output port to
view the status of the parity check.

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

**Introduced in R2022a**

### R2025a: Support for vector input

The DVB-S2 LDPC Decoder block now supports column vector as input.

### R2024b: Support for parallelism level 180 and option to specify scaling factor through input port

The DVB-S2 LDPC Decoder block now supports specifying the scaling factor
through an input port and the parallelism level for the block for faster decoding.

- To enable the **scalingFactorIdx** input port, set the
  **Algorithm** parameter to `Normalized
  min-sum`, and then set the **Source for scaling
  factor** parameter to `Input port`.
- To specify parallelism for the block, set the **Parallelism
  level** parameter to `45` or
  `180`.

## Description

Decode LDPC code according to DVB-S2 standard

The DVB-S2 LDPC Decoder block implements a low-density parity-check (LDPC)
decoder using layered belief propagation with min-sum approximation and normalized min-sum
approximation algorithms for decoding LDPC codes according to the Digital Video Broadcast
Satellite Second Generation (DVB-S2) standard. The block accepts log-likelihood ratio (LLR)
values, a stream of control signals, a frame type, and a code rate as inputs and outputs
decoded bits, a stream of control signals, and a signal that indicates when the block is ready
to accept new inputs.

The DVB-S2 LDPC Decoder block supports early termination to help improve
decoding performance and convergence speeds at high signal-to-noise-ratio (SNR) conditions.
The block supports parallelism at two levels 45 and 180. The block supports scalar and vector
values through the input/output (I/O) interface. It also supports forward error correction
(FEC) frames of type normal and short with all the code rates supported by the DVB-S2
standard. For more information about the DVB-S2 standard, see [1].

The block provides an architecture suitable for HDL code generation and hardware
deployment. You can use this block in DVB-S2 modem development.
