---
type: simulink-block
title: 'SCI Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'sciread'
documentation_source_path: 'nucleo/ref/sciread.html'
language: zh-CN
chinese_source: official
---

# SCI Read

## 端口

### 输出

### **Rx** — 从 UART 读取的数据 向量

该端口输出从选定 UART 读取的数据。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态 标量

当您选择**输出错误状态**参数时，标签为 `Status` 的输出端口变为可用。

该端口输出每个读取请求的状态，如下表所示：

**返回状态代码**

| **状态** | 描述 |
| --- | --- |
| `0` | SUCCESS |
| `1` | RX\_BUSY |
| `2` | TX\_BUSY |
| `4` | PARITY\_ERROR |
| `8` | FRAME\_ERROR |
| `16` | BUS\_ERROR |
| `32` | DATA\_NOT\_AVAILABLE |

当接收到的数据长度大于或等于在**数据长度(N)** 参数中指定的长度时，输出为 `0`。否则，输出为非零值，表示可用数据的长度小于在**数据长度(N)** 参数中指定的长度。

`0` 表示成功的读取操作。

例如，当接收到的数据长度为 9 且 *N* = 8 时，**状态**端口输出 `0` 表示成功的读取操作。当接收到的数据长度为 9 且 *N* = 10 时，**状态**端口输出 `32` 表示数据不可用。

| 接收到的数据长度 = 9 | | | | |
| --- | --- | --- | --- | --- |
| **端口** | **数据类型** | **数据长度** | | |
| *N* = 8 | *N* = 9 | *N* = 10 |
| **Rx** | `uint8` | `8` | `9` | `9` |
| **状态** | `uint8` | `0` | `0` | `32` |

#### 依赖关系

要启用该端口，请选择**输出状态**参数。

**数据类型:** `uint8`

## 参数

### **SCI 模块** — 用于通信的 SCI 模块 `0` (默认) | 任何整数值

SCI 设备连接到的 SCI 模块。

**注意**

在外部模式下，SCI0 模块保留用于外部模式通信，无法由 SCI Read 模块使用。

### **数据类型** — 来自 UART 端口的数据的数据类型 `uint8` (默认) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

要从 UART 端口读取的数据的数据类型。

### **数据长度(N)** — 要从 UART 端口读取的数据点数 `1` (默认) | 任何大于或等于 0 的整数

为选定数据类型要从 UART 端口读取的数据点数。

### **输出状态** — 读取操作的状态 off (默认) | on

选择此参数可启用**状态**端口。

### **采样时间** — 从 UART 端口读取数据的频率 `0.1` (默认)

从 UART 端口读取数据的频率，以秒为单位指定。当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

在 UART 上读取 N × 1 数据数组

SCI Read 模块从通用异步接收机/发射机 (UART) 读取一个 *N*×*1* 数据数组，其中 *N* 是要读取的数据的长度。您可以从**配置参数** > **硬件实现窗格** > **SCI** 更改**波特率**并选择 UART 串行通信接口 (SCI) 的**接收针**。

在外部模式仿真期间，模块输出从在目标硬件上运行的可执行文件返回的仿真结果。在所有其他模式下的仿真期间，模块输出零。

此模块在非阻塞模式下运行。
