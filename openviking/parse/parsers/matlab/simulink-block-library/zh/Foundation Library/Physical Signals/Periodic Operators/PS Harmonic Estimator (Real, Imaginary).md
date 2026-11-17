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

### **I** — 周期信号，无类型物理信号

输入物理信号。该信号必须是周期性的。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到该名称。

### 输出

### **Re** — 谐波信号的实部，无类型物理信号

对应于所选谐波实部的输出物理信号。

### **Im** — 谐波信号的虚部，无类型物理信号

对应于所选谐波虚部的输出物理信号。

## 参数

### **基频** — 周期信号频率 `60 Hz`（默认值）

周期信号的基频。

### **谐波次数** — 谐波次数 `1`（默认值）

周期信号中的谐波次数。该值必须为正整数。

## 所属库

Simscape / Foundation Library / Physical Signals / Periodic Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

测量周期信号谐波的实部和虚部

PS Harmonic Estimator (Real, Imaginary) 模块测量周期信号的单个频率分量（谐波）的实部和虚部。

如果信号在可测量的时间范围内完成一个模式（称为周期），并在随后的相同周期内重复该模式，则该信号是周期性的。信号基频是每秒的周期数。

该模块接受包含一个或多个谐波的物理信号。它输出所选谐波信号的实部和虚部。无类型物理端口有助于单位传播。两个端口上的输出信号与输入信号具有相同的物理单位。

为获得有意义的结果，请至少运行信号一个完整时间周期的仿真。
