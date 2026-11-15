---
type: simulink-block
title: 'Hardware Interrupt SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Event Scheduling and Interrupt Handling'
documentation_page: 'hardwareinterruptadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedsamd.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt SAMD

## 端口

### 输出

### **Event name** — 生成中断请求标量

该模块输出一个函数调用。函数调用输出的数量取决于你在 ISR 中选择服务的事件数量。例如，如果你在 **Events to serve** 部分中选择 **ADC RESRDY** 和 **Custom event**，则该模块会启用 **ADC RESRDY** 和 **Custom event** 输出端口。

## 参数

### **Interrupt group** — 选择外设 ISR `Analog to digital converter (ADC)`（默认） | `Timer/Counter for Control Applications (TCC)`

此参数列出 Arduino 板中特定类型外设的所有可用 ISR。**Interrupt name** 参数中的可用值取决于你在此参数中选择的中断组。

### **Interrupt name** — 选择 ISR `ADC_Handler`（默认） | `TCC0_Handler` | `TCC1_Handler` | `TCC2_Handler`

中断名称指定 Hardware Interrupt 模块的 ISR。此参数对应于 Arduino 板中断向量表中的特定条目。可用的 ISR 取决于 **Interrupt group**。

#### 依赖关系

- 要启用 `TCC0_Handler`、`TCC1_Handler` 和 `TCC2_Handler` 中断，请将 **Interrupt group** 设置为 `Timer/Counter for Control Applications (TCC)`。
- 要启用 `ADC_Handler` 中断，请将 **Interrupt group** 设置为 `Analog to digital converter (ADC)`。

### **Interrupt number** — ISR 在中断向量表中的位置 `23`（默认） | `15` | `16` | `17`

此只读参数指示 ISR 在 Arduino 板中断向量表中的位置。

### **Events to serve** — 选择事件及其执行顺序 `ADC RESRDY`（默认） | `ADC OVERRUN` | `Custom event` | `TCC0 overflow` | `TCC0 MCx0` | `TCC0 MCx1` | `TCC0 MCx2` | `TCC0 MCx3` | `TCC1 overflow` | `TCC1 MCx0` | `TCC1 MCx1` | `TCC2 overflow` | `TCC2 MCx0` | `TCC2 MCx1`

从 **Events to serve** 组中选择事件或自定义事件及其各自的执行顺序，以便为你选择的 **Interrupt name** 服务事件。你可以选择自定义事件与其他事件一起执行。你也可以更改事件的执行顺序。

#### 依赖关系

- 要启用 `TCC0 overflow`、`TCC0 MCx0`、`TCC0 MCx1`、`TCC0 MCx2`、`TCC0 MCx3` 和 `Custom event` 事件，请将 **Interrupt group** 设置为 `Timer/Counter for Control Applications (TCC)`，并将 **Interrupt name** 设置为 `TCC0_Handler`。
- 要启用 `TCC1 overflow`、`TCC1 MCx0`、`TCC1 MCx1` 和 `Custom event` 事件，请将 **Interrupt group** 设置为 `Timer/Counter for Control Applications (TCC)`，并将 **Interrupt name** 设置为 `TCC1_Handler`。
- 要启用 `TCC2 overflow`、`TCC2 MCx0`、`TCC2 MCx1` 和 `Custom event` 事件，请将 **Interrupt group** 设置为 `Timer/Counter for Control Applications (TCC)`，并将 **Interrupt name** 设置为 `TCC2_Handler`。
- 要启用 `ADC RESRDY`、`ADC OVERRUN` 和 `Custom event` 事件，请将 **Interrupt group** 设置为 `Analog to digital converter (ADC)`，并将 **Interrupt name** 设置为 `ADC_Handler`。

### **Simulink task priority** — 设置 ISR 的优先级 `30`（默认） | 正整数或非负整数

你在此参数中指定的值设置下游函数调用子系统的优先级。ISR 在 Simulink 中的任务优先级相对于你在 Simulink 模型中设置的基础速率优先级。

**注意**

Simulink 模型中基础速率的默认优先级为 `40`，优先级值越低表示优先级越高。要实现这一点，请在 Configuration Parameters 对话框中，在 **Solver** 窗格中选择 **Higher priority value indicates higher task priority**。

### **Run interrupt service routine as atomic unit** — 选择以禁用中断抢占 `off`（默认） | `on`

选择此参数可在执行当前 ISR 时屏蔽所有其他中断。

### **Clear status after servicing each event** — 选择以清除中断状态标志 `off`（默认） | `on`

选择此选项可在服务每个事件后清除所有中断状态标志。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

针对 Arduino SAMD21 内核，从中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块可为所选中断在 Simulink® 模型的生成代码中自动创建中断服务例程 (ISR)。ISR 执行与该模块事件端口关联的下游函数调用子系统。

与事件输出端口关联的函数调用子系统以与 ISR 相同的优先级运行。

使用此模块，你可以：

- 在 Arduino® 板上创建 ISR。
- 设置 ISR 的优先级。
- 启用或禁用中断抢占。

此模块仅为所选或指定的 ISR 和事件生成代码。要更改配置、启用中断并指定触发选项，请使用所选外设的设置。例如，要在 Hardware Interrupt 模块上为 ADC 外设创建 ISR：

- 你的 Simulink 模型必须包含 Analog Input 模块。在该模块中，选择 **Enable end of conversion interrupt** 参数。
- 在 Hardware Interrupt 模块中，设置以下参数：

  - 将 **Interrupt group** 设置为 `Analog to digital converter`
  - 将 **Interrupt name** 设置为 `ADC_Handler`
  - 将 **Events to serve** 设置为 `ADC RESRDY` 或 `ADC OVERRUN`

类似地，要在 Hardware Interrupt 模块上为 PWM 外设创建 ISR：

- 你的 Simulink 模型必须包含 PWM 模块。在该模块中，选择 **Enable compare match (MCx) interrupt** 或 **Enable overflow/underflow (OVF) interrupt** 参数，或同时选择这两个参数。
- 在 Hardware Interrupt 模块中，设置以下参数：

  - 将 **Interrupt group** 设置为 `Timer/Counter for Control Applications (TCC)`。
  - 将 **Interrupt name** 设置为 `TCC0_Handler`、`TCC1_Handler` 或 `TCC2_Handler`。
  - 将 **Events to serve** 设置为 `TCCx overflow`、`TCCx MCx`。

**注意**

Hardware Interrupt 模块支持 C/C++ 代码生成。此功能允许你使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 板

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
