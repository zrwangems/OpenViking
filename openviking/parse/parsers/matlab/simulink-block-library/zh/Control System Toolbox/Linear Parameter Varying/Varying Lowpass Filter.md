---
type: simulink-block
title: 'Varying Lowpass Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyinglowpassfilter'
documentation_source_path: 'ref/varyinglowpassfilter.html'
language: zh-CN
chinese_source: official
---

# Varying Lowpass Filter

## 端口

### 输入

### **u** — 滤波器输入 标量

低通滤波器输入信号。

### **freq** — 截止频率 标量

滤波器截止频率，指定以弧度/秒为单位。
### 输出

### **y** — 滤波器输出 标量

低通滤波器输出信号。

## 参数

### **滤波器阶数** — 低通滤波器阶数 1 (默认) | 正整数

低通滤波器阶数，指定为正整数。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

具有可变系数的巴特沃斯滤波器

该模块实现一个模拟 N 阶巴特沃斯滤波器，该滤波器具有单位 DC 增益和可变截止频率，可作为模块的输入。

使用此模块和线性参数变化库中的其他模块来实现具有变量参数或系数的常见控制元素。有关详细信息，请参阅Model Gain-Scheduled Control Systems in Simulink。

**小心**

避免使截止频率依赖于模块输出 **y**。如果存在这种依赖，则生成的滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。这种代数环容易带来不稳定性和发散性。
