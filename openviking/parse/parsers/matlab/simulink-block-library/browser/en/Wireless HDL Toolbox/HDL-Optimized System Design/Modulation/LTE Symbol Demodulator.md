---
type: simulink-block
title: 'LTE Symbol Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Modulation'
documentation_page: 'ltesymboldemodulator'
documentation_source_path: 'ref/ltesymboldemodulator.html'
language: en
---

# LTE Symbol Demodulator

## Ports

### Input

### **data** — Input data symbols complex scalar

Input data symbols, specified as a complex scalar. The block performs demodulation
assuming the input constellation power normalization is in accordance with LTE
standard TS 36.211, Section 7.1 [1]. The normalization
values are based on the modulation type.

- 1/√2 for BPSK and QPSK
- 1/√10 for 16-QAM
- 1/√42 for 64-QAM
- 1/√170 for 256-QAM

**Example:** For BPSK modulation, the input values can be `[0.707 +0.707i;
-0.707 -0.707i]`

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

For HDL code generation, the input data type must be `signed fixed
point` and the maximum input word length the block supports is 32
bits.

**Data Types:** `single` | `double` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Valid input data indication scalar

Control signal that indicates if the input data is valid. When this value is
`1` (true), the block accepts the values on the
**data** input port. When this value is `0`
(false), the block ignores the values on the **data** input
port.

**Data Types:** `Boolean`

### **modSel** — Modulation selection integer from 0 to 4

Select the modulation type by specifying its corresponding value shown in this
table. Valid **modSel** values are from 0 to 4. Each value represents
a specific modulation type, as shown in this table.

| Value | Modulation Type |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |

If you specify a value other than one listed in this table, the block displays a
warning message and applies QPSK modulation.

For HDL code generation, specify this value in `fixdt(0,3,0)`
format. `double` and `single` data types are
supported for simulation but not for HDL code generation.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `signed fixed point`
### Output

### **data** — Output demodulated data bits or LLR values scalar

Output demodulated data bits or LLR values, returned as a scalar.

- When you set the **Decision type** parameter to
  `Soft`, the block outputs demodulated LLR values. A
  positive LLR output value is considered as 1 and a negative LLR output value is
  considered as 0. The magnitude of the output gives a piecewise linear
  approximation to the LLR of the demodulated bits. The algorithm used for the LLR
  approximation is described in [1]. The returned
  LLR values for the input signal located on these constellation points lie within
  these magnitudes.

  - 1 for BPSK
  - 1/√2 for QPSK
  - [1 3]/√10 for 16-QAM
  - [1 3 5 7]/√42 for 64-QAM
  - [1 3 5 7 9 11 13 15]/√170 for 256-QAM

  The output word length increases by 2 bits for inputs with data type
  `signed fixed point`. For input with data types
  `double` or `single`, the output data type is
  the same as the input data type.

- When you set the **Decision type** parameter to
  `Hard`, the block results in the output containing the
  bit sequences corresponding to the closest constellation points to the input. The
  data type of this output is `Boolean`.

**Data Types:** `single` | `double` | `signed fixed point` | `Boolean`

### **valid** — Valid output data indication scalar

Control signal that indicates if data from the **data** output
port is valid. When this value is `1` (true), the block returns valid
data on the **data** output port. When this value is
`0` (false), the values on the **data** output
port are not valid.

**Data Types:** `Boolean`

### **ready** — Block ready indicator scalar

Control signal that indicates when the block is ready to accept new input data.
When this value is `1` (true), the block accepts input data in the
next time step. When this value is `0` (false), the block ignores the
input data in the next time step.

The **ready** signal remains `0` (false) until
the block outputs data of the corresponding input data symbol. The number of clock
cycles the **ready**  signal remains `0` (false)
depends on the selected modulation type. If the selected modulation type is 16-QAM,
the **ready**  signal remains `0` (false) for 3
clock cycles, calculated as *NBPS* – 1 and then it changes to
`1` (true) indicating that the block is ready to accept data in the
next time step.

**Data Types:** `Boolean`

## Parameters

### **Modulation source** — Source for modulation type `Property` (default) | `Input port`

To specify the modulation type by using the **Modulation**
parameter, select `Property`. To specify the modulation type
from the **modSel** port during run time, select `Input
port`.

### **Modulation** — Modulation type `BPSK` (default) | `QPSK` | `16-QAM` | `64-QAM` | `256-QAM`

Select the modulation type.

#### Dependencies

To enable this parameter, set the **Modulation source** parameter
to `Property`.

### **Decision type** — Type of demapping `Soft` (default) | `Hard`

Select the demapping type.

- `Soft` — Demap data symbols to LLR values. This
  LLR value for each bit indicates how likely the bit is `1` or
  `0`.
- `Hard` — Demap data symbols to bits
  `1` or `0`.

### **Rounding Method** — Rounding mode for internal fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

This parameter specifies the type of rounding mode for internal fixed-point
calculations. For more information about rounding modes, see Rounding Modes. This parameter does not apply when the
input is of data type `double` or `single`.

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

This block does not have any HDL Block
Properties.

## Version History

**Introduced in R2019b**

## Description

Demodulate complex LTE data symbols to data bits or LLR values

The LTE Symbol Demodulator block demodulates complex data symbols to data
bits or log likelihood ratios (LLR) values based on the modulation types supported by LTE
standard TS 36.211 [1]. The block provides an
architecture suitable for HDL code generation and hardware deployment. You can use this block
in the development of an LTE receiver.

The block accepts data symbols, along with a valid signal, and outputs demodulated bits or
LLR values with valid and ready signals. The number of demodulated bits or LLR values for a
given symbol depends on the modulation type, as shown in this table.

| Modulation Type | Number of Bits per Symbol (NBPS) |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |

The **ready** output port indicates when the block can accept an input
data sample. You can use **ready** output port to control the upstream data
coming to the block.
