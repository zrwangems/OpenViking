---
type: simulink-block
title: 'Serial Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'serialreceive'
documentation_source_path: 'freedomboard/ref/serialreceive.html'
language: en
---

# Serial Receive

## Ports

Not documented in R2025b.

## Parameters

**UART**
:   Select the UART for the serial communication interface.

**Data type**
:   Select the data type of the output data. You can choose from the options
    `double`, `single`,
    `int8`, `uint8`,
    `int16`, `uint16`,
    `int32`, `uint32` and
    `boolean`.

**Data length**
:   Specify the number of data bytes that you want to receive using the block. Enter
    a value greater than zero. This value defaults to a data length of
    `1` byte.

**Sample time**
:   Specify how often the block reads the data available on the UART, in seconds.
    This value defaults to a sample time of `0.1` seconds.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Receive an [Nx1] array of byte data on the UART

Receive an [Nx1] array of byte data on the UART that you select.

The Serial Receive block has two output ports, **Data** and
**Status**.

When length of the data received is greater than or equal to the length specified in
the **Data length** parameter:

- **Data** — This output port emits data values from the
  serial receive buffer.
- **Status** — This output port emits
  `1`.

When length of the data received is less than the length specified in the
**Data length** parameter:

- **Data** — This output port emits
  `0`.
- **Status** — This output port emits `0`.

The **Data** port emits values of the data type that you choose from
the **Data type** parameter.

The **Status** port emits `uint8` values.

During simulations without the hardware, this block emits zeroes. This block operates
in ‘non-blocking mode'.

The FRDM-KL25Z hardware has three UARTs, UART0, UART1, and UART2.

You can change the Tx pin, Rx pin, and baud for the selected UARTx Serial Interfaces,
and view the FRDM-KL25Z pin map from **Configuration Parameters > Hardware
Implementation pane > UARTx**.
