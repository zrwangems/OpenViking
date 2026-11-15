---
type: simulink-block
title: 'TCP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'tcpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/tcpsend.html'
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
port on the TCP/IP server.

When you set this parameter to `Client`, you must provide
the **Server IP Address** and the **Server IP
Port** on the TCP/IP server to which you want to send the
data.

### **Server IP Address** — Remote IP address of server to which to send data is sent `192.168.1.2` (default) | any valid IP address

Specify the remote IP address of the receiving server to which the data is
sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Server IP Port** — Remote IP port on server to which data is sent `25000` (default) | any integer from 1 to 65,535

Specify the port number on the receiving server to which data is
sent.

#### Dependencies

This parameter appears only when you set the **Connection
mode** parameter to
`Client`.

### **Local IP Port** — IP port on sending host from which to send data `25000` (default) | any integer from 1 to 65,535

Specify the port number of the application from which to send the data.
This local port acts as the listening port of the TCP/IP server.

### **Wait until previous packet transmitted** — Wait until data received in previous time step is sent `on` (default) | `off`

- When you select this parameter, the send operation runs in
  blocking mode. If the send operation of the data received in the
  previous time step is complete, the block accepts data from the
  input port. If the send operation is in progress, the block waits
  for the data to be sent and then it accepts data from the input
  port.

  A task overrun occurs if the target hardware is still waiting for
  the requested data to be sent when the next send operation is
  scheduled to begin. To fix overruns:

  - Increase the sample time of input data.
  - Reduce the length of data at the input port.
- When you clear this parameter, the send operation runs in the
  non-blocking mode. If the send operation of the data received in the
  previous time step is still in progress, the data at the input port
  at the given time step is discarded.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Send data over TCP/IP network to remote host

The TCP Send block sends data to a remote host or another hardware
board over a TCP/IP network. You can set the **Connection mode** of the
block to `Server` or `Client`. When you set
**Connection mode** to `Client`, you must provide
the **Server IP Address** and the **Server IP Port**
on the server to which you want to send data. When you set **Connection
mode** to `Server`, you must provide the **Local
IP Port**. This **Local IP Port** acts as a listening port
on the TCP/IP server. The server must be up and running before deploying the model that
contains the TCP Send block to the target.

The block sends data either in blocking mode or in non-blocking mode. In blocking
mode, the model blocks the execution while it waits for the data to be sent completely.
In non-blocking mode, the model runs continuously. To set the block in blocking mode,
select the **Wait until data received** option.

**Note**

When DHCP is enabled with TCP/IP or UDP blocks in the model, the code waits in
an infinite loop until IP is assigned to the board. Hence, user must ensure
board is connected to router, if their model has any UDP/TCP block in their
model with DHCP enabled.
