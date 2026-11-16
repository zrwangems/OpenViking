---
type: simulink-block
title: 'True Dual Port RAM System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / RAM and ROM Blocks'
documentation_page: 'truedualportramsystem'
documentation_source_path: 'ref/truedualportramsystem.html'
language: en
---

# True Dual Port RAM System

## Ports

### Input

### **din\_a** — Data to write `scalar` | `vector`

Data to write, specified as scalar or vector. You can write the data
into the RAM memory location when the signal at port
**we\_a** is `true`. This value can
be an integer, or of type `double`,
`single` or `half`. The value can
also be a `fi` object and can be real or
complex.

#### Bus Support:

You can use non-virtual bus and arrays of buses for HDL code
generation.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **addr\_a** — Address to write `scalar` | `vector`

Address to write, specified as a scalar or a vector. Use this address
to write the data from the **din\_a** port to the RAM.
This value can be either a `fixed-point (fi)` or an
unsigned `integer` and must be between
`2` and `31` bits long. The values
at the **addr\_a** and **addr\_b** ports
cannot be the same.

**Data Types:** `uint8` | `uint16` | `fixed point`

### **we\_a** — Write enable `scalar` | `vector`

Write enable, specified as a scalar or a vector. When the signal at
port **we\_a** is `true`, the block
writes data from the **din\_a** port to the memory
location specified by the **addr\_a** port.

**Note**

To use column-write method, the data type must be an
`integer` or a
`fixed-point`.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **din\_b** — Data to write `scalar` | `vector`

Data to write, specified as scalar or vector. You can write the data
into the RAM memory location when the signal at port
**we\_b** is `true`. This value can
be an integer, or of type `double`,
`single` or `half`. The value can
also be a `fi` object and can be real or
complex.

#### Bus Support:

You can use non-virtual bus and arrays of buses for HDL code
generation.

**Data Types:** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr\_b** — Address to write `scalar` | `vector`

Address to write, specified as a scalar or a vector. Use this address
to write data from the **din\_b** port to the RAM. This
value can be either a `fixed-point (fi)` or an unsigned
`integer` and must be between `2`
and `31` bits long. The values at the
**addr\_a** and **addr\_b** ports
cannot be the same.

**Data Types:** `uint8` | `uint16` | `fixed point`

### **we\_b** — Write enable `scalar` | `vector`

Write enable, specified as a scalar or a vector. When the signal at
port **we\_b** is `true`, the block
writes data from the **din\_b** port to the memory
location specified by the **addr\_b** port.

**Note**

To use column-write method, the data type must be an
`integer` or a
`fixed-point`.

**Data Types:** `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **dout\_a** — Write data output `scalar` | `vector`

Write data output, returned as a scalar or vector. The block reads the
new or old output data from the memory location specified by the
**addr\_a** port.

### **dout\_b** — Write data output `scalar` | `vector`

Write data output, returned as a scalar or vector. The block reads the
new or old data from the memory location specified by the
**addr\_b** port.

## Parameters

### Main

### **Type of RAM** — RAM type `True dual port` (default) | `Simple dual port` | `Single port` | `Dual port` | `Simple tri port`

Type of RAM, specified as either:

- `Single port` — Create a single
  port RAM with write data, address, and write enable data as
  inputs and read data as the output.
- `Simple dual port` — Create a
  simple dual port RAM with write data, write address, write
  enable, and read address as inputs, and data from the read
  address as the output.
- `Dual port` — Create a dual port
  RAM with write data, write address, write enable, and read
  address as inputs, and data from the read address and write
  address as the outputs.
- `True dual port` — Create a true
  dual port RAM with write data `a` and
  `b`, write and read addresses for
  `a` and `b`, and write
  enable `a` and `b` as
  inputs and data from write addresses `a`
  and `b` as the outputs.
- `Simple tri port` — Create a
  simple tri port RAM with write data, write address, write
  enable, and read addresses `a` and
  `b` as inputs and data from read
  addresses `a` and `b` as
  the outputs.

The code generator dynamically configures the input and output ports
of the block based on the RAM type that you specify.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`RAMType` |
| **Type:**  character vector, string |
| **Values:**  `Dual port` | `Simple dual port` | `Single port` | `True dual port` | `Simple tri port` |
| **Default:**  `True dual port` |

### **Behavior for write output** — Write output behavior `New data` (default) | `Old data`

Select the behavior for write output as `New data` or
`Old data`:

- `New data` — Send out new data at
  the address to the output.
- `Old data` — Send out old data at
  the address to the output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`WriteOutputValue` |
| **Type:**  character vector, string |
| **Values:**  `New data` | `Old data` |
| **Default:**  `New data` |

### **Initial output of RAM** — Initial simulation output of RAM `'0.0'` (default) | `Scalar` | `Vector`

Specify the initial simulation output of the RAM by using one of these options:

- A scalar value.
- A vector with a one-to-one mapping between the initial value and the RAM
  words.
- An *n*-by-*m* matrix with a one-to-one mapping
  between the initial values and the RAM words in the RAM banks, where
  *n* represents the number of RAM banks and *m*
  represents the number of address locations in the RAM block, or vice-versa.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`RAMInitialValue` |
| **Type:**  integer, floating point |
| **Values:**  `0.0` | `Scalar` | `Vector` |
| **Default:**  `0.0` |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### Advanced

### **Model RAM with one cycle of delay** — Model RAM with one cycle of delay `on` (default) | `off`

*Since R2024b*

- When you select this parameter, the RAM delays the input data by one cycle
  before the output can read it. Use this option to ensure the block is
  cycle-accurate with the generated HDL code.
- When you clear this parameter, the RAM reads and outputs the input data
  immediately, but adds one cycle of latency during HDL code generation. Use
  this option to leverage clock-rate pipelining when you specify an
  oversampling value or work with multirate models.

#### Dependencies

To enable this parameter, clear the **Use asynchronous read feature in
target hardware** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`ModelRAMDelay` |
| **Type:**  character vector, string |
| **Values:**  `'on'` | `'off'` |
| **Default:**  `'on'` |

### **Specify vector input access** — Specify vector input access as serial or parallel `serial` (default) | `parallel`

*Since R2025a*

- When you set this parameter to `serial`, the code
  generator infers parallel banks of RAM from vector inputs to RAM System
  block.
- When you set this parameter to `parallel`:

  - The code generator does not scale up RAM consumption with the size
    of the vector input when you generate HDL Code. Instead, it applies
    each operation of the input signals one at a time, starting with the
    first index. Enabling serial access allows you to leverage
    multicycle RAM access at a faster clock rate while modeling with a
    vector input at the data rate.
  - If the RAM System block exists in a clock-rate
    pipelining region, the serialization uses a clock-rate
    implementation instead of local multirate implementation.

#### Dependencies

To enable this parameter, clear the **Model RAM with one cycle of
delay** parameter or enable the **Use asynchronous read
feature in target hardware** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`VectorAccess` |
| **Type:**  character vector, string |
| **Values:**  `'serial'` | `'parallel'` |
| **Default:**  `'serial'` |

## Libraries

HDL Coder / HDL RAMs

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

The block has a `MATLAB System` architecture, which
indicates that the block implementation uses the `hdl.RAM`
System object™.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **RAMDirective** | Specify whether to map RAM blocks in your design to the RAM blocks on the target FPGA. For UltraRAM mapping, **Initial output of RAM** must be set to `0`. For more details, see RAMDirective. |

**Complex Data Support**

This block supports code generation for complex signals.

## Version History

**Introduced in R2023b**

### R2024b: Use clock-rate pipelining

You can use True Dual Port RAM System block inside a data rate feedback loop and use clock-rate
pipelining optimization. This model design is helpful for applications that require
programmable or tunable lookup tables without having to regenerate
bitstreams.

Use the new parameter **Model RAM with one cycle of delay** to
model delay in your simulation. **Model RAM with one cycle of delay**
is enabled by default.

### R2024b: Parameter name changes

These parameters are renamed:

| Previous Name | Current Name |
| --- | --- |
| **Specify the type of RAM** | **Type of RAM** |
| **Specify the output data for a write operation** | **Behavior for write output** |
| **Specify the RAM initial value** | **Initial output of RAM** |

### R2024b: Write to RAM in columns using column-write operations in RAM System blocks

In this block, you can use the column-write method to selectively modify specific
parts of the memory without altering the remaining parts at a specified memory
address.

### R2024b: Initialize RAM banks with unique initial values for vector data inputs

In this block, you can initialize RAM banks with unique initial values.

### R2024a: Array of Buses Input Support

The block now supports HDL code generation for input data specified as an array of
buses.

### R2024a: Half-Precision and Boolean Data Support

The block now supports HDL code generation with input data of type
`Half` or
`Boolean`.

## Description

True dual-port RAM that supports simultaneous read and write operations

The True Dual Port RAM System block models a true dual-port RAM that
supports simultaneous read and write operations through two output ports for read data.
This blocks allows concurrent access to different memory addresses for both read and
write operations. To configure this block, open the block and set the **Type of
RAM** parameter to `True dual port`. By using
this block, you can:

- Create parallel RAM banks by using vector data at the
  **din**, **addr**, and
  **we** ports.
- Specify an initial value for the RAM using the **Initial output
  of RAM** parameter.
- Perform cycle-accurate read operation by selecting the **Model
  RAM with one cycle of delay** parameter.
- Use the column-write method to write to specified bits in an addressed
  memory location.

**Note**

During a write operation, if a read operation occurs simultaneously at the
same address, old data appears at the read output port.
