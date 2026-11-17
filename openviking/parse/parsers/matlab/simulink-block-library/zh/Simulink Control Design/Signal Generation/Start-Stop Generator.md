---
type: simulink-block
title: 'Start-Stop Generator'
family: 'signal-generation'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Signal Generation'
documentation_page: 'startstopgenerator'
documentation_source_path: 'ug/startstopgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Start-Stop Generator

## 端口

### 输入

### **enable** — 启用和禁用启动-停止信号生成 标量

指定一个信号以启用 (`1`) 或禁用 (`0`) 模块动作。

**数据类型：** `single` | `double`

### **start times** — 起始时间 标量 | 向量

将信号的起始时间指定为标量或向量。

该模块生成一个信号，该信号在指定的起始时间从 0 变为 1，持续时间为使用 **持续时间 (sec)** 参数指定的持续时间。持续时间过后，信号从 1 变为 0。

**数据类型：** `single` | `double`

### **y** — 稳态值 标量 | 向量

将被控对象输出连接到此端口。该模块确定系统的当前工作状态，并使用此信号生成启动-停止信号。

**数据类型：** `single` | `double`
### 输出

### **start/stop** — 启动-停止信号 标量

启动-停止信号。信号的值变化如下：

- 在使用 **start times** 指定的值处，或在使用 **稳态设置** 确定的稳态时间处，从负值或零变为正值。
- 在 **持续时间 (sec)** 中指定的持续时间过后，从正值变为负值或零。

通常，您使用此信号来启动和停止频率响应估计、信号生成或自动整定过程。当 **enable** 端口设置为 0 时，该模块不生成启动-停止信号。

**数据类型：** `single` | `double`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，从 **仿真** 选项卡的 **准备** 库中选择 **属性检查器**。

### **采样时间 (Ts)** — 采样时间 `0.1` (默认) | 正标量

指定所生成启动-停止信号的采样时间。

### **数据类型** — 浮点精度 `double` (默认) | `single`

根据仿真环境或硬件要求指定浮点精度。

### **起始时间点来源** — 起始时间点来源 `External time vector` (默认) | `Time after reaching steady-state`

将起始时间点来源指定为以下之一：

- `External time vector` — 使用 **start times** 输出端口指定起始时间的显式值。
- `Time after reaching steady-state` — 使用被控对象输出信号 **y** 和 **稳态设置** 确定开始生成启动-停止信号的时间。

### **持续时间 (sec)** — 启动-停止信号持续时间 `10` (默认) | 标量

指定启动-停止信号的持续时间。

### **达到稳态后生成启动-停止信号的样本数** — 开始信号生成的延迟 `2` (默认) | 非负整数

指定达到稳态后，模块延迟生成启动-停止信号的样本数。

### **调节时间上界** — 调节时间上界 `[1.1 2.1 3.1]` (默认) | 向量

指定用于确定工作点调节时间和稳态的工作值上界。

此向量的每个值对应于该索引处工作点值的上界。

### **调节时间下界** — 调节时间下界 `[0.9 1.9 2.9]` (默认) | 向量

指定用于确定工作点调节时间和稳态的工作值下界。

此向量的每个值对应于该索引处工作点值的下界。

### **调节时间区间** — 调节时间区间 `5` (默认) | 标量 | 向量

指定工作条件保持稳态的时间区间。

使用向量为不同工作点指定不同的时间区间。

## 所属库

Simulink Control Design / Signal Generation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

生成供信号生成、估计和自动整定模块使用的启动-停止信号

使用此模块为 Simulink® Control Design™ 库中的信号生成、频率响应估计和 PID 自动整定模块的 **start/stop** 输入端口生成信号。此端口确定何时开始和停止生成这些模块中的扰动信号。Start-Stop Generator 模块生成一个信号，该信号在指定时间值处从 0 变为 1 以启用这些模块，并在指定持续时间过后从 1 变为 0 以禁用。

当您在不同工作条件下生成启动-停止信号以启用估计或自动整定过程时，此模块很有用。
