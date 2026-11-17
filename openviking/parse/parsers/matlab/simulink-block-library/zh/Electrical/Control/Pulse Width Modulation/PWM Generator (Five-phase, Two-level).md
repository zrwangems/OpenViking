---
type: simulink-block
title: 'PWM Generator (Five-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorfivephasetwolevel'
documentation_source_path: 'ref/pwmgeneratorfivephasetwolevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Generator (Five-phase, Two-level)

## 端口

### 输入

### **Vabcde** — 五相正弦参考信号向量

您希望所连接的变换器输出的正弦电压，指定为包含五个元素的向量，每个元素对应一相。

### **vdc** — 直流母线电压信号标量

变换器直流母线电压的正实数值，指定为标量。
### 输出

### **g** — 门极控制向量

决定所连接功率变换器中开关行为的十个脉冲波形，以向量形式返回。

### **ModWave** — 调制波向量

调制波，以包含五个元素的向量形式返回，每个元素对应一相。

## 参数

### **Continuous PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认）| `SVM: space vector modulation`

连续脉宽调制方法。

### **Sampling mode** — 波采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

波采样方法。采样模式决定了模块是在波形相交时采样调制波形，还是在载波处于一个或两个边界条件时采样调制波形。

### **Switching frequency (Hz)** — 开关频率 `1e3`（默认）| 正标量

功率变换器中开关的切换速率，单位为 Hz。

### **Sample time (s)** — 模块采样时间 `5e-5`（默认）| 正标量

连续模块执行之间的时间间隔，单位为秒。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于 `1/(50*Fsw)`，其中 *F*sw 为 **Switching frequency (Hz)** 参数的值。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

生成五相两电平脉宽调制波形

PWM Generator (Five-phase, Two-level) 模块控制五相两电平功率变换器的开关行为。该模块：

1. 根据模块输入计算开通门极时间和关断门极时间：

   - 五个正弦参考电压，每相一个
   - 一个直流母线电压
2. 使用门极时间生成十个控制开关的脉冲。
3. 使用门极时间生成调制波形。

### 连续 PWM

该模块仅提供连续脉宽调制（PWM）。图中显示了连续正弦脉宽调制（SPWM）与连续空间矢量调制（SVM）波形之间的一般区别。

### 采样模式

该模块允许您选择调制波的自然采样、对称采样或非对称采样。

PWM Generator (Five-phase, Two-level) 模块不执行基于载波的 PWM。相反，该模块使用输入信号计算门极时间，然后使用门极时间生成其输出的控制开关脉冲和调制波形。

然而，基于载波的 PWM 有助于说明您选择的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用两电平基于载波 PWM 方法的发生器：

1. 采样参考波。
2. 将采样值与三角载波进行比较。
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲。

为确定开通和关断脉冲行为，两电平基于载波的 PWM 发生器使用以下方法对三角波进行采样：

- Natural — 采样和比较发生在调制波与载波的交点处。
- Asymmetric — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- Symmetric — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。
