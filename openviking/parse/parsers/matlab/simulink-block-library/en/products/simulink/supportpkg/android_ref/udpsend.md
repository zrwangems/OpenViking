---
type: simulink-block
title: 'UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'udpsend'
documentation_source_path: 'supportpkg/android_ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Input data signal numeric vector

Input data signal, specified as a numeric vector. The block sends this data as UDP
data to the remote IP address at the remote IP port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32`

## Parameters

### **Remote IP address ('255.255.255.255' for broadcast)** — IP address of remote host `'255.255.255.255'` (default) | valid IP address

Specify the IP address of the remote host to which you want to send UDP data. To
broadcast the UDP message, use the default value, `'255.255.255.255'`.
Use the default IP address sparingly to avoid creating unnecessary broadcast traffic on
your network. Often, IP routers are configured to drop broadcast UDP packets sent to
this default IP address.

### **Remote IP port** — IP port number of remote host `25000` (default) | integer from 1 to 65,535

Specify the IP port number of the remote host to which you want to send UDP data.
The IP port number must be an integer from 1 to 65,535.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014a**

## Description

Send data over UDP network to remote host

Use the UDP Send block to send user datagram protocol (UDP) data to a
remote host.

**Note**

If you are having trouble using UDP to communicate between your host computer and your
Android® device, antivirus or firewall software might be blocking UDP traffic. In
this case, reconfigure the software to enable UDP traffic for a specific IP port
number.
