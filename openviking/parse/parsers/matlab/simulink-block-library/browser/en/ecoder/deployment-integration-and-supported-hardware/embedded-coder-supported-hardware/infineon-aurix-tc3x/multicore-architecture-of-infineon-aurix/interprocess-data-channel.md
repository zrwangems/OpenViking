---
type: simulink-block
title: 'Interprocess Data Channel'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / Interprocess Data Communication'
documentation_page: 'interprocessdatachannel'
documentation_source_path: 'ref/interprocessdatachannel.html'
language: en
---

# Interprocess Data Channel

## Ports

### Input

### **datain** — Input data message scalar

This message port receives input data as a message from a connected Interprocess
Data Write block. For more information on messages, see Messages.

**Data Types:** `SoCData`
### Output

### **dataout** — Output data message scalar

This message port sends output data as a message to a connected Interprocess Data
Read block. For more information on messages, see Messages.

**Data Types:** `SoCData`

### **overwritten** — Output overwrite notification signal scalar

This port sends a true signal output whenever an overwrite of the internal buffer
queue occurs. When the connected processor model executes in external mode, the
connected Interprocess Data Write block generates the **overwritten**
signal in the Simulation Data
Inspector tool.

#### Dependencies

To enable this port, select the **Show when buffer is
overwritten** parameter.

**Data Types:** `Boolean`

### **used** — Output number of buffers in use scalar

This port outputs the number of buffers currently in use in the block's internal
buffer queue. When the connected processor model executes in external mode, the
connected Interprocess Data Write block generates the **used** signal
in the Simulation Data
Inspector tool.

#### Dependencies

To enable this port, select the **Show number of used buffers**
parameter.

**Data Types:** `Boolean`

### **event** — Task event signal scalar

This port sends a task event signal that triggers the Task Manager block to
execute the associated event-driven task.

#### Dependencies

To enable this port, select the **Show event port**
parameter.

**Data Types:** `rteEvent`

## Parameters

#### Main

### **Circular FIFO depth** — Number of storage buffers `1` (default) | positive integer

Buffers are circular buffers created in shared message RAM. Number of buffer is the
number of elements stored at a time in the shared message RAM. These are not FIFO but
will be overwritten at next instance.

### **Propagation delay** — Propagation delay of data through the channel `1e-6` (default) | non-negative number

Specify the propagation delay of data transfers through the this block. To ignore
propagation delays, set this parameter to `0`.

### **Show event port** — Option to enable task event ports `off` (default) | `on`

Enable an event port that, when connected to the Task Manager block, can execute
event-driven tasks.

#### Statistics

### **Show number of used circular FIFO** — Option to enable circular FIFO count ports `off` (default) | `on`

Enable an output port that shows the current number of circular FIFO used in the
Interprocess Data Channel block internal buffer queue.

### **Show when circular FIFO is overwritten** — Enable port that shows circular FIFO overwrites `off` (default) | `on`

Enable an output port that signals when an overwrite of the Interprocess Data
Channel block internal circular FIFO queue occurred.

## Libraries

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Model interprocessor data channel between two processors

The Interprocess Data Channel block simulates the interprocessor data channel available in
multiprocessor or OS managed SoC hardware board families. The block provides a channel for
asynchronous data transfer between two processors. This diagram shows a generalized view of
the interprocessor data connection.

Interprocess data channel diagram.

To generate and execute C code for your SoC models, this block
requires Embedded Coder® Support Package for Infineon®
AURIX™ TC4x Microcontrollers or Embedded Coder Support Package for Infineon
AURIX TC3x Microcontrollers.

**Note**

If you are using multiprocessor modeling approach with single model triggering
multiple cores using Task manager, use the Interprocess Data Read and Interprocess Data
Write blocks to send and receive data between cores.

Use IPC Receive and IPC Transmit blocks to receive or sent data to either core for
multi-core processors. Use these blocks for flat model approach where you are using
separate models for each core.
