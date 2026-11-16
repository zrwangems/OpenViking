---
type: simulink-block
title: 'TCP Send'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'tcpsend'
documentation_source_path: 'freescalefrdmk64fboard/ref/tcpsend.html'
language: en
---

# TCP Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts data specified as an *N*-by-1
array. The block sends this data over a TCP/IP network to the receiving
host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP Port**. The local port acts as the listening
port of the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Remote IP Address** and the **Remote IP
Port** of the TCP/IP server to which you want to send the
data.

### **Remote IP Address** — Remote IP address of server to which to send data is sent `192.168.1.2` (default) | any valid IP address

Specify the remote IP address of the server to which the data is
sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Remote IP Port** — Remote IP port of server to which data is sent `25000` (default) | [1 to 65,535]

Specify the port number of the server to which data is sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Local IP Port** — IP port of sending host from which to send data `25001` (default) | [1 to 65,535]

Specify the port number of the application from which to send the data.
This local port acts as the listening port of the sending host.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Send data over TCP/IP network to remote host

The TCP Send block sends data to a remote host or another hardware
board over a wired network. You can set the **Connection mode** of the
block to `Server` or `Client`. When you set
**Connection mode** to `Client`, you must provide
the **Remote IP Address** and the **Remote IP Port**
of the server to which you want to send data. When you set **Connection
mode** to `Server`, you must provide the **Local
IP Port**. This **Local IP Port** acts as a listening port
of the TCP/IP server.
