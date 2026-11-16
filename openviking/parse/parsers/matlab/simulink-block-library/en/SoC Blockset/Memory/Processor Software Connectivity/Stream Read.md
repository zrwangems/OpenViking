---
type: simulink-block
title: 'Stream Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'streamread'
documentation_source_path: 'ref/streamread.html'
language: en
---

# Stream Read

## Ports

### Output

### **data** — Data frame from shared memory vector

This port emits a data frame read from shared a region of shared memory defined in
the Memory Channel
block.

**Data Types:** `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

### **valid** — Valid frame data scalar

A flag indicating a valid data frame read from the memory channel.

**Data Types:** `Boolean`

### **done** — Notification message of completed read scalar

This message port sends notification, as a message, to the connected Memory Channel
or IO Data Source
block that the read completed. For more information on messages, see Messages.

**Data Types:** `Boolean`
### Input

### **msg** — Data message from memory scalar

This message port receives data messages from the connected Memory Channel
or IO Data Source
block. The messages process when the Task Manager
block triggers the task containing the Stream Read block. For more
information on messages, see Messages.

**Data Types:** `SoCData`

## Parameters

#### Main

### **Device name** — Name of IP core device `ip:s2mm0` (default) | colon-separated list of IP core name and channel

Enter the name and channel of the IP core on the FPGA as a colon separated
list.

### **Output data type** — Data type of IP core `uint32` (default) | `uint16` | `uint64` | `fixdt(0,128,0)`

Enter the data type used by the memory channel.

### **Samples per frame** — Size of data vector read from IP core `1024` (default) | positive scalar integer

Enter the size of the data vector read from the memory channel.

### **Number of buffers** — Number of data buffers `16` (default) | positive integer

Enter the number of data frame buffers in physical memory. This number should match
the **Number of buffers** parameter in the Memory
Channel block or IO Data Source block.

### **Enable event-based execution** — Enable event-driven task execution `on` (default) | `off`

To use this block in event-driven task subsystems, select this parameter. To use
this block in timer-driven task subsystems, clear this parameter.

When **Enable event-based execution** is selected, this block reads
from the Memory Channel
each time a full buffer is available in the shared memory region. When
**Enable event-based execution** is cleared, the block reads the data
in the shared memory region at each sample time.

### **Sample time** — Sample time in seconds `-1` (default) | positive scalar

Enter the sample time used by the timer-driven task subsystem when the
**Enable event-based execution** is cleared.

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

The SoC Builder tool implements the Stream Read,
Stream Write, Memory Channel, and Task
Manager blocks with FPGA and processor IPs that use the AXI4-stream communication
protocol. The AXI4-stream protocol uses a direct memory access (DMA) to read a data vector
to a shared region on the external memory. This protocol enables high-speed streaming of
data between the FPGA and the embedded processor through external memory. This diagram shows
a generalized representation of the generated code implementation.

## Version History

**Introduced in R2019a**

## Description

Stream data from shared memory to processor algorithms

The Stream Read block streams data from shared memory in the memory channel
to your processor algorithm. In simulation, a timer-driven or event-driven task subsystem
contains the Stream Read block. The data signals from the Memory Channel block
connect to the Stream Read block. Following a write to the shared memory, the
Memory Channel notifies the Task Manager block of
the write event. The Task Manager block then triggers the event-driven
subsystem containing the Stream Read block and associated algorithm.

When developing or analyzing the software side of an SoC application, the Stream
Read block can be connected to an IO Data Source block.
In this configuration, the IO Data Source block provides either previously
recorded or artificial data, enabling a more directed simulation of the software and processor
side of the application, without need to explicitly model the hardware and memory
interactions.
