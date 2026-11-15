---
type: simulink-block
title: 'UDP Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpwritehost'
documentation_source_path: 'ref/udpwritehost.html'
language: en
---

# UDP Write (HOST)

## Ports

### Input

### **Port\_1** — Input signal numeric vector

Input signal, specified as a numeric vector. The block sends this data as a UDP
packets to the specified remote IP address and port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address of remote host `'255.255.255.255'` (default) | dotted-quad expression

Specify the IP address of the remote host. To broadcast UDP packets, use the default
value, `'255.255.255.255'`.

### **Remote IP port** — IP port number of remote host `25000` (default) | integer from 1 to 65,535

Specify the IP port number of the remote host.

### **Local IP port source** — Source of local IP port source `Automatically determine` (default) | `Specify via dialog`

Set the source of Local IP port for the block by selecting one of these values:

- `Automatically determine` — Assigns an available
  local IP port number randomly from which UDP packets are sent.
- `Specify via dialog` — Allows you to specify the
  local IP port number using the **Local IP port**
  parameter.

### **Local IP port** — IP port number of local host `-1` (default) | integer from 1 to 65,535

Specify the port number of the local host. If this value is set to
`-1` (default), the block sets the local IP port number to a random
available port number and uses that port to send the UDP packets. If the remote host
accepts UDP packets from a particular IP port number, specify that IP port number for
this value.

## Libraries

SoC Blockset / Host I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Send UDP packets from host computer to remote host

The UDP Write (HOST) block sends UDP (User Datagram Protocol) packets from
a local host to a remote host. The local host in the host computer from which you want to send
UDP packets. The remote host is the host computer or hardware to which you want to send UDP
packets. The remote host is identified by the remote IP address and remote IP port parameters
from host computer.
