---
type: simulink-block
title: 'Simple Dual Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'simpledualportram'
documentation_source_path: 'ref/simpledualportram.html'
language: en
---

# Simple Dual Port RAM

## Ports
```yaml
ports:
- name: wr_din
  summary: Write data input Scalar (default)
  direction: input
  data_types: int8 | int16 | int32 | int64 | fixed point
- name: wr_addr
  summary: Write address Scalar (default)
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
- name: wr_en
  summary: Write enable Scalar (default)
  direction: input
  data_types: Boolean
- name: rd_addr
  summary: Read address Scalar (default)
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
- name: rd_dout
  summary: Output data from read address Scalar (default)
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### Input

### **wr\_din** — Write data input `Scalar` (default)

Data that you write into the RAM memory location when `wr_en` is
true. The data inherits the width and data type from the input signal.
`wr_din` can be a `double`,
`single`, `integer`, or a `fixed-point
(fi)` object, and can be real or complex.

Data type: scalar fixed point, integer, or complex

**Data Types:** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **wr\_addr** — Write address `Scalar` (default)

Write address.

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

### **rd\_dout** — Output data from read address `Scalar` (default)

Output data from read address, `rd_addr`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Address port width
  summary: Address bit width 8 (default)
  group: ''
  block_parameter: ram_size
  type: string scalar | character vector
  values: A minimum value of 2 and maximum value of 29
  default: '''8'''
```

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
| **RAMDirective** | Specify whether to map RAM blocks in your design to distributed RAMs, block RAMs, or UltraRAM memory on the target FPGA. See also RAMDirective. |

**Complex Data Support**

This block supports code generation for complex signals.

**Simple Dual Port RAM System**

The Simple Dual Port RAM
System block implementation uses a MATLAB System block that uses
the `hdl.RAM`
System object™. Use this block to perform simultaneous read and write operations. It has a
single output port to read data. In the Block Parameters dialog box of the block, you can
specify an initial value for the RAM.

Use this block to replace the Simple Dual Port RAM block in your model.
You obtain faster simulation results when using this block in your model.

## Version History

**Introduced in R2014a**

### R2024b: To be removed

The Simple Dual Port RAM is no longer recommended. This block will be removed in a
future release. Instead, use the Simple Dual Port RAM System block. For more
information, see Simple Dual Port RAM System.

## Description

(To be removed) Dual port RAM with single output port

The Simple Dual Port RAM block models RAM that supports simultaneous read
and write operations, and has a single output port for read data. You can use this block to
generate HDL code that maps to RAM in most FPGAs.

The Simple Dual Port RAM is similar to the Dual Port RAM,
but the Dual Port RAM has both a write data output port and a read data output
port.

### Read-During-Write Behavior

During a write operation, if a read operation occurs at the same address, old data
appears at the output.
