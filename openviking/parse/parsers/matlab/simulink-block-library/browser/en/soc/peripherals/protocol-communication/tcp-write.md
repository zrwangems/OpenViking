---
type: simulink-block
title: 'TCP Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'tcpwrite'
documentation_source_path: 'ref/tcpwrite.html'
language: en
---

# TCP Write

## Ports

### Input

### **data** — Input data numeric vector

Input data, specified as a numeric vector. The block sends this data over a TCP/IP
network to the remote host.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **msg** — Stream of TCP/IP packets sent to the remote host scalar

This message port sends TCP/IP packets, as messages, to a connected IO Data Sink
block. For more information on messages, see Messages.

**Note**

This output is used only during simulation. and does nothing in code generation
and external mode simulation.

**Data Types:** `SoCData`

## Parameters

### **Network role** — Set the block as server or client `Client` (default) | `Server`

To configure this block as a TCP/IP client or server, set this parameter to
`Client` or `Server`,
respectively.

When you set this parameter to `Client`, you must provide
the remote IP address and remote IP port number of the TCP/IP server to which you want
to send TCP/IP packets. Specify this information by using the **Remote
address** and **Remote port** parameters.

When you set this parameter to `Server`, you must provide
the local IP port number, which acts as the listening port of the TCP/IP server running
in the hardware. Specify this information using the **Local port**
parameter.

### **Remote address** — IP address of remote server to which TCP/IP packets are sent `127.0.0.1` (default) | dotted-quad expression

Specify the IP address of the remote server to which you want to send TCP/IP
packets.

#### Dependencies

To enable this parameter, set the **Network role** parameter to
`Client`.

### **Remote port** — IP port of remote server to which TCP/IP packets are sent `25000` (default) | integer from 1 to 65,535

Specify the port number of the remote server to which you want to send TCP/IP
packets.

#### Dependencies

To enable this parameter, set the **Network role** parameter to
`Client`.

### **Local port** — IP port on sending host from which TCP/IP packets are sent `-1` (default) | integer from 1 to 65535

When the **Network role** parameter is set to
`Client`, specify the IP port number of the application from
which you want to send TCP/IP packets. The default value `-1`, sets
this IP port number to a random available port number and uses that port to send the
packets.

When the **Network role** parameter is set to
`Server`, this local port acts as the listing port of the
TCP/IP server running in the hardware. In this case, specify a value from 1 to 65,535
for this parameter.

### **Byte order** — Byte order `LittleEndian` (default) | `BigEndian`

Byte order of the TCP/IP packets, specified as one of these values:

- `LittleEndian` — Sets the byte order of TCP/IP packets to
  little endian.
- `BigEndian` — Sets the byte order of TCP/IP packets to big
  endian.

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

Embedded Coder generates event driven code for this block. This
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

Send TCP/IP packets to remote host over TCP/IP network

The TCP Write block sends TCP/IP packets to a remote host over a TCP/IP
(Transmission Control Protocol/Internet Protocol) network.
