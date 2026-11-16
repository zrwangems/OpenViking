---
type: simulink-block
title: 'Varying Notch Filter'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingnotchfilter'
documentation_source_path: 'ref/varyingnotchfilter.html'
language: zh-CN
chinese_source: official
---

# Varying Notch Filter

## 端口

### 输入

### **u** — 滤波器输入 标量

陷波滤波器输入信号

### **freq** — 陷波频率 标量

陷波频率的值，以弧度/秒为单位指定。

### **gmin** — 陷波频率下的增益 标量

陷波频率下的增益的值，以绝对单位表示。此值控制陷波深度。陷波滤波器在低频率和高频率下具有单位增益。在陷波频率（**freq** 端口处的值）下，增益最低。

### **damp** — 滤波器极点的阻尼比 标量

阻尼比的值，指定为正标量值。阻尼比控制陷波宽度；越接近 0，陷波越陡峭。
### 输出

### **y** — 滤波器输出 标量

陷波滤波器输出信号。

## 参数

R2025b 官方文档未提供。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

具有可变系数的陷波滤波器

此模块实现具有可变系数的连续时间陷波滤波器。滤波器的瞬时传递函数由以下公式给出：

N(s)=s2+2\*gmin\*damp\*freq\*s+freq2s2+2\*damp\*freq\*s+freq2,

其中 *gmin*、*damp* 和 *freq* 是在相应输入端口提供的值。这些参数控制陷波深度和频率，如下图所示。阻尼比 *damp* 控制陷波宽度 *Δ*；*damp* 越大，*Δ* 就越大。

使用此模块和线性参数变化库中的其他模块来实现具有变量参数或系数的常见控制元素。有关详细信息，请参阅Model Gain-Scheduled Control Systems in Simulink。

**小心**

避免使滤波器系数依赖于模块输出 **y**。如果存在这种依赖，则生成的滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。这种代数环容易带来不稳定性和发散性。
