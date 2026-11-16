---
type: simulink-block
title: 'PS Constant Delay'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Delays'
documentation_page: 'psconstantdelay'
documentation_source_path: 'ref/psconstantdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Constant Delay

## 端口

### 输入

### **U** — 输入物理信号，untyped physical signal

输入物理信号。
### 输出

### **Y** — 输出物理信号，untyped physical signal

输出物理信号。

## 参数

### **Input history** — 初始时间区间内的信号值和单位 `0.0 1`（默认）

在初始时间区间内的输出信号值和单位，直到仿真开始后经过指定的延迟时间为止。第一个编辑框表示信号值。

第二个组合框表示信号单位，该单位必须与端口 **Y** 处输出信号的单位一致。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位
和单位定义。

### **Delay time** — 信号的延迟时间 `1 s`（默认）

信号的延迟，以时间单位表示。参数值必须为正。

## 所属库

Simscape / Foundation Library / Physical Signals / Delays

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关更多信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

将输入物理信号延迟指定时间

PS Constant Delay 模块通过延迟输入物理信号 **U** 来生成输出物理信号 **Y**：

*Y* = *U* ( *t* – *τ* )

其中 *τ* 是延迟时间。

延迟时间在整个仿真过程中保持恒定。您将延迟时间的值指定为 **Delay time** 参数。

对于初始时间区间，当 *t* <= StartTime + *τ* 时，模块输出 **Input history** 参数值。为 **Input history** 参数指定的单位必须与输出信号的单位一致。

**注意**

- 当仿真包含带延迟模块的模型时，用于存储数据历史的内存分配由 Solver Configuration 模块中的 **Delay memory budget
  [kB]** 参数控制。如果超出此预算，仿真将出错。您可以根据可用内存资源
  调整此参数值。
- 有关如何对包含带延迟模块的模型进行线性化的建议，请参阅使用 Simulink Linearization Blocks
  进行线性化。

无类型物理端口有助于单位传播。输出信号与输入信号具有相同的物理单位。
