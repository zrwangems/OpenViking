---
type: simulink-block
title: 'PS Abs'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Nonlinear Operators'
documentation_page: 'psabs'
documentation_source_path: 'ref/psabs.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Abs

## 端口

### 输入

### **I** — 输入物理信号，untyped physical signal

输入物理信号。

端口名称在模块图标中不可见，但您可以单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中查看此名称。
### 输出

### **O** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以单击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中查看此名称。

## 参数

### **Enable zero-crossing detection** — 是否启用过零检测 `on`（默认）| `off`

清除此选项可禁用过零检测并提高仿真速度。有关详细信息，请参阅管理 Simscape 模型中的过零。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **Enable zero-crossing detection** 复选框。清除此复选框使您能够禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

输出输入物理信号的绝对值

PS Abs 模块返回输入物理信号的绝对值：

O=|I|

其中

|  |  |
| --- | --- |
| *I* | 输入端口处的物理信号 |
| *O* | 输出端口处的物理信号 |

Untyped physical ports 有助于单位传播。输出信号与输入信号具有相同的物理单位。
