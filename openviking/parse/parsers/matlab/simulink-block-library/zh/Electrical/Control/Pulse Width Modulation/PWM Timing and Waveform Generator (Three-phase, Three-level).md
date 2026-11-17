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
```yaml
ports:
- name: Vabc
  summary: 三相正弦参考信号向量
  direction: input
- name: vdc
  summary: 直流母线电压信号标量
  direction: input
- name: vneutral
  summary: 直流母线中性点平衡控制标量
  direction: input
- name: TgabcON
  summary: 开通门极时间向量
  direction: output
- name: TgabcOFF
  summary: 关断门极时间向量
  direction: output
- name: SmallHexNum
  summary: 小六边形编号标量
  direction: output
- name: ModWave
  summary: 调制波向量
  direction: output
```

### 输入

### **Vabc** — 三相正弦参考信号向量

希望所连接的变换器输出的正弦电压，指定为包含三个元素的向量，每个元素对应一相。

### **vdc** — 直流母线电压信号标量

变换器直流母线电压的正实数，指定为标量。

### **vneutral** — 直流母线中性点平衡控制标量

用于平衡直流电源的反馈控制环的输出，指定为介于 `–1` 和 `+1` 之间的实数。
### 输出

### **TgabcON** — 开通门极时间向量

开通门极时间，以包含三个元素的向量形式返回，每个元素对应一相。

### **TgabcOFF** — 关断门极时间向量

关断门极时间，以包含三个元素的向量形式返回，每个元素对应一相。

### **SmallHexNum** — 小六边形编号标量

构成传统两电平逆变器空间矢量图的小六边形编号，以介于 1 和 6 之间的标量形式返回。有关详细信息，请参阅 PWM Gate Signal Generator (Three-phase, Three-level) 模块中的 Simplified Space-Vector PWM Method 部分。

### **ModWave** — 调制波向量

调制波，以包含三个元素的向量形式返回，每个元素对应一相。
## 参数
```yaml
parameters:
- name: Continuous PWM
  summary: '连续脉宽调制方法 SPWM: sinusoidal PWM（默认）| SVM: space vector modulation'
  group: ''
- name: Sampling mode
  summary: 波形采样方法 Natural（默认）| Asymmetric | Symmetric
  group: ''
- name: Switching frequency (Hz)
  summary: 开关频率 1e3（默认）| 正标量
  group: ''
```

### **Continuous PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认）| `SVM: space vector modulation`

指定波形技术。

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

波形采样方法。采样模式决定了模块是在波形相交时采样调制波形，还是在载波处于其一个或两个边界条件时采样调制波形。

### **Switching frequency (Hz)** — 开关频率 `1e3`（默认）| 正标量

功率变换器中开关的切换速率。
## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

生成三相三电平门极时间信息

PWM Timing and Waveform Generator (Three-phase, Three-level) 模块控制三相三电平功率变换器的开关行为。该模块根据以下模块输入计算开通门极时间和关断门极时间以及调制波：

- 三个正弦参考电压
- 一个直流母线电压
- 一个直流母线中性点平衡控制信号

该模块可与平均变换器一起使用，以加速仿真。

### 采样模式

该模块允许您选择调制波的自然采样、对称采样或非对称采样。

PWM Timing and Waveform Generator (Three-phase, Three-level) 模块不执行基于载波的脉宽调制（PWM）。相反，该模块使用输入信号来计算门极时间。

然而，基于载波的 PWM 有助于说明您所选的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用三电平基于载波 PWM 方法的发生器：

1. 采样参考波
2. 将采样值与两个相隔一个电平的平行三角载波进行比较
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为确定开通和关断脉冲行为，三电平基于载波 PWM 发生器使用以下方法对每个三角波进行采样：

- Natural — 采样和比较在调制波与载波的交点处进行。
- Asymmetric — 采样在载波的上边界和下边界处进行。比较在采样之后的交点处进行。
- Symmetric — 采样仅在载波的上边界处进行。比较在采样之后的交点处进行。
