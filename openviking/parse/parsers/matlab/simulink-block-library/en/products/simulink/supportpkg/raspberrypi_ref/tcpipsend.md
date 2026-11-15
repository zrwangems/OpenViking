---
type: simulink-block
title: 'TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'tcpipsend'
documentation_source_path: 'supportpkg/raspberrypi_ref/tcpipsend.html'
language: en
---

# TCP/IP Send

## Ports

### Input

### **Port1** — Input port to accept data [Nx1] array

The block accepts data as an [Nx1] array.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

#### Main Tab

### **Connection mode** — Option to set the block as client or server `Client` (default) | `Server`

Select this option to set the block as TCP/IP client or TCP/IP
server.

### **Local IP port** — Local port acting as the listening port of the server 25000 (default) | scalar

Enter the local port number which acts as the listening port of the TCP/IP server. This
parameter appears only when you set the **Connection mode**
to `Server`.

### **Remote IP address** — Remote address of the server to which to send the data 127.0.0.1 (default) | scalar

Enter the remote server address to which to send the data. This
parameter appears only when you set the **Connection mode** to `Client`.

### **Remote IP port** — Remote port of the server to which to send data 25000 (default) | scalar

Enter the remote server port. This parameter appears only when
you set the **Connection mode** to `Client`.

#### Advanced Tab

### **Manually specify local IP port** — Manually specify the number of the local IP port off (default) | on

Allow manual specification of local IP port from which to send
data. This parameter appears only when you set the **Connection
mode** to `Client`.

### **Local IP port** — Local port from which to send the data 25000 (default) | scalar

Enter the local port of the client to send data. This parameter
appears only when you set the **Connection mode** to `Client` and
select the check box **Manually specify local IP port**.

### **Wait until previous packet transmitted** — Option to set for the block to wait for the data to be sent off (default) | on

Select this option to specify for block to wait for the current
data to be sent. Selecting this check box enables the ‘blocking
mode’.

### **Timeout in seconds** — Time to wait until the data is sent 0.1 (default) | scalar

Specify the time the block waits for the data to be sent during
each simulation time step. This field is unavailable, if you have
not selected **Wait until previous packet transmitted** parameter.
Enter `inf` value in this parameter, if you want
the block to wait indefinitely until it sends the data.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication Simulink Support Package for Android Devices / Communication Simulink Support Package for LEGO MINDSTORMS EV3 Hardware Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Send data over TCP/IP network to another remote host

Send data to a remote host/another hardware board over the network.
You can set the connection mode of the block as a server or a client.
When you set connection mode as TCP/IP client, you must provide the
remote address and the remote IP port of the TCP/IP server to which
you have to send the data. When you set the block as a TCP/IP server,
you must provide the local IP port of the TCP/IP server. This IP port
acts as the listening port of the TCP/IP server.
