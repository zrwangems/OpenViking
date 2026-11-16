---
type: simulink-block
title: 'ADC Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Other'
documentation_page: 'adcread'
documentation_source_path: 'ref/adcread.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Read

## 端口

### 输入

### **msg** — 来自寄存器标量的数据消息

此消息端口接收来自所连接的 ADC Interface 模块的 ADC 值消息。当 Task Manager 模块触发包含 ADC Read 模块的任务时，这些消息会进行处理。有关消息的详细信息，请参阅消息。

**数据类型：** `SoCData`

### 输出

### **data** — 标量输出信号

此端口输出来自 ADC Interface 模块的测量值。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **数据类型** — 接收到的 ADC 测量值的数据类型 `double`（默认） | `single` | `uint8` | `int8` | `int16` | `int32` | `uint16` | `uint32`

选择输入数据的数据类型。将此数据类型与 ADC 硬件的数据类型匹配。

### **采样时间** — 采样时间 `-1`（默认） | 非负标量

指定调度器运行此模块的频率。如果此值为 `-1`（默认），则调度器会为该模块分配采样时间。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当部署到受支持的硬件板时，此模块生成的代码会读取指定 ADC 模块的 MCU 中的 ADC 寄存器。有关配置寄存器设置的详细信息，请参阅硬件映射。

## 版本历史

**在 R2020b 中引入**

## 描述

从 ADC Interface 模块读取 ADC 数据值

ADC Read 模块将接收自 ADC Interface 模块的消息转换为可供算法使用的信号。输出信号的数据类型与所包含数据消息中的数据类型相同。
