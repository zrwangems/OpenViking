---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/raspberrypi_ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts an array and sends it as UDP packets over an IP network port to
the receiving UDP host.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — `'255.255.255.255'` (default) | any valid IP address

Specify the IP address or the host name to which the block sends the UDP packets. To
broadcast packets to all the receiving hosts, specify
`'255.255.255.255'`.

### **Remote IP port** — IP port on receiving host to which data is sent `25000` (default) | positive integer in the range [`1`,`65535`]

Specify the port number of the application on the receiving host to which you want
to send the packets. Match the remote port number with the local port number of the
receiving host.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Send UDP packets over IP network

The UDP Send block sends UDP packets to a UDP host. Use the block for
stateless and connectionless data transmission.

**Note**

Your antivirus software or firewall might block UDP traffic. Configure the software to
allow traffic from a specific IP port number.
