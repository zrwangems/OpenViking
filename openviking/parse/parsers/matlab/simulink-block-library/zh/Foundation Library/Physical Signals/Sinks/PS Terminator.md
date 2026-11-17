---
type: simulink-block
title: 'PS Terminator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sinks'
documentation_page: 'psterminator'
documentation_source_path: 'ref/psterminator.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Terminator

## 端口

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Sinks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关详细信息，请参阅使用旧版物理信号模块升级模型。

## 描述

用于未连接物理信号输出的终结器

使用 PS Terminator 模块来封端未连接到其他模块的物理信号输出端口。

与物理建模中的守恒端口或 Simulink® 输出端口不同，未连接的物理信号输出端口不会生成警告。但是，您可以使用 PS Terminator 模块来明确表示信号并非无意中未连接。

该模块图标的大小允许您将 PS Terminator 模块连接到开路端口，而无需重新布线相邻的线路：
