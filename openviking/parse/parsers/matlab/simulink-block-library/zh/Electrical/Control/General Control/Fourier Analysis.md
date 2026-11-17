---
type: simulink-block
title: 'Fourier Analysis'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'fourieranalysis'
documentation_source_path: 'ref/fourieranalysis.html'
language: zh-CN
chinese_source: worker-translation
---

# Fourier Analysis

## 端口

### 输入

### **u** — 傅里叶分析输入 scalar | vector

要分析的输入信号。输入可以是单个信号或多个多路复用信号。输入信号可以是电气系统中的交流电流或电压。

**数据类型：** `single` | `double`
### 输出

### **Magnitude** — 信号幅值 scalar | vector

对应于谐波次数的信号幅值。

**数据类型：** `single` | `double`

### **Angle** — 信号角度 scalar | vector

对应于谐波次数的信号角度。

**数据类型：** `single` | `double`

## 参数

### **Fundamental frequency (Hz)** — 信号基频 `60`（默认值） | positive scalar | vector with positive values

信号的基频，单位为 Hz。如果使用向量指定基频，则它必须与输入向量维度匹配。

### **Harmonic numbers** — 信号谐波次数 `[1 2]`（默认值） | vector with elements ≥ `0`

指定信号谐波次数。向量元素必须大于或等于 0。

### **Initial magnitude** — 信号初始幅值 `1`（默认值） | vector with elements ≥ `0`

指定信号的初始幅值。向量元素必须大于或等于 0。

### **Initial phase (rad)** — 信号初始相位 `0`（默认值） | vector

信号的初始相位角，单位为 rad。

### **Buffer size** — 缓冲区大小 `8192`（默认值） | scalar

缓冲区的大小。

#### 依赖项

要启用此参数，请将 **Sample time (-1 for inherited)** 设置为 `0`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值） | `0` | positive scalar

连续两次模块执行之间的时间。在执行期间，模块生成输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散或连续时间傅里叶分析

Fourier Analysis 模块对输入信号执行离散或连续时间傅里叶分析。

### 方程

周期函数 *x(t)* 可以分解为无限个正弦和余弦函数之和，如下所示：

x(t)=a02+∑n=1∞[ancos(nt)+bnsin(nt)]

其中：

- *a0* 是 DC 分量。
- *an* 和 *bn* 是常数傅里叶系数。
- *n* 是谐波次数。

系数 *an* 和 *bn* 定义为：

an=2T0∫t0t0+T0x(t)cos(nΩ0t)dt, n=0,1,...

bn=2T0∫t0t0+T0x(t)sin(nΩ0t)dt, n = 1,2, ...

Ω0=2πT0

T0=1f

其中 *f* 是基频。

这些方程定义了对应于谐波次数的幅值和角度：

|Xn|=an2+bn2

θn=−tan−1[anbn]

**注意**

如果将此模块用于连续时间操作，并将 **Sample time (-1 for inherited)** 参数设置为 `0`，则还应指定 **Buffer size** 参数的值，以确保其覆盖移动时间窗口。
