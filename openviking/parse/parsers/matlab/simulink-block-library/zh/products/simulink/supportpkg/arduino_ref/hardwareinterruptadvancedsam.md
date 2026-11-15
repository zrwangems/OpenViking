---
type: simulink-block
title: 'Hardware Interrupt SAM'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'hardwareinterruptadvancedsam'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedsam.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt SAM

## 端口

### 输出

### **Event name** — 生成中断请求标量

该模块输出一个函数调用。函数调用输出的数量取决于您选择在 ISR 中服务的事件数量。例如，如果您在 **要服务的事件** 部分选择 **CAN rx** 和 **Custom event**，则该模块会启用 **CAN rx** 和 **Custom event** 输出端口。

## 参数

### **中断组** — 选择外设 ISR `Controller area network (CAN1)`（默认）| `Controller area network (CAN0)`

此参数列出 Arduino 开发板中特定类型外设的所有可用 ISR。**中断名称** 参数中可用的值取决于您在此参数中选择的中断组。

### **中断名称** — 选择 ISR `CAN1_Handler`（默认）| `CAN0_Handler`

中断名称指定 Hardware Interrupt 模块的 ISR。此参数对应于 Arduino 开发板中断向量表中的特定条目。可用的 ISR 取决于 **中断组**。

#### 依赖关系

- 要启用 `CAN1_Handler`，请将 **中断组** 设置为 `Controller area network (CAN1)`。
- 要启用 `CAN0_Handler`，请将 **中断组** 设置为 `Controller area network (CAN0)`。

### **中断编号** — ISR 在中断向量表中的位置 `15`（默认）

此只读参数指示 ISR 在 Arduino 开发板中断向量表中的位置。

### **事件名称** — 选择事件及其执行顺序 `CAN rx`（默认）| `Custom event`

从 **要服务的事件** 组中选择事件或自定义事件及其各自的执行顺序，以便为您选择的 **中断名称** 服务事件。您可以选择自定义事件与其他事件一起执行。您还可以更改事件的执行顺序。

### **Simulink 任务优先级** — 设置 ISR 的优先级 `30`（默认）| 正整数或非负整数

您在此参数中指定的值将设置下游函数调用子系统的优先级。ISR 在 Simulink 中的任务优先级相对于您在 Simulink 模型中设置的基础速率的优先级。

**注意**

Simulink 模型中基础速率的默认优先级为 `40`，较低的优先级值表示较高的优先级。为此，在“配置参数”对话框中，在 **求解器** 窗格中选择 **较高的优先级值表示较高的任务优先级**。

### **将中断服务例程作为原子单元运行** — 选择以禁用中断抢占 `off`（默认）| `on`

选择此参数可在执行当前 ISR(s) 时屏蔽所有其他中断。

### **服务每个事件后清除状态** — 选择以清除中断状态标志 `off`（默认）| `on`

选择此选项可在服务每个事件后清除所有中断状态标志。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / SAM

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

从 Arduino SAM 内核的中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块可针对所选中断，在 Simulink® 模型的生成代码中自动创建中断服务例程 (ISR)。ISR 执行与该模块的事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 相同的优先级运行。

使用此模块，您可以：

- 在 Arduino® 开发板上创建 ISR。
- 设置 ISR 的优先级。
- 启用或禁用中断抢占。

此模块仅为 ISR 以及您选择或指定的事件生成代码。要更改配置、启用中断以及指定触发选项，请使用所选外设的设置。例如，要在 Hardware Interrupt 模块上为 CAN 通信外设创建 ISR，您的 Simulink 模型必须具有 On-board CAN Receive 或 On-board CAN Transmit 模块。

**注意**

Hardware Interrupt 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 开发板

Arduino Due
