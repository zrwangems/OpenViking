---
type: simulink-block
title: 'External Interrupt'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Event Scheduling and Interrupt Handling'
documentation_page: 'externalinterrupt'
documentation_source_path: 'supportpkg/arduino_ref/externalinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# External Interrupt

## 端口

### 输入

### **SimIRQ** — 用于仿真目的的引脚输入 标量

在仿真期间，您可以通过将 Simulink 库中的 Source 模块连接到 **SimIRQ** 端口来仿真该模块的输入。如果提供给该模块的输入为布尔 true，则该模块会触发下游 Function-Call Subsystem。如果未提供输入，则该模块会在仿真持续运行期间触发下游 Function-Call Subsystem。在代码生成期间，连接到该端口的任何模块都会被忽略，并且对生成的代码没有任何影响。

#### 依赖关系

仅当您在模块参数对话框中选择 **Add simulation input port** 参数时，**SimIRQ** 端口才可用。

**数据类型：** `Boolean`
### 输出

### **IRQ** — 中断请求 标量

**IRQ** 端口连接下游 Function-Call Subsystem，使其在所选中断发生时被触发。

## 参数

### **Pin number** — 硬件上的引脚编号 `2`（默认）

指定硬件上用于生成外部中断的数字输入引脚编号。对于不同的 Arduino 硬件，可用于中断的引脚不同。有关 Arduino 支持的中断引脚的信息，请参阅 Pins With Interrupts。

单击 **查看引脚映射** 以打开 Arduino Pin Mapping 表。

要了解如何为该模块分配引脚，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Pull-Up input pin** — 硬件上的引脚编号 off（默认） | on

- on – 当没有输入连接到该引脚时，所选硬件引脚被设置为逻辑高电平。
- off – 当没有输入连接到该引脚时，所选硬件引脚保持悬空。

### **Mode** — 数字引脚上触发函数调用的跳变 `RISING`（默认） | `FALLING` | `CHANGE` | `LOW` | `HIGH`

选择 **Mode** 以指定所选引脚上的哪种跳变触发下游函数调用。

| Mode | 中断触发条件 |
| --- | --- |
| `LOW` | 引脚为低电平。 |
| `CHANGE` | 引脚值发生变化。 |
| `RISING` | 引脚值从低变为高。 |
| `FALLING` | 引脚值从高变为低。 |
| `HIGH` | 引脚为高电平。 |

下图显示了在不同中断模式下，当引脚值变化时，该模块如何执行下游函数调用。

### **Add simulation input port** — 用于提供仿真用途输入的选项 off（默认） | on

当您选择 **Add simulation input port** 参数时，**SimIRQ** 输入端口变为可用。要在仿真期间向该模块提供输入，请将 Source 模块连接到 **SimIRQ** 输入端口。在代码生成期间，连接到该端口的任何模块都会被忽略，并且对生成的代码没有任何影响。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

从中断服务例程触发下游 Function-Call Subsystem

External Interrupt 模块配置 Simulink®，将连接到该模块输出端口的下游 Function-Call Subsystem 视为中断服务例程 (ISR)。ISR 是一段代码，当所选中断在硬件的所选引脚上发生时，CPU 会触发该代码。

在仿真期间，您可以通过将 Simulink 库中的 Source 模块连接到该模块的输入端口，向该模块提供输入。如果提供给该模块的输入为布尔 true，则该模块会触发下游 Function-Call Subsystem。如果未提供输入，则该模块会在仿真持续运行期间触发下游 Function-Call Subsystem。在代码生成期间，连接到该模块输入端口的任何仿真模块都会被忽略，并且对生成的代码没有任何影响。

**注意**

- 我们建议您仅在模型层级的父模型中使用 External Interrupt 模块。有关详细信息，请参阅 Model References。
- External Interrupt 模块目前不支持 Arduino® Nano 33 BLE Sense 开发板。
