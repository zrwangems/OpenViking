---
type: simulink-block
title: 'EtherCAT Get Emergency'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / EtherCAT'
documentation_page: 'ethercatgetemergency'
documentation_source_path: 'io_ref/ethercatgetemergency.html'
language: en
---

# EtherCAT Get Emergency

## Ports

### Output

### **Err Code** — Error Code uint16

The `Err Code` output provides the primary error code
produced by the device for a class of emergency issues.

**Data Types:** `uint16`

### **Err Reg** — Error Register uint8

The `Err Reg` output provides specific error
information that identifies a specific emergency issue inside the class
of emergency issues that is specified by the error code.

**Data Types:** `uint8`

### **Data** — Emergency data vector uint8

The `Data` output is a vector of 5 uint8 values that
the device can send to attach values to a specified emergency issue. At
least one of the values must be non-zero.

**Data Types:** `uint8`

### **Name** — Station address uint8

The `Name` output is a null terminated character
array that identifies the device that sent the emergency message. This
output is the name of the device that is in the ENI file. This name can
differ depending on the string that the TwinCAT® or EC-Engineer software uses to identify the
device.

**Data Types:** `uint8`

## Parameters

### **Network Device Index** — EtherCAT network identifier `0` (default) | `0-11`

To associate a block with an EtherCAT network, enter the **Network Device Index** value from the
EtherCAT Init block representing that network into the **Network
Device Index** for the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `device_id` |

### **Log messages to statusmonitor** — Enable message logging `on` (default) | `off`

The `Log messages to statusmonitor` parameter enables
logging the message to the status monitor.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `logmsg` |

### **Sample time** — Sample time of block `.001` (default) | numeric

Enter the base sample time or a multiple of the base sample time. Use the
EtherCAT task sample time.

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

**Introduced in R2023b**

## Description

Collect emergency messages from the EtherCAT bus

The EtherCAT Get Emergency block collects emergency messages from
EtherCAT® devices and presents the messages as output in the model. Optionally, the
block can log the condition to the Target Computer Status Monitor. The outputs
in the model and the logged status include all the emergency data, so action can be
taken in the model.

Add one block to call into the notification code to collect the emergency message. The
EtherCAT Technology Group defines general types of emergency error codes. Specific
information coding is available in the documentation from each device
manufacturer.

While there can be overlap in emergency message error codes sent by a device, device
manufacturers often do not implement all codes and do not use the same codes for similar
emergency issues. For more information, see the device documentation from the
manufacturer. For example, a search in the Elmo Gold series motor drive application
manual finds a description of error codes and error register values for error situations
that the drive can encounter. The table shows a subset of the information from this
manual.

**Elmo Gold Series Motor Drive Error Codes (subset)**

| Description | Error code | Error reg | Data field |
| --- | --- | --- | --- |
| CAN message lost | `0x8110` | `11` | `[0 0 0 0 0]` |
| Motor stuck | `0x7121` | `21` | `[0 0 0 0 0]` |
| Queue is low. | `0xff00` | `81` | `[0x56, idx, 0, 0, 0]` |
