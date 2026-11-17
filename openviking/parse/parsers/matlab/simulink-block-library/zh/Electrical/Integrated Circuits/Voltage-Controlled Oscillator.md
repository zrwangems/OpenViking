---
type: simulink-block
title: 'Voltage-Controlled Oscillator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'voltagecontrolledoscillator'
documentation_source_path: 'ref/voltagecontrolledoscillator.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage-Controlled Oscillator

## 端口
```yaml
ports:
- name: 1+
  summary: 正输入电压电气
  direction: unspecified
- name: 1-
  summary: 负输入电压电气
  direction: unspecified
- name: 2+
  summary: 正输出电压电气
  direction: unspecified
- name: 2-
  summary: 负输出电压电气
  direction: unspecified
```

### 守恒

### **1+** — 正输入电压电气

与振荡器正输入电压关联的电气守恒端口。

### **1-** — 负输入电压电气

与振荡器负输入电压关联的电气守恒端口。

### **2+** — 正输出电压电气

与振荡器正输出电压关联的电气守恒端口。

### **2-** — 负输出电压电气

与振荡器负输出电压关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Frequency dependence on input voltage
  summary: 模块参数化 Linear（默认）| Tabulated
  group: 频率
- name: Nominal frequency
  summary: 标称频率 1000 Hz（默认）
  group: 频率
- name: Input voltage corresponding to nominal frequency
  summary: 对应于标称频率的输入电压 0.5 V（默认）
  group: 频率
- name: Rate of change of frequency with input voltage
  summary: 频率随输入电压的变化率 1 Hz/V（默认）
  group: 频率
- name: Minimum input voltage
  summary: 最小输入电压 0 V（默认）
  group: 频率
- name: Maximum input voltage
  summary: 最大输入电压 1 V（默认）
  group: 频率
- name: Input voltage vector
  summary: 输入电压向量 [0, .2, .4, .6, .8, 1] V（默认）
  group: 频率
- name: Frequency deviation from nominal
  summary: 相对于标称值的频率偏差 [-1000, -329, -51, 162, 342, 500] Hz（默认）
  group: 频率
- name: Output voltage peak amplitude
  summary: 输出电压峰值幅度 1 V（默认）
  group: 电气特性
- name: Input resistance
  summary: 输入电阻 inf Ohm（默认）
  group: 电气特性
- name: Output resistance
  summary: 输出电阻 0 Ohm（默认）
  group: 电气特性
- name: Dynamics
  summary: 动态特性指定 No dynamics（默认）| Model frequency tracking dynamics
  group: 动态特性
- name: Frequency tracking time constant
  summary: 频率跟踪时间常数 1e-3 s（默认）
  group: 动态特性
- name: Initial frequency
  summary: 初始频率 1000 Hz（默认）
  group: 动态特性
```

### 频率

### **Frequency dependence on input voltage** — 模块参数化 `Linear`（默认）| `Tabulated`

选择以下方法之一进行模块参数化：

- `Linear` — 通过指定频率随输入电压的变化率来定义线性函数。这是默认选项。
- `Tabulated` — 提供输入电压向量以及对应的输出频率相对于标称值的偏差。模块根据这些值通过查表确定频率偏差。

### **Nominal frequency** — 标称频率 `1000` `Hz`（默认）

当输入控制电压为标称值时的振荡器频率。

### **Input voltage corresponding to nominal frequency** — 对应于标称频率的输入电压 `0.5` `V`（默认）

对应于振荡器标称频率的输入电压。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Linear` 时，此参数可见。

### **Rate of change of frequency with input voltage** — 频率随输入电压的变化率 `1` `Hz/V`（默认）

定义频率随输入电压变化率的线性系数。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Linear` 时，此参数可见。

### **Minimum input voltage** — 最小输入电压 `0` `V`（默认）

影响 VCO 频率的最小输入电压。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Linear` 时，此参数可见。

### **Maximum input voltage** — 最大输入电压 `1` `V`（默认）

影响 VCO 频率的最大输入电压。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Linear` 时，此参数可见。

### **Input voltage vector** — 输入电压向量 `[0, .2, .4, .6, .8, 1]` `V`（默认）

用于表格化 VCO 频率的电压向量。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Tabulated` 时，此参数可见。

### **Frequency deviation from nominal** — 相对于标称值的频率偏差 `[-1000, -329, -51, 162, 342, 500]` `Hz`（默认）

相对于标称频率的对应 VCO 频率向量。

#### 依赖关系

仅当为 **Frequency dependence on input voltage** 参数选择 `Tabulated` 时，此参数可见。

### 电气特性

### **Output voltage peak amplitude** — 输出电压峰值幅度 `1` `V`（默认）

2+ 和 2– 端子之间电压的峰值幅度。

### **Input resistance** — 输入电阻 `inf` `Ohm`（默认）

1+ 和 1– 端子处的电阻。

### **Output resistance** — 输出电阻 `0` `Ohm`（默认）

串联输出电阻的值。

### 动态特性

### **Dynamics** — 动态特性指定 `No dynamics`（默认）| `Model frequency tracking dynamics`

选择以下方法之一来指定动态特性：

- `No dynamics` — 不对输入控制电压变化与振荡器频率之间的时间延迟进行建模。这是默认选项。
- `Model frequency tracking dynamics` — 对输入控制电压与振荡器频率之间的一阶动态特性进行建模。

### **Frequency tracking time constant** — 频率跟踪时间常数 `1e-3` `s`（默认）

用于延迟所测量的输入控制电压的一阶滤波器的时间常数，以对 VCO 所需频率变化与所产生的 VCO 频率之间的滞后进行建模。

#### 依赖关系

仅当为 **Dynamics** 参数选择 `Model frequency tracking dynamics` 时，此参数可见。

### **Initial frequency** — 初始频率 `1000` `Hz`（默认）

初始 VCO 输出频率。
## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

压控振荡器的行为模型

Voltage-Controlled Oscillator 模块提供压控振荡器（VCO）的行为模型。输出电压由以下方程定义：

vlim={vminfor vin<vminvinfor vmin≤vin≤vmaxvmaxfor vin>vmax

Φ˙=2πF(vlim)

vout=Asin(2πfnomt+Φ)−ioutRout

其中：

- *v*in 是施加在 1+ 和 1– 端口上的电压。
- *v*out 是 2+ 和 2– 端口上的电压。
- *f*nom 是当输入控制电压为 *v*nom 时的振荡器频率。
- *F* 是 *v*lim 的线性函数或 *v*lim 的查找表函数。
- *A* 是输出电压峰值幅度。
- *t* 是仿真时间。
- *i*out 是输出电流。
- *R*out 是输出电阻。

如果为 **Frequency dependence on input voltage** 参数选择 `Linear`，则函数 *F* 由下式给出：

F=fnom+k(vlim−vnom)

其中 *k* 是频率随输入电压的变化率。

如果为 **Frequency dependence on input voltage** 参数选择 `Tabulated`，则函数 *F* 由您提供的输入电压向量以及对应的输出频率相对于标称值的偏差定义。*v*min 和 *v*max 的值分别是输入电压向量的第一个值和最后一个值。

您可以对输入控制电压变化与振荡器频率之间的时间延迟进行建模。为此，对 *v*lim 与传递给函数 *F* 的值之间的一阶动态特性进行建模。
