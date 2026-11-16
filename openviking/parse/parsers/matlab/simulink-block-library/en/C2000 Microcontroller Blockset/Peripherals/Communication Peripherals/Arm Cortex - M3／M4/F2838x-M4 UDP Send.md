---
type: simulink-block
title: 'F2838x-M4 UDP Send'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4udpsend'
documentation_source_path: 'ref/f2838xm4udpsend.html'
language: en
---

# F2838x-M4 UDP Send

## Ports

### Input

### **Port\_1** — Input data port vector

The port accepts an array and sends it as UDP packets over an IP network to the
receiving UDP host.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Length** — Variable length scalar

The length of variable input message received

#### Dependencies

To enable this port, select **Enable variable
length** parameter.

**Data Types:** `uint32`

## Parameters

### **Remote IP address (255.255.255.255 for broadcast)** — IP address of receiving UDP host `192.168.1.10` (default) | `255.255.255.255`

Specify the IP address or the host name to which the block sends the UDP packets.
To broadcast packets to all the receiving hosts, specify
`255.255.255.255`.

### **Remote IP Port** — IP port on receiving UDP host `25000` (default) | positive integer in the range `[1,65535]`

Specify the port number of the application on the receiving host to which you want
to send the packets. Match the remote port number with the local port number of the
receiving host.

### **Local IP Port (-1 for automatic port assignment)** — IP port on sending UDP host `-1` (default) |

Specify the port number of the application from which you want to send the
packets.

When you specify the default value of `-1`, the block randomly
selects a port from the available ports to send the data. If the receiving host
expects UDP packets from a particular port number, specify the number of that
port.

### **Enable variable length** — Variable length `off` (default) | `on`

When you select the **Enable variable length**
parameter, the block configures an input port, **Length**.

### **Wait until previous packet transmitted** — Wait to sent new packets off (default) | on

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

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Send UDP packets to UDP host

The UDP Send block sends UDP packets to a UDP host. Use the block for stateless and
connectionless data transmission.

The block sends packets from the port number specified in the **Local IP Port
(-1 for automatic port assignment)** parameter. The IP address and the port
number of the receiving host are specified in the **Remote IP address
(255.255.255.255 for broadcast)** and **Remote IP Port**
parameters.

You can choose to send UDP packets in the blocking or nonblocking mode.

**Note**

- Your antivirus software or firewall might block UDP traffic. Configure the
  software to allow traffic from a specific IP port number.
- Due to RAM memory limitations on the F2838x (ARM Cortex-M4), loading application
  to RAM is not supported for this block.
- CPU Timer 2 of F2838x Arm Cortex-M core (Connectivity Manager) provides time base
  to lwIP stack. It is configured to trigger an interrupt every 1 ms. This timer should
  not be re-configured if Ethernet blocks are being used in the model. If the
  corresponding interrupt is armed through Hardware Interrupt block, it will run the
  interrupt handler every 1 ms.
