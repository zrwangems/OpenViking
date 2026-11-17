---
type: simulink-block
title: 'Single Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'singleportram'
documentation_source_path: 'ref/singleportram.html'
language: en
---

# Single Port RAM

## Ports
```yaml
ports:
- name: din
  summary: Write data input Scalar (default)
  direction: input
  data_types: single | double | int8 | int16 | uint8 | uint16 | fixed point
- name: addr
  summary: Write address Scalar (default)
  direction: input
  data_types: uint8 | uint16 | fixed point
- name: we
  summary: Write enable Scalar (default)
  direction: input
  data_types: Boolean
- name: dout
  summary: Output data Scalar (default)
  direction: output
```

### Input

### **din** — Write data input `Scalar` (default)

Data that you write into the RAM memory location when
`we` is true. The data inherits the width and data
type from the input signal. `din` can be a
`double`, `single`,
`integer`, or a `fixed-point (fi)`
object, and can be real or complex.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr** — Write address `Scalar` (default)

Address that you write the data into when `we` is
true. This value can be either `fixed-point(fi)` or
`integer`, must be unsigned, and have a fraction
length of `0`.

**Data Types:** `uint8` | `uint16` | `fixed point`

### **we** — Write enable `Scalar` (default)

When `we` is true, the RAM writes the data into the
memory location that you specify.

**Data Types:** `Boolean`
### Output

### **dout** — Output data `Scalar` (default)

Output data from address, `addr`.
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
- name: Output data during write
  summary: Controls output data New data (default) | Old data
  group: ''
  block_parameter: dout_type
  type: string scalar | character vector
  values: '"New data" | "Old data"'
  default: '''New data'''
```

### **Address port width** — Address bit width `8` (default)

Minimum bit width is 2, and maximum bit width is 29.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ram_size` |
| **Type:** string scalar | character vector |
| **Value:** A minimum value of `2` and maximum value of `29` |
| **Default:** `'8'` |

### **Output data during write** — Controls output data `New data` (default) | `Old data`

Controls the output data, `dout`, during a write access.
Specified as either:

- `New data`—During a write, new
  data appears at the output port, `dout`.
- `Old data`— During a write,
  old data appears at the output port, `dout`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `dout_type` |
| **Type:** string scalar | character vector |
| **Value:** `"New data"` | `"Old data"` |
| **Default:** `'New data'` |
## Libraries

HDL Coder / HDL RAMs

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized
logic.

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

**Single Port RAM System**

The Single
Port RAM System block implementation uses a MATLAB System block that uses
the `hdl.RAM`
System object™. Use this block to perform sequential read and write operations.
In the Block Parameters dialog box of the block, you can specify an initial
value for the RAM.

Use this block to replace the Single Port RAM block in your
model. You obtain faster simulation results when using this block in your model.

To perform simultaneous read and write operations to different addresses, use
the Simple Dual Port RAM System or the Dual Port RAM
System block instead.

## Version History

**Introduced in R2014a**

### R2024b: To be removed

The Single Port RAM is no longer recommended. This block will be
removed in a future release. Instead, use the Single Port RAM System
block. For more information, see Single Port RAM System.

## Description

(To be removed) Single port RAM

The Single Port RAM block models RAM that supports sequential read and
write operations.

If you want to model RAM that supports simultaneous read and write operations, use the
Dual Port RAM block or Simple Dual Port RAM block.
