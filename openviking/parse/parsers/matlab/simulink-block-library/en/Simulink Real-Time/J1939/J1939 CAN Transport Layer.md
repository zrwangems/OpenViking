---
type: simulink-block
title: 'J1939 CAN Transport Layer'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'J1939'
documentation_page: 'j1939cantransportlayer'
documentation_source_path: 'io_ref/j1939cantransportlayer.html'
language: en
---

# J1939 CAN Transport Layer

## Ports
```yaml
ports:
- name: CAN Msg
  summary: CAN MESSAGE structures being consumed vector
  direction: input
- name: N
  summary: Number of messages integer
  direction: input
- name: CAN Msg
  summary: CAN MESSAGE structures being generated vector
  direction: output
- name: N
  summary: Number of messages integer
  direction: output
```

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
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Real-Time / J1939

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Generate and consume J1939 messages that are transported by CAN hardware

The J1939 CAN Transport Layer block handles CAN messages that your
model transmits or receives by using Simulink®
Real-Time™ CAN library blocks.

Connect the input side of the block to a block that receives CAN messages. Connect the
output side of the block to a block that transmits the J1939 messages over CAN. Set up
the transmitting block so that a CAN message is sent only when an J1939 message is
available. Otherwise, the block sends `0` byte data when J1939 messages
are not available, causing undefined behavior.
