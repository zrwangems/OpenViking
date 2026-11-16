---
type: simulink-block
title: 'Convolutional Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Interleaving / Convolutional'
documentation_page: 'convolutionalinterleaver'
documentation_source_path: 'ref/convolutionalinterleaver.html'
language: en
---

# Convolutional Interleaver

## Ports

Not documented in R2025b.

## Parameters

**Rows of shift registers**
:   The number of shift registers that the block uses internally.

**Register length step**
:   The number of additional symbols that fit in each successive shift
    register, where the first register holds zero symbols.

**Initial conditions**
:   The values that fill each shift register when the simulation
    begins.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

You can generate HDL code for the Convolutional Interleaver
block using a shift-register-based implementation, or a RAM-based
implementation.

The default implementation for the Convolutional Interleaver
block is shift register-based. To suppress generation of reset logic, set the
implementation parameter `ResetType`
to`'none'`. When you set
`ResetType`
to`'none'`, reset is not
applied to the shift registers.

When registers are not fully loaded, mismatches between Simulink® and the generated code occur for some number of samples during the
initial phase. To avoid spurious test bench errors, determine the number of
samples required to fill the shift registers. Set the **Ignore output
data checking (number of samples)** option accordingly. (If you are
using the command-line interface, you can use the
`IgnoreDataChecking` property for this purpose.)

When you select the `RAM` implementation for a
Convolutional Interleaver block, HDL Coder uses RAM resources instead of shift registers.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

**Restrictions**

When you select the `RAM` implementation:

- Double or single data types are not supported for either input or
  output signals.
- You must set **Initial conditions** for the block to
  zero.
- At least two rows of interleaving are required.

## Version History

**Introduced before R2006a**

## Description

Permute input symbols using set of shift registers

The Convolutional Interleaver block permutes the symbols in the input signal.
Internally, it uses a set of shift registers. For information about delays, see Delays of Convolutional Interleaving and Deinterleaving.

The **Initial conditions** parameter indicates the values that fill
each shift register at the beginning of the simulation (except for the first shift
register, which has zero delay). If **Initial conditions** is a scalar,
then its value fills all shift registers except the first; if **Initial
conditions** is a column vector whose length is the **Rows of shift
registers** parameter, then each entry fills the corresponding shift
register. The value of the first element of the **Initial conditions**
parameter is unimportant, since the first shift register has zero delay.

This block accepts a scalar or column vector input signal, which can be real or
complex. The output signal has the same sample time as the input signal.

The block can accept the data types `int8`, `uint8`,
`int16`, `uint16`, `int32`,
`uint32`, `boolean`, `single`,
`double`, and fixed-point. The data type of this output will be the
same as that of the input signal.
