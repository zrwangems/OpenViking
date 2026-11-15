---
type: simulink-block
title: 'UDP Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpwrite'
documentation_source_path: 'ref/udpwrite.html'
language: en
---

# UDP Write

## Ports

### Input

### **data** — Input signal numeric vector

Input data, specified as a numeric vector. The block sends this data as UDP packet
to the remote host. To set the byte order in which you want to send this UDP data, set
the **Byte order** parameter. The block converts this input data to
the specified byte order type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **msg** — UDP packet sent to remote host numeric vector

This message port sends UDP packets, as messages, to a connected IO Data Sink
block. For more information on messages, see Messages.

**Note**

This output is used only during simulation. and does nothing in code generation
and external mode simulation.

**Data Types:** `SoCData`

## Parameters

### **Remote IP address (255.255.255.255 for broadcast)** — IP address of remote host to which data is sent `127.0.0.1` (default) | dotted-quad expression

Specify the remote IP address of the host to which you want to send UDP
packets.

### **Remote port** — IP port of remote host to which data is sent `25000` (default) | integer from 1 to 65,535

Specify the port number of the host to which you want to send UDP packets.

### **Local port** — IP port number of application on target from which data is sent `-1` (default) | integer from 1 to 65,535

Specify the port number of the application on the target from which you want to send
the UDP packets. The default value `-1`, sets the local port number to
a random available port number and uses that port to send the UDP packets.

### **Byte order** — Byte order `LittleEndian` (default) | `BigEndian`

Byte order of the UDP packets, specified as one of these values:

- `LittleEndian` — Sets the byte order of UDP packets to little
  endian.
- `BigEndian` — Sets the byte order of UDP packets to big
  endian.

## Libraries

SoC Blockset / Processor I/O SoC Blockset / Host I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

Embedded Coder generates event-driven code for this block. This
diagram shows a generalized representation of the generated code implementation.

**Note**

Timing measurements from generated code might vary within the execution of a task
instance compared to the timing of tasks in simulation. You can configure your model to
use data caching in task signals to reach improved agreement between the simulation and
generated code. For more information, see Value and Caching of Task
Subsystem Signals.

## Version History

**Introduced in R2019a**

## Description

Send UDP packets to remote host

The UDP Write block sends UDP (User Datagram Protocol) packets from the
application on target to a remote host. The remote host is the computer or hardware to which
you want to send UDP packets.
