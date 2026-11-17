---
type: simulink-block
title: 'EtherCAT Async SDO Upload'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatasyncsdoupload'
documentation_source_path: 'io_ref/ethercatasyncsdoupload.html'
language: en
---

# EtherCAT Async SDO Upload

## Ports
```yaml
ports:
- name: Enable
  summary: Enables block to upload data int32
  direction: input
- name: Data
  summary: Data received from subordinate device numeric
  direction: output
- name: Status
  summary: Status of data transfer 0 | 1 | 2 | 3
  direction: output
- name: Error
  summary: Report an EtherCAT network error 0 | integer
  direction: output
```

### Input

### **Enable** — Enables block to upload data int32

A value of `0` disables uploads. A constant value of
1 will send a new request each time the status returns to the idle
state.
### Output

### **Data** — Data received from subordinate device numeric

Returns data received from the EtherCAT subordinate device.

### **Status** — Status of data transfer `0` | `1` | `2` | `3`

Status of asynchronous data transfer:

- `0` — Mailbox transfer object idle, transfer not
  running
- `1` — Mailbox transfer object running, transfer not
  complete
- `2` — Transfer
  successfully executed
- `3` — Error occurred during transfer request

### **Error** — Report an EtherCAT network error `0` | integer

If no error occurs, this port transmits
`0`. Otherwise, it transmits a nonzero value. For a list of error codes,
see EtherCAT Error Codes.
## Parameters
```yaml
parameters:
- name: Index
  summary: Index of CANopen register integer
  group: ''
  block_parameter: index
- name: Access Mode
  summary: Select access mode for CoE variables Single Subindex (default) | Complete Access
  group: ''
  block_parameter: complete
- name: Subindex
  summary: Subindex of CANopen register integer
  group: ''
  block_parameter: subIndex
- name: Data Type
  summary: Data type of CANopen register double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: sig_type
- name: Dimension
  summary: Dimension of CANopen register 1 (default)
  group: ''
  block_parameter: sig_dim
- name: Network Device Index
  summary: EtherCAT network identifier 0 (default) | 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: Name of device that contains CANopen register character vector
  group: ''
  block_parameter: subdevice_name
- name: Sample time
  summary: Sample time of block -1 (default) | numeric
  group: ''
  block_parameter: sample_time
```

### **Index** — Index of CANopen register integer

Specify the hexadecimal (for example, 0x7) or decimal index of the CANopen
register.

If you specify an invalid index, the block returns a `3` through the
`Status` output and a nonzero value through the
`Error` output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `index` |

### **Access Mode** — Select access mode for CoE variables `Single Subindex` (default) | `Complete Access`

When the **Access Mode** is `Complete
Access`, the SubIndex parameter is hidden, and the correct
subindex is assumed in each case. The complete access protocol for CoE
access to variables provides:

- Access to all subindexes attached to a single index in the CoE
  dictionary for a single terminal device.
- Read or write all subindexes in the time it would take to read or
  write a single one of them.
- Simultaneously update all subindexes when a tuning parameter set
  is being written
- Capture a simultaneous read of all subindexes
- Allow use of EtherCAT devices that require complete access for
  configuration

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `complete` |

### **Subindex** — Subindex of CANopen register integer

Specify the hexadecimal (for example, 0x7) or decimal subindex of the CANopen
register.

If you specify an invalid subindex, the block returns a nonzerio value through the
`Error` output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `subIndex` |

### **Data Type** — Data type of CANopen register `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

From the list, select the data type of the CANopen register.

If you select a data type that does not match the type of the entry, the block returns
a nonzero value through the `Error` output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_type` |

### **Dimension** — Dimension of CANopen register `1` (default)

Specify the row and column dimension of the CANopen register.

Enter the vector length as found in the CoE description for the subordinate device in
its manual.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_dim` |

### **Network Device Index** — EtherCAT network identifier `0` (default) | `0-11`

To associate a block with an EtherCAT network, enter the **Network Device Index** value from the
EtherCAT Init block representing that network into the **Network
Device Index** for the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_id` |

### **SubDevice Name** — Name of device that contains CANopen register character vector

From the list, select the name of the device that contains the CANopen register.

The block populates this drop-down list with the contents of the configuration file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `subdevice_name` |

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

### R2022a: Complete Access Mode

You can select the access mode for the EtherCAT Async SDO Upload
block and EtherCAT Async SDO Download block.

## Description

Read data asynchronously from subordinate device represented by service data object

The EtherCAT Async SDO Upload block selects a CANopen register by
**Index** value in the specified EtherCAT® subordinate device and sends a read request. It then immediately returns whatever value
was returned from the device on an earlier call to the block.
