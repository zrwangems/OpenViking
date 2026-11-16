---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'hardwareinterruptblock'
documentation_source_path: 'ref/hardwareinterruptblock.html'
language: zh-CN
chinese_source: official
---

# Hardware Interrupt

## 端口

### 输入

### ***`name`* Event Task** — 函数调用事件输入仿真 标量

当连接到 Function-Call Generator 模块时，仅用于仿真的消息输入端口会作为直通模块，其输出会在仿真中通过 ***`name`* Event** 端口发出。

#### 依赖关系

要启用此端口，请选择**启用仿真端口**参数。
### 输出

### ***`name`* Event** — 生成中断请求 `Scalar`

该模块的输出是一个函数调用。函数调用输出的数量将与 ISR 中选择处理的事件数量相同。

## 参数

### **要服务的事件数量** — 指定要服务的事件数量 `1` (默认) | `2` | `3` | `<32`

指定要为 Hardware Interrupt 模块服务的事件数量。此参数启用指定数量的事件作为输出端口 `event#`

### **Simulink 任务优先级** — 设置所选 ISR 的优先级 `50` (默认) | `positive integer or nonnegative integer`

此参数中指定的值设置下游函数调用子系统的优先级。所选 (ISR) 的 Simulink 任务优先级是相对于模型基本速率优先级而言的。

**注意**

默认模型基本采样率优先级设置为 40，优先级值越低表示任务优先级越高。要实现这一点，必须在**配置参数** > **求解器**窗格中启用**优先级值越高，任务优先级越高**选项。

### **禁用中断抢占** — 选择此项可禁用中断抢占。 `off` (默认) | `on`

默认情况下，优先级更高的中断可以抢占优先级较低的中断。选择此选项可使低优先级中断完成执行，而不会被其他中断抢占。

### **启用仿真端口** — 启用仿真端口以阻止 `off` (默认) | `on`

选择此参数可添加兼容的仿真输入端口。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2023a 中推出**

## 描述

从中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块在模型生成的代码中自动创建中断服务例程 (ISR)。ISR 执行与该模块的事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 优先级相同的优先级运行。

使用此模块，您可以：

- 创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。
- 使用 Hardware Mapping 工具配置所需的事件或中断。

**硬件映射**工具允许您为选定的硬件板配置硬件中断任务。借助此工具，您可以将软件模型中的任务映射到可用的事件源和中断：

- 在**映射浏览器** > **任务** > **`CPU name`** 中手动选择任务。选择所需的事件或中断源。有关更多信息，请参阅使用硬件映射配置中断和事件
