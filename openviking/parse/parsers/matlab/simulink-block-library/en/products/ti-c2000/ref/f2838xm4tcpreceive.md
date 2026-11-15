---
type: simulink-block
title: 'F2838x-M4 TCP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4tcpreceive'
documentation_source_path: 'ref/f2838xm4tcpreceive.html'
language: en
---

# F2838x-M4 TCP Receive

## Ports

### Output

### **Data** — Output data vector

At each time step, the port outputs data as a vector of the size specified in
the **Data size (N)** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Requested data received at given time step scalar

The port outputs `0` if the data is received at a given time
step. Otherwise, it outputs a nonzero value, indicating that no new data is
available.

**Data Types:** `uint8`

### **Length** — Receive data length scalar

The length of variable output message received

#### Dependencies

To enable this port, select **Enable variable
length** parameter.

**Data Types:** `uint32`

## Parameters

### **Connection mode** — Set the block as server or client `Server` (default) | `Client`

Set the block as TCP/IP server or client.

When you set connection mode parameter to `Server`, provide a
**Local IP Port**. The local port acts as the listening port on the
TCP/IP server.

When you set connection mode parameter to `Client`, provide the
**Server IP Address** and the **Server IP Port**
of the TCP/IP server from which you want to receive the data.

### **Local IP Port** — IP port on receiving host from which data is received `25000` (default) | positive integer in the range [1,65535]

This local port number acts as a listening port on the TCP/IP server. Match the
local port number with the remote port number of the sending host.

### **Server IP Address** — Remote IP address of server from which data is received `192.168.1.10` (default) | any valid IP address

Specify the IP address of the sending server from which the data is
received.

#### Dependencies

This parameter appears only when **Connection mode** parameter
is set to `Client`.

### **Server IP Port** — Remote IP port on server from which data is received `25002` (default) | positive integer in the range [1,65535]

Specify port number on the sending server from which data is received.

#### Dependencies

This parameter appears only when **Connection mode** is set to
`Client`.

### **Data type** — Data type of received data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the elements in the TCP data received by the block. The
size of each element depends on its data type.

### **Enable variable length** — Enable to receive variable data length `off` (default) | `on`

When you select the **Enable variable length**
parameter, the block configures an output port, **Length**.

### **Data size (N)** — Number of data bytes in received data `1` (default) | positive integer

Specify number of data bytes to receive at each time step.

### **Maximum data size (N)** — Maximum length of data `1` (default) | positive integer

Specify the maximum length of data to receive.

#### Dependencies

To enable this parameter, select **Enable variable length**
parameter.

### **Wait until data received** — Wait until requested data is available `on` (default) | `off`

- `on` — When you select this parameter, the read
  operation runs in the blocking mode. The read operation is blocked when the block
  is waiting for the requested data. If data is available, the block outputs the
  data. If data is not available, the block waits for the data.

  A task overrun occurs if the target hardware is still waiting for the data
  when the next read operation begins.

  To fix overruns, increase the time step by using the **Sample
  time** parameter.
- `off` — When you clear this parameter, the read
  operation runs in the nonblocking mode. When reading data, if data is not
  available, the block contains the packet received in the previous time step (the
  block outputs 0). In this mode, the block does not wait for the requested data to
  be available.

### **Sample time** — Interval at which block reads data from sending host `0.1` (default) | nonnegative value

Specify how often the block should read the port buffer. Enter a value greater
than `0` or `-1` (for inherited sample time).

This value defaults to a sample time of `0.1` seconds. Smaller
values require the processor to complete the same number of instructions in less time,
and this can cause task overruns.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Receive data over TCP/IP network from remote host

The TCP Receive block receives data from a remote host or other target
hardware over a network. The server must be up and running before deploying the model that
contains the TCP Receive block to the target.

The block outputs data either in blocking mode or in non-blocking mode. In blocking
mode, the model blocks the execution while it waits for the requested data to be available.
In non-blocking mode, the model runs continuously. To set the block in blocking mode, select
the **Wait until data received** option.

At each time step, the **Data** port outputs data as a vector of the
size specified in the **Data size (N)** parameter. The
**Status** port outputs 0 or a nonzero value indicating whether new data
is received. 0 at the **Status** port indicates that a valid data is
received.

**Note**

- Your antivirus software or firewall might block TCP traffic. Configure the
  software to allow traffic from a specific IP port number.
- Due to RAM memory limitations on the F2838x(ARM Cortex-M4), loading application to
  RAM is not supported for this block.
- CPU Timer 2 of F2838x Arm Cortex-M core (Connectivity Manager) provides time base
  to lwIP stack. It is configured to trigger an interrupt every 1 ms. This timer should
  not be re-configured if Ethernet blocks are being used in the model. If the
  corresponding interrupt is armed through Hardware Interrupt block, it will run the
  interrupt handler every `1` ms.
- When establishing TCP communication between TI C2000 and other targets like
  Raspberry Pi, configure TCP Send and TCP Receive blocks as either both client or both
  server to establish successful communication. Mixed configurations are not
  supported.
