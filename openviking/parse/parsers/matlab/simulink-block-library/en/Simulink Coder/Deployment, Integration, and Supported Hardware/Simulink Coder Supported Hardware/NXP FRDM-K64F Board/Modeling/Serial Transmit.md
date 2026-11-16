---
type: simulink-block
title: 'Serial Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'serialtransmit'
documentation_source_path: 'freescalefrdmk64fboard/ref/serialtransmit.html'
language: en
---

# Serial Transmit

## Ports

### Input

### **Tx** — Accept data and send to the UART port vector

The port accepts values as an [Nx1] or [1xN] array from your
model.

The port sends the values to the UART port using the Tx pin on the
port. To specify the Tx pin for the UART Serial Interface, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Tx Pin**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### Output

### **Status** — Determine if the input data is sent to the UART at the given time step scalar

When you select the **Output status** parameter, the
`Status` port becomes available.

The port outputs `0` for a successful send operation.
A value of `0` indicates that the input data is sent to
the UART port at the given time step.

The port outputs `32` for an unsuccessful send
operation. A value of `32` indicates that the input
data received in the previous time step is not sent.

#### Dependencies

You can choose to display the status of the send operation only in
the non-blocking mode. To run the send operation in the non-blocking
mode, clear the **Wait until data received**
parameter. To make the `Status` port available,
select the **Output status** parameter, and then
click **Apply**.

**Data Types:** `uint8`

## Parameters

### **UART** — UART port for serial communication `0` (default) | `1` | `2` | `3`

Select the UART port on the board to which the block sends data. The
`Tx` port on the block sends the values to the UART
port using the Tx pin on the port. To specify the Tx pin for the UART Serial
Interface, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Tx Pin**.

### **Wait until data is sent** — Wait until the input data received in the previous time step is sent off (default) | on

- `on` — When you select this parameter, the
  send operation runs in the **Blocking
  mode**. If data received in the previous time step is
  sent, the block accepts data from the input port. If the send
  operation is in progress, the block waits for the data to be sent,
  and then it accepts data from the input port.

  A task overrun occurs if the input data received in the previous
  time is not sent when the next send operation is scheduled to begin.
  To fix overruns:

  - Increase sample time of the block.
  - Reduce the length of data at the input port.
- `off` — When you clear this parameter, the
  send operation runs in the **Non-blocking
  mode**. When sending data, if the transmission of the
  data received in the previous time step is still in progress, the
  data at the input port at the given time step is dropped.

#### Dependencies

When you select this parameter, the `Status` port is
hidden.

### **Output status** — Option to display the status of write operation off (default) | on

When you select this parameter, the `Status` port becomes
available.

The port outputs `0` for a successful send operation. A
value of `0` indicates that the input data is sent to the
UART port at the given time step.

The port outputs `32` for an unsuccessful send operation.
A value of `32` indicates that the input data received in
the previous time step is not sent.

#### Dependencies

You can choose to display the status of the send operation only in the
non-blocking mode. To run the send operation in the non-blocking mode,
clear the **Wait until data received** parameter. To
make the `Status` port available, select the
**Output status** parameter, and then click
**Apply**.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Send serial data to UART port

The Serial Transmit block sends serial data to the Universal
Asynchronous Receiver Transmitter (UART) port that is on the board.

To select the UART port, use the **UART** parameter.

To send the values to the UART port, use the Tx pin on the port. To specify the Tx
(transmitting) pin, go to **Configuration Parameters**  > **Hardware Implementation pane** > **UARTx** > **Tx Pin**.

The block inherits the data type from the signal at the input port.

During the external mode simulation, the block outputs the results from the executable
running on the target hardware.

During simulation in all other modes, the block outputs zeroes.
