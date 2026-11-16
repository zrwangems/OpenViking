---
type: simulink-block
title: 'NR LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrldpcdecoder'
documentation_source_path: 'ref/nrldpcdecoder.html'
language: en
---

# NR LDPC Decoder

## Ports

### Input

### **data** — Input LLR values scalar | column vector

Input log-likelihood ratio (LLR) values, specified as a scalar or a column vector
of size 64.

The data type of this input must be a signed fixed-point with a word length from
4 to 16 bits. For more information on how to specify vector input data, see Specifying Vector Input.

**Data Types:** `int8` | `int16` | `fixed point`

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
current frame and waits for the new frame. For more information about the supported
lifting size values, see section 5.3.2, of TS 38.212 [1].

**Data Types:** `uint16`

### **iter** — Number of iterations scalar

Number of iterations, specified as a integer in the range from 1 to 63.

If you specify **iter** as a value greater than 63, the block
automatically sets the **iter** value to `8` and
performs the decoding operation.

#### Dependencies

To enable this port, set the **Source for number of
iterations** parameter to `Input port`.

**Data Types:** `uint8`

### **numRows** — Number of rows scalar

Number of rows, specified as a scalar.

When you set the **bgn** value to `0` the block
supports the number of rows in the range from 4 to 46. When you set the
**bgn** value to `1`, the block supports the
number of rows in the range from 4 to 42.

#### Dependencies

To enable this port, select the **Enable multiple code rates**
parameter.

**Data Types:** `fixdt(0,6,0)`
### Output

### **data** — Decoded output data bits scalar | column vector

Decoded output data bits, returned as a scalar or a column vector of size
64.

The block outputs data bits in a similar format as the input LLR
values. Extract these output data bits in a similar format for further
processing.

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

### **nextFrame** — Block ready indicator Boolean scalar

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`

### **actIter** — Actual number of iterations scalar

Actual number of iterations the block takes to decode the output, returned as a
scalar.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Early`.

**Data Types:** `uint8`

### **parityCheck** — Parity check status indicator scalar

Parity check status indicator, returned as a Boolean scalar. The port indicates
the status of the parity check after the decoding operation.

- `0` — Indicates that the parity check failed
- `1` — Indicates that the parity check passed

#### Dependencies

To enable this port, select the **Enable parity check output
port** parameter.

**Data Types:** `Boolean`

## Parameters

### **Algorithm** — Type of algorithm `Min-sum` (default) | `Normalized min-sum`

Select the type of algorithm. For more information, see Algorithm (5G Toolbox).

### **Scaling factor** — Scaling factor `0.75` (default) | values in the range from 0.5 to 1, incremented by 0.0625

Specify the scaling factor.

#### Dependencies

To enable this parameter, set the **Algorithm** parameter to
`Normalized min-sum`.

### **Decoding termination criteria** — Termination criteria `Max` (default) | `Early`

Select the decoding termination criteria.

- `Max` — Terminates decoding when the block
  reaches the number of iterations specified through the **Number of
  iterations** parameter or through the **iter** input
  port
- `Early` — Terminates decoding when all of the
  parity checks are met or when the block reaches the maximum number of iterations
  specified through the **Maximum number of iterations** parameter or
  through the **iter** input port

### **Source for number of iterations** — Source selection for number of iterations `Property` (default) | `Input port`

Select the source for specifying the number of iterations.

You can set the number of iterations by using either an input port or a
parameter.

- Select `Property` to enable either the **Number
  of iterations** parameter or the **Maximum number of
  iterations** parameter.
- Select `Input port` to enable the
  **iter** port.

### **Number of iterations** — Number of iterations `8` (default) | integer in the range from 1 to 63

Specify the number of iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Max` and the
**Source for number of iterations** parameter to
`Property`.

### **Maximum number of iterations** — Maximum number of iterations `8` (default) | integer in the range from 1 to 63

Specify the maximum number of iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Early` and the
**Source for number of iterations** parameter to
`Property`.

### **Enable multiple code rates** — Multiple code rates `off` (default) | `on`

Select this parameter to enable the **numRows** input port to
support multiple code rates. For more information about multiple code rates, see Multiple Code Rates.

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

**Introduced in R2020a**

## Description

Decode LDPC code according to 5G NR standard

The NR LDPC Decoder block implements a low-density parity-check (LDPC)
decoder with hardware-friendly control signals. The block accepts punctured log-likelihood
ratio (LLR) values, a stream of control signals, a base graph number, and lifting sizes. The
block outputs decoded bits, a stream of control signals, lifting sizes, and a signal that
indicates when the block is ready to accept new inputs.

This block provides an option to implement layered belief propagation with either the
normalized min-sum approximation algorithm or the min-sum approximation algorithm. This
implementation matches that of the function `nrLDPCDecode` (5G Toolbox). You can use this block
for channel coding of downlink and uplink shared channels and paging channel according to 5G
new radio (NR) standard TS 38.212 [1].

The NR LDPC Decoder block supports scalar and 64-element column vector
inputs. The block supports the early termination feature to help improve decoding performance
and faster convergence speeds at high signal noise ratio (SNR) conditions. The block enables
decoding of multiple code rates to help achieve high throughput efficiency with a high degree
of code rate flexibility. The block provides an architecture suitable for HDL code generation
and hardware deployment. For more information, see Algorithms.
