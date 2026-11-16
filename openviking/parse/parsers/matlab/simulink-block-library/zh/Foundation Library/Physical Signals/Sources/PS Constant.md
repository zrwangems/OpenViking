---
type: simulink-block
title: 'PS Constant'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psconstant'
documentation_source_path: 'ref/psconstant.html'
language: zh-CN
chinese_source: official
---

# PS Constant

## 端口

### 输出

### **O** — 输出物理信号，由模块参数值定义类型 物理信号

输出物理信号。信号的值和单位由**常数**参数的值和单位确定。

端口名称在模块图标中不可见，但您可以在模块对话框的**描述**选项卡中点击**源代码**链接，在基础源文件中查看此名称。

## 参数

### **常数** — 信号值和单位 `1 1` (默认)

端口 **O** 处的输出信号的值和单位。第一个编辑框表示信号值。您可以指定正值和负值。

第二个组合框表示输出信号的单位。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需的单位名称，例如 `rpm`，或键入有效的表达式，例如 `rad/s`。有关详细信息以及单位缩写列表，请参阅How to Specify Units in Block Dialogs和Unit Definitions。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007b 中推出**

### R2019a: 单位传播

在 R2019a 之前，此模块不会传播物理单位。

如果您的模型包含没有单位传播的旧模块，请使用升级顾问将您的模块升级到最新版本。有关详细信息，请参阅Upgrading Models with Legacy Physical Signal Blocks。

## 描述

生成恒定的物理信号

PS Constant 模块生成一个恒定的物理信号。您可以将信号的值和单位指定为**常数**参数。
