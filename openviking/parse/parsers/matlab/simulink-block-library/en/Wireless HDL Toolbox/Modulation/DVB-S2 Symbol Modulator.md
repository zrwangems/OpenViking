---
type: simulink-block
title: 'DVB-S2 Symbol Modulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'dvbs2symbolmodulator'
documentation_source_path: 'ref/dvbs2symbolmodulator.html'
language: en
---

# DVB-S2 Symbol Modulator

## Ports
```yaml
ports:
- name: data
  summary: Data bits Boolean scalar | real scalar
  direction: input
  data_types: Boolean | fixdt(0,1,0)
- name: valid
  summary: Indication of whether input data is valid 0 | 1
  direction: input
  data_types: Boolean
- name: modIdx
  summary: Modulation index 0 | 1 | 2 | 3 | 4
  direction: input
  data_types: single | double | fixdt(0,3,0)
- name: codeRateIdx
  summary: Code rate index 5 | 6 | 7 | 8 | 9 | 10
  direction: input
  data_types: single | double | fixdt(0,4,0)
- name: load
  summary: Modulation and code rate control 0 | 1
  direction: input
  data_types: Boolean
- name: data
  summary: Modulated constellation data symbols complex scalar
  direction: output
  data_types: single | double | fixdt(1,wordlength,wordlength-2)
- name: valid
  summary: Valid output data indication 0 | 1
  direction: output
  data_types: Boolean
```

### Input

### **data** — Data bits Boolean scalar | real scalar

Input data bits, specified as a Boolean or real scalar. The block accepts
`Boolean` or `ufix1` data bits.

**Data Types:** `Boolean` | `fixdt(0,1,0)`

### **valid** — Indication of whether input data is valid `0` | `1`

Control signal that indicates whether the input data is valid. When this value is
`1`, the block accepts the values on the **data**
input port. When this value is `0`, the block ignores the values on
the **data** input port.

**Data Types:** `Boolean`

### **modIdx** — Modulation index `0` | `1` | `2` | `3` | `4`

Modulation index, specified as `0`, `1`,
`2`, `3`, or `4`. Each value
represents a specific modulation type, as table shows.

| Modulation Index | Modulation Type |
| --- | --- |
| `0` | QPSK |
| `1` | 8-PSK |
| `2` | 16-APSK |
| `3` | 32-APSK |
| `4` | π/2-BPSK |

For HDL code generation, specify this value in `fixdt(0,3,0)`
format.

If you specify a value other than one listed in this table, the block displays a
warning message and:

- Applies QPSK modulation when **load** is
  `1`.
- Continues with the current modulation when **load** is
  `0`.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `fixdt(0,3,0)`

### **codeRateIdx** — Code rate index `5` | `6` | `7` | `8` | `9` | `10`

Code rate index, specified as `5`, `6`,
`7`, `8`, `9`, or
`10`. Each value represents a specific code rate, as this table
shows.

| Code Rate Index | Code Rate |
| --- | --- |
| `5` | 2/3 |
| `6` | 3/4 |
| `7` | 4/5 |
| `8` | 5/6 |
| `9` | 8/9 |
| `10` | 9/10 |

If you specify a value other than `5`, `6`,
`7`, `8`, `9`, or
`10` for 16-APSK and other than `6`,
`7`, `8`, `9`, or
`10` for 32-APSK, the block displays a warning message and applies
the code rate 3/4. For HDL code generation, specify this value in
`fixdt(0,4,0)` format.

The code rates in this table apply to the **modIdx** input port
values `2` and `3`, which indicate 16-APSK and
32-APSK modulation, respectively. When you set the **modIdx** port
value to `0`, `1`, or `4`, the
block ignores the **codeRateIdx** input port values.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `single` | `double` | `fixdt(0,4,0)`

### **load** — Modulation and code rate control `0` | `1`

Modulation and code rate control, specified as a Boolean scalar.

When this value is `1`, the block samples the
**modIdx** and **codeRateIdx** values. When this
value is `0`, the block ignores any changes in the
**modIdx** and **codeRateIdx** and continues with
the current modulation index and code rate until **load** changes to
`1`.

If the **load** value changes to `1` during
block operation, the block resynchronizes and restarts modulation using the current
value of **modIdx**. This restart occurs regardless of whether the
**modIdx** value changes.

If you do not specify the **load** value as `1`
at the start of block operation, by default, the block operates with QPSK
modulation.

#### Dependencies

To enable this port, set the **Modulation source** parameter to
`Input port`.

**Data Types:** `Boolean`
### Output

### **data** — Modulated constellation data symbols complex scalar

Modulated constellation data symbols, returned as a complex scalar.

The block supports `double` and
`single` data types for simulation, but not for HDL code
generation.

For HDL code generation, set the **Output data type** parameter
to `Custom` and specify the word length.

**Data Types:** `single` | `double` | `fixdt(1,wordlength,wordlength-2)`
**Complex Number Support:** Yes

### **valid** — Valid output data indication `0` | `1`

Control signal that indicates whether the data from the **data**
output port is valid. When this value is `1`, the block returns valid
data on the **data** output port. When this value is
`0`, the values on the **data** output port are
not valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Modulation source
  summary: Source for modulation type Property (default) | Input port
  group: Main
- name: Modulation
  summary: Modulation type QPSK (default) | 8-PSK | 16-APSK | 32-APSK | pi/2-BPSK
  group: Main
- name: Code rate
  summary: Code rate 3/4 (default) | 2/3 | 4/5 | 5/6 | 8/9 | 9/10
  group: Main
- name: Unit average power
  summary: Spectral growth reduction off (default) | on
  group: Main
- name: Output data type
  summary: Output data type Custom (default) | double | single
  group: Data Types
- name: Word length
  summary: Word length 16 (default) | integer in the range [3, 32]
  group: Data Types
```

### Main

### **Modulation source** — Source for modulation type `Property` (default) | `Input port`

To specify the modulation type using the **Modulation**
parameter, select `Property`. To specify the modulation using
the **modIdx** port during run time, select `Input
port`.

### **Modulation** — Modulation type `QPSK` (default) | `8-PSK` | `16-APSK` | `32-APSK` | `pi/2-BPSK`

Select the modulation type.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Property`.

### **Code rate** — Code rate `3/4` (default) | `2/3` | `4/5` | `5/6` | `8/9` | `9/10`

Select the code rate.

#### Dependencies

To enable this parameter set the **Modulation source**
parameter to `Property` and the
**Modulation** parameter to `16-APSK` or
`32-APSK`.

### **Unit average power** — Spectral growth reduction `off` (default) | `on`

Select this parameter to perform symbol modulation with a normalized
constellation. Clear this parameter to perform symbol modulation using the
constellation defined in the standard [1].

When you specify `0`, `1`, or
`4` in the **modIdx** input port or set the
**Modulation** parameter to `QPSK`,
`8-PSK`, or `pi/2-BPSK`, the block
ignores this parameter during its operation.

#### Dependencies

To enable this parameter, set the **Modulation source**
parameter to `Input port` or set the **Modulation
source** to `Property` and the
**Modulation** parameter to `16-APSK` or
`32-APSK`.

### Data Types

### **Output data type** — Output data type `Custom` (default) | `double` | `single`

Specify the data type for the output data.

The block supports `double` and
`single` data types for simulation.

For simulation and HDL code generation, set this value to
`Custom`.

### **Word length** — Word length `16` (default) | integer in the range [3, 32]

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

**Introduced in R2022b**

### R2023b: Change in output data type default settings

The default value for **Output data type** parameter is now changed to
`Custom`. To see this change, double-click the block and then click
**Data Types** tab.

## Description

Modulate data bits to complex constellation symbols according to DVB-S2 standard

The DVB-S2 Symbol Modulator block modulates data bits to complex data
symbols based on the modulation types supported by the Digital Video Broadcast Satellite
Second Generation (DVB-S2) standard [1]. The block accepts data bits
and a `valid` signal and outputs modulated complex constellation symbols and
a `valid` signal.

Each complex output symbol comprises a standard number of data bits based on the
modulation type, as this table shows. If you provide input data bits with a nonmultiple of the
number of data bits per symbol, the block ignores the output symbol with insufficient or
excess bits.

| Modulation Type | Number of Data Bits Per Symbol |
| --- | --- |
| π/2-BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-APSK | 4 |
| 32-APSK | 5 |

The block provides an architecture suitable for HDL code generation and hardware
deployment. You can use this block in the development of a DVB-S2 transmitter.
