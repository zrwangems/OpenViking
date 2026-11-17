---
type: simulink-block
title: 'EtherCAT Sync SDO Download'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsdodownload'
documentation_source_path: 'io_ref/ethercatsyncsdodownload.html'
language: en
---

# EtherCAT Sync SDO Download

## Ports
```yaml
ports:
- name: Data
  summary: Data to write to subordinate device numeric
  direction: input
- name: Error
  summary: Report an EtherCAT network error 0 | integer
  direction: output
```

### Input

### **Data** — Data to write to subordinate device numeric

Input data for writing to the EtherCAT subordinate device.
### Output

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
- name: Timeout
  summary: Time to wait for response from subordinate device numeric
  group: ''
  block_parameter: timeout
```

### **Index** — Index of CANopen register integer

Specify the hexadecimal (for example, 0x7) or decimal index of the CANopen
register.

If you specify an invalid index, the block returns a nonzero value through the
`Error` output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `index` |

### **Subindex** — Subindex of CANopen register integer

Specify the hexadecimal (for example, 0x7) or decimal subindex of the CANopen
register.

If you specify an invalid subindex, the block returns a nonzero value through the
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

### **Timeout** — Time to wait for response from subordinate device numeric

The maximum number of milliseconds to wait for a response before returning a timeout
error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `timeout` |
## Libraries

Simulink Real-Time / EtherCAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Transmit data synchronously to subordinate device represented by service data object

The EtherCAT Sync SDO Download block selects a CANopen register by
**Index** value in the specified EtherCAT® subordinate device and sends a write request. The block then waits until it receives a
response or until the timeout period is over.

The response to an operation takes several ticks of the main
task sample time. Assign the synchronous blocks a sample time slower than the main task sample
time.
