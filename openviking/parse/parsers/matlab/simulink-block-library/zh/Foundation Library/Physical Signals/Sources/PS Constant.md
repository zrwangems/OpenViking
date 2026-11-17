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
chinese_source: worker-translation
---

# PS Constant

## 端口

### 输出

### **O** — 输出物理信号，类型由模块参数值物理信号决定

输出物理信号。信号值和单位由 **Constant** 参数的值和单位决定。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

### **Constant** — 信号值和单位 `1 1`（默认值）

端口 **O** 处输出信号的值和单位。第一个编辑框表示信号值。您可以指定正值和负值。

第二个组合框表示输出信号的单位。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关更多信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

生成恒定物理信号

PS Constant 模块生成恒定值的物理信号。您可以将信号的值和单位指定为 **Constant** 参数。
