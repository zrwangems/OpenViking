---
type: simulink-block
title: 'LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'ldpcencoder'
documentation_source_path: 'ref/ldpcencoder.html'
language: en
---

# LDPC Encoder

## Ports

### Input

### **data** — Data bits scalar | column vector *(since R2025a)*

Data bits, specified as a specified as a scalar or a column vector of size
*n*, where *n* must be factor of **Block
size**. The input data length must be
(*N*–*M*) x *Z*, where
*M* is the number of rows in the parity-check matrix,
*N* is the number of columns in the parity-check matrix, and
*Z* is the block size.

The size of the vector must be a factor of block size. In case
of prime number block size, the supported vector sizes are 1 and block size
itself.

**Example:** If block size is equal to 56, the supported vector sizes are 1, 2, 4, 7,
8, 14, 28, and 56.

**Example:** If block size is equal to 73, the supported vector sizes are 1 and
73.

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

### **data** — Encoded data bits scalar | column vector *(since R2025a)*

Encoded data bits, returned as a scalar or a column vector of size
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

### **nextFrame** — Ready for new inputs scalar

The block sets this signal to `1` when the block is ready to accept the start
of the next frame. If the block receives an input **start** signal
while **nextFrame** is `0`, the block discards the
frame in progress and begins processing the new data.

For more information, see Using the nextFrame Output Signal.

**Data Types:** `Boolean`

## Parameters

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

**Introduced in R2023a**

### R2025a: Support for vector input

The LDPC Encoder block now supports column vector as input.

## Description

Encode data with quasi-cyclic low-density parity-check code

The LDPC Encoder block implements a quasi-cyclic low-density parity-check
(QC-LDPC) encoder with hardware-friendly control signals. The block accepts data bits and a
stream of control signals and outputs encoded bits, a stream of control signals, and a signal
that indicates whether the block is ready to accept new inputs.

The block supports scalar inputs and vector inputs with a specified parity-check matrix
and block size. The block also supports lower-triangular or upper-triangular, dual-diagonal,
and mixed-diagonal parity-check matrices. The block supports LDPC codes of circulant weight 1.
For more information, see Parity-Check Matrix.

You can use this block to develop a standard-based or generalized transmitter that uses a
QC-LDPC for forward error correction (FEC) coding. The block provides an architecture suitable
for HDL code generation and hardware deployment. See Algorithms.
