---
type: simulink-block
title: 'PS Sum of Elements'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'pssumofelements'
documentation_source_path: 'ref/pssumofelements.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Sum of Elements

## 端口

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号，指定为行向量、列向量或矩阵。

端口名称在模块图标中不可见，但您可以通过点击模块对话框**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。如果输入信号是向量，则输出信号是标量。如果输入信号是矩阵，则默认情况下模块计算每个维度沿列方向的元素和。例如，如果输入信号是二维矩阵，则默认情况下输出信号是向量。如果您选中**对所有元素求和**复选框，则输出信号是标量。

端口名称在模块图标中不可见，但您可以通过点击模块对话框**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

### **Sum all elements** — 指定矩阵的求和方法 `Off`（默认）| `On`

如果输入信号是矩阵，则默认情况下模块计算每个维度沿列方向的元素和。要对矩阵的所有元素求和，请选中**对所有元素求和**复选框。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

计算向量或矩阵输入物理信号的元素和

PS Sum of Elements 模块计算向量或矩阵输入物理信号的元素和：

y=sum(u)

其中：

- *y* 是输出端口 **O** 处的物理信号。
- *u* 是输入端口 **I** 处的物理信号。
