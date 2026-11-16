---
type: simulink-block
title: 'PWM Timing and Waveform Generator (Three-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmtimingandwaveformgeneratorthreephasetwolevel'
documentation_source_path: 'ref/pwmtimingandwaveformgeneratorthreephasetwolevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Timing and Waveform Generator (Three-phase, Two-level)

## 端口

### 输入

### **Vabc** — 三相正弦参考信号向量

希望所连接的变换器输出的正弦电压，指定为包含三个元素的向量，每个相位一个元素。

### **vdc** — 直流母线电压信号标量

变换器直流母线电压的正实数，指定为标量。

### 输出

### **TgabcON** — 开通门极时间向量

开通门极时间，以包含三个元素的向量形式返回，每个相位一个元素。

### **TgabcOFF** — 关断门极时间向量

关断门极时间，以包含三个元素的向量形式返回，每个相位一个元素。

### **ModWave** — 调制波向量

调制波，以包含三个元素的向量形式返回，每个相位一个元素。

## 参数

### **PWM mode** — 脉宽调制方法 `Continuous PWM (CPWM)`（默认） | `Discontinuous PWM (DPWM)`

脉宽调制方法。`Discontinuous PWM (DPWM)` 在每个基波周期内将波形钳位到直流母线总共 120 度。`Continuous PWM (CPWM)` 则不会。

### **Continuous PWM** — 连续脉宽调制方法 `SVM: space vector modulation`（默认） | `SPWM: sinusoidal PWM`

连续脉宽调制方法。

#### 依赖关系

要启用此参数，请将 **PWM mode** 设置为 `Continuous PWM (CPWM)`。

### **Discontinuous PWM (DPWM)** — 钳位方法 `60 DPWM: 60 degree discontinuous PWM`（默认） | ...

不连续脉宽调制方法。指定用于分配每周期 120 度的方法，在此期间模块将调制波钳位到直流母线。选项包括：

- `60 DPWM: 60 degree discontinuous
  PWM`
- `60 DPWM (+30 degree shift): +30 degree shift from
  60 DPWM`
- `60 DPWM (-30 degree shift): -30 degree shift from
  60 DPWM`
- `30 DPWM: 30 degree discontinuous
  PWM`
- `120 DPWM: positive dc
  component`
- `120 DPWM: negative dc
  component`

当波形被钳位时，调制中断。

#### 依赖关系

要启用此参数，请将 **PWM mode** 设置为 `Discontinuous PWM (DPWM)`。

### **Sampling mode** — 波采样方法 `Natural`（默认） | `Asymmetric` | `Symmetric`

波采样方法。采样模式决定模块是在波相交时对调制波形采样，还是在载波处于其一个或两个边界条件时采样。

### **Switching frequency (Hz)** — 开关速率 `1e3`（默认） | 正标量

功率变换器中开关进行开关切换的速率。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

生成三相两电平门极时间信息

PWM Timing and Waveform Generator (Three-phase, Two-level) 模块控制三相两电平功率变换器的开关行为。该模块基于以下模块输入计算开通门极和关断门极时间以及调制波：

- 三个正弦参考电压
- 一个直流母线电压

该模块可与平均值变换器一起使用，以加速仿真。

### 连续和不连续 PWM

该模块提供连续和不连续脉宽调制 (PWM) 的模式。该图展示了连续正弦脉宽调制 (SPWM) 与连续空间矢量调制 (SVM) 波形之间的一般区别。

对于不连续脉宽调制 (DPWM)，模块在每个基波周期内将调制波钳位到正或负直流母线总共 120 度。在钳位区间内，调制中断。

采用 30 度 DPWM 的波形在每个基波周期内有四个 30 度区间。

选择正或负 30 度相移会影响 60 度 DPWM 的钳位区间。

该图展示了 120 度 DPWM 的正直流钳位和负直流钳位的波形。

### 采样模式

该模块允许您选择调制波的自然、对称或不对称采样。

PWM Timing and Waveform Generator (Three-phase, Two-level) 模块不执行基于载波的 PWM。相反，该模块使用输入信号来计算门极时间。

不过，基于载波的 PWM 有助于展示您所选的采样模式如何与模块生成脉冲的开通和关断行为相关。使用两电平、基于载波 PWM 方法的生成器：

1. 对参考波采样
2. 将采样值与三角载波进行比较
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为确定开通和关断脉冲行为，两电平基于载波的 PWM 生成器使用以下方法对三角波采样：

- Natural — 采样和比较发生在调制波与载波的交点处。
- Asymmetric — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- Symmetric — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。
