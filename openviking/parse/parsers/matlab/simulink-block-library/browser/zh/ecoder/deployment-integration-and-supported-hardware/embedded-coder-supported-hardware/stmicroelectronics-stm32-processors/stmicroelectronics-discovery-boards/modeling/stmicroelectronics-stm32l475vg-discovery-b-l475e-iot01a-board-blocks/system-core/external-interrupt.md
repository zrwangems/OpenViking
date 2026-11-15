---
type: simulink-block
title: 'External Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'externalinterrupt'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/externalinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# External Interrupt

## 端口

### 输入

### **SimIRQ** — 用于仿真目的的引脚输入标量

在仿真期间，您可以通过将来自 Simulink 库的 boolean 信号连接到 **SimIRQ** 端口来模拟模块的输入。如果提供给模块的输入为 boolean true，则模块触发下游 function-call subsystem。如果未提供输入，则模块会在仿真持续运行期间一直触发下游 function-call subsystem。在代码生成期间，连接到此端口的所有模块都会被忽略，并且不会对生成的代码产生任何影响。

#### 依赖项

要启用此端口，请选择 **Enable simulation input**。

**数据类型：** `Boolean`

### 输出

### **IRQ** — 中断请求 标量 | 向量

**IRQ** 端口连接下游 Function-Call Subsystem，以便在所选中断发生时触发。

## 参数

### **Pin** — 硬件上的引脚名称 `5`（默认） | `any pin number from pin map of board`

指定要用于生成外部中断的硬件上的数字输入引脚名称。可用于中断的引脚因不同的 STMicroelectronics® 硬件板而异。

点击 **View pin map** 打开 STMicroelectronics Pin Mapping 表。

### **Pull mode** — 将硬件引脚设置为逻辑高或逻辑低 `Pull-up`（默认） | `Pull-down` | `No pull-up or pull-down`

选择以下模式之一。

- `Pull-up` – 当没有输入连接到引脚时，所选硬件引脚设置为逻辑高。
- `Pull-down` – 当没有输入连接到引脚时，所选硬件引脚保持悬空。
- `No pull-up or pull-down` – 当没有输入连接到引脚时，所选硬件引脚既不设置为逻辑高也不保持悬空。

### **Trigger type** — 数字引脚上触发函数调用的跳变 `Rising`（默认） | `Falling` | `Either`

选择 **Trigger type** 以指定所选引脚上的哪种跳变触发下游函数调用。

| Trigger type | 中断触发条件 |
| --- | --- |
| `Rising` | 数字引脚值从低变为高。 |
| `Falling` | 数字引脚值从高变为低。 |
| `Either` | 数字引脚值从低变为高或从高变为低。 |

下图展示了当引脚值在不同中断模式下变化时，模块如何执行下游函数调用。

### **Enable simulation input** — 用于提供仿真用途输入的选项 `off`（默认） | `on`

该参数启用 **SimIRQ** 输入端口。

### **Initial pin status** — 输入引脚的初始状态 `false`（默认） | `true`

选择以下引脚状态之一。

- `false` - 初始引脚状态为 `0`。
- `true` - 初始引脚状态为 `1`。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

从中断服务例程触发下游 function-call subsystem

External Interrupt 模块配置 Simulink®，将连接到该模块输出端口的下游 Function-Call Subsystem 视为中断服务例程 (ISR)。ISR 是一段代码，当所选中断在硬件的所选引脚上发生时，CPU 会触发该代码。

在仿真期间，您可以通过将来自 Simulink 库的 boolean 信号连接到 External Interrupt 模块的输入端口，为 External Interrupt 模块提供输入。如果在 boolean 输入中检测到所选的 `Trigger type` 边沿，则模块触发下游 function-call subsystem。如果未提供输入，则模块会在仿真持续运行期间一直触发下游 function-call subsystem。在代码生成期间，连接到 External Interrupt 模块输入端口的所有仿真模块都会被忽略，并且不会对生成的代码产生任何影响。

**注**

我们建议仅在模型层次结构的父模型中使用 External Interrupt 模块。有关详细信息，请参阅模型引用。
