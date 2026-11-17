---
type: simulink-block
title: 'Counter Limited'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterlimited'
documentation_source_path: 'slref/counterlimited.html'
language: en
---

# Counter Limited

## Ports

### Output

### **Port\_1** — Count value scalar

Count value, returned as an unsigned integer of 8 bits, 16 bits, 32 bits, 64 bits, or
ufix128. The block uses the smallest number of bits required to
represent the upper limit.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Upper limit** — Upper limit `7` (default) | scalar

Specify the upper limit for the block to count to as a finite, real-valued scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `uplimit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'7'` |

### **Sample time** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples as a scalar (`sampling
period`), or a two-element vector (`sampling period,
initial offset`). To inherit the sample time, set this
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
| **Data Types** | `Boolean` | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- The code generator does not explicitly group primitive blocks that
  constitute a nonatomic masked subsystem block in the generated code. This
  flexibility allows for more efficient code generation. In certain cases, you
  can achieve grouping by configuring the masked subsystem block to execute as
  an atomic unit by selecting the **Treat as atomic
  unit** option.
- Not recommended for production code. Relates to resource limits and
  restrictions on speed and memory often found in embedded systems. Generated
  code can contain dynamic allocation and freeing of memory, recursion,
  additional memory overhead, and widely-varying execution times. While the
  code is functionally valid and generally acceptable in resource-rich
  environments, smaller embedded targets often cannot support such code.
  Usually, blocks evolve toward being suitable for production code. Thus,
  blocks suitable for production code remain suitable.

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

Count up and wrap to zero after specified upper limit

The Counter Limited block counts up until the specified upper limit is reached. Then the counter wraps back to zero, and restarts counting up. The counter always initializes to zero.

**Note**

This block does not report wrap on overflow warnings during simulation. To report
these warnings, see the `Simulink.restoreDiagnostic`
reference page. The block does report errors due to wrap on overflow.
