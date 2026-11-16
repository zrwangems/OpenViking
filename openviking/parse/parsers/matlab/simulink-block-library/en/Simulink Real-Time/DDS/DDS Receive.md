---
type: simulink-block
title: 'DDS Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'DDS'
documentation_page: 'ddsreceive'
documentation_source_path: 'io_ref/ddsreceive.html'
language: en
---

# DDS Receive

## Ports

### Output

### **DDS Msg** — DDS message simulink message of Bus type

Returns the DDS message sent.

## Parameters

### **Data Dictionary** — Associate a data dictionary string | char

Associate a simulink data dictionary containing dds data definitions or create a new
data dictionary for the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `datadict` |

### **Topic** — Select a topic name string scalar | char vector

Select a topic from the drop-down menu for the data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `topic` |

### **Reader XML Path** — Data writer XML path string (default)

select the data writer XML path.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `xmlPath` |

### **Reader QoS** — Quality of service string (default)

Select the quality of service from the drop-down menu.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `qos` |

### **Sample time** — Sample time -1 (default) | numeric

Enter the base sample time or a multiple of the base sample time.
`-1` means that the sample time is inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampletime` |

## Libraries

Simulink Real-Time / DDS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Receive a DDS message

The DDS Receive block receives a DDS message for a selected topic in the
Simulink®
Real-Time™ model. The block allows you to attach a simulink data dictionary containing the
DDS data definitions with the model.

The DDS Receive and DDS Send blocks let Simulink
Real-Time applications communicate with Data Distribution Service (DDS) middleware
applications through a shared Simulink data dictionary. These blocks are compatible with the
DDS Blockset, which includes a DDS dictionary that lets you manage, create, and edit your DDS
definitions in Simulink. You can import DDS specifications as XML files to create a skeleton Simulink
model as a starting point for developing algorithms for DDS applications. For more
information, see How Does DDS Blockset Work? (DDS Blockset).

The DDS Receive block receives a DDS message for a selected topic in the
real-time application. You attach a Simulink data dictionary containing the DDS data
definitions to the block. You can create a new data dictionary or associate an existing data
dictionary to the block and select a topic, data writer path, and Quality of Service (QoS)
from the data dictionary.

The DDS Receive block and DDS Send block have some limitations:

- You can use these blocks in the top level of a model. These blocks cannot be used in
  the referenced models.
- You can use these blocks in a real-time application. These blocks cannot be used for
  simulation in normal mode, accelerator mode, or rapid accelerator mode.
- You cannot use these blocks in protected models.
