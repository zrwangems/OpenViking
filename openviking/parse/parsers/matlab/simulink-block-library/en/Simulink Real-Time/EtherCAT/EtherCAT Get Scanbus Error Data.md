---
type: simulink-block
title: 'EtherCAT Get Scanbus Error Data'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetscanbuserrordata'
documentation_source_path: 'io_ref/ethercatgetscanbuserrordata.html'
language: en
---

# EtherCAT Get Scanbus Error Data

## Ports
```yaml
ports:
- name: Values
  summary: Input from EtherCAT Get Notifications block [Length 20 * Notification]
  direction: input
- name: Error
  summary: Indicates scanbus error false (default) | true
  direction: output
```

### Input

### **Values** — Input from EtherCAT Get Notifications block [`Length` `20 * Notification`]

The block scans input from the EtherCAT Get Notifications
block.
### Output

### **Error** — Indicates scanbus error false (default) | true

One boolean output that is true for one cycle following a notification for a
scanbus error.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Real-Time / EtherCAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Detects when an EtherCAT device in the model is not responding

The EtherCAT Get Scanbus Error Data block detects when a device in the
model is not responding, provides error output to stop the model, and generates log output
that indicates which device is not responding. The log message provides detailed information
about where the EtherCAT network does not match the ENI file. The log message indicates either
that there is a missing device at a network position or that a different device is found in a
network position than is specified in the ENI for that position. Only the first mismatch found
is reported. The block `Error` output can be used to trigger the Stop
Simulation block.
