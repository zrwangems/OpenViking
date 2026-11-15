---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'udpreceiveblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpreceiveblock.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Output UDP packets received from UDP host vector

At each sample time, the port outputs the
contents of a packet received as a data vector of
the size that you specify in the **Data
size (N)** parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Determine if requested data is received at given time step scalar

At each sample time, the port outputs
`0` when the length of data
received is greater than or equal to the length
specified in the **Data size
(N)** parameter. A value of
`0` indicates that the requested
data is received at the given time step.
Otherwise, it outputs a nonzero value, indicating
that no new data is available.

For more information, see Receive UDP Packets.

#### Dependencies

To enable this port, select the
**Output error status**
parameter.

**Data Types:** `uint16`

## Parameters

### **Remote IP address (0.0.0.0 for accepting all)** — IP address from which block receives UDP packets `0.0.0.0` (default)

Specify the IP address of the remote host from which
the block receives packets. To receive packets from
all the sending hosts, specify
`0.0.0.0`.

### **Local IP Port** — IP port on receiving UDP host `25010` (default) | `Any integer between 1 and 65535`

Specify the port number of the application from which
you want to receive the packets. Match the local
port number with the remote port number of the
sending host.

### **Wait until data received** — Wait until requested data is available `off` (default) | `on`

- `on` — When you
  select this parameter, the read operation runs in
  the **Blocking
  mode**. The read operation is blocked
  while waiting for the requested data to be
  available. If data is available, the
  `Data` port outputs data. If data
  is not available, the `Data` port
  waits for data.

  A task overrun occurs if the target hardware
  is still waiting for the data to be available when
  the next read operation is scheduled to
  begin.

  To fix overruns:

  - Increase the time step by using the
    **Sample time** parameter.
  - Reduce the length of data requested by using
    the **Data size (N)**
    parameter.
- `off` — When you
  clear this parameter, the read operation runs in
  the **Non-blocking
  mode**. When reading data, if data is not
  available, the `Data` port
  contains the packet received in the previous time
  step. In this mode, the block does not wait for
  the requested data to be available.

### **Data type** — Data type of elements in UDP packets `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type in which the block receives the
elements from the sending host. The size of each
element depends on its data type.

### **Data size (N)** — Number of data elements in each UDP packet `1` (default) | `scalar`

Specify the number of elements that you want to
receive in each packet. The data size must be scalar
values.

### **Output error status** — Option to display the error status during data transmission `off` (default) | `on`

Select this parameter to display the error status
during data transmission.

When you select the Output error status parameter,
the block configures an output port. The port on the
block is labeled as Status, indicating that the
block outputs the status of the read operation at
the output port.

### **Sample time** — How often this block reads packets from the sending UDP host `-1` (default)

When you specify this parameter
as`-1`, Simulink® determines the best sample time for
the block based on the block context within the
model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Receive UDP packets from UDP host

The UDP Receive block receives UDP packets from a UDP host. Use
the block for stateless and connectionless data transmission.

With each sample, the block outputs the contents of a UDP packet as a
**(Nx1)** array.

The block receives the packets on the port number specified in the
**Local IP Port** parameter from the IP address
specified in the **Remote IP address (0.0.0.0 for accepting
all)** parameter. To receive packets from all the sending
hosts, specify the remote IP address as `0.0.0.0`. Match
the port number specified in the **Local IP Port**
parameter with the remote port number of the sending host.

You can choose to receive the UDP packets in blocking or non-blocking
mode.

**Note**

- Ensure to configure the Ethernet options in
  STM32CubeMX project. For more, see Configure Ethernet Options in STM32CubeMX for STM32 Processor Based Boards.
- If you are having trouble using UDP to communicate
  with a computer, investigate if antivirus or
  firewall software is blocking UDP traffic. If so,
  try to configure the software to allow the traffic
  for a specific IP port number.
