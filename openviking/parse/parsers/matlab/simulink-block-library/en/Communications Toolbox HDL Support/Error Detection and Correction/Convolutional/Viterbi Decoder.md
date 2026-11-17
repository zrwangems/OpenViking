---
type: simulink-block
title: 'Viterbi Decoder'
family: 'wireless-hdl'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'viterbidecoder'
documentation_source_path: '../wireless-hdl/ref/viterbidecoder.html'
language: en
---

# Viterbi Decoder

## Ports

### Input

### **data** — Input sample column vector

Input sample, specified as an *n*-by-1 column vector,
where *n* is the length of the generator polynomial.
The block performs soft-decision decoding when the input data type is
fixed point or integer and hard-decision decoding when the input data
type is `Boolean` or `fixdt(0,1,0)`.
The block performs unquantized soft-decision decoding for
`single` and `double` data types,
but these data types are not supported for HDL code generation.

For soft-decision input samples, the block supports word lengths up to
16 bits. For HDL code generation, a word length more than 8 bits is not
recommended due to hardware resource usage. The input data must have a
fraction length of 0.

**Data Types:** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — Validity of input samples scalar

Control signal that indicates when the sample from the
**data** input port is valid. When the
**valid** input port is `1`
(`true`), the block captures the values of the
**data** input port. When the
**valid** input port is `0`
(`false`), the block ignores the input samples.

#### Dependencies

To enable this port, set **Operation mode** to
`Continuous`.

**Data Types:** `Boolean`

### **erasure** — Neutral symbol locations column vector

Neutral symbol locations, specified as a column vector of binary
values the same size as the input **data** vector. When
an **erasure** element is `1`
(`true`), the corresponding input
**data** element is a depunctured neutral value,
and the decoder does not update the branch metric. When an
**erasure** element is `0`
(`false`), the block uses the corresponding input
**data** element to update the branch metric. You
can use the Depuncturer block to drive this port.

#### Dependencies

To enable this port, select **Enable erasure input
port**.

**Data Types:** `Boolean`

### **reset** — Clear internal state scalar

Clear internal state, specified as a `Boolean`
scalar. When **reset** is `1`
(`true`), after one cycle, the block stops the
current calculation and clears internal branch and state metrics.

#### Dependencies

To enable this port, set **Operation mode** to
`Continuous` and select
**Enable reset input port**.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the
`start`, `end`, and
`valid` control signals, which indicate the
boundaries of the frame and the validity of the input samples.

#### Dependencies

To enable this port, set **Operation mode** to
`Terminated` or
`Truncated`.

**Data Types:** `bus`
### Output

### **data** — Output sample scalar

Output sample, returned as a scalar with the same data type as the
input samples.

**Data Types:** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — Validity of output samples scalar

Control signal that indicates when the sample from the
**data** output port is valid. The block sets the
**valid** port to `1`
(`true`) when there is a valid sample on the output
**data** port.

#### Dependencies

Tho enable this port, set **Operation mode** to
`Continuous`.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a
`samplecontrol` bus. The bus includes the
`start`, `end`, and
`valid` control signals, which indicate the
boundaries of the frame and the validity of the samples.

#### Dependencies

To enable this port, set **Operation mode** to
`Terminated` or
`Truncated`.

**Data Types:** `bus`

## Parameters

### **Constraint length** — Trellis constraint length `7` (default) | integer in the range [3, 9]

Trellis constraint length, specified as an integer in the range [3,
9].

### **Code generator** — Code generation polynomial `[171, 133]` (default) | vector of octal values

Code generation polynomial, specified as a 1-by-*n*
vector of octal values, where *n* is the length of the
polynomial. The block accepts polynomials from 2 to 7 elements long.

The block does not support codes with feedback connections.

### **Enable erasure input port** — Use optional erasure signal `off` (default) | `on`

Select this parameter to enable the **erasure** port.

### **Traceback depth** — Number of trellis branches `32` (default) | integer in the range [3, 256]

Number of trellis branches used to construct each traceback path,
specified as an integer. The block supports traceback depth in the range [3,
256]. For nonpunctured samples, the recommended depth is
5×**constraintLength**. For punctured samples, the
recommended depth is 10×**constraintLength**. These values
balance decoding accuracy with the amount of memory used.

For HDL code generation, a traceback depth more than 128 is not
recommended due to hardware resource usage.

### **Operation mode** — End of frame behavior `Continuous` (default) | `Truncated` | `Terminated`

End of frame behavior, specified as one of these modes:

- `Continuous` – The block does not clear
  the internal state metric. The input **valid**
  signal qualifies the input samples.
- `Truncated` – The block resets the state
  metrics after each frame, and the traceback path starts at the state
  with the best metric and ends in the all-zeros state. The input
  **ctrl** bus qualifies the input samples and
  marks the frame boundaries.

  **Note**

  This mode requires a minimum space of **Constraint
  length**–1 cycles between frames.
- `Terminated` – The block resets the state
  metrics after each frame, and the traceback path always starts and
  ends in the all-zeros state. The input **ctrl** bus
  qualifies the input samples and marks the frame boundaries.

### **Enable reset input port** — Use optional reset signal `off` (default) | `on`

Select this parameter to enable the **reset** port. When
**reset** is `1`
(`true`), after one cycle, the block stops the current
calculation and clears internal branch and state metrics.

#### Dependencies

To enable this parameter, set **Operation mode** to
`Continuous`.

## Libraries

Wireless HDL Toolbox / Error Detection and Correction

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

You cannot generate HDL for this block inside a Resettable Synchronous
Subsystem (HDL Coder).

## Version History

**Introduced in R2018b**

## Description

Decode convolutionally encoded data using Viterbi algorithm

The Viterbi Decoder block decodes convolutionally encoded data using a
RAM-based traceback implementation. Viterbi decoding is widely used in LTE standard TS
36.212 [1] and other
forward-error-correction (FEC) applications such as wireless networks
(802.11a/b/g/n/ac), digital satellite communications, digital video broadcast (DVB),
IEEE 802.16, and HiperLAN. To support any of these standards, the block accepts
convolution codes with constraint lengths of 3 to 9, code rates 1/2 to 1/7, and provides
continuous, terminated, and truncated modes. The block provides an architecture and
interface suitable for HDL code generation.

The block supports decoding of punctured codes by providing an optional
**erasure** input port. You can use the Depuncturer
block to insert neutral values in a punctured sample stream, and generate the
**erasure** signal.

The Viterbi Decoder block accepts input samples as hard-decision binary
values or soft-decision log-likelihood-ratios (LLR). Each sample is a column vector,
whose length depends on the encoding scheme. The first waveform shows continuous
operation mode with input samples of signed 4-bit data, using the default block
parameters. The **Traceback depth** is `32`. The block
returns the first decoded output data sample after 148 clock cycles. The decoding
latency is 4×**Traceback depth** + **Constraint
length** + 13 valid input cycles.

Logic Analyzer waveform of continuous operation mode

The second waveform shows three frames in terminated operation mode. The input is
unsigned 4-bit samples, and the block is using the trellis (7,[171 133 112]). The
**Traceback depth** is `32`. The input and output
**ctrl** buses are expanded to show their three control signals.
The latency from each input **ctrl**.`start` to output
**ctrl**.`start` is also 148 clock cycles.

The control signals in the bus indicate the validity of each sample and the boundaries
of the frame. To convert a matrix into a sample stream and corresponding control
signals, use the Frame To
Samples block or the `whdlFramesToSamples` function. For a full description of the streaming
sample interface, see Streaming Sample Interface.

Logic Analyzer waveform of terminated operation mode
