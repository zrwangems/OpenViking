---
type: simulink-block
title: 'TCP Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'tcpread'
documentation_source_path: 'ref/tcpread.html'
language: en
---

# TCP Read

## Ports

### Input

### **msg** — Stream of TCP/IP packets received from the remote host scalar

This message port receives TCP/IP packets, as messages, from a connected IO Data Source
block. The messages process when the Task Manager
block triggers task containing the TCP Read block. For more information
on messages, see Messages.

**Note**

This input is used only during simulation. and does nothing in code generation
and external mode simulation.

**Data Types:** `SoCData`
### Output

### **data** — TCP/IP packet received from remote host numeric vector

Output TCP/IP packets received from remote host, returned as a numeric vector. The
size and data type of this output is same as the size and data type of the input
message.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **length** — Length of output TCP/IP packet nonnegative scalar

Length of output TCP/IP packets returned on the output **data**
port.

**Data Types:** `uint32`

## Parameters

### **Network role** — Set block as client or server `Client` (default) | `Server`

To configure this block as a TCP/IP client or server, set this parameter to
`Client` or `Server`,
respectively.

When you set this parameter to `Client`, you must provide
the remote IP address and remote IP port number of the TCP/IP server from which you want
to receive TCP/IP packets. Specify this information by using the **Remote
address** and **Remote port** parameters.

When you set this parameter to `Server`, you must provide
the local IP port number, which acts as the listening port of the TCP/IP server running
in the hardware. Specify this information using the **Local port**
parameter. When you set this parameter to `Server`, you can
only connect to one client at a time.

### **Remote address** — IP address of remote server from which TCP/IP packets are received `127.0.0.1` (default) | dotted-quad expression

Specify the IP address of remote server from which you want to receive TCP/IP
packets.

#### Dependencies

To enable this parameter, set the **Network role** parameter to
`Client`.

### **Remote port** — IP port on remote server from which TCP/IP packets are received `25000` (default) | integer from 1 to 65535

Specify the port number of the remote server from which you want to receive TCP/IP
packets.

#### Dependencies

To enable this parameter, set the **Network role** parameter to
`Client`.

### **Local port** — IP port of host on which data is received `-1` (default) | integer from 1 to 65,535

Specify the port number of the application on which you want to receive the TCP/IP
packets when the **Network role** is set to
`Client`. The default value `-1` assigns any
random available port as local port when you set the **Network role**
parameter to `Client`.

This local port acts as the listening port on the TCP/IP server when the
**Network role** is set to `Server`. Specify
a value from 1 to 65535 when you set **Network role** parameter to
`Server`. Specify this local port number as the remote port
number in the sending host from which you want to receive TCP/IP packets.

### **Data type** — Data type of TCP/IP packets received `uint8` (default) | `single` | `double` | `int8` | `int16` | `int32` | `uint16` | `uint32`

Select the data type of the input data. Match this data type with data type of
TCP/IP packets sent from the remote host.

### **Maximum data length (elements)** — Maximum length of output TCP/IP packet `1` (default) | positive scalar

Specify the maximum number of data elements that the output
**data** port can produce at every time step.

### **Enable event-based execution** — Enable event-based task execution off (default) | on

To generate event-driven code, select this parameter. To generate timer-driven code,
clear this parameter.

When **Enable event-based execution** is selected, the block reads
TCP/IP packets from the socket buffer whenever any TCP/IP packet is received in the
socket buffer irrespective of the sample time. When **Enable event-based
execution** is cleared, the block reads available TCP/IP packets from the
socket buffer at each sample time. To set the size of the TCP/IP packet that the block
can read from the socket buffer, specify the size in the **Receive buffer
size** parameter.

### **Sample time** — Sample time `-1` (default) | nonnegative scalar

Specify how often the scheduler runs this block. If this value is
`-1` (default), the scheduler assigns the sample time for the
block.

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

Embedded Coder generates event-driven or timer-driven code for
this block based on the **Enable event-based execution** parameter
selection. This diagram shows a generalized representation of the generated code
implementation.

**Note**

Timing measurements from generated code might vary within the execution of a task
instance compared to the timing of tasks in simulation. You can configure your model to
use data caching in task signals to reach improved agreement between the simulation and
generated code. For more information, see Value and Caching of Task
Subsystem Signals.

## Version History

**Introduced in R2019a**

## Description

Receive TCP/IP packets from remote host over TCP/IP network

The TCP Read block receives a stream of TCP/IP packets from a remote host
over a TCP/IP (Transmission Control Protocol/Internet Protocol) network.
