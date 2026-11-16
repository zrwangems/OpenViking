---
type: simulink-block
title: 'Register Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'registerwrite'
documentation_source_path: 'ref/registerwrite.html'
language: en
---

# Register Write

## Ports

### Input

### **data** — Data input vector

This port receives the data vector to write to the registers on the IP core
starting at **Offset address** from the base address of the IP
core.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **msg** — Output register data message scalar

This message port sends the output register data, as a message, to the connected
Register
Channel or IO Data Sink
block. For more information on messages, see Messages.

**Data Types:** `SoCData`

## Parameters

### **Output sink** — Direct output to port or base workspace `To output port` (default) | `Base workspace` | `IP core register`

Select `To output port` to write data to the output port,
`msg`. Select `Base workspace` to write data to a
variable in the base workspace. When writing to the base workspace, the block updates
the value of a `Simulink.Parameter` object with name set
by `Simulink.Parameter object name` parameter in the base workspace.
Select `IP core register` to write to an IP Core Register
Read block with the same `Register name` parameter.

**Note**

Placing the Register Write block inside a Initialize Function block subsystem, writes to a
`Simulink.Parameter` object at the start of simulation. A register,
represented as a Constant block, in an FPGA reference
model can be initialized at the start of simulation with the value of the
`Simulink.Parameter` object. This method of writing to FPGA registers
requires a constant value throughout the simulation but can reduce the simulation time
required by your SoC model.

### **Simulink.Parameter object name** — Name of `Simulink.Parameter` object `A` (default) | character vector

Name of `Simulink.Parameter` object to be created
in the `Base workspace`.

**Example:** `A`

#### Dependencies

To enable this parameter, set `Output sink` to `Base
workspace`.

### **Register name** — Name of a register in IP Core `RegA` (default) | character vector

Name of register defined in an IP Core Register Read block located in
the FPGA reference model.

**Example:** `RegA`

#### Dependencies

To enable this parameter, set `Output sink` to `IP core
register`.

### **Device name** — Path and file name of IP core device `/dev/mwipcore` (default) | character array

Enter the path and file name of the IP core device.

### **Offset address** — Offset from the base address of the IP core to the register `hex2dec('0100')` (default) | positive integer

Enter the offset from the base address of the IP core to the register. The block
writes data to this register. Use the `hex2dec` function when you specify the offset address using a hexadecimal
number expressed as a character vector. The offset address can be selected using the
Hardware Mapping
tool.

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

SoC Builder implements the Register Write block with FPGA and processor
IPs that use the AXI4 interface protocol. The AXI4 interface protocol allows the processor
to write vector data from the processor to a contiguous group of registers on the FPGA. Use
this block for simple, low-throughput memory-mapped communication, such as writing to
control and status registers. This diagram shows a generalized representation of the
generated code implementation.

## Version History

**Introduced in R2019a**

## Description

Write data to a register region on the specified IP core

The Register Write block writes data from your processor algorithm to a
register region on the specified IP core. In simulation, a timer-driven or event-driven task
subsystem contains the Register Write block. The data signals from the
Register Write block connect to the Register Channel block
managing those registers and their transactions.

When developing or analyzing the software side of an SoC application, the Register
Write block can be connected to an IO Data Sink block. In
this configuration, the IO Data Sink block provides either previously recorded
or artificial data, enabling a more directed simulation of the software and processor side of
the application, without need to explicitly model the hardware and memory interactions.
