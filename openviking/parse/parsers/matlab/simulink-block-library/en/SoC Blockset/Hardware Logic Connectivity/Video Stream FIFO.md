---
type: simulink-block
title: 'Video Stream FIFO'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'videostreamfifo'
documentation_source_path: 'ref/videostreamfifo.html'
language: en
---

# Video Stream FIFO

## Ports
```yaml
ports:
- name: pixelIn
  summary: Input pixel data scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: ctrlIn
  summary: Control signals accompanying input pixel data pixelcontrol bus
  direction: input
  data_types: pixelcontrol
- name: rdyFromDown
  summary: Ready signal from downstream interface Boolean scalar
  direction: input
  data_types: Boolean
- name: pixelOut
  summary: Output pixel data scalar
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: ctrlOut
  summary: Control signals accompanying output pixel data pixelcontrol bus
  direction: output
  data_types: pixelcontrol
- name: rdyToUp
  summary: Ready signal to upstream interface Boolean scalar
  direction: output
  data_types: Boolean
```

### Input

### **pixelIn** — Input pixel data scalar

Input pixel data from the data source. Specify this value as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ctrlIn** — Control signals accompanying input pixel data `pixelcontrol` bus

Control signals accompanying the pixel stream, specified as a
`pixelcontrol` bus containing five signals. The signals describe
the validity of the pixel and its location in the frame.

**Data Types:** `pixelcontrol`

### **rdyFromDown** — Ready signal from downstream interface `Boolean` scalar

Control signal that indicates if the block can send pixel data to the downstream
interface. When this value is `1` (true), the downstream interface is
ready, and the block can send the pixel data. When this value is `0`
(false), the downstream interface is not ready, and the block cannot send the pixel
data.

**Data Types:** `Boolean`
### Output

### **pixelOut** — Output pixel data scalar

Output pixel data to the downstream interface. The data type of this output data
is the same as the data type of the input data.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ctrlOut** — Control signals accompanying output pixel data `pixelcontrol` bus

Control signals accompanying output pixel stream, returned as a
`pixelcontrol` bus containing five signals. The signals describe
the validity of the pixel and its location in the frame.

**Data Types:** `pixelcontrol`

### **rdyToUp** — Ready signal to upstream interface `Boolean` scalar

Control signal that indicates if the block is ready to receive pixel data from the
upstream interface. When this value is `1` (true), the block is ready
to accept pixel data from the upstream interface. When this value is
`0` (false), the block is not ready to accept pixel data from the
upstream interface.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Depth of FIFO
  summary: FIFO depth 16 (default) | positive integer
  group: ''
- name: Almost full threshold
  summary: Almost full threshold value 8 (default) | positive integer
  group: ''
```

### **Depth of FIFO** — FIFO depth `16` (default) | positive integer

Specify the depth of the FIFO. This value must be a positive scalar integer and is
the maximum number of entries that can be buffered before data gets dropped.

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

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Control backpressure between hardware logic and upstream video interface

The Video Stream FIFO block controls the back-pressure from the hardware
logic to the upstream video interface. It also controls the flow between the upstream and
downstream pixel data interfaces of hardware logic. Integrate this block as a configurable
first-in, first-out (FIFO) block for AXI4 video stream applications. The block enables you to
configure its depth and set its almost full threshold value.
