---
type: simulink-block
title: 'Byte Reversal'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Utilities'
documentation_page: 'bytereversal'
documentation_source_path: 'nucleo/ref/bytereversal.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Reversal

## 端口

### 输入

### **Port\_1** — *N* 个输入端口中的第一个 标量 | 向量 | 矩阵

输入端口数量在 **Number of inputs** 参数中指定。
该模块可以有 `1` 到 *N* 个输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 包含反转数据的输出端口 标量 | 向量

输出端口从 `1` 到 *N*，如 **Number of inputs** 参数所指定。
输出端口数量会调整以匹配输入端口数量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Number of inputs** — 模块输入的数量 `1`（默认）

输入端口和输出端口的数量会调整以匹配此参数中指定的值。

当使用多个输入端口时，每个输入端口映射到匹配的输出端口。进入输入端口 1 的数据从输出端口 1 输出，依此类推。反转字节不会更改数据类型。

### 示例

假设您正在发送一个信号。信号具有以下属性：

| 常量值 | 类型 | 字节结构 |
| --- | --- | --- |
| -234 | `int16` | `1111 1111 0001 0110` |
| 234 | `uint16` | `0000 0000 1110 1010` |
| 234 | `uint32` | `0000 0000 0000 0000 0000 0000 1110 1010` |

1. 将输入数量设置为 3。

   该模块创建三个输入端口和三个输出端口。
2. 将信号连接到 Byte Reversal 模块。

以下模型展示了字节反转。在第一个值为 -234 的信号中，低序字节 `0001 0110` 与高序字节 `1111 1111` 交换。因此，信号输出为 `0001 0110 1111 1111`。

## 所属库

Simulink Support Package for Arduino Hardware / Utilities Embedded Coder / Embedded Targets / Host Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Utilities Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities SoC Blockset Support Package for Infineon AURIX Microcontrollers / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

为大端处理器反转小端数据

Byte Reversal 模块更改输入数据中字节的顺序。当您的进程在使用不同字节序的处理器之间通信时，请使用此模块。例如，将此模块用于在采用小端的 Intel® 处理器与采用大端的其他处理器之间进行通信。与 Intel 80x86 处理器和 Texas Instruments® 处理器兼容的处理器是小端。在这种情况下，请在 Byte Pack 模块之前插入一个 Byte Reversal 模块，并在 Byte Unpack 模块之后紧接着插入另一个 Byte Reversal 模块。

使用此模块的参数，指定模块输入的数量。
