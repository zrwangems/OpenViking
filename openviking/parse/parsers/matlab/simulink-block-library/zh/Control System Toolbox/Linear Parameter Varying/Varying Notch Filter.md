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
chinese_source: worker-translation
---

# Varying Notch Filter

## 端口

### 输入

### **u** — 滤波器输入 标量

陷波滤波器输入信号

### **freq** — 陷波频率 标量

陷波频率的值，以 rad/s 为单位指定。

### **gmin** — 陷波频率处的增益 标量

陷波频率处的增益值，以绝对单位表示。该值控制陷波深度。陷波滤波器在低频和高频处具有单位增益。增益在陷波频率处最低，即 **freq** 端口处的值。

### **damp** — 滤波器极点阻尼比 标量

阻尼比的值，指定为正标量值。阻尼比控制陷波宽度；越接近 0，陷波越陡峭。

### 输出

### **y** — 滤波器输出 标量

陷波滤波器输出信号。

## 参数

R2025b 中未记录。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有可变系数的陷波滤波器

该模块实现具有可变系数的连续时间陷波滤波器。滤波器的瞬时传递函数由下式给出：

N(s)=s2+2\*gmin\*damp\*freq\*s+freq2s2+2\*damp\*freq\*s+freq2，

其中 *gmin*、*damp* 和 *freq* 是在对应输入端口提供的值。这些参数控制陷波深度和频率，如下图所示。阻尼比 *damp* 控制陷波宽度 *Δ*；*damp* 越大意味着 *Δ* 越大。

使用此模块以及 Linear Parameter Varying 库中的其他模块，可以实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使滤波器系数依赖于模块输出 **y**。如果存在这种依赖关系，则产生的滤波器会导致代数环，因为计算模块输出值需要知道模块输出值。这种代数环容易导致不稳定和发散。
