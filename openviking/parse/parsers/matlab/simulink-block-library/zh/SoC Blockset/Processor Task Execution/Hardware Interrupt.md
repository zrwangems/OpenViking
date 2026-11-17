---
type: simulink-block
title: 'Hardware Interrupt'
family: 'processor-task-execution'
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

### **event1 Task** — 模拟中断触发 `scalar`

仅用于仿真的消息输入用作直通，并在输出端反映。该端口从函数调用接收输入。

#### 依赖关系

要启用此端口，请选择 **启用仿真端口** 参数。

### 输出

### **event1** — 中断请求 `scalar`

该端口将中断触发连接到软件任务。输出为函数调用。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **任务优先级** — 所选中断的优先级 `50` (默认) | 正整数

指定事件驱动任务的调度优先级，范围在 `1` 到 `99` 之间。较高优先级任务会抢占较低优先级任务。任务优先级范围受硬件属性限制。有关任务优先级的详细信息，请参阅任务优先级和抢占。

### **处理器核** — 核编号 `0` (默认) | 整数 | `-1`

指定任务执行的处理器核编号。有关选择核和核执行可视化的详细信息，请参阅多核执行和核可视化。

要让操作系统动态为任务分配核，请将此值设置为 `-1`。

### **启用仿真端口** — 启用模块中的仿真端口 `off` (默认) | `on`

选择此参数以启用外设仿真。选中后，模块会添加一个用于仿真的输入端口。

### **硬件映射** — 打开硬件映射工具按钮

点击此参数以打开硬件映射工具。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

Hardware Interrupt 模块在事件发生时触发任务。该任务必须与事件中断服务例程关联。一旦触发，任务将执行下游子系统。使用 IP 核生成工作流时，此模块会被配置并放置在生成的软件模型中。

**提示**

要生成软件模型，请使用 IP 核生成工作流，而不是手动创建模型并配置 Hardware Interrupt 参数。该工作流会配置 Hardware Interrupt 模块并将其放置在生成的模型中。

要将任务与中断事件关联，请使用硬件映射应用。要启动该应用，请在模块封装上点击 **硬件映射**。
