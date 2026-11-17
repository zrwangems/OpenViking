---
type: simulink-block
title: 'M-PSK Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'mpskmodulatorbaseband'
documentation_source_path: 'ref/mpskmodulatorbaseband.html'
language: en
---

# M-PSK Modulator Baseband

## Ports
```yaml
ports:
- name: In_1
  summary: Input signal scalar | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out_1
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double | fixed point
```

### Input

### **In\_1** — Input signal scalar | vector

Specify the input signal as an integer scalar, integer vector, or
binary vector.

- When **Input type** is
  `Integer`, specify the input signal
  elements as integers from 0 to *M* – 1.
- When **Input type** is
  `Bit`, specify the input signal as
  a binary vector in which the number of elements is an integer
  multiple of the bits per symbol. The bits per symbol is equal to log2(*M*).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out\_1** — Output signal scalar | vector

Output signal, returned as a complex scalar or vector. The output is
the complex baseband representation of the PSK-modulated signal.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: M-ary number
  summary: Modulation order of the PSK constellation 8 (default) | scalar
  group: Main
- name: Input type
  summary: Type of input signal Integer (default) | Bit
  group: Main
- name: Constellation ordering
  summary: Symbol mapping Gray (default) | Binary | User-defined
  group: Main
- name: Constellation mapping
  summary: User-defined symbol mapping [0:7] (default) | vector
  group: Main
- name: Phase offset (rad)
  summary: Phase offset in radians pi/8 (default) | scalar
  group: Main
- name: View constellation
  summary: Option to plot reference constellation button
  group: Main
- name: Output data type
  summary: Output data type double (default) | single | Inherit via back propagation | fixdt(1,16) | fixdt(1,16,0) | <data
    type expression>
  group: Data Types
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **M-ary number** — Modulation order of the PSK constellation `8` (default) | scalar

Specify the modulation order as a positive integer power of
two.

**Example:** `2` | `16`

### **Input type** — Type of input signal `Integer` (default) | `Bit`

Specify the elements of the input signal as integers or bits. If
**Input type** is `Bit`,
the number of samples per frame must be an integer multiple of the
number of bits per symbol. The number of bits per symbol is log2(*M*).

### **Constellation ordering** — Symbol mapping `Gray` (default) | `Binary` | `User-defined`

Symbol mapping of integer or groups of log2(*M*) bit inputs, specified as
`Gray`, `Binary`,
or `User-defined`.

- When you set **Constellation ordering** to
  `Gray`, the input signal is mapped
  to the output symbols using a Gray-encoded signal
  constellation.
- When you set **Constellation ordering** to
  `Binary`, the modulated symbol is exp(*jϕ*+*j2πm/M*), where *ϕ* is the phase
  offset in radians, *m* is the integer input
  such that 0 ≤ *m* ≤ M – 1, and *M* is the modulation
  order.
- When you set **Constellation ordering** to
  `User-defined`, specify a vector of
  size *M*, which has unique integer values in
  the range [0, *M*–1]. The first element of this
  vector corresponds to the constellation point having an value of e*jϕ* with subsequent elements running
  counterclockwise.

**Example:** `[0 3 2 1]`

### **Constellation mapping** — User-defined symbol mapping `[0:7]` (default) | vector

User-defined symbol mapping, specified as an
*M*-element vector having unique integer values in the
range [0, *M* – 1]. Use this parameter to specify a
custom order for mapping the input integers to output integers.

The first element of this vector corresponds to the constellation
point at (0 + ϕ) angle, with subsequent elements running
counterclockwise. The last element corresponds to the
(-2π/*M* + ϕ) constellation point. ϕ is the value
of phase offset (**Phase offset
(rad)**) and *M* is the modulation order
(**M-ary
number**).

#### Dependencies

This parameter applies when you set **Constellation ordering** to
`User-defined`.

### **Phase offset (rad)** — Phase offset in radians `pi/8` (default) | scalar

Specify, in radians, the phase offset of the initial constellation as
a real scalar.

**Example:** `pi/4`

### **View constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `Inherit via back propagation` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

Specify the data type of the modulated output signal. Set this
parameter to one of the fixed point options or `<data
type expression>` to enable parameters in which you
specify additional details. Set this parameter to `Inherit
via back propagation`, to match the output data type
and scaling to the following block in the model.

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

**Introduced before R2006a**

## Description

Modulate using M-ary phase shift keying

The M-PSK Modulator Baseband block modulates an input signal using
M-ary phase shift keying (PSK) and returns a complex baseband output. The modulation
order, *M*, which is equivalent to the number of points in the signal
constellation, is determined by the **M-ary number** parameter. The
block accepts scalar or column vector input signals.
