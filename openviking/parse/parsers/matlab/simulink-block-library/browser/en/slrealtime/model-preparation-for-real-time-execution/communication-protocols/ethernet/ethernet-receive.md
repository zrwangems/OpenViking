---
type: simulink-block
title: 'Ethernet Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / Ethernet'
documentation_page: 'ethernetreceive'
documentation_source_path: 'io_ref/ethernetreceive.html'
language: en
---

# Ethernet Receive

## Ports

### Output

### **Data** — Ethernet packet Simulink message

Connect the Ethernet packet signal from this port to the model. If you enable the
**Enable Simulink messages** parameter, the data type is
`Ethernet_Packet`. This data type consists of:

- `Data`: DataType: uint8, Complexity: real, Dimensions: [64
  1]
- `Length`: DataType: uint8, Complexity: real, Dimensions:
  1

**Data Types:** `uint8` | `Ethernet_Packet`

### **Length** — Number of bytes received double

This port is available when you disable the **Enable Simulink
messages** parameter. The Length is the number of bytes in the new packet
received, otherwise it is `0`.

**Data Types:** `double`

## Parameters

### **Interface Name** — Target computer Ethernet interface name `wm0` | `wm1` | character vector

The **Interface Name** is the name of the target computer Ethernet
interface. Use the Speedgoat Ethernet Configuration Tool to identify the Ethernet index
(interface) on the target computer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterfaceName` |

### **Data Width** — Data port width in bytes 64 (default) | integer

The **Data Width** is the width of the Data port in bytes. Ethernet
packets that are shorter than this width are padded with zeros.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataWidth` |

### **Enable Simulink messages** — Data as messages `off` (default) | `on`

The Enable Simulink messages directs the block to treat data as messages. When
enabled, the Length port is removed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MessageOut` |

### **Maximum messages in a time step** — Limit packets per time step 1 (default) | integer

The **Maximum messages in a time step** selects the maximum number
of packets that the block outputs for each time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxMessagesPerStep` |

### **Capture filter** — Filter on received packets character vector

The Capture filter selects which packets to receive. If no filter is provided, all
packets are received. For information about capture filter syntax, see the
**Expressions** section in the `tcpdump` page in the QNX Neutrino documentation. This example
filter captures packets that are addressed to destination port 9001.

```
dst port 9001
```

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterString` |

### **Sample Time** — Sample time of block -1 (default) | numeric

Enter the base sample time or a multiple of the base sample time.
`-1` means that sample time is inherited.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |

## Libraries

Simulink Real-Time / IP / Ethernet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Receive Ethernet packets from Simulink Real-Time target computer

The Ethernet Receive block enables you to receive Ethernet packets on a
Simulink®
Real-Time™ target computer. The block receives the packet from the Ethernet interface
(device) that you select on the target computer.
