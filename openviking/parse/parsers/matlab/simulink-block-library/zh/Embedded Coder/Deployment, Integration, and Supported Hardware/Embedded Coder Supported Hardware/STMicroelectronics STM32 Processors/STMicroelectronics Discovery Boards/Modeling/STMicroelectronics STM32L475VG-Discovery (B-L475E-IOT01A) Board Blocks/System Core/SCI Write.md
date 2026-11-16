---
type: simulink-block
title: 'SCI Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'sciwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/sciwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# SCI Write

## 端口

### 输入

### **Tx** — 发送到 UART 的数据向量

来自模型的发送到 UART 端口的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写操作的状态标量

当接收的数据长度大于或等于 **Data length (N)** 参数中指定的长度时，输出为 `0`。否则，输出为非零值，表示可用数据的长度小于 **Data length (N)** 参数中指定的长度。

`0` 表示写操作成功。

例如，当接收的数据长度为 9 且 *N* = 8 时，**Status** 端口输出 `0`，表示写操作成功。当接收的数据长度为 9 且 *N* = 10 时，**Status** 端口输出 `32`，表示数据不可用。

| 接收的数据长度 = 9 | | | | |
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

对应于与 SCI 设备通信的 SCI 引脚组的 SCI 模块。

**注意**

在外部模式下，SCI0 模块保留用于外部模式通信，不能由 SCI Write 模块使用。

### **Output status** — 显示写操作状态的选项 off（默认） | on

选择此参数以启用 **Status** 端口。

对于成功的写操作，该端口输出 `0`。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

向 UART 发送 N×1 数据数组

SCI Write 模块将 *N*×*1* 数据数组发送到所选的通用异步收发器 (UART)，其中 *N* 是要读取的数据长度。该模块从输入端口处的信号继承数据类型。您可以从 **Configuration Parameters**  > **Hardware Implementation pane** > **SCI** 更改 **Baudrate**，并选择 UART 串行通信接口 (SCI) 的 **Transmit pin**。

在外部模式仿真期间，该模块输出目标硬件上运行的可执行文件返回的仿真结果。在所有其他模式的仿真期间，该模块输出零。
