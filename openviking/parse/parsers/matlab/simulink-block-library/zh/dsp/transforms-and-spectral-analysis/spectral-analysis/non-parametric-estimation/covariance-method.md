---
type: simulink-block
title: 'Covariance Method'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Spectral Analysis / Non-Parametric Estimation'
documentation_page: 'covariancemethod'
documentation_source_path: 'ref/covariancemethod.html'
language: zh-CN
chinese_source: worker-translation
---

# Covariance Method

## 端口

### 输入

### **Input** — 输入列向量 | 未定向向量

将输入指定为列向量或未定向向量。此输入表示来自单通道信号的一帧连续时间样本。

**数据类型：** `single` | `double`
### 输出

### **Output** — 功率谱密度估计列向量

在 *Nfft* 个等间隔频率点处信号的功率谱密度估计，以列向量形式返回。频率点位于 [0,*Fs*) 范围内，其中 *Fs* 是信号的采样率。

**数据类型：** `single` | `double`

## 参数

### **Estimation order** — AR 模型的阶数 `6` (默认) | 正整数

将 AR 模型（全极点模型）的估计阶数指定为正整数。该模块根据估计的 AR 模型参数的 FFT 计算频谱。为保证输出非奇异，**Estimation order** 参数的值必须小于或等于输入向量长度的一半。

### **Inherit FFT length from estimation order** — 从估计阶数继承 FFT 长度 `off` (默认) | `on`

当您选择 **Inherit FFT length from estimation order** 参数时，FFT 长度 *Nfft* 比估计阶数大一。要指定执行 FFT 的点数，请清除 **Inherit FFT length from estimation order** 参数。然后，您可以使用 **FFT length** 参数指定 2 的幂的 FFT 长度。该模块在计算 FFT 之前将输入补零或环绕到 *Nfft*。

### **FFT length** — FFT 长度 `256` (默认) | 大于或等于 2 的正整数

输入用于执行 FFT 的数据点数 *Nfft*，其为大于或等于 2 的正整数。当 *Nfft* 大于输入帧大小时，该模块根据需要将每一帧补零。当 *Nfft* 小于输入帧大小时，该模块根据需要环绕每一帧。

#### 依赖关系

要启用此参数，请清除 **Inherit FFT length from input dimensions** 参数。

### **Inherit sample time from input** — 从输入继承采样时间 `on` (默认) | `off`

当您选择 **Inherit sample time from input** 参数时，该模块根据输入信号的采样周期计算频率数据。为使该模块产生有效输出，必须满足以下条件：

- 模块的输入是原始信号，其中没有添加或删除样本（例如，通过插入零）。
- 仿真中时域信号的采样周期等于原始时间序列的采样周期。

如果这些条件不成立，请清除 **Inherit sample time from input** 参数。然后，您可以使用 **Sample time of original time series** 参数指定采样时间。

### **Sample time of original time series** — 原始时域信号的采样时间 `1` (默认) | 正标量

将原始时域信号的采样时间指定为正标量。

#### 依赖关系

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

使用协方差方法进行功率谱密度估计

Covariance Method 模块使用协方差方法估计输入的功率谱密度 (PSD)。此方法通过最小化最小二乘意义下的前向预测误差，将自回归 (AR) 模型拟合到信号。

该模块根据估计的 AR 模型参数的 FFT 计算频谱。
