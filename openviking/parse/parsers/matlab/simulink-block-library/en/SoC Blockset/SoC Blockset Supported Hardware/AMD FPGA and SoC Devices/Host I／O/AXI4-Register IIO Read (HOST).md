---
type: simulink-block
title: 'AXI4-Register IIO Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4registeriioreadhost'
documentation_source_path: 'ref/axi4registeriioreadhost.html'
language: en
---

# AXI4-Register IIO Read (HOST)

## Ports

### Output

### **data** — Data from IP core registers vector

This block outputs the *N*-by-1 vector read from memory-mapped
registers on the IP core, starting from the **Register
offset**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Device name** — Path and name of IP core device `mwipcore0:mmrd0` (default)

Enter the path and name of the IP core.

**Note**

If you use HDL Coder™ to generate the IP core, HDL Coder maps the IP core to `mwipcore0:mmrd0`.

### **Address offset** — Offset of register from base address of IP core `hex2dec('0100')` (default)

Enter the offset of the register from the base address of the IP core on the device.
The block reads data from this register. Use the `hex2dec` function when you specify the address offset using a hexadecimal
number character vector.

**Note**

If you use HDL Coder to generate the IP core, you can get the value of the address offset
from the “Register Address Mapping” section of Custom IP Core Report (HDL Coder). For more information, see Register Address Mapping (HDL Coder).

### **Remote IP address** — Network address of SoC device `192.168.1.101` (default) | network address

Enter the network address of the connected SoC device.

**Example:** `10.0.0.201`

### **Timeout (sec)** — Timeout for register read `Inf` (default) | positive scalar

Specify the maximum time out delay for the register read.

### **Output data type** — Data type of IP core on the device `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

Select the data type used by the IP core on the device.

### **Sample time** — Sample time in seconds `0.001` (default) | positive scalar

The signal data output by the AXI4-Register IIO Read (HOST) block
polls directly from the IP core using AXI4-Lite protocol. The **Sample
time** parameter value or the base-rate of the subsystem specifies the
polling rate of the registers.

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

Read memory-mapped registers into simulation model

The AXI4-Register IIO Read (HOST) block reads value from memory-mapped
registers in the programmable logic of the connected Xilinx® SoC device to a running Simulink® model on the host computer. This block enables low-latency high-throughput data
transmission between your simulation model and the FPGA registers on the SoC device.

The AXI4-Register IIO Read (HOST) block receives a copy of the
memory-mapped registers from the programmable logic in the SoC device on the host computer.
This block uses the Industrial I/O (IIO) library driver to create a network server daemon on
the SoC device and client host computer to pass the register data copies to the host computer
running the simulated portion of the model. This diagram shows the connection between the
memory-mapped registers, central interconnect, and communication bridge to the running
Simulink model.

AXI4-Register IIO Read (HOST) diagram
