---
type: simulink-block
title: 'PS Harmonic Estimator (Real, Imaginary)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Periodic Operators'
documentation_page: 'psharmonicestimatorrealimaginary'
documentation_source_path: 'ref/psharmonicestimatorrealimaginary.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Harmonic Estimator (Real, Imaginary)

## 端口

### 输入

### **I** — 周期信号，untyped physical signal

输入物理信号。该信号必须为周期信号。

端口名称在模块图标中不可见，但你可以通过点击模块对话框的 **描述** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

### 输出

### **Re** — 谐波信号的实部，untyped physical signal

输出物理信号，对应所选谐波的实部。

### **Im** — 谐波信号的虚部，untyped physical signal

输出物理信号，对应所选谐波的虚部。

## 参数

### **Base frequency** — 周期信号频率 `60 Hz`（默认）

周期信号的基频。

### **Harmonic number** — 谐波次数 `1`（默认）

周期信号中的谐波次数。该值必须为正整数。

## 所属库

Simscape / Foundation Library / Physical Signals / Periodic Operators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果你的模型包含不带单位传播的旧版模块，请使用 Upgrade Advisor 将你的模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

测量周期信号谐波的实部和虚部

The PS Harmonic Estimator (Real, Imaginary) 模块测量周期信号的单个频率分量（谐波）的实部和虚部。

如果一个信号在称为周期的可测量时间范围内完成一个模式，并在后续相同周期中重复该模式，则该信号是周期性的。信号基频是每秒的周期数。

该模块接受存在一个或多个谐波的物理信号。它输出所选谐波的信号的实部和虚部。Untyped physical ports 便于单位传播。两个端口处的输出信号与输入信号具有相同的物理单位。

为获得有意义的结果，请至少运行信号的一个完整时间周期的仿真。
