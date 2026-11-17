---
type: simulink-block
title: 'TCP Server'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'IP'
documentation_page: 'tcpserver'
documentation_source_path: 'io_ref/tcpserver.html'
language: en
---

# TCP Server

## Ports
```yaml
ports:
- name: Enable
  summary: Connect block to remote Ethernet device integer
  direction: input
- name: Status
  summary: Device returns a status of not connected or connected 0 | 1
  direction: output
```

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
```yaml
parameters:
- name: Use host-target connection
  summary: Use Ethernet connection between the development computer and target computers 'off' (default) | 'on'
  group: ''
  block_parameter: useHostTargetConn
- name: Server IP address
  summary: IP address of the server device that is being configured x.x.x.x
  group: ''
  block_parameter: serverAddress
- name: Server port
  summary: IP port of the server device that is being configured 1–65535
  group: ''
  block_parameter: serverPort
- name: Use Nagle's algorithm
  summary: Enable Nagle's algorithm to combine packets on (default) | off
  group: ''
  block_parameter: useNaglesAlgorithm
```

### **Use host-target connection** — Use Ethernet connection between the development computer and target computers `'off'` (default) | `'on'`

#### Dependency

When you select this parameter, it deactivates the **Server IP
address** parameter and excludes the ports
`1` through `1023` and
`5500` through `5560` from use by
TCP.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `useHostTargetConn` |

### **Server IP address** — IP address of the server device that is being configured `x.x.x.x`

If you are using a dedicated Ethernet card, this value must match the IP
address configured for the Ethernet card on the target computer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `serverAddress` |

### **Server port** — IP port of the server device that is being configured `1–65535`

The combination of **Server IP address** and **Server
port** must be unique.

Ports `1` through `1023` and
`5500` through `5560` are reserved for Simulink Real-Time
communications.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `serverPort` |

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
## Libraries

Simulink Real-Time / IP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2025a: Added parameter to enable or disable Nagle's algorithm

You can reduce network latency (and reduce network efficiency) by disabling
Nagle's algorithm for the TCP Client block and TCP Server block. For more
information, see the **Use Nagle's algorithm** block
parameter.

## Description

Configure TCP server

The TCP Server block configures a TCP server.
