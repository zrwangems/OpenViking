---
type: simulink-block
title: 'Sine HDL Optimized and Cosine HDL Optimized'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2023b
official_category: 'Lookup Tables'
documentation_page: 'sinehdloptimizedandcosinehdloptimized'
documentation_source_path: 'ref/sinehdloptimizedandcosinehdloptimized.html'
language: en
---

# Sine HDL Optimized and Cosine HDL Optimized

## Ports
```yaml
ports:
- name: Input
  summary: Input signal to implement sine or cosine wave real-valued signal
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point | enumerated | bus
- name: sin(2\*pi\*u)
  summary: Fixed-point sine wave real-valued fixed-point signal
  direction: output
  data_types: fixed point
- name: cos(2\*pi\*u)
  summary: Fixed-point cosine wave real-valued fixed-point signal
  direction: output
  data_types: fixed point
- name: exp(j\*2\*pi\*u)
  summary: Complex exponential complex-valued fixed-point signal
  direction: output
  data_types: fixed point
```

### Input

### **Input** — Input signal to implement sine or cosine wave real-valued signal

Input signal, u, specified as a real-valued scalar, vector, or matrix.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **sin(2\*pi\*u)** — Fixed-point sine wave real-valued fixed-point signal

Fixed-point sine wave, implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula** is set to
`sin(2*pi*u)` or `sin(2*pi*u) and
cos(2*pi*u)`.

**Data Types:** `fixed point`

### **cos(2\*pi\*u)** — Fixed-point cosine wave real-valued fixed-point signal

Fixed-point cosine wave, implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula** is set to
`cos(2*pi*u)` or `sin(2*pi*u) and
cos(2*pi*u)`.

**Data Types:** `fixed point`

### **exp(j\*2\*pi\*u)** — Complex exponential complex-valued fixed-point signal

Complex exponential, implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula** is set to
`exp(j*2*pi*u)`.

**Data Types:** `fixed point`
## Parameters
```yaml
parameters:
- name: Output formula
  summary: Select the signal(s) to output cos(2*pi*u) | sin(2*pi*u) | exp(j*2*pi*u) | sin(2*pi*u) and cos(2*pi*u)
  group: ''
- name: Number of data points
  summary: Specify the number of data points to retrieve from the lookup table 64 (default) | integer, greater than or equal
    to 2
  group: ''
- name: Table data type
  summary: Specify the table data type fixdt(0,16,15) (default) | fixed point expression
  group: ''
- name: Data type assistant
  summary: Select the mode of data type specification Fixed point (default) | Expression
  group: ''
- name: Simulate RAM Delay
  summary: Insert a unit delay off (default) | on
  group: ''
```

### **Output formula** — Select the signal(s) to output `cos(2*pi*u)` | `sin(2*pi*u)` | `exp(j*2*pi*u)` | `sin(2*pi*u) and cos(2*pi*u)`

Select the signal(s) to output.

### **Number of data points** — Specify the number of data points to retrieve from the lookup table `64` (default) | `integer, greater than or equal to 2`

Specify the number of data points to retrieve from the lookup table. The
implementation is most efficient when you specify the lookup table data points to be
`(2^n)`, where *n* is an
integer.

### **Table data type** — Specify the table data type `fixdt(0,16,15)` (default) | `fixed point expression`

Specify the table data type. You can specify an expression that evaluates to a data
type, for example, `fixdt(1,16,0)`.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the table data type.

### **Data type assistant** — Select the mode of data type specification `Fixed point` (default) | `Expression`

Select the mode of data type specification. If you select
`Expression`, enter an expression that evaluates to a data
type, for example, `fixdt(1,16,0)`.

If you select `Fixed point`, you can use the options in the
**Data Type Assistant** to specify the fixed-point data type. In the
`Fixed point` mode, you can choose binary point scaling, and
specify the signedness, word length, fraction length, and the data type override
setting.

### **Simulate RAM Delay** — Insert a unit delay `off` (default) | `on`

Selecting this check box inserts a unit delay without reset. You can simulate this
delay in the Simulink® modeling environment. When you generate HDL code, a
no-reset register is inserted after the block. The
combination of lookup table with no-reset register maps
to RAM on the target hardware.
## Libraries

HDL Coder / Lookup Tables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized logic.

**HDL Architecture**

The HDL code implements the Sine HDL Optimized or Cosine HDL
Optimized block by using the quarter-wave lookup table that you specify in the
Simulink block parameters.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **MapToRAM** | Map lookup tables (LUTs) to RAM. The default is `on`. See also MapToRAM. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

**Limitations and Considerations**

When the blocks have Delay block at the output and **Number of data
points** is greater than `1024`, the blocks does not map to
the Block RAM if the target frequency is greater than 400 MHz.

## Version History

**Introduced in R2016b**

## Description

Implement fixed-point sine and cosine wave by using lookup table approach optimized for HDL code generation

The Sine HDL Optimized block and Cosine HDL Optimized block
implements a fixed-point sine or cosine wave by using a lookup table method that exploits
quarter-wave symmetry.

For the most efficient HDL implementation, configure the block with an exact power of two
as the number of elements. In the Block Parameters dialog box, for **Number of data
points**, specify an integer that is an exact power of two. That is, specify the
lookup table data points to be `(2^n)`, where
*n* is an integer. By default, the **Number of data
points** is 64.

When you specify a power of two for the **Number of data points**, the
lookup tables precede a register without reset after HDL code generation. The combination of
the lookup table block and register without reset maps efficiently to RAM on the target
device.

Depending on your selection of the **Output formula** parameter, the
blocks can output these functions of the input signal:

- sin(2π*u*)
- cos(2π*u*)
- exp(*i*2π*u*)
- sin(2π*u*) and cos(2π*u*)

Use the **Table data type** parameter to specify the word length of the
fixed-point output data type. The fraction length of the output is the output word length
minus 2.
