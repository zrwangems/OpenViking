---
type: simulink-block
title: 'QPSK Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'qpskmodulatorbaseband'
documentation_source_path: '../comm/ref/qpskmodulatorbaseband.html'
language: en
---

# QPSK Modulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | column vector
  direction: input
  data_types: double | single | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Out
  summary: QPSK-modulated baseband signal scalar | vector
  direction: output
  data_types: double | single | fixed point
```

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or column vector.

- When you set **Input
  type** to `Integer`, specify the input
  signal elements as integers in the range [0, 3].
- When you set **Input type** to
  `Bit`, specify the input signal as a binary vector
  containing an even number of elements to ensure a whole number of the 2-bit QPSK
  modulation symbols.

This port in unnamed on the block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **Out** — QPSK-modulated baseband signal scalar | vector

QPSK-modulated baseband signal, returned as a complex-valued scalar or vector. The
output is the complex baseband representation of the QPSK-modulated signal.

This port in unnamed on the block.

**Data Types:** `double` | `single` | `fixed point`
## Parameters
```yaml
parameters:
- name: Input type
  summary: Integer or bit pair input indicator Integer (default) | Bit
  group: Main
- name: Constellation ordering
  summary: Symbol mapping Gray (default) | Binary
  group: Main
- name: Phase offset (rad)
  summary: Phase offset of zeroth point pi/4 (default) | scalar
  group: Main
- name: View constellation
  summary: Option to plot reference constellation button
  group: Main
- name: Output data type
  summary: Output data type double (default) | single | fixdt(1,16) | fixdt(1,16,0) | Inherit via back propagation | <data
    type expression>
  group: Data Types
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Input type** — Integer or bit pair input indicator `Integer` (default) | `Bit`

Integer or bit pair input indicator, specified as
`Integer` or `Bit`.

### **Constellation ordering** — Symbol mapping `Gray` (default) | `Binary`

Symbol mapping of integer or bit pair inputs, specified as
`Gray` or `Binary`.

- To map symbols using Gray-coded ordering, set this parameter to
  `Gray`.
- To map symbols using binary-coded ordering, set this parameter to
  `Binary`.

For more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Phase offset (rad)** — Phase offset of zeroth point `pi/4` (default) | scalar

Phase of the zeroth point of the signal constellation in radians, specified as a
scalar.

### **View constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit via back propagation` | `<data type expression>`

Output data type, specified as `double`,
`single`, `fixdt(1,16)`,
`fixdt(1,16,0)`, `Inherit via back
propagation`, or `<data type
expression>`.

- `fixdt(1,16)`,
  `fixdt(1,16,0)`, or `<data type
  expression>` enables parameters in which you can further specify
  details.
- `Inherit via back propagation` sets the output data
  type and scaling to match the following block.

For information about specifying data types, see Data Type Assistant.
## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a ufix(1) at the input if ''input type'' is set to ''bit''. ufix(ceil(log2(M))) at input if ''input type'' is set to ''integer'' for M-ary modulation.  b Fixed-point outputs must be signed. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

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

## Version History

**Introduced before R2006a**

## Description

Modulate using quadrature phase shift keying method

The QPSK Modulator Baseband block modulates signals using the quadrature phase shift
keying (QPSK) method. The output is a baseband representation of the modulated signal. This
block accepts a scalar or column vector input signal. For information about the data types,
see Supported Data Types.
