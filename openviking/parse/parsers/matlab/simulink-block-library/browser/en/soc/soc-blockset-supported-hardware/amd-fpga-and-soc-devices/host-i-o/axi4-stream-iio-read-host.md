---
type: simulink-block
title: 'AXI4-Stream IIO Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4streamiioreadhost'
documentation_source_path: 'ref/axi4streamiioreadhost.html'
language: en
---

# AXI4-Stream IIO Read (HOST)

## Ports

### Output

### **data** — Data frame from DMA buffer vector

This port outputs the *N*-by-1 vector received from the DMA
buffer transfer. Use the **Frame size** parameter to set the number
of samples read for each DMA transfer.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`

### **valid** — Valid data frame from DMA buffer scalar

A flag indicating a valid data frame read from the memory channel.

#### Dependencies

To enable this port, set the **Timeout (sec)** parameter to a
finite value.

**Data Types:** `Boolean`

## Parameters

### **Device name** — Name of IP core device `mwipcore0:s2mm0` (default) | IP core name and channel

Enter the name and channel of the IP core on the FPGA as a colon-separated
list.

**Note**

If you are using HDL Coder to generate the IP core, HDL Coder maps the IP core to `mwipcore0` and uses channel
`s2mm0`.

### **Remote IP address** — Network address of SoC device `192.168.1.101` (default) | valid URI string

Enter the network address of the connected SoC device.

**Example:** `10.0.0.201`

### **Timeout (sec)** — Timeout for DMA stream read `Inf` (default) | positive scalar

Specify the maximum timeout delay for the DMA stream read.

### **Output data type** — Data type of IP core on device `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(0,128,0)`

Select the data type used by the IP core on the device.

### **Frame size** — Size of data vector to be read from IP core `1024` (default) | positive integer

Enter the size of the data vector to be read from the IP core device.

### **Sample time** — Sample time in seconds `0.1` (default) | positive scalar

The signal data output by the AXI4-Stream IIO Read blocks polls from the DMA buffer
using the AXI4-Stream protocol. The **Sample time** or base-rate of the
subsystem specifies the polling rate of the DMA buffer.

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

Read DDR memory buffer from IP core device into simulation model

The AXI4-Stream IIO Read (HOST) block reads data from the
direct-memory-access (DMA) buffer of the specified AXI4-Stream IP core device on a connected
Xilinx® SoC device to a running Simulink® model. This block enables low-latency high-throughput data transmission between
your simulation model and the IP core on the SoC device.

The AXI4-Stream IIO Read (HOST) block receives a copy of the DDR memory
buffer from the SoC device on the host computer. This block uses the Industrial I/O (IIO)
library driver to create a network server daemon on the SoC device and client host computer to
pass the buffer data copies to the host computer running the simulated portion of the model.
This diagram shows the connection between the HDL Coder™ generated IP core, DDR memory buffer, and communication bridge to the running
Simulink model.

AXI4-Stream IIO Read diagram
