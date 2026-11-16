---
type: simulink-block
title: 'PWM Timing and Waveform Generator (Five-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmtimingandwaveformgeneratorfivephasetwolevel'
documentation_source_path: 'ref/pwmtimingandwaveformgeneratorfivephasetwolevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Timing and Waveform Generator (Five-phase, Two-level)

## 端口

### 输入

### **Vabcde** — 五相正弦参考信号向量

希望所连接变换器输出的正弦电压，指定为包含五个元素的向量，每个相位一个元素。

### **vdc** — 直流母线电压信号标量

变换器直流母线电压的正实数，指定为标量。
### 输出

### **TgabcdeON** — 开通门极时间向量

开通门极时间，返回为包含五个元素的向量，每个相位一个元素。

### **TgabcdeOFF** — 关断门极时间向量

关断门极时间，返回为包含五个元素的向量，每个相位一个元素。

### **ModWave** — 调制波向量

调制波，返回为包含五个元素的向量，每个相位一个元素。

## 参数

### **连续 PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认） | `SVM: space vector modulation`

连续脉宽调制方法。

### **采样模式** — 波形采样方法 `Natural`（默认） | `Asymmetric` | `Symmetric`

波形采样方法。采样模式确定模块是在波形相交时采样调制波形，还是在载波处于其一个或两个边界条件时采样调制波形。

### **开关频率 (Hz)** — 开关速率 `1e3`（默认） | 正标量

功率变换器中开关进行开关的速率，以 Hz 为单位。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

生成五相、两电平门极时间信息

PWM Timing and Waveform Generator (Five-phase, Two-level) 模块控制五相、两电平功率变换器的开关行为。该模块根据以下模块输入计算开通门极时间、关断门极时间和调制波：

- 五个正弦参考电压
- 一个直流母线电压

该模块可与平均值变换器一起使用，以加速仿真。

### 连续 PWM

该模块仅提供连续脉宽调制（PWM）。该图显示了连续正弦脉宽调制（SPWM）与连续空间矢量调制（SVM）波形之间的一般差异。

### 采样模式

该模块允许您选择调制波的 natural、symmetric 或 asymmetric 采样。

PWM Timing and Waveform Generator (Five-phase, Two-level) 模块不执行基于载波的 PWM。相反，该模块使用输入信号计算门极时间。

然而，基于载波的 PWM 有助于说明您选择的采样模式如何与模块生成脉冲的开通和关断行为相关。使用两电平、基于载波 PWM 方法的生成器：

1. 采样参考波
2. 将采样值与三角载波进行比较
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为了确定开通和关断脉冲行为，两电平基于载波的 PWM 生成器使用以下方法对三角波进行采样：

- Natural — 采样和比较在调制波与载波的交点处进行。
- Asymmetric — 采样在载波的上边界和下边界处进行。比较在采样之后的交点处进行。
- Symmetric — 采样仅在载波的上边界处进行。比较在采样之后的交点处进行。
