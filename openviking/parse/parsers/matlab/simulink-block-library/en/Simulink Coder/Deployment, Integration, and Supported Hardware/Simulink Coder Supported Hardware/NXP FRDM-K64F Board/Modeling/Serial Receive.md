---
type: simulink-block
title: 'Serial Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'serialreceive'
documentation_source_path: 'freescalefrdmk64fboard/ref/serialreceive.html'
language: en
---

# Serial Receive

## Ports

### Output

### **Rx** — Output data received from the UART port vector

At each sample time, the **Rx** port outputs the
values read from the UART port using the Rx pin on the port. To specify
the Rx pin, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Rx Pin**.

The port outputs a data vector of the size that you specify in the
**Data length (N)** parameter. For more
information, see Receive data from UART port.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — Determine if the requested data is received at the given time step scalar

When you select the **Output status** parameter, the
`Status` port becomes available. The port outputs
`0` when the length of data received is greater
than or equal to the length specified in the **Data length
(N)** parameter. A value of `0` indicates
a successful read operation.

Otherwise, it outputs `32`, indicating that no new
data is available.

#### Dependencies

You can choose to display the status of the read operation only in
the non-blocking mode. To enable the non-blocking mode, clear the
**Wait until data received** parameter, and
then select the **Output status** parameter.

**Data Types:** `uint8`

## Parameters

### **UART** — UART port for serial communication `0` (default) | `1` | `2` | `3`

Select the UART port on the board from which the block reads data. At each
sample time, the `Rx` port on the block outputs the
values read from the UART port using the Rx pin on the port. To specify the
Rx pin, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Rx Pin**.

### **Data type** — Data type of data read from the UART port `uint8` (default) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

Select the data type in which the block receives data from the UART
port.

### **Data length (N)** — Length of data read from the UART port `10` (default) | any integer greater than or equal to 0

Specify the length of data that you want to receive at each sample
time.

### **Wait until data received** — Wait until the requested data is available off (default) | on

- `on` — When you select this parameter, the
  read operation runs in the **Blocking
  mode**. The read operation is blocked while waiting for
  the requested data to be available. If data is available, the
  `Rx` port outputs data. If data is not
  available, the `Rx` port waits for data. The
  `Status` port is hidden.

  A task overrun occurs if the target hardware is still waiting for
  the data to be available when the next read operation is scheduled
  to begin.

  To fix overruns:

  - Increase the time step by using the **Sample
    time** parameter.
  - Reduce the length of data requested by using the
    **Data length (N)** parameter.
- `off` — When you clear this parameter, the
  read operation runs in the **Non-blocking
  mode**. When reading data, if data is not available,
  the `Rx` port outputs zeroes. The
  `Status` port outputs `32`,
  indicating that no new data is available.

### **Output status** — Option to display the status of read operation on (default) | off

When you select this parameter, the `Status` port becomes
available.

The port outputs `0` when the length of data received is
greater than or equal to the length that you specify in the **Data
length (N)** parameter. A value of `0`
indicates a successful read operation.

Otherwise, it outputs `32`, indicating that no new data
is available.

#### Dependencies

You can choose to display the status of the read operation only in the
non-blocking mode. To enable the non-blocking mode, clear the
**Wait until data received** parameter, and then
select the **Output status** parameter.

### **Sample time** — How often to read data from the UART port `0.1` (default)

Specify how often the block reads data from the UART port. When you
specify this parameter as`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Receive data from UART port

This section explains the values at the output port, with the following block
parameters specified as:

| Block Parameter | Value |
| --- | --- |
| **Data type** | `uint8` |
| **Data length (N)** | `4` |

The value at the output port vary depending on whether the length of data received
is less than, greater than, or equal to the length of requested data.

- Length of data received = Data length (N): The `Rx`
  port outputs a data vector of the size specified in the **Data
  length (N)** parameter.

  Suppose that the **Data length (N)** parameter
  specified is 4 and the length of data received is also 4.

  In this case, the port outputs a data vector of size 4 filled with the
  bytes from the received data.
- Length of data received < Data length (N): The
  `Rx` port outputs a data vector of the size
  specified in the **Data length (N)** parameter filled
  with zeroes.

  Suppose that the **Data length (N)** parameter
  specified is 4 and the length of data received is 3 bytes.

  In blocking mode, the read operation is blocked while waiting for the
  fourth byte to be available.

  In non-blocking mode, the port outputs a data vector of size 4. All
  the spaces in the vector are filled with zeroes.
- Length of data received > Data length (N): The
  `Rx` port outputs a data vector of the size
  specified in the **Data length (N)** parameter. The
  vector contains only the first *N* bytes from the
  received data. The remaining data bytes are dropped.

  Suppose that the **Data length (N)** parameter
  specified is 4 and the length of data received is 5 bytes. In this case,
  the port outputs a data vector of size 4. The vector contains only the
  first 4 bytes from the received data. The remaining data byte is
  dropped.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read data from UART port

The Serial Receive block reads data from the Universal Asynchronous
Receiver Transmitter (UART) port on the board.

To select the UART port, use the **UART** parameter.

The block reads the values from the UART port, using the Rx (receiving) pin on the
port. To specify the Rx pin, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Rx Pin**.

During the external mode simulation, the block outputs the results from the executable
running on the target hardware.

During simulation in all other modes, the block outputs zeroes.

You can choose to read data in blocking or non-blocking mode.
