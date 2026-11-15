---
type: simulink-block
title: 'Bus to Vector'
family: signal-attributes
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'bustovector'
---

# Bus to Vector

Convert virtual bus to vector

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Bus to Vector block converts a virtual bus to a vector. Use the
Bus to Vector block only to replace an implicit bus-to-vector conversion with
an explicit conversion.

Blocks that do not accept buses may implicitly convert buses to vectors. When a bus is
treated as a vector, bus elements become inaccessible. To identify and correct buses
used as vectors, use the Model Advisor check Check bus signals treated as
vectors or the function `Simulink.BlockDiagram.addBusToVector`.

## Ports

### Input

### **Port\_1** — Bus to convert to vector scalar | vector | bus

An input bus must consist of scalars or 1-D, row, or column vectors that have the
same data type, signal type, and sampling mode. If the input is a nonbus signal, the
block does no conversion.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output vector vector

The dimensions of the output vector depend on the dimensions of the input bus elements.
If the input bus contains row or column vectors, the block output is a row or column
vector, respectively. Otherwise, the output is a 1-D vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**Complex Number Support:** Yes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

To learn more about using buses for HDL code generation, see Buses (HDL Coder) and Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2007a**
