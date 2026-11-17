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

### **data** — 事件触发信号 标量

指定一个事件信号以在 CPU 或 CLA 中启动软件中断。

**数据类型：** `Boolean`
### 输出

### **event** — 任务事件信号 标量

当触发条件发生时，此端口发送消息。在 **Trigger condition** 参数中指定触发条件。此输出连接到 Task Manager (SoC Blockset) 模块的输入，以执行关联的事件驱动任务。

**注意**

在包含 Software Trigger CPU<->CLA 模块的参考模型的顶层，连接到该 **event** 端口的 Outport 模块必须配置为非虚拟总线。

**数据类型：** `rteEvent`

## 参数

### **Task number** — 任务标识号 `1`（默认）| 从 `1` 到 `8` 的整数

指定要触发的 CLA 任务编号。

### **Trigger condition** — 触发事件的条件 `Rising edge`（默认）| `Input high`

在 **data** 端口的上升沿或输入为高电平时，在 **event** 端口上生成事件。要在输入信号从零变为一时生成事件，请将此参数设置为 `Rising edge`。要在任务每次执行时生成一次事件，请将此参数设置为 `Input high`。

### **Trigger type** — 触发类型 `Trig`（默认）| `TrigAndWait(codegen)`

指定 CPU 上的触发类型。要生成事件并继续运行 CPU，请将此参数设置为 `Trig`。要生成事件并指示 CPU 等待中断完成，请将此参数设置为 `TrigAndWait(codegen)`。`TrigAndWait(codegen)` 选项在仿真中不运行。

#### 依赖关系

要启用此参数，模块必须位于 **Processing Unit** 设置为某个 CPU 的参考模型内。

## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

在处理器 (CPU) 与控制律加速器 (CLA) 之间触发软件事件

Software Trigger CPU<->CLA 模块模拟在支持的 Texas Instruments® 硬件板中处理器 (CPU) 与 CLA 之间软件事件的触发。当您将此模块用作 CPU 上的任务时，该模块生成一个事件以在连接的 CLA 单元上执行任务。当您将此模块用作 CLA 上的任务时，该模块生成一个事件以在连接的 CPU 上执行任务。使用此模块管理 CPU 与 CLA 之间的通信和同步。
