---
type: simulink-block
title: 'PWM Gate Signal Generator (Five-phase, Two-level)'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgatesignalgeneratorfivephasetwolevel'
documentation_source_path: 'ref/pwmgatesignalgeneratorfivephasetwolevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Gate Signal Generator (Five-phase, Two-level)

## 端口

### 输入

### **TgabcdeON** — 开通门控时间向量

开通门控时间，指定为包含五个元素的向量，每个相位对应一个元素。

### **TgabcdeOFF** — 关断门控时间向量

关断门控时间，指定为包含五个元素的向量，每个相位对应一个元素。

### 输出

### **g** — 门极控制向量

确定所连接功率变换器中开关行为的十个脉冲波形，以向量形式返回。

## 参数

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

波形采样方法。采样模式决定模块是在波形相交时对调制波形进行采样，还是在载波处于其一个或两个边界条件时对调制波形进行采样。

### **Switching frequency (Hz)** — 开关速率 `1e3`（默认）| 正标量

功率变换器中的开关进行切换的速率，以 Hz 为单位。

### **Sample time (s)** — 模块采样时间 `5e-5`（默认）| 正标量

连续模块执行之间的时间间隔，以秒为单位。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于 `1/(50*Fsw)`，其中 *F*sw 是 **Switching frequency (Hz)** 参数的值。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

为五相、两电平门控开关器件生成十个用于控制开关的脉冲

PWM Gate Signal Generator (Five-phase, Two-level) 模块控制五相、两电平功率变换器的开关行为。该模块使用作为输入提供的门控时间生成十个用于控制开关的脉冲。您可以使用 PWM Timing and Waveform Generator (Five-phase, Two-level) 模块获取门控时间信息。

### 采样模式

此模块允许您选择调制波的自然采样、对称采样或非对称采样。

PWM Gate Signal Generator (Five-phase, Two-level) 模块不执行基于载波的脉宽调制 (PWM)。相反，该模块使用门控时间生成用于控制开关的脉冲以及模块输出的调制波形。

然而，基于载波的 PWM 有助于说明您选择的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用三电平、基于载波的 PWM 方法的生成器：

1. 对参考波进行采样
2. 将采样值与两个平行的三角载波进行比较，这两个载波相隔一个电平
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为确定开通和关断脉冲行为，三电平、基于载波的 PWM 生成器使用以下方法对每个三角波进行采样：

- Natural — 采样和比较发生在调制波与载波的交点处。
- Asymmetric — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- Symmetric — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。
