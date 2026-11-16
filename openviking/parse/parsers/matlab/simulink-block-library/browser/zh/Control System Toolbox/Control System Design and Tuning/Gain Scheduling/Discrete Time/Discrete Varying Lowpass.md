---
type: simulink-block
title: 'Discrete Varying Lowpass'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / LPV and LTV Models / Discrete-Time Varying Systems'
documentation_page: 'discretevaryinglowpass'
documentation_source_path: 'ref/discretevaryinglowpass.html'
language: zh-CN
chinese_source: official
---

# Discrete Varying Lowpass

## 端口

### 输入

### **u** — 滤波器输入 标量

低通滤波器输入信号。

### **freq** — 截止频率 标量

截止频率的连续时间值，以弧度/秒为单位指定。
### 输出

### **y** — 滤波器输出 标量

低通滤波器输出信号。

## 参数

### **滤波器阶数** — 低通滤波器阶数 1 (默认) | 正整数

低通滤波器阶数，指定为正整数。

### **预修正频率 w0 (弧度/秒)** — 预修正频率 0 (默认) | 正标量

预修正频率，指定为正标量。当截止频率接近奈奎斯特频率时，对连续时间巴特沃斯滤波器进行离散化可能会使截止频率发生偏移。为确保模拟和数字滤波器在特定频率 `w0` 附近具有匹配的频率响应，请将此参数设置为 `w0`。默认值 `w0 = 0` 对应于无预修正的双线性（突斯汀）变换：

s=2Ts(z−1z+1),

其中 *Ts* 是模块采样时间，由**采样时间 Ts** 参数指定。

### **采样时间 Ts** — 采样时间 1 (默认) | 正标量

模块采样时间，指定为正标量。此模块不支持继承的采样时间，因为它需要使用指定的采样时间来计算巴特沃斯滤波器的离散化。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2017b 中推出**

## 描述

具有可变系数的离散巴特沃斯滤波器

此模块实现连续时间 N 阶巴特沃斯滤波器的突斯汀离散化。结果为一个具有单位 DC 增益和可变截止频率的数字滤波器，您可将其作为输入提供给此模块。

使用此模块和线性参数变化库中的其他模块来实现具有变量参数或系数的常见控制元素。有关详细信息，请参阅Model Gain-Scheduled Control Systems in Simulink。

**小心**

避免使截止频率依赖于模块输出 **y**。如果存在这种依赖，则生成的滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。这种代数环容易带来不稳定性和发散性。
