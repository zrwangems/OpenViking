---
type: simulink-block
title: 'UDP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'udpsend'
documentation_source_path: 'beagleboneblue/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input port to accept data

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Remote IP address (‘255.255.255.255’ for broadcast)** — Remote IP address of the remote host 127.0.0.1 (default) | scalar

Enter the address or hostname of the IP node on the remote device.

To broadcast the UDP message to all devices, use the default
parameter value, `'255.255.255.255'`. Use this approach
sparingly to avoid creating unnecessary broadcast traffic. Often,
IP routers are configured to drop broadcast UDP packets sent to `'255.255.255.255'`.

### **Remote IP port** — Remote IP port number of the remote host 25000 (default) | scalar

The number of the IP port on the remote device, which can range
from 1 to 65535. This value defaults to `25000`.

### **Local IP port source** — Local IP port source from which the block sends data Automatically determine (default) | Specify

Select this option to determine the local port source from which
the block sends the data.

### **Local port** — Local port from which the block sends data 2048 (default) | scalar

Enter the local port from which the block sends the data to
the remote host.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

Not documented in R2025b.

## Description

Send UDP packets to another UDP host on Internet network

Send a UDP packet to a network address identified by the remote
IP address and remote IP port parameters.

**Note**

If you are having trouble using UDP to communicate with a computer,
investigate whether antivirus or firewall software might be blocking
UDP traffic. If so, try reconfiguring the software to allow UDP traffic
for a specific IP port number.
