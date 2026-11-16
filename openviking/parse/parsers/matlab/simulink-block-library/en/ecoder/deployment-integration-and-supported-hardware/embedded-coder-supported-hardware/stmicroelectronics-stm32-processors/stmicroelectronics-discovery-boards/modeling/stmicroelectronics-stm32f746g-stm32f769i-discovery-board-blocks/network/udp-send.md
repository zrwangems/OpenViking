---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'udpsend'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpsend.html'
language: en
---

# UDP Send

## Ports

### Input

### **Port\_1** — Send UDP packets to UDP host vector

The port accepts an array and sends it as UDP packets over an
IP network port to the receiving host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## Parameters

### **Remote IP address (255.255.255.255 for broadcast)** — IP address of the receiving UDP host `192.168.1.2` (default)

Specify the IP address or the host name to which the block sends
the UDP packets. To broadcast packets to all the receiving hosts,
specify `255.255.255.255`.

### **Remote IP Port** — IP port on the receiving UDP host `25002` (default) | `Any integer between 1 and 65535`

Specify the port number of the application on the receiving
host to which you want to send the packets. Match the remote port
number with the local port number of the receiving host.

### **Local IP Port (-1 for automatic port assignment)** — IP port on the sending UDP host `-1` (default)

Specify the port number of the application from which you want
to send the packets.

The default value, `-1`, sets the local port
number to a random available port number and uses that port to send
the packets. If the receiving host expects UDP packets from a particular
port number, specify that number.

### **Wait until previous packet transmitted** — Wait until the packet received in the previous time step is sent on (default) | off

- `on` — When you select this
  parameter, the send operation runs in the **Blocking
  mode**. If packet received in the previous time step is sent,
  the block accepts data from the input port. If the send operation
  is in progress, the block waits for the packet to be sent, and then
  it accepts data from the input port.

  If the connection between the sending and the receiving host
  is not established, or if the connection is lost, the data at the
  input port is dropped.

  A task overrun occurs if the target hardware is still waiting
  for the requested data to be sent when the next send operation is
  scheduled to begin. To fix overruns:

  - Increase the sample time of input data.
  - Reduce the length of data at the input port.
- `off` — When you clear this
  parameter, the send operation runs in the **Non-blocking
  mode**. When sending packets, if the transmission of the
  packets received in the previous time step is still in progress, the
  data at the input port at the given time step is dropped.

  If the connection between the sending and the receiving host
  is not established, or if the connection is lost, the data at the
  input port is dropped.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Send UDP packets to UDP host

The UDP Send block sends an input vector as UDP
packets over an IP network port to a UDP host. Use the block for stateless
and connectionless data transmission.

The block sends packets from the port number specified in the **Local
IP Port (-1 for automatic port assignment)** parameter.

Specify the IP address and the port number of the receiving
host in the **Remote IP address (255.255.255.255 for broadcast)** and **Remote
IP Port** parameter.

You can choose to send the UDP packets in blocking or non-blocking
mode.

**Note**

When DHCP is enabled with TCP/IP or UDP blocks in the model,
the code waits in an infinite loop until IP is assigned to
the board. Hence, user must ensure board is connected to
router, if their model has any UDP/TCP block in their model
with DHCP enabled.
