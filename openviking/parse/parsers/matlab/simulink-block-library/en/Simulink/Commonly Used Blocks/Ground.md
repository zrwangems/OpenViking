---
type: simulink-block
title: 'Ground'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'ground'
documentation_source_path: '../simulink/slref/ground.html'
language: en
---

# Ground

## Ports

### Output

### **Port\_1** — Ground signal scalar

The Ground block outputs a scalar signal with zero value, and the same
data type as the port to which it connects.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Commonly Used Blocks Simulink / Sources HDL Coder / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

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
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Ground unconnected input port

The Ground block connects to blocks whose input ports do not connect to other
blocks. If you run a simulation with blocks that have unconnected input ports, the
software issues warnings. Using a Ground block to ground those
unconnected blocks can prevent these warnings.

### Working with Fixed-Point Data Types

When working with fixed-point data types, there may be instances where the fixed-point data
type cannot represent zero exactly. In these cases, the Ground block
outputs a nonzero value that is the closest possible value to zero. This behavior
applies only to fixed-point data types with nonzero bias. These expressions are
examples of fixed-point data types that cannot represent zero:

- `fixdt(0, 8, 1, 1)` — an unsigned 8-bit type with
  slope of 1 and bias of 1
- `fixdt(1, 8, 6, 3)` — a signed 8-bit type with
  slope of 6 and bias of 3

### Working with Enumerated Data Types

When working with enumerated data types, the Ground block outputs the
default value of the enumeration. This behavior applies whether:

- The enumeration can represent zero
- The default value of the enumeration is zero

If the enumerated type does not have a default value, the Ground block
outputs the first enumeration value in the type definition.
