---
type: simulink-block
title: 'PS Saturation'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'pssaturation'
documentation_source_path: 'ref/pssaturation.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Saturation

## 端口

### 输入

### **I** — 输入物理信号，untyped physical signal

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **Upper limit** — 信号上限 `0.5 1`（默认）

输入信号的上界。当 PS Saturation 模块的输入信号高于此值时，模块的输出会被限幅到此值。

参数单位必须与输入信号的单位一致。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`），或有效表达式（如 `rad/s`）。有关更多信息和单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **Lower limit** — 信号下限 `-0.5 1`（默认）

输入信号的下界。当 PS Saturation 模块的输入信号低于此值时，模块的输出会被限幅到此值。

参数单位必须与输入信号的单位一致。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`），或有效表达式（如 `rad/s`）。有关更多信息和单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **Enable zero-crossing detection** — 是否启用过零检测 `on`（默认） | `off`

清除此复选框可禁用过零检测并提高仿真速度。有关更多信息，请参阅管理 Simscape 模型中的过零。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **Enable zero-crossing detection** 复选框。清除此复选框可以禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不会传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关更多信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

限制物理信号的范围

PS Saturation 模块对物理信号施加下限和上限。当输入信号处于 **Lower limit** 和 **Upper limit** 参数指定的范围内时，输入信号原样通过。当输入信号超出这些边界时，信号会被限幅到上限或下限。

当 **Lower limit** 和 **Upper limit** 参数设置为相同值时，模块输出该值。

输入和输出都是物理信号。无类型物理端口有助于单位传播。输出信号与输入信号具有相同的物理单位。
