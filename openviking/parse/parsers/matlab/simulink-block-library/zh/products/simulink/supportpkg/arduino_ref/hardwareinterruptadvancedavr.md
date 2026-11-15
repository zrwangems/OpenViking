---
type: simulink-block
title: 'Hardware Interrupt AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Event Scheduling and Interrupt Handling'
documentation_page: 'hardwareinterruptadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedavr.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt AVR

## 端口

### 输出

### **Default event** — 生成中断请求标量

模块输出一个函数调用。

## 参数

### **Interrupt group** — 选择外设 ISR `Timer 0` (默认) | `Timer 1` | `Timer 2` | `Timer 3` | `Timer 4` | `Timer 5` | `Analog to digital converter (ADC)`

此参数列出 Arduino 板上某一类型外设的所有可用 ISR。**Interrupt name** 参数中可用的值取决于在此参数中选择的中断组。

### **Interrupt name** — 选择 ISR `Timer0_COMPA` (默认) | `Timer0_COMPB` | `Timer1_COMPA` | `Timer1_COMPB` | `Timer1_COMPC` | `Timer1_OVF` | `Timer2_COMPA` | `Timer2_COMPB` | `Timer2_OVF` | `Timer3_COMPA` | `Timer3_COMPB` | `Timer3_COMPC` | `Timer3_OVF` | `Timer4_COMPA` | `Timer4_COMPB` | `Timer4_COMPC` | `Timer4_COMPD` | `Timer4_OVF` | `Timer5_COMPA` | `Timer5_COMPB` | `Timer5_COMPC` | `Timer5_OVF` | `Analog to digital converter (ADC)`

中断名称指定 Hardware Interrupt 模块的 ISR。此参数对应 Arduino 板中断向量表中的特定条目。可用的 ISR 取决于 **Interrupt group**。

#### 依赖关系

- 要启用 `Timer0_COMPA` 和 `Timer0_COMPB` 中断，请将 **Interrupt group** 设置为 `Timer 0`。
- 要启用 `Timer1_COMPA` 和 `Timer1_COMPB`、`Timer1_COMPC` 和 `Timer1_OVF` 中断，请将 **Interrupt group** 设置为 `Timer 1`。
- 要启用 `Timer2_COMPA` 和 `Timer2_COMPB`，以及 `Timer1_OVF` 中断，请将 **Interrupt group** 设置为 `Timer 2`。
- 要启用 `Timer3_COMPA` 和 `Timer3_COMPB`、`Timer3_COMPC` 和 `Timer3_OVF` 中断，请将 **Interrupt group** 设置为 `Timer 3`。
- 要启用 `Timer4_COMPA` 和 `Timer4_COMPB`、`Timer4_COMPC`、`Timer4_COMPC` 和 `Timer4_OVF` 中断，请将 **Interrupt group** 设置为 `Timer 4`。
- 要启用 `Timer5_COMPA` 和 `Timer5_COMPB`、`Timer5_COMPC` 和 `Timer5_OVF` 中断，请将 **Interrupt group** 设置为 `Timer 5`。
- 要启用 `Analog to digital converter (ADC)` 中断，请将 **Interrupt group** 设置为 `ADC`。

## 所属库

Simulink Support Package for Arduino Hardware / Advanced / AVR

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从 Arduino AVR 内核的中断服务例程触发下游函数调用子系统

使用 Hardware Interrupt 模块，可以在 Simulink® 模型生成的代码中，为所选中断自动创建中断服务例程 (ISR)。该 ISR 执行与模块事件端口关联的下游函数调用子系统。

此模块仅为您选择或指定的 ISR 生成代码。要更改配置、启用中断并指定触发选项，请使用所选外设的设置。例如，要在 Hardware Interrupt 模块上为 ADC 外设创建 ISR：

- 您的 Simulink 模型必须包含 Analog Input 模块。在该模块中，选择 **Enable ADC conversion complete interrupt** 参数。
- 在 Hardware Interrupt 模块中，设置以下参数：

  - **Interrupt group** 设置为 `Analog to digital converter (ADC)`
  - **Interrupt name** 设置为 `ADC`

类似地，要在 Hardware Interrupt 模块上为 PWM 外设创建 ISR：

- 您的 Simulink 模型必须包含 PWM 模块。在该模块中，选择 **Enable compare match (MCx) interrupt** 或 **Enable overflow/underflow (OVF) interrupt** 参数，或同时选择这两个参数。
- 在 Hardware Interrupt 模块中，设置以下参数：

  - **Interrupt group** 设置为 `Timer 0`、`Timer 1`、`Timer 2`、`Timer 2`、`Timer 3`、`Timer 4` 或 `Timer 5` 之一。
  - **Interrupt name** 设置为可用的 ISR，具体取决于 **Interrupt group**。

**注意**

Hardware Interrupt 模块支持 C/C++ 代码生成。此功能允许您使用 Embedded Coder® 生成 C 和 C++ 代码。

### 支持的 Arduino 板

- Arduino® Uno
- Arduino Mega 2560
- Arduino Mega ADK
- Arduino Leonardo
- Arduino Micro
