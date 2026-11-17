---
type: simulink-block
title: 'BPSK Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'bpskmodulatorbaseband'
documentation_source_path: 'ref/bpskmodulatorbaseband.html'
language: en
---

# BPSK Modulator Baseband

## Ports

### Input

### **In** — Input data scalar | vector

Input signal, specified as a scalar or vector with element values in
the range [0,1].

This port in unnamed on the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — BPSK-modulated baseband signal scalar | vector

BPSK-modulated baseband signal, returned as a complex-valued scalar or
vector.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Phase offset (rad)** — Phase offset of zeroth point `0` (default) | scalar

Phase offset of the zeroth point of the constellation in radians,
specified as a scalar.

**Example:** `pi/4`

### **View constellation** — Option to plot reference constellation button

Click **View
Constellation** on the block mask to visualize a signal constellation for the
specified block parameters. Before viewing a constellation, apply the parameter settings. For
more information, see View Constellation of Modulator Block.

### Data Types

### **Output data type** — Output data type `double` (default) | `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit via back propagation` | `<data type expression>`

The output data type, specified as `double`,
`single`,
`fixdt(1,16)`,
`fixdt(1,16,0)`, `Inherit via
back propagation`, or `<data type
expression>`.

Setting this parameter to

- `fixdt(1,16)`,
  `fixdt(1,16,0)`, or
  `<data type expression>` enables
  parameters in which you can further specify details.
- `Inherit via back propagation` sets
  the output data type and scaling to match the following
  block.

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
| a ufix(ceil(log2(M))) only at the input for M-ary modulation.  b Fixed-point outputs must be signed. | |

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

Modulate using BPSK method

The BPSK Modulator Baseband block modulates a signal by using the binary phase shift keying (BPSK)
method. The output is a baseband representation of the modulated signal. The input
signal must be a discrete-time binary-valued signal. If the input bit is 0 or 1, then
the modulated symbol is exp(jϕ) or -exp(jϕ), respectively. The `Phase offset
(rad)` parameter specifies the value of ϕ in radians.
