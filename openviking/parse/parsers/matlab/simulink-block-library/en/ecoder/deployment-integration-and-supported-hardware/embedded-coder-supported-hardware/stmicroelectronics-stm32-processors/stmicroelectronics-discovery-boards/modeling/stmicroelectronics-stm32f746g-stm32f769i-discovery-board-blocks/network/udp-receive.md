---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Network'
documentation_page: 'udpreceive'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Output UDP packets received from the sending UDP host vector

At each sample time, the port outputs the contents of a packet received as a data vector of
the size that you specify in the **Data size (N)** parameter. For
more information, see Receive UDP Packets.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Determine if requested data is received at the given time step scalar

At each sample time, the port outputs `0` when
the length of data received is greater than or equal to the length
specified in the **Data size (N)** parameter. A value
of `0` indicates that the requested data is received
at the given time step. Otherwise, it outputs a nonzero value, indicating
that no new data is available.

For more information, see Receive UDP Packets.

**Data Types:** `uint16`

## Parameters

### **Local IP Port** — IP port on the receiving UDP host `25000` (default) | `Any integer between 1 and 65535`

Specify the port number of the application from which you want
to receive the packets. Match the local port number with the remote
port number of the sending host.

### **Remote IP address (0.0.0.0 for accepting all)** — IP address from which the block receives UDP packets `0.0.0.0` (default)

Specify the IP address of the remote host from which the block
receives packets. To receive packets from all the sending hosts, specify `0.0.0.0`.

### **Data type** — Data type of the elements in UDP packets `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type in which the block receives the elements
from the sending host. The size of each element depends on its data
type.

### **Data size (N)** — Number of data elements in each UDP packet `1` (default)

Specify the number of elements that you want to receive in each
packet.

### **Wait until data received** — Wait until the requested data is available on (default) | off

- `on` — When you select this
  parameter, the read operation runs in the **Blocking
  mode**. The read operation is blocked while waiting for the
  requested data to be available. If data is available, the `Data` port
  outputs data. If data is not available, the `Data` port
  waits for data.

  A task overrun occurs if the target hardware is still waiting
  for the data to be available when the next read operation is scheduled
  to begin.

  To fix overruns:

  - Increase the time step by using the **Sample
    time** parameter.
  - Reduce the length of data requested by using the **Data
    size (N)** parameter.
- `off` — When you clear this
  parameter, the read operation runs in the **Non-blocking
  mode**. When reading data, if data is not available, the `Data` port
  contains the packet received in the previous time step. In this mode,
  the block does not wait for the requested data to be available.

### **Sample time** — How often this block reads packets from the sending UDP host `-1` (default)

When you specify this parameter as`-1`, Simulink®
determines the best sample time for the block based on the block context
within the model.

### Receive UDP Packets

This example describes the values at the output ports when the length
of the packets received is less than, greater than, or equal to the
length of requested data.

- **Length of UDP packet
  received = Data size (N)**: The
  `Data` port outputs the packet as
  a data vector of the size specified in the
  **Data size (N)**
  parameter.

  The `Status` port outputs
  `0`, indicating that the
  requested data is received.

  Suppose that the **Data size
  (N)** parameter specified is 4 and the
  length of the packet received is also 4.

  In this case, the `Data` port
  outputs a data vector of size 4 filled with the
  elements of the packet.

  The value at the `Status`
  port is `0`.
- **Length of UDP packet
  received < Data size (N)**: The
  `Data` port outputs the packet as
  a data vector of the size specified in the
  **Data size (N)** parameter. All
  the empty spaces in the vector are filled with
  random values.

  The `Status` port outputs a
  nonzero value, indicating that no new data is
  received.

  Suppose that the **Data size
  (N)** parameter specified is 4 and the
  length of data received is 3 bytes.

  In this case, the `Data` port
  outputs a data vector of size 4. The first three
  elements in the vector are the elements from the
  received packet. The remaining space is filled
  with a random value.

  The `Status` port outputs a
  nonzero value.
- **Length of UDP packet
  received > Data size (N)**: The
  `Data` port outputs a data vector
  of the size specified in the **Data size
  (N)** parameter. The vector contains only
  the first *N* elements from the
  packet. The remaining elements are dropped.

  The `Status` port outputs
  `0`, indicating that the
  requested data is received.

  Suppose that the **Data size
  (N)** parameter specified is 4 and the
  length of data received is 5 bytes. In this case,
  the `Data` port outputs a data
  vector of size 4. The vector contains only the
  first four elements from the received packet. The
  remaining element is dropped. The value at the
  `Status` port is
  `0`.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Receive UDP packets from UDP host

The UDP Receive block receives UDP packets from
a UDP host. Use the block for stateless and connectionless data transmission.

With each sample, the block outputs the contents of a UDP packet
as a data vector of the size that you specify in the **Data
size (N)** parameter.

The block receives the packets on the port number specified
in the **Local IP Port** parameter from the IP address
specified in the **Remote IP address (0.0.0.0 for accepting
all)** parameter. To receive packets from all the sending
hosts, specify the remote IP address as `0.0.0.0`.
Match the port number specified in the **Local IP Port** parameter
with the remote port number of the sending host.

You can choose to receive the UDP packets in blocking or non-blocking
mode.

**Note**

- When DHCP is enabled with TCP/IP or UDP blocks
  in the model, the code waits in an infinite loop
  until IP is assigned to the board. Hence, user
  must ensure board is connected to router, if their
  model has any UDP/TCP block in their model with
  DHCP enabled
- If you are having trouble using UDP to
  communicate with a computer, investigate if
  antivirus or firewall software is blocking UDP
  traffic. If so, try to configure the software to
  allow the traffic for a specific IP port
  number.
