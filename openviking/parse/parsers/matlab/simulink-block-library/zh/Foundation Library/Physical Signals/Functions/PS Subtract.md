---
type: simulink-block
title: 'PS Subtract'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'pssubtract'
documentation_source_path: 'ref/pssubtract.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Subtract

## 端口

### 输入

### **I1** — 输入物理信号，untyped physical signal

第一个输入物理信号。在模块图标中，此端口标有加号 (**+**)。

端口名在模块图标中不可见，但您可以在模块对话框的 **描述**选项卡中点击 **Source code** 链接，在底层源文件中看到此名称。

### **I2** — 输入物理信号，untyped physical signal

第二个输入物理信号，将从第一个输入物理信号中减去。在模块图标中，此端口标有减号 (**-**)。

端口名在模块图标中不可见，但您可以在模块对话框的 **描述**选项卡中点击 **Source code** 链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名在模块图标中不可见，但您可以在模块对话框的 **描述**选项卡中点击 **Source code** 链接，在底层源文件中看到此名称。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不带单位传播的旧模块，请使用 Upgrade Advisor 将您的模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

计算两个输入物理信号的简单减法

PS Subtract 模块从一个物理信号输入中减去另一个物理信号输入，并输出差值：

O=I1−I2

其中

|  |  |
| --- | --- |
| *I*1 | 第一个输入端口处的物理信号（标有加号） |
| *I*2 | 第二个输入端口处的物理信号（标有减号） |
| *O* | 输出端口处的物理信号 |

两个输入端口处的物理信号必须具有相容单位。输出端口处的单位由单位传播规则确定。有关详细信息，请参阅 Physical Signal Unit Propagation。
