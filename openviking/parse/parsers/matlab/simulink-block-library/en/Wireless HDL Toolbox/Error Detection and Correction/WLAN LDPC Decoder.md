---
type: simulink-block
title: 'WLAN LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'wlanldpcdecoder'
documentation_source_path: 'ref/wlanldpcdecoder.html'
language: en
---

# WLAN LDPC Decoder

## Ports
```yaml
ports:
- name: data
  summary: LLR values scalar | column vector
  direction: input
  data_types: int8 | int16 | signed fixed point
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: blkLenIdx
  summary: Block length index 0 | 1 | 2
  direction: input
  data_types: fixdt(0,2,0)
- name: codeRateIdx
  summary: Code rate index 0 | 1 | 2 | 3
  direction: input
  data_types: fixdt(0,2,0)
- name: iter
  summary: Number of iterations scalar
  direction: input
  data_types: uint8
- name: data
  summary: Decoded bits scalar | column vector
  direction: output
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: nextFrame
  summary: Block ready indicator Boolean scalar
  direction: output
  data_types: Boolean
- name: actIter
  summary: Actual number of iterations scalar
  direction: output
  data_types: uint8
- name: parityCheck
  summary: Parity check status indicator scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — LLR values scalar | column vector

LLR values, specified as a scalar or a column vector of size 8-by-1.

For HDL code generation, specify this value in `signed fixed
point` format. The input word length must be in the range from 4 to
16.

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

### **blkLenIdx** — Block length index `0` | 1 | 2

Block length index, specified as `0`, `1`, or
`2`. The block length varies based on the specified block length
index.

This table shows the block length index values and their corresponding block
lengths.

| blkLenIdx Value | Block Length |
| --- | --- |
| `0` | 648 |
| `1` | 1296 |
| `2` | 1944 |

When you specify a value other than `0`, `1`, or
`2`, the block discards the frame and sets the
**nextFrame** output port to `1`.

#### Dependencies

To enable this port, set the **Standard** parameter to
`IEEE 802.11 n/ac/ax`.

**Data Types:** `fixdt(0,2,0)`

### **codeRateIdx** — Code rate index `0` | 1 | 2 | 3

Code rate index, specified as `0`, `1`,
`2`, or `3`. The code rate varies based on the
standard and code rate index that you specify.

This table shows the code rate index values and their corresponding code rates
based on the standard.

| Standard Parameter Value | codeRateIdx Value | Code Rate |
| --- | --- | --- |
| `IEEE 802.11 n/ac/ax` | `0` | 1/2 |
| `1` | 2/3 |
| `2` | 3/4 |
| `3` | 5/6 |
| `IEEE 802.11 ad` | `0` | 1/2 |
| `1` | 5/8 |
| `2` | 3/4 |
| `3` | 13/16 |

**Data Types:** `fixdt(0,2,0)`

### **iter** — Number of iterations scalar

Number of iterations, specified as an unsigned integer in the range from 1 to
63.

If you specify an **iter** value greater than 63 or less than 1,
the block overrides your specification and sets the **iter** value to
`8` before decoding.

#### Dependencies

To enable this port, set the **Decoding termination criteria**
parameter to `Max` and the **Source for number of
iterations** parameter to `Input port`.

**Data Types:** `uint8`
### Output

### **data** — Decoded bits scalar | column vector

Decoded bits, returned as a scalar or a column vector of size 8-by-1.

For a vector input, if the output data length is not a multiple of 8, the block
appends zeros at the end of the output to make it as a multiple of 8.

For example, when you set the **Standard** parameter to
`IEEE 802.11 n/ac/ax`, the **blkLenIdx**
input port to `0`, and the **codeRateIdx** input
port to `2`, instead of the block returning the 486 samples, the
block appends two zeros to the 486 samples to make it as a multiple of 8. In this
case, the block returns 488 samples in 61 (488/8) clock cycles.

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
```yaml
parameters:
- name: Standard
  summary: Type of standard IEEE 802.11 n/ac/ax (default) | IEEE 802.11 ad
  group: ''
- name: Algorithm
  summary: LDPC decoding algorithm Min-sum (default) | Normalized min-sum
  group: ''
- name: Scaling factor
  summary: Scaling factor for normalized min-sum decoding 0.75 (default) | scalar in the range from 0.5 to 1, incremented
    by 0.0625
  group: ''
- name: Decoding termination criteria
  summary: Termination criteria Max (default) | Early
  group: ''
- name: Source for number of iterations
  summary: Source selection for number of iterations Property (default) | Input port
  group: ''
- name: Number of iterations
  summary: Number of decoding iterations 8 (default) | integer in the range from 1 to 63
  group: ''
- name: Maximum number of iterations
  summary: Maximum number of decoding iterations 8 (default) | integer in the range from 1 to 63
  group: ''
- name: Enable parity check output port
  summary: Parity check status off (default) | on
  group: ''
```

### **Standard** — Type of standard `IEEE 802.11 n/ac/ax` (default) | `IEEE 802.11 ad`

Select the type of standard. For more information, see [1], [2], and [3].

When you set the **Standard** parameter to `IEEE 802.11
ad`, the **blkLenIdx**  input port is disabled and the
block considers a fixed block length of 672 for its operation.

### **Algorithm** — LDPC decoding algorithm `Min-sum` (default) | `Normalized min-sum`

Select the type of LDPC decoding algorithm. For more information, see Algorithm.

- `Min-sum` — Use this option to select the layered
  belief propagation algorithm with a min-sum approximation. For more information, see
  Min-Sum Approximation.
- `Normalized min-sum` — Use this option to select the
  layered belief propagation algorithm with a normalized min-sum approximation. For
  more information, see Normalized Min-Sum Approximation.

### **Scaling factor** — Scaling factor for normalized min-sum decoding `0.75` (default) | scalar in the range from 0.5 to 1, incremented by 0.0625

Specify the scaling factor as scalar in the range from 0.5 to 1, incremented by
0.0625.

#### Dependencies

To enable this parameter, set the **Algorithm** parameter to
`Normalized min-sum`.

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

#### Dependencies

To enable this parameter, set the **Decoding termination
criteria** parameter to `Max`.

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
criteria** parameter to `Early`.

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

**Introduced in R2021b**

## Description

Decode LDPC code according to WLAN standard

The WLAN LDPC Decoder block implements a low-density parity-check (LDPC)
decoder using a layered belief propagation with min-sum approximation and normalized min-sum
approximation algorithms for decoding LDPC codes according to the wireless local area network
(WLAN) standards IEEE®
802.11n™, 802.11ac™, 802.11ax™, and 802.11ad™. The block accepts log-likelihood ratio (LLR) values, a stream of control
signals, a block length, and a code rate as inputs and outputs decoded bits, a stream of
control signals, and a signal that indicates when the block is ready to accept new
inputs.

The WLAN LPDC Decoder block supports scalar inputs and vector inputs. The
block supports early termination to help improve decoding performance and convergence speeds
at high signal-noise-ratio (SNR) conditions. For more information about WLAN standards, see
[1], [2], and [3].

The block provides an architecture suitable for HDL code generation and hardware
deployment. You can use this block in the WLAN modem development.
