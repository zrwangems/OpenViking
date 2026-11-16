---
type: simulink-block
title: 'UDP Send'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'udpsend'
documentation_source_path: 'nvidia/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data port vector

The port accepts an array and sends it as UDP packets over an IP
network port to the receiving UDP host.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address of receiving UDP host `'255.255.255.255'` (default) | `any valid IP address`

Specify the IP address or the host name to which the block sends the UDP
packets. To broadcast packets to all the receiving hosts, specify
`'255.255.255.255'`.

### **Remote IP port** — IP port on receiving host to which data is sent `25000` (default) | positive integer in the range [1,65535]

Specify the port number of the application on the receiving host to which
you want to send the packets. Match the remote port number with the local
port number of the receiving host.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Send UDP packets to UDP host

The UDP Send block sends UDP packets to a UDP host. Use the block for stateless and
connectionless data transmission.

The IP address and the port number of the receiving host are specified in the
**Remote IP address (255.255.255.255 for broadcast)** and
**Remote IP Port** parameters.

The block accepts input with data type `int8`,
`uint8`, `int16`, `uint16`,
`int32`, `uint32`, `single`, or
`double`.

**Note**

Your antivirus software or firewall might block UDP traffic. Configure the
software to allow traffic from a specific IP port number.
