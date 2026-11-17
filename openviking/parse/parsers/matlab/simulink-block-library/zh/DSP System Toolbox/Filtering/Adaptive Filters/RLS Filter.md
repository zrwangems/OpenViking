---
type: simulink-block
title: 'RLS Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'rlsfilter'
documentation_source_path: 'ref/rlsfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# RLS Filter

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
- name: Lambda
  summary: 遗忘因子 范围 [0,1] 内的标量
  direction: input
  data_types: single | double
- name: Adapt
  summary: 更新滤波器权重的选项 标量 | 列向量
  direction: input
  data_types: single | double
- name: Reset
  summary: 复位信号 标量
  direction: input
  data_types: single | double
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

指定要滤波的输入信号，可以是标量或列向量。

输入信号和期望信号必须具有相同的大小、数据类型和复数特性。

输入信号可以是可变大小信号，也就是说，只要信号维度与输入信号匹配，信号的帧长度可以在仿真期间变化。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Desired** — 期望信号 标量 | 列向量

指定要建模的信号，可以是标量或列向量。RLS 滤波器自适应调整其系数以最小化误差，并使输入信号尽可能接近期望信号。

输入信号和期望信号必须具有相同的大小、数据类型和复数特性。

期望信号可以是可变大小信号，也就是说，只要信号维度与输入信号匹配，信号的帧长度可以在仿真期间变化。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Lambda** — 遗忘因子 范围 [0,1] 内的标量

通过此输入端口指定 RLS 遗忘因子 *λ*，为范围 `0` ≤ *λ* ≤ `1` 内的标量。有关此参数的详细信息，请参阅 **Forgetting factor (0 to 1)** 参数说明。

#### 依赖关系

要启用此端口，请将 **Specify forgetting factor via** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

### **Adapt** — 更新滤波器权重的选项 标量 | 列向量

如果输入为非零值，模块会持续更新滤波器权重。如果此输入的值为零，滤波器权重保持其当前值。

#### 依赖关系

要启用此端口，请选中 **Adapt port** 参数。

**数据类型：** `single` | `double`

### **Reset** — 复位信号 标量

将复位信号指定为标量信号。当您想将滤波器权重的值复位为其初始值时，请使用 **Reset port** 参数。模块在 **Reset** 端口检测到复位事件时复位滤波器权重。复位信号速率必须与数据信号输入的速率相同。

要启用 **Reset** 端口，请从 **Reset port** 列表中选择以下选项之一：

- `Rising edge` — 当 **Reset** 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零
  - 从零上升到正值，且该上升不是从负值上升到零的延续

- `Falling edge` — 当 **Reset** 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零
  - 从零下降到负值，且该下降不是从正值下降到零的延续

- `Either edge` — 当 **Reset** 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作
- `Non-zero sample` — 在每个采样时间，当 **Reset** 输入不为零时触发复位操作

要禁用复位端口，请将 **Reset port** 设置为 `None`。

#### 依赖关系

要启用此端口，请将 **Reset port** 设置为除 `None` 以外的任何选项。

**数据类型：** `single` | `double`
### 输出

### **Output** — 滤波后的信号 标量 | 列向量

滤波后的信号，以标量或列向量形式返回。模块自适应调整其滤波器系数，使输入信号收敛以匹配期望信号。滤波器输出收敛后的信号。有关模块如何计算输出的更多详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Error** — 输出与期望信号之间的差值 标量 | 列向量

滤波后的信号与期望信号之间的差值，以标量或列向量形式返回。RLS 滤波器的目标是最小化此误差。模块自适应调整其系数以收敛到最优滤波器系数，从而产生与期望信号紧密匹配的输出信号。有关模块如何计算误差的更多详细信息，请参阅算法。

模块通过 **Wts** 端口输出 RLS 滤波器系数。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Wts** — 自适应滤波器权重 标量 | 列向量

RLS 滤波器的权重，以长度等于您在 **Filter length** 参数中指定的值的列向量形式返回。对于每次迭代，模块从此端口输出当前更新后的滤波器权重。有关模块如何更新滤波器权重的更多信息，请参阅算法。

滤波器权重的数据类型与滤波后信号的数据类型匹配。

#### 依赖关系

要启用此端口，请选中 **Output filter weights** 参数。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter length
  summary: FIR 滤波器系数向量的长度 向量 32（默认）| 正整数
  group: ''
- name: Specify forgetting factor via
  summary: 指定遗忘因子 Dialog（默认）| Input port
  group: ''
- name: Forgetting factor (0 to 1)
  summary: RLS 遗忘因子 1.0（默认）| 范围 [0,1] 内的标量
  group: ''
- name: Initial value of filter weights
  summary: FIR 滤波器权重的初始值 0（默认）| 向量
  group: ''
- name: Initial input variance estimate
  summary: 初始输入协方差估计 0.1（默认）| 标量 | 方阵
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

### **Filter length** — FIR 滤波器系数向量的长度 向量 `32`（默认）| 正整数

将 FIR 滤波器系数向量 *L* 的长度指定为正整数。

### **Specify forgetting factor via** — 指定遗忘因子 `Dialog`（默认）| `Input port`

通过以下方式指定遗忘因子：

- `Dialog` –– 使用 **Forgetting factor (0 to 1)** 参数在模块对话框中指定遗忘因子。
- `Input port` –– 使用 **Lambda** 输入端口指定遗忘因子。

### **Forgetting factor (0 to 1)** — RLS 遗忘因子 `1.0`（默认）| 范围 [0,1] 内的标量

将 RLS 遗忘因子 *λ* 指定为范围 `0` ≤ *λ* ≤ `1` 内的标量。此参数指定滤波器遗忘过去样本信息的速度。设置 *λ* = `1` 表示无限记忆，同时自适应寻找新的滤波器。通常，1−12L<λ<1，其中 *L* 是滤波器长度。您可以使用输入端口 **Lambda** 指定遗忘因子，或在模块对话框的 **Forgetting factor (0 to 1)** 参数中输入值。

#### 依赖关系

要启用此参数，请将 **Specify forgetting factor via** 参数设置为 `Dialog`。

**可调：** 是

### **Initial value of filter weights** — FIR 滤波器权重的初始值 `0`（默认）| 向量

将 FIR 滤波器权重 w^(0) 的初始值指定为标量或长度等于滤波器长度的向量。当您指定标量时，模块使用该标量值创建滤波器权重向量。此向量的长度等于滤波器长度，且其所有值都等于该标量值。

### **Initial input variance estimate** — 初始输入协方差估计 `0.1`（默认）| 标量 | 方阵

将输入协方差估计 1/**P**(*n*) 的初始值指定为：

- 标量 –– **P**(*n*) 是对角矩阵，其对角元素等于该标量值。
- 方阵 –– 矩阵的每个维度等于您在 **Filter length** 参数中指定的值。

**P**(*n*) 的初始值为 1σ2I，其中您在 **Initial input variance estimate** 参数中指定 σ2。

### **Adapt port** — 启用 Adapt 端口 `off`（默认）| `on`

选中此参数以启用 **Adapt** 输入端口。使用此端口指定模块必须更新其滤波器权重还是将其保持在当前水平。有关更多信息，请参阅 **Adapt** 输入端口的说明。

### **Reset port** — 启用 Reset 端口 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

选中此参数以启用 **Reset** 输入端口。有关每个复位选项的更多信息，请参阅 **Reset** 输入端口的说明。

### **Output filter weights** — 输出滤波器权重 `on`（默认）| `off`

选中此参数以从 **Wts** 端口导出滤波器权重。
## 所属库

DSP System Toolbox / Filtering / Adaptive Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 RLS 自适应滤波器算法，针对给定输入和期望信号计算滤波输出、滤波器误差和滤波器权重

RLS Filter 模块递归计算 FIR 滤波器权重的递归最小二乘（RLS）估计。该模块估计最小化输出信号 *y*(*n*) 与期望信号 *d*(*n*) 之间误差 *e*(*n*) 所需的滤波器权重（也称为系数）。有关更多信息，请参阅算法。有关自适应滤波器的更多信息，请参阅自适应滤波器与应用概述。
