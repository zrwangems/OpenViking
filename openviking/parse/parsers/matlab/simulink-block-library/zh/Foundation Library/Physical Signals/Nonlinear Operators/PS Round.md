---
type: simulink-block
title: 'PS Round'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psround'
documentation_source_path: 'ref/psround.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Round

## 端口

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号。传递给舍入函数（例如 `round`）的参数必须是无量纲的。因此，输入信号不必是标量，但必须具有单位 `1`（无量纲）。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级含旧版物理信号模块的模型。

## 描述

将输入物理信号舍入到最接近的整数

PS Round 模块将输入物理信号舍入到最接近的整数：

O=round(I)

其中

|  |  |
| --- | --- |
| *I* | 输入端口处的物理信号 |
| *O* | 输出端口处的物理信号 |

输入和输出都是物理信号。无类型物理端口有助于信号大小传播。然而，传递给舍入函数（例如 `round`）的参数必须是无量纲的。因此，输入信号必须具有单位 1（无量纲），并且输出信号也是无量纲的。
