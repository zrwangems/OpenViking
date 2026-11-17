---
type: simulink-block
title: 'LMS Update'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'lmsupdate'
documentation_source_path: 'ref/lmsupdate.html'
language: zh-CN
chinese_source: worker-translation
---

# LMS Update

## 端口

### 输入

### **Input** — 数据输入 标量 | 列向量

自适应滤波器的数据输入，指定为以下之一：

- 标量 –– 当您将 **Adaptive filter mode** 参数设置为 `Tapped delay-line FIR filter` 时，模块的输入应为标量。

  模块算法对输入样本进行缓冲以生成向量 u(n)=[u(n),u(n−1),...,u(n−L+1)]，其中 *L* 是自适应滤波器的长度，*n* 是时间索引。然后模块算法将该向量通过滤波器。
- 长度为 *L* 的列向量 –– 当您将 **Adaptive filter mode** 参数设置为 `Adaptive linear combiner` 时，模块不对输入样本进行缓冲，模块的输入应为列向量形式。模块将该向量与滤波器权重相乘，生成滤波器输出。在这种情况下，输入样本之间没有关系。

当您将 **Number of adaptive filters** 参数设置为大于 1 的值时，模块假定所有滤波器在同一输入上运行。

当您将 **Algorithm** 参数设置为 `Sign—Error LMS`、`Sign—Data LMS` 或 `Sign—Sign LMS` 时，通过 **Input** 端口输入的数据必须为实数。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Error** — 误差 标量 | 列向量

将输出信号与期望信号之间的误差指定为：

- 当自适应滤波器数量 *N* = 1 时为标量。
- 当 *N* > 1 时为长度为 *N* 的列向量。

当您将 **Algorithm** 参数设置为 `Sign—Error LMS`、`Sign—Data LMS` 或 `Sign—Sign LMS` 时，通过 **Error** 端口输入的误差必须为实数。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Mu** — 滤波器自适应步长 0.1（默认）| 范围 [0,1] 内的标量

将滤波器自适应步长指定为范围 [0,1] 内的标量。

#### 依赖关系

要启用此端口，请将 **Step size source** 设置为 `Input port`。

**数据类型：** `single` | `double`

### **Adapt** — 更新滤波器权重 实数标量 | 向量

此端口的输入可以是以下之一：

- 标量 –– 如果自适应滤波器数量（*N*）大于 1，则当端口处的值非零时，模块更新所有滤波器的滤波器权重；当端口处的值为 0 时不更新。
- 长度为 *N* 的向量 –– 如果自适应滤波器数量（*N*）大于 1，则模块根据 **Adapt** 向量输入中对应元素的值，在运行时确定是否更新每个滤波器。当 **Adapt** 端口输入元素不为 0 时，模块更新滤波器权重。当输入为 0 时，滤波器权重不变。

有关示例，请参阅 Adapt Multiple Filters Using LMS Update Block。

#### 依赖关系

要启用此端口，请在模块对话框中选中 **Enable adapt input** 参数。

**数据类型：** `single` | `double` | `Boolean` | `int16` | `int32` | `int64` | `int8` | `uint16` | `uint32` | `uint64` | `uint8`

### **Reset** — 重置滤波器权重 实数标量

当此端口的输入不为 0 时，模块将滤波器权重重置为其初始值。当此端口的输入为 0 时，滤波器权重不变。

#### 依赖关系

要启用此端口，请在模块对话框中选中 **Enable reset input** 参数。

**数据类型：** `single` | `double` | `Boolean` | `int16` | `int32` | `int64` | `int8` | `uint16` | `uint32` | `uint64` | `uint8`
### 输出

### **Wts** — 滤波器权重 行向量 | 矩阵

模块将滤波器权重输出为 1×*L* 行向量或 *N*×*L* 矩阵，其中 *N* 是自适应滤波器数量，*L* 是每个滤波器的长度。

**数据类型：** `single` | `double`

## 参数

### **Algorithm** — LMS 自适应算法 `LMS`（默认）| `Normalized LMS` | `Sign—Error LMS` | `Sign—Data LMS` | `Sign—Sign LMS`

模块使用所列算法之一来计算滤波器权重。有关算法的更多详细信息，请参阅 Algorithms。

### **Filter length** — 滤波器长度 32（默认）| 正整数

将每个自适应滤波器的长度 *L* 指定为正整数。

当有 *N* 个自适应滤波器时，模块通过 **Wts** 输出端口生成的权重向量为 *N*×*L* 矩阵。

### **Number of adaptive filters** — 自适应滤波器数量 1（默认）| 正整数

将模块支持的自适应滤波器数量 *N* 指定为正整数。

当您将此值指定为大于 1 的整数时，可以通过提供长度为 *N* 的逻辑向量作为 **Adapt** 输入，在运行时选择每个滤波器独立自适应。假定所有滤波器在同一输入上运行，并具有共同的步长、泄漏因子和重置输入。

模块通过 **Wts** 输出端口生成的权重为 *N*×*L* 矩阵，其中 *L* 是每个滤波器的长度。

有关展示如何自适应多个滤波器的示例，请参阅 Adapt Multiple Filters Using LMS Update Block。

### **Step size source** — 指定步长的方法 `Property`（默认）| `Input port`

- `Property` — 使用 **Step size (mu)** 参数指定滤波器自适应步长。
- `Input port` — 使用 **Mu** 输入端口传递滤波器自适应步长。

### **Step size (mu)** — 自适应步长的大小 0.1（默认）| 非负标量

**Step size (mu)** 表示每次迭代中滤波器权重更新的量。选择最优步长，使滤波器稳定且收敛速度最优。

此参数可调。您甚至可以在仿真期间更改其值。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Step size source** 设置为 `Property`。

### **Leakage factor (0 to 1)** — 泄漏因子 1.0（默认）| 范围 [0,1] 内的实数标量

**Leakage factor (0 to 1)** 通过减少系数从其最优值的漂移，防止滤波器系数无界增长。泄漏因子为 `1.0` 表示无泄漏。如果您遇到系数漂移，即围绕最优解的大幅波动，请减小泄漏因子，直到系数波动变小。

此参数可调。您甚至可以在仿真期间更改其值。

**可调：** 是

### **Initial value of filter weights** — 滤波器权重的初始值 0（默认）| 实数标量 | 向量 | 矩阵

将滤波器权重的初始值指定为以下之一：

- 标量
- 大小为 1×*L* 的向量 –– *N* 设置为 1
- 大小为 *N*×*L* 的矩阵 –– *N* > 1 且 *L* > 1

其中 *N* 是在 **Number of adaptive filters** 中指定的自适应滤波器数量，*L* 是在 **Filter length** 中指定的每个滤波器的长度。

此参数指定滤波器权重 **w**(*n*−1) 的初始值。当 *n* = 1 时，模块使用此值计算权重 **w**(*n*)。有关更多信息，请参阅 Algorithms。

### **Adaptive filter mode** — 自适应滤波器模式 `Tapped delay-line FIR filter`（默认）| `Adaptive linear combiner`

将自适应滤波器模式指定为以下之一：

- `Tapped delay-line FIR filter` –– 模块假定自适应滤波器的可变部分为抽头延迟线 FIR 滤波器。在此模式下，输入样本使用以下方程关联：

  u(n)=[u(n),u(n−1),...,u(n−L+1)]

  其中 *n* 是当前时间索引，*L* 是在 **Filter length** 参数中指定的自适应滤波器长度。

  模块在此模式下接受标量输入样本。模块算法对样本进行缓冲以形成 **u**(*n*) 向量。
- `Adaptive linear combiner` –– 模块不对输入样本进行缓冲，您提供给模块的输入必须是长度等于 **Filter length** 参数的列向量。在这种情况下，输入样本之间没有关系。

有关更多详细信息，请参阅 Algorithms。

### **Enable adapt input** — 更新滤波器权重 off（默认）| on

当您选中此复选框时，**Adapt** 输入端口出现在模块上。当此端口的输入大于 0 时，模块更新滤波器权重。当此端口的输入小于或等于 0 时，滤波器权重不变。

### **Enable reset input** — 重置滤波器权重 off（默认）| on

当您选中此复选框时，**Reset** 输入端口出现在模块上。当此端口的输入大于 0 时，模块将滤波器权重重置为其初始值。当此端口的输入小于或等于 0 时，滤波器权重不变。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 为模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但提供更快的后续仿真。

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

## 版本历史

**在 R2016b 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

## 描述

估计最小均方（LMS）自适应滤波器的权重

LMS Update 模块估计最小均方（LMS）自适应滤波器的权重。将数据和误差指定为输入，模块根据 **Algorithm** 参数中指定的算法计算滤波器权重。有关算法的更多详细信息，请参阅 Algorithms。

您可以使用 **Adaptive filter mode** 参数将模块配置为抽头延迟线 FIR 滤波器或自适应线性组合器。当您将 **Number of adaptive filters** 参数指定为大于 1 的值时，模块还可以独立地自适应多个滤波器。

您可以使用此模块在系统辨识、逆建模和 filtered-x LMS 算法等应用中计算自适应滤波器权重，这些应用用于声学噪声消除。有关更多详细信息，请参阅 References。
