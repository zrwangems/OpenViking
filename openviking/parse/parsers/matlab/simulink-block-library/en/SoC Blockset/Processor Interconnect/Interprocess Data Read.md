---
type: simulink-block
title: 'Interprocess Data Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Interconnect'
documentation_page: 'interprocessdataread'
documentation_source_path: 'ref/interprocessdataread.html'
language: en
---

# Interprocess Data Read

## Ports

### Input

### **msg** — Data message from interprocess data channel scalar

This message port receives data messages from the connected Interprocess Data
Channel block. The messages process when the Task Manager block triggers the task
containing the this block. For more information on messages, see Messages.

#### Dependencies

This port appears only when **Enable simulation port**
parameter is enabled.

**Data Types:** `SoCData`
### Output

### **data** — Data frame read from another processor vector

This port emits a data frame read from another processor connected via the
Interprocess data Channel block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`

### **status** — Interprocess data read status 0 | 1 | 2 | 4 | 6

The status port outputs one of these values:

- `0—`No errors
- `1—`Data not available
- `2—`Data type mismatch
- `4—`Data length mismatch
- `6—`Data type and Data length mismatch

#### Dependencies

This port appears when you disable the **Enable simulation
port** parameter.

## Parameters

### **Enable simulation port** — Enable peripheral simulation port to block `on` (default) | `off`

Select this parameter to configure the **msg** output port to
enable peripheral simulation capability.

### **Data type** — Data type of interprocess data channel `double` (default) | `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

Enter the data type used by the interprocess data channel.

You can selectively show or hide the **Data Type
Assistant** options by clicking >> button or << button. For more
information, refer to Specify Data Types Using Data Type Assistant.

### **Circular FIFO depth** — Number of storage buffers `1` (default) | positive integer

Buffers are circular buffers created in shared message RAM. Number of buffer is the
number of elements stored at a time in the shared message RAM. These are not FIFO but
will be overwritten at next instance.

Ensure that the number of buffers specified must same at both the Tx and Rx
side.

#### Dependencies

This parameter is visible only when you disable the **Enable simulation
port** parameter.

### **Circular FIFO element size** — Size of data vector read from interprocess data channel `1` (default) | positive integer

Enter the circular FIFO element size of the data vector read from the interprocess
data channel.

### **Channel number** — Select the channel number `0` (default) | `1` | `2` | `...`

Select the channel where you want to send the data.

#### Dependencies

This parameter is visible only when you disable the **Enable simulation
port** parameter.

### **Participating cores** — Select the participating cores of the processor `The options vary based on the hardware board you select`

Select the participating cores as per the **Hardware board** you
select in the Configuration Parameters window.

#### Dependencies

This parameter is visible only when you disable the **Enable simulation
port** parameter.

**Note**

Ensure that **Channel number**, **Number of
buffers** and **Participating cores** parameters match
for the corresponding Interprocess Data Read and Interprocess Data Write blocks of
the model.

### **Sample time** — Sample time `-1` (default) | positive scalar

Enter the sample time of the block to apply to the timer-driven task
subsystem.

## Libraries

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Receive messages from another processor using interprocess communication channel

The Interprocess data Read block asynchronously receives messages from another processor
in an SoC using an interprocess data channel. The Interprocess Data Read block connects to an
Interprocess Data Channel block that similarly connects to an Interprocess Data Write block
contained in a separate processor reference model. In simulation, data from another processor
is asynchronously received and processed in the processor containing the Interprocess Data
Read block and associated asynchronous task. This diagram shows a generalized view of the
interprocessor data channel connection.

**Note**

- Ensure that the number of buffers specified must same at both the Tx and Rx
  side.
- If you are using multiprocessor modeling approach with single model triggering
  multiple cores using Task manager, use the Interprocess Data Read and Interprocess
  Data Write blocks to send and receive data between cores.

Interprocess data channel diagram.
