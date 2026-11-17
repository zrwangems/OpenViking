---
type: simulink-block
title: 'J1939 CAN Transport Layer'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939cantransportlayer'
documentation_source_path: 'ug/j1939cantransportlayer.html'
language: en
---

# J1939 CAN Transport Layer

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Config name
  summary: J1939 network configuration name configuration list option
  group: ''
- name: Device
  summary: CAN device device list option
  group: ''
- name: Bus speed
  summary: Speed of CAN bus 250000 (default) | 500000
  group: ''
- name: Sample time
  summary: Simulation refresh rate 0.01 (default) | numeric
  group: ''
```

### **Config name** — J1939 network configuration name configuration list option

The name of the J1939 Network Configuration block to associate this
transport layer block with.

### **Device** — CAN device device list option

The CAN device, chosen from all connected CAN devices.

### **Bus speed** — Speed of CAN bus `250000` (default) | `500000`

Speed of the CAN bus in bits per second, specified as one of the two rates supported
by the J1939 protocol, 250000 or 500000. The default is 250000.

### **Sample time** — Simulation refresh rate `0.01` (default) | numeric

Simulation refresh rate, specified as the sampling time of the block during
simulation. This value defines the frequency at which the J1939 CAN Transport Layer
block runs during simulation. For information about simulation sample timing, see Timing in Hardware Interface Models. If the block is inside a
triggered subsystem or inherits a sample time, specify a value of `-1`.
You can also specify a MATLAB® variable for sample time. The default value is `0.01`
simulation seconds.
## Libraries

Vehicle Network Toolbox / J1939 Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Transport J1939 messages via CAN

The J1939 CAN Transport Layer block allows J1939 communication via a CAN
bus. This block associates a user-defined J1939 network configuration with a connected CAN
device. Use one block for each J1939 Network Configuration block in your
model.

### Other Supported Features

The J1939 communication blocks support the use of Simulink® accelerator and rapid accelerator modes. Using this feature, you can speed up
the execution of Simulink models. For more information on this feature, see Acceleration (Simulink).

The J1939 communication blocks also support code generation with limited deployment
capabilities. Code generation requires the Microsoft® C++ compiler.
