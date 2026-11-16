---
type: simulink-block
title: 'Rectangular QAM Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / AM'
documentation_page: 'rectangularqammodulatorbaseband'
documentation_source_path: '../comm/ref/rectangularqammodulatorbaseband.html'
language: en
---

# Rectangular QAM Modulator Baseband

## Ports

### Input

### **In** — Input data scalar | column vector

Input data, specified as a scalar or column vector. The input data must be binary values
or integers in the range [0, (*M* – 1)], where *M* is the modulation order as
specified by **M-ary
number**. Use **Input
type** to specify the input data as
`Integer` or
`Bit`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — Output data scalar | column vector

Rectangular QAM-modulated baseband signal, returned as a scalar or vector. Use the
**Output
data type** parameter to specify the output data
type.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **M-ary number** — Modulation order `16` (default) | positive integer

Modulation order, specified as a positive integer power of two. The
modulation order specifies the number of points in the signal
constellation. For more information, see Constellation Size and Scaling.

### **Input type** — Input type `Integer` (default) | `Bit`

Input type, specified as `Integer` or
`Bit` to indicate whether the input
consists of integers or groups of bits.

- To use `Integer`, the input
  signal must consist of integers in the range [0,
  (*M* – 1)]. *M* is
  **M-ary number**.
- To use `Bit`, the input signal
  must contain binary values, and the number of rows must be
  an integer multiple of log2(*M*).

For more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Constellation ordering** — Mapping order of symbols `Gray` (default) | `Binary` | `User-defined`

Mapping order of the symbols, specified as `Gray`,
`Binary`, or
`User-defined`. This parameter determines
how the block maps each symbol to constellation points. Based on setting
of **Input
type**, the block maps input integers or groups of log2(*M*) input bits onto a symbol. For bits, the first bit
represents the MSB and the last bit represents the LSB.
*M* is **M-ary
number**. For more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Constellation mapping** — User-defined constellation mapping `[0:15]` (default) | vector

Constellation mapping that you define, specified as an *M*-element
vector containing unique integer values in the range [0, (*M* – 1)]. *M* is **M-ary
number**.

The first element of this vector corresponds to the top-leftmost point
of the constellation, with subsequent elements running down column-wise,
from left to right. The last element corresponds to the bottom-rightmost
point.

#### Dependencies

This parameter appears when you set **Constellation ordering** to
`User-defined`.

### **Normalization method** — Scaling method for constellation `Min. distance between symbols` (default) | `Average Power` | `Peak Power`

Scaling method for constellation, specified as `Min.
distance between symbols`, `Average
Power`, or `Peak Power`. For
more information, see Constellation Size and Scaling

### **Minimum distance** — Distance between two nearest constellation points `2` (default) | positive scalar

Distance between the two nearest constellation points, specified as a positive
scalar.

#### Dependencies

This parameter appears when you set **Normalization method** to `Min. distance
between symbols`.

### **Average power, referenced to 1 ohm (watts)** — Average power `1` (default) | positive scalar

Average power of the symbols in the constellation in watts, specified
as a positive scalar. Power values assume a nominal impedance of 1
ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Average
Power`.

### **Peak power, referenced to 1 ohm (watts)** — Maximum power `1` (default) | positive scalar

Maximum power of the symbols in the constellation in watts, specified as a positive
scalar. Power values assume a nominal impedance of 1 ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Peak
Power`.

### **Phase offset (rad)** — Rotation of signal constellation `0` (default) | numeric scalar

Rotation of the signal constellation in radians, specified as a
numeric scalar.

### **View constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

Output data type, specified as `double`,
`single`,
`fixdt(1,16)`,
`fixdt(1,16,0)`, `Inherit:
Inherit via back propagation`, or `<data
type expression>`.

- `fixdt(1,16)`,
  `fixdt(1,16,0)`, or
  `<data type expression>`
  enables parameters in which you can further specify
  details.
- `Inherit: Inherit via back
  propagation` sets the output data type and
  scaling to match the following block.

For information about specifying data types, see Data Type Assistant.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox HDL Support / Modulation / AM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b, c` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Square QAM only.  b ufix(1) at the input if ''input type'' is set to ''bit''. ufix(ceil(log2(M))) at input if ''input type'' is set to ''integer'' for M-ary modulation.  c Fixed-point outputs must be signed. | |

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

**Restrictions**

- The block does not support `single` or
  `double` data types for HDL code generation.
- When **Input Type** is set to
  `Bit`, the block does not support HDL code
  generation for input types other than `boolean` or
  `ufix1`.

When the input type is set to `Bit`, but the block
input is actually multibit (`uint16`, for example), the
Rectangular QAM Modulator Baseband block does not support HDL
code generation.

## Version History

**Introduced before R2006a**

## Description

Modulate using rectangular quadrature amplitude modulation

The Rectangular QAM Modulator Baseband block modulates the input signal using M-ary quadrature
amplitude modulation with a constellation on a rectangular lattice. The output is a
baseband representation of the modulated signal.

**Note**

All values of power assume a nominal impedance of 1 ohm.
