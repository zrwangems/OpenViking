---
type: simulink-block
title: 'Frame To Samples'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Model Architecture'
documentation_page: 'frametosamples'
documentation_source_path: 'ref/frametosamples.html'
language: en
---

# Frame To Samples

## Ports

### Input

### **frame** — Frame of input samples column vector

Frame of input samples, specified as a column vector. All samples in
the vector are considered valid. Each frame must be the same size.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **sample** — Output sample stream scalar | vector

Output sample stream, returned **Output size** values
at a time. The output stream includes idle samples as specified by
**Idle cycles between samples** and **Idle
cycles between frames**. Each output sample has a
corresponding set of control signals on the **ctrl**
port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

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

## Parameters

### **Idle cycles between samples** — Number of idle cycles to insert after each sample `0` (default) | integer

Number of idle cycles to insert after each sample, specified as a scalar
integer. The block returns a vector of **Output size**
zeros for each idle cycle and sets all control signals to 0
(`false`).

### **Idle cycles between frames** — Number of idle cycles to insert at the end of each frame `0` (default) | integer

Number of idle cycles to insert at the end of each frame, specified as a
scalar integer. The block returns a vector of **Output
size** zeros for each idle cycle and sets all control signals
to 0 (`false`).

### **Output size** — Number of values representing each sample `1` (default) | positive integer

Number of values representing each sample, specified as a positive integer
scalar. The block outputs a vector of **Output size**
values. Each vector has one corresponding set of control signals. For
example, you can use this parameter to serialize turbo-encoded samples. In
the LTE standard, the turbo code rate is 1/3, so each sample is represented
by one systematic value and two parity values: *S\_n*,
*P1\_n*, and *P2\_n*. In this case, set
**Output size** to `3`.

### **Compose output from interleaved input samples** — Order of output samples relative to input order off (default) | on

Order of output samples relative to input order, when more than one value
represents each sample. For example, for 1/3 turbo-encoded samples, the
input frame can be ordered `[S_1 P1_1 P2_1 S_2 P1_2 P2_2]`
or `[S_1 S_2 P1_1 P1_2 P2_1 P2_2]`. In the first case, the
output is two vectors, `[S_1 P1_1 P2_1]` and `[S_2
P1_2 P2_2]`. To achieve the same output in the second case,
select **Compose output from interleaved input
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

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

## Version History

**Introduced in R2017b**

## Description

Convert frame-based data to sample stream

The Frame To Samples block flattens frame-based input into a stream of
samples. The block also returns a stream of corresponding control signals that indicate
sample validity and the boundaries of the frame. You can configure idle cycles inserted
between samples or between frames, and how many values represent each sample. See Streaming Sample Interface for details of the
streaming format.

Use this block to generate input for a subsystem targeted for HDL code generation.
This block does not support HDL code generation.
