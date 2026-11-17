---
type: simulink-block
title: 'EtherCAT PDO Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatpdoreceive'
documentation_source_path: 'io_ref/ethercatpdoreceive.html'
language: en
---

# EtherCAT PDO Receive

## Ports
```yaml
ports:
- name: D
  summary: Data received from subordinate device [double]
  direction: output
```

### Output

### **D** — Data received from subordinate device [double]

Vector of data received from the EtherCAT subordinate device.
## Parameters
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT network identifier 0 (default) | 0-15
  group: ''
  block_parameter: device_id
- name: Signal name
  summary: EtherCAT device variable name character vector
  group: ''
  block_parameter: sig_name
- name: Signal Offset
  summary: 'Location in the process of signal data Read-only: integer'
  group: ''
  block_parameter: sig_offset
- name: Signal Type
  summary: 'Data type for EtherCAT data Read-only: character vector'
  group: ''
  block_parameter: sig_type
- name: Type Size (bits)
  summary: 'Size of EtherCAT data type Read-only: integer'
  group: ''
  block_parameter: type_size
- name: Signal Dimension
  summary: 'Dimension of the signal Read-only: integer'
  group: ''
  block_parameter: sig_dim
- name: Sample Time
  summary: 'Rate at which this block is executed Read-only: numeric'
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT network identifier `0` (default) | `0-15`

To associate a block with an EtherCAT network, copy the **Device index** value from the
EtherCAT Init block representing that network into the
**Device index** for the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_id` |

### **Signal name** — EtherCAT device variable name character vector

From the list, select the EtherCAT device variable
name.

The block parameter dialog box updates the read-only signal information to reflect
the device variable that you
selected.

For a mapping of EtherCAT configurator components to Simulink®
Real-Time™ blocks and block attributes, see EtherCAT Configurator Component Mapping.

For a mapping of Simulink data types to EtherCAT data types, see EtherCAT Data Types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_name` |

### **Signal Offset** — Location in the process of signal data Read-only: integer

This parameter is read-only.

After the execution of the EtherCAT Init block, location in
the process image from which the data is available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_offset` |

### **Signal Type** — Data type for EtherCAT data Read-only: character vector

This parameter is read-only.

Simulink data type for the EtherCAT data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_type` |

### **Type Size (bits)** — Size of EtherCAT data type Read-only: integer

This parameter is read-only.

Size in bits of the EtherCAT data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `type_size` |

### **Signal Dimension** — Dimension of the signal Read-only: integer

This parameter is read-only.

The EtherCAT blocks support vectors and scalars (vectors of dimension
`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sig_dim` |

### **Sample Time** — Rate at which this block is executed Read-only: numeric

This parameter is read-only.

This rate is the execution rate of the EtherCAT task, as specified in the ENI file.

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

Receive data from subordinate device represented by process data object

The EtherCAT PDO Receive block receives data from the EtherCAT® subordinate device.

The block parameter dialog box has two sections, parameters and signal information.
When you specify an EtherCAT network and device variable name:

- The EtherCAT PDO Receive block mask is updated with the
  selected signal name.
- The signal information in the block parameter dialog box is updated to
  reflect the device variable.

**Note**

If an error occurs while the software parses the configuration file specified in the
EtherCAT Init block, this block displays an error message.
