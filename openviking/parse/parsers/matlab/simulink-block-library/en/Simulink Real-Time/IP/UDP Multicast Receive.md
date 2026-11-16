---
type: simulink-block
title: 'UDP Multicast Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'udpmulticastreceive'
documentation_source_path: 'io_ref/udpmulticastreceive.html'
language: en
---

# UDP Multicast Receive

## Ports

### Output

### **Data** — Data received vector

Vector of `uint8` containing data received over the
UDP network. If no new
packet is received, the data values are held. To determine whether a new
packet has been received, use the **Length** output
port.

**Data Types:** `uint8`

### **Length** — Number of bytes received double

Number of bytes in the new packet received, otherwise
`0`. If more bytes are received than can be output
through the receive port with width defined by **Receive
width**, the excess bytes are discarded.

## Parameters

### General Parameters

### **Bind address** — Bind IP address for receiving multicast data `0.0.0.0` (default)

The **Bind address** can be either
`0.0.0.0` or a multicast address. When
**Bind address** is set to
`0.0.0.0`, the block binds to
`INADDR_ANY`, which enables the socket to receive
datagrams on all interfaces. This specification enables the
**Group address** field on the block mask. When
**Bind address** is set to a multicast IP address,
the **Group address** field is hidden on the block
mask.

If the **Bind address** is set to
`0.0.0.0`, the block also can receive unicast
messages if the block is configured on a group interface over which
unicast messages are sent. This unicast message receive occurs because
address `0.0.0.0` allows listening to any messages on
all interfaces of the target computer. To avoid this unicast message
receive operation, use a multicast address as a bind address. Using that
setup, the block only receives multicast messages and does not receive
unicast messages.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `bindAddress` |

### **Local port** — Destination UDP port to receive data `1–65535`

Specifies UDP port to receive data.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `localPort` |

### **Receive width** — Width of `Data` output vector `16` (default) | `1–65504`

Determines the width of the `Data` output vector. If
this value is less than the number of bytes in the received packet, the
excess bytes are discarded.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `rcvWidth` |

### **Group address** — Multicast group to join `{}` (default) | `{'x.x.x.x'}` | dotted decimal character vector

This field is hidden when the bind address is a multicast address.
Enter a valid IP address as a dotted decimal character vector, for
example, `{'224.0.0.0'}`. One or more group addresses
can be specified.

The UDP Multicast Receive block
issues an error at model update if the group IP address is not a valid
multicast address in the range `224.0.0.0` through
`239.255.255.255`.

**Example:** `{'224.100.1.1'}`

**Example:** `{'224.100.1.1',
'224.100.1.2'}`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `multicastAddress` |

### **Group interface** — Local IP interface from which to receive data `{}` (default) | `{'x.x.x.x'}` | dotted decimal character vector

The **Group interface** IP address specifies the
interfaces over which incoming multicast messages should be received.
When the bind address is `0.0.0.0`, the multicast
groups specified in the field **Group address** receive
messages over the specified group interface or interfaces. When the bind
address is a multicast address, that address receives messages over the
specified group interface or interfaces. Enter a valid interface IP
address as a dotted decimal character vector, for example,
`{'192.168.7.5'}`. You can also use a MATLAB expression that returns a valid IP address as a character
vector. One or more group interfaces can be specified.

**Example:** `{'192.168.7.5'}`

**Example:** `{'192.168.7.5',
'192.168.7.10'}`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `multicastInterface` |

### **Sample time (-1 for inherited)** — Sample time of block `-1` (default) | numeric

Enter the base sample time or a multiple of the base sample
time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleTime` |

## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Receive data over UDP network from a remote device

The UDP Multicast Receive block receives multicast data over a UDP
network from a remote device. It
can receive data by using the connection between the MATLAB® development computer and Speedgoat® target computers or
by using a dedicated Ethernet card. If you use a dedicated Ethernet card, use the Speedgoat configuration utility to
configure the dedicated Ethernet board.

The UDP Multicast Receive block operates in a real-time application
running on a target computer. The block does not operate in a model simulation on a
development computer.

A maximum of 20 multicast groups can be joined. This number is determined as a product
of the group address and group interface fields on the block mask.
