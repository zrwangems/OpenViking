---
type: simulink-block
title: 'UDP Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'freescalefrdmk64fboard/ref/udpreceive.html'
language: en
---

# UDP Receive

## Ports

### Output

### **Data** — Output UDP message received from the sending UDP host vector

At each sample time, the port outputs the data bytes of a message
received as a data vector of the size that you specify in the **Data
size (N)** parameter. For more information, see Receive UDP messages.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — Number of data bytes in the UDP message received scalar

At each sample time, the port outputs the number of data bytes
in the received message. For more information, see Receive UDP messages.

**Data Types:** `uint16`

## Parameters

### **Local IP Port** — IP port on the receiving UDP host `25000` (default) | `Any integer between 1 and 65535`

Specify the port number of the application on which you want
to receive the message. Match the local port number with the remote
port number of the sending host.

### **Data type** — Data type of the data bytes in UDP message `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type in which the block receives the data bytes
from the sending host.

### **Data size (N)** — Number of data bytes in each UDP message `1` (default)

Specify the number of data bytes that you want to receive in
each message.

### **Wait until data received** — Wait until the requested data is available off (default) | on

- `on` — When you select this
  parameter, the read operation runs in the **Blocking
  mode**. The read operation is blocked while waiting for the
  requested data to be available. If data is available, the `Data` port
  outputs data. If data is not available, the `Data` port
  waits for data. While the block waits for new data to arrive, the `Size` port
  outputs `0`. When the new data arrives, the value
  at the `Size` port changes to a nonzero value.

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
  contains the message it received in the previous time step. The `Size` port
  outputs `0`. In this mode, the block does not wait
  for the requested data to be available.

### **Sample time** — How often this block reads messages from the sending UDP host `0.1` (default)

When you specify this parameter as`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Receive UDP messages

This example describes the values at the output ports when the length of the messages received
is less than, greater than, or equal to the length of requested data. This section
explains the values at the output ports, with **Data type** set to
`uint8` and **Data size (N)** set to
`4`.

- **Length of UDP message received
  = Data size (N)**: The `Data` port outputs
  the message as a data vector of the size specified in the **Data
  size (N)** parameter.

  The `Size` port outputs the number of data
  bytes received.

  Suppose that the **Data size (N)** parameter
  specified is 4 and the length of the message received is also 4.

  In this case, the `Data` port outputs a data
  vector of size 4 filled with the data bytes of the message.

  The value at the `Size` port is `4`.
- **Length of UDP message received
  < Data size (N)**: The `Data` port outputs
  the message as a data vector of the size specified in the **Data
  size (N)** parameter. All the empty spaces in the vector
  are filled with random values.

  The `Size` port outputs the number of data
  bytes received (excluding random values).

  Suppose that the **Data size (N)** parameter
  specified is 4 and the length of data received is 3 bytes.

  In this case, the `Data` port outputs a data
  vector of size 4. The first three data bytes in the vector are the
  bytes from the received message. The remaining space is filled with
  a random value.

  The value at the `Size` port is `3`.
- **Length of UDP message received
  > Data size (N)**: The `Data` port outputs
  a data vector of the size specified in the **Data size (N)** parameter.
  The vector contains only the first *N* data bytes
  from the message. The remaining data bytes are dropped.

  The `Size` port outputs the number of data
  bytes received (including the output data bytes and the dropped data
  bytes).

  Suppose that the **Data size (N)** parameter
  specified is 4 and the length of data received is 5 bytes. In this
  case, the `Data` port outputs a data vector of size
  4. The vector contains only the first four data bytes from the received
  message. The remaining data byte is dropped. The value at the `Size` port
  is `4+1=5`.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Receive UDP message from UDP host

The UDP Receive block receives UDP message from
a UDP host.

With each sample, the block outputs the data bytes of a UDP
message as a data vector of the size that you specify in the **Data
size (N)** parameter.

The block receives the message on the port number specified
in the **Local IP Port** parameter. Match the port
number specified in the **Local IP Port** parameter
with the remote port number of the sending host.

You can choose to receive the UDP message in blocking or non-blocking
mode.

**Note**

If you are having trouble using UDP to communicate with a computer,
investigate if antivirus or firewall software is blocking UDP traffic.
If so, try to configure the software to allow the traffic for a specific
IP port number.
