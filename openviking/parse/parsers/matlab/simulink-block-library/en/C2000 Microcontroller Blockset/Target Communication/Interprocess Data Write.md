---
type: simulink-block
title: 'Interprocess Data Write'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Target Communication'
documentation_page: 'interprocessdatawrite'
documentation_source_path: 'ref/interprocessdatawrite.html'
language: en
---

# Interprocess Data Write

## Ports

### Input

### **data** — Data input vector

This port receives a data vector to send to another processor over the
interprocess data channel.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **msg** — Output data message scalar

This message port sends the output data as a message to the connected Interprocess
Data Channel block. For more information on messages, see Messages.

#### Dependencies

This port appears only when **Enable simulation port**
parameter is enabled.

**Data Types:** `SoCData`

## Parameters

### **Enable simulation port** — Enable peripheral simulation port to block `on` (default) | `off`

Select this parameter to configure the **msg** output port to
enable peripheral simulation capability.

### **Channels number** — Select the channel number `0` (default) | `1` | `2` | `...`

Select the channel where you want to send the data.

#### Dependencies

This parameter is visible only when you disable the **Enable simulation
port** parameter.

### **Circular FIFO depth** — Number of storage buffers `1` (default) | positive integer

Buffers are circular buffers created in shared message RAM. Number of buffer is the
number of elements stored at a time in the shared message RAM. These are not FIFO but
will be overwritten at next instance.

Ensure that the number of buffers specified must same at both the Tx and Rx
side.

#### Dependencies

This parameter is visible only when you disable the **Enable simulation
port** parameter.

### **Trigger interrupt on receiving core** — Select to trigger interrupt `off` (default) | `on`

Select this parameter to trigger IPC interrupt at the receiving core.

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

## Libraries

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Send messages to another processor using interprocessor data write

The Interprocess Data Write block asynchronously sends messages to another processor in an
SoC using an interprocess data channel. The Interprocess Data Write block connects to an
Interprocess Data Channel block that similarly connects to an Interprocess Data Read block
contained in a separate processor reference model. In simulation, data from the current
processor is asynchronously sent and processed in the processor containing the Interprocess
Data Read block and associated asynchronous task. This diagram shows a generalized view of the
interprocess data channel.

**Note**

- Ensure that the number of buffers specified must same at both the Tx and Rx
  side.
- If you are using multiprocessor modeling approach with single model triggering
  multiple cores using Task manager, use the Interprocess Data Read and Interprocess
  Data Write blocks to send and receive data between cores.

  Use IPC Receive and IPC Transmit blocks to receive or sent data
  to either core for multi-core processors. Use these blocks for flat model approach
  where you are using separate models for each core.

  To help you choose the right solution for your application, see
  Communication Between Cores Using IPC Blocks for the detailed
  comparison between the IPC Transmit/Receive blocks and Interprocess Data Read/Write
  blocks

Interprocess data channel diagram.
