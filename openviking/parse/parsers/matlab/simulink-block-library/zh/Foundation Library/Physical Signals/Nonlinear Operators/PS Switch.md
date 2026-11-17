---
type: simulink-block
title: 'PS Switch'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psswitch'
documentation_source_path: 'ref/psswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Switch

## 端口

### 输入

### **I1** — 输入物理信号，无类型物理信号

第一个输入物理信号。如果端口 **I2** 处的控制信号值大于或等于 **Threshold** 参数值，则输出此信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

### **I2** — 控制物理信号，无类型物理信号

第二个输入物理信号。这是开关的控制信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

### **I3** — 输入物理信号，无类型物理信号

第三个输入物理信号。如果端口 **I2** 处的控制信号值小于 **Threshold** 参数值，则输出此信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

## 参数

### **Threshold** — 打开和关闭开关的阈值 `0.5 1`（默认值）

用于打开和关闭开关的阈值。如果第二个（中间）输入端口 **I2** 处提供的控制物理信号大于或等于此值，则输出连接到第一个输入。否则，输出连接到第三个输入。

参数单位必须与端口 **I2** 处控制信号的单位一致。您可以从下拉列表中选择单位，或键入所需的单位名称或表达式。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Enable zero-crossing detection** — 是否启用过零检测 `on`（默认值） | `off`

清除此选项以禁用过零检测并提高仿真速度。有关更多信息，请参阅 Managing Zero Crossings in Simscape Models。

## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **Enable zero-crossing detection** 复选框。清除此复选框可以禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关更多信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

由外部物理信号控制的单刀双掷开关

PS Switch 模块将第二个（中间）输入端口处的物理信号值与阈值进行比较：

- 如果控制输入值大于或等于阈值，则输出连接到第一个输入。这是模块图标中显示的默认连接。
- 如果控制输入值小于阈值，则输出连接到第三个输入。

第二个（中间）输入端口是控制端口，它从不连接到输出。

所有输入和输出均为物理信号。无类型物理端口便于单位传播。第一个和第三个输入端口处的物理信号必须具有一致的单位。输出端口处的单位由单位传播规则确定。有关详细信息，请参阅 Physical Signal Unit Propagation。
