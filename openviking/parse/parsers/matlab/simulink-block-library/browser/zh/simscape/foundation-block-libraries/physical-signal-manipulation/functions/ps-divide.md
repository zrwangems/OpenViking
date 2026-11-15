---
type: simulink-block
title: 'PS Divide'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Functions'
documentation_page: 'psdivide'
documentation_source_path: 'ref/psdivide.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Divide

## 端口

### 输入

### **I1** — 分子输入，无类型物理信号

第一个输入物理信号，表示分子。在模块图标中，此端口用 **x** 符号标记。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的 **描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

### **I2** — 分母输入，无类型物理信号

第二个输入物理信号，表示分母。在模块图标中，此端口用 **÷** 符号标记。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的 **描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的 **描述**选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧式模块，请使用 Upgrade Advisor 将您的模块升级到最新版本。有关详细信息，请参阅升级包含旧式物理信号模块的模型。

## 描述

计算两个输入物理信号的逐元素除法

PS Divide 模块将一个物理信号输入除以另一个物理信号输入，并输出商：

O=I1./I2

其中

|  |  |
| --- | --- |
| *I*1 | 第一个输入端口处的物理信号（用 **x** 符号标记） |
| *I*2 | 第二个输入端口处的物理信号（用 **÷** 符号标记） |
| *O* | 输出端口处的物理信号 |

输出端口处的信号单位由单位传播规则确定。有关详细信息，请参阅物理信号单位传播。
