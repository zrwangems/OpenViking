---
type: simulink-block
title: 'Sinusoidal Measurement (PLL)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sinusoidalmeasurementpll'
documentation_source_path: 'ref/sinusoidalmeasurementpll.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Measurement (PLL)

## 端口

### 输入

### **u** — 输入信号 标量或向量

周期性输入信号。

**数据类型：** `single` | `double`
### 输出

### **freq** — 频率 标量或向量

输入信号的估计频率，单位为 Hz。

**数据类型：** `single` | `double`

### **angle** — 相位角 标量或向量

输入信号的估计相位角，单位为 rad。

**数据类型：** `single` | `double`

### **mag** — 幅值 标量或向量

输入信号的估计幅值。

**数据类型：** `single` | `double`

## 参数

### **Phase detector integral gain** — PD 积分增益 `1000`（默认）| 正标量或向量

相位检测器的积分增益。这决定了 PLL 在跟踪和锁定幅值时的激进程度。

如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Loop filter proportional gain** — LF 比例增益 `400`（默认）| 正标量或向量

环路滤波器的比例增益。这决定了 PLL 在跟踪和锁定相位角时的激进程度。增大此值可改善跟踪对相位角阶跃变化的反应时间。

如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Loop filter integral gain** — LF 积分增益 `20000`（默认）| 正标量或向量

环路滤波器的积分增益。增大此值可提高相位角稳态误差的消除速率。此值还决定了 PLL 在跟踪和锁定相位时的激进程度。

如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Initial frequency (Hz)** — 初始频率 `60 Hz`（默认）| 标量或向量

输入频率的初始估计值。如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Initial phase angle (rad)** — 初始相位 `0 rad`（默认）| 标量或向量

相位角的初始估计值。如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Initial magnitude** — 初始幅值 `1`（默认）| 标量或向量

幅值的初始估计值。如果输入信号是向量，请使用标量参数或使用与输入信号大小相同的向量参数。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

使用锁相环估计正弦特性

Sinusoidal Measurement (PLL) 模块估计单相正弦信号或多相正弦信号各相的频率、相位角和幅值。该模块使用增强型锁相环 (PLL) 策略来估计输入信号的这些正弦特性。

当需要频率、相位角或幅值且无法直接测量时，可在控制应用中使用此模块。要为平衡三相输入信号提供更快的相位锁定，请使用 Three-Phase Sinusoidal Measurement (PLL) 模块。

### 方程

锁相环生成一个近似输入信号 *u(t)* 的正弦波，其形式为：

y(t)=A(t)sin(ϕ0+∫2πf(t)dt),

其中：

- *y* 是输入信号的估计值。
- *A* 是输入信号幅值的估计值。
- *ϕ0* 是输入信号的初始相位角。

估计的相位角 *ϕ* 是此生成正弦波的角度：

ϕ(t)=ϕ0+∫2πf(t)dt,

其中 *f* 是正弦波的频率，*ϕ0* 是初始相位角。

此图显示了锁相环的整体结构。

在图中：

- 相位检测器产生一个相对于输入正弦波 *u* 与合成正弦波 *y* 之间相位差 *eϕ* 的误差信号。它还输出幅值 *A* 的估计值。
- 环路滤波器通过滤除相位差的高频分量来提供输入角频率 *ω* 的估计值。该模块还输出转换后的频率 *f*，单位为 Hz。
- 压控振荡器对角速度进行积分以产生相位估计值 *ϕ*。振荡器还生成归一化合成正弦波 *(1/A)y*，并将其发送到相位检测器进行比较。
