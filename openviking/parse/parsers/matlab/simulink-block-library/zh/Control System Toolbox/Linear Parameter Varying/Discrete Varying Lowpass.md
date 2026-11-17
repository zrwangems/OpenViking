---
type: simulink-block
title: 'Discrete Varying Lowpass'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryinglowpass'
documentation_source_path: 'ref/discretevaryinglowpass.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Lowpass

## 端口

### 输入

### **u** — 滤波器输入标量

低通滤波器输入信号。

### **freq** — 截止频率标量

截止频率的连续时间值，以 rad/s 为单位指定。

### 输出

### **y** — 滤波器输出标量

低通滤波器输出信号。

## 参数

### **Filter order** — 低通滤波器阶数 1（默认）| 正整数

低通滤波器阶数，指定为正整数。

### **Pre-warping frequency w0 (rad/s)** — 预畸变频率 0（默认）| 正标量

预畸变频率，指定为正标量。当截止频率接近奈奎斯特频率时，连续时间巴特沃斯滤波器的离散化可能会使截止频率发生偏移。为确保模拟滤波器和数字滤波器在特定频率 `w0` 附近具有匹配的频率响应，请将此参数设置为 `w0`。默认值 `w0 = 0` 对应于不带预畸变的双线性（Tustin）变换：

s=2Ts(z−1z+1),

其中 *Ts* 是模块采样时间，由 **Sample time Ts** 参数指定。

### **Sample time Ts** — 采样时间 1（默认）| 正标量

模块采样时间，指定为正标量。此模块不支持继承采样时间，因为它需要指定的采样时间来计算巴特沃斯滤波器的离散化。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有可变系数的离散巴特沃斯滤波器

该模块实现连续时间 N 阶巴特沃斯滤波器的 Tustin 离散化。结果是一个具有单位直流增益和可变截止频率的数字滤波器，截止频率作为模块的输入提供。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使截止频率依赖于模块输出 **y**。如果存在这种依赖关系，则所得滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易产生不稳定和发散。
