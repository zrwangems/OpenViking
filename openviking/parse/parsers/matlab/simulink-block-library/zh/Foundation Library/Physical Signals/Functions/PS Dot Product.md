---
type: simulink-block
title: 'PS Dot Product'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psdotproduct'
documentation_source_path: 'ref/psdotproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Dot Product

## 端口

### 输入

### **I1** — 输入物理信号，无类型物理信号

第一个输入物理信号，指定为行向量、列向量或矩阵。

端口名称在模块图标中不可见，但你可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### **I2** — 输入物理信号，无类型物理信号

第二个输入物理信号，指定为与 **I1** 大小相同的向量或矩阵。

端口名称在模块图标中不可见，但你可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号，标量。

端口名称在模块图标中不可见，但你可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

计算两个向量或矩阵物理信号的标量点积

PS Dot Product 模块计算两个向量或矩阵物理信号的标量点积：

y=dot(u1,u2)

其中：

- *y* 是输出端口 **O** 处的物理信号。
- *u1* 是输入端口 **I1** 处的物理信号。
- *u2* 是输入端口 **I2** 处的物理信号。

这两个输入物理信号可以是向量或矩阵：

- 如果 *u1* 和 *u2* 是向量，则它们必须具有相同的长度。
- 如果 *u1* 和 *u2* 是矩阵，则它们必须具有相同的大小，并且该模块计算逐列点积。

输出端口处的单位由单位传播规则确定。有关详细信息，请参阅物理信号单位传播。
