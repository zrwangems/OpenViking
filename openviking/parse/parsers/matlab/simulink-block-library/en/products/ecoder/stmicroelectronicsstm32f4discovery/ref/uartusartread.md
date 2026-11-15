---
type: simulink-block
title: 'UART/USART Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'uartusartread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/uartusartread.html'
language: en
---

# UART/USART Read

## Ports

### Output

### **Data** — Output data vector | scalar

Outputs the read data from the UART/USART port.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Length** — UART/USART message length scalar

The port outputs the number of elements received.

#### Dependencies

To enable this port, select the **Output read
length** parameter.

**Data Types:** `uint8`

### **Status** — Status of read operation `0` | `1` | `2` | `3` | `4` | `...`

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
- 9 — represents arbe error

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `uint8`

## Parameters

### **UART/USART module** — UART/USART module `USART1` (default) | `USART2` | `USART3` | `UART4` | `UART5` | `USART6` | `UART7` | `UART8`

Select the UART/USART module for the block.

### **Data type** — Type of data to be read `uint8` (default) | `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

Select the type of the data the block reads from the host. The size of
each element depends on its data type.

### **Data length** — Size of data to be read `1` (default) | `scalar`

Specify the data length to receive.

Specify the number of elements that you want to receive in each data
length. The data length must be scalar values.

### **Enable blocking mode** — Enable blocking mode for data transmission `off` (default) | on

- `On` - When you select this parameter, the
  read operation runs in the **Blocking mode**.
  The read operation is blocked while waiting for the requested
  data to be available. If data is available, the
  `Data` port outputs data. If data is not
  available, the `Data` port waits for
  data.
- `Off` - When you clear this parameter, the
  read operation runs in the **Non-blocking
  mode**. When reading data, if data is not
  available, the `Data` port contains the data
  received in the previous time step. In this mode, the block does
  not wait for the requested data to be available.

### **Blocking timeout (in s)** — Time in seconds for blocking mode `0.1` (default) | `non-negative value`

Specify the time in seconds for blocking mode.

#### Dependencies

To enable this parameter, select the **Enable blocking
mode** parameter.

### **Output read length** — Enable output read length `off` (default) | on

The number of elements block received. When you select the **Output read length** parameter, the block
configures an output port, **length**.

### **Output status** — Enable output status `off` (default) | on

When you select the **Output Status**
parameter, the block configures an output port, **Status**. The port outputs the status of UART/USART
message.

### **Sample time** — Time interval at which block reads data `0.1` (default) | `-1` | `non-negative real value`

Specify how often the block receives message, in seconds. When you specify
this parameter as -1, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Read data from the Universal Asynchronous Receiver Transmitter (UART/USART) port

Read serial data from the Universal Asynchronous Receiver/ Transmitter (UART/USART)
port.

The UART/USART Read block outputs the read values as an [Nx1] array.
You can specify the data type and the data length that you want to read using the
block.
