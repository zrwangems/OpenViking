---
type: simulink-block
title: 'PS Variable Delay'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Delays'
documentation_page: 'psvariabledelay'
documentation_source_path: 'ref/psvariabledelay.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Variable Delay

## 端口

### 输入

### **U** — 输入物理信号，untyped physical signal

正在被延迟的输入物理信号。

### **T** — 延迟时间，s physical signal

提供延迟时间的输入物理信号。

### **H** — 初始时间间隔内的输出，untyped physical signal

提供初始时间间隔内要输出的值的输入物理信号，此时自仿真开始以来的时间小于或等于延迟时间。该信号单位必须与端口 **Y** 处输出信号的单位一致。
### 输出

### **Y** — 输出物理信号，untyped physical signal

输出物理信号。

## 参数

### **Maximum delay time** — 信号的延迟时间 `10 s`（默认值）

延迟时间的上限。在仿真期间超过最大延迟时间将导致运行时错误。参数值必须为正。

## 所属库

Simscape / Foundation Library / Physical Signals / Delays

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

按可变时间延迟输入物理信号

PS Variable Delay 模块通过延迟输入物理信号 **U** 来生成输出物理信号 **Y**：

*Y* = *U* ( *t* –
*τ* )

其中 *τ* 是延迟时间，可在整个仿真过程中变化。您通过输入端口 **T** 以信号形式提供延迟时间。

在初始时间间隔内，当 *t* <= StartTime + *τ* 时，模块输出通过输入端口 **H** 提供的信号值。

**注意**

- 仿真包含带延迟模块的模型时，用于存储数据历史的内存分配由 Solver Configuration 模块中的 **Delay memory budget [kB]** 参数控制。如果超出该预算，仿真将报错。您可以根据可用内存资源调整此参数值。
- 有关如何对包含带延迟模块的模型进行线性化的建议，请参阅 Linearizing with Simulink Linearization Blocks。

无类型物理端口有助于单位传播。端口 **Y** 处的输出信号与端口 **U** 处的输入信号具有相同的物理单位。端口 **H** 处的信号单位必须与输出信号的单位一致。

Variable Transport Delay 示例展示了如何使用通过 Simscape™ 语言编写的自定义模块来对可变传输延迟进行建模。
