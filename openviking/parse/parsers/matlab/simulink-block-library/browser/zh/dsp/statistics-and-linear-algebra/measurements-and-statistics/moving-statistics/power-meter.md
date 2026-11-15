---
type: simulink-block
title: 'Power Meter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Measurements and Statistics / Moving Statistics'
documentation_page: 'powermeter'
documentation_source_path: 'ref/powermeter.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Meter

## 端口

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵

以 volts 为单位将输入信号指定为向量或矩阵。如果 `x` 是矩阵，则模块将每一列视为独立通道，并沿每个通道计算功率测量。

当 **Allow arbitrary frame length for fixed-size input signals** 参数出现且未选中，并且您输入固定大小信号时，帧长度必须是 hop size（窗口长度 − 重叠长度）的整数倍。在所有其他情况下，输入帧长度可以是任意的。

模块接受可变大小输入（帧长度在仿真期间变化）。当您输入可变大小信号时，信号的帧长度可以是任意的。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Rst** — 复位端口 标量

将布尔复位信号指定为标量。如果 **Rst** 端口上的输入为 `true`，则模块在处理当前输入之前清除内部直方图和统计量。如果 **Rst** 端口上的输入为 `false`，则模块从仿真开始或上次复位开始计算测量。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 和 **Reset port** 参数。

**数据类型：** `Boolean`
### 输出

### **Avg** — 平均功率 标量 | 向量 | 矩阵

从仿真开始或上次复位开始的电压信号平均功率，以标量、向量或矩阵形式返回。模块按照 **Output power units** 参数中指定的单位沿每个通道计算平均功率。有关模块如何计算平均功率的详细信息，请参阅平均功率。

如果您清除 **Compute CCDF** 参数，则模块使用 Sliding Window Method 计算移动平均功率。

有关输出信号维度的详细信息，请参见此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*×*M*，其中 *M* 是 hop size（窗口长度 − 重叠长度）的整数倍 | (*P*/hop size)×*M* | *P*×*M* |
| 固定大小信号 | *P*×*M*，其中 *M* 不是 hop size（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/hop size)×*M*。如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块会报错。 | *P*×*M* |
| 可变大小信号 | *P*×*M* | `ceil`(*P*/hop size)×*M* | *P*×*M* |

当输出的上限大小为 `ceil`(*P*/hop size)×*M* 时，在仿真期间，第一维的大小在此界限内变化，而第二维的大小保持恒定。

如果您选择 **Compute CCDF** 参数，则模块计算每个通道上整个信号的平稳平均功率。在这种情况下，输出大小为 1×*M*，其中 *M* 是输入信号中的通道数（列数）。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Average power` 或 `All`。

**数据类型：** `single` | `double`

### **Peak** — 峰值功率 标量 | 向量 | 矩阵

从仿真开始或上次复位开始的电压信号峰值功率，以标量、向量或矩阵形式返回。模块按照 **Output power units** 参数中指定的单位沿每个通道计算峰值功率。有关模块如何计算峰值功率的详细信息，请参阅峰值功率。

如果您清除 **Compute CCDF** 参数，则模块使用 Sliding Window Method 计算移动峰值功率。

有关输出信号维度的详细信息，请参见此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*×*M*，其中 *M* 是 hop size（窗口长度 − 重叠长度）的整数倍 | (*P*/hop size)×*M* | *P*×*M* |
| 固定大小信号 | *P*×*M*，其中 *M* 不是 hop size（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/hop size)×*M*。如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块会报错。 | *P*×*M* |
| 可变大小信号 | *P*×*M* | `ceil`(*P*/hop size)×*M* | *P*×*M* |

当输出的上限大小为 `ceil`(*P*/hop size)×*M* 时，在仿真期间，第一维的大小在此界限内变化，而第二维的大小保持恒定。

如果您选择 **Compute CCDF** 参数，则模块计算每个通道上整个信号的平稳峰值功率。在这种情况下，输出大小为 1×*M*，其中 *M* 是输入信号中的通道数（列数）。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Peak power` 或 `All`。

**数据类型：** `single` | `double`

### **PAPR** — 峰均功率比 标量 | 向量 | 矩阵

电压信号的峰值功率与平均功率之比（PAPR），以标量、向量或矩阵形式返回。模块沿每个通道计算峰均功率比。有关模块如何计算此测量的详细信息，请参阅峰均功率比。

如果您清除 **Compute CCDF** 参数，则模块使用 Sliding Window Method 计算移动峰均功率比。

有关输出信号维度的详细信息，请参见此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*×*M*，其中 *M* 是 hop size（窗口长度 − 重叠长度）的整数倍 | (*P*/hop size)×*M* | *P*×*M* |
| 固定大小信号 | *P*×*M*，其中 *M* 不是 hop size（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/hop size)×*M*。如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块会报错。 | *P*×*M* |
| 可变大小信号 | *P*×*M* | `ceil`(*P*/hop size)×*M* | *P*×*M* |

当输出的上限大小为 `ceil`(*P*/hop size)×*M* 时，在仿真期间，第一维的大小在此界限内变化，而第二维的大小保持恒定。

如果您选择 **Compute CCDF** 参数，则模块计算每个通道上整个信号的平稳峰均功率比。在这种情况下，输出大小为 1×*M*，其中 *M* 是输入信号中的通道数（列数）。

为获得准确的 CCDF 测量，PAPR 应小于 100 dB。如果 PAPR 高于 100 dB，则模块仅显示最高的 100 dB 功率水平。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Peak-to-average power ratio` 或 `All`。

**数据类型：** `single` | `double`

### **RelPwr** — 相对功率 *N*×*M* 矩阵

相对功率（高于平均功率的 dB 值），以 *N*×*M* 矩阵形式返回，其中：

- *M* 是输入信号中的通道数（列数）。
- 当您将 **CCDF output** 设置为 `Relative power (dB above average power)` 时，*N* 等于您在 **Specify probability (%) for relative power output** 参数中指定的列向量长度。
- 当您将 **CCDF output** 设置为 `Relative power and probability (whole CCDF curve)` 时，*N* 等于 `ceil`(**Power range (dB)**/**Power resolution (dB)**) + 1。

相对功率是这样的功率（以 dB 为单位）：瞬时信号功率以 **Prob**（以百分比表示）的概率高于平均信号功率。有关模块如何计算相对功率的详细信息，请参阅相对功率。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 参数，然后将 **CCDF output** 参数设置为 `Relative power (dB above average power)` 或 `Relative power and probability (whole CCDF curve)`。

**数据类型：** `single` | `double`

### **Prob** — 百分比概率 *N*×*M* 矩阵

百分比概率，以 *N*×*M* 矩阵形式返回，其中：

- *M* 是输入信号中的通道数（列数）。
- 当您将 **CCDF output** 设置为 `Probability (%)` 时，*N* 等于您在 **Specify relative power (dB) for probability output** 参数中指定的列向量长度。
- 当您将 **CCDF output** 设置为 `Relative power and probability (whole CCDF curve)` 时，*N* 等于 `ceil`(**Power range (dB)**/**Power resolution (dB)**) + 1。

**Prob**(*i*)/100 是第 *j* 个通道的瞬时信号功率高于其平均信号功率 **RelPwr**(*i*,*j*) dB 的概率。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 参数，然后将 **CCDF output** 参数设置为 `Probability (%)` 或 `Relative power and probability (whole CCDF curve)`。

**数据类型：** `single` | `double`

## 参数

### **Measurement** — 期望功率测量 `Average power`（默认） | `Peak power` | `Peak-to-average power ratio` | `All`

将期望功率测量指定为以下之一：

- `Average power`（默认）
- `Peak power`
- `Peak-to-average power ratio`
- `All`

有关模块如何计算这些测量的详细信息，请参阅算法。

### **Reference load (ohms)** — 以 ohms 为单位的参考负载 `1`（默认） | 以 ohms 为单位的正标量

指定功率计用于计算功率值的参考负载，以 ohms 为单位的实正标量。

**可调：** 是

**数据类型：** `single` | `double`

### **Output power units** — 测量功率值的单位 `dBm`（默认） | `dBW` | `Watts`

将测量功率值的单位指定为以下之一：

- `dBm`
- `dBW`
- `Watts`

### **Compute CCDF** — 启用 CCDF 计算 off（默认） | on

选择 **Compute CCDF** 参数以使模块能够计算电压信号功率的 CCDF。CCDF 测量包括相对功率和概率（以百分比表示）。相对功率是瞬时信号功率高于平均信号功率的功率量（以 dB 为单位）。百分比概率是指瞬时信号功率高于平均信号功率达相对功率（以 dB 为单位）的概率。

这些测量提供了一种定性方式来查看输入信号幅度值随时间的功率分布。CCDF 曲线（百分比概率对相对功率（以 dB 为单位）的图）是信号动态范围的有用指标。

当您选择 **Compute CCDF** 时：

- 模块使用从仿真开始或从 **Rst** 端口上的复位信号开始的所有输入采样来计算统计量。功率测量是平稳的。
- 您可以指定可变大小输入信号。

当您清除 **Compute CCDF** 时，

- 模块不计算 CCDF 测量，并使用 Sliding Window Method 计算功率测量。
- 仅当您选择 **Allow arbitrary frame length for fixed-size input signals** 参数时，模块才接受任意帧长度的输入信号。

### **Window length** — 窗口长度 `256`（默认） | 正整数

将模块用于计算测量的窗口长度指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 复选框。当您选择 **Compute CCDF** 时，**Window length** 变为 `Inf`。

**数据类型：** `single` | `double`

### **Overlap length** — 窗口之间的重叠长度 `255`（默认） | 非负整数

将滑动窗口之间的重叠长度指定为非负整数。重叠长度的值在 [0, **Window length** − 1] 范围内变化。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 复选框。当您选择 **Compute CCDF** 时，**Overlap length** 变为 `0`。

**数据类型：** `single` | `double`

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号使用任意帧长度 off（默认） | on

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是 hop size 的整数倍。Hop size 定义为 **Window length** − **Overlap length**。模块仅对固定大小输入信号使用此参数设置，如果输入为可变大小，则忽略此参数。

当输入信号为可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是 hop size 的整数倍。

对于固定大小输入信号，如果您：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是 hop size 的整数倍。如果输入不是 hop size 的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，模块还必须支持可变大小运算，您可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该运算。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是 hop size 的整数倍。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 参数。

### **Power range (dB)** — 以 dB 为单位的功率范围 `50`（默认） | 正标量

将 CCDF 曲线的 *x* 轴范围指定为以 dB 为单位的正标量。CCDF 曲线结束于最大相对功率，即信号的 PAPR，并从 PAPR − **Power range (dB)** 开始。在 Power Meter 模块的 CCDF 功能中，相对功率是瞬时信号功率高于平均信号功率的功率（以 dB 为单位）。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

**数据类型：** `single` | `double`

### **Power resolution (dB)** — 以 dB 为单位的功率分辨率 `0.1`（默认） | 正标量

将 CCDF 曲线的 *x* 轴分辨率指定为以 dB 为单位的正标量。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

**数据类型：** `single` | `double`

### **CCDF output** — CCDF 输出 `Relative power (dB above average power)`（默认） | `Probability (%)` | `Relative power and probability (whole CCDF curve)`

指定模块输出：

- **RelPwr** –– 相对功率（高于平均功率的 dB 值）。这是瞬时信号功率高于平均功率的功率量（以 dB 为单位）。
- **Prob** –– 百分比概率。这是瞬时信号功率高于平均信号功率达相对功率 dB 值的概率。
- **RelPwr** 和 **Prob** 两者。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

### **Specify probability (%) for relative power output** — 为相对功率输出指定概率 [`10`;`1`;`0.1`;`0.01`;`0.001`;`0.0001`]（默认） | 列向量

将相对功率输出的概率（以百分比表示）指定为列向量。此向量的长度决定 **RelPwr** 端口处相对功率输出的行数。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框，并将 **CCDF output** 参数设置为 `Relative power (dB above average power)`。

这也会启用 **RelPwr** 输出端口。

**数据类型：** `single` | `double`

### **Specify relative power (dB) for probability output** — 为概率输出指定相对功率 [`0`;`3`;`6`;`9`;`12`]（默认） | 列向量

将概率输出的相对功率（以 dB 为单位）指定为列向量。此向量的长度决定 **Prob** 端口处概率输出的行数。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框，并将 **CCDF output** 参数设置为 `Probability (%)`。

这也会启用 **Prob** 输出端口。

**数据类型：** `single` | `double`

### **Reset port** — 启用复位端口 off（默认） | on

选择此参数以启用接受布尔信号的输入端口 **Rst**。如果 **Rst** 端口处的值为 `true`，则模块在处理当前输入之前清除内部直方图和统计量。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不变，C 代码会在后续仿真中复用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Statistics Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a：更改 **Simulate using** 参数的默认值

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

### R2022b：新增 **Overlap length** 参数

从 R2022b 开始，当模块不计算 CCDF 测量时，您可以使用 **Overlap length** 参数指定滑动窗口之间的重叠长度。

### R2022b：支持任意输入帧长度

当以下情况时，Power Meter 模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变），并且您选择 **Allow arbitrary frame length for fixed-size input signals** 参数（如果已启用）。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当此模块支持任意帧长度输入信号时，输入帧长度不必是 hop size 的整数倍。

## 描述

在 Simulink 中测量电压信号的功率以及功率的 CCDF

Power Meter 模块计算电压信号的功率测量。当您选择 **Compute CCDF** 参数时，模块还会计算电压信号功率的互补累积分布函数（CCDF）。模块输出的 CCDF 测量包括相对功率和概率（以百分比表示）。功率测量包括平均功率、峰值功率和峰均功率比。

有关模块如何计算功率测量和 CCDF 测量的更多详细信息，请参阅算法。
