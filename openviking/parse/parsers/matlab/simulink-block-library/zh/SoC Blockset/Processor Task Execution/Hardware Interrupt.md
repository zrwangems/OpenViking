---
type: simulink-block
title: 'Hardware Interrupt'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'ref/hardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口

### 输入

### **event1 Task** — 仿真中断触发 `scalar`

仅用于仿真的消息输入充当直通通道，其内容会反映到输出端。该端口接收来自函数调用的输入。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数。
### 输出

### **event1** — 中断请求 `scalar`

此端口将中断触发与软件任务关联。输出为函数调用。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Task priority** — 所选中断的优先级 `50`（默认值）| 正整数

指定事件驱动任务的调度优先级，取值范围为 `1` 到 `99`。优先级较高的任务会抢占优先级较低的任务。任务优先级范围受硬件属性限制。有关任务优先级的详细信息，请参阅“任务优先级和抢占”。

### **Processor core** — 核心编号 `0`（默认值）| 整数 | `-1`

指定执行任务的处理器核心编号。有关选择核心以及核心执行可视化的详细信息，请参阅“多核执行和核心可视化”。

要让操作系统动态地为任务分配核心，请将此值设置为 `-1`。

### **Enable simulation port** — 在模块中启用仿真端口 `off`（默认值）| `on`

选择此参数可启用外设仿真。选中后，该模块会添加一个用于仿真的输入端口。

### **Hardware Mapping** — 用于打开硬件映射工具的按钮

点击此参数可打开硬件映射工具。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

未在 R2025b 中提供文档。

## 版本历史

**在 R2024b 中推出**

## 描述

从中断服务例程触发下游函数调用子系统

当事件发生时，Hardware Interrupt 模块会触发一个任务。该任务必须与事件中断服务例程相关联。任务一旦被触发，就会执行下游子系统。使用 IP Core Generation Workflow 时，此模块会被配置并放置在生成的软件模型中。

**提示**

要生成软件模型，请使用 IP Core Generation Workflow，而不要手动创建模型并配置 Hardware Interrupt 参数。该工作流会配置 Hardware Interrupt 模块，并将其放置在生成的模型中。

要将任务与中断事件相关联，请使用 Hardware Mapping 应用。要启动该应用，请点击模块封装上的 **Hardware Mapping**。
