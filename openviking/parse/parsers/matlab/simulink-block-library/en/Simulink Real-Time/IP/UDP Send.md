---
type: simulink-block
title: 'UDP Send'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpsend'
documentation_source_path: 'io_ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Data** — Data to transmit vector

Vector of `uint8` containing data to transmit over
the UDP network. To determine how many bytes of data to transmit, use
the **Length** input port. If you enable the
**Enable Simulink messages** parameter, the data
type is `UDP_Packet`. Use the `slrealtime.createUDPPacketBusObj` function to create the
`Simulink.Bus` type
`Ethernet_Packet`. This data type consists
of:

- `IP_Address`: DataType: uint8, Complexity:
  real, Dimensions: [4 1]
- `IP_Port`: DataType: uint16, Complexity:
  real, Dimensions: 1
- `Length`: DataType: uint16, Complexity: real,
  Dimensions: 1
- `Data`: DataType: uint8, Complexity: real,
  Dimensions: [75 1]

**Data Types:** `uint8` | `UDP_Packet`

### **Length** — Number of bytes of data to transmit double

This port is available when you disable the **Enable Simulink
messages** parameter. The Length determines the number of
bytes of data to transmit. Specify the width of the
`Data` vector as the maximum number of bytes that
you expect to transmit.

## Parameters

### **Use host-target connection** — Use Ethernet connection between development and target computers `'off'` (default) | `'on'`

#### Dependency

When you select this parameter, it deactivates the **Local IP
address** parameter and excludes the ports
`1` through `1023` and
`5500` through `5560` from use by
UDP.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useHostTargetConn` |

### **To IP address** — IP address of target device `10.10.10.10` (default) | `x.x.x.x`

Specifies IP address of target
device. To broadcast
to all devices on the local subnetwork, send to
`255.255.255.255`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `toAddress` |

### **To port** — UDP port of target device `34` (default) | `1–65535`

Specify the UDP port of target
device. With
**To IP address**, this parameter defines the
destination of the data transmission.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `toPort` |

### **Sample time (-1 for inherited)** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample
time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleTime` |

### **Enable Simulink messages** — Data as messages `off` (default) | `on`

The Enable Simulink messages directs the block to treat data as messages.
When enabled, the Length port is removed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MessageIn` |

### Advanced Parameters

### **Local IP address** — Source IP address for sending data no value (default) | `x.x.x.x`

When **Local IP address** is set to **Use
host-target connection**, the block uses the connection
between the development and target computers. When **To IP
address** is specified as a multicast address, the local IP
address is used to determine the outbound interface over which multicast
datagrams are sent. The default value for the Local IP address field is
no value. This empty field means that the operating system chooses the
Local IP address for UDP transmission.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ipAddress` |

### **Local port** — Source UDP port to transmit data no value (default) | `0–65535` | `-1`

Specifies local UDP port to transmit data.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

The value `0`, `−1`, or no value
mean that the block transmits data by using
any available
port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2021b: Changed Parameters Local IP Address and Local Port

The parameters for the UDP Send block have changed. For unicasting,
broadcasting, and multicasting, the parameters **Local IP address**
and **Local port** are optional.

### R2021a: Added Multicast Support

The UDP Multicast Receive block was added, and the UDP
Send block has multicast support. These blocks provide multicast message
support for the UDP communications protocol.

## Description

Send data over UDP network to a remote device

The UDP Send block sends data over a UDP network to a remote
device. The block can send data by
using the connection between the MATLAB® development computer and Speedgoat® target computers or
by using a dedicated Ethernet card. If you use a dedicated Ethernet card, use the Speedgoat configuration utility to
configure the dedicated Ethernet board. One of the settings provided by this utility is
the **Default Gateway** setting. When using the UDP Send
block to broadcast to 255.255.255.255, the IP interface for broadcast is based on this
**Default Gateway** setting.

To broadcast to all devices on the
local subnetwork, set **To IP address** to
`255.255.255.255`. Otherwise, set **To IP
address** to a valid IP address.

For unicasting, broadcasting and multicasting, the
parameters **Local IP address** and **Local port** are
optional. The **Local IP address** applies when the block executes in a
real-time application on a target computer or in a model simulation on a development
computer. If your model is running in Simulink® on the development computer, you can use this block to transmit data to a
remote device. In this case, the Windows® operating system determines the network connection.
