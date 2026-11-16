---
type: simulink-block
title: 'F2838x-M4 TCP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4tcpsend'
documentation_source_path: 'ref/f2838xm4tcpsend.html'
language: en
---

# F2838x-M4 TCP Send

## Ports

### Input

### **Port\_1** — Input data vector

The block accepts data specified as an *N*-by-1 array. The
block sends this data over a TCP/IP network to the receiving host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Length** — Receive data length scalar

The length of variable input message received.

#### Dependencies

To enable this port, select **Enable variable
length** parameter.

**Data Types:** `uint32`
### Output

### **Status** — Data transmitted at given time step scalar

The port outputs `0` if the data is transmitted at a given time
step. Otherwise, it outputs a nonzero value, indicating that data transmission is
not successful.

#### Dependencies

This parameter appears only when **Output transmit status**
parameter is enabled.

**Data Types:** `uint8`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as a TCP/IP server or client.

When you set connection mode parameter to `Server`, provide a
**Local IP Port**. The local port acts as the listening port on the
TCP/IP server.

When you set connection mode parameter to `Client`, provide the
**Server IP Address** and the **Server IP Port**
of the TCP/IP server to which you want to send the data.

### **Server IP Address** — Remote IP address of server to which to send data is sent `192.168.1.10` (default) | `any valid IP address`

Specify the remote IP address of the receiving server to which the data is
sent.

#### Dependencies

This parameter appears only when **Connection mode** parameter
is set to `Client`.

### **Server IP Port** — Remote IP port on server to which data is sent `25002` (default) | positive integer in the range [1,65535]

Specify the port number on the receiving server to which data is sent.

#### Dependencies

This parameter appears only when **Connection mode** parameter
is set to `Client`.

### **Local IP Port** — IP port on sending host from which to send data `25000` (default) | positive integer in the range [1,65535]

Specify the port number of the application from which to send the data. This local
port acts as the listening port of the TCP/IP server.

### **Enable variable length** — Enable to receive variable data length `off` (default) | `on`

When you select the **Enable variable length**
parameter, the block configures an input port, **Length**.

### **Wait until previous packet transmitted** — Wait until data received in previous time step is sent `off` (default) | `on`

- `on` — When you select this parameter, the send
  operation runs in the blocking mode. In this mode, if the block is still
  transmitting the packets received in the previous time step, the block retains the
  data at the input port in the current time step and waits to send it.

  A task overrun occurs if the target hardware is still waiting for the
  requested data to be sent when the next send operation is scheduled to begin. To
  fix overruns increase the time step by using the **Sample time**
  parameter.
- `off` — When you clear this parameter, the send
  operation runs in the nonblocking mode. In this mode, if the block is still
  transmitting the packets received in the previous time step, the data at the input
  port in the current time step is dropped.

  In either mode, if the block is yet to establish the connection between the
  sending and receiving hosts. or if the connection is lost, the data at the input
  port is dropped.

### **Output transmit status** — Option to display the transmit status during data transmission `off` (default) | `on`

Select this option to display the transmit status during data
transmission.

When you select the Output transmit status parameter, the block configures an
output port. The port on the block is labeled as Status, indicating that the block
outputs the status of the transmit operation at the output port.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Send data over TCP/IP network to remote host

The TCP Send block sends data to a remote host or another hardware board
over a TCP/IP network. The server must be up and running before deploying the model that
contains the TCP Send block to the target.

The block sends data either in blocking mode or in non-blocking mode. In blocking mode,
the model blocks the execution while it waits for the data to be sent completely. In
non-blocking mode, the model runs continuously. To set the block in blocking mode, select
the **Wait until previous packet transmitted** option.

**Note**

- Your antivirus software or firewall might block TCP traffic. Configure the
  software to allow traffic from a specific IP port number.
- Due to RAM memory limitations on the F2838x (ARM Cortex-M4), loading application
  to RAM is not supported for this block.
- CPU Timer 2 of F2838x Arm Cortex-M core (Connectivity Manager) provides time base
  to lwIP stack. It is configured to trigger an interrupt every 1 ms. This timer should
  not be re-configured if Ethernet blocks are being used in the model. If the
  corresponding interrupt is armed through Hardware Interrupt block, it will run the
  interrupt handler every 1 ms.
- When establishing TCP communication between TI C2000 and other targets like
  Raspberry Pi, configure TCP Send and TCP Receive blocks as either both client or both
  server to establish successful communication. Mixed configurations are not
  supported.
