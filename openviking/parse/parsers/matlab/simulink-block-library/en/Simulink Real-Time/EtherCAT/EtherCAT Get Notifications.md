---
type: simulink-block
title: 'EtherCAT Get Notifications'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetnotifications'
documentation_source_path: 'io_ref/ethercatgetnotifications.html'
language: en
---

# EtherCAT Get Notifications

## Ports
```yaml
ports:
- name: Values
  summary: Self-descriptive 21-element vector containing EtherCAT notification codes [Length 20 * Notification]
  direction: output
  data_types: int32
```

### Output

### **Values** — Self-descriptive 21-element vector containing EtherCAT notification codes [`Length` `20 * Notification`]

- `Length` (`0` –
  `20`) — the number of notifications
  in the vector.
- `Notification` — a composite of a
  notification type and a specific value. The types are:
- - `EC_NOTIFY_GENERIC`
    [`0x00000000`
    (`0`)] — Represents state
    changes, such as:`0x00000001`
    (`1`) — `EtherCAT
    operational state change`.
  - `EC_NOTIFY_ERROR`
    [`0x00010000`
    (`65536`)] — Represents
    error states, such as `0x00010001`
    (`65537`):`cyclic command:
    working counter error`. Some describe
    changes in error state.
  - `EC_NOTIFY_SCANBUS`
    [`0x00030000`
    (`3*65536`)] — Represents
    ScanBus error states, such as
    `0x00030002`
    (`196610`):`ScanBus
    mismatch`.
  - `EC_NOTIFY_HOTCONNECT`
    [`0x00040000`
    (`4*65536`)] — Represents
    hot connect states, such as
    `0x00040005`
    (`262149`):`Subordinate device
    disappears`.

To print the valid notification values and descriptions, call
`slrealtime.EtherCAT.filterNotifications` without an
argument.

**Data Types:** `int32`
## Parameters
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT network identifier 0 (default) | 0-11
  group: ''
  block_parameter: device_id
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

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample
time. Use the EtherCAT task sample time.

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

Collect notifications from the EtherCAT bus

The EtherCAT Get Notifications block collects notifications from the
EtherCAT® stack and presents them to the output as a 21-element vector of
`int32`. At each time step, the block outputs what it has
accumulated and clears itself for the next time step.

The vector contains the number of notifications in element `1`,
followed by up to `20` notification codes. The maximum number of
notifications is `20`. If the bus presents more than
`20` notifications to the output, the block discards the newest
notifications and presents the first `20` that were received.
