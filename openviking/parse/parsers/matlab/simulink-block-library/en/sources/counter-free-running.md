---
type: simulink-block
title: 'Counter Free-Running'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterfreerunning'
language: en
---

# Counter Free-Running

## Ports

### Output

### **Port\_1** — Count value scalar

Count value, returned as an unsigned integer with a length specified
by the **Number of Bits** parameter. When the number
of bits is anything other than 8, 16, 32, or 64, the output type is an
unsigned fixed-point data type.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Number of Bits** — Number of bits `16` (default) | scalar

Specify the number of bits as a finite, real-valued. When you
specify:

- A positive integer, for example `8`, the block
  counts up to `28 – 1`,
  which is `255`.
- An unsigned integer expression, for example
  `uint8(8)`, the block counts up to
  `uint8(2uint8(8) –
  1)`, which is `254`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBits` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'16'` |

### **Sample time** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples as a scalar (`sampling
period`), or a two-element vector (`[sampling period,
initial offset]`). To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tsamp` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

## Libraries

Simulink / Sources HDL Coder / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Count up and overflow back to zero after reaching maximum value for specified number of bits

The Counter Free-Running block counts up until reaching the maximum value,
2*Nbits* – 1, where
*Nbits* is the number of bits. Then the counter overflows to zero
and begins counting up again.

After overflow, the counter always initializes to zero. However, if you select the global
doubles override, the Counter Free-Running block does not wrap back to
zero.

**Note**

This block does not report wrap on overflow warnings during simulation. To report
these warnings, see the `Simulink.restoreDiagnostic`
reference page. The block does report errors due to wrap on overflow.
