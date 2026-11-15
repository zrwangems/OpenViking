---
type: simulink-block
title: 'AXI4-Register IIO Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4registeriiowritehost'
documentation_source_path: 'ref/axi4registeriiowritehost.html'
language: en
---

# AXI4-Register IIO Write (HOST)

## Ports

### Input

### **data** — Data frame to DMA buffer vector

This port accepts an *N*-by-1 vector written to memory in the DMA
buffer transfer.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix64` | `ufix128`

## Parameters

### **Device name** — File name of IP core device `mwipcore0:mmwr0` (default)

Enter the name and channel of the IP core device on the FPGA as a colon-separated
list. If you are using HDL Coder to generate the IP core, HDL Coder maps the IP core to `mwipcore0` and uses channel
`mm2s0`.

### **Address offset** — Offset of register from base address of IP core `hex2dec('0100')` (default)

Enter the offset of the register from the base address of the IP core on the device.
The block writes data to this register. Use the `hex2dec` function when you specify the address offset using a hexadecimal
number character vector.

**Note**

If you use HDL Coder to generate the IP core, you can get the value of the address offset
from the “Register Address Mapping” section of Custom IP Core Report (HDL Coder). For more information, see Register Address Mapping (HDL Coder).

### **Remote IP address** — Network address of SoC device `192.168.1.101` (default) | valid URI string

Enter the network address of the connected SoC device.

**Example:** `10.0.0.201`

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

Write data to memory-mapped registers from a simulation model

The AXI4-Register IIO Write (HOST) block writes data to memory-mapped
registers in the programmable logic of the connected Xilinx® SoC device from a running Simulink® model on the host computer. This block enables low-latency high-throughput data
transmission between your simulation model and the FPGA registers on the SoC device.

The AXI4-Stream IIO Write (HOST) block sends data on the host computer to
the register in the IP core on the SoC device. This block uses the Industrial I/O (IIO)
library driver to create a network server daemon on the SoC device and host computer to pass
the data between the host computer running the simulated portion of the model. This diagram
shows the connection between the HDL Coder™ generated IP core, memory-mapped register, and communication bridge to the
running Simulink model.

AXI4-Register IIO Write (HOST) diagram
