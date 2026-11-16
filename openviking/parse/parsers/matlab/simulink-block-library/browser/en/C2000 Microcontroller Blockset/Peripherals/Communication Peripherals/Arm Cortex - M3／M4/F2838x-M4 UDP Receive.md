---
type: simulink-block
title: 'F2838x-M4 UDP Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4udpreceive'
documentation_source_path: 'ref/f2838xm4udpreceive.html'
language: en
---

# F2838x-M4 UDP Receive

## Ports

### Output

### **Data** — UDP packets received from sending UDP host vector

At each sample time, the port outputs the contents of a packet received as a
data vector of the size specified in the **Data size (N)**
parameter.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — Determine if requested data is received at the given time step scalar

The port outputs `0` (success) when the received number of data
elements is less than or equal to **Data size (N)** specified in
the block. Otherwise, it outputs a nonzero value, indicating that no new data is
available.

**Data Types:** `uint8`

### **Length** — Variable length scalar

The length of variable output message received

#### Dependencies

To enable this port, select **Enable variable
length** parameter.

**Data Types:** `uint32`

## Parameters

### **Local IP Port** — IP port on the receiving UDP host `25000` (default) | positive integer in the range `[1,65535]`

Specify the port number of the application from which you want to receive the
packets. Match the local port number with the remote port number of the sending
host.

### **Remote IP address (0.0.0.0 for accepting all)** — IP address from which the block receives UDP packets `192.1.168.10` (default) | `0.0.0.0`

Specify the IP address of the remote host from which the block receives packets.
To receive packets from all the sending hosts, specify
`0.0.0.0`.

### **Data type** — Data type of elements in UDP packets `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the elements in the UDP packets received by the block. The
size of each element depends on its data type.

### **Data size (N)** — Number of data elements in each UDP packet `1` (default)

Specify the number of elements that you want to receive in each packet.

Ensure the following conditions are considered when data is sent to UDP Receive in
the target to avoid data loss.

**Note**

- The UDP block can handle the maximum packet size (datagram size) of
  `1472` bytes. Ensure the packet size sent to the target is
  less than or equal to `1472` bytes.
- Ensure the size of the data sent to the target is less than or equal the
  packet size (datagram size).

### **Enable variable length** — Variable length `off` (default) | `on`

When you select the **Enable variable length**
parameter, the block configures an output port, **Length**.

### **Maximum data size (N)** — Maximum length of data `1` (default) | positive integer

Specify the maximum length of data to receive.

#### Dependencies

To enable this parameter, select **Enable variable length**
parameter.

### **Wait until data received** — Wait until requested data is available on (default) | off

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
  available, the block contains the packet received in the previous time step. In
  this mode, the block does not wait for the requested data to be available.

### **Sample time** — How often this block reads packets from the sending UDP host `0.1` (default)

Specify how often the block should read the port buffer. Enter a value greater
than `0` or `-1` (for inherited sample time).

This value defaults to a sample time of `0.1` seconds. Smaller
values require the processor to complete the same number of instructions in less time,
and this can cause task overruns.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 Instrument Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Receive UDP packets from UDP host

The UDP Receive block receives UDP packets from a UDP host. Use the block
for stateless and connectionless data exchange.

With each sample, the block outputs the contents of a UDP packet as a data vector of the
size specified in the **Data size (N)** parameter.

The block receives the packets on the port number specified in the **Local IP
Port** parameter from the IP address specified in the **Remote IP address
(0.0.0.0 for accepting all)** parameter.

You can choose to receive the UDP packets in the blocking or nonblocking mode.

**Note**

- Your antivirus software or firewall might block UDP traffic. Configure the
  software to allow traffic from a specific IP port number.
- Due to RAM memory limitations on the F2838x(ARM Cortex-M4), loading application
  to RAM is not supported for this block.
- CPU Timer 2 of F2838x Arm Cortex-M core (Connectivity Manager) provides time
  base to lwIP stack. It is configured to trigger an interrupt every 1 ms. This timer
  should not be re-configured if Ethernet blocks are being used in the model. If the
  corresponding interrupt is armed through Hardware Interrupt block, it will run the
  interrupt handler every 1 ms.
