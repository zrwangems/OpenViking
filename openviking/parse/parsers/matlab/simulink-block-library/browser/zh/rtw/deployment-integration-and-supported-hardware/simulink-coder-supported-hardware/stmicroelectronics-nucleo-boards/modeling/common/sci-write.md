---
type: simulink-block
title: 'SCI Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'sciwrite'
documentation_source_path: 'nucleo/ref/sciwrite.html'
language: zh-CN
chinese_source: official
---

# SCI Write

## 端口

### 输入

### **Tx** — 发送到 UART 的数据 向量

从您的模型发送到 UART 端口的数据。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写入操作的状态 标量

当接收到的数据长度大于或等于在**数据长度(N)** 参数中指定的长度时，输出为 `0`。否则，输出为非零值，表示可用数据的长度小于在**数据长度(N)** 参数中指定的长度。

`0` 表示成功的写入操作。

例如，当接收到的数据长度为 9 且 *N* = 8 时，**状态**端口输出 `0` 表示成功的写入操作。当接收到的数据长度为 9 且 *N* = 10 时，**状态**端口输出 `32` 表示数据不可用。

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

与 SCI 设备通信的 SCI 引脚组对应的 SCI 模块。

**注意**

在外部模式下，SCI0 模块保留用于外部模式通信，无法由 SCI Write 模块使用。

### **输出状态** — 显示写入操作状态的选项 off (默认) | on

选择此参数可启用**状态**端口。

该端口输出 `0` 表示成功的写入操作。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

将 N × 1 数据数组发送到 UART

SCI Write 模块将一个 *N*×*1* 数据数组发送到选定通用异步接收机/发射机 (UART)，其中 *N* 是要读取的数据长度。该模块从输入端口处的信号继承数据类型。您可以从**配置参数** > **硬件实现窗格** > **SCI** 更改**波特率**并选择 UART 串行通信接口 (SCI) 的**传输针**。

在外部模式仿真期间，模块输出从在目标硬件上运行的可执行文件返回的仿真结果。在所有其他模式下的仿真期间，模块输出零。
