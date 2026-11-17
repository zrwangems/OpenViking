---
type: simulink-block
title: 'NR Symbol Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'nrsymbolmodulator'
documentation_source_path: 'ref/nrsymbolmodulator.html'
language: en
---

# NR Symbol Modulator

## Ports
```yaml
ports:
- name: data
  summary: Input data bits scalar
  direction: input
  data_types: Boolean | fixdt(0,1,0)
- name: valid
  summary: Indicate valid input data scalar
  direction: input
  data_types: Boolean
- name: modSel
  summary: Modulation selection integer
  direction: input
  data_types: fixdt(0,3,0) | double | single
- name: load
  summary: Modulation control scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Modulated complex data symbols scalar
  direction: output
  data_types: single | double | fixdt(1,wordlength,wordlength-2)
- name: valid
  summary: Valid output data indication scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data bits scalar

Input data bits, specified as a scalar. The block accepts
`Boolean` or `ufix1` data bits.

**Data Types:** `Boolean` | `fixdt(0,1,0)`

### **valid** — Indicate valid input data scalar

Control signal that indicates if the input data is valid. When this value is
`1` (true), the block accepts the values on the
**data** input port. When this value is `0`
(false), the block ignores the values on the **data** input
port.

**Data Types:** `Boolean`

### **modSel** — Modulation selection integer

Select the modulation type by specifying its corresponding value shown in this
table.

The **modSel** values are from 0 to 5. Each value represents a
specific modulation type.

| Value | Modulation Type |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 16-QAM |
| `3` | 64-QAM |
| `4` | 256-QAM |
| `5` | pi/2-BPSK |

If you specify a value other than one listed in this table, the block displays a
warning message and:

- Applies QPSK modulation when **load** is
  `1` (true).
- Continues with the current modulation when **load** is
  `0` (false).

For HDL code generation, specify this value in `fixdt(0,3,0)`
format.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `fixdt(0,3,0)` | `double` | `single`

### **load** — Modulation control scalar

Control signal to sample modulation.

When this value is `1` (true), the block applies the modulation
based on the **modSel** value. When this value is
`0` (false), the block ignores any changes in the **modSel** value and continues with the current modulation until
**load** changes to `1` (true).

If the **load** value changes to `1` (true)
during the block operation, the block resynchronizes and restarts modulation using the
current value of **modSel**. This restart occurs whether
or not the **modSel** value has changed. For example, if
the block is operating in 256-QAM mode and the **load** value changes
to `1` (true) after four of the eight required input bits are sent
into the block, the block discards those first four bits and restarts its operation
from the fifth bit.

If you do not apply the **load** value as `1`
(true) at the start of block operation, by default, the block operates with QPSK
modulation.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `Boolean`
### Output

### **data** — Modulated complex data symbols scalar

Modulated complex data symbols, returned as a scalar.

**Data Types:** `single` | `double` | `fixdt(1,wordlength,wordlength-2)`
**Complex Number Support:** Yes

### **valid** — Valid output data indication scalar

Control signal that indicates if data from the **data** output
port is valid. When this value is `1` (true), the block returns valid
data on the **data** output port. When this value is
`0` (false), the block ignores values on the
**data** output port.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Modulation source
  summary: Source for modulation type Property (default) | Input port
  group: Main
- name: Modulation
  summary: Modulation type BPSK (default) | QPSK | 16-QAM | 64-QAM | 256-QAM | pi/2-BPSK
  group: Main
- name: Output data type
  summary: Output data type selection Custom (default) | double | single
  group: Data Types
- name: Word length
  summary: Output word length 16 (default) | integer in the range [3, 32]
  group: Data Types
```

### Main

### **Modulation source** — Source for modulation type `Property` (default) | `Input port`

To specify the modulation type by using the **Modulation**
parameter, select `Property`. To specify the modulation type
from the **modSel** port during run time, select `Input
port`.

### **Modulation** — Modulation type `BPSK` (default) | `QPSK` | `16-QAM` | `64-QAM` | `256-QAM` | `pi/2-BPSK`

Select the modulation type.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property`.

### Data Types

### **Output data type** — Output data type selection `Custom` (default) | `double` | `single`

Specify the data type for the output data.

`double` and `single` data types
are supported for simulation.

For simulation and HDL code generation, set this value to
`Custom`.

### **Word length** — Output word length `16` (default) | integer in the range [3, 32]

Specify the output word length. This value must be an integer in the range [3,
32].

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

This block does not have any HDL Block
Properties.

## Version History

**Introduced in R2019a**

### R2023b: Change in output data type default settings

The default value for **Output data type** parameter is now changed to
`Custom`. To see this change, double-click the block and then click
**Data Types** tab.

## Description

Modulate data bits to complex NR data symbols

The NR Symbol Modulator block maps a group of data bits to complex data
symbols by using the modulation types supported by NR standard TS 38.211 [1]. The block provides an
architecture suitable for HDL code generation and hardware deployment.

The block accepts 1-bit of data at a time, along with control signals, and outputs a
modulated complex symbol with a valid signal. Each complex symbol comprises a standard number
of bits based on the modulation type, as shown in this following table. If you provide a
nonmultiple of modulation-order bits as an input, the block ignores the output symbol with
insufficient or excessive bits. The modulation order is the number of bits per symbol.

| Modulation Type | Modulation Order - Number of Bits per Symbol |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |
| pi/2-BPSK | 1 |
