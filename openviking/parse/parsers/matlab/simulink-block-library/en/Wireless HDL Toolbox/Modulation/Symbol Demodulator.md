---
type: simulink-block
title: 'Symbol Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'symboldemodulator'
documentation_source_path: 'ref/symboldemodulator.html'
language: en
---

# Symbol Demodulator

## Ports
```yaml
ports:
- name: data
  summary: Data symbols real-valued scalar | complex-valued scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: Valid input data indication scalar
  direction: input
  data_types: Boolean
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: input
  data_types: bus
- name: modSel
  summary: Modulation selection 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
  direction: input
  data_types: single | double | fixdt(0,3,0)
- name: nVar
  summary: Noise variance real-valued positive scalar
  direction: input
  data_types: single | double | uint8 | uint16 | unsigned fixed point
- name: data
  summary: Demodulated LLR values or data bits scalar | real-valued column vector
  direction: output
  data_types: single | double | Boolean | signed fixed point
- name: ctrl
  summary: Control signals accompanying sample stream samplecontrol bus
  direction: output
  data_types: bus
- name: valid
  summary: Valid output data indication scalar
  direction: output
  data_types: Boolean
- name: ready
  summary: Indicates block is ready scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Data symbols real-valued scalar | complex-valued scalar

Data symbols, specified as a real- or complex-valued scalar.

`double` and
`single` data types are supported for simulation, but not for HDL
code generation.

For HDL code generation, the input data type must be `signed fixed
point` and the maximum input word length the block supports is 32
bits.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Valid input data indication scalar

Control signal that indicates if the input data is valid. When this value is
`1` (true), the block accepts the values on the
**data** input port. When this value is `0`
(false), the block ignores the values on the **data** input
port.

#### Dependencies

To enable this port, set the **Output type** parameter to
`Scalar`.

**Data Types:** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, specified as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate
the boundaries of the frame and the validity of the samples.

- `start` — Indicates the start of the input
  frame
- `end` — Indicates the end of the input frame
- `valid` — Indicates that the data on the input
  **data** port is valid

For more detail, see Sample Control Bus.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port` and set the **Output type**
parameter to `Vector`.

**Data Types:** `bus`

### **modSel** — Modulation selection `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7`

Modulation selection, specified as `0`, `1`,
`2`, `3`, `4`,
`5`, `6`, or `7`. Each value
represents a specific modulation type, as shown in this table.

| Modulation Selection Value | Modulation Type |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 8-PSK |
| `3` | 16-PSK |
| `4` | 16-QAM |
| `5` | 32-PSK |
| `6` | 64-QAM |
| `7` | 256-QAM |

If you specify a value other than the values listed in this table or greater than
the value specified on the block mask using the **Maximum
modulation** parameter, the block displays a warning message and applies
BPSK modulation. The values specified through the **modSel** port
must be with respect to the value set with the **Maximum modulation**
parameter.

For example, if the **Maximum modulation** parameter is set to
`32-PSK`, the block allows the **modSel**
values `0`, `1`, `2`,
`3`, `4`, and `5`. For the
**modSel** values `6` and `7`,
the block displays a warning message and applies BPSK modulation.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `fixdt(0,3,0)`

### **nVar** — Noise variance real-valued positive scalar

Noise variance, specified as a real-valued positive scalar.

This value must be of data type
`fixdt(0,k,m)`, where
*k* is less than or equal to 32 and *m* is less
than or equal to *k*.

When the **Output type** parameter is set to
`Scalar` or `Vector`, the block
samples the values on this port when the input **valid** is set to
`1`.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, select the **Enable noise variance input
port** parameter.

**Data Types:** `single` | `double` | `uint8` | `uint16` | `unsigned fixed point`
### Output

### **data** — Demodulated LLR values or data bits scalar | real-valued column vector

Demodulated LLR values or data bits, returned as a scalar when the
**Output type** parameter is set to
`Scalar` and as a real-valued column vector when the
**Output type** parameter is set to
`Vector`.

If you set the **Modulation source** parameter to
`Property`, the output vector size is based on the
**Modulation** parameter value. If you set the **Modulation
source** parameter to `Input port`, the output
vector size is based on the **Maximum modulation** parameter
value.

- When the **Decision type** parameter is set to
  `Approximate log-likelihood ratio`

  - For `double` and `single` inputs, the
    output data type is same as the input data type. `double`
    and `single` data types are supported for simulation data
    types are supported for simulation.
  - For `fixed point` inputs, the block provides the output
    with an integer bit growth of 4 bits and supports HDL code generation. If
    the **Enable noise variance input port** parameter is
    selected, the integer bit growth of the output is 13 bits.
- When the **Decision type** parameter is set to
  `Hard`, the output data type is
  `Boolean` irrespective of the input data type.

**Data Types:** `single` | `double` | `Boolean` | `signed fixed point`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

Control signals accompanying the sample stream, returned as a
`samplecontrol` bus. The bus includes the `start`,
`end`, and `valid` control signals, which indicate
the boundaries of the frame and the validity of the samples.

- `start` — Indicates the start of the output
  frame
- `end` — Indicates the end of the output frame
- `valid` — Indicates that the data on the output
  **data** port is valid

For more detail, see Sample Control Bus.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port` and set the **Output type**
parameter to `Vector`.

**Data Types:** `bus`

### **valid** — Valid output data indication scalar

Control signal that indicates if data from the **data** output
port is valid. When this value is `1` (true), the block returns valid
data on the **data** output port. When this value is
`0` (false), the values on the **data** output
port are not valid.

#### Dependencies

To enable this port:

- Set the **Modulation source** parameter to
  `Input port` or `Property`
  and set the **Output type** parameter to
  `Scalar`.
- Set the **Modulation source** parameter to
  `Property` and set the **Output
  type** parameter to `Vector`.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready scalar

Control signal that indicates when the block is ready to accept new input data.
When this value is `1` (true), the block accepts input data in the
next time step. When this value is `0` (false), the block ignores the
input data in the next time step.

The **ready** signal remains `0` (false) until
the block outputs data of the corresponding input data symbol. The number of clock
cycles that the **ready** signal remains `0` (false)
depends on the selected modulation type.

#### Dependencies

To enable this port, set the **Output type** parameter to
`Scalar`.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Modulation source
  summary: Source for modulation type Property (default) | Input port
  group: ''
- name: Modulation
  summary: Modulation type BPSK (default) | QPSK | 8-PSK | 16-PSK | 16-QAM | 32-PSK | 64-QAM | 256-QAM
  group: ''
- name: Maximum modulation
  summary: Maximum modulation type 256-QAM (default) | BPSK | QPSK | 8-PSK | 16-PSK | 16-QAM | 32-PSK | 64-QAM
  group: ''
- name: Constellation ordering
  summary: Constellation ordering Default (default) | User-defined
  group: ''
- name: Constellation mapping
  summary: Constellation mapping [2, 3, 1, 0, 6, 7, 5, 4, 14, 15, 13, 12, 10, 11, 9, 8] (default) | unique integer-valued
    gray-coded row vector
  group: ''
- name: Decision type
  summary: Type of demapping Approximate log-likelihood ratio (default) | Hard
  group: ''
- name: Phase offset
  summary: Phase offset for constellation points pi/2 (default) | pi/4 | pi/8 | pi/16 | pi/32 | 0 | -pi/32 | -pi/16 | -pi/8
    | -pi/4 | -pi/2
  group: ''
- name: Output type
  summary: Type of output Vector (default) | Scalar
  group: ''
- name: Normalization method
  summary: Scale signal constellation Unit average power (default) | Custom
  group: ''
- name: Minimum distance between symbols
  summary: Minimum distance between symbols 2 (default) | values in the range from 1/32 to 2
  group: ''
- name: Enable noise variance input port
  summary: Option to enable noise variance port off (default) | on
  group: ''
```

### **Modulation source** — Source for modulation type `Property` (default) | `Input port`

To specify the modulation type from the **Modulation** parameter,
select `Property`. To specify the modulation type from the
**modIdx** port during run time, select `Input
port`.

### **Modulation** — Modulation type `BPSK` (default) | `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM` | `256-QAM`

Select the modulation type.

#### Dependencies

To enable this parameter, set the **Modulation source** parameter
to `Property`.

### **Maximum modulation** — Maximum modulation type `256-QAM` (default) | `BPSK` | `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM`

Select the maximum modulation type. This parameter value defines the modulation
types that the block can support through the **modSel** port.

For example, when you specify `16-PSK` using this
parameter, the number of hardware resources the block generates for the
`16-PSK` modulation type can accommodate configurations with
`BPSK`, `QPSK`, and
`8-PSK` modulation types specified through the
**modSel** port, but not configurations with the
`16-QAM`, `32-PSK`,
`64-QAM`, and `256-QAM` modulation
types.

#### Dependencies

To enable this parameter, set the **Modulation source** parameter
to `Input port`.

### **Constellation ordering** — Constellation ordering `Default` (default) | `User-defined`

Select the constellation ordering, that is, how the block assigns binary words to
points of the signal constellation.

- `Default` — Specifies default constellation
  ordering values `[2, 3, 1, 0, 6, 7, 5, 4, 14, 15, 13, 12, 10, 11, 9,
  8]`
- `User defined` — Enables you to specify custom
  constellation ordering values using the **Constellation mapping**
  parameter

#### Dependencies

- To enable this parameter, set the **Modulation source**
  parameter to `Property` and set the
  **Modulation** parameter to `16-QAM`,
  `64-QAM`, or `256-QAM`.
- To enable this parameter, set the **Modulation source**
  parameter to `Input port` and set the **Maximum
  modulation** parameter to `16-QAM`,
  `64-QAM`, or `256-QAM`.

### **Constellation mapping** — Constellation mapping `[2, 3, 1, 0, 6, 7, 5, 4, 14, 15, 13, 12, 10, 11, 9, 8]` (default) | unique integer-valued gray-coded row vector

Specify a unique integer-valued gray-coded row vector corresponding to the
modulation type selected using the **Modulation** parameter or
**Maximum modulation** parameter. The first element of this vector
corresponds to the top-leftmost point of the constellation, with subsequent elements
running down column-wise, from left to right. The last element corresponds to the bottom
rightmost point. For more information on supported gray codes, see Specify Gray Code.

This parameter is specific to the `16-QAM`,
`64-QAM`, and `256-QAM` modulation
types.

#### Dependencies

To enable this parameter, set the **Constellation ordering**
parameter to `User defined`.

### **Decision type** — Type of demapping `Approximate log-likelihood ratio` (default) | `Hard`

Select the demapping type.

- `Approximate log-likelihood ratio` — Demap data
  symbols to LLR values. This LLR value for each bit indicates how likely the bit is
  `1` or `0`.
- `Hard` — Demap data symbols to bits
  `1` or `0`.

### **Phase offset** — Phase offset for constellation points `pi/2` (default) | `pi/4` | `pi/8` | `pi/16` | `pi/32` | `0` | `-pi/32` | `-pi/16` | `-pi/8` | `-pi/4` | `-pi/2`

Select the phase offset. This parameter is specific to the
`BPSK`, `QPSK`,
`8-PSK`, `16-PSK`, and
`32-PSK` modulation types.

#### Dependencies

- To enable this parameter, set the **Modulation source**
  parameter to `Property` and set the
  **Modulation** parameter to `BPSK`,
  `QPSK`, `8-PSK`,
  `16-PSK`, or `32-PSK`.
- To enable this parameter, set the **Modulation source**
  parameter to `Input port` irrespective of the modulation
  types specified for the **Maximum modulation** parameter.

### **Output type** — Type of output `Vector` (default) | `Scalar`

Select the type of output as `Vector` or
`Scalar`.

- `Vector` — Use this option to receive data in
  vector format from the output **data** port.

  When you set the **Modulation source** parameter to
  `Property`, the output vector size is based on the
  **Modulation** parameter value. When you set the
  **Modulation source** parameter to `Input
  port`, the output vector size is based on the **Maximum
  modulation** parameter value.
- `Scalar` — Use this option to receive data in
  scalar format from the output **data** port.

### **Normalization method** — Scale signal constellation `Unit average power` (default) | `Custom`

Select how the block scales the signal constellation.

- `Unit average power` — Normalizes the
  constellation to unit average power
- `Custom` — Enables you to normalize the
  constellation by specifying the minimum distance between the constellation points
  using the **Minimum distance between symbols** parameter

**Note**

When you specify `0`, `1`, `2`,
`3`, or `5` using the **modSel**
input port, the block ignores this parameter during its operation. This is parameter
is applicable for QAM-based modulations.

#### Dependencies

- To enable this parameter, set the **Modulation source**
  parameter to `Property` and set the
  **Modulation** parameter to `16-QAM`,
  `64-QAM`, or `256-QAM`.
- To enable this parameter, set the **Modulation source**
  parameter to `Input port` and set the **Maximum
  modulation** parameter to `16-QAM`,
  `64-QAM`, or `256-QAM`.

### **Minimum distance between symbols** — Minimum distance between symbols `2` (default) | values in the range from 1/32 to 2

Specify the minimum distance between the symbols with the values in the range from
1/32 to 2.

**Note**

When you specify `0`, `1`, `2`,
`3`, or `5` using the **modSel**
input port, the block ignores this parameter during its operation. This parameter is
applicable for QAM-based modulations.

#### Dependencies

To enable this parameter, set the **Normalization method**
parameter to `Custom`.

### **Enable noise variance input port** — Option to enable noise variance port `off` (default) | `on`

Select this parameter to enable the noise variance input port.
## Libraries

Wireless HDL Toolbox / Modulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink® accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that affect HDL implementation and
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

**Introduced in R2022a**

## Description

Demodulate complex constellation symbol to set of LLR values or data bits

The Symbol Demodulator block demodulates a complex constellation symbol to
a set of log-likelihood ratio (LLR) values or data bits. The block accepts equalized complex
data symbols and a `samplecontrol` bus or a `valid` signal
and outputs demodulated LLR values or data bits and a `samplecontrol` bus or
a `valid` signal based on the selected output type. The block provides an
option to select the output type as vector or scalar and provides an input port to specify the
noise variance.

The block supports BPSK, QPSK, 8-PSK, 16-PSK, 32-PSK, 16-QAM, 64-QAM, and 256-QAM
modulations. The number of demodulated LLR values or data bits for a given symbol depends on
the modulation type, as shown in this table.

| Modulation Type | Number of LLR Values or Data Bits per Symbol |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-PSK | 4 |
| 16-QAM | 4 |
| 32-PSK | 5 |
| 64-QAM | 6 |
| 256-QAM | 8 |

This block provides an interface and architecture for HDL code generation with HDL Coder™. You can use this block in the development of a digital receiver.
