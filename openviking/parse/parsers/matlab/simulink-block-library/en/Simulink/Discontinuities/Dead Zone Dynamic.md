---
type: simulink-block
title: 'Dead Zone Dynamic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discontinuities'
documentation_page: 'deadzonedynamic'
documentation_source_path: 'slref/deadzonedynamic.html'
language: en
---

# Dead Zone Dynamic

## Ports

### Input

### **u** — Input signal scalar | vector

Input signal to the dead zone algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — Lower limit for the dead zone scalar | vector

Dynamic value providing the lower bound of the region of zero output.
When the input is less than **lo** then the output
value is shifted down by value of **lo**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — Upper limit for the dead zone scalar

Dynamic value providing the upper bound of the region of zero output.
When the input is greater than **up** then the output
value is shifted down by value of **up**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **y** — Output signal scalar | vector

Output signal after the dynamic dead zone algorithm is applied to the
input signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
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
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Provide dynamic region of zero output

The Dead Zone Dynamic block generates a region of zero output based on dynamic input
signals that specify the upper and lower limit. The block output depends on the input
**u**, and the values of the input signals **up**
and **lo**.

| Input | Output |
| --- | --- |
| `u >= lo` and `u <= up` | Zero |
| `u > up` | `u` – `up` |
| `u < lo` | `u` – `lo` |

The Dead Zone Dynamic block is a masked subsystem and does not have any
parameters.
