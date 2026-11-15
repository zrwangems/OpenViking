---
type: simulink-block
title: 'TCP Client'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / TCP'
documentation_page: 'tcpclient'
documentation_source_path: 'io_ref/tcpclient.html'
language: en
---

# TCP Client

## Ports

### Input

### **Enable** — Connect block to remote Ethernet device integer

If `Enable` is greater than zero, the block connects to the Ethernet
device. Otherwise, the block does not
connect to the Ethernet device.
### Output

### **Status** — Device returns a status of not connected or connected `0` | `1`

The status value is one of:

- `0` — Not connected
- `1` — Connected

As a best practice, connect the `Status` output
of a TCP configure block to the `Enable` input of
the associated TCP Send and TCP Receive blocks.

## Parameters

### **Use host-target connection** — Use Ethernet connection between development and target computers `'off'` (default) | `'on'`

#### Dependency

When you select this parameter, it deactivates the **Client IP
address** parameter and excludes the ports
`1` through `1023` and
`5500` through `5560` from use by
TCP.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useHostTargetConn` |

### **Remote server IP address** — IP address of the server device `x.x.x.x`

Enter the IP address of the server to which you want to connect
the client.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remoteAddress` |

### **Remote server port** — Port number of the server device `1–65535`

Enter the port number of the server to which you want to connect the client.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `remotePort` |

### **Use Nagle's algorithm** — Enable Nagle's algorithm to combine packets `on` (default) | `off`

Enables Nagle's algorithm to improve the efficiency of the TCP/IP network. Nagle's
algorithm reduces the number of packet that are sent over the network. The tradeoff for
this improved efficiency is that Nagle's algorithm introduces a delay before a packet is
sent over the network. You can reduce network latency by disabling Nagle's algorithm for
this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useNaglesAlgorithm` |

### Advanced Parameters

### **Client IP address** — IP address of the client device that is being configured no value (default) | `x.x.x.x`

If you are using a dedicated Ethernet card, this value must match the
**Local IP Address** parameter in the IP
Config block for the network interface. The default value
for the Client IP address field is no value. This empty field means that
the operating system chooses the Client IP address for TCP
transmission.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `clientAddress` |

### **Client local port** — IP port of the client device that is being configured no value (default) | `0–65535`

The combination of **Client IP address** and **Client local
port** must be unique.

Ports `1` through
`1023` and `5500` through `5560` are
reserved for Simulink Real-Time communications. Values '-1', '0', or 'empty' mean that the
block transmits data by using any available port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `clientPort` |

## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2025a: Added parameter to enable or disable Nagle's algorithm

You can reduce network latency (and reduce network efficiency) by disabling
Nagle's algorithm for the TCP Client block and TCP Server block. For more
information, see the **Use Nagle's algorithm** block
parameter.

### R2021b: Changed Parameters Client IP Address and Client Port

The parameters for the TCP Client block have changed. The
parameters **Client IP address** and **Client
port** are optional.

## Description

Configure TCP client

The TCP Client block configures a TCP client.

The parameters **Client IP address**
and **Client port** are optional. The **Client IP
address** applies when the block executes in a real-time application on a
Speedgoat® target computer or in a model simulation on a MATLAB® development computer. If your model is running in Simulink® on the development computer, you can use this block to transmit data to a
remote device. In this case, the Windows® operating system determines the network connection.

If the TCP Client in the real-time application cannot establish the connection
immediately, the connection is established asynchronously and becomes available in the
next time step.
