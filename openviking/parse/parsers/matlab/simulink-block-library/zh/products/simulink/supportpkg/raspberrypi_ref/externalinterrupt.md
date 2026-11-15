---
type: simulink-block
title: 'External Interrupt'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'externalinterrupt'
documentation_source_path: 'supportpkg/raspberrypi_ref/externalinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# External Interrupt

## 端口

### 输入

### **SimIRQ** — 用于为仿真提供输入的端口 `0` | `1`

在仿真期间，您可以通过将 Simulink 库中的源模块连接到 **SimIRQ** 端口来为 External Interrupt 模块模拟输入。如果提供给模块的输入为 boolean true，则模块会触发下游函数调用子系统。External Interrupt 模块在每个时间步接收 `0` 或 `1` 的输入值。当模块端口处的输入为 `1` 时，模块执行 Function-Call Subsystem。如果您不提供输入，则模块会触发下游函数调用子系统，直到仿真继续运行。在代码生成期间，连接到 External Interrupt 模块输入端口的所有 Simulink 模块都会被忽略，并且不会对生成的代码产生影响。

#### 依赖关系

要启用此端口，请选择 **Add simulation input port** 参数。

**数据类型：** `Boolean`
### 输出

### **IRQ** — 函数调用事件输出 标量 | 向量

将函数调用事件发送到函数调用子系统或模型的函数调用输入端口。

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择 Raspberry Pi 硬件板。

### **View pin map** — 打开引脚映射按钮

点击 **View pin map** 查看与所选 Raspberry Pi 硬件板关联的引脚映射图。

### **Pin** — 用于生成外部中断的 Raspberry Pi 硬件板引脚 `9`（默认） | `4` | `17` | `27` | `27` | `22` | `10` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

选择 Raspberry Pi 硬件上的数字输入引脚以生成外部中断。使用多个 Raspberry Pi 板时，可以为每个板选择不同的引脚。

### **Pull mode** — 将 Raspberry Pi 硬件引脚设置为逻辑高电平或低电平 `Pull-up`（默认） | `Pull-down`

选择以下模式之一。

- `Pull-up`：选择此模式时，当没有输入连接到引脚时，您在 Pin 参数中设置的引脚被上拉为逻辑高电平。
- `Pull-down`：选择此模式时，当没有输入连接到引脚时，您在 Pin 参数中设置的引脚被下拉为逻辑低电平。

### **Edge selection** — 数字引脚上触发函数调用的跳变 `Rising`（默认） | `Falling` | `Either`

选择边沿选择模式，以指定所选 Raspberry Pi 硬件引脚上的哪些信号跳变会触发下游函数调用。

- `Rising`：当数字引脚值从低变为高时
- `Falling`：当数字引脚值从高变为低时
- `Either`：当数字引脚值从低变为高或从高变为低时

此图展示了在不同中断模式下，当硬件引脚值变化时，模块如何执行下游函数调用。ISR 在不同中断模式下触发。

**注意**

对于您选择的任何 **Edge selection** 模式，下游函数调用都会出现延迟，该延迟接近 Simulink 模型的基础速率。

### **Add simulation input port** — 用于为仿真提供输入的选项 `off`（默认） | `on`

此参数启用 **SimIRQ** 输入端口。要在仿真期间为模块提供输入，请将源模块连接到 **SimIRQ** 输入端口。在代码生成期间，连接到该端口的任何模块都会被忽略，并且不会对生成的代码产生影响。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

External Interrupt 模块从中断服务例程 (ISR) 触发下游 Function-Call Subsystem。Function-Call Subsystem 应连接到 External Interrupt 模块的输出端口。ISR 是当在您指定的硬件引脚上发生中断时，由 Raspberry Pi® 内核触发的一段代码。

在仿真期间，您可以通过将 Simulink® 库中的源模块连接到 External Interrupt 模块的输入端口，为 External Interrupt 模块提供输入。External Interrupt 模块在每个时间步接收 `0` 或 `1` 的输入值。当模块端口处的输入为 `1` 时，模块触发下游函数调用子系统。当模块端口处的输入为 `0`，或者没有输入源连接到模块的输入端口时，模块不会触发下游函数调用子系统。在代码生成期间，连接到 External Interrupt 模块输入端口的所有 Simulink 模块都会被忽略，并且不会对生成的代码产生影响。

**注意**

我们建议您仅在模型层次结构中的父模型中使用 External Interrupt 模块。有关详细信息，请参阅模型引用。
