---
type: simulink-block
title: 'PS Signal Specification'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Utilities'
documentation_page: 'pssignalspecification'
documentation_source_path: 'ref/pssignalspecification.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Signal Specification

## 端口

### 输入

### **I** — 输入物理信号，由模块参数值指定 physical signal 类型

输入物理信号。信号类型（大小和单位）由 **Signal size and unit** 参数值确定。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，由模块参数值指定 physical signal 类型

输出物理信号。信号类型（大小和单位）由 **Signal size and unit** 参数值确定。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **Signal size and unit** — 输入和输出物理信号的大小和单位 `zeros(1, 1) 1`（默认值）

物理信号的大小和单位，将传播到与模块连接的未类型化物理信号端口。

第一个编辑框表示信号大小。将其指定为 `zeros(m, n)`。默认大小 `zeros(1, 1)` 为标量。

第二个组合框表示信号单位。默认情况下，单位为 `1`（无量纲）。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`）或有效表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位 和 单位定义。

## 所属库

Simscape / Foundation Library / Physical Signals / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

指定物理信号的大小和单位

PS Signal Specification 模块允许您显式指定物理信号的大小和单位。当信号大小和单位无法根据模型中的端口连接隐式确定时，请使用此模块。

端口 **I** 处的输入信号和端口 **O** 处的输出信号具有相同的大小和单位。两者均由 **Signal size and unit** 参数的值确定。将此模块连接到未类型化物理信号端口，以指定所需的信号类型。

将信号大小指定为 `zeros(m, n)`。例如，标量为 `zeros(1, 1)`。

单位组合框包含常用单位的下拉列表，例如 Simulink-PS Converter 和 PS-Simulink Converter 模块对话框中提供的单位。它还包含一个字段，您可以在其中键入单位名称或表达式。有关更多信息，请参阅如何在模块对话框中指定单位。
