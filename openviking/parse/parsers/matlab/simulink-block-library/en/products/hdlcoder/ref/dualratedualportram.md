---
type: simulink-block
title: 'Dual Rate Dual Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'dualratedualportram'
documentation_source_path: 'ref/dualratedualportram.html'
language: en
---

# Dual Rate Dual Port RAM

## Ports

### Input

### **din\_A** — Port A write data input `Scalar` (default)

Data that you write into the RAM memory location when `we_A` is
true. The data inherits the width and data type from the input signal.
`din_A` can be a `double`,
`single`, `integer`, or a `fixed-point
(fi)` object, and can be real or complex.

Data type: scalar fixed point, integer, or complex

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **addr\_A** — Port A write address `Scalar` (default)

Address that you write the data into when `we_A` is true. This
value can be either `fixed-point(fi)` or `integer`,
must be unsigned, and have a fraction length of `0`.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **we\_A** — Port A write enable `Scalar` (default)

Write enable for RAM port A. Set `we_A` to
`true` for a write operation, or `false` for a
read operation.

**Data Types:** `Boolean`

### **din\_B** — Port B write data `Scalar` (default)

Data that you write into the RAM memory location when `we_B` is
true. The data inherits the width and data type from the input signal.
`din_B` can be a `double`,
`single`, `integer`, or a `fixed-point
(fi)` object, and can be real or complex.

Data type: scalar fixed point, integer, or complex

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **addr\_B** — Port B write address `Scalar` (default)

Address that you write the data into when `we_B` is true. This
value can be either `fixed-point(fi)` or `integer`,
must be unsigned, and have a fraction length of `0`.

Data type: scalar fixed point, integer, or complex

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **we\_B** — Port B write enable `Scalar` (default)

Write enable for RAM port B. Set `we_B` to
`true` for a write operation, or `false` for a
read operation.

**Data Types:** `Boolean`
### Output

### **dout\_A** — Port A output data `Scalar` (default)

Output data from RAM port A address, `addr_A`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **dout\_B** — Port B output data `Scalar` (default)

Output data from RAM port B address, `addr_B`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Address port width** — Address bit width 8 (default)

Minimum bit width is 2, and maximum bit width is 28.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ram_size` |
| **Type:** string scalar | character vector |
| **Value:** A minimum value of `2` and maximum value of `28` |
| **Default:** `'8'` |

## Libraries

HDL Coder / HDL RAMs

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

**Note**

For simulation results that match the generated HDL code, in the Solver pane of the
Configuration Parameters dialog box, clear the checkbox for **Treat each
discrete rate as a separate task**. When the checkbox is cleared,
single-tasking mode is enabled. If you simulate the block with this check box selected,
the output data can update in the same cycle but in the generated HDL code, the output
data is updated one cycle later.

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

**Note**

The **RAMDirective** property is not available for use with the
Dual Rate Dual Port RAM because the block does not have a single clock
interface.

**Complex Data Support**

This block supports code generation for complex
signals. You cannot have mixed real-value and complex inputs.

## Version History

**Introduced in R2014a**

## Description

Dual Port RAM that supports two rates

The Dual Rate Dual Port RAM block models a RAM that supports simultaneous
read and write operations to different addresses at two clock rates. Port A of the RAM can run
at one rate, and port B can run at a different rate.

In high-performance hardware applications, you can use this
block to access the RAM twice per clock cycle. If you generate HDL code, this block maps to a
dual-clock dual-port RAM in most FPGAs.

### Simultaneous Access

You can access different addresses from ports A and B simultaneously. You can also read
the same address from ports A and B simultaneously.

However, do not access an address from one RAM port while it is being written from the
other RAM port. During simulation, if you access an address from one RAM port at the same
time as you write that address from the other RAM port, the software reports an
error.

### Read-During-Write Behavior

The RAM has write-first behavior. When you write to the RAM, the new write data is
immediately available at the output port.
