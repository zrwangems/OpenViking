---
type: simulink-block
title: 'Sinusoidal Measurement (PLL, Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sinusoidalmeasurementpllthreephase'
documentation_source_path: 'ref/sinusoidalmeasurementpllthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinusoidal Measurement (PLL, Three-Phase)

## 端口

### 输入

### **abc** — 输入信号向量

三相输入信号。

**数据类型：** `single` | `double`
### 输出

### **freq** — 频率，Hz 标量

输入信号的估计频率，以 Hz 为单位。

**数据类型：** `single` | `double`

### **angle** — 相位角，rad 标量

输入信号第一相的估计相位角，以 rad 为单位。

**数据类型：** `single` | `double`

### **mag** — 幅值，无量纲标量

输入信号的幅值。

**数据类型：** `single` | `double`

## 参数

### **Enable moving average filter on input** — 用于启用频率相关移动平均滤波器的选项 `On`（默认）| `Off`

*自 R2025a 起*

用于对输入信号启用频率相关移动平均滤波器的选项。选择此参数时，模块会滤除来自负序和零序的噪声。

### **Enable input normalization** — 用于启用输入归一化的选项 `Off`（默认）| `On`

*自 R2025a 起*

用于启用输入归一化的选项。

### **Loop filter proportional gain** — LF 比例增益 `1`（默认）| 正标量

环路滤波器的比例增益。增大此值可提高相位角中稳态误差被消除的速率。此值还决定 PLL 在跟踪并锁定到相位角时的响应强度。

### **Loop filter integral gain** — LF 积分增益 `10`（默认）| 正标量

环路滤波器的积分增益。此参数决定 PLL 在跟踪并锁定到相位时的响应强度。增大此值可减小并消除相位角中的稳态误差。

### **Initial frequency (Hz)** — 输入频率的初始估计值 `60 Hz`（默认）| 标量

输入频率的初始估计值。

### **Initial phase angle (rad)** — 相位角的初始估计值 `0 rad`（默认）| 标量或向量

相位角的初始估计值。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩膜子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：启用频率相关移动平均滤波器和输入归一化

现在，您可以使用 **Enable moving average filter on input** 参数启用或禁用输入信号上的频率相关移动平均滤波器。

您还可以使用 **Enable input normalization** 参数启用或禁用输入信号的归一化。

## 描述

使用锁相环估计三相正弦特性

Sinusoidal Measurement (PLL, Three-Phase) 模块估计平衡三相正弦信号的频率特性。该模块使用标准锁相环 (PLL) 策略来估计输入信号的频率和相位角。它还会输出输入信号的幅值。

当需要频率、相位角或幅值且无法直接测量时，可在控制应用中使用此模块。要估计非三相或不平衡正弦信号的频率特性，请改用 Sinusoidal Measurement (PLL) 模块。

### 方程

锁相环生成一个近似输入信号 *u(t)* 的正弦波，其形式为：

y(t)=A(t)sin(ϕ0+∫2πf(t)dt),

其中：

- *y* 是输入信号的估计值。
- *A* 是输入信号的幅值。
- *ϕ0* 是输入信号的初始相位角。

由于假设输入信号是平衡的，模块直接根据三相的瞬时幅值计算幅值。估计的相位角 *ϕ* 是此生成正弦波的相位角：

ϕ(t)=ϕ0+∫2πf(t)dt,

其中 *f* 是正弦波的频率，*ϕ0* 是初始相位角。

此图显示了锁相环的整体结构。

图中：

- 鉴相器产生一个相对于输入正弦波 *u* 与合成正弦波 *y* 之间相位差 *eϕ* 的误差信号。它还输出幅值 *A*。
- 环路滤波器通过滤除相位差的高频分量来提供输入角频率 *ω* 的估计值。模块还输出以 Hz 为单位的转换后频率 *f*。
- 压控振荡器对角速度进行积分以产生相位估计值 *ϕ*，并将其发送到 Phase Detector 进行比较。
