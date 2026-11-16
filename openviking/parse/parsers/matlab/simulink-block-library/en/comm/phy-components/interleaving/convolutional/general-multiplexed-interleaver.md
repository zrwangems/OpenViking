---
type: simulink-block
title: 'General Multiplexed Interleaver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Interleaving / Convolutional'
documentation_page: 'generalmultiplexedinterleaver'
documentation_source_path: 'ref/generalmultiplexedinterleaver.html'
language: en
---

# General Multiplexed Interleaver

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

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

The implementation for the General Multiplexed Interleaver
block is shift register based. If you want to suppress generation of reset
logic, set the implementation parameter `ResetType`
to`'none'`.

When you set `ResetType`
to`'none'`, reset is not
applied to the shift registers. Mismatches between Simulink® and the generated code occur for some number of samples during the
initial phase, when registers are not fully loaded. To avoid spurious test bench
errors, determine the number of samples required to fill the shift registers.
Then, set the **Ignore output data checking (number of
samples)** option accordingly. (You can use the
`IgnoreDataChecking` property for this purpose, if you
are using the command-line interface.)

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

Permute input symbols using set of shift registers with specified delays
