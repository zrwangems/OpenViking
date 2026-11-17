---
type: simulink-block
title: 'EtherCAT Sync SSC/SoE Download'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsscsoedownload'
documentation_source_path: 'io_ref/ethercatsyncsscsoedownload.html'
language: en
---

# EtherCAT Sync SSC/SoE Download

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

Input data for writing to the EtherCAT subordinate device. The data
signal has the type specified in **Data Type** and vector dimension given
by **Dimension**.
### Output

### **Error** — Report an EtherCAT network error `0` | integer

If no error occurs, this port transmits
`0`. Otherwise, it transmits a
nonzero value. For list of error codes, see EtherCAT Error Codes.
## Parameters
```yaml
parameters:
- name: IDN
  summary: Identification Number character vector
  group: ''
  block_parameter: idn
- name: Drive Number
  summary: Index number of the drive integer
  group: ''
  block_parameter: drive
- name: Data Type
  summary: Data type of the IDN double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: sig_type
- name: Dimension
  summary: Dimension of data for this IDN 1 (default)
  group: ''
  block_parameter: sig_dim
- name: Network Device Index
  summary: EtherCAT network identifier 0 (default) | 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: Name of device that contains the IDN character vector
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

### **IDN** — Identification Number character vector

Identify parameters.

The documentation for your EtherCAT device specifies the **IDN**
values. You can select the **IDN** as a character vector that
represents a 16-bit integer (according to IEC 61800 -7 -204), such as
`S-0-0150` or `P-0-0150` with:

- First field (bit 15): `S` for Standard data,
  `P` for product-specific data
- Second field (bit 14 - 12): `0..7` for parameter set
- Third field (bit 11 - 0): `0..4095` for data-block
  number

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `idn` |

### **Drive Number** — Index number of the drive integer

Specify the decimal index of the drive.

SoE blocks apply to only motor controllers. A single subordinate device can support one or more
drive or motor channels. The drive number is the zero-based index of the drive or motor
channel on this subordinate device at which this block is aimed. In SoE terminology, the drive is the
logic that sends control signals to the motor. Typically, this logic is a small
processor inside the subordinate device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `drive` |

### **Data Type** — Data type of the IDN `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

To identify the data type for the IDN, refer to the subordinate device documentation
for the description of the IDN and the data type it uses. From the list, select the data
type of the **IDN**.

If you select a data type that does not match the type of the entry, the block returns
a nonzero value through the `Error` output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_type` |

### **Dimension** — Dimension of data for this IDN `1` (default)

Specify the row dimension of data for this IDN.

To identify the dimension of data (vector size) for the IDN, refer to the subordinate device
documentation for the description of the IDN and the number of data type values (the
dimension) it uses. Enter the vector length as found in the SoE description for the
subordinate device in its manual.

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

### **SubDevice Name** — Name of device that contains the IDN character vector

From the list, select the name of the device that contains the
**IDN**.

The block populates this drop-down list with the contents of the configuration file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `subdevice_name` |

### **Sample time** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample time. `-1`
means that the sample time is inherited. The EtherCAT Sync SSC/SoE Download
block and the EtherCAT Sync SSC/SoE Uploadblock require at least three steps
of the main EtherCAT processing task. Select a sample time that is three times that of the
main task sample time or the model can overload and stop.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sample_time` |

### **Timeout** — Time to wait for response from subordinate device numeric

Enter the maximum number of milliseconds to wait for a response from the EtherCAT subordinate device.

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

The EtherCAT Sync SSC/SoE Download block provides synchronous SERCOS
interface (SErial Real time COmmunication Specification) over EtherCAT® (SoE) download. The block selects an **IDN** in the
specified subordinate device and sends a download (write) request. The block then waits until it
receives a response to the request or until the timeout period expires.

The response to an operation takes several ticks of the main
task sample time. Assign the synchronous blocks a sample time slower than the main task sample
time.
