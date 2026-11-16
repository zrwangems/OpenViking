---
type: simulink-block
title: 'Fast Block LMS Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'fastblocklmsfilter'
documentation_source_path: 'ref/fastblocklmsfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Fast Block LMS Filter

## 端口

### 输入

### **Input** — 输入信号 标量 | 列向量

将您想要滤波的输入信号指定为标量或列向量。

输入信号和期望信号必须具有相同的大小、数据类型和复/实性。

输入帧长度（输入中的行数）必须是您在 **Block size** 参数中指定的值的整数倍。

**数据类型:** `single` | `double`
**复数支持:** 是

### **Desired** — 期望信号 标量 | 列向量

将您想要建模的信号指定为标量或列向量。LMS 滤波器调整其系数以最小化误差，并使输入信号尽可能接近地收敛到期望信号。

输入信号和期望信号必须具有相同的大小、数据类型和复/实性。

**数据类型:** `single` | `double`
**复数支持:** 是

### **Step-size** — 自适应步长 非负标量

将自适应步长指定为非负标量。步长输入的数据类型必须与输入信号和期望信号的数据类型匹配。

较小的步长可确保输出信号与期望信号之间具有较小的稳态误差。如果步长较小，滤波器的收敛速度会降低。要提高收敛速度，请增大步长。请注意，如果步长较大，滤波器可能变得不稳定。

#### 依赖关系

要启用此端口，请将 **Specify step size via** 设置为 `'Input port'`。

**数据类型:** `single` | `double`

### **Adapt** — 更新滤波器权重的选项 标量

如果输入为非零值，该模块会持续更新滤波器权重。如果此输入的值为零，滤波器权重保持其当前值。

#### 依赖关系

要启用此端口，请选择 **Adapt port** 参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Reset** — 复位信号 标量

将复位信号指定为标量信号。当您想要将滤波器权重的值复位为其初始值时，请使用 **Reset port** 参数。当在 **Reset** 端口检测到复位事件时，该模块会复位滤波器权重。复位信号速率必须与数据信号输入的速率相同。

要启用 **Reset** 端口，请从 **Reset port** 列表中选择以下选项之一：

- `Rising edge` — 当 **Reset** 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续

- `Falling edge` — 当 **Reset** 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续
- `Either edge` — 当 Reset 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作
- `Non-zero sample` — 在 **Reset** 输入不为零的每个采样时间触发复位操作

要禁用复位端口，请将 **Reset port** 设置为 `None`。

#### 依赖关系

要启用此端口，请将 **Reset port** 设置为除 `None` 以外的任意选项。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Output** — 滤波后的信号 标量 | 列向量

滤波后的信号，以标量或列向量形式返回。该模块调整其滤波器系数，使输入信号收敛以匹配期望信号。滤波器输出收敛后的信号。

**数据类型:** `single` | `double`
**复数支持:** 是

### **Error** — 输出信号与期望信号之间的差 标量 | 列向量

滤波后信号与期望信号之间的差，以标量或列向量形式返回。LMS 滤波器的目标是最小化该误差。该模块调整其系数以收敛到最优滤波器系数，从而产生与期望信号紧密匹配的输出信号。

**数据类型:** `single` | `double`
**复数支持:** 是

### **Wts** — 自适应滤波器权重 标量 | 列向量

LMS 滤波器的权重，以长度等于您在 **Filter length** 参数中指定的值的列向量形式返回。对于每次迭代，该模块从此端口输出当前更新后的滤波器权重。

滤波器权重的数据类型与滤波后信号的数据类型匹配。

#### 依赖关系

要启用此端口，请选择 **Output filter weights** 参数。

**数据类型:** `single` | `double`
**复数支持:** 是

## 参数

### **Filter length** — FIR 滤波器系数向量的长度 `32`（默认）| 正整数

将 FIR 滤波器系数向量的长度指定为正整数。滤波器长度与块长度之和必须是 2 的幂。

### **Block size** — 权重自适应前采集的样本数 `32`（默认）| 正整数

将模块更新滤波器权重之前要采集的输入信号样本数指定为正整数。输入帧长度（输入中的行数）必须是您在此参数中指定的值的整数倍。滤波器长度与块长度之和必须是 2 的幂。

### **Specify step size via** — 自适应步长的来源 `Dialog`（默认）| `Input port`

通过以下方式指定自适应步长：

- `Dialog` –– 使用 **Step size (mu)** 参数在模块对话框中指定步长。
- `Input port` –– 使用 **Step-size** 输入端口指定步长。

### **Step-size (mu)** — 步长 `0.008`（默认）| 非负整数

将自适应步长 *µ* 指定为非负整数。您可以使用输入端口 **Step-size** 指定步长，或在此参数中输入值。

较小的步长可确保输出信号与期望信号之间具有较小的稳态误差。如果步长较小，滤波器的收敛速度会降低。要提高收敛速度，请增大步长。请注意，如果步长较大，滤波器可能变得不稳定。

**可调:** 是

#### 依赖关系

要启用此参数，请将 **Specify step size via** 参数设置为 `Dialog`。

### **Leakage factor (0 to 1)** — 泄漏 LMS 算法中使用的泄漏因子 `1.0`（默认）| [0, 1] 范围内的标量

将下面所示的泄漏 LMS 算法中使用的泄漏因子指定为 [0, 1] 范围内的标量，0<1−μα≤1。

w(k)=(1−μα)w(k−1)−f(u(n),e(n),μ)

当该值小于 1 时，该模块实现泄漏 LMS 算法。默认值为 `1`，表示自适应算法中无泄漏。

**可调:** 是

### **Initial value of filter weights** — 滤波器权重的初始值 `0`（默认）| 标量 | 向量

将滤波器权重 w(0) 的初始值指定为标量或长度等于滤波器长度的向量。当您指定标量时，该模块使用该标量值创建滤波器权重向量。此向量的长度等于滤波器长度，并且其所有值都等于该标量值。

### **Adapt port** — 启用 Adapt 端口 `off`（默认）| `on`

选择此参数以启用 **Adapt** 输入端口。使用此端口可指定该模块必须更新其滤波器权重，还是将其保持当前水平。有关详细信息，请参阅 **Adapt** 输入端口的描述。

### **Reset port** — 启用 Reset 端口 `None`（默认）| `Rising Edge` | `Falling Edge` | `Either Edge` | `Non-zero sample`

选择此参数以启用 **Reset** 输入端口。有关每个复位选项的详细信息，请参阅 **Reset** 输入端口的描述。

### **Output filter weights** — 输出滤波器权重 `on`（默认）| `off`

选择此参数以从 **Wts** 端口输出滤波器权重。

## 所属库

DSP System Toolbox / Filtering / Adaptive Filters

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用最小均方 (LMS) 自适应算法计算输出、误差和权重

Fast Block LMS Filter 模块实现自适应最小均方 (LMS) 滤波器，其中滤波器权重的自适应针对每个数据样本块发生一次。该模块估计最小化输出信号 *y*(*n*) 与期望信号 *d*(*n*) 之间的误差 *e*(*n*) 所需的滤波器权重（也称为系数）。

Fast Block LMS Filter 模块使用 Block LMS Filter 方程来估计滤波器权重。有关详细信息，请参阅算法。Fast Block LMS Filter 模块使用 Frequency-Domain FIR Filter 模块中使用的 FFT 算法，在频域中实现滤波输出计算和权重更新函数所涉及的卷积运算。

有关自适应滤波器的详细信息，请参阅自适应滤波器概述与应用。
