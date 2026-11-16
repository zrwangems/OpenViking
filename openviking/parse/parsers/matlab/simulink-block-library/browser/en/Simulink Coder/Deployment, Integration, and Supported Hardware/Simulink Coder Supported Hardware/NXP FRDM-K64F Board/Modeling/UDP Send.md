---
type: simulink-block
title: 'UDP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'udpsend'
documentation_source_path: 'freescalefrdmk64fboard/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Send UDP messages to another UDP host vector

The port accepts an array and sends it as UDP messages over
an IP network port to the receiving host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Remote IP address (255.255.255.255 for broadcast)** — IP address of the receiving UDP host `192.168.1.2` (default)

Specify the IP address or the host name to which the block sends
the UDP messages. To broadcast messages to all the receiving hosts,
specify `255.255.255.255`.

### **Remote IP Port** — IP port on the receiving UDP host `25000` (default) | `Any integer between 1 and 65535`

Specify the port number of the application on the receiving
host to which you want to send the messages. Match the remote port
number with the local port number of the receiving host.

### **Local IP Port (-1 for automatic port assignment)** — IP port on the sending UDP host `-1` (default)

Specify the port number of the application from which you want
to send the messages.

The default value, `-1`, sets the local port
number to a random available port number and uses that port to send
the messages. If the receiving host expects UDP messages from a particular
port number, specify that number.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Send UDP message to UDP host

The UDP Send block sends an input vector as UDP
message over an IP network port to a UDP host.

The block sends messages from the port number specified in the **Local
IP Port (-1 for automatic port assignment)** parameter.

Specify the IP address and the port number of the receiving
host in the **Remote IP address (255.255.255.255 for broadcast)** and **Remote
IP Port** parameter.

The block sends the UDP messages in non-blocking mode.
