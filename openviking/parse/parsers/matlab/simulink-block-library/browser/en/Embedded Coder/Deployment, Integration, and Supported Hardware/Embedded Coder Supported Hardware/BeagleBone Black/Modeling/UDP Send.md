---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'beaglebone/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Input** — Input data vector vector

Specify the input data vector that the block transmits as a UDP packet.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**Complex Number Support:** Yes

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address from which to accept UDP packets `'127.0.0.1'` (default) | IP address | string

Specify the IP address or host name to which to send UDP packets. If you specify a
host name, specify it as a string. To broadcast a UDP packet, specify
`'255.255.255.255'`.

### **Remote IP port** — Number of remote IP port 25000 (default) | scalar in the range [1, 65535]

Specify the IP port number to which to send UDP packets. This parameter is tunable
in the generated code but is not tunable during simulation.

On Linux®, to set the IP port number below 1024, run MATLAB® with root privileges. For example, at the Linux command line, enter `sudo matlab`.

### **Local IP port source** — Source of local IP port `Automatically determine` (default) | `Specify via dialog`

Specify whether the block uses a local port number that the system assigns or that
you specify by using the **Local IP port** parameter. For the system to
assign the port number, select `Automatically determine`. If
the receiving address expects UDP packets from a specific port number, select
`Specify via dialog` and specify the port number by using the
**Local IP port** parameter.

### **Local IP port** — Number of local IP port -1 (default) | scalar in the range [1, 65535]

Specify the IP port number from which the block sends UDP packets. Use this
parameter when the receiving address expects messages from a specific port
number.

#### Parameter Dependencies

- To enable this parameter, set **Local IP port source**  to
  `Specify via dialog`.

### **Send buffer size (bytes)** — Size of buffer that sends UDP packets 8192 (default) | scalar in the range [1, 67108864]

Specify the size of the buffer, in bytes, that sends the UDP packets. Make the
buffer large enough to avoid data loss caused by buffer overflows.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Send UDP message

The UDP Send block transmits user datagram protocol (UDP) data to a remote
host. The block transmits an input data vector as a UDP packet to a remote IP network port.
The remote IP port number to which the block sends the UDP packets is tunable in the generated
code.
