---
type: simulink-block
title: 'LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ldpcdecoder'
documentation_source_path: 'ref/ldpcdecoder.html'
language: en
---

# LDPC Decoder

## Ports
```yaml
ports:
- name: data
  summary: Input LLR values scalar | column vector
  direction: input
  data_types: int8 | int16 | fixed point
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: iter
  summary: Number of iterations scalar
  direction: input
  data_types: uint8
- name: data
  summary: Decoded data bits scalar | column vector
  direction: output
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: actIter
  summary: Actual number of iterations scalar
  direction: output
  data_types: uint8
- name: parityCheck
  summary: Parity check status indicator scalar
  direction: output
  data_types: Boolean
- name: nextFrame
  summary: Ready for new inputs scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input LLR values scalar | column vector

Input log-likelihood ratio (LLR) values, specified as a scalar or a column vector
of size *n*, where *n* must be factor of
**Block size**.

The data type of this input must be a signed fixed-point with a word length in the
range [4, 16 ] and fraction length in the range [0, 15 ].

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

### **iter** — Number of iterations scalar

Number of iterations, specified as a integer in the range [1, 63].

If you specify **iter** as a value greater than 63, the block
automatically sets the **iter** value to `8` and
performs the decoding operation.

#### Dependencies

To enable this port, set the **Source for number of
iterations** parameter to `Input port`.

**Data Types:** `uint8`
### Output

### **data** — Decoded data bits scalar | column vector

Decoded output data bits, returned as a scalar or a column vector of size
*n*, where *n* must be factor of **Block
size**.

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
- name: Parity-check matrix
  summary: QC-LDPC matrix [5 14 12 1 2 37 45 26 24 0 3 -1 34 7 46 10 -1 -1 -1 -1; 0 35 1 26 0 10 16 16 34 4 2 23 0 51 -1 49
    20 -1 -1 -1; 12 28 22 46 3 16 51 2 25 29 19 18 52 -1 37 -1 34 39 -1 -1; 0 51 16 31 13 39 27 33 8 27 53 13 -1 52 33 -1
    -1 38 7 -1; 36 6 3 51 4 19 4 45 48 9 -1 11 22 23 43 -1 -1 -1 14 1] (default) | any QC-LDPC matrix with circulant weight
    1
  group: ''
- name: Block size
  summary: Size of block 56 (default) | integer in the range [2, 512]
  group: ''
- name: Algorithm
  summary: Type of algorithm Min-sum (default) | Normalized min-sum
  group: ''
- name: Scaling factor
  summary: Scaling factor 0.75 (default) | values in the range from 0.5 to 1, incremented by 0.0625
  group: ''
- name: Decoding termination criteria
  summary: Termination criteria Max (default) | Early
  group: ''
- name: Source for number of iterations
  summary: Source selection for number of iterations Property (default) | Input port
  group: ''
- name: Number of iterations
  summary: Number of iterations 8 (default) | integer in the range [1, 63]
  group: ''
- name: Maximum number of iterations
  summary: Maximum number of iterations 8 (default) | integer in the range [1, 63]
  group: ''
- name: Enable parity check output port
  summary: Parity check status off (default) | on
  group: ''
```

### **Parity-check matrix** — QC-LDPC matrix `[5 14 12 1 2 37 45 26 24 0 3 -1 34 7 46 10 -1 -1 -1 -1; 0 35 1 26 0 10 16 16 34 4 2 23 0 51 -1 49 20 -1 -1 -1; 12 28 22 46 3 16 51 2 25 29 19 18 52 -1 37 -1 34 39 -1 -1; 0 51 16 31 13 39 27 33 8 27 53 13 -1 52 33 -1 -1 38 7 -1; 36 6 3 51 4 19 4 45 48 9 -1 11 22 23 43 -1 -1 -1 14 1]` (default) | any QC-LDPC matrix with circulant weight 1

Specify a QC-LDPC parity-check matrix of size
*M*-by-*N*, where *M* is the number
of rows in the parity-check matrix and *N* is the number of columns in
the parity-check matrix. *N* must be in the range [4, 128].
*M* must be less than *N* and must be in the range
[3, *N*–1]. The last *M* columns of the parity-check
matrix must be invertible in GF(2).

To learn more about the supported parity-check matrices, see Parity-Check Matrix.

### **Block size** — Size of block `56` (default) | integer in the range [2, 512]

Specify the block size. The block size must be an integer in the range [2,
512].

### **Algorithm** — Type of algorithm `Min-sum` (default) | `Normalized min-sum`

Select the type of LDPC decoding algorithm. For more information, see Algorithms.

- `Min-sum` — Use this option to select the layered
  belief propagation algorithm with a min-sum approximation. For more information, see
  Min-Sum Approximation.
- `Normalized min-sum` — Use this option to select the
  layered belief propagation algorithm with a normalized min-sum approximation. For
  more information, see Normalized Min-Sum Approximation.

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
  port.
- `Early` — Terminates decoding when all of the
  parity checks are met or when the block reaches the maximum number of iterations
  specified through the **Maximum number of iterations** parameter or
  through the **iter** input port.

### **Source for number of iterations** — Source selection for number of iterations `Property` (default) | `Input port`

Select the source for specifying the number of iterations.

You can set the number of iterations by using either an input port or a
parameter.

- Select `Property` to enable either the **Number
  of iterations** parameter or the **Maximum number of
  iterations** parameter.
- Select `Input port` to enable the
  **iter** port.

### **Number of iterations** — Number of iterations `8` (default) | integer in the range [1, 63]

Specify the number of iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Max` and the
**Source for number of iterations** parameter to
`Property`.

### **Maximum number of iterations** — Maximum number of iterations `8` (default) | integer in the range [1, 63]

Specify the maximum number of iterations.

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Early` and the
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

**Introduced in R2023b**

## Description

Decode quasi-cyclic low-density parity-check code

The LDPC Decoder block implements a quasi-cyclic low-density parity-check
(QC-LDPC) decoder with hardware-friendly control signals. The block accepts log-likelihood
ratio (LLR) values and a stream of control signals and outputs decoded bits, a stream of
control signals, and a signal that indicates whether the block is ready to accept new inputs.

This block provides an option to implement layered belief propagation with either the
normalized min-sum approximation algorithm or the min-sum approximation algorithm. The
LDPC Decoder block supports scalar and N-element column vector inputs with a
specified parity-check matrix and block size. The block supports the early termination feature
to help improve decoding performance and faster convergence speeds at high signal noise ratio
(SNR) conditions. The block supports QC-LDPC codes of circulant weight 1.

The block enables decoding of multiple code rates to help achieve high throughput
efficiency with a high degree of code rate flexibility. You can use this block to develop a
standard-based or generalized receiver that uses a QC-LDPC for forward error correction (FEC)
coding. The block provides an architecture suitable for HDL code generation and hardware
deployment. For more information, see Algorithms.
