---
type: simulink-block
title: 'PWM Timing and Waveform Generator (Three-phase, Three-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmtimingandwaveformgeneratorthreephasethreelevel'
documentation_source_path: 'ref/pwmtimingandwaveformgeneratorthreephasethreelevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Timing and Waveform Generator (Three-phase, Three-level)

## 端口

### 输入

### **Vabc** — 三相正弦参考信号向量

希望所连接的变换器输出的正弦电压，指定为包含三个元素的向量，每相一个元素。

### **vdc** — 直流母线电压信号标量

变换器直流母线电压的正实数，指定为标量。

### **vneutral** — 直流母线中点平衡控制标量

来自平衡直流电源的反馈控制环路的输出，指定为介于 `–1` 和 `+1` 之间的实数。

### 输出

### **TgabcON** — 开通门极时间向量

开通门极时间，返回为包含三个元素的向量，每相一个元素。

### **TgabcOFF** — 关断门极时间向量

关断门极时间，返回为包含三个元素的向量，每相一个元素。

### **SmallHexNum** — 小六边形编号标量

构成传统两电平逆变器空间矢量图的小六边形编号，返回为介于 1 和 6 之间的标量。有关详细信息，请参阅 PWM Gate Signal Generator (Three-phase, Three-level) 模块中的 Simplified Space-Vector PWM Method 部分。

### **ModWave** — 调制波向量

调制波，返回为包含三个元素的向量，每相一个元素。

## 参数

### **Continuous PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认） | `SVM: space vector modulation`

指定波形技术。

### **Sampling mode** — 波采样方法 `Natural`（默认） | `Asymmetric` | `Symmetric`

波采样方法。采样模式决定模块是在波相交时对调制波形进行采样，还是在载波处于其一个或两个边界条件时进行采样。

### **Switching frequency (Hz)** — 开关速率 `1e3`（默认） | 正标量

功率变换器中的开关进行切换的速率。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

生成三相三电平门极时间信息

PWM Timing and Waveform Generator (Three-phase, Three-level) 模块控制三相三电平功率变换器的开关行为。该模块根据以下模块输入计算开通门极时间、关断门极时间和调制波：

- 三个正弦参考电压
- 一个直流母线电压
- 一个直流母线中点平衡控制信号

此模块可与平均变换器一起使用，以加快仿真速度。

### 采样模式

此模块允许您选择调制波的 Natural、Symmetric 或 Asymmetric 采样。

PWM Timing and Waveform Generator (Three-phase, Three-level) 模块不执行基于载波的脉宽调制（PWM）。相反，该模块使用输入信号来计算门极时间。

然而，基于载波的 PWM 有助于说明您选择的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用三电平、基于载波的 PWM 方法的发生器：

1. 对参考波进行采样
2. 将采样值与两个平行的三角载波进行比较，这两个载波相隔一个电平
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为了确定开通和关断脉冲行为，三电平基于载波的 PWM 发生器使用以下方法对每个三角波进行采样：

- Natural — 采样和比较在调制波与载波的交点处发生。
- Asymmetric — 采样在载波的上边界和下边界处发生。比较在采样之后的交点处发生。
- Symmetric — 采样仅在载波的上边界处发生。比较在采样之后的交点处发生。
