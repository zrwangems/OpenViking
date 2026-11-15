---
type: simulink-block
title: 'External Interrupt'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'externalinterrupt'
documentation_source_path: 'nucleo/ref/externalinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# External Interrupt

## 端口

### 输入

### **SimIRQ** — 用于仿真目的的引脚输入 标量

在仿真期间，您可以通过将来自 Simulink 库的布尔信号连接到 **SimIRQ** 端口来仿真该模块的输入。如果提供给该模块的输入为布尔值 true，则该模块会触发下游 Function-Call Subsystem。如果未提供输入，则该模块会在仿真继续运行期间触发下游 Function-Call Subsystem。在代码生成期间，任何连接到此端口的模块都会被忽略，并且对生成的代码没有影响。

#### 依赖关系

要启用此端口，请选择 **Enable simulation input**。

**数据类型：** `Boolean`

### 输出

### **IRQ** — 中断请求 标量 | 向量

**IRQ** 端口连接下游 Function-Call Subsystem，以在所选中断发生时触发。

## 参数

### **Pin** — 硬件上的引脚名称 `5`（默认） | `any pin number from pin map of board`

指定硬件上用于生成外部中断的数字输入引脚名称。可用于中断的引脚因不同的 STMicroelectronics® 硬件板而异。

点击 **View pin map** 以打开 STMicroelectronics Pin Mapping 表。

### **Pull mode** — 将硬件引脚设置为逻辑高电平或低电平 `Pull-up`（默认） | `Pull-down` | `No pull-up or pull-down`

选择以下模式之一。

- `Pull-up` – 当没有输入连接到该引脚时，所选硬件引脚设置为逻辑高电平。
- `Pull-down` – 当没有输入连接到该引脚时，所选硬件引脚保持悬空。
- `No pull-up or pull-down` – 当没有输入连接到该引脚时，所选硬件引脚既不设置为逻辑高电平，也不保持悬空。

### **Trigger type** — 数字引脚上触发函数调用的跳变 `Rising`（默认） | `Falling` | `Either`

选择 **Trigger type** 以指定所选引脚上的哪种跳变触发下游函数调用。

| Trigger type | 中断触发条件 |
| --- | --- |
| `Rising` | 数字引脚值从低变为高。 |
| `Falling` | 数字引脚值从高变为低。 |
| `Either` | 数字引脚值从低变为高或从高变为低。 |

下图展示了在不同中断模式下，当引脚值变化时，该模块如何执行下游函数调用。

### **Enable simulation input** — 用于仿真目的提供输入的选项 `off`（默认） | `on`

该参数启用 **SimIRQ** 输入端口。

### **Initial pin status** — 输入引脚的初始状态 `false`（默认） | `true`

选择以下引脚状态之一。

- `false` - 初始引脚状态为 `0`。
- `true` - 初始引脚状态为 `1`。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

从中断服务例程触发下游 Function-Call Subsystem

External Interrupt 模块将 Simulink® 配置为将连接到该模块输出端口的下游 Function-Call Subsystem 视为中断服务例程 (ISR)。ISR 是当所选中断在硬件所选引脚上发生时由 CPU 触发的一段代码。

在仿真期间，您可以通过将来自 Simulink 库的布尔信号连接到 External Interrupt 模块的输入端口，为 External Interrupt 模块提供输入。如果在布尔输入中检测到所选的 `Trigger type` 边沿，则该模块触发下游 Function-Call Subsystem。如果未提供输入，则该模块会在仿真继续运行期间触发下游 Function-Call Subsystem。在代码生成期间，连接到 External Interrupt 模块输入端的任何仿真模块都会被忽略，并且对生成的代码没有影响。

**注意**

我们建议仅在模型层次结构中的父模型中使用 External Interrupt 模块。有关详细信息，请参阅模型引用。
