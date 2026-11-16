---
type: simulink-block
title: 'UDP Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpreceive'
documentation_source_path: 'io_ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Data received vector

Vector of `uint8` containing data received over the
UDP network. If no new
packet is received, the data values are held. To determine whether a new
packet has been received, use the **Length** output
port. If you enable the **Enable Simulink messages**
parameter, the data type is `UDP_Packet`. This data
type consists of:

- `IP_Address`: DataType: uint8, Complexity:
  real, Dimensions: [4 1]
- `IP_Port`: DataType: uint16, Complexity:
  real, Dimensions: 1
- `Length`: DataType: uint16, Complexity: real,
  Dimensions: 1
- `Data`: DataType: uint8, Complexity: real,
  Dimensions: [75 1]

**Data Types:** `uint8` | `UDP_Packet`

### **Length** — Number of bytes received double

This port is available when you disable the **Enable Simulink
messages** parameter. The Length is the number of bytes in
the new packet received, otherwise `0`. If more bytes
are received than can be output through the **Data**
port with width defined by **Receive width**, the
excess bytes are discarded.

## Parameters

### General Parameters

### **Use host-target connection** — Use Ethernet connection between development and target computers `'off'` (default) | `'on'`

#### Dependency

When you select this parameter, it deactivates the **Local
IP address** parameter and excludes the ports
`1` through `1023` and
`5500` through `5560` from use
by UDP.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useHostTargetConn` |

### **Local IP address** — Destination IP address for receiving data `Use host-target connection` (default)

When **Local IP address** is set to `Use
host-target connection`, the block uses the connection
between the development and
target computers.
Use `0.0.0.0` to bind to `INADDR_ANY`,
which enables the socket to receive broadcast datagrams.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ipAddress` |

### **Local port** — Destination UDP port to receive data `1–65535`

Specifies UDP port to receive data.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

### **Receive width** — Width of `Data` output vector `1–65504`

Determines the width of the `Data` output vector. If
this value is less than the number of bytes in the received packet, the
excess bytes are discarded.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rcvWidth` |

### **Receive from any source** — Causes receiver to accept data from any IP address `on` (default) | `off`

When **Receive from any source** is
`on`, the block receives data from
any accessible IP address. When it
is `off`, the block receives data from only the address
that you specify in **From IP address**.

To make the **From IP address** parameter visible,
clear the **Receive from any source** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rcvFmAny` |

### **From IP address** — Source from which to receive data `x.x.x.x`

Enter a valid IP address as a dotted decimal character vector, for
example, `192.168.7.2`. You can also use a MATLAB expression that returns a valid IP address as a character
vector.

The address `255.255.255.255` is an invalid IP
address.

To make this parameter visible, clear the **Receive from any
source** check box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `fmAddress` |

### **Sample time (-1 for inherited)** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample
time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleTime` |

### **Enable Simulink messages** — Data as messages `off` (default) | `on`

The Enable Simulink messages directs the block to treat data as
messages. When enabled, the Length port is removed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MessageOut` |

### **Maximum messages per timestep** — Limits messages `1` (default) | int

The Maximum messages per time step value limits the number of messages
to permit in a time step. If the number of messages exceeds this limit,
an error is generated..

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `maxPacket` |

## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Receive data over UDP network from a remote device

The UDP Receive block receives data over a UDP network from a remote
device. It can receive data by
using the connection between the MATLAB® development computer and Speedgoat® target computers or
by using a dedicated Ethernet card. If you use a dedicated Ethernet card, use the Speedgoat configuration utility to
configure the dedicated Ethernet board.

The parameter **Local IP address**
applies when the block executes in a real-time application on a target computer or in a
model simulation on a development computer. If your model is running in Simulink® on the development computer, you can use this block to receive data to a
remote device. In this case, the Windows® operating system determines the network connection.
