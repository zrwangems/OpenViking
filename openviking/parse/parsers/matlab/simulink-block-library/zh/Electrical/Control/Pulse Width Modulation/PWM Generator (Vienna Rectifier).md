---
type: simulink-block
title: 'PWM Generator (Vienna Rectifier)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorviennarectifier'
documentation_source_path: 'ref/pwmgeneratorviennarectifier.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Generator (Vienna Rectifier)

## 端口

### 输入

### **Vabc** — 三相正弦参考信号向量

三个正弦电压，每相一个。

### **Iabc** — 三相电流参考信号向量

三个电流，每相一个。

### **vdc** — 直流母线电压信号正标量

变换器的直流母线电压。信号值必须大于 0。

### **vneutral** — 直流母线中性点平衡控制标量

平衡直流电源的反馈控制环路的输出。信号值必须介于 `–1` 和 `+1` 之间。
### 输出

### **g** — 门极控制向量

三个脉冲波形，用于确定所连接功率变换器中的开关行为。

## 参数

### **Sampling mode** — 波形采样方法 `Natural` (default) | `Asymmetric` | `Symmetric`

采样模式，用于确定模块是在波形相交时还是在载波处于其一个或两个边界条件时对调制波形进行采样。

### **Switching frequency (Hz)** — 开关速率 `1e3` `Hz` (default) | 正数

功率变换器中开关切换的速率，以 Hz 为单位。

### **Sample time (s)** — 模块采样时间 `5e-5` `s` (default) | 正数

连续模块执行之间的时间间隔，以 s 为单位。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于 `1/(50*Fsw)`，其中 *F*sw 是 **Switching frequency (Hz)**。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

Vienna 整流器脉宽调制波形生成器

PWM Generator (Vienna Rectifier) 模块：

1. 根据模块输入计算开通门控和关断门控时间：

   - 三个正弦参考电压，每相一个，必须在 Vienna 整流器的交流侧生成，每相一个
   - 三个 Vienna 整流器的滤波输入正弦电流测量值，每相一个
   - 一个直流母线电压
   - 一个直流母线中性点平衡控制信号
2. 使用门控时间生成三个控制开关的脉冲。

该模块使用基于两电平和三电平变换器等效性的简化空间矢量调制方法生成控制脉冲 [1]。

三相滤波输入电流用于识别有效电压矢量六边形。通过将三电平逆变器的空间矢量图简化为两电平逆变器的空间矢量图，确定开关序列选择以及开通门控和关断门控时间 [2]。

来自外部直流母线中性点控制环路的直流母线中性点平衡控制信号用于调整单个开关周期内冗余电压矢量的时间分布。

### 采样模式

该模块允许您选择调制波的 natural、symmetric 或 asymmetric 采样。

PWM Generator (Vienna Rectifier) 模块不执行基于载波的脉宽调制 (PWM)。相反，该模块使用输入信号计算门控时间，并使用门控时间生成控制开关的脉冲。

有关采样模式的详细信息，请参阅 PWM Generator (Three-phase, Two-level)。
