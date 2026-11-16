---
type: simulink-block
title: 'PS Bias'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Functions'
documentation_page: 'psbias'
documentation_source_path: 'ref/psbias.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Bias

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

### **Bias** — 要添加到输入信号的常量偏置 `1 1`（默认）

要添加到输入信号的常量偏置。第一个编辑框表示偏置的值。如果输入信号是标量，则该值也必须是标量。如果输入信号是向量或矩阵，则该值可以是标量，也可以是与输入信号维度匹配的向量或矩阵。您可以指定正值和负值。

第二个组合框表示偏置的单位。此单位必须与输入信号的单位量纲一致。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需的单位名称，例如 `rpm`，或有效表达式，例如 `rad/s`。
有关更多信息和单位缩写列表，请参阅“如何在模块对话框中指定单位”和“单位定义”。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

向输入物理信号添加常量偏置

PS Bias 模块向输入物理信号添加常量偏置：

y=u+b

其中：

- *y* 是输出端口 **O** 处的物理信号。
- *u* 是输入端口 **I** 处的物理信号。
- *b* 是偏置。
