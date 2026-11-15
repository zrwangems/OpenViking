---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Internet'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/arduino_ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data vector numeric vector

Specify the input data vector that the block transmits as a UDP packet.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

## Parameters

### **Remote IP address** — IP address of remote host `192.168.0.5` (default) | valid IP address | string

Specify the IP address or host name to which to send UDP packets. If you specify a
host name, specify it as a string. To broadcast a UDP packet, specify
`255.255.255.255`.

### **Remote port** — IP port number of remote port `55001` (default) | integer in the range [1, 65535]

Specify the IP port number to which to send UDP packets.

### **Local port** — IP port number of local port `55002` (default) | integer in the range [1, 65535]

Specify the IP port number from which the block sends UDP packets. Use this
parameter when the receiving address expects messages from a specific port
number.

## Libraries

Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013b**

## Description

Send data over UDP network to remote host

Use the UDP Send block to send user datagram protocol (UDP) data to a
remote host. Use this block when the transmission speed is of higher priority than the
transmission reliability or the order of messages. During simulations without the hardware,
this block does nothing.
