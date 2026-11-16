---
type: simulink-block
title: 'PS Min'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psmin'
documentation_source_path: 'ref/psmin.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Min

## 端口

### 输入

### **I1** — 输入物理信号，无类型物理信号

第一个输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### **I2** — 输入物理信号，无类型物理信号

第二个输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **启用过零检测** — 是否启用过零检测 `on`（默认） | `off`

清除此选项可禁用过零检测并提高仿真速度。有关详细信息，请参阅管理 Simscape 模型中的过零。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，模块包含 **启用过零检测** 复选框。清除此复选框可禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

输出两个输入物理信号的最小值

PS Min 模块输出其两个输入物理信号的最小值：

O=min(I1,I2)

其中

|  |  |
| --- | --- |
| *I*1 | 第一个输入端口处的物理信号 |
| *I*2 | 第二个输入端口处的物理信号 |
| *O* | 输出端口处的物理信号 |

两个输入端口处的物理信号必须具有一致的单位。输出端口处的单位由单位传播规则确定。有关详细信息，请参阅物理信号单位传播。
