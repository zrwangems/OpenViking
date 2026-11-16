---
type: simulink-block
title: 'PS Fix'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psfix'
documentation_source_path: 'ref/psfix.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Fix

## 端口

### 输入

### **I** — 输入物理信号，untyped physical signal

输入物理信号。传递给舍入函数（如 `fix`）的参数必须为无量纲。因此，输入信号不必为标量，但其单位必须为 `1`（无量纲）。

端口名称在模块图标中不可见，但您可以单击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以单击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不带单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

将输入物理信号向零舍入

PS Fix 模块将输入物理信号向零舍入，即，对于正信号，返回小于或等于输入值的最近整数；对于负信号，返回大于或等于输入值的最近整数：

O=fix(I)

其中

|  |  |
| --- | --- |
| *I* | 输入端口处的物理信号 |
| *O* | 输出端口处的物理信号 |

输入和输出均为物理信号。无类型物理端口便于信号大小传播。但是，传递给舍入函数（如 `fix`）的参数必须为无量纲。因此，输入信号的单位必须为 1（无量纲），输出信号也无量纲。
