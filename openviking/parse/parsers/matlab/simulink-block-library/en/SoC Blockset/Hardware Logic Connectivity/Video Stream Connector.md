---
type: simulink-block
title: 'Video Stream Connector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'videostreamconnector'
documentation_source_path: 'ref/videostreamconnector.html'
language: en
---

# Video Stream Connector

## Ports

### Input

### **wrData** — Input video data scalar

Input video data from the data source. Specify this value as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlIn** — Input control signals accompanying pixel stream `pixelControl` bus

Control signals accompanying the pixel stream, specified as a
`pixelcontrol` bus containing five signals. The signals describe
the validity of the pixel and its location in the frame. For additional information
about the `pixelcontrol` bus type, see AXI4-Stream Video Interface.

**Data Types:** `pixelcontrol`

### **rdCtrlIn** — Ready signal from downstream interface boolean scalar

Control signal that indicates if the block can send video data to downstream
interface. When this value is (true), the downstream block is ready to receive
data.
### Output

### **rdData** — Output video data scalar

Output video data to the downstream destination IP.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlOut** — Output control signals accompanying output pixel stream `pixelcontrol` bus

Control signals accompanying the output video data, specified as a
`pixelcontrol` bus containing five signals. The signals describe
the validity of the pixel and its location in the frame.

**Data Types:** `pixelcontrol`

### **wrCtrlOut** — Ready signal to the upstream interface boolean scalar

Control signal that indicates that the block can receive stream data from upstream
interface.

**Data Types:** `Boolean`

## Parameters

Not documented in R2025b.

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

Connect two IPs with video streaming interfaces

The Stream Connector block connects two IPs with video streaming
interfaces. Use this block in the FPGA model of an SoC application to connect two IPs.
