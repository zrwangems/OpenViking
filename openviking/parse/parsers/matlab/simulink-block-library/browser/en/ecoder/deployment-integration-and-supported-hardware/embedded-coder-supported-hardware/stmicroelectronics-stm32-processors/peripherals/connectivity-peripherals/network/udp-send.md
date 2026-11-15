---
type: simulink-block
title: 'UDP Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'udpsendblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpsendblock.html'
language: en
---

# UDP Send

## Ports

### Input

### **data** — Send UDP packets to UDP host vector

The port accepts an array and sends it as UDP
packets over an IP network port to the receiving
host.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### Output

### **Status** — Determine if requested data is transmitted at given time step scalar

At each sample time, the port outputs
`0` when the length of data
transmitted is greater than or equal to the length
specified in the **Data size
(N)** parameter. A value of
`0` indicates that the requested
data is transmitted at the given time step.
Otherwise, it outputs a nonzero value, indicating
that no new data is available.

#### Dependencies

To enable this port, select the
**Output error status**
parameter.

**Data Types:** `uint16`

## Parameters

### **Remote IP address (255.255.255.255 for broadcast)** — IP address of receiving UDP host `0.0.0.0` (default)

Specify the IP address to which the block sends the
UDP packets. This parameter does not accept host
name as input. To broadcast packets to all the
receiving hosts, specify
`255.255.255.255`.

### **Local IP Port** — IP port on sending UDP host `25010` (default) | `-1`

Specify the port number of the application from which
you want to send the packets.

The value, `-1`, sets the local port
number to a random available port number and uses
that port to send the packets. If the receiving host
expects UDP packets from a particular port number,
specify that number.

### **Remote IP Port** — IP port on receiving UDP host `25002` (default) | `Any integer between 1 and 65535`

Specify the port number of the application on the
receiving host to which you want to send the
packets. Match the remote port number with the local
port number of the receiving host.

### **Wait until previous packet transmitted** — Wait until the packet received in previous time step is sent `off` (default) | `on`

- `on` — When you
  select this parameter, the send operation runs in
  the **Blocking
  mode**. If packet received in the
  previous time step is sent, the block accepts data
  from the input port. If the send operation is in
  progress, the block waits for the packet to be
  sent, and then it accepts data from the input
  port.

  If the connection between the sending and
  the receiving host is not established, or if the
  connection is lost, the data at the input port is
  dropped.

  A task overrun occurs if the target hardware
  is still waiting for the requested data to be sent
  when the next send operation is scheduled to
  begin. To fix overruns:

  - Increase the sample time of input
    data.
  - Reduce the length of data at the input
    port.
- `off` — When you
  clear this parameter, the send operation runs in
  the **Non-blocking
  mode**. When sending packets, if the
  transmission of the packets received in the
  previous time step is still in progress, the data
  at the input port at the given time step is
  dropped.

  If the connection between the sending and
  the receiving host is not established, or if the
  connection is lost, the data at the input port is
  dropped.

### **Output error status** — Option to display error status during data transmission `off` (default) | `on`

Select this parameter to display the error status
during data transmission.

When you select the Output error status parameter,
the block configures an output port. The port on the
block is labeled as Status, indicating that the
block outputs the status of the read operation at
the output port.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Send UDP packets to UDP host

The UDP Send block sends an input vector as UDP packets over an
IP network port to a UDP host. Use the block for stateless and
connectionless data transmission.

The block sends packets from the port number specified in the **Local
IP Port (-1 for automatic port assignment)** parameter.

Specify the IP address and the port number of the receiving host in the
**Remote IP address (255.255.255.255 for
broadcast)** and **Remote IP Port**
parameter.

You can choose to send the UDP packets in blocking or non-blocking
mode.

**Note**

Ensure to configure the Ethernet options in STM32CubeMX
project. For more, see Configure Ethernet Options in STM32CubeMX for STM32 Processor Based Boards.
