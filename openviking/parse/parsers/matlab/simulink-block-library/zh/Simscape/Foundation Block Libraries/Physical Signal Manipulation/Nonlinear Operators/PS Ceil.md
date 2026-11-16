---
type: simulink-block
title: 'PS Ceil'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Nonlinear Operators'
documentation_page: 'psceil'
documentation_source_path: 'ref/psceil.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Ceil

## 端口

### 输入

### **I** — 输入物理信号，untyped physical signal

输入物理信号。传递给舍入函数（如 `ceil`）的参数必须无量纲。因此，输入信号不必是标量，但必须具有单位 `1`（无量纲）。

端口名在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

R2025b 中未记载。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记载。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不带单位传播的旧版模块，请使用 Upgrade Advisor 将您的模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

输出大于或等于输入物理信号的最小整数

PS Ceil 模块将输入物理信号朝正无穷大方向舍入，即舍入到大于或等于输入值的最近整数：

O=ceil(I)

其中

|  |  |
| --- | --- |
| *I* | 输入端口处的物理信号 |
| *O* | 输出端口处的物理信号 |

输入和输出都是物理信号。无类型物理端口有助于信号大小传播。但是，传递给舍入函数（如 `ceil`）的参数必须无量纲。因此，输入信号必须具有单位 1（无量纲），输出信号也无量纲。
