---
type: simulink-block
title: 'AXI4-Stream IIO Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4streamiiowritehost'
documentation_source_path: 'ref/axi4streamiiowritehost.html'
language: en
---

# AXI4-Stream IIO Write (HOST)

## Ports

### Input

### **data** — Data frame to DMA buffer vector

This port takes an *N*-by-1 vector and writes to the memory in
the DDR via a DMA buffer transfer.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`
### Output

### **status** — Status of stream write to IP core in SoC device scalar

This port outputs a validation flag indicating a successful write of the data to
the IP core in the SoC device. A value of `1` indicates a successful
write.

#### Dependencies

To enable this port, set the **Data timeout (seconds)**
parameter to a finite value.

**Data Types:** `Boolean`

## Parameters

### **Device name** — Name of IP core device `mwipcore0:mm2s0` (default) | IP core name and channel

Enter the name and channel of the IP core on the FPGA as a colon-separated
list.

**Note**

If you are using HDL Coder to generate the IP core, HDL Coder maps the IP core to `mwipcore0` and uses channel
`s2mm0`.

### **Remote IP address** — Network address of SoC device `192.168.1.101` (default) | valid URI string

Enter the network address of the connected SoC device.

**Example:** `10.0.0.201`

### **Data timeout (seconds)** — Timeout for DMA stream write `Inf` (default) | positive scalar

Specify the maximum timeout delay for the DMA stream write.

### **Enable simulation I/O** — Read and write data from board on (default) | off

When connected to a board, this block writes data directly to the board. When used
in a simulation environment, clear this parameter to enable simulation without error due
to lack of IIO connection. When cleared, the data displayed in the
**data** output port does not reflect actual data.

## Libraries

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Write arrays to DDR memory buffer of IP core device from simulation model

The AXI4-Stream IIO Write (HOST) block writes data to the
direct-memory-access (DMA) buffer of the specified AXI4-Stream IP core device on a connected
Xilinx® SoC device from a running Simulink® model. This block enables low-latency high-throughput data transmission between
your simulation model and the IP core on the SoC device.

The AXI4-Stream IIO Write (HOST) block sends a data on the host computer to
the DDR memory buffer on the SoC device. This block uses the Industrial I/O (IIO) library
driver to create a network server daemon on the SoC device and client host computer to pass
the buffer data copies to the host computer running the simulated portion of the model. This
diagram shows the connection between the HDL Coder™ generated IP core, DDR memory buffer, and communication bridge to the running
Simulink model.

AXI4-Stream IIO Write (HOST) diagram
