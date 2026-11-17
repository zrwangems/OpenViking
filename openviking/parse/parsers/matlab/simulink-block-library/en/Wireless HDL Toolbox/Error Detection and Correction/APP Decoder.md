---
type: simulink-block
title: 'APP Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'appdecoder'
documentation_source_path: 'ref/appdecoder.html'
language: en
---

# APP Decoder

## Ports
```yaml
ports:
- name: LLRc
  summary: Coded LLR values real-valued column vector
  direction: input
  data_types: single | double | int8 | int16 | signed fixed point
- name: LLRu
  summary: Uncoded LLR values real-valued scalar
  direction: input
  data_types: single | double | int8 | int16 | signed fixed point
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: LLRu
  summary: Uncoded LLR values real-valued scalar
  direction: output
  data_types: single | double | int8 | int16 | fixed point
- name: LLRc
  summary: Coded LLR values real-valued column vector
  direction: output
  data_types: single | double | int8 | int16 | fixed point
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: nextFrame
  summary: Block ready indicator Boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **LLRc** — Coded LLR values real-valued column vector

Coded LLR values, specified as a real-valued column vector of size
*N*-by-1, where *N* is the decoding rate in the
range from 2 to 7.

The input vector size depends on the code rate of the block. The block derives the
code rate from the code generator polynomial value specified in the block mask. The
block supports these code rates: 1/2, 1/3, 1/4, 1/5, 1/6, or 1/7.

`double` and `single` data types are supported for
simulation, but not for HDL code generation. For HDL code generation, the block
supports `fixdt(1,WL,FL)` data type and the input word length (WL)
must be in the range from 4 to 16.

**Data Types:** `single` | `double` | `int8` | `int16` | `signed fixed point`

### **LLRu** — Uncoded LLR values real-valued scalar

Uncoded LLR values, specified as a real-valued scalar.

`double` and `single` data types are supported for
simulation, but not for HDL code generation. For HDL code generation, the block
supports `fixdt(1,WL,FL)` data type and the input word length (WL)
must be in the range from 4 to 16.

**Data Types:** `single` | `double` | `int8` | `int16` | `signed fixed point`

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

### **LLRu** — Uncoded LLR values real-valued scalar

Uncoded LLR values, returned as a real-valued scalar. The output data type is the
same as the input data type.

For inputs of `fixed point` data type, the output word length
increases by
`floor`(log2(*N*)) +
`floor`(log2(*K* – 1)) + 2
bits. *N* is the code rate, and *K* is the
constraint length of the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `fixed point`

### **LLRc** — Coded LLR values real-valued column vector

Coded LLR values, returned as a real-valued column vector of size
*N*-by-1. The output data type is the same as the input data
type.

For `fixed point` inputs, the output word length increases by
`floor`(log2(*N*)) +
`floor`(log2(*K* – 1)) + 2
bits, where *N* is the code rate and *K* is the
constraint length of the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `fixed point`

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

### **nextFrame** — Block ready indicator Boolean scalar

Block ready indicator, returned as a Boolean scalar.

The block sets this signal to `1` (`true`) when
the block is ready to accept the start of the next frame. If the block receives an
input **ctrl.start** signal while **nextFrame** is
`0` (`false`), the block discards the frame in
progress and begins processing the new data.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Code generator
  summary: Code generator polynomial [171,133] (default) | row vector of 2 to 7 elements
  group: ''
- name: Feedback connection
  summary: Code generator polynomial 171 (default) | octal value
  group: ''
- name: Termination method
  summary: End of frame behavior Truncated (default) | Terminated
  group: ''
- name: Algorithm
  summary: Decoding algorithm type Max Log MAP (max) (default) | Log MAP (max*)
  group: ''
- name: Window length
  summary: Window on which MAP algorithm is to be performed 64 (default) | integer in the range 3 to 128
  group: ''
- name: Disable LLRc output port
  summary: Option to disable LLRc output port off (default) | on
  group: ''
```

### **Code generator** — Code generator polynomial `[171,133]` (default) | row vector of 2 to 7 elements

Specify a 1-by-*n* vector of octal values, where
*n* is the length of the polynomial. The block accepts polynomials
from 2 to 7 elements long.

The block derives the constraint length and code rate based on the specified code
generator polynomial. Specify the code generator polynomial in such a way that the
constraint length is in the range from 3 to 9 and the code rates are 1/2, 1/3, 1/4, 1/5,
1/6, or 1/7.

For more information on how to specify a code generator polynomial for decoding
blocks, see Trellis Description of a Convolutional Code.

### **Feedback connection** — Code generator polynomial `171` (default) | octal value

*Since R2023b*

Specify a scalar octal value with reference to the code generator value. If you
specify `0` or `[]`, the block performs decoding
without feedback.

### **Termination method** — End of frame behavior `Truncated` (default) | `Terminated`

Select the termination method to specify the end of the frame behavior.

- `Truncated` — The block resets the state metrics
  after each frame, starts at the all-zeros state, and ends with the non-all-zeros
  state. The input **ctrl** bus qualifies the input samples and marks
  the frame boundaries.
- `Terminated` — The block resets the state
  metrics after each frame and starts and ends in the all-zeros state. The input
  **ctrl** bus qualifies the input samples and marks the frame
  boundaries.

### **Algorithm** — Decoding algorithm type `Max Log MAP (max)` (default) | `Log MAP (max*)`

Select the type of decoding algorithm.

- `Max Log MAP (max)` — Max log MAP
  approximation
- `Log MAP (max*)` — Log MAP approximation

For more information about these algorithms, see [1].

### **Window length** — Window on which MAP algorithm is to be performed `64` (default) | integer in the range 3 to 128

Window on which the MAP algorithm is to be performed, specified as an integer in the
range from 3 to 128. This integer represents the window length.

For better block performance results, the recommended window length is at least five
times the constraint length.

### **Disable LLRc output port** — Option to disable LLRc output port `off` (default) | `on`

Select this parameter to disable the output port **LLRc** from the
block. Clear this parameter to enable the output port **LLRc** on the
block.
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

**Introduced in R2021b**

### R2023b: Support trellis feedback structure

The APP Decoder block now supports trellis feedback structure through a
new parameter **Feedback connection**. This parameter supports a scalar
value.

## Description

Decode convolutionally-coded LLR values using MAP algorithm

The APP Decoder block decodes convolutionally-coded log-likelihood ratio
(LLR) values using the maximum a-posteriori probability (MAP) decoding algorithm. The block
accepts coded and uncoded LLR values and a `samplecontrol` bus, decodes the
coded LLR values, and outputs the updated versions of the coded and uncoded LLR values and
`samplecontrol` bus.

The block supports two decoding algorithms: `Max Log MAP (max)` and
`Log MAP (max*)`. You can select the algorithm by setting the
**Algorithm** parameter. The block supports terminated and truncated modes
and these decoding rates: 1/2, 1/3, 1/4, 1/5, 1/6, and 1/7. The block provides an architecture
suitable for HDL code generation and hardware deployment.

The block supports decoding of serial and parallel concatenated codes. Using this block,
you can build turbo decoders, custom decoders for concatenated codes, and product codes for
iterative decoding.
