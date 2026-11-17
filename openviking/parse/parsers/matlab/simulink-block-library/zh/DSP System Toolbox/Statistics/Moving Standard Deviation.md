---
type: simulink-block
title: 'Moving Standard Deviation'
family: 'statistics'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'movingstandarddeviation'
documentation_source_path: 'ref/movingstandarddeviation.html'
language: zh-CN
chinese_source: worker-translation
---

# Moving Standard Deviation

## 端口

### 输入

### **x** — 数据输入 向量 | 矩阵

该模块计算此输入端口处所指定数据的移动标准差。指定大小为 *m*×*n* 的实值或复值多通道输入，其中 *m* ≥ 1 且 *n* ≥ 1。

当 **Allow arbitrary frame length for fixed-size input signals** 参数出现且未选中，并且输入固定大小信号时，帧长度必须是跳跃大小（窗口长度 − 重叠长度）的倍数。在所有其他情况下，输入帧长度可以是任意的。

该模块接受可变大小输入（帧长度在仿真期间变化）。当输入可变大小信号时，信号的帧长度可以是任意的。

在将 **Method** 设置为 `Exponential weighting` 并选中 **Specify forgetting factor from input port** 参数之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **lambda** — 遗忘因子 范围 [0,1] 中的非负实数标量

将遗忘因子指定为范围 [0,1] 中的非负实数标量。遗忘因子决定过去数据被赋予的权重。与遗忘因子 0.1 相比，遗忘因子 0.9 为较旧数据赋予更多权重。遗忘因子 1.0 表示无限记忆，并且所有先前样本被赋予相等权重。遗忘因子 0 表示无记忆，并且过去样本对当前计算没有权重。

#### 依赖关系

当你将 **Method** 设置为 `Exponential weighting` 并选中 **Specify forgetting factor from input port** 参数时，此端口出现。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 移动标准差输出 向量 | 矩阵

移动标准差输出，以向量或矩阵形式返回。该模块根据 **Method** 参数设置，使用滑动窗口方法或指数加权方法计算移动标准差。有关更多详细信息，请参阅算法。

下表提供了有关输出信号维度的更多详细信息。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 不出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *m*×*n*，其中 *m* 是跳跃大小（窗口长度 − 重叠长度）的倍数 | (*m*/跳跃大小)×*n* | *m*×*n* |
| 固定大小信号 | *m*×*n*，其中 *m* 不是跳跃大小（窗口长度 − 重叠长度）的倍数 | 当你选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*m*/跳跃大小)×*n*  如果你不选中 **Allow arbitrary frame length for fixed-size input signals**，该模块会报错。 | *m*×*n* |
| 可变大小信号 | *m*×*n* | `ceil`(*m*/跳跃大小)×*n* | *m*×*n* |

当输出的上限大小为 `ceil`(*m*/跳跃大小)×*n* 时，在仿真期间，第一个维度的大小在此界限内变化，而第二个维度的大小保持不变。有关显示此行为的示例，请参阅 Compute Moving Standard Deviation of Noisy Square Wave Signal。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

如果参数列为可调，则可以在仿真期间更改其值。

### **Method** — 移动标准差方法 `Sliding window` (默认) | `Exponential weighting`

- `Sliding window` — 长度为 **Window length** 的窗口沿每个通道在输入数据上移动。窗口每移动一个样本，该模块就计算窗口内数据的标准差。
- `Exponential weighting` — 该模块计算指数加权移动标准差并取其平方根。加权因子的幅度随着数据年龄的增加呈指数下降，但幅度永远不会达到零。

有关这些方法的更多详细信息，请参阅算法。

### **Specify window length** — 用于指定窗口长度的标志 on (默认) | off

当你选中此复选框时，滑动窗口的长度等于你在 **Window length** 中指定的值。当你清除此复选框时，滑动窗口的长度为无限。在此模式下，该模块计算当前样本相对于通道中所有先前样本的标准差。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Sliding window`。

### **Window length** — 滑动窗口的长度 4 (默认) | 正标量整数

指定滑动窗口的长度，以样本为单位。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Sliding window` 并选中 **Specify window length** 复选框。

### **Overlap length** — 窗口之间的重叠长度 `3` (默认) | 非负整数

将滑动窗口之间的重叠长度指定为非负整数。重叠长度的值在 [0, **Window length** − 1] 范围内变化。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Sliding window` 并选中 **Specify window length** 复选框。

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号使用任意帧长度 off (默认) | on

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是跳跃大小的倍数。跳跃大小定义为 **Window length** − **Overlap length**。该模块仅对固定大小输入信号使用此参数设置，如果输入为可变大小，则忽略此参数。

当输入信号为可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是跳跃大小的倍数。

对于固定大小输入信号，如果你：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是跳跃大小的倍数。如果输入不是跳跃大小的倍数，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，你可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该支持。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是跳跃大小的倍数。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Sliding window` 并选中 **Specify window length** 复选框。

### **Specify forgetting factor from input port** — 用于指定遗忘因子的标志 off (默认) | on

当你选中此复选框时，遗忘因子通过 **lambda** 端口输入。当你清除此复选框时，遗忘因子通过 **Forgetting factor** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Exponential weighting`。

### **Forgetting factor** — 指数加权因子 0.9 (默认) | 范围 [0,1] 中的非负实数标量

将指数加权因子指定为范围 [0,1] 中的非负实数标量。此值决定过去数据被赋予的权重。与遗忘因子 0.1 相比，遗忘因子 0.9 为较旧数据赋予更多权重。遗忘因子 1.0 表示无限记忆，并且所有过去样本被赋予相等权重。遗忘因子 0 表示无记忆，并且过去样本对当前计算没有权重。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Exponential weighting` 并清除 **Specify forgetting factor from input port** 复选框。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。你可以将此参数设置为：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024b：指定遗忘因子为 0

现在你可以在 Moving Standard Deviation 模块中指定遗忘因子为 0。

### R2024a：**Simulate using** 参数的默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2022b：新增 **Overlap length** 参数

从 R2022b 开始，你可以使用 **Overlap length** 参数指定滑动窗口之间的重叠长度。

### R2022b：支持任意输入帧长度

Moving Standard Deviation 模块在以下情况下支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变），并且你选中 **Allow arbitrary frame length for fixed-size input signals** 参数（如果启用）。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当此模块支持任意帧长度输入信号时，输入帧长度不必是跳跃大小的倍数。

## 描述

移动标准差

Moving Standard Deviation 模块沿每个通道独立地随时间计算输入信号的移动标准差。该模块使用滑动窗口方法或指数加权方法来计算移动标准差。在滑动窗口方法中，指定长度的窗口逐个样本地在数据上移动，并且该模块计算窗口内数据的标准差。在指数加权方法中，该模块计算指数加权移动方差并取其平方根。有关这些方法的更多详细信息，请参阅算法。
