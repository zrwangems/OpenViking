---
type: simulink-block
title: 'Yule-Walker Method'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'yulewalkermethod'
documentation_source_path: 'ref/yulewalkermethod.html'
language: zh-CN
chinese_source: worker-translation
---

# Yule-Walker Method

## 端口
```yaml
ports:
- name: Input
  summary: 输入列向量 | 非定向向量
  direction: input
  data_types: single | double
- name: Output
  summary: 功率谱密度估计列向量
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 输入列向量 | 非定向向量

将输入指定为列向量或非定向向量。此输入表示来自单通道信号的一帧连续时间采样。

**数据类型：** `single` | `double`
### 输出

### **Output** — 功率谱密度估计列向量

信号在 *Nfft* 个等间隔频率点处的功率谱密度估计，以列向量形式返回。频率点位于范围 [0,*Fs*) 内，其中 *Fs* 是信号的采样率。

模块输出始终为非奇异的。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Inherit estimation order from input dimensions
  summary: 从输入维度继承估计阶数 off（默认）| on
  group: ''
- name: Estimation order
  summary: AR 模型阶数 6（默认）| 非负整数
  group: ''
- name: Inherit FFT length from estimation order
  summary: 从估计阶数继承 FFT 长度 off（默认）| on
  group: ''
- name: FFT length
  summary: FFT 长度 256（默认）| 大于或等于 2 的正整数
  group: ''
- name: Inherit sample time from input
  summary: 从输入继承采样时间 on（默认）| off
  group: ''
- name: Sample time of original time series
  summary: 原始时域信号的采样时间 1（默认）| 正标量
  group: ''
```

### **Inherit estimation order from input dimensions** — 从输入维度继承估计阶数 `off`（默认）| `on`

当您选中 **Inherit estimation order from input dimensions** 参数时，模块将全极点模型阶数（估计阶数）设置为比输入帧长度小 1 的值。否则，由 **Estimation order** 参数值指定阶数。模块根据估计的 AR 模型参数的 FFT 计算频谱。

### **Estimation order** — AR 模型阶数 `6`（默认）| 非负整数

将 AR 模型的估计阶数指定为非负整数。为保证有效输出，**Estimation order** 参数必须小于或等于输入向量长度的 1/2。

#### 依赖

要启用此参数，请清除 **Inherit estimation order from input dimensions** 参数。

### **Inherit FFT length from estimation order** — 从估计阶数继承 FFT 长度 `off`（默认）| `on`

当您选中 **Inherit FFT length from estimation order** 参数时，FFT 长度 *Nfft* 比估计阶数大 1。要指定执行 FFT 的点数，请清除 **Inherit FFT length from estimation order** 参数。然后您可以使用 **FFT length** 参数将 FFT 长度指定为 2 的幂。模块在计算 FFT 之前对输入进行零填充或环绕至 *Nfft*。

### **FFT length** — FFT 长度 `256`（默认）| 大于或等于 2 的正整数

输入执行 FFT 的数据点数 *Nfft*，为大于或等于 2 的正整数。当 *Nfft* 大于输入帧长度时，模块根据需要为每帧进行零填充。当 *Nfft* 小于输入帧长度时，模块根据需要环绕每帧。

#### 依赖

要启用此参数，请清除 **Inherit FFT length from input dimensions** 参数。

### **Inherit sample time from input** — 从输入继承采样时间 `on`（默认）| `off`

当您选中 **Inherit sample time from input** 参数时，模块根据输入信号的采样周期计算频率数据。为使模块产生有效输出，必须满足以下条件：

- 模块的输入是原始信号，未添加或删除样本（例如通过插入零）。
- 仿真中时域信号的采样周期等于原始时间序列的采样周期。

如果这些条件不满足，请清除 **Inherit sample time from input** 复选框。然后您可以使用 **Sample time of original time series** 参数指定采样时间。

### **Sample time of original time series** — 原始时域信号的采样时间 `1`（默认）| 正标量

将原始时域信号的采样时间指定为正标量。

#### 依赖

要启用此参数，请清除 **Inherit sample time from input** 参数。
## 所属库

DSP System Toolbox / Estimation / Power Spectrum Estimation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Yule-Walker 方法估计功率谱密度

Yule-Walker Method 模块使用 Yule-Walker AR 方法估计输入的功率谱密度（PSD）。此方法也称为自相关方法，通过最小化最小二乘意义下的前向预测误差，将自回归（AR）模型拟合到加窗输入数据。此过程导出 Yule-Walker 方程，由 Levinson-Durbin 递推求解。

模块根据估计的 AR 模型参数的 FFT 计算频谱。
