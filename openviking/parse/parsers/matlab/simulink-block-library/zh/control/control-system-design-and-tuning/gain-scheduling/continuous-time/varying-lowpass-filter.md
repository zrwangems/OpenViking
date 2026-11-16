---
type: simulink-block
title: 'Varying Lowpass Filter'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Continuous Time'
documentation_page: 'varyinglowpassfilter'
documentation_source_path: '../control/ref/varyinglowpassfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Lowpass Filter

## 端口

### 输入

### **u** — 滤波器输入标量

低通滤波器输入信号。

### **freq** — 截止频率标量

滤波器截止频率，以 rad/s 为单位指定。

### 输出

### **y** — 滤波器输出标量

低通滤波器输出信号。

## 参数

### **Filter order** — 低通滤波器阶数 1（默认）| 正整数

低通滤波器阶数，指定为正整数。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有可变系数的 Butterworth 滤波器

该模块实现一个模拟 N 阶 Butterworth 滤波器，该滤波器具有单位 DC 增益以及您作为模块输入提供的可变截止频率。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元素。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使截止频率依赖于模块输出 **y**。如果有这种依赖关系，则所得滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易出现不稳定和发散。
