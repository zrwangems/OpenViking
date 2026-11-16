---
type: simulink-block
title: 'PS Gain'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psgain'
documentation_source_path: 'ref/psgain.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Gain

## 端口

### 输入

### **I** — 输入物理信号，未类型化物理信号

输入物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，未类型化物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

### **Gain** — 乘法系数 `1 1`（默认）

乘法系数。第一个编辑框表示系数的值。您可以指定正值和负值。

第二个组合框表示乘法系数的单位。默认情况下，单位为 `1`（无单位），这意味着端口 **O** 处的输出信号与输入信号具有相同的单位。如果您为 **Gain** 参数指定了不同的单位，则输出端口 **O** 处的信号单位是输入信号单位乘以 **Gain** 参数的单位。您可以从下拉列表中选择单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。有关更多信息以及单位缩写列表，请参见如何在模块对话框中指定单位和单位定义。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将您的模块升级到最新版本。有关更多信息，请参见升级包含旧版物理信号模块的模型。

## 描述

将输入物理信号乘以常量

PS Gain 模块对输入物理信号与常量值（增益）执行逐元素乘法。您将增益指定为 **Gain** 参数的值和单位。

输入信号值乘以 **Gain** 参数的值。

输出端口处的信号单位由单位传播规则确定。例如，如果输入信号以 `N` 为单位，且 **Gain** 参数单位为 `m`，则输出物理信号的单位为 `N*m`。有关更多信息，请参见物理信号单位传播。
