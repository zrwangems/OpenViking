---
type: simulink-block
title: 'PWM Gate Signal Generator (Three-phase, Three-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgatesignalgeneratorthreephasethreelevel'
documentation_source_path: 'ref/pwmgatesignalgeneratorthreephasethreelevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Gate Signal Generator (Three-phase, Three-level)

## 端口
```yaml
ports:
- name: TgabcON
  summary: 开通门极时间向量
  direction: input
- name: TgabcOFF
  summary: 关断门极时间向量
  direction: input
- name: SmallHexNum
  summary: 小六边形编号标量
  direction: input
- name: g
  summary: 门极控制向量
  direction: output
```

### 输入

### **TgabcON** — 开通门极时间向量

开通门极时间，指定为包含三个元素的向量，每个相位对应一个元素。

### **TgabcOFF** — 关断门极时间向量

关断门极时间，指定为包含三个元素的向量，每个相位对应一个元素。

### **SmallHexNum** — 小六边形编号标量

构成传统两电平逆变器空间矢量图的其中一个小六边形的编号，指定为 1 到 6 之间的标量。
有关详细信息，请参阅简化空间矢量 PWM 方法一节。
### 输出

### **g** — 门极控制向量

用于确定所连接功率变换器中开关行为的十二个脉冲波形，以向量形式返回。
## 参数
```yaml
parameters:
- name: Sampling mode
  summary: 波形采样方法 Natural（默认）| Asymmetric | Symmetric
  group: ''
- name: Switching frequency (Hz)
  summary: 开关频率 1e3（默认）| 正标量
  group: ''
- name: Sample time (s)
  summary: 模块采样时间 5e-5（默认）| 正标量
  group: ''
```

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

波形采样方法。采样模式决定了模块是在波形相交时采样调制波形，还是在载波处于一个或两个边界条件时采样调制波形。

### **Switching frequency (Hz)** — 开关频率 `1e3`（默认）| 正标量

功率变换器中开关的切换速率。

### **Sample time (s)** — 模块采样时间 `5e-5`（默认）| 正标量

连续模块执行之间的时间间隔。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于
`1/(50*Fsw)`，
其中 *F*sw 为
**Switching frequency (Hz)**。
## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

为三相三电平门极开关器件生成十二个开关控制脉冲

PWM Gate Signal Generator (Three-phase, Three-level) 模块控制三相三电平功率变换器的开关行为。该模块使用作为输入提供的门极时间生成十二个开关控制脉冲。您可以使用 PWM Timing and Waveform Generator (Three-phase, Three-level) 模块获取门极时间信息。

### 简化空间矢量 PWM 方法

为了确定开关序列和电压矢量的持续时间，PWM Gate Signal Generator (Three-phase, Three-level) 模块在三电平逆变器的空间矢量图上使用简化空间矢量脉宽调制（SVPWM）方法 [2]。

下图显示了构成三电平逆变器空间矢量图的六个小六边形：

这六个小六边形中的每一个都代表一个两电平逆变器的空间矢量图，这些图以内小六边形的六个顶点为中心，如下图所示：

要简化为两电平逆变器的空间矢量图，您必须通过在 **SmallHexNum** 端口指定一个值来选择其中一个小六边形。然后，该模块通过从原始参考电压矢量中减去所选六边形的中心电压矢量，将三电平空间矢量平面变换为两电平空间矢量平面。

### 采样模式

该模块允许您选择调制波的自然采样、对称采样或非对称采样。

PWM Gate Signal Generator (Three-phase, Three-level) 模块不执行基于载波的脉宽调制。相反，该模块使用门极时间生成开关控制脉冲以及模块输出的调制波形。

然而，基于载波的 PWM 有助于展示您选择的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用三电平基于载波 PWM 方法的发生器：

1. 采样参考波
2. 将采样值与两个平行的三角载波进行比较，两者相隔一个电平
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲

为了确定开通和关断脉冲行为，三电平基于载波的 PWM 发生器使用以下方法对每个三角波进行采样：

- Natural — 采样和比较发生在调制波与载波的交点处。
- Asymmetric — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- Symmetric — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。
