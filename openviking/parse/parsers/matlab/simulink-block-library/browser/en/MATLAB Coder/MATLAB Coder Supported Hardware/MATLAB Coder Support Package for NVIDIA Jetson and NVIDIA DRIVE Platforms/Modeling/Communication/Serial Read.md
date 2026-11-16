---
type: simulink-block
title: 'Serial Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'serialread'
documentation_source_path: 'nvidia/ref/serialread.html'
language: en
---

# Serial Read

## Ports

### Output

### **Data** — Output port to read data [Nx1] array

The data port through which the block reads the data from the serial
device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — Status of read operation `scalar`

This output port shows the status of the read data. This table lists
the possible status values and their description.

| Status Value | Status Description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `RX_BUSY` |
| `2` | `TX_BUSY` |
| `4` | `PARITY_ERROR` |
| `8` | `FRAME_ERROR` |
| `16` | `BUS_ERROR` |
| `32` | `DATA_NOT_AVAILABLE` |

#### Dependencies

This output port is available only if the **Output
partially received data** option is not
selected.

**Data Types:** `uint8`

### **Length** — Number of data bytes received scalar

The **Length** port outputs the number of data bytes
in the received message.

#### Dependencies

This output is available only if the **Output partially
received data** option is selected.

**Data Types:** `uint8`

## Parameters

#### Main Tab

### **Port** — Port at which you connect board to serial device `/dev/ttyTHS1` (default)

The port at which you connect the NVIDIA
Jetson board to the serial device.

### **Baudrate (in bits/s)** — Bits per second `9600` (default) | `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

Select the rate at which the data is read over the serial line. The baud
rate is measured as the number of bits read per second.

### **Parity** — Parity added to data to detect error `None` (default) | `Even` | `Odd`

Select the parity you want to add to the transmitted data. A parity bit is
used to detect error in the data transmission.

- **None** – This value means that no parity is
  used for error detection in the data transmission.
- **Even** – The parity bit value is 1 if the
  number of bits with value 1 is odd. The parity bit value is 0 if the
  number of bits with value 1 is even.
- **Odd** – The parity bit value is 1 if the number
  of bits with value 1 is even. The parity bit value is 0 if the
  number of bits with value 1 is odd.

### **Stop bits** — Bits used to signal stop of data transmission `1` (default) | `2`

Select the number of bits used to signal the stop of data
transmission.

### **Data length (N)** — Data length for transmission `1` (default) | `scalar`

Enter the data size of the data that you want to read from the serial
device for the selected data type.

### **Data type** — Data type for transmission `uint8` (default) | `uint16` | `uint32` | `int8` | `int16` | `int32` | `single` | `double`

Select the data type you want to read.

### **Sample time** — Time frequency at which block reads data `0.1` (default) | `scalar`

Specify how often the block should read the serial data. Enter a value
greater than zero.

#### Advanced Tab

### **Wait until data received** — Wait until the requested data is available off (default) | on

- `on` — When you select this parameter, the
  read operation runs in *blocking* mode. The read
  operation is blocked while waiting for the requested data to be
  available. If data is available, the `Data` port
  outputs data. If data is not available, the `Data`
  port waits for data.

  A task overrun occurs if the target hardware is still waiting for
  the data to be available when the next read operation is scheduled
  to begin.

  To fix overruns:

  - Increase the time step by using the **Sample
    time** parameter.
  - Reduce the length of data requested by using the
    **Data length (N)** parameter.
- `off` — When you clear this parameter, the
  read operation runs in *nonblocking* mode. When
  reading data, if data is not available, the `Data`
  port outputs zeros. The `Status` port outputs
  `32`, indicating that no new data is
  available.

### **Timeout in seconds** — Amount of time block waits until data is received `5` (default)

Specify the amount of time that the block should wait for the data during
each time step if the **Wait until data received**
parameter is selected. If timeout occurs, the read operation is aborted.

#### Dependencies

To enable this parameter, select **Wait until data
received** parameter.

### **Output partially received data** — Output data even if complete data is not available at sample time `off` (default) | `on`

- `on` — When you select this parameter, the
  `Data` port outputs partially received data at
  the sample time.
- `off` — When you clear this parameter, the
  `Data` port outputs zeros at every sample time
  till the requested number of data elements is received.

#### Dependencies

To enable this parameter, clear the **Wait until data
received** parameter to run the read operation in
nonblocking mode. For more information, see Partially receive data from serial port.

### Partially receive data from serial port

The Serial Read block can receive partial data when you enable the
**Output partially received data** parameter. This section
describes the values at the `Length` output port when the length of
the messages received is less than, greater than, or equal to the length of the
requested data. For an example, the values at the output ports with the
**Data type** set to `uint8` and the
**Data size (N)** set to `4`.

- Length of data received = Data length (N): The `Data`
  port outputs the message as a data vector of the size specified in the
  **Data size (N)** parameter.

  Suppose that the **Data size (N)** parameter specified is
  `4` and the length of the message received is also
  `4`.

  In this case, the `Data` port outputs a data vector of
  size 4 filled with the data bytes of the message and the
  `Length` port outputs `4`.

  Receive buffer when length of data received is equal to value specified for data size N
- Length of data received < Data length (N): The `Data`
  port outputs the message as a data vector of the size specified in the
  **Data size (N)** parameter. All the empty spaces in
  the vector are filled with zeros.

  Suppose that the **Data size (N)** parameter specified is
  `4` and the length of data received is
  `3` bytes.

  In this case, the `Data` port outputs a data vector of
  size `4`. The first three data bytes in the vector are the
  bytes from the received message and the remaining space is filled with zero.
  The `Length` port outputs `3`.

  Receive buffer when length of data received is less than the value specified for data size N. Space in buffer filled with zeros
- Length of data received > Data length (N): The `Data`
  port outputs a data vector of the size specified in the **Data size
  (N)** parameter. The vector contains only the first
  *N* data bytes from the message. The remaining data
  bytes are left in the buffer.

  Suppose that the **Data length (N)** parameter specified
  is `4` and the length of data received is
  `5` bytes. In this case, the port outputs a data vector
  of size `4`. The vector contains only the first
  `4` bytes from the received data. The remaining data
  byte is left in the buffer. The `Length` port outputs
  `4`.

  Receive buffer when length of data received is greater than the value specified for data size N. Additional data left in buffer

### Receive data from serial port

This section describes the values at the `Status` output port
when the length of the messages received is less than, greater than, or equal to the
length of the requested data. This section explains the values at the output ports
with **Data type** set to `uint8` and
**Data size (N)** set to `4` in blocking and
nonblocking modes.

- Length of data received = Data length (N): The `Data`
  port outputs the message as a data vector of the size specified in the
  **Data size (N)** parameter.

  Suppose that the **Data size (N)** parameter specified is
  `4` and the length of the message received is also
  `4`.

  In this case, for both blocking and nonblocking modes, the
  `Data` port outputs a data vector of size
  `4` filled with the data bytes of the message, and the
  `Status` port outputs `0`.

  Receive buffer when length of data received is equal to value specified for data size N
- Length of data received < Data length (N): The `Data`
  port outputs the message as a data vector of the size specified in the
  **Data size (N)** parameter. All the empty spaces in
  the vector are filled with .

  Suppose that the **Data size (N)** parameter specified is
  `4` and the length of data received is
  `3` bytes.

  For nonblocking mode, the `Data` port outputs a data
  vector of size `4`. The first three data bytes in the
  vector are the bytes from the received message. The remaining space is
  filled with zero. The `Status` port outputs
  `1`.

  For blocking mode, the block waits until all the data bytes are received
  within the time specified in the `Timeout` parameter. If
  the fourth data byte is not received before timeout, the
  `Data` outputs zeros and the `Status`
  port outputs `1`. The three received data bytes are left in
  the buffer.

  Receive buffer filled with zeros till all data bytes received
- Length of data received > Data length (N): The `Data`
  port outputs a data vector of the size specified in the **Data size
  (N)** parameter. The vector contains only the first
  *N* data bytes from the message. The remaining data
  bytes are left in the buffer.

  Suppose that the **Data length (N)** parameter specified
  is 4 and the length of data received is `5` bytes. In this
  case, for both blocking and nonblocking modes, the port outputs a data
  vector of size `4`. The vector contains only the first
  `4` bytes from the received data. The remaining data
  byte is left in the buffer. The `Status` port outputs
  zero.

  Receive buffer when length of data received is greater than the value specified for data size N. Additional data left in buffer

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Read data from serial port

Use the Serial Read block to read data from a serial device connected
to a NVIDIA®
Jetson™ board.

To open the serial pin map on the NVIDIA
Jetson board, click the **View pin map** button. For more
information, see Serial Port Mapping for NVIDIA Jetson Boards.

During Monitor and Tune, the block outputs results from the executable running on the
target hardware. During simulation in all other modes, the block outputs zeros.

You can choose to read the data in the blocking or the nonblocking mode. For more
information, see Partially receive data from serial port and Receive data from serial port
