---
type: simulink-block
title: 'Depuncturer'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'depuncturer'
documentation_source_path: 'ref/depuncturer.html'
language: en
---

# Depuncturer

## Ports
```yaml
ports:
- name: data
  summary: Input sample scalar
  direction: input
  data_types: int8 | int16 | uint8 | uint16 | Boolean | fixdt(0,1,0) | fixdt(S,WL,0) | single | double
- name: puncVector
  summary: Puncture vector column vector of binary values
  direction: input
  data_types: Boolean
- name: syncPunc
  summary: Puncture synchronization signal scalar
  direction: input
  data_types: Boolean
- name: valid
  summary: Validity of input samples scalar
  direction: input
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: data
  summary: Output sample 2-by-1 column vector
  direction: output
  data_types: int8 | int16 | uint8 | uint16 | Boolean | fixdt(0,1,0) | fixdt(S,WL,0) | single | double
- name: valid
  summary: Validity of output data samples scalar
  direction: output
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: erasure
  summary: Neutral symbol locations 2-by-1 column vector
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input sample scalar

Input sample, specified as a scalar. The block inserts a neutral value
at punctured locations based on the data type of the input samples.

| Input Data Type | Inserted Neutral Value |
| --- | --- |
| - `boolean` - `fixdt(0,1,0)` | 0 |
| `fixdt(0,WL,0)` | 2(WL-1) |
| `uint8` | 128 |
| `uint16` | 32768 |
| - `fixdt(1,WL,0)` - `int8` - `int16` - `single` - `double` | 0 |

The block treats the input as hard-decision samples when the input
type is `Boolean` or `fixdt(0,1,0)`.
For signed and unsigned numeric types, the block assumes soft-decision
samples. The block treats samples as signed integers for
`single` and `double` data types,
but these data types are not supported for HDL code generation.

The input sample must have a word length less than or equal to 16
bits, and a fraction length of 0 bits.

**Data Types:** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **puncVector** — Puncture vector column vector of binary values

Puncture vector, specified as a column vector of binary values. The
length of the puncture vector must be an even number in the range [4,
28]. The length must remain constant. The block removes initial zeros
from the provided vector, up to the first `1`
(`true`). After the first `1`
(`true`), the puncture vector cannot contain any
[1:0] subvector matching [0 0].

For example, IEEE 802.11 WLAN standard [1] supports
puncture rates 2/3, 3/4, and 5/6, with respective vector lengths of 4,
6, and 10. To support these multiple rates, set **Puncture
vector source** to `Input port`.
To support the largest vector size, the vector length must be 10 for all
rates. For 2/3 and 3/4 rates, pad the **puncVector**
input with zeros to create a 10-element vector. The puncture vector for
rate 3/4 is `[1 1 0 1 1 0]'`. For a vector length of
10, use `[0 0 0 0 1 1 0 1 1 0]'` as the input
**puncVector**.

When **Operation mode** is set to
`Continuous`, the block captures the value
of **puncVector** when both the
**syncPunc** and input **valid**
ports are `1` (`true`).

When **Operation mode** is set to
`Frame`, the block captures the value of
**puncVector** when both
**ctrl**`.start` and
**ctrl**`.valid` are
`1` (`true`).

#### Dependencies

To enable this port, set **Puncture vector
source** to `Input
port`.

**Data Types:** `Boolean`

### **syncPunc** — Puncture synchronization signal scalar

Puncture synchronization signal, specified as a
`Boolean` scalar value. This input is a control
signal that synchronizes the puncture vector input with the input
sample. When both **syncPunc** and
**valid** are `1`
(`true`), the block aligns the puncture vector to
begin puncturing. The block captures the vector from either the
**puncVector** input port or the **Puncture
vector** parameter. The block ignores the
**puncVector** port when
**syncPunc** is `0`
(`false`).

#### Dependencies

To enable this port, set **Operation mode** to
`Continuous`. When **Operation
mode** is `Frame`, the block
synchronizes the puncture vector using control signals in the input
**ctrl** bus.

**Data Types:** `Boolean`

### **valid** — Validity of input samples scalar

Control signal that indicates when the sample from
**data** input port is valid. When
**valid** is 1 (`true`), the block
captures the values of the **data** input port. When
**valid** is 0 (`false`), the
block ignores the input samples.

#### Dependencies

To enable this port, set **Operation mode** to
`Continuous`.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the
`start`, `end`, and
`valid` control signals, which indicate the
boundaries of the frame and the validity of the samples.

#### Dependencies

To enable this port, set **Operation mode** to
`Frame`.

**Data Types:** `bus`
### Output

### **data** — Output sample 2-by-1 column vector

Output sample, returned as a 2-by-1 column vector. The data type is
same as the data type of the input samples.

**Data Types:** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — Validity of output data samples scalar

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
`Frame`.

**Data Types:** `bus`

### **erasure** — Neutral symbol locations 2-by-1 column vector

Neutral symbol locations, returned as a 2-by-1 column vector
corresponding to the output samples. When **erasure**
is `1` (`true`), the corresponding
output **data** element is a depunctured neutral
value.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Operation mode
  summary: End of frame behavior Continuous (default) | Frame
  group: ''
- name: Puncture vector source
  summary: Source of puncture vector Input port (default) | Property
  group: ''
- name: Puncture vector
  summary: Locations to insert neutral values [1;1;0;1;1;0] (default) | column vector of binary values
  group: ''
```

### **Operation mode** — End of frame behavior `Continuous` (default) | `Frame`

End of frame behavior, specified as one of these modes:

- `Continuous` – Allow changes to
  **puncVector** at any time. To force the
  block to capture the new puncture vector, set
  **syncPunc** to
  `1`(`true`). This waveform
  shows `ufix4` input samples depunctured in
  `Continuous` mode.

  Logic Analyzer waveform that shows depuncture behavior in continuous mode.
- `Frame` – You can only change
  **puncVector** at the start of a frame,
  indicated by **ctrl**`.start`.
  This waveform shows `ufix4` input samples
  depunctured in `Frame` mode.

  Logic Analyzer waveform that shows depuncture behavior in frame mode.

### **Puncture vector source** — Source of puncture vector `Input port` (default) | `Property`

Source of puncture vector, specified as either:

- `Input port` – Specify the puncture
  vector using the **puncVector** port.
- `Property` – Specify the puncture
  vector using the **Puncture vector**
  parameter.

### **Puncture vector** — Locations to insert neutral values `[1;1;0;1;1;0]` (default) | column vector of binary values

Puncture vector, specified as a column vector of binary values. The length
of the puncture vector must be an even number in the range [4, 28]. The
default value is the puncture vector for 3/4 code rate of IEEE 802.11 WLAN
[1].

The puncture vector cannot contain any [1:0] subvector matching
`[0 0]`.

#### Dependencies

To enable this port, set **Puncture vector source**
to `Property`.
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

## Version History

**Introduced in R2018b**

## Description

Reverse puncturing scheme to prepare for decoding

The Depuncturer block replaces punctured symbols with neutral values as
directed by an input puncture vector. The block returns erasure bits, which indicate the
presence of neutral symbols in the output data stream. The block supports continuous and
frame modes of operation. It provides an interface and architecture suitable for HDL
code generation and hardware deployment.

Many wireless communication standards implement different code rates by puncturing
patterns with a base code rate 1/2. The input to the block is a stream of one sample at
a time. You can provide samples represented by hard-decision binary values or
soft-decision log-likelihood ratios (LLR). The block returns output samples as 2-by-1
vectors.

The inserted neutral value depends on the data type of the input sample. For details,
see the input **data** port.
