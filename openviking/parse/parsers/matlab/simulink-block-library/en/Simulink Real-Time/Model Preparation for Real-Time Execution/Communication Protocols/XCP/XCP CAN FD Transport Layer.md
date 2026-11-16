---
type: simulink-block
title: 'XCP CAN FD Transport Layer'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpcanfdtransportlayer'
documentation_source_path: 'io_ref/xcpcanfdtransportlayer.html'
language: en
---

# XCP CAN FD Transport Layer

## Ports

### Input

### **CAN FD Msg** — CAN FD MESSAGE structures being consumed vector

The block input is a Simulink
`CAN_FD_MESSAGE_BUS` signal. For more information on
Simulink bus objects, see Composite Interfaces.

### **N** — Number of messages integer

Number of messages in the vector.
### Output

### **CAN FD Msg** — CAN FD message output `CAN_FD_MESSAGE_BUS`

The block output is a Simulink
`CAN_FD_MESSAGE_BUS` signal. For more information on
Simulink bus objects, see Composite Interfaces.

### **N** — Number of messages integer

Number of messages in the vector.

## Parameters

Not documented in R2025b.

## Libraries

Simulink Real-Time / XCP / CAN FD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Generate and consume XCP messages that are transported by CAN FD hardware

The XCP CAN FD Transport Layer block handles CAN FD messages that your
model transmits or receives by using Simulink®
Real-Time™ CAN FD library blocks.

Connect the input side of the block to a block that receives CAN FD messages. Connect
the output side of the block to a block that transmits the XCP messages over CAN FD. Set
up the transmitting block so that a CAN FD message is sent only when an XCP message is
available. Otherwise, the block sends `0` byte data when XCP messages
are not available, causing undefined behavior.
