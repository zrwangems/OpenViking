---
type: simulink-block
title: 'Serial Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'serialreceive'
documentation_source_path: 'px4/ref/serialreceive.html'
language: en
---

# Serial Receive

## Ports

### Output

### **Data** — Data received from the UART or USART port vector

At each sample time, the **Data** port outputs the values read
from the UART or USART port.

The port outputs a data vector of the size that you specify in the **Data
length (N)** parameter.

For more information, see Receive data from serial port

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Determine if the requested data is received at the given time step scalar

The **Status** port outputs `0` when the length
of data received is greater than or equal to the length specified in the
**Data length (N)** parameter. A value of `0`
indicates a successful read operation.

Otherwise, it outputs `1`, indicating that no new data is
available.

#### Dependencies

In non-blocking mode, if the **Output partially received data**
option is checked, then the **Status** port is not available

**Data Types:** `uint8`

### **Length** — Number of data bytes received scalar

The **Length** port outputs the number of data bytes in the
received message. For more information, see Partially receive data from serial port.

#### Dependencies

This output is available only if the **Output partially received
data** option is checked.

**Data Types:** `uint8`

## Parameters

#### Main Tab

### **Port** — UART or USART port for serial communication `/dev/ttyACM0` (default) | `/dev/ttyS1` | `/dev/ttyS2` | `/dev/ttyS3` | `/dev/ttyS5` | `/dev/ttyS6`

Enter the name of the UART or USART port on the board from which the block reads
data. To view the mapping between UART/USART ports and the labels on the Pixhawk flight
controller, see Serial Port Names and Corresponding Labels on PX4 Flight Controller Boards.

### **Data type** — Data type of data read from the UART or USART port `uint8` (default) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

Select the data type in which the block receives data from the UART or USART
port.

### **Data length (N)** — Length of data read from the UART or USART port `1` (default) | any integer greater than or equal to 0

Specify the length of data that you want to receive at each sample time.

### **Sample time** — How often to read data from the UART or USART port `0.1` (default)

Specify how often the block reads data from the UART port. When you specify this
parameter as`-1`, Simulink determines the best sample time for the
block based on the block context within the model.

#### Advanced Tab

### **Wait until data received** — Wait until the requested data is available off (default) | on

- `on` — When you select this parameter, the read
  operation runs in the **Blocking mode**. The read
  operation is blocked while waiting for the requested data to be available. If data
  is available, the `Data` port outputs data. If data is not
  available, the `Data` port waits for data.

  A task overrun occurs if the target hardware is still waiting for the data to be
  available when the next read operation is scheduled to begin.

  To fix overruns:

  - Increase the time step by using the **Sample time**
    parameter.
  - Reduce the length of data requested by using the **Data length
    (N)** parameter.
- `off` — When you clear this parameter, the read
  operation runs in the **Non-blocking mode**. When
  reading data, if data is not available, the `Data` port outputs
  zeroes. The `Status` port outputs `32`, indicating
  that no new data is available.

### **Timeout in seconds** — Time to wait until the data is received `5` (default) | (0, 2^32/1000]

Specify the amount of time that the block waits for the data during each time step,
if the **Wait until data received** parameter is selected. If timeout
occurs, the read operation is aborted.

#### Dependencies

This parameter appears only when you select the **Wait until data
received** parameter.

### **Output partially received data** — Output the data even if the complete data is not available at the sample time off (default) | on

- `on` — When you select this parameter, the
  `Data` port outputs partially received data at the sample
  time.
- `off` — When you clear this parameter, the
  `Data` port waits for the next sample time so that the data for
  the whole Data Length (N) is received, and then only provides the output.

#### Dependencies

This parameter is visible only if the **Wait until data
received** option is unchecked (non-blocking mode). For more information,
see Partially receive data from serial port.

### Partially receive data from serial port

This example describes the values at the `Length` output port when the
length of the messages received is less than, greater than, or equal to the length of
requested data. This section explains the values at the output ports, with **Data
type** set to `uint8` and **Data size (N)** set
to `4` in non-blocking mode with the **Output partially received
data** option checked.

- Length of data received = Data length (N): The `Data` port outputs
  the message as a data vector of the size specified in the **Data size
  (N)** parameter.

  Suppose that the **Data size (N)** parameter specified is 4 and the
  length of the message received is also 4.

  In this case, the `Data` port outputs a data vector of size 4
  filled with the data bytes of the message, and the `Length` port
  outputs `4`.
- Length of data received < Data length (N): The `Data` port
  outputs the message as a data vector of the size specified in the **Data size
  (N)** parameter. All the empty spaces in the vector are filled with
  zeroes.

  Suppose that the **Data size (N)** parameter specified is 4 and the
  length of data received is 3 bytes.

  In this case, the `Data` port outputs a data vector of size 4. The
  first three data bytes in the vector are the bytes from the received message; the
  remaining space is filled with zero. The `Length` port outputs
  `3`.
- Length of data received > Data length (N): The `Data` port
  outputs a data vector of the size specified in the **Data size (N)**
  parameter. The vector contains only the first *N* data bytes from the
  message. The remaining data bytes are left in the buffer.

  Suppose that the **Data length (N)** parameter specified is 4 and
  the length of data received is 5 bytes. In this case, the port outputs a data vector of
  size 4. The vector contains only the first 4 bytes from the received data. The remaining
  data byte is left in the buffer. The `Length` port outputs
  `4`.

### Receive data from serial port

This example describes the values at the `Status` output port when the
length of the messages received is less than, greater than, or equal to the length of
requested data. This section explains the values at the output ports, with **Data
type** set to `uint8` and **Data size (N)** set
to `4` in blocking and non-blocking modes.

- Length of data received = Data length (N): The `Data` port outputs
  the message as a data vector of the size specified in the **Data size
  (N)** parameter.

  Suppose that the **Data size (N)** parameter specified is 4 and the
  length of the message received is also 4.

  In this case, for both blocking and non-blocking modes, the `Data`
  port outputs a data vector of size 4 filled with the data bytes of the message, and the
  `Status` port outputs `0`.
- Length of data received < Data length (N): The `Data` port
  outputs the message as a data vector of the size specified in the **Data size
  (N)** parameter. All the empty spaces in the vector are filled with
  zeroes.

  Suppose that the **Data size (N)** parameter specified is 4 and the
  length of data received is 3 bytes.

  For non-blocking mode, the `Data` port outputs a data vector of
  size 4. The first three data bytes in the vector are the bytes from the received
  message. The remaining space is filled with zero. The `Status` port
  outputs `1`.

  For blocking mode, the block waits till all the data bytes are received within the
  time specified in the `Timeout` parameter. If the fourth data byte is
  not received within the timeout, the `Data` outputs zeroes, and the
  `Status` port outputs `1`. The three received data
  bytes are left in the buffer.
- Length of data received > Data length (N): The `Data` port
  outputs a data vector of the size specified in the **Data size (N)**
  parameter. The vector contains only the first *N* data bytes from the
  message. The remaining data bytes are left in the buffer.

  Suppose that the **Data length (N)** parameter specified is 4 and
  the length of data received is 5 bytes. In this case, for both blocking and non-blocking
  modes, the port outputs a data vector of size 4. The vector contains only the first 4
  bytes from the received data. The remaining data byte is left in the buffer. The
  `Status` port outputs zero.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read data from UART or USART port on PX4 flight controller

The Serial Receive block reads data from the Universal Asynchronous
Receiver Transmitter (UART) port or the Universal Synchronous and Asynchronous Receiver
Transmitter (USART) port on the PX4® flight controller.

The block reads the values from the specified UART or USART port, and outputs the received
values as a N-by-1 array. The properties for each port for serial communication are mentioned
in the Configuration Parameters dialog box in Simulink® (go to **Configuration Parameters**  > **Hardware Implementation** > **/dev/tty**\* pane).

During the external mode simulation, the block outputs the results from the executable
running on the target hardware.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the specified serial port of
the hardware.

You can choose to read data in blocking or non-blocking mode. For more information, see
Partially receive data from serial port and Receive data from serial port.

**Note**

If you are using Cube Orange autopilot, then use `GPS2` for serial data
communication, as there might be issues using `TELEM1` or
`TELEM2` ports.
