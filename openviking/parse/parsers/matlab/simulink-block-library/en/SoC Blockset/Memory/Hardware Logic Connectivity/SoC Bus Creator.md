---
type: simulink-block
title: 'SoC Bus Creator'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Hardware Logic Connectivity'
documentation_page: 'socbuscreator'
documentation_source_path: 'ref/socbuscreator.html'
language: en
---

# SoC Bus Creator

## Ports

### Input

### **valid** — Valid control signal boolean scalar

Valid control signal, specified as a scalar. You can use this port for data stream
and pixel stream protocols only.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
either `Data stream` or `Pixel
stream` and the **Control type** parameter to
`Valid`.

**Data Types:** `Boolean`

### **tlast** — Indication of end of data packet boolean scalar

Indication of end of the data packet, specified as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Data stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **ready** — Ready control signal boolean scalar

Ready control signal, specified as a Boolean scalar. This port is available for
`Data stream` and `Pixel stream`
control protocols.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
either `Data stream` or `Pixel
stream` and the **Control type** parameter to
`Ready` or `Ready with frame
sync`.

**Data Types:** `Boolean`

### **hStart** — First pixel in horizontal line of frame boolean scalar

First pixel in a horizontal line of a frame, specified as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **hEnd** — Last pixel in horizontal line of frame boolean scalar

Last pixel in a horizontal line of a frame, specified as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **vStart** — First pixel in first (top) line of frame boolean scalar

First pixel in the first (top) line of a frame, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **vEnd** — Last pixel in last (bottom) line of frame boolean scalar

Last pixel in the last (bottom) line of a frame, specified as a Boolean
scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **fsync** — Frame synchronization boolean scalar

Frame synchronization, specified as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Ready with frame sync`.

**Data Types:** `Boolean`

### **rd\_addr** — Reader address scalar

Reader address, specified as a scalar. It is the starting address for the read
transaction that is sampled at the first cycle of the transaction.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `uint32`

### **rd\_len** — Reader data length scalar

Reader data length, specified as a scalar. It means the number of data values that
you want to read, sampled at the first cycle of the transaction.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `uint32`

### **rd\_avalid** — Reader valid status boolean scalar

Reader valid status, specified as a Boolean scalar. It indicates whether the read
request is valid.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `Boolean`

### **rd\_dready** — Reader ready status boolean scalar

Reader ready status, specified as a Boolean scalar. It indicates when the hardware
logic can start accepting data.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `Boolean`

### **wr\_addr** — Writer address scalar

Specify the starting address to which the hardware writes.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `uint32`

### **wr\_len** — Writer data length scalar

Specify the number of data elements in the write transaction.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `uint32`

### **wr\_valid** — Writer valid data boolean scalar

Writer valid data, specified as a scalar. It indicates the data signal sampled at
the output is valid.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `Boolean`
### Output

### **ctrlBus** — Output control bus bus

Output control bus, returned as a bus.

The data type of the output control bus depends on the values of the
**Control protocol** and **Control type**
parameters.

| Parameter Configuration | Output Data Type |
| --- | --- |
| Set **Control protocol** to `Data stream` and **Control type** to `Ready`. | `StreamS2MBusObj` |
| Set **Control protocol** to `Data stream` and **Control type** to `Valid`. | `StreamM2SBusObj` |
| Set **Control protocol** to `Pixel stream` and **Control type** to `Ready`. | `StreamVideoS2MBusObj` |
| Set **Control protocol** to `Pixel stream` and **Control type** to `Valid`. | `pixelcontrol` |
| Set **Control protocol** to `Pixel stream` and **Control type** to `Ready frame with sync`. | `StreamvideoFsyncS2MBusObj` |
| Set **Control protocol** to `Random access read` and **Control type** to `Ready`. | `ReadControlM2SBusObj` |
| Set **Control protocol** to `Random access write` and **Control type** to `Valid`. | `WriteControlM2SBusObj` |

**Data Types:** `StreamS2MBusObj` | `StreamM2SBusObj` | `StreamVideoS2MBusObj` | `pixelcontrol` | `StreamvideoFsyncS2MBusObj` | `ReadControlM2SBusObj` | `WriteControlM2SBusObj`

## Parameters

### **Control protocol** — Protocol interface selection `Data stream` (default) | `Pixel stream` | `Random access read` | `Random access write`

Specify the protocol interface as one of these values:

- `Data stream` — Use this protocol if you require
  AXI4 data stream.
- `Pixel stream` — Use this protocol if you
  require AXI4 video stream.
- `Random access read` — Use this protocol if you
  require AXI4 read.
- `Random access write` — Use this protocol if you
  require AXI4 write.

The input ports of the block vary based on the type of **Control
protocol** and **Control type** that you select. For more
details, see Description.

### **Control type** — Control type selection `Valid` (default) | `Ready` | `Ready with frame sync`

Specify the type of control.

To enable the `Ready with frame sync` option, set the
**Control protocol** parameter to `Pixel
stream`.

The input ports of the block vary based on the type of **Control
protocol** and **Control type** that you select. For more
details, see Description.

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

Convert control signals to bus

The SoC Bus Creator block combines a set of signals into a bus. The block
accepts control signals and outputs a bus.

You can configure this block to support multiple protocol interface types. Parameter and
port configurations for this block vary based on your desired protocol interface type and mode
of operation, as outlined in this table.

| Protocol Interface Type | Mode of Operation | Parameter Configuration | Enabled Input Ports |
| --- | --- | --- | --- |
| Data stream | Read data stream | Set **Control protocol** to `Data stream` and **Control type** to `Ready`. | **ready** |
| Write data stream | Set **Control protocol** to `Data stream` and **Control type** to `Valid`. | **valid** |
| **tlast** |
| Pixel stream | Read video stream | Set **Control protocol** to `Pixel stream` and **Control type** to `Ready`. | **ready** |
| Write video stream | Set **Control protocol** to `Pixel stream` and **Control type** to `Valid`. | **hStart** |
| **hEnd** |
| **vStart** |
| **vEnd** |
| **valid** |
| Read video stream with frame sync | Set **Control protocol** to `Pixel stream` and **Control type** to `Ready frame with sync`. | **ready** |
| **fsync** |
| Random access read | Read data | Set **Control protocol** to `Random access read` and **Control type** to `Ready`. | **rd\_addr** |
| **rd\_len** |
| **rd\_avalid** |
| **rd\_dready** |
| Random access write | Write data | Set **Control protocol** to `Random access write` and **Control type** to `Valid`. | **wr\_addr** |
| **wr\_len** |
| **wr\_valid** |
