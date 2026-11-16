---
type: simulink-block
title: 'C29x Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Scheduling'
documentation_page: 'c29xhardwareinterruptblock'
documentation_source_path: 'ref/c29xhardwareinterruptblock.html'
language: zh-CN
chinese_source: worker-translation
---

# C29x Hardware Interrupt

## 端口

### 输出

### ***`name`* 事件** — 生成中断请求 `Scalar`

此模块的输出是函数调用。函数调用输出的数量将与在 ISR 中选择要服务的事件数量相同。

## 参数

### **中断组** — 选择外设 ISR `External interrupts (EXTI)`（默认） | `Analog to digital converter (ADC)` | `Pulse width modulation (PWM)` | `Direct memory access (DMA)`

中断组列出同一类型外设的所有 ISR。选择中断组会更改 **中断名称** 参数中的值列表。

### **中断名称** — 选择 ISR `EXTI0_IRQHandler`（默认） | `ADC_IRQHandler` | `TIM1_BRK_TIM9_IRQHandler` | `DMA0_Stream0_IRQHandler`

中断名称指定要为硬件中断模块生成的 ISR。**中断** 名称对应于处理器中断向量表中的特定条目。可用的 ISR 取决于中断组。

### **中断编号** — ISR 在中断表中的位置 `21`（默认） | `33` | `71` | `…`

此只读参数指示所选 ISR 在目标硬件中断向量表中的位置。

### **要服务的事件** — 选择事件 `EXTI0 Event`（默认） | `ADC1 OVR` | `Stream0 TC` | `…`

从 **要服务的事件** 组中选择事件或自定义事件及其各自的事件执行顺序，以便为所选的 **中断名称** 服务事件。您可以选择自定义事件与其他所选事件一起执行。有关更多信息，请参阅 Limitations (Embedded Coder)。

要服务的事件

### **Simulink 任务优先级** — 设置所选 ISR 的优先级 `30`（默认） | `positive integer or nonnegative integer`

您在此参数中指定的值设置下游函数调用子系统的优先级。所选 (ISR) 的 Simulink® 任务优先级相对于模型基本速率优先级。

**注意**

默认模型基本采样率优先级设置为 40，较低的优先级值表示较高的优先级任务。要实现此目的，必须在 **Configuration Parameters** > **Solver** 窗格中启用 **Higher priority value indicates higher task priority** 选项。

### **Run interrupt service routine as atomic unit** — 选择以禁用中断抢占 `off`（默认） | `on`

启用“将中断服务例程作为原子单元运行”以在执行所选中断服务例程时阻止所有其他中断。

### **在服务每个事件后清除状态** — 选择以清除中断状态标志 `off`（默认） | `on`

选择此参数以在执行每个事件后清除中断服务例程中的事件状态。

## 所属库

C2000 Microcontroller Blockset / F29H85x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块在模型的生成代码中自动创建中断服务例程 (ISR)，以响应所选事件。ISR 执行与模块事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 优先级相同的优先级运行。

使用此模块，您可以：

- 创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。

此模块仅为指定的 ISR 和所选事件生成代码。要更改配置、启用中断和特定触发选项，请使用所选外设的设置。

例如，要在 Hardware Interrupt 模块上为 ADC 外设创建 ISR：

- 模型必须具有 **Analog to digital Converter** (ADC) 模块。
- 从硬件中断模块中，在 **中断组** 参数中选择 `Analog to digital converter (ADC)`，并在 **中断名称** 参数中选择 `ADCA#_INT`。
- 在 **要服务的事件** 参数中选择 `EOC event` 或 `Overflow event` 事件名称。

要了解有关何时不使用自定义事件的更多信息，请参阅 Limitations (Embedded Coder)。
