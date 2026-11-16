---
type: simulink-block
title: 'Design Mel Filter Bank'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'designmelfilterbankblock'
documentation_source_path: 'ref/designmelfilterbankblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Design Mel Filter Bank

## 端口

### 输出

### **fb** — 滤波器组列向量 | 矩阵

Mel 滤波器组，以 *M*×*N* 矩阵形式返回，其中：

- *M* 是频带数，由 **Auto-determine number of bands** 和 **Number of bands** 参数确定。
- *N* 是频谱中的点数。如果选择 **Design one-sided filter bank**，则 *N* 等于 `ceil(NFFT/2)`，其中 `NFFT` 是 **FFT length**。如果未选择 **Design one-sided filter bank**，则 *N* 等于 **FFT length**。

在选择 **Output center frequencies** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **fvec** — 中心频率行向量

带通滤波器的中心频率，以 Hz 为单位，返回为行向量，其元素数等于频带数。

#### 依赖关系

要启用此端口，请选择 **Output center frequencies** 参数。

**数据类型：** `single` | `double`

## 参数

### **FFT length** — 用于计算 DFT 的点数 `1024` (默认值) | 正整数

用于计算 DFT 的点数，指定为正整数。

### **Design one-sided filter bank** — 设计单边或双边滤波器组 `on` (默认值) | `off`

当选择此参数时，模块设计单边滤波器组。否则，滤波器组为双边。

### **Number of bands** — 带通滤波器数 `32` (默认值) | 正整数

带通滤波器数，指定为正整数。

### **Auto-determine frequency range** — 自动确定频率范围 `on` (默认值) | `off`

当选择此参数时，模块将 **Frequency range** 设置为 `[0,fs/2]`，其中 `fs` 使用 **Sample rate (Hz)** 指定。

### **Frequency range (Hz)** — 设计滤波器组的频率范围 `[0,22050]` (默认值) | 二元素行向量

用于设计滤波器组的频率范围，以 Hz 为单位，指定为二元素行向量。

#### 依赖关系

要启用此参数，请清除 **Auto-determine frequency range** 参数。

### **Filter bank design domain** — 设计滤波器组的域 `linear` (默认值) | `warped`

模块用于设计滤波器组的域，指定为 `linear` 或 `warped`。将滤波器组设计域设置为 `linear`，以在线性 (Hz) 域中设计带通滤波器。将滤波器组设计域设置为 `warped`，以在 warped (mel) 域中设计带通滤波器。

### **Filter bank normalization** — 滤波器组归一化技术 `bandwidth` (默认值) | `area` | `none`

用于滤波器组权重的归一化技术，指定为 `bandwidth`、`area` 或 `none`。

- `bandwidth` —— 按滤波器的对应带宽归一化每个带通滤波器的权重。
- `area` —— 按带通滤波器的对应面积归一化每个带通滤波器的权重。
- `none` —— 模块不归一化滤波器的权重。

### **Mel style** — Mel 样式 `oshaughnessy` (默认值) | `slaney`

mel 尺度的样式，指定为 `oshaughnessy` 或 `slaney`。

### **Output data type** — 输出数据类型 `double` (默认值) | `single`

输出的数据类型，指定为 `double` 或 `single`。

### **Sample rate (Hz)** — 采样率 `44.1e3` (默认值) | 正标量

滤波器设计的采样率，以 Hz 为单位，指定为正标量。

### **Visualize filter bank** — 打开绘图以可视化滤波器组的按钮

打开绘图以在频域中可视化滤波器。

### **Output center frequencies** — 为中心频率指定额外输出端口 `off` (默认值) | `on`

当选择此参数时，模块显示一个额外输出端口 **fvec**。此端口输出带通滤波器的中心频率。

## 所属库

Audio Toolbox / Features

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022a 中引入**

### R2023b: 支持 Slaney 样式的 mel 尺度

将 **Mel style** 参数设置为 `slaney` 以使用 Slaney 样式的 mel 尺度。

## 描述

设计频域 mel 滤波器组

Design Mel Filter Bank 模块使用 mel 频率尺度输出频域听觉滤波器组。您可以使用 mel 滤波器组将音频信号分解为 mel 频率尺度上的独立频带，这模拟了人类对声音的非线性感知。
