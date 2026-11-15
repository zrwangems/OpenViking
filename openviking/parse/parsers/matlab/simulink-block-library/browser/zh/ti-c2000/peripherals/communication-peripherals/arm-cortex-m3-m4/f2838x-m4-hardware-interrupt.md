---
type: simulink-block
title: 'F2838x-M4 Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4hardwareinterrupt'
documentation_source_path: 'ref/f2838xm4hardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# F2838x-M4 Hardware Interrupt

## 端口

### 输入

### **SimIRQ** — 仿真中断输入端口标量

当您启用 SimIRQ 输入端口时，Interrupt 模块会在仿真中发起函数调用。但是，**SimIRQ** 在生成的代码中会被忽略。

#### 依赖关系

要启用 **SimIRQ** 端口，请选择 **添加仿真输入端口** 参数。

**数据类型：** `Boolean`
### 输出

### **IRQ** — 生成中断请求 `Scalar`

该模块的输出是一个函数调用。函数调用线的大小等于该模块设置为处理的中断数。

## 参数

### **中断组** — 选择中断组 `Cortex-M Exceptions` (默认) | `MCANSS` | `ECAT` | `DCAN` | `EMAC` | `UART` | `SSI` | `I2C` | `USB` | `DMA` | `DMA` | `IPC` | `FMC` | `AES` | `Timer` | `Errors`

**中断组** 列出中断描述文件中的所有中断组。选择某个中断组会更改 **中断名称** 参数中的值列表。

### **中断名称** — 选择 ISR `NMI_Handler` (默认) | `HardFault_Handler` | `…`

**中断名称** 对应于处理器中断向量表中的特定条目。可用的 ISR 取决于中断组。

### **中断编号** — 只读参数 `-14` (默认) | `0` | `5` | `…`

此只读参数指示所选 ISR 在目标硬件中断向量表中的位置。

### **Simulink 任务优先级** — 设置下游函数调用的优先级 `30` (默认) | 正整数或非负整数

您在此参数中指定的值设置下游函数调用子系统的优先级。所选 (ISR) 的 Simulink 任务优先级相对于模型基础速率优先级。

**注意**

默认模型基础采样率优先级设置为 40，其中较低的优先级值表示较高优先级的任务。为实现这一点，**较高优先级值表示较高的任务优先级** 选项在 **配置参数** 的 **求解器** 窗格中处于禁用状态。

### **禁用中断抢占** — 选择以禁用中断抢占 `off` (默认) | `on`

默认情况下，中断可以被更高优先级的中断抢占。选择此选项可允许低优先级中断完成其执行，而不会被其他中断抢占。

### **添加仿真输入端口** — 选择以启用输入端口 off (默认) | on

选择此选项以启用 **SimIRQ** 输入。当您启用 SimIRQ 输入端口时，Interrupt 模块会在仿真中发起函数调用。但是，**SimIRQ** 在生成的代码中会被忽略。

## 所属库

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / Scheduling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

使用 F2838x-M4 Hardware Interrupt 模块在模型的生成代码中自动创建中断服务例程 (ISR)。ISR 执行与该模块关联的下游函数调用子系统。

使用此模块，您可以：

- 在 TI C2000 ARM Cortex-M4 上创建 ISR。
- 设置 ISR 优先级。
- 启用或禁用中断抢占。
- 使用仿真输入模拟中断和下游子系统的触发。

此模块仅为指定的 ISR 生成代码。要更改配置以启用中断和特定触发选项，请使用所选外设的设置。

例如，要在 Hardware Interrupt 模块上为 UART 外设创建 ISR，请在 **中断组** 参数中选择 `UART`，并在 **中断名称** 参数中选择 `UART0INT_Handler`。要在 UART Transmit 和 UART Receive 模块上创建 ISR，请将 **中断名称** 参数设置为 `UART0INT_Handler`。

要从 UART Transmit 模块触发 ISR，请在 **配置参数 > 硬件实现 > 目标硬件资源 > UART** 中选中 **启用发送中断** 复选框。如果您的模型没有 UART Transmit 模块，则选中此复选框没有效果。

当您选择必要的 Hardware Interrupt 模块设置时，来自 UART Receive 模块的 ISR 会自动触发，因为在 **配置参数 > 硬件实现 > 目标硬件资源 > UART** 中，**启用接收中断** 复选框默认处于选中状态。

**注意**

使用中断函数调用子系统内的 MCAN Interrupt Status 模块清除中断源。
