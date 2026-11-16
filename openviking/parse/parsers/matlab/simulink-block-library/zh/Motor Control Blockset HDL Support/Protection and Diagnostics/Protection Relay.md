---
type: simulink-block
title: 'Protection Relay'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'protectionrelay'
documentation_source_path: '../mcb/ref/protectionrelay.html'
language: zh-CN
chinese_source: official
---

# Protection Relay

## 端口

### 输入

### **Imax** — 电流上限 标量

反馈环中的电流上限（以安培为单位），用于提供过流保护。当反馈环中的电流 (`Ifb`) 超出此值时，模块会生成锁存故障信号。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**过电流**。

**数据类型:** `single` | `double` | `fixed point`

### **Ifb** — 反馈环中的实际电流 标量

在给定时间的反馈环中的实际电流（以安培为单位）。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**过电流**。

**数据类型:** `single` | `double` | `fixed point`

### **⍵m max** — 超速保护的转子转速限值 标量

转子的转速限值（以 RPM 为单位）。当转子转速 (`⍵m fb`) 超出此值时，模块生成一个锁定故障信号。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**超速**。

**数据类型:** `single` | `double` | `fixed point`

### **⍵m fb** — 实际转子转速 标量

给定时间的实际转子转速 (RPM)。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**超速**。

**数据类型:** `single` | `double` | `fixed point`

### **Vmax** — 过压保护的电压上限 标量

反馈环上的电压上限（以伏特为单位）。当反馈环上的电压 (`Vfb`) 超出此值时，此模块会生成一个锁存故障信号。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**过压**。

**数据类型:** `single` | `double` | `fixed point`

### **Vmin** — 欠压保护的电压下限 标量

反馈环上的电压下限（以伏特为单位）。当反馈环两端的电压 (`Vfb`) 小于此值时，模块生成一个锁存故障信号。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**欠压**。

**数据类型:** `single` | `double` | `fixed point`

### **Vfb** — 反馈环上的实际电压 标量

在给定时间的反馈环上的实际电压（以伏特为单位）。

#### 依赖关系

要启用此端口，请将**选择保护类型**设置为**过压**或**欠压**。

**数据类型:** `single` | `double` | `fixed point`

### **Reset** — 外部重置脉冲 标量

用于重置故障锁存的外部脉冲。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **y** — 锁存的故障信号 标量

在过电流、超速、过压和欠压条件下，模块生成的锁存故障信号，用于保护硬件和电机。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **选择保护类型** — 保护中继的类型 **过电流** (默认) | **超速** | **过压** | **欠压**

可用于配置过电流、超速、过压和欠压条件下的模块行为的保护类型。

### **最大计数输入类型** — 最大计数的输入方法 **通过对话框指定** (默认) | **输入端口**

使用以下方法之一指定计数器限值：

- **通过对话框指定** - 使用**最大计数**参数指定计数器限值。
- **输入端口** - 使用输入端口 **Cntmax** 指定计数器限值。

### **最大计数** — 计数器限值 `100` (默认) | 标量

计数器支持的最大计数，模块使用该计数来计算反馈信号是否出现阈值违规。

### **去抖滤波器采样数** — 去抖采样数 `3` (默认) | 标量

去抖算法用于检验每个阈值违规停止的模块采样数。此值确定去抖周期。

## 所属库

Motor Control Blockset HDL Support / Protection and Diagnostics Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

实现具有确定最短时间 (DMT) 跳闸特性的保护中继设备

Protection Relay 模块使用参考限值、反馈和重置输入信号，为硬件和电机实现具有确定最短时间 (DMT) 跳闸特性的保护中继设备。发生故障时，该模块会生成锁存故障信号，您可以用它来保护硬件和电机。您可以使用外部重置信号重置故障锁存。

有关该模块使用的算法的更多详细信息，请参阅算法。
