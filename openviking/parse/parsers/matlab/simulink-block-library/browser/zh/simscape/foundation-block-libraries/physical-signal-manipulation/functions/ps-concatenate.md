---
type: simulink-block
title: 'PS Concatenate'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Functions'
documentation_page: 'psconcatenate'
documentation_source_path: 'ref/psconcatenate.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Concatenate

## 端口

### 输入

### **I1** — 输入物理信号，untyped physical signal

要拼接的第一个输入物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

### **I2** — 输入物理信号，untyped physical signal

要拼接的第二个输入物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

## 参数

### **水平拼接** — 指定矩阵的拼接方法 `Off`（默认）| `On`

如果输入信号是矩阵，则默认情况下模块垂直拼接它们。要水平拼接矩阵，请选中 **水平拼接** 复选框。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

拼接两个向量或矩阵物理信号

PS Concatenate 模块将两个输入向量或矩阵拼接为单个输出。

两个输入端口处的物理信号必须具有一致的单位。输出端口处的单位由单位传播规则确定。有关详细信息，请参阅物理信号单位传播。

默认情况下，模块垂直拼接矩阵。要水平拼接，请选中 **水平拼接** 复选框。
