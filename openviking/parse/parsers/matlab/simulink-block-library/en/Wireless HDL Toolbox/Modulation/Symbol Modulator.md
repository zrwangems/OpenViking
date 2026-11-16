---
type: simulink-block
title: 'Symbol Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'symbolmodulator'
documentation_source_path: 'ref/symbolmodulator.html'
language: en
---

# Symbol Modulator

## Ports

### Input

### **data** — Data bits scalar | column vector

Data bits, specified as a scalar or a column vector.

Input data bits must be a multiple of *NBPS*, where
*NBPS* is number of bits per symbol. If the specified input data
bits are a nonmultiple of *NBPS*, the block ignores the input with
insufficient or excessive bits.

When you set the **Modulation source** parameter to
`Property`:

- For a scalar input, the data type must be `Boolean`,
  `fixdt(0,1,0)`, or
  `fixdt(0,NBPS,0)`.
- For a vector input, the data type must be `Boolean` or
  `fixdt(0,1,0)`. The dimension of the vector must be
  *NBPS*-by-1.

When you set the **Modulation source** parameter to
`Input port`, for scalar input, the data type must be
`Boolean` or `fixdt(0,1,0)`. This parameter
setting does not support vector input.

**Data Types:** `Boolean` | `unsigned fixed point`

### **valid** — Indicate valid input data scalar

Control signal that indicates if the input data is valid. When this value is
`1` (true), the block accepts the values on the
**data** input port. When this value is `0`
(false), the block ignores the values on the **data** input
port.

**Data Types:** `Boolean`

### **modArrIdx** — Modulation array index integer

Modulation array index, specified as an integer. This value must be corresponding
to the index of the **Modulation array** parameter. For HDL code
generation, specify the value in the `fixdt(0,4,0)` format.

For example, if the **Modulation array** parameter is specified
as `{"QPSK","BPSK,"16-QAM"}` and you want the block to perform in
this sequence: BPSK, 16-QAM, BPSK, and QPSK, then you have to specify the
**modArrIdx** values in the order `1`,
`2`, `1`, and `0`, respectively.
Here, the indices values `0`, `1`, and
`2` correspond to QPSK, BPSK, and 16-QAM, respectively.

If you specify a value that exceeds the index of the modulation types specified in
the **Modulation array** parameter, the block displays a warning
message and:

- Applies the first-specified modulation in the **Modulation
  array** parameter, when **load** is
  `1` (true).
- Continues with the previous modulation when **load** is
  `0` (false).

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `double` | `single` | `fixdt(0,4,0)`

### **load** — Modulation control scalar

Modulation control signal to sample modulation, specified as a
`Boolean` scalar.

When this value is `1` (true), the block applies the modulation
based on the **modArrIdx** value. When this value is
`0` (false), the block ignores any changes in the **modArrIdx** value and continues with the previous modulation
until this value changes to `1` (true).

If the **load** value changes to `1` (true)
during the block operation, the block resynchronizes and restarts modulation using the
current value of **modArrIdx**. This restart occurs
whether or not the **modArrIdx** value has
changed.

For example, if the block is operating in 256-QAM mode and the
**load** value changes to `1` (true) after four of
the eight required input bits are sent into the block, the block discards those first
four bits and restarts its operation from the fifth bit.

If you do not apply the **load** value as `1`
(true) at the start of block operation, by default, the block applies the
first-specified modulation in the **Modulation array**
parameter.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `Boolean`

### **reset** — Clear internal states scalar

Clear internal states, specified as a `Boolean` scalar. When this
value is `1`, the block stops the current calculation and clears all
internal states.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Property` and then select the **Enable reset
input port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Modulated complex data symbols complex scalar

Modulated complex data symbols, returned as a complex scalar.

The block supports `double` and
`single` data types for simulation, but not for HDL code
generation.

For HDL code generation, set the **Output data type** parameter
to `Custom` and specify the word length.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **valid** — Valid output data indication scalar

Control signal that indicates if data from the **data** output
port is valid. When this value is `1` (true), the block returns valid
data on the **data** output port. When this value is
`0` (false), the values on the **data** output
port are not valid.

**Data Types:** `Boolean`

## Parameters

### Main

### **Modulation source** — Source for modulation type `Property` (default) | `Input port`

To specify the modulation type by using the **Modulation**
parameter, select `Property`. To specify the modulation type
through the **modArrIdx** port during run time, select
`Input port`.

### **Modulation** — Modulation type `BPSK` (default) | `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM` | `256-QAM` | `1024-QAM` | `4096-QAM`

Select the modulation type.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property`.

### **Modulation array** — Modulation array `{"BPSK", "QPSK"}` (default) | all the supported modulation types

Specify the modulation types as a string in a cell-array format. The supported
modulation types are: BPSK, QPSK, 8-PSK, 16-PSK, 16-QAM, 32-PSK, 64-QAM, 256-QAM,
1024-QAM, and 4096-QAM.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Input port`.

### **Constellation ordering type** — Type of constellation ordering `Default` (default) | `User-defined`

Select the type of constellation ordering as `Default` or
`User-defined`.

### **Constellation mapping** — Constellation mapping `[0 1]` (default) | row vector

Specify the constellation mapping as a row vector. The row vector must contain
unique elements in the range [0, (*M* – 1)], where
*M* is the modulation order. The dimension of the vector must be
1-by-*M*.

For QAM modulations, the first element corresponds to the upper-left point of the
constellation, with subsequent elements running down column-wise from left to right.
If you set the **Modulation** parameter to
`16-QAM`, the modulation order is 16 and the vector
dimension is 1-by-16. The vector must contain unique elements in the range [0,
15].

**Example:** `[0 1 3 2 4 5 7 6 12 13 15 14 8 9 11 10]`

For PSK modulations, the first element correlates to the constellation point
corresponding to angle specified in the **Phase offset (rad)**
parameter, with subsequent elements running counter-clockwise .If you set the
**Modulation** parameter to `8-PSK`, the
modulation order is 8 and the vector dimension is 1-by-8. The vector must contain
unique elements in the range [0, 7].

**Example:** `[0 1 3 2 6 7 5 4]`

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property` and then set the
**Constellation ordering type** parameter to
`User-defined`.

### **Constellation mapping array** — Constellation mapping array `{[0 1],[0 1 3 2]}` (default) | row vector in a cell array

Specify the constellation mapping array as a row vector in a cell array. The size
of the cell array must be equal to the size of the modulation array.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Input port` and then set the
**Constellation ordering type** parameter to
`User-defined`.

### **Phase offset (rad)** — Phase offset `0` (default) | `pi` | `pi/2` | `pi/4` | `pi/8` | `pi/16` | `pi/32` | `-pi/32` | `-pi/16` | `-pi/8` | `-pi/4` | `-pi/2`

Select the phase offset. This parameter is applicable only for PSK modulation
types, BPSK, QPSK, 8-PSK, 16-PSK, and 32-PSK.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property` and set the
**Modulation** parameter to `BPSK`,
`QPSK`, `8-PSK`,
`16-PSK`, or `32-PSK`.

### **Phase offset type** — Type of phase offset `Default` (default) | `User-defined`

Select the type of phase offset as `Default` or
`User-defined`.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Input port`.

### **Phase offset array (rad)** — Phase offset array `[0 pi/4]` (default) | scalar | row vector of supported phase offset values

Specify the phase offset array. The supported phase offset values are:
`pi`, `pi/2`, `pi/4`,
`pi/8`, `pi/16`, `pi/32`,
`0`, `-pi/2`, `-pi/4`,
`-pi/8`, `-pi/16`, and `-pi/32`.
This parameter is applicable for PSK modulations only.

**Note**

If you specify 16-QAM, 64-QAM, 256-QAM, 1024-QAM, or 4096-QAM in the
**Modulation array**, you have to specify `0` in
the **Phase offset array (rad)** parameter for each QAM.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Input port` and then set the **Phase
offset type** parameter to
`User-defined`.

### **Normalization method** — Scale signal constellation `Minimum distance between symbols` (default) | `Average power`

Select how the block scales the signal constellation.

- `Minimum distance between symbols` — Enables
  you to normalize the constellation by specifying the minimum distance between the
  constellation points using the **Minimum distance**
  parameter.
- `Average power` — Normalizes the constellation
  to average power using the **Average power, referenced to 1 ohm (watts)** parameter.

#### Dependencies

To enable this parameter:

- Set the **Modulation source** parameter to
  `Input port`. Or
- Set the **Modulation source** parameter to
  `Property` and then set the
  **Modulation** parameter to
  `16-QAM`, `64-QAM`,
  `256-QAM`, `1024-QAM`, or
  `4096-QAM`.

### **Minimum distance** — Minimum distance between symbols `0.125` (default) | positive scalar in the range from 1/32 to 1/8

Specify the minimum distance between the symbols as a positive scalar in the range
from 1/32 to 1/8.

#### Dependencies

To enable this parameter:

- Set the **Modulation source** parameter to
  `Input port` and then set the **Normalization
  method** parameter to `Minimum distance between
  symbols`. Or
- Set the **Modulation source** parameter to
  `Property`, set the **Modulation**
  parameter to `16-QAM`,
  `64-QAM`, `256-QAM`,
  `1024-QAM`, or `4096-QAM`,
  and then set the **Normalization method** parameter to
  `Minimum distance between symbols`.

### **Average power, referenced to 1 ohm (watts)** — Average power of the symbols in the constellation `1` (default) | positive scalar in the range 1/32 to 10

Specify the average power of the symbols in the constellation as a positive scalar
in the range 1/32 to 10. Power values assume a nominal impedance of 1 ohm.

#### Dependencies

To enable this parameter:

- Set the **Modulation source** parameter to
  `Input port` and then set the **Normalization
  method** parameter to `Average power`.
  Or
- Set the **Modulation source** parameter to
  `Property`, set the **Modulation**
  parameter to `16-QAM`,
  `64-QAM`, `256-QAM`,
  `1024-QAM`, or `4096-QAM`,
  and then set the **Normalization method** parameter to
  `Average power`.

### **Enable reset input port** — Reset input port `off` (default) | `on`

Select this parameter to enable the **reset** input port.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property`.

### Data Types

### **Output data type** — Output data type selection `Custom` (default) | `double` | `single`

Select the data type for the output data.

`double` and `single` data types
are supported for simulation. For simulation and HDL code generation, set this value
to `Custom`.

### **Word length** — Output word length `16` (default) | integer in the range from 3 to 32

Specify the output word length. This value must be an integer in the range from 3
to 32.

#### Dependencies

To enable this parameter, set the **Output data type**
parameter to `Custom`.

## Libraries

Wireless HDL Toolbox / Modulation

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

**Introduced in R2025a**

## Description

Modulate data bits to complex data symbols

The Symbol Modulator block modulates data bits to complex data symbols. The
block accepts data bits, along with a control signal, and outputs a modulated complex symbol
with a valid signal. Each complex symbol comprises a standard number of bits based on the
modulation type, as shown in this table. The modulation order specifies the number of points
in the signal constellation.

| Modulation Type | Number of Bits Per Symbol (NBPS) | Modulation Order |
| --- | --- | --- |
| BPSK | 1 | 2 |
| QPSK | 2 | 4 |
| 8-PSK | 3 | 8 |
| 16-PSK | 4 | 16 |
| 16-QAM | 4 | 16 |
| 32-PSK | 5 | 32 |
| 64-QAM | 6 | 64 |
| 256-QAM | 8 | 256 |
| 1024-QAM | 10 | 1024 |
| 4096-QAM | 12 | 4096 |

The block supports both scalar and vector inputs when you set the **Modulation
source** parameter to `Property`. It supports only scalar
input when you set the **Modulation source** parameter to `Input
port`. You can use this block to develop transmitters in a digital
communication system. The block provides an architecture suitable for HDL code generation and
hardware deployment.
