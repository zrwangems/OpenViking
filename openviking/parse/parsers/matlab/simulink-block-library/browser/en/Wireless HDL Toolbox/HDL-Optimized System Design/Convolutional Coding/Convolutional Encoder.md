---
type: simulink-block
title: 'Convolutional Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Convolutional Coding'
documentation_page: 'convolutionalencoder'
documentation_source_path: 'ref/convolutionalencoder.html'
language: en
---

# Convolutional Encoder

## Ports

### Input

### **data** — Input data bits scalar

Input data bits, specified as `Boolean` or
`ufix1`.

**Data Types:** `Boolean` | `fixed point`

### **valid** — Validity of input data scalar

Control signal that indicates if the input data is valid. When this value is
`1` (true), the block accepts the values on the
**data** input port. When this value is `0`
(false), the block ignores the values on the **data** input
port.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Continuous`.

**Data Types:** `Boolean`

### **reset** — Clears internal states scalar

Clears internal states, specified as a `Boolean` scalar. When
this value is `1` (`true`), the block stops the
current calculation and clears all encoder states.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Continuous` and select the **Enable reset input
port** parameter.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate
the boundaries of the frame and the validity of the input samples.

- `start` — Indicates start of input frame.
- `end` — Indicates end of input frame.
- `valid` — Indicates the data on the input
  **data** port is valid.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Truncated` or
`Terminated`.

**Data Types:** `bus`

### **ISt** — Initial state at every start of frame scalar

Initial state of block at every start of frame, specified as
`fixdt(0,constraint length -1,0)`. Input state is the number of
binary bits in the shift register at the frame start of the block, which is read from
most significant bit (MSB) to least significant bit (LSB).

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Truncated` and select the **Enable initial state
input port** parameter.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **data** — Encoded output data column vector

Output data, returned as 1-by-*n* column vector, if the code rate
is 1/n. The *n* value ranges from 2 to 7.

**Data Types:** `Boolean`

### **valid** — Validity of output samples scalar

Control signal that indicates if the data from the **data**
output port is valid. When this value is `1` (true), the block
returns valid data on the **data** output port. When
**valid** is `false` (`0`), the
values on **data** output port are not valid.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Continuous`.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate
the boundaries of the frame and the validity of the samples.

- `start` — Indicates start of output frame.
- `end` — Indicates end of output frame.
- `valid` — Indicates the data on the output
  **data** port is valid.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Truncated` or
`Terminated`.

**Data Types:** `bus`

### **FSt** — Final state of frame at every frame end scalar

Final state of frame at every frame end, returned as `fixdt(0,constraint
length -1,0)`. Final state is the number of binary bits in the shift
register at the frame end of the block, which is read from most significant bit (MSB)
to least significant bit (LSB).

The block returns the same as the **ISt** data type.

#### Dependencies

To enable this port, set the **Operation mode** parameter to
`Truncated` and select the **Enable final state
output port** parameter.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Main

### **Constraint length** — Constraint length of block `7` (default) | integer in the range [3, 9]

Constraint length of the block, specified as an integer in the range [3,
9].

### **Code generator** — Code generation polynomial `[171 133]` (default) | vector of octal values

Code generation polynomial, specified as a 1-by-*n* vector of
octal values, where *n* is the length of the polynomial ranged from 2
to 7.

### **Feedback connection** — Feedback connection polynomial `0` (default) | scalar octal number

Feedback polynomial, specified as a scalar octal number. If the feedback
connection is `0`, there is no feedback connection enabled.

To enable feedback connection, specify an octal value whose binary representation
must be a K-bit number with MSB `1`, where *K* is
the **Constraint length**. For more information on how to construct a
feedback polynomial, refer to Convolutional Codes.

### **Operation mode** — Mode of operation `Continuous` (default) | `Terminated` | `Truncated`

Mode of operation, specified as one of these modes:

- `Continuous` — In this mode, the block starts
  with all zeros state and retains the encoder states at the end of each input, for
  use with the next input.
- `Terminated` — In this mode, the block
  considers each input frame independently. The encoder states of the block are
  reset to all-zeros state at the end of each frame by appending bits.

  **Note**

  This mode requires a minimum frame gap of **Constraint
  length** – 1 cycles between frames. If no sufficient frame gap is
  provided, the block stops processing the old frame and starts processing a new
  frame.
- `Truncated` — In this mode, the block
  considers each input frame independently. The encoder states are reset to
  all-zeros state at the start of each input.

### Control Ports

### **Enable reset input port** — Reset input signal `off` (default) | `on`

Select this parameter to enable the **reset** port. When
**reset** is `1` (`true`), the
block resets the encoder state in the next clock cycle.

#### Dependencies

To enable this parameter, set the **Operation mode** parameter
to `Continuous`.

### **Enable initial state input port** — Initial state input signal `Off` (default) | `On`

Select this parameter to enable the **ISt** port.

#### Dependencies

To enable this parameter, set the **Operation mode** parameter
to `Truncated`.

### **Enable final state output port** — Final state output signal `Off` (default) | `On`

Select this parameter to enable the **FSt** port.

#### Dependencies

To enable this parameter, set the **Operation mode** parameter
to `Truncated`.

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

## Version History

**Introduced in R2019b**

## Description

Encode data bits using convolution coding — optimized for HDL code generation

The Convolutional Encoder block encodes data bits using convolution coding.
The block supports code rates from 1/2 to 1/7 and constraint lengths from 3 to 9 including
both recursive and nonrecursive polynomials. The block provides an architecture suitable for
HDL code generation and hardware deployment.

The block operates in three modes: continuous with an optional reset port, terminated, and
truncated with optional initial state and final state ports. In
`Continuous` mode, the block accepts data bits, along with a valid
signal, and outputs encoded bits with a valid signal. In `Terminated`
and `Truncated` modes, the block accepts data bits, along with a
`samplecontrol` bus and outputs encoded bits with a
`samplecontrol` bus.

The block supports communication standards such as Wi-Fi (802.11a/b/g/n/ac), digital
satellite communications, digital video broadcast (DVB), 3GPP2, IEEE 802.16, HIPERLAN, and
other technologies. You can use this block to implement other channel codes such as turbo
codes, which are used in LTE standards.

This waveform shows the encoded output of the block in
`Terminated` mode, when block parameter **Constraint
length** is set to `7`, **Code generator** to
`[133 171]`, and **Feedback connection** to
`0`. The input and output **ctrl** buses are expanded to
show their control signals.

The latency of the block is three clock cycles, so the block returns the first encoded
output data after three clock cycles. In the `Terminated` mode, after
the end of the frame, the block resets the encoded states to all zeros state by appending
(**Constraint length** – 1) bits. So, the waveform shows the frame gap of
six (**Constraint length** – 1) clock cycles between the end of the frame
(**ctrlIn.endIn**) and the start of the next frame
**ctrlln.startIn**.
