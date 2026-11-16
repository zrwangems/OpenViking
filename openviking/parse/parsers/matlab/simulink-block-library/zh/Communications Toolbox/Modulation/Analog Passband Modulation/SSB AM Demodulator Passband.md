---
type: simulink-block
title: 'SSB AM Demodulator Passband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Passband Modulation'
documentation_page: 'ssbamdemodulatorpassband'
documentation_source_path: 'ref/ssbamdemodulatorpassband.html'
language: zh-CN
chinese_source: worker-translation
---

# SSB AM Demodulator Passband

## 端口

### 输入

### **In** — 输入信号标量

输入信号，指定为标量。输入是已调制信号的通带表示。

此端口在模块上未命名。

**数据类型：** `double`
### 输出

### **Out** — 解调后的输出信号标量

解调后的输出信号，以标量形式返回。

此端口在模块上未命名。

**数据类型：** `double`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的 **仿真** 选项卡中，在 **准备** 库中，选择 **属性检查器**。

### **载波频率 (Hz)** — 载波频率，单位为 Hz `300`（默认）| 正标量

载波频率，单位为 Hz，指定为正标量。将载波频率 *f*c 与相应的 SSB AM Modulator Passband 模块匹配。

通常，合适的载波频率远高于输入信号的最高频率。根据 Nyquist 采样定理，1 / *T*s > (2 × *f*c)，其中 *T*s 表示输入信号的采样时间。有关详细信息，请参阅基带仿真与通带仿真。

### **初始相位 (rad)** — 初始相位偏移，单位为弧度 `0`（默认）| 标量

已调制信号的初始相位偏移，以弧度为单位，指定为标量。

### **低通滤波器设计方法** — 低通滤波器的设计方法 `Butterworth`（默认）| `Chebyshev type I` | `Chebyshev type II` | `Elliptic`

低通滤波器的设计方法，指定为 `Butterworth`、`Chebyshev type I`、`Chebyshev type II` 或 `Elliptic`。

### **滤波器阶数** — 低通滤波器的阶数 `4`（默认）| 正标量

低通滤波器的阶数，指定为范围 [1, 500] 内的正标量。此参数值定义由 **低通滤波器设计方法** 参数指定的滤波器阶数。

### **截止频率** — 截止频率，单位为 Hz `300`（默认）| 正标量

截止频率，单位为 Hz，指定为正标量。此参数值定义由 **低通滤波器设计方法** 参数指定的滤波器的截止频率。

### **通带纹波 (dB)** — 峰峰值通带纹波，单位为 dB `0.1`（默认）| 正标量

峰峰值通带纹波，单位为 dB，指定为正标量。

#### 依赖关系

要启用此参数，请将 **低通滤波器设计方法** 设置为 `Chebyshev type I` 或 `Elliptic`。

### **阻带纹波 (dB)** — 峰峰值阻带纹波，单位为 dB `0.1`（默认）| 正标量

峰峰值阻带纹波，单位为 dB，指定为正标量。

#### 依赖关系

要启用此参数，请将 **低通滤波器设计方法** 设置为 `Chebyshev type II` 或 `Elliptic`。

## 所属库

Communications Toolbox / Modulation / Analog Passband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 SSB-AM 调制数据

SSB AM Demodulator Passband 模块解调使用单边带幅度调制进行调制的信号。输入和输出信号均为实标量信号。
