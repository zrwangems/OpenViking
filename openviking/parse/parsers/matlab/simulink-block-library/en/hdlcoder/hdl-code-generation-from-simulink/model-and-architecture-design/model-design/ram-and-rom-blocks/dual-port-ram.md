---
type: simulink-block
title: 'Dual Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'dualportram'
documentation_source_path: 'ref/dualportram.html'
language: en
---

# Dual Port RAM

## Ports

### Input

### **wr\_din** — Write data input `Scalar` (default)

Data that you write into the RAM memory location when `wr_en` is
true. The data inherits the width and data type from the input signal.
`wr_din` can be a `double`,
`single`, `integer`, or a `fixed-point
(fi)` object, and can be real or complex.

Data type: scalar fixed point, integer, or complex

**Data Types:** `int8` | `int16` | `int32` | `int64` | `Boolean` | `fixed point`

### **wr\_addr** — Write address `Scalar` (default)

Address that you write the data into when `wr_en` is true. This
value can be either `fixed-point(fi)` or `integer`,
must be unsigned, and have a fraction length of `0`.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wr\_en** — Write enable `Scalar` (default)

When `wr_en` is true, the RAM writes the data into the memory
location that you specify.

**Data Types:** `Boolean`

### **rd\_addr** — Read address `Scalar` (default)

Address that you read the data from. This value can be either
`fixed-point(fi)` or `integer`, must be unsigned,
and have a fraction length of `0`.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **wr\_dout** — Output data from write address `Scalar` (default)

Output data from write address, `wr_addr`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **rd\_dout** — Output data from read address `Scalar` (default)

Output data from read address, `rd_addr`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Address port width** — Address bit width 8 (default)

Minimum bit width is 2, and maximum bit width is 29.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ram_size` |
| **Type:** string scalar | character vector |
| **Value:** A minimum value of `2` and maximum value of `29` |
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

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **RAMDirective** | Specify whether to map the RAM blocks in your design to RAM blocks on the target FPGA. You cannot map Dual Port RAM blocks to UltraRAM. Mapping to UltraRAM requires the block to have a fixed read behavior. For more details, see RAMDirective. |

**Complex Data Support**

This block supports code generation for complex signals.

**Dual Port RAM System**

The Dual Port RAM
System block implementation uses a MATLAB System block that uses
the `hdl.RAM`
System object™. Use this block to perform simultaneous read and write operations. It has a
read data output port and a write data output port. In the Block Parameters dialog box of
the block, you can specify an initial value for the RAM. If you do not want to use the
write data output port, to achieve better RAM inference, use the Simple Dual Port
RAM System block instead.

Use this block to replace the Dual Port RAM block in your model. You
obtain faster simulation results when using this block in your model.

## Version History

**Introduced in R2014a**

### R2024b: To be removed

The Dual Port RAM is no longer recommended. This block will be removed in a
future release. Instead, use the Dual Port RAM System block. For more
information, see Dual Port RAM System.

## Description

(To be removed) Dual port RAM with two output ports

The Dual Port RAM block models a RAM that supports simultaneous read and
write operations, and has both a read data output port and write data output port. You can use
this block to generate HDL code that maps to RAM in most FPGAs.

If you do not need to use the write output data, `wr_dout`, you can
achieve better RAM inference with synthesis tools by using the Simple Dual Port RAM block.

### Read-During-Write Behavior

During a write, new data appears at the output of the write port
(`wr_dout`) of the Dual Port RAM block. If a read operation occurs
simultaneously at the same address as a write operation, old data appears at the read output
port (`rd_dout`).
