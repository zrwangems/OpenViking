---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'ref/hardwareinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware Interrupt

## 端口

### 输入

### **Default event task** — 函数调用事件输入仿真 `scalar`

仅用于仿真的消息输入用作直通，在仿真中输出从该模块发出。

#### 依赖关系

要启用此端口，请选择 **启用仿真端口** 参数。
### 输出

### **Default event** — 生成中断请求 `scalar`

该模块的输出为函数调用。

## 参数

### **Simulink 任务优先级** — 设置所选 ISR 的优先级 `50`（默认） | `0-255`

在此参数中指定的值设置下游函数调用子系统的优先级。所选 (ISR) 的 Simulink 任务优先级相对于模型基础速率优先级。

### **将中断服务例程作为原子单元运行** — 选择以禁用中断抢占 `off`（默认） | `on`

选择此参数可在执行所选中断服务例程时阻止所有其他中断。

### **启用仿真端口** — 启用模块中的外设仿真端口 `off`（默认） | `on`

选择此参数可启用外设仿真功能。

### **端口类型** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 Simulink® 信号的仿真端口，以启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **启用仿真端口** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从中断服务例程触发下游函数调用子系统

从中断服务例程 (ISR) 触发下游函数调用子系统。
