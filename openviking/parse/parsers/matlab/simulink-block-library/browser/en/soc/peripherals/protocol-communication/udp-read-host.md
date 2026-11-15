---
type: simulink-block
title: 'UDP Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Protocol Communication'
documentation_page: 'udpreadhost'
documentation_source_path: 'ref/udpreadhost.html'
language: en
---

# UDP Read (HOST)

## Ports

### Output

### **data** — UDP packet received from remote host numeric vector

UDP packet received on local host computer, returned as a numeric vector. The
**Data type for Message** and **Length**
parameters set this output data type and packet length, respectively.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **length** — Length of UDP packet nonnegative scalar

Length of UDP packet returned on the **data**
port.

This port is unnamed until you clear the **Output variable-size
signal** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Local IP port** — IP port number of local host `25000` (default) | integer from 1 to 65,535

Specify the IP port number of local host.

**Note**

On Linux®, to set the local IP port number to a value less than 1024, run
MATLAB® with root privileges. For example, at the Linux command line, enter:

```
sudo matlab
```

### **Remote IP address ('0.0.0.0' to accept all)** — IP address of remote host `'0.0.0.0'` (default) | dotted-quad expression

Specify the IP address of the remote host. Set this value to a specific IP address,
to block UDP packets from all other IP addresses. To accept UDP packets from all IP
addresses, use the default value `'0.0.0.0'`.

### **Receive buffer size (bytes)** — Maximum number of data bytes in received data `8192` (default) | positive integer

Specify the maximum number of data bytes of UDP packets you want to store in the
local buffer. Set this value large enough to avoid data loss caused by buffer
overflows.

### **Maximum length for Message** — Maximum length of data `255` (default) | positive integer scalar

Specify the maximum length of the output UDP packet. Set this parameter to a value
equal to or greater than the data size of the UDP packet. The block truncates any data
that exceeds this length.

The maximum payload size of a UDP packet is 65,507 bytes. The **Maximum
length for Message** is equal to the maximum payload size of a UDP packet in
bytes divided by the data type size of the UDP packet. For example, if the output data
type is `double`, then set **Maximum length for
Message** value to 65507/8 = 8118.

### **Data type for Message** — Data type of output UDP packet `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type for the vector elements of output UDP packet. Match this data
type with the data type of the UDP packets sent by the remote host.

### **Blocking time (seconds)** — Time to wait for UDP packet `0` (default) | nonnegative scalar

Specify the duration of time to wait for a UDP packet before returning control to
the scheduler for each sample.

### **Sample time (seconds)** — Sample time `0.01` (default) | nonnegative scalar

Specify how often the scheduler runs this block.

## Libraries

SoC Blockset / Host I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Receive UDP packets on local host computer from remote host

The UDP Read (HOST) block receives UDP (User Datagram Protocol) packets
from remote host on the local host. The local host in the host computer on which you want to
receive UDP packets. The remote host is the host computer or hardware from which you want to
receive UDP packets.
