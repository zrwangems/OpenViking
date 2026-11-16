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
language: zh-CN
chinese_source: official
---

# UART/USART Read

## 端口

### 输出

### **Data** — 输出数据 向量 | 标量

输出从 UART/USART 端口读取的数据。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Length** — UART/USART 报文长度 标量

端口输出接收到的元素数。

#### 依赖关系

要启用此端口，请选择**输出读取长度**参数。

**数据类型:** `uint8`

### **Status** — 读取操作的状态 `0` | `1` | `2` | `3` | `4` | `...`

状态端口输出 `0`（即数据接收无错误或成功），或下表中所示的任一位值。

下表列出了各个位及其相关联的错误。

**状态**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 位 | `15` | `14` | `13` | `12` | `11` | `10` | `9` | `8` | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `0` |
| 错误 | X | X | X | X | X | X | ARBE\_ERROR | RX\_BUSY | TX\_BUSY | TX\_FAILED | RX\_BUFFER\_FULL | NOISE\_ERROR | FRAME\_ERROR | PARITY\_ERROR | OVERRUN ERROR | DATA\_NOT\_AVAILABLE |

端口输出状态 `7(transmit failed)` 和 `8(transmit busy)`，这些状态仅对 UART/USART Write 模块有效。

- 0 - 未接收到请求的数据长度
- 1 - 表示超限错误
- 2 - 表示奇偶校验错误
- 3 - 表示帧错误
- 4 - 表示噪声误差
- 5 - 表示接收缓冲区已满
- 6 - 表示发射失败
- 7 - 表示发射繁忙
- 8 - 表示接收繁忙
- 9 - 表示 ARBE 错误

#### 依赖关系

要启用此端口，请选择**输出状态**参数。

**数据类型:** `uint8`

## 参数

### **UART/USART 模块** — UART/USART 模块 `USART1` (默认) | `USART2` | `USART3` | `UART4` | `UART5` | `USART6` | `UART7` | `UART8`

选择 UART/USART 模块。

### **数据类型** — 要读取的数据的类型 `uint8` (默认) | `double` | `single` | `int8` | `int8` | `int16` | `int32` | `uint32` | `boolean`

选择模块从主机读取的数据的类型。每个元素的大小取决于其数据类型。

### **数据长度** — 要读取的数据的大小 `1` (默认) | `scalar`

指定要接收的数据长度。

指定您要在每个数据长度中接收的元素数。数据长度必须为标量值。

### **启用阻塞模式** — 对数据传输启用阻塞模式 `off` (默认) | on

- `On` - 当选择此参数时，读取操作在**阻塞模式**下运行。读取操作在等待请求的数据可用时被阻止。如果数据可用，则 `Data` 端口输出数据。如果数据不可用，则 `Data` 端口等待数据。
- `Off` - 当清除此参数时，读取操作在**非阻塞模式**下运行。读取数据时，如果数据不可用，则 `Data` 端口包含在前一个时间步中接收到的数据。在此模式下，模块不会等待请求的数据可用。

### **阻塞超时(秒)** — 阻塞模式的时间（以秒为单位） `0.1` (默认) | `non-negative value`

指定阻塞模式的时间（秒）。

#### 依赖关系

要启用此参数，请选择**启用阻塞模式**参数。

### **输出读取长度** — 启用输出读取长度 `off` (默认) | on

模块接收到的元素数。当选择**输出读取长度**参数时，模块会配置输出端口**长度**。

### **输出状态** — 启用输出状态 `off` (默认) | on

当选择**输出状态**参数时，模块会配置输出端口**状态**。端口输出 UART/USART 报文的状态。

### **采样时间** — 模块读取数据的时间间隔 `0.1` (默认) | `-1` | `non-negative real value`

指定模块接收报文的频率（以秒为单位）。当您将此参数指定为 -1 时，Simulink® 根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2022a 中推出**

## 描述

从通用异步接收机/发射机 (UART/USART) 端口读取数据

从通用异步接收机/发射机 (UART/USART) 端口读取串行数据。

UART/USART Read 模块将读取的值以 [N×1] 数组形式输出。您可以使用模块指定数据类型和要读取的数据长度。
