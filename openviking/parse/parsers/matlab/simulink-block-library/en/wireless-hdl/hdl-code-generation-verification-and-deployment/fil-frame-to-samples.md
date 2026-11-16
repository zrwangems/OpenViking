---
type: simulink-block
title: 'FIL Frame To Samples'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation, Verification, and Deployment'
documentation_page: 'filframetosamples'
documentation_source_path: 'ref/filframetosamples.html'
language: en
---

# FIL Frame To Samples

## Ports

### Input

### **frame** — Frame of input samples column vector

Frame of input samples, specified as a column vector. All samples in
the vector are considered valid. Each frame must be the same
size.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **sampleN** — Sample stream vector

Stream of samples, returned as a vector representing an entire frame.
The output stream includes idle cycles between samples and between
frames as specified in the block parameters.

If you set **Output size** greater than one, the
block shows one port for each output value. In this case, a single
sample is represented by N values, such as turbo-encoded samples
represented by one systematic value and two parity values. The output
data is one vector for each port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **start** — Start of frame vector

Start of frame, returned as a `Boolean` vector
containing one value for each sample in the frame. This signal is 1
(true) for one time step corresponding to the first valid sample of the
frame.

**Data Types:** `Boolean`

### **end** — End of frame vector

End of frame, returned as a `Boolean` vector
containing one value for each sample in the frame. This signal is 1
(true) for one time step corresponding to the last valid sample of the
frame.

**Data Types:** `Boolean`

### **valid** — Validity of samples vector

Validity of samples, returned as a `Boolean` vector
containing one value for each sample in the frame. This signal is 1
(true) on time steps that correspond to valid samples.

**Data Types:** `Boolean`

## Parameters

### **Idle cycles between samples** — Number of idle cycles to insert after each sample `0` (default) | integer

Number of idle cycles to insert after each sample, specified as a scalar
integer. The block returns a zero on each **sampleN** port
for each idle cycle and sets all control signals to 0
(`false`).

### **Idle cycles between frames** — Number of idle cycles to insert at the end of each frame `0` (default) | integer

Number of idle cycles to insert at the end of each frame, specified as a
scalar integer. The block returns a zero on each
**sampleN** port for each idle cycle and sets all
control signals to 0 (`false`).

### **Output size** — Number of values representing each sample `1` (default) | positive integer

Number of values representing each sample, specified as a positive integer
scalar. The block has **Output size** output sample ports.
The control signals apply to all **sampleN** ports.

For example, you can use this parameter to serialize turbo-encoded
samples. In the LTE standard, the turbo code rate is 1/3, so each sample is
represented by one systematic value and two parity values:
*S\_n*, *P1\_n*, and
*P2\_n*. In this case, set **Output
size** to `3`.

### **Compose output from interleaved input samples** — Order of output samples relative to input order off (default) | on

Order of output samples relative to input order, when more than one value
represents each sample.

For example, for 1/3 turbo-encoded samples, the input frame can be ordered
`[S_1 P1_1 P2_1 S_2 P1_2 P2_2]` or `[S_1 S_2
P1_1 P1_2 P2_1 P2_2]`. In the first case, the output is two
vectors, `[S_1 P1_1 P2_1]` and `[S_2 P1_2
P2_2]`. To achieve the same output in the second case, select
**Compose output from interleaved input
samples**.

#### Dependencies

This parameter applies when **Output size** is
greater than one.

## Libraries

Wireless HDL Toolbox / I/O Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

## Version History

**Introduced in R2017b**

## Description

Convert frame-based data to sample stream for FPGA-in-the-loop

The FIL Frame To Samples block performs the same frame-to-sample
conversion as the Frame To
Samples block. It returns output data as vectors of the entire frame of
samples. The block returns control signal vectors of the same width as the sample data.
This optimization makes more efficient use of the communication link between the FPGA
board and your Simulink® simulation when using FPGA-in-the-loop (FIL). To run FPGA-in-the-loop, you
must have an HDL Verifier™ license.

When you generate a programming file for a FIL target in Simulink, the tool creates a model to compare the FIL simulation with your
Simulink design. For Wireless HDL Toolbox™ designs, the FIL block in that model replicates the sample-streaming
interface to send one sample at a time to the FPGA. You can modify the autogenerated
model to use the FIL Frame To Samples and FIL Samples To
Frame blocks to improve communication bandwidth with the FPGA board by
sending one frame at a time. For how to modify the autogenerated model, see FPGA-in-the-Loop.
