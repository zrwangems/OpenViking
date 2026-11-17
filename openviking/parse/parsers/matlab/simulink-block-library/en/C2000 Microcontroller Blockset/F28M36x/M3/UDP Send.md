---
type: simulink-block
title: 'UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'udpsend'
documentation_source_path: '../simulink/supportpkg/parrot_ref/udpsend.html'
language: en
---

# UDP Send

## Ports
```yaml
ports:
- name: Port1
  summary: Send UDP messages to another UDP host vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
```

### Input

### **Port1** — Send UDP messages to another UDP host vector

The port accepts an array and sends it as UDP messages over an IP
network port to the receiving host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Remote IP address
  summary: IP address of receiving UDP host 192.168.3.2 (default)
  group: ''
- name: Remote IP Port
  summary: IP port on the receiving UDP host 25000 (default) | [1, 65535]
  group: ''
- name: Local IP Port
  summary: IP port on the sending UDP host 2048 (default) | [1, 65535]
  group: ''
```

### **Remote IP address** — IP address of receiving UDP host `192.168.3.2` (default)

Specify the IP address or the host name to which the block sends the UDP
messages. The **Remote IP address** is set at 192.168.3.2;
do not change this IP address.

### **Remote IP Port** — IP port on the receiving UDP host `25000` (default) | [1, 65535]

Specify the port number of the application on the receiving host to which
you want to send the messages. Match the remote port number with the local
port number of the receiving host.

**Note**

Do not use ports `24099` and `26061`
for UDP communication with Parrot minidrone as these ports are
reserved.

### **Local IP Port** — IP port on the sending UDP host `2048` (default) | [1, 65535]

This parameter appears if you select the `Specify via
dialog` option for **Local IP port
source**. Specify the port number of the application from which
you want to send the messages.
## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Send UDP message to UDP host

The UDP Send block sends an input vector as UDP message over an IP
network port to a UDP host.

Specify the IP address and the port number of the receiving host in the
**Remote IP address** and **Remote IP Port**
parameter.
