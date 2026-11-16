---
type: simulink-block
title: 'CCSDS LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsldpcdecoder'
documentation_source_path: 'ref/ccsdsldpcdecoder.html'
language: en
---

# CCSDS LDPC Decoder

## Ports

### Input

### **data** — LLR values scalar | column vector

LLR values, specified as a scalar or an eight-element column vector.

For HDL code generation, specify this value in signed fixed-point format. The
input word length must be an integer in the range [4, 16] and the fractional length
must be in the range [0, 15].

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

### **codeRateIdx** — Code rate index `0` | `1` | `2`

Code rate index, specified as `0`, `1`, or
`2`. You must specify this value in the
`fixdt(0,2,0)` format. Each code rate index value represents a
specific code rate, as this table shows.

| `codeRateIdx` Value | Code Rate |
| --- | --- |
| `0` | 1/2 |
| `1` | 2/3 |
| `2` | 4/5 |

#### Dependencies

To enable this port, set the **Configuration type** parameter
to `AR4JA LDPC`.

**Data Types:** `fixdt(0,2,0)`

### **blkLenIdx** — Block length index `0` | `1` | `2`

Block length index, specified as `0`, `1`, or
`2`. You must specify this value in the
`fixdt(0,2,0)` format.

The block length varies with the specified block length index. The input block
length must be a multiple of 8. This table shows the block length index values and
their corresponding block lengths.

| `blkLenIdx` Value | Block Length |
| --- | --- |
| `0` | 1024 |
| `1` | 4096 |
| `2` | 16384 |

#### Dependencies

To enable this port, set the **Configuration type** parameter
to `AR4JA LDPC`.

**Data Types:** `fixdt(0,2,0)`

### **iter** — Number of iterations integer in the range [1, 63]

Number of iterations, specified as an unsigned integer in the range [1,
63].

If you specify an **iter** value greater than 63 or less than 1,
the block overrides your specification and sets the **iter** value to
`8` before it performs decoding.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Max` and the **Source for number of
iterations** parameter to `Input port`.

**Data Types:** `uint8`
### Output

### **data** — Decoded bits scalar | column vector

Decoded bits, returned as a scalar or an eight-element column vector.

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

### **nextFrame** — Block ready indicator `0` | `1`

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` when the block is ready to
accept the start of the next frame. If the block receives an input
**ctrl.start** signal while **nextFrame** is
`0`, the block discards the frame in progress and begins processing
the new data.

**Data Types:** `Boolean`

### **actIter** — Actual number of iterations positive scalar

Actual number of iterations the block takes to decode the output, returned as a
positive scalar.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Early`.

**Data Types:** `uint8`

### **parityCheck** — Parity check status indicator `0` | `1`

Parity check status indicator, returned as a Boolean scalar. The port indicates
the status of the parity check after the decoding operation.

- `0` — Indicates that the parity check failed
- `1` — Indicates that the parity check passed

#### Dependencies

To enable this port, select the **Enable parity check output
port** parameter.

**Data Types:** `Boolean`

## Parameters

### **Configuration type** — Type of configuration `(8160,7136) LDPC` (default) | `AR4JA LDPC`

Select the configuration type. For more information about the supported
configurations, see [1].

### **Decoding termination criteria** — Termination criteria `Max` (default) | `Early`

Select the decoding termination criteria.

- `Max` — Terminate decoding when the block
  reaches the number of iterations specified in the block mask or the
  **iter** input port.
- `Early` — Terminate decoding when the block
  completes all of the parity checks or when the block reaches the maximum number of
  iterations specified in the block mask.

### **Source for number of iterations** — Source selection for number of iterations `Property` (default) | `Input port`

Select the source for specifying the number of iterations.

You can set the number of iterations by using an input port or a parameter.

- `Property` — Select this option to enable the
  **Number of iterations** parameter.
- `Input port` — Select this option to enable the
  **iter** port.

### **Number of iterations** — Number of decoding iterations `8` (default) | integer in the range [1, 63]

Specify the number of decoding iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Max` and the
**Source for number of iterations** parameter to
`Property`.

### **Maximum number of iterations** — Maximum number of decoding iterations `8` (default) | integer in the range [1, 63]

Specify the maximum number of decoding iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Early` and set the
**Source for number of iterations** parameter to
`Property`.

### **Enable parity check output port** — Parity check status `off` (default) | `on`

Select this parameter to enable the **parityCheck** output port.
Use this output port to view the status of the parity check.

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

**Introduced in R2022b**

## Description

Decode LDPC code according to CCSDS standard

The CCSDS LPDC Decoder block implements a low-density parity-check (LDPC)
decoder using a layered belief propagation algorithm with min-sum approximation for decoding
LDPC codes according to the Consultative Committee for Space Data Systems (CCSDS) standard
[1]. The block accepts
log-likelihood ratio (LLR) values, a stream of control signals, a block length, and a code
rate as inputs. The block outputs decoded bits, a stream of control signals, and a signal that
indicates when the block is ready to accept new inputs.

The block supports scalar inputs and vector inputs of size 8. The block supports early
termination to improve decoding performance and convergence speeds at high signal-to-noise
ratio (SNR) conditions.

The block provides an architecture suitable for HDL code generation and hardware
deployment. You can use this block in a CCSDS receiver for satellite communication.
