---
type: simulink-block
title: 'SoC Bus Selector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Hardware Logic Connectivity'
documentation_page: 'socbusselector'
documentation_source_path: 'ref/socbusselector.html'
language: en
---

# SoC Bus Selector

## Ports

### Input

### **ctrlBus** — Input control bus bus

Input control bus, specified as a bus.

The data type of the input control bus depends on the values of the
**Control protocol** and **Control type**
parameters.

| Parameter Configuration | Input Data Type |
| --- | --- |
| Set **Control protocol** to `Data stream` and **Control type** to `Valid`. | `StreamM2SBusObj` |
| Set **Control protocol** to `Data stream` and **Control type** to `Ready`. | `StreamS2MBusObj` |
| Set **Control protocol** to `Pixel stream` and **Control type** to `Valid`. | `pixelcontrol` |
| Set **Control protocol** to `Pixel stream` and **Control type** to `Ready`. | `StreamVideoS2MBusObj` |
| Set **Control protocol** to `Random access read` and **Control type** to `Valid`. | `ReadControlS2MBusObj` |
| Set **Control protocol** to `Random access write` and **Control type** to `Ready`. | `WriteControlS2MBusObj` |

**Data Types:** `StreamM2SBusObj` | `StreamS2MBusObj` | `pixelcontrol` | `StreamVideoS2MBusObj` | `ReadControlS2MBusObj` | `WriteControlS2MBusObj`
### Output

### **valid** — Valid control signal boolean scalar

Valid control signal, returned as a scalar. You can use this port for data stream
and pixel stream protocols only.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
either `Data stream` or `Pixel
stream` and the **Control type** parameter to
`Valid`.

**Data Types:** `Boolean`

### **tlast** — Indication of end of data packet boolean scalar

Indication of end of the data packet, returned as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Data stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **ready** — Ready control signal boolean scalar

Ready control signal, returned as a Boolean scalar. This port is available for
`Data stream` and `Pixel stream`
control protocols.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
either `Data stream` or `Pixel
stream` and the **Control type** parameter to
`Ready`.

**Data Types:** `Boolean`

### **hStart** — First pixel in horizontal line of frame boolean scalar

First pixel in a horizontal line of a frame, returned as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **hEnd** — Last pixel in horizontal line of frame boolean scalar

Last pixel in a horizontal line of a frame, returned as a Boolean scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **vStart** — First pixel in first (top) line of frame boolean scalar

First pixel in the first (top) line of a frame, returned as a Boolean
scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **vEnd** — Last pixel in last (bottom) line of frame boolean scalar

Last pixel in the last (bottom) line of a frame, returned as a Boolean
scalar.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Pixel stream` and the **Control type**
parameter to `Valid`.

**Data Types:** `Boolean`

### **rd\_aready** — Accept read requests boolean scalar

Accept read requests, returned as a scalar. It indicates when to accept read
requests.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `Boolean`

### **rd\_dvalid** — Read request valid boolean scalar

Read request valid, returned as a Boolean scalar. It is the control signal that
indicates the data returned from the read request is valid.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access read`.

**Data Types:** `Boolean`

### **wr\_ready** — Write ready signal boolean scalar

Write ready signal, returned as a Boolean scalar. It corresponds to the
backpressure from the slave IP core or external memory. When this value is
`1` (`high`), it indicates that data can be sent.
When this value is `0` (`low`), it indicates that
the hardware logic must stop sending data within one clock cycle.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `Boolean`

### **wr\_bvalid** — Write valid signal boolean scalar

Write valid signal, returned as a Boolean scalar. It is the response signal from
the slave IP core that you can use for diagnosis purposes. This value becomes
`1` (`high`) after the AXI4 interconnect accepts
each burst transaction.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `Boolean`

### **wr\_complete** — Write transaction complete boolean scalar

Write transaction complete, specified as a Boolean scalar. It is the control
signal that when remains high for one clock cycle indicates that the write transaction
has completed. This signal asserts at the last `wr_bvalid` of the
burst.

#### Dependencies

To enable this port, set the **Control protocol** parameter to
`Random access write`.

**Data Types:** `Boolean`

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

The output ports of the block vary based on the type of **Control
protocol** and **Control type** that you select. For more
details, see Description.

### **Control type** — Control type selection `Valid` (default) | `Ready`

Specify the type of control.

The output ports of the block vary based on the type of **Control
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

Convert bus to control signals

The SoC Bus Selector block converts a set of control signals from a bus.
The block accepts a bus and outputs control signals.

You can configure this block to support multiple protocol interface types. Parameter and
port configurations for this block vary based on your desired protocol interface type and mode
of operation, as outlined in this table.

| Protocol Interface Type | Mode of Operation | Parameter Configuration | Enabled Output Ports |
| --- | --- | --- | --- |
| Data stream | Read stream data | Set **Control protocol** to `Data stream` and **Control type** to `Valid`. | **valid** |
| **tlast** |
| Write stream data | Set **Control protocol** to `Data stream` and **Control type** to `Ready`. | **ready** |
| Pixel stream | Read video stream | Set **Control protocol** to `Pixel stream` and **Control type** to `Valid`. | **hStart** |
| **hEnd** |
| **vStart** |
| **vEnd** |
| **valid** |
| Write video stream | Set **Control protocol** to `Pixel stream` and **Control type** to `Ready`. | **ready** |
| Random access read | Read data | Set **Control protocol** to `Random access read` and **Control type** to `Valid`. | **rd\_aready** |
| **rd\_dvalid** |
| Random access write | Write data | Set **Control protocol** to `Random access write` and **Control type** to `Ready`. | **wr\_ready** |
| **wr\_bvalid** |
| **wr\_complete** |
