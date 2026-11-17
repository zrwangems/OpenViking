---
type: simulink-block
title: 'Discrete Varying Notch'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingnotch'
documentation_source_path: 'ref/discretevaryingnotch.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Notch

## 端口

### 输入

### **u** — 滤波器输入 标量

陷波滤波器输入信号

### **freq** — 陷波频率 标量

陷波频率的连续时间值，以 rad/s 为单位指定。

### **gmin** — 陷波频率处的增益 标量

陷波频率处增益的连续时间值，以绝对单位表示。该值控制陷波深度。陷波滤波器在低频和高频处具有单位增益。增益在陷波频率处最低。

### **damp** — 滤波器极点阻尼比 标量

阻尼比的连续时间值，指定为正标量值。阻尼比控制陷波宽度；越接近 0，陷波越陡峭。

### 输出

### **y** — 滤波器输出 标量

陷波滤波器输出信号。

## 参数

### **Pre-warping frequency w0 (rad/s)** — 预畸变频率 0（默认）| 正标量

预畸变频率，指定为正标量。当陷波频率接近奈奎斯特频率时，连续时间陷波滤波器传递函数的离散化可能会使陷波频率发生偏移。为确保连续和离散滤波器在特定频率 `w0` 附近具有匹配的频率响应，请将此参数设置为 `w0`。默认值 `w0 = 0` 对应于无预畸变的双线性（Tustin）变换：

s=2Ts(z−1z+1),

其中 *Ts* 是模块采样时间，通过 **Sample time Ts** 参数指定。

### **Sample time Ts** — 采样时间 1（默认）| 正标量

模块采样时间，指定为正标量。此模块不支持继承采样时间，因为它需要指定的采样时间来计算陷波滤波器的离散化。

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

具有可变系数的离散时间陷波滤波器

该模块实现具有可变系数的连续时间陷波滤波器的 Tustin 离散化。将陷波频率、最小增益和阻尼比的连续时间值分别馈送到 **freq**、**gmin** 和 **damp** 输入端口。这些参数控制连续时间陷波频率的陷波深度和频率，如下图所示。阻尼比 **damp** 控制陷波宽度 *Δ*；较大的 **damp** 意味着较大的 *Δ*。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使滤波器系数依赖于模块输出 **y**。如果您有这种依赖关系，则所得滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。此代数环容易产生不稳定和发散。
