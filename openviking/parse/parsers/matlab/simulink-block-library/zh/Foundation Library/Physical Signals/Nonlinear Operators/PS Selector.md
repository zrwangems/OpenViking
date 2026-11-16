---
type: simulink-block
title: 'PS Selector'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psselector'
documentation_source_path: 'ref/psselector.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Selector

## 端口

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号，指定为向量或矩阵。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中查看此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号，包含输入信号的选定元素。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中查看此名称。

## 参数

### **Indices** — 选定信号元素的索引 `1` (默认) | 大于 1 的整数标量或向量

通过指定索引来选择输入信号的元素。参数值可以是范围为 1 到输入信号中元素数量的整数标量或向量。索引可以按任意顺序排列，以便构造排列和重复。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从向量或矩阵输入物理信号中选择元素

PS Selector 模块允许您从输入向量或矩阵中选择一个或多个元素。使用 **Indices** 参数选择输入信号中的元素。索引可以按任意顺序排列，以便构造排列和重复。
