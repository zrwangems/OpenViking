---
type: simulink-block
title: 'Switch'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'switch'
documentation_source_path: '../simscape/ref/switch.html'
language: zh-CN
chinese_source: worker-translation
---

# Switch

## 端口
```yaml
ports:
- name: PS
  summary: 控制信号，无量纲物理信号
  direction: input
- name: p
  summary: 电气端子 electrical
  direction: input
- name: n
  summary: 电气端子 electrical
  direction: input
```

### 输入

### **PS** — 控制信号，无量纲物理信号

控制开关断开或闭合的输入物理信号。
### 守恒

### **p** — 电气端子 electrical

与其中一个开关端子关联的电气守恒端口。该模块没有固有的方向性。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### **n** — 电气端子 electrical

与另一个开关端子关联的电气守恒端口。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters:
- name: Closed resistance R_closed
  summary: 闭合开关的电阻 0.01 Ohm（默认值）| 正标量
  group: ''
- name: Open conductance G_open
  summary: 断开开关的电导 1e-8 1/Ohm（默认值）| 正标量
  group: ''
- name: Threshold
  summary: 断开和闭合开关的阈值 0.5（默认值）| 无量纲标量
  group: ''
```

### **Closed resistance R\_closed** — 闭合开关的电阻 `0.01 Ohm`（默认值）| 正标量

开关闭合时的电阻。参数值必须大于零。

### **Open conductance G\_open** — 断开开关的电导 `1e-8 1/Ohm`（默认值）| 正标量

开关断开时的电导。参数值必须大于零。

### **Threshold** — 断开和闭合开关的阈值 `0.5`（默认值）| 无量纲标量

断开和闭合开关的阈值。如果端口 **PS** 处的外部物理信号大于此值，则开关闭合，否则开关断开。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

由外部物理信号控制的开关

Switch 模块对由外部物理信号控制的开关进行建模。如果端口 **PS** 处的外部物理信号大于 **Threshold** 参数中指定的值，则开关闭合，否则开关断开。

电气开关会为模型增加不连续性，因此求解器的选择会影响模型行为。有关求解器设置的详细信息，请参阅 Making Optimal Solver Choices for Physical Simulation。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
