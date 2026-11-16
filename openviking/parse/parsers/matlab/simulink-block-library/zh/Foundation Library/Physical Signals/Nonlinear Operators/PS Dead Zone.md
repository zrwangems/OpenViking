---
type: simulink-block
title: 'PS Dead Zone'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psdeadzone'
documentation_source_path: 'ref/psdeadzone.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Dead Zone

## 端口

### 输入

### **I** — 输入物理信号，untyped physical signal

输入物理信号。

端口名称在模块图标中不可见，但您可以在模块对话框的 **描述** 选项卡中点击 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以在模块对话框的 **描述** 选项卡中点击 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **上限** — 死区上界 `0.5 1`（默认）

死区的上限，或终点。

参数单位必须与输入信号的单位相容。您可以从下拉列表中选择单位，或键入所需单位名称（如 `rpm`）或有效表达式（如 `rad/s`）。有关详细信息和单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **下限** — 死区下界 `-0.5 1`（默认）

死区的下限，或起点。

参数单位必须与输入信号的单位相容。您可以从下拉列表中选择单位，或键入所需单位名称（如 `rpm`）或有效表达式（如 `rad/s`）。有关详细信息和单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **启用过零检测** — 是否启用过零检测 `on`（默认）| `off`

清除以禁用过零检测并提高仿真速度。有关详细信息，请参阅管理 Simscape 模型中的过零。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **启用过零检测** 复选框。清除此复选框可禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

为物理信号提供零输出区域

当输入信号落在指定的区域内时，PS Dead Zone 模块生成零输出，该区域称为死区。您可以将死区的下限和上限指定为模块参数。模块输出取决于输入和死区：

- 如果输入在死区内（大于下限且小于上限），则输出为零。
- 如果输入大于或等于上限，则输出为输入减去上限。
- 如果输入小于或等于下限，则输出为输入减去下限。

输入和输出都是物理信号。Untyped physical ports 支持单位传播。输出信号具有与输入信号相同的物理单位。
