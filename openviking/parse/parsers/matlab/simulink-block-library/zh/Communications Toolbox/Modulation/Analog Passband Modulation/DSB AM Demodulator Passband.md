---
type: simulink-block
title: 'DSB AM Demodulator Passband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'dsbamdemodulatorpassband'
documentation_source_path: 'ref/dsbamdemodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# DSB AM Demodulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。输入是已调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 解调输出信号标量

解调输出信号，以标量形式返回。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的
**准备** 库中，选择 **属性检查器**。

### **输入信号偏移** — 输入信号偏移因子 `1` (默认) | 标量

输入信号偏移因子，*k*，指定为标量。此值
应大于或等于输入信号最小值的绝对值。将此参数设置为对应 DSB AM
Modulator Passband 模块中的输入信号偏移值。

### **载波频率 (Hz)** — 载波频率，以 Hz 为单位 `300` (默认) | 正标量

载波频率，以 Hz 为单位，指定为正标量。将载波
频率 *f*c 与对应的 DSB AM
Modulator Passband 模块匹配。

通常，合适的载波频率远高于
输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 ×
*f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带仿真与通带仿真。

### **初始相位 (rad)** — 载波的初始相位偏移，以弧度为单位 `0` (默认) | 标量

载波的初始相位偏移，以弧度为单位，指定为标量。

### **低通滤波器设计方法** — 低通滤波器的设计方法 `Butterworth` (默认) | `Chebyshev type I` | `Chebyshev type II` | `Elliptic`

低通滤波器的设计方法，指定为
`Butterworth`、`Chebyshev type I`、`Chebyshev type II` 或 `Elliptic`。

### **滤波器阶数** — 低通滤波器的阶数 `4` (默认) | 正标量

低通滤波器的阶数，指定为 [1, 500] 范围内的正标量。
此参数值定义由 **低通滤波器设计方法** 参数指定的滤波器阶数。

### **截止频率** — 截止频率，以 Hz 为单位 `300` (默认) | 正标量

截止频率，以 Hz 为单位，指定为正标量。此参数值定义
由 **低通滤波器设计方法** 参数指定的滤波器截止频率。

### **通带波纹 (dB)** — 峰间通带波纹，以 dB 为单位 `0.1` (默认) | 正标量

峰间通带波纹，以 dB 为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **低通滤波器设计方法** 设置为 `Chebyshev type I` 或
`Elliptic`。

### **阻带波纹 (dB)** — 峰间阻带波纹，以 dB 为单位 `0.1` (默认) | 正标量

峰间阻带波纹，以 dB 为单位，指定为正标量。

#### 依赖关系

要启用此参数，请将 **低通滤波器设计方法** 设置为 `Chebyshev type II` 或
`Elliptic`。

## 所属库

Communications Toolbox / Modulation / Analog Passband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 DSB-AM 调制数据

DSB AM Demodulator Passband 模块对使用
双边带幅度调制进行调制的信号进行解调。该模块使用包络检测方法。输入
是已调制信号的通带表示。输入和输出信号均为
实标量信号。
