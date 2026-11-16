---
type: simulink-block
title: 'Ethernet Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / Ethernet'
documentation_page: 'ethernetsend'
documentation_source_path: 'io_ref/ethernetsend.html'
language: en
---

# Ethernet Send

## Ports

### Input

### **Data** — Inport for Ethernet packet signal input for constructed Ethernet packet

Connect the constructed Ethernet packet signal from the model to this inport. If
you enable the **Enable Simulink messages** parameter, the data type
is `Ethernet_Packet`. Use the `slrealtime.createEthernetPacketBusObj` function to create the `Simulink.Bus` type `Ethernet_Packet`. This data type
consists of:

- `Data`: DataType: uint8, Complexity: real, Dimensions: [64
  1]
- `Length`: DataType: uint8, Complexity: real, Dimensions:
  1

**Data Types:** `uint8` | `Ethernet_Packet`

### **Length** — Number of bytes of data to transmit double

This port is available when you disable the **Enable Simulink
messages** parameter. The **Length** determines the number
of bytes of data to transmit. Specify the width of the `Data` vector
as the maximum number of bytes that you expect to transmit.

**Data Types:** `double`

## Parameters

### **Interface Name** — Target computer interface name `wm0` | `wm1` | character vector

The **Interface Name** is the name of the target computer Ethernet
interface. Use the Speedgoat Ethernet Configuration Tool to identify the Ethernet index
(interface) on the target computer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterfaceName` |

### **Overwrite source MAC address** — Replace source MAC Address with MAC address from Data port `off` (default) | `on`

If enabled (`on`), the block sends the packet with the actual MAC
address of the target computer, overwriting the MAC address set by the user. If disabled
(`off`), the block sends the packet with the MAC address specified in
the packet constructed by the user.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OverwriteSrcMACAddress` |

### **Enable Simulink messages** — Data as messages `off` (default) | `on`

The Enable Simulink messages directs the block to treat data as messages. When
enabled, the Length port is removed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MessageIn` |

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

Send Ethernet packets from target computer

The Ethernet Send block enables you to send an Ethernet packet that you
construct by using Simulink® blocks or a MATLAB® Function block and connects this signal to the Data inport. This input is fully
customizable. The block sends the packet to the Ethernet interface (device) that you select on
the Speedgoat® target computer.
