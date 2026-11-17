---
type: simulink-block
title: 'PS RMS Estimator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Periodic Operators'
documentation_page: 'psrmsestimator'
documentation_source_path: 'ref/psrmsestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# PS RMS Estimator

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

输入物理信号。该信号必须是周期性的。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters:
- name: Base frequency
  summary: 周期信号频率 60 Hz（默认值）
  group: ''
```

### **Base frequency** — 周期信号频率 `60 Hz`（默认值）

周期信号的基频。
## 所属库

Simscape / Foundation Library / Physical Signals / Periodic Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

测量周期信号的 RMS 值

PS RMS Estimator 模块测量周期信号的均方根（RMS）值。

如果信号在可测量的时间范围内完成一个模式（称为周期），并在后续相同的周期内重复该模式，则该信号是周期性的。信号基频是每秒的周期数。

该模块接受存在一个或多个交流分量的物理信号。它输出一个 RMS 值，其中每个频率分量在其时间周期内取平均。

输入和输出均为物理信号。无类型物理端口便于单位传播。输出信号具有与输入信号相同的物理单位。

为获得有意义的结果，请至少运行信号一个完整时间周期的仿真。
