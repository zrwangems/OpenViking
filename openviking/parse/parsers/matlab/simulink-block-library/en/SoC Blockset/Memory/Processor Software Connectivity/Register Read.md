---
type: simulink-block
title: 'Register Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'registerread'
documentation_source_path: 'ref/registerread.html'
language: en
---

# Register Read

## Ports

### Input

### **msg** — Data message from register scalar

This message port receives data messages from a connected Register
Channel or IO Data Source
block. The messages process when the Task Manager
block triggers task containing the Register Read block. For more
information on messages, see Messages.

**Data Types:** `SoCData`
### Output

### **data** — Output signal vector

This port emits the data vector read from the specified registers in the Register
Channel starting at **Offset address** from the base
address of the IP core.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Device name** — Path and file name of IP core device `/dev/mwipcore` (default) | character array

Enter the path and file name of the IP core device.

### **Offset address** — Offset from the base address of the IP core to the register `hex2dec('0100')` (default) | positive integer

Enter the offset from the base address of the IP core to the register. The block
reads data from this register. Use the `hex2dec` function when you specify the offset address using a hexadecimal
number expressed as a character vector. The offset address can be selected using the
Hardware Mapping
tool.

### **Output data type** — Data type used by IP core uint32 (default) | single | int8 | uint8 | int16 | int32 | uint32 | boolean | fixed-point

Enter the data type used by the IP core.

### **Output vector size** — Size of data vector from IP core `1` (default) | positive integer

Enter the size of the data vector read from the IP core device.

### **Sample time** — Sample time `0.1` (default) | positive number

Enter the sample time in seconds. Either the connected Register Channel
or IO Data Source
blocks get polled at this rate when this block is used in a timer-driven task.

## Libraries

SoC Blockset / Processor I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

SoC Builder implements the Register Read block with FPGA and processor
IPs that use the AXI4 interface protocol. The AXI4 interface protocol allows the processor
algorithm to read vector data from a contiguous group of registers on the FPGA. Use this
block for simple, low-throughput memory-mapped communication, such as reading from control
and status registers. This diagram shows a generalized representation of the generated code
implementation.

## Version History

**Introduced in R2019a**

## Description

Read data from a register region on the specified IP core

The Register Read block reads data from a register region on the specified
IP core. In simulation, a timer-driven or event-driven task subsystem contains the
Register Read block. The data signals from the Register Read
block connect to the Register Channel block
managing those registers and their transactions.

When developing or analyzing the software side of an SoC application, the Register
Read block can be connected to an IO Data Source block.
In this configuration, the IO Data Source block provides either previously
recorded or artificial data, enabling a more directed simulation of the software and processor
side of the application, without need to explicitly model the hardware and memory
interactions.
