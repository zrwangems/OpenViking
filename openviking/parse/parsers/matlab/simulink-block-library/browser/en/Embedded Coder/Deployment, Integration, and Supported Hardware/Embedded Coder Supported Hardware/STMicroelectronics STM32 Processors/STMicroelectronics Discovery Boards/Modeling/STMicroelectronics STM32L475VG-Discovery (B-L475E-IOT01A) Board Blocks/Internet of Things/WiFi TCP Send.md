---
type: simulink-block
title: 'WiFi TCP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'wifitcpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/wifitcpsend.html'
language: en
---

# WiFi TCP Send

## Ports

### Input

### **Input** — Input data vector

The block accepts data as an *N*-by-1 array. The
block sends this data over a TCP/IP network to the receiving
host.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set this parameter to `Server`, you must specify
**Local IP Port**. The local port acts as the listening
port on the TCP/IP server.

When you set this parameter to `Client`, you must specify
**Remote IP address** and the **Remote IP
port** on the TCP/IP server to which you want to send the data.
Before you deploy a model that includes a client WiFi TCP/IP
Send block, ensure that the server is up and running.

### **Local IP port** — IP port on sending host from which data is sent `25000` (default) | `positive integer in the range [1 to 65,535]`

Specify the port number of the application from which data is sent. This
local port acts as the listening port on the TCP/IP server.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Server`.

### **Remote IP address** — Remote IP address of server to which data is sent `192.168.1.2` (default) | `any valid IP address`

Specify the remote IP address of the server to which the data is
sent.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Client`.

### **Remote IP port** — Remote IP port on server to which data is sent `25000` (default) | `positive integer in the range [1 to 65,535]`

Specify the port number on the receiving server to which data is
sent.

#### Dependencies

To enable this parameter, set **Connection mode**
parameter to `Client`.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Send TCP/IP packets to another TCP/IP host on internet network

The WiFi TCP Send block sends data to a remote host or other hardware
board over a wireless network.

**Note**

Your antivirus software or firewall might block TCP traffic. Configure the
software to allow traffic from a specific IP port number.
