---
type: simulink-block
title: 'Switch'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'switch'
documentation_source_path: 'ref/switch.html'
language: zh-CN
chinese_source: official
---

# Switch

## 端口

### 输入

### **PS** — 控制信号，无单位 物理信号

控制是断开还是闭合开关的输入物理信号。
### 守恒

### **p** — 电气端子 电气

与其中一个开关端子关联的电气守恒端口。该模块没有固有方向性。

端口名称在模块图标中不可见，但您可以在模块对话框的**描述**选项卡中点击**源代码**链接，在基础源文件中查看此名称。

### **n** — 电气端子 电气

与其他开关端子关联的电气守恒端口。

端口名称在模块图标中不可见，但您可以在模块对话框的**描述**选项卡中点击**源代码**链接，在基础源文件中查看此名称。

## 参数

### **闭合电阻 R\_closed** — 闭合开关的电阻 `0.01 Ohm` (默认) | 正标量

开关闭合时的电阻。该参数值必须大于零。

### **断开电导 G\_open** — 断开开关的电导 `1e-8 1/Ohm` (默认) | 正标量

断开开关时的电导。该参数值必须大于零。

### **阈值** — 断开和闭合开关的阈值 `0.5` (默认) | 无单位标量

断开和闭合开关的阈值。如果端口 **PS** 处的外部物理信号大于该值，则开关闭合，否则开关断开。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

由外部物理信号控制的开关

Switch 模块对由外部物理信号控制的开关进行建模。如果端口 **PS** 处的外部物理信号大于**阈值**参数中指定的值，则开关闭合，否则开关断开。

电气开关会给您的模型添加不连续性，因此选择的求解器可能会影响模型行为。有关求解器设置的详细信息，请参阅Making Optimal Solver Choices for Physical Simulation。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
