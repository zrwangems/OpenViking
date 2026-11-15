---
type: simulink-block
title: 'Euler to NED Transformation HDL Optimized'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: 'Embedded Implementation / Fixed-Point Math Operations in MATLAB and Simulink / Coordinate Transformations'
documentation_page: 'eulertonedtransformationhdloptimized'
documentation_source_path: 'ref/eulertonedtransformationhdloptimized.html'
language: en
---

# Euler to NED Transformation HDL Optimized

## Ports

### Input

### **U In** — Input array 3-by-1 vector

Input array, specified as a 3-by-1 vector.

Fixed-point inputs must use binary-point scaling.

**Example:**
`UIn = [0;0;1]`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **Angle In** — Angles to rotate by 3-by-1 vector

Angles to rotate by, specified as a 3-by-1 real-valued vector containing the
angles phi, theta, and psi in radians.

**Example:**
`AngleIn = [phi;theta;psi]`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Valid In** — Whether input is valid `Boolean` scalar

Whether input is valid, specified as a Boolean scalar. This control signal
indicates when the data from the **U In** and **Angle
In** input ports are valid. When this value is `1`
(`true`), the block captures the values at the input ports
**U In** and **Angle In**. When this value is
`0` (`false`), the block ignores the input
samples.

**Data Types:** `Boolean`

### **Restart** — Whether to clear internal states `Boolean` scalar

Whether to clear internal states, specified as a Boolean scalar. When this value
is 1 (`true`), the block stops the current calculation and clears all
internal states. When this value is 0 (`false`) and the
**Valid In** value is 1 (`true`), the block begins
a new subframe.

**Data Types:** `Boolean`
### Output

### **U Out** — Rotated array 3-by-1 vector

Rotated array, returned as a 3-by-1 vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Valid Out** — Whether output data is valid boolean scalar

Whether the output data is valid, returned as a Boolean scalar. When the value of
this control signal is `1` (`true`), the block has
successfully computed the output **U Out**. When this value is
`0` (`false`), the output data is not
valid.

**Data Types:** `Boolean`

### **Ready** — Whether block is ready for input `Boolean` scalar

Whether the block is ready for input, returned as a Boolean scalar. This control
signal indicates when the block is ready for new input data. When this value is 1
(`true`) and **Valid In** value is 1
(`true`), the block accepts input data in the next time step. When
this value is 0 (`false`), the block ignores input data in the next
time step.

**Data Types:** `Boolean`

## Parameters

### **Architecture** — Architecture type `Pipelined` (default) | `Burst`

This parameter specifies the type of architecture.

- `Pipelined` — Select this value to specify low-latency
  architecture.
- `Burst` — Select this value to specify minimum resource
  architecture.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Architecture` |
| **Type:** character vector |
| **Values:** `'Pipelined'` | `'Burst'` |
| **Default:** `'Pipelined'` |

## Libraries

Fixed-Point Designer HDL Support / Coordinate Transformations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Supports fixed-point data types only. Fixed-point data types must use binary-point
scaling.

Generated C/C++ code will have timing of the HDL block.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

Supports fixed-point data types only. Fixed-point data types must use binary-point
scaling.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Computes Euler to North-East-Down transformation using pipelined or burst architecture and generates optimized HDL code

The Euler to NED Transformation HDL Optimized block provides two
architectures that implement Euler to North-East-Down (NED) transformation using a CORDIC
rotation kernel for FPGA and ASIC applications.

You can select an architecture that optimizes for either throughput or area.

- `Pipelined` — Use this architecture for high-throughput
  applications.
- `Burst` — Use this architecture for a minimum resource
  implementation.

The Euler to NED Transformation HDL Optimized block provides
hardware-friendly control signals.
