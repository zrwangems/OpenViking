---
type: simulink-block
title: 'EtherCAT Set State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsetstate'
documentation_source_path: 'io_ref/ethercatsetstate.html'
language: en
---

# EtherCAT Set State

## Ports
```yaml
ports:
- name: New State
  summary: State transmitted to the EtherCAT network 1 | 2 | 4 | 8
  direction: input
- name: Prev State
  summary: Previous state of the network 1 | 2 | 4 | 8
  direction: output
- name: Error
  summary: Report an EtherCAT state error 0 | integer
  direction: output
```

### Input

### **New State** — State transmitted to the EtherCAT network `1` | `2` | `4` | `8`

| State | Value | Description |
| --- | --- | --- |
| `INIT` | 1 | Initialization — The system finds terminal devices and initializes the communication controller. |
| `PREOP` | 2 | Preoperational — The system uses the communication controller to exchange system-specific initialization data. In this state, the network cannot transmit or receive signal data. |
| `SAFEOP` | 4 | Safe operational — The network is running and ready for full operation. The supervisor sends input data to the terminal device. The terminal device output remains in a safe state. |
| `OP` | 8 | Operational — The network is in full operation. The supervisor sends input data to the terminal device. The terminal device responds with output data. |
### Output

### **Prev State** — Previous state of the network `1` | `2` | `4` | `8`

This port returns the value of the previous setting of the
`New State` port.

### **Error** — Report an EtherCAT state error `0` | integer

If no error occurs, this port
returns `0`. Otherwise, it returns a nonzero
value.
## Parameters
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT network identifier 0 (default) | 0-11
  group: ''
  block_parameter: device_id
- name: Timeout
  summary: Time to wait for the network to change state integer
  group: ''
  block_parameter: timeout
- name: Sample time
  summary: Sample time of block -1 (default) | numeric
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT network identifier `0` (default) | `0-11`

To associate a block with an EtherCAT network, enter the **Network Device Index** value from the
EtherCAT Init block representing that network into the **Network
Device Index** for the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_id` |

### **Timeout** — Time to wait for the network to change state integer

Enter the number of seconds to wait for the EtherCAT network state to transition.

Set the timeout to `0` to return immediately. If you
specify a nonzero **Timeout** value, in the Configuration
Parameters **Solver** pane, set the **Fixed-step
size** parameter to a value larger than the
**Timeout** value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `timeout` |

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1` means
that the sample time is inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sample_time` |
## Libraries

Simulink Real-Time / EtherCAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Set state of EtherCAT network

The EtherCAT Set State block sets the state of the EtherCAT® network to the value passed in through the `New State`
port.
