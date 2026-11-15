---
type: simulink-block
title: 'XCP CAN Transport Layer'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpcantransportlayer'
documentation_source_path: 'io_ref/xcpcantransportlayer.html'
language: en
---

# XCP CAN Transport Layer

## Ports

### Input

### **CAN Msg** — CAN MESSAGE structures being consumed vector

Vector of CAN MESSAGE structures being consumed.

### **N** — Number of messages integer

Number of messages in the vector.
### Output

### **CAN Msg** — CAN MESSAGE structures being generated vector

Vector of CAN MESSAGE structures being generated.

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

**Introduced in R2020b**

## Description

Generate and consume XCP messages that are transported by CAN hardware

The XCP CAN Transport Layer block handles CAN messages that your model
transmits or receives by using Simulink®
Real-Time™ CAN library blocks.

Connect the input side of the block to a block that receives CAN messages. Connect the
output side of the block to a block that transmits the XCP messages over CAN. Set up the
transmitting block so that a CAN message is sent only when an XCP message is available.
Otherwise, the block sends `0` byte data when XCP messages are not
available, causing undefined behavior.
