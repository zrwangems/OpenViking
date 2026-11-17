---
type: simulink-block
title: 'PS Dead Zone'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Nonlinear Operators'
documentation_page: 'psdeadzone'
documentation_source_path: 'ref/psdeadzone.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Dead Zone

## 端口
```yaml
ports:
- name: I
  summary: 输入物理信号，无类型物理信号
  direction: input
- name: O
  summary: 输出物理信号，无类型物理信号
  direction: output
```

### 输入

### **I** — 输入物理信号，无类型物理信号

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters:
- name: Upper limit
  summary: 死区上限 0.5 1（默认值）
  group: ''
- name: Lower limit
  summary: 死区下限 -0.5 1（默认值）
  group: ''
- name: Enable zero-crossing detection
  summary: 是否启用过零检测 on（默认值） | off
  group: ''
```

### **Upper limit** — 死区上限 `0.5 1`（默认值）

死区的上限，即终点。

参数单位必须与输入信号的单位一致。您可以从下拉列表中选择单位，或输入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Lower limit** — 死区下限 `-0.5 1`（默认值）

死区的下限，即起点。

参数单位必须与输入信号的单位一致。您可以从下拉列表中选择单位，或输入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Enable zero-crossing detection** — 是否启用过零检测 `on`（默认值） | `off`

清除此选项以禁用过零检测并提高仿真速度。有关更多信息，请参阅 Managing Zero Crossings in Simscape Models。
## 所属库

Simscape / Foundation Library / Physical Signals / Nonlinear Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **Enable zero-crossing detection** 复选框。清除此复选框可以禁用过零检测并提高仿真速度。

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关更多信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

为物理信号提供零输出区域

当输入信号落在指定区域（称为死区）内时，PS Dead Zone 模块生成零输出。您可以将死区的下限和上限指定为模块参数。模块输出取决于输入和死区：

- 如果输入在死区内（大于下限且小于上限），则输出为零。
- 如果输入大于或等于上限，则输出为输入减去上限。
- 如果输入小于或等于下限，则输出为输入减去下限。

输入和输出均为物理信号。无类型物理端口便于单位传播。输出信号具有与输入信号相同的物理单位。
