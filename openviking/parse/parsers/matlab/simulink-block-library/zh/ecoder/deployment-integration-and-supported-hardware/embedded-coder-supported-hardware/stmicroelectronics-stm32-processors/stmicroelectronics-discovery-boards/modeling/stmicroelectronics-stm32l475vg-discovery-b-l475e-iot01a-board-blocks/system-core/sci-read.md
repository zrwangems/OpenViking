---
type: simulink-block
title: 'SCI Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'sciread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/sciread.html'
language: zh-CN
chinese_source: worker-translation
---

# SCI Read

## 端口

### 输出

### **Rx** — 从 UART 读取的数据向量

该端口输出从所选 UART 读取的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态标量

当你选择 **Output error status** 参数时，将提供一个标记为 `Status` 的输出端口。

该端口按下表所述输出每个读取请求的状态：

**返回状态代码**

| **Status** | 描述 |
| --- | --- |
| `0` | SUCCESS |
| `1` | RX\_BUSY |
| `2` | TX\_BUSY |
| `4` | PARITY\_ERROR |
| `8` | FRAME\_ERROR |
| `16` | BUS\_ERROR |
| `32` | DATA\_NOT\_AVAILABLE |

当接收到的数据长度大于或等于 **Data length (N)** 参数中指定的长度时，输出为 `0`。否则，输出为非零值，表示可用数据的长度小于 **Data length (N)** 参数中指定的长度。

`0` 表示读取操作成功。

例如，当接收到的数据长度为 9 且 *N* = 8 时，**Status** 端口输出 `0`，表示读取操作成功。当接收到的数据长度为 9 且 *N* = 10 时，**Status** 端口输出 `32`，表示数据不可用。

| 接收到的数据长度 = 9 | | | | |
| --- | --- | --- | --- | --- |
| **端口** | **数据类型** | **数据长度** | | |
| *N* = 8 | *N* = 9 | *N* = 10 |
| **Rx** | `uint8` | `8` | `9` | `9` |
| **Status** | `uint8` | `0` | `0` | `32` |

#### 依赖关系

要启用该端口，请选择 **Output status** 参数。

**数据类型：** `uint8`

## 参数

### **SCI module** — 用于通信的 SCI 模块 `0`（默认） | 任意整数值

SCI 设备连接到的 SCI 模块。

**注意**

在外部模式中，SCI0 模块保留用于外部模式通信，不能由 SCI Read 模块使用。

### **Data type** — 来自 UART 端口的数据的数据类型 `uint8`（默认） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

要从 UART 端口读取的数据的数据类型。

### **Data length (N)** — 要从 UART 端口读取的数据点数量 `1`（默认） | 大于或等于 0 的任意整数

针对所选数据类型，要从 UART 端口读取的数据点数量。

### **Output status** — 读取操作的状态 off（默认） | on

选择此参数以启用 **Status** 端口。

### **Sample time** — 从 UART 端口读取数据的频率 `0.1`（默认）

从 UART 端口读取数据的频率，以 seconds 为单位指定。当你将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

读取 UART 上的 N-by-1 数据数组

SCI Read 模块从通用异步收发器 (UART) 读取 *N*-by-*1* 数据数组，其中 *N* 是要读取的数据长度。你可以更改 **Baudrate**，并从 **配置参数** > **硬件实现窗格** > **SCI** 为 UART 串行通信接口 (SCI) 选择 **Receive pin**。

在外部模式仿真期间，该模块输出从目标硬件上运行的可执行文件返回的仿真结果。在所有其他模式下进行仿真期间，该模块输出零。

此模块以非阻塞模式运行。
