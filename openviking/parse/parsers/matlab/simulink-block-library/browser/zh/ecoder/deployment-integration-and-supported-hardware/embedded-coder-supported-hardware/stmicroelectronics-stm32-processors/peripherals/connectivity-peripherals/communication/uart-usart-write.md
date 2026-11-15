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
language: zh-CN
chinese_source: worker-translation
---

# UART/USART Write

## 端口

### 输入

### **Data** — UART/USART 写入数据向量 | 标量

发送到 UART/USART 端口的写入数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Length** — UART/USART 消息长度标量

在 UART/USART 端口接收的输入数据长度。

#### 依赖项

要启用此端口，请选择 **指定要写入的输入数据长度** 参数。

**数据类型：** `uint8`
### 输出

### **Status** — 写入操作的状态 `0` | `7` | `8`

状态端口输出 `0`，即数据接收无错误或 Success，或下表中所示的任一位值。

该表表示位及其关联的错误。

**Status**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 位 | `15` | `14` | `13` | `12` | `11` | `10` | `9` | `8` | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `0` |
| 错误 | X | X | X | X | X | X | ARBE\_ERROR | RX\_BUSY | TX\_BUSY | TX\_FAILED | RX\_BUFFER\_FULL | NOISE\_ERROR | FRAME\_ERROR | PARITY\_ERROR | OVERRUN ERROR | DATA\_NOT\_AVAILABLE |

端口输出状态 `7(transmit failed)` 和 `8(transmit busy)`，这些状态仅对 UART/USART Write 模块有效。

- 0 — 未收到请求的数据长度
- 1 — 表示溢出错误
- 2 — 表示奇偶校验错误
- 3 — 表示帧错误
- 4 — 表示噪声错误
- 5 — 表示接收缓冲区已满
- 6 — 表示发送失败
- 7 — 表示发送忙
- 8 — 表示接收忙
- 9 — 表示自动波特率错误

#### 依赖项

要启用此端口，请选择 **输出状态** 参数。

**数据类型：** `uint8`

## 参数

### **UART/USART 模块** — UART/USART 模块 `USART1` (默认) | `USART2` | `USART3` | `UART4` | `UART5` | `USART6` | `UART7` | `UART8`

为该模块选择 UART/USART 模块。

### **指定要写入的输入数据长度** — 要读取的数据大小 `off` (默认) | on

选择 **指定要写入的输入数据长度** 参数以启用端口 `length`。

### **启用阻塞模式** — 为数据传输启用阻塞模式 `off` (默认) | on

- `On` - 选择此参数时，写入操作在 **阻塞模式** 下运行。如果上一时间步接收的输入数据已发送，则模块从输入端口接受数据。如果写入操作正在进行，模块会等待数据发送完成，然后从输入端口接受数据。

  如果发送主机与接收主机之间的连接未建立，或者连接丢失，则输入端口的数据会被丢弃。

  如果上一个字节传输已在进行中，或缓冲区已满（缓冲模式），则不会发送输入数据。
- `Off` - 清除此参数时，发送操作在 **非阻塞模式** 下运行。发送数据时，如果上一时间步接收的输入数据传输仍在进行中，则给定时间步输入端口的数据会被丢弃。

  如果发送主机与接收主机之间的连接未建立，或者连接丢失，则输入端口的数据会被丢弃。

### **阻塞超时（以 s 为单位）** — 阻塞模式的时间（以秒为单位） `0.1` (默认) | `non-negative value`

指定阻塞模式的时间（以秒为单位）。

#### 依赖项

要启用此参数，请选择 **启用阻塞模式** 参数。

### **输出状态** — 启用输出状态 `off` (默认) | on

选择 **输出状态** 参数时，模块会配置一个输出端口 **Status**。该端口输出 UART/USART 消息的状态。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

从通用异步收发器 (UART/USART) 端口写入串行数据

从通用异步接收器/发送器 (UART/USART) 端口写入串行数据。

UART/USART Write 模块要求写入的数据为 [Nx1] 或 [1xN] 数组。选择 **指定要写入的数据长度** 以指定要写入 UART/USART 端口的输入数据长度。
