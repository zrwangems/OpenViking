---
type: simulink-block
title: 'UART/USART Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'uartusartwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/uartusartwrite.html'
language: en
---

# UART/USART Write

## Ports

### Input

### **Data** — UART/USART write data vector | scalar

The write data sent to the UART/USART port.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Length** — UART/USART message length scalar

The length of input data received at UART/USART port.

#### Dependencies

To enable this port, select the **Specify length of input
data to write** parameter.

**Data Types:** `uint8`
### Output

### **Status** — Status of write operation `0` | `7` | `8`

The status port outputs `0` i.e. no error in data
reception or Success or any one of the bit values shown in the following
table.

The table represents the bits and error associated with it.

**Status**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bits | `15` | `14` | `13` | `12` | `11` | `10` | `9` | `8` | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `0` |
| Error | X | X | X | X | X | X | ARBE\_ERROR | RX\_BUSY | TX\_BUSY | TX\_FAILED | RX\_BUFFER\_FULL | NOISE\_ERROR | FRAME\_ERROR | PARITY\_ERROR | OVERRUN ERROR | DATA\_NOT\_AVAILABLE |

Port outputs status `7(transmit failed)` and
`8(transmit busy)`which are valid only for
UART/USART Write blocks.

- 0 — requested data length not received
- 1 — represents overrun error
- 2 — represents parity error
- 3 — represents frame error
- 4 — represents noise error
- 5 — represents receive buffer full
- 6 — represents transmit failed
- 7 — represents transmit busy
- 8 — represents receive busy
- 9 — represents auto baud rate error

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `uint8`

## Parameters

### **UART/USART module** — UART/USART module `USART1` (default) | `USART2` | `USART3` | `UART4` | `UART5` | `USART6` | `UART7` | `UART8`

Select the UART/USART module for the block.

### **Specify length of input data to write** — Size of data to be read `off` (default) | on

Select the **Specify length of input data to write**
parameter to enable the port `length`.

### **Enable blocking mode** — Enable blocking mode for data transmission `off` (default) | on

- `On` - When you select this parameter, the write
  operation runs in the **Blocking
  mode**. If input data received in the previous time step is
  sent, the block accepts data from the input port. If the write
  operation is in progress, the block waits for the data to be sent,
  and then it accepts data from the input port.

  If the connection between the sending and the receiving host is
  not established, or if the connection is lost, the data at the input
  port is dropped.

  If previous byte transmit is already in progress, or the buffer is
  full (Buffered Mode), input data is not sent.
- `Off` - When you clear this parameter, the send
  operation runs in the **Non-blocking
  mode**. When sending data, if the transmission of the
  input data received in the previous time step is still in progress,
  the data at the input port at the given time step is dropped.

  If the connection between the sending and the receiving host is
  not established, or if the connection is lost, the data at the input
  port is dropped.

### **Blocking timeout (in s)** — Time in seconds for blocking mode `0.1` (default) | `non-negative value`

Specify the time in seconds for blocking mode.

#### Dependencies

To enable this parameter, select the **Enable blocking
mode** parameter.

### **Output status** — Enable output status `off` (default) | on

When you select the **Output Status**
parameter, the block configures an output port, **Status**. The port outputs the status of UART/USART
message.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Write serial data from the Universal Asynchronous Receiver Transmitter (UART/USART) port

Write serial data from the Universal Asynchronous Receiver/ Transmitter (UART/USART)
port.

The UART/USART Write block expects the data to be written as an [Nx1]
or [1xN] array. Select **Specify length of data to write** to specify
the length of input data to be written to the UART/USART port.
