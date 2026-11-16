---
type: simulink-block
title: 'EtherCAT Get Device State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetdevicestate'
documentation_source_path: 'io_ref/ethercatgetdevicestate.html'
language: en
---

# EtherCAT Get Device State

## Ports

### Output

### **State** — State received from the selected device `1` | `2` | `4` | `8`

| State | Value | Description |
| --- | --- | --- |
| `INIT` | 1 | Initialization — The system finds terminal devices and initializes the communication controller. |
| `PREOP` | 2 | Preoperational — The system uses the communication controller to exchange system-specific initialization data. In this state, the network cannot transmit or receive signal data. |
| `SAFEOP` | 4 | Safe operational — The network is running and ready for full operation. The supervisor sends input data to the terminal device. The terminal device output remains in a safe state. |
| `OP` | 8 | Operational — The network is in full operation. The supervisor sends input data to the terminal device. The terminal device responds with output data. |

## Parameters

### **Network Device Index** — EtherCAT network identifier `0` (default) | `0-11`

To associate a block with an EtherCAT network, enter the **Network Device Index** value from the
EtherCAT Init block representing that network into the **Network
Device Index** for the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_id` |

### **SubDevice Name** — Name of EtherCAT subordinate device character vector

Select an EtherCAT subordinate device from the list of available subordinate
devices provided by the ENI configuration file. The configuration file is
selected by the EtherCAT Init
block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_name` |

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

**Introduced in R2021b**

## Description

Get state of EtherCAT network

The EtherCAT Get Device State block returns the state of a device on
the EtherCAT® network.
