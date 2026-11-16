---
type: simulink-block
title: 'Software Trigger CPU<->CLA'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'softwaretriggercpucla'
documentation_source_path: 'ref/softwaretriggercpucla.html'
language: zh-CN
chinese_source: worker-translation
---

# Software Trigger CPU<->CLA

## 端口

### 输入

### **data** — 事件触发信号标量

指定一个事件信号，以在 CPU 或 CLA 中启动软件中断。

**数据类型：** `Boolean`
### 输出

### **event** — 任务事件信号标量

每当触发条件发生时，此端口发送一条消息。在 **触发条件** 参数中指定触发条件。此输出连接到 Task Manager (SoC Blockset) 模块的输入，以执行关联的事件驱动任务。

**注意**

在包含 Software Trigger CPU<->CLA 模块的引用模型顶层中，连接到该 **event** 端口的 Outport 模块必须配置为非虚拟总线。

**数据类型：** `rteEvent`

## 参数

### **任务编号** — 任务标识编号 `1`（默认）| 从 `1` 到 `8` 的整数

指定要触发的 CLA 任务编号。

### **触发条件** — 触发事件的条件 `Rising edge`（默认）| `Input high`

在 **event** 端口上生成事件，条件为 **data** 端口出现上升沿或每当输入为高电平。若要在输入信号从零变为一时生成事件，请将此参数设置为 `Rising edge`。若要在任务每次执行时生成一次事件，请将此参数设置为 `Input high`。

### **触发类型** — 触发类型 `Trig`（默认）| `TrigAndWait(codegen)`

指定 CPU 上的触发类型。若要生成事件并继续运行 CPU，请将此参数设置为 `Trig`。若要生成事件并指示 CPU 等待中断完成，请将此参数设置为 `TrigAndWait(codegen)`。`TrigAndWait(codegen)` 选项不在仿真中运行。

#### 依赖关系

要启用此参数，该模块必须位于一个引用模型内，且其 **处理单元** 设置为其中一个 CPU。

## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

在处理器 (CPU) 和控制律加速器 (CLA) 之间触发软件事件

Software Trigger CPU<->CLA 模块在支持的 Texas Instruments® 硬件板上模拟处理器 (CPU) 和 CLA 之间的软件事件触发。当您将此模块用作 CPU 上的任务时，该模块会生成一个事件，以在连接的 CLA 单元上执行任务。当您将此模块用作 CLA 上的任务时，该模块会生成一个事件，以在连接的 CPU 上执行任务。使用此模块可管理 CPU 和 CLA 之间的通信与同步。
