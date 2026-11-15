---
type: simulink-block
title: 'UDP Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpread'
documentation_source_path: 'ref/udpread.html'
language: en
---

# UDP Read

## Ports

### Input

### **msg** — UDP packet numeric vector

This message port receives UDP packets, as messages, from a connected IO Data Source
block. The messages process when the Task Manager
block triggers task containing the UDP Read block. For more information
on messages, see Messages.

**Note**

This input is used only during simulation. and does nothing in code generation
and external mode simulation.

**Data Types:** `SoCData`
### Output

### **data** — Output UDP packet numeric vector

Output UDP packet, received from a remote host, returned as a numeric
vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **length** — Length of received UDP packet nonnegative scalar

Length of output UDP packet returned on the output **data**
port.

**Data Types:** `uint32`

## Parameters

### **Local port** — IP port number of local host `25000` (default) | integer from 1 to 65,535

Specify the port number of the application on target in which you want to receive
data. Match the local IP port number with the remote IP port number of the remote
host.

### **Data type** — Data type of received data uint8 (default) | single | double | int8 | int16 | int32 | uint16 | uint32

Select the type of data the block receives from the sending host. Match the data
type with data type of input data.

### **Maximum data length (elements)** — Maximum length of output UDP packet `1` (default) | positive integer

Specify the maximum number of data elements that the output
**data** port can produce at every time step.

### **Receive buffer size (bytes)** — Number of data bytes in received data `65535` (default) | integer from 1 to 65,535

Specify the maximum number of data bytes that the block can receive at each time
step.

### **Enable event-based execution** — Enable or disable event-based task execution `off` (default) | `on`

To generate event-driven code, select this parameter. To generate timer-driven code,
clear this parameter.

When **Enable event-based execution** is selected, the block reads
data from the socket buffer whenever any UDP data is received in the socket buffer
irrespective of the sample time. When **Enable event-based execution**
is cleared, the block reads available UDP data from the socket buffer at each sample
time. To set the size of the data that the block can read from the socket buffer,
specify the size in the **Receive buffer size** parameter.

### **Sample time** — Sample time `-1` (default) | nonnegative scalar

Specify how often the scheduler runs this block. If this value is
`-1` (default), the scheduler assigns the sample time for the
block.

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

Embedded Coder generates event-driven or timer-driven code for
this block, based on the **Enable event-based execution** parameter
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

Receive UDP packets from remote host

The UDP Read block receives UDP (User Datagram Protocol) packets from a
remote host on the application on target. The remote host is the computer or hardware from
which you want to receive UDP packets. The block reads UDP packets from UDP socket buffer and
returns the UDP packets as a one-dimensional array.
