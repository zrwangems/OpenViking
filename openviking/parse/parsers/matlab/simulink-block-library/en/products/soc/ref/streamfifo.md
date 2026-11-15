---
type: simulink-block
title: 'Stream FIFO'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Hardware Logic Connectivity'
documentation_page: 'streamfifo'
documentation_source_path: 'ref/streamfifo.html'
language: en
---

# Stream FIFO

## Ports

### Input

### **dataIn** — Input stream data scalar

Input stream data from the data source. Specify this value as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dValidIn** — Indication of valid input stream data `Boolean` scalar

Control signal that indicates if the input stream data from the data source is
valid. When this value is `1` (true), the block accepts the values on
the **dataIn** port. When this value is `0` (false), the
block ignores the values on the **dataIn** port.

**Data Types:** `Boolean`

### **rdyFromDown** — Ready signal from downstream interface `Boolean` scalar

Control signal that indicates if the block can send stream data to the downstream
interface. When this value is `1` (true), the downstream interface is
ready, and the block can send the stream data. When this value is `0`
(false), the downstream interface is not ready, and the block cannot send the stream
data.

**Data Types:** `Boolean`
### Output

### **dataOut** — Output stream data scalar

Output stream data to the downstream interface. The data type of this output data
is the same as the data type of the input data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dValidOut** — Indication of valid output stream data `Boolean` scalar

Control signal that indicates if the output stream data is valid. When this value
is `1` (true), the output stream data on the **dataOut**
port is valid. When this value is `0` (false), the output stream data
on the **dataOut** port is not valid.

**Data Types:** `Boolean`

### **rdyToUp** — Ready signal to upstream interface `Boolean` scalar

Control signal that indicates if the block is ready to receive stream data from
the upstream interface. When this value is `1` (true), the block is
ready to accept stream data from the upstream interface. When this value is
`0` (false), the block is not ready to accept stream data from the
upstream interface.

**Data Types:** `Boolean`

## Parameters

### **Depth of FIFO** — FIFO depth `16` (default) | integer greater than or equal to four

Specify the depth of the FIFO as an integer greater than or equal to four. This
value is the maximum number of entries that can be buffered before data gets
dropped.

### **Almost full threshold** — Almost full threshold value `8` (default) | positive integer

Specify a value that asserts a back-pressure signal from the block to the data
source.

To avoid dropping data, set a value allowing the data source enough time to react to
backpressure. This value must be a positive integer and smaller than the FIFO
depth.

## Libraries

SoC Blockset / Hardware Logic Connectivity

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

Using SoC Blockset™, you can model a simplified streaming protocol in your model. Use HDL Coder™ to generate AXI4-Stream interfaces in the IP core. For more information about
the AXI4-stream protocol, see AXI4-Stream Interface.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Control backpressure between hardware logic and upstream data interface

The Stream FIFO block controls the backpressure from the hardware logic to
the upstream data interface. It also controls the flow between the upstream and downstream
data interfaces of the hardware logic. Integrate this block as a configurable first-in,
first-out (FIFO) block for AXI4 data stream applications. The block enables you to configure
its depth and set its almost full threshold value.
