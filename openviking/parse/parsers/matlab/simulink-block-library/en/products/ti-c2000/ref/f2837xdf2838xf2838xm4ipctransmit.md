---
type: simulink-block
title: 'F2837xD/F2838x/F2838x-M4 IPC Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / F2837x/F2838x IPC (Flat Model Semantics)'
documentation_page: 'f2837xdf2838xf2838xm4ipctransmit'
documentation_source_path: 'ref/f2837xdf2838xf2838xm4ipctransmit.html'
language: en
---

# F2837xD/F2838x/F2838x-M4 IPC Transmit

## Ports

### Input

### **Input** — Data to be send to the other Core uint16 | single | int8 | uint8 | int16 | int32 | uint32 | boolean

The port accepts data to be transmitted to the other Core as a vector or
scalar.

## Parameters

### **Destination** — Destination selected to send data `C28x (CPU1/CPU2)/CPU1` (default) | `ARM Cortex-M4 (CM)/CPU2`

The destination to which you want to send data. The destination selection is based
on the processor you choose. For F2838x(C28x) processor, the destination is either
C28x (CPU1/CPU2) or ARM Cortex-M4 (CM). For F2838x-M4 ARM core processor, the
destination is CPU1 or CPU2.

The IPC Transmit block mask displays the current destination and the channel
selected. For example, if the block displays `C28x_Ch0`, then the
destination is `C28x (CPU1/CPU2)` and channel is
`0`. Similarly if the IPC Transmit block displays
`CM_Ch1`, then the destination is `ARM Cortex-M4
(CM)` and channel is `1`.

**Note**

This parameter is only available for F2838x(C28x) and F2838x-M4 ARM core
processors.

### **Channel** — Channel selected to transmit data `0` (default) | `0–31`

The channel from which you want to transmit data. Each channel is a separate
memory location in the shared memory.

**Note**

The transmitter and receiver have 32 channels each to transmit and receive data.
For data transmission and reception, the transmitter and receiver must be set to the
same channel number.

### **Enable blocking** — Specify if Core must wait until sent data is read `off` (default) | on

When enabled, after sending data, the Core waits until the other Core reads the
data.

## Libraries

C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Transmit data to either core while using separate model for each core

The IPC Transmit block transmits data from one Core to the other.

**Note**

Use IPC Receive and IPC Transmit blocks to receive or sent data to either core for
multi-core processors. Use these blocks for flat model approach where you are using
separate models for each core.

If you are using multiprocessor modeling approach with single model triggering
multiple cores using Task Manager, use the Interprocess Data Read and Interprocess Data Write blocks to send and
receive data between cores.

Core1 transmits data to its allocated memory (Core1-to-Core2 Message RAM) and receives
data from the allocated memory of Core2 (Core2-to-Core1 Message RAM). Similarly Core2
transmits data to its allocated memory (Core2-to-Core1 Message RAM) and receives data from
allocated memory of Core1 (Core1-to-Core2 Message RAM). For F2838xD, Core1/Core2 can be
CPU1,CPU2 or ARM Cortex-M4 (CM) and for F2837xD, Core1/Core2 can be CPU1 or CPU2.

If Core1 and Core2 are both C28x core, then the data and channel structure between two
cores are allocated in Message RAM and the data array is allocated in Global Shared RAM. In
C28x core, by default all the channel structures are created in Message RAM.

However, if one of the core is ARM Cortex M4 (applicable only for F2838x), then the data
array is allocated only using Message RAM as global shared RAM is not available between
cores. In order to accommodate more data, only required channel structures are created in
Message RAM. Hence if the channel number used for transmit block in one core does not match
with the receive block in other core the data transmission will not occur.

For more information on how the memory is allocated for IPC block, see Memory Allocation for IPC Flat Models
