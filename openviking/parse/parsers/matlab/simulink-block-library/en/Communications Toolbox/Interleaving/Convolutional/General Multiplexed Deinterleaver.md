---
type: simulink-block
title: 'General Multiplexed Deinterleaver'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Interleaving'
documentation_page: 'generalmultiplexeddeinterleaver'
documentation_source_path: '../comm/ref/generalmultiplexeddeinterleaver.html'
language: en
---

# General Multiplexed Deinterleaver

## Ports

Not documented in R2025b.

## Parameters

**Interleaver delay (samples)**
:   A vector that lists the number of symbols that fit in each shift register
    of the corresponding interleaver. The length of this vector is the number of
    shift registers.

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

The implementation for the General Multiplexed Deinterleaver
block is shift register based. If you want to suppress generation of reset
logic, set the implementation parameter `ResetType`
to`none`.

When you set `ResetType` to
`none`, reset is not applied
to the shift registers. When registers are not fully loaded, mismatches between
Simulink® and the generated code occur for some number of samples during the
initial phase. To avoid spurious test bench errors, determine the number of
samples required to fill the shift registers. Set the **Ignore output
data checking (number of samples)** option accordingly. (If you are
using the command-line interface, you can use the
`IgnoreDataChecking` property for this purpose.)

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |

## Version History

**Introduced before R2006a**

## Description

Restore ordering of symbols using specified-delay shift registers

The General Multiplexed Deinterleaver block restores the original ordering of a
sequence that was interleaved using the General Multiplexed Interleaver block.

In typical usage, the parameters in the two blocks have the same values. As a result,
the **Interleaver delay** parameter, *V*, specifies
the delays for each shift register in the corresponding
*interleaver*, so that the delays of the deinterleaver's shift
registers are actually
`max(V)-V`.

This block accepts a scalar or column vector input signal, which can be real or
complex. The output signal has the same sample time as the input signal.

The block can accept the data types `int8`, `uint8`,
`int16`, `uint16`, `int32`,
`uint32`, `boolean`, `single`,
`double`, and fixed-point. The data type of the output will be the
same as that of the input signal.
