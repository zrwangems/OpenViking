---
type: simulink-block
title: 'Block LMS Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'blocklmsfilter'
documentation_source_path: 'ref/blocklmsfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Block LMS Filter

## 端口
```yaml
ports:
- name: Input
  summary: 输入信号 标量 | 列向量
  direction: input
  data_types: single | double
- name: Desired
  summary: 期望信号 标量 | 列向量
  direction: input
  data_types: single | double
- name: Step size
  summary: 自适应步长 非负标量
  direction: input
  data_types: single | double
- name: Adapt
  summary: 更新滤波器权重的选项 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Reset
  summary: 复位信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Output
  summary: 滤波后的信号 标量 | 列向量
  direction: output
  data_types: single | double
- name: Error
  summary: 输出与期望信号之间的差值 标量 | 列向量
  direction: output
  data_types: single | double
- name: Wts
  summary: 自适应滤波器权重 标量 | 列向量
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 输入信号 标量 | 列向量

指定要滤波的输入信号，为标量或列向量。

输入信号和期望信号必须具有相同的大小、数据类型和复/实性。

输入帧长度（输入中的行数）必须是 **Block size** 参数中指定值的整数倍。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Desired** — 期望信号 标量 | 列向量

指定要建模的信号，为标量或列向量。LMS 滤波器自适应其系数以最小化误差，并使输入信号尽可能接近期望信号。

输入信号和期望信号必须具有相同的大小、数据类型和复/实性。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Step size** — 自适应步长 非负标量

指定自适应步长，为非负标量。步长输入的数据类型必须与输入信号和期望信号的数据类型匹配。

较小的步长可确保输出信号与期望信号之间具有较小的稳态误差。如果步长较小，滤波器的收敛速度会降低。要提高收敛速度，请增大步长。请注意，如果步长过大，滤波器可能变得不稳定。

#### 依赖关系

要启用此端口，请将 **Specify step size via** 设置为 `'Input port'`。

**数据类型：** `single` | `double`

### **Adapt** — 更新滤波器权重的选项 标量

如果输入为非零值，模块会持续更新滤波器权重。如果此输入的值为零，滤波器权重保持其当前值。

#### 依赖关系

要启用此端口，请选中 **Adapt port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Reset** — 复位信号 标量

指定复位信号，为标量信号。当您想将滤波器权重的值复位为其初始值时，请使用 **Reset port** 参数。每当在 **Reset** 端口检测到复位事件时，模块会复位滤波器权重。复位信号速率必须与数据信号输入的速率相同。

要启用 **Reset** 端口，请从 **Reset port** 列表中选择以下选项之一：

- `Rising edge` — 当 **Reset** 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续

- `Falling edge` — 当 Reset 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续
- `Either edge` — 当 Reset 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作
- `Non-zero sample` — 在 Reset 输入不为零的每个采样时刻触发复位操作

要禁用复位端口，请将 **Reset port** 设置为 `None`。

#### 依赖关系

要启用此端口，请将 **Reset port** 设置为 `None` 以外的任何选项。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Output** — 滤波后的信号 标量 | 列向量

滤波后的信号，以标量或列向量形式返回。模块自适应其滤波器系数以使输入信号收敛以匹配期望信号。滤波器输出收敛后的信号。有关模块如何计算输出的更多信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Error** — 输出与期望信号之间的差值 标量 | 列向量

滤波后的信号与期望信号之间的差值，以标量或列向量形式返回。LMS 滤波器的目标是最小化此误差。模块自适应其系数以收敛到最优滤波器系数，从而产生与期望信号紧密匹配的输出信号。有关模块如何计算误差的更多信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Wts** — 自适应滤波器权重 标量 | 列向量

LMS 滤波器的权重，以列向量形式返回，其长度等于 **Filter length** 参数中指定的值。对于每次迭代，模块从此端口输出当前更新后的滤波器权重。有关模块如何更新滤波器权重的更多信息，请参阅算法。

滤波器权重的数据类型与滤波后信号的数据类型匹配。

#### 依赖关系

要启用此端口，请选中 **Output filter weights** 参数。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter length
  summary: FIR 滤波器系数向量的长度 32（默认）| 正整数
  group: ''
- name: Block size
  summary: 权重自适应前获取的采样数 32（默认）| 正整数
  group: ''
- name: Specify step size via
  summary: 自适应步长的来源 Dialog（默认）| Input port
  group: ''
- name: Step size (mu)
  summary: 自适应步长 0.1（默认）| 非负整数
  group: ''
- name: Leakage factor (0 to 1)
  summary: 泄漏 LMS 算法中使用的泄漏因子 1.0（默认）| [0, 1] 范围内的标量
  group: ''
- name: Initial value of filter weights
  summary: 滤波器权重的初始值 0（默认）| 标量 | 向量
  group: ''
- name: Adapt port
  summary: 启用 Adapt 端口 off（默认）| on
  group: ''
- name: Reset port
  summary: 启用 Reset 端口 None（默认）| Rising edge | Falling edge | Either edge | Non-zero sample
  group: ''
- name: Output filter weights
  summary: 输出滤波器权重 on（默认）| off
  group: ''
```

### **Filter length** — FIR 滤波器系数向量的长度 `32`（默认）| 正整数

指定 FIR 滤波器系数向量的长度，为正整数。

### **Block size** — 权重自适应前获取的采样数 `32`（默认）| 正整数

指定模块在更新滤波器权重之前必须获取的输入信号采样数，为正整数。输入帧长度（输入中的行数）必须是此参数中指定值的整数倍。

### **Specify step size via** — 自适应步长的来源 `Dialog`（默认）| `Input port`

通过以下方式指定自适应步长：

- `Dialog` –– 使用 **Step size (mu)** 参数在模块对话框中指定步长。
- `Input port` –– 使用 **Step-size** 输入端口指定步长。

### **Step size (mu)** — 自适应步长 `0.1`（默认）| 非负整数

指定自适应步长 *µ*，为非负整数。您可以使用 **Step-size** 输入端口指定步长，或在此参数中输入值。

较小的步长可确保输出信号与期望信号之间具有较小的稳态误差。如果步长较小，滤波器的收敛速度会降低。要提高收敛速度，请增大步长。请注意，如果步长过大，滤波器可能变得不稳定。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Specify step size via** 参数设置为 `Dialog`。

### **Leakage factor (0 to 1)** — 泄漏 LMS 算法中使用的泄漏因子 `1.0`（默认）| [0, 1] 范围内的标量

指定泄漏 LMS 算法中使用的泄漏因子，为 [0, 1] 范围内的标量，0<1−μα≤1。

w(k)=(1−μα)w(k−1)+f(u(n),e(n),μ)

当该值小于 1 时，模块实现泄漏 LMS 算法。默认值为 `1`，在自适应算法中不提供泄漏。

**可调：** 是

### **Initial value of filter weights** — 滤波器权重的初始值 `0`（默认）| 标量 | 向量

指定滤波器权重的初始值，为标量或长度等于滤波器长度的向量。当您指定标量时，模块使用该标量值创建滤波器权重向量。此向量的长度等于滤波器长度，且其所有值均等于该标量值。

### **Adapt port** — 启用 Adapt 端口 `off`（默认）| `on`

选中此参数以启用 **Adapt** 输入端口。使用此端口指定模块是否必须更新其滤波器权重或将其保持在当前水平。有关更多信息，请参阅 **Adapt** 输入端口的描述。

### **Reset port** — 启用 Reset 端口 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

选中此参数以启用 **Reset** 输入端口。有关每个复位选项的更多信息，请参阅 **Reset** 输入端口的描述。

### **Output filter weights** — 输出滤波器权重 `on`（默认）| `off`

选中此参数以从 **Wts** 端口导出滤波器权重。
## 所属库

DSP System Toolbox / Filtering / Adaptive Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 LMS 自适应算法计算输出、误差和权重

Block LMS Filter 模块实现自适应最小均方 (LMS) 滤波器，其中滤波器权重的自适应对每块采样执行一次。模块估计最小化输出信号 *y*(*n*) 与期望信号 *d*(*n*) 之间误差 *e*(*n*) 所需的滤波器权重（也称为系数）。有关更多信息，请参阅算法。有关自适应滤波器的更多信息，请参阅自适应滤波器与应用概述。
