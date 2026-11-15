---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/parrot_ref/tcpipsend.html'
language: en
---

# TCP/IP Send

## Ports

### Input

### **Port1** — Input port to accept data [Nx1] array

The block accepts data specified as an *N*-by-1
array. The block sends this data over a TCP/IP network to the receiving
host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

#### Main Tab

### **Connection mode** — Set block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set this parameter to `Server`, you must provide
a **Local IP port**. The local port acts as the listening
port of the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Remote IP port** of the TCP/IP server to which you
want to send the data.

### **Local IP port** — Local port acting as the listening port of the server `25000` (default) | [1, 65535]

Enter the local port number which acts as the listening port of the
TCP/IP server.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Server`.

### **Remote IP Address** — Remote IP address of server to which to send data `192.168.3.2` (default)

The remote IP address of the server to which the data is sent. The
**Remote IP address** is set at 192.168.3.2; do not
change this IP address.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Remote IP port** — Remote IP port of server to which data is sent `25000` (default) | [1, 65535]

Specify the port number of the server to which data is sent.

**Note**

Do not use ports `24099` and `26061`
for TCP/IP communication with Parrot minidrone as these ports are
reserved.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

#### Advanced Tab

### **Manually specify local IP port** — Manually specify the number of the local IP port off (default) | logical

Allow manual specification of local IP port from which to send data. This
parameter appears only when you set the **Connection mode**
to `Client`.

### **Local IP port** — Local port from which to send the data 25000 (default) | scalar

Enter the local port of the client to send data. This parameter appears
only when you set the **Connection mode** to
`Client` and select the check box
**Manually specify local IP port**.

## Libraries

Simulink Support Package for Parrot Minidrones

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Send data over TCP/IP network to remote host

The TCP/IP Send block sends data to a remote host over a Bluetooth® network. You can set the **Connection mode** of the block
to `Server` or `Client`. When you set
**Connection mode** to `Client`, you must provide
the **Remote IP port** of the server to which you want to send data.
When you set **Connection mode** to `Server`, you must
provide the **Local IP port**. This **Local IP port**
acts as a listening port of the TCP/IP server.
