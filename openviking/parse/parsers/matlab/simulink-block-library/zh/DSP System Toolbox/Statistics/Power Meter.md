---
type: simulink-block
title: 'Power Meter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'powermeter'
documentation_source_path: 'ref/powermeter.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Meter

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Rst
  summary: 复位端口 标量
  direction: input
  data_types: Boolean
- name: Avg
  summary: 平均功率 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
- name: Peak
  summary: 峰值功率 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
- name: PAPR
  summary: 峰均功率比 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
- name: RelPwr
  summary: 相对功率 *N*-by-*M* 矩阵
  direction: output
  data_types: single | double
- name: Prob
  summary: 概率（百分比） *N*-by-*M* 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵

以伏特为单位指定输入信号，可以是向量或矩阵。如果 `x` 是矩阵，模块将每一列视为独立通道，并沿每个通道计算功率测量值。

当 **Allow arbitrary frame length for fixed-size input signals** 参数出现且未被选中，并且您输入固定大小信号时，帧长度必须是跳数（窗口长度 − 重叠长度）的整数倍。在所有其他情况下，输入帧长度可以是任意的。

模块接受可变大小输入（帧长度在仿真期间变化）。当您输入可变大小信号时，信号的帧长度可以是任意的。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Rst** — 复位端口 标量

以标量形式指定布尔复位信号。如果 **Rst** 端口上的输入为 `true`，模块在处理当前输入之前清除内部直方图和统计量。如果 **Rst** 端口上的输入为 `false`，模块从仿真开始或从上次复位开始计算测量值。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 和 **Reset port** 参数。

**数据类型：** `Boolean`
### 输出

### **Avg** — 平均功率 标量 | 向量 | 矩阵

从仿真开始或从上次复位开始的电压信号的平均功率，以标量、向量或矩阵形式返回。模块沿每个通道以 **Output power units** 参数指定的单位计算平均功率。有关模块如何计算平均功率的详细信息，请参阅 Average Power。

如果您清除 **Compute CCDF** 参数，模块使用 Sliding Window Method 计算滑动平均功率。

有关输出信号维度的详细信息，请参阅此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*-by-*M*，其中 *M* 是跳数（窗口长度 − 重叠长度）的整数倍 | (*P*/跳数)-by-*M* | *P*-by-*M* |
| 固定大小信号 | *P*-by-*M*，其中 *M* 不是跳数（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/跳数)-by-*M*  如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块将报错。 | *P*-by-*M* |
| 可变大小信号 | *P*-by-*M* | `ceil`(*P*/跳数)-by-*M* | *P*-by-*M* |

当输出的上限大小为 `ceil`(*P*/跳数)-by-*M* 时，在仿真期间，第一维的大小在此范围内变化，而第二维的大小保持不变。

如果您选择 **Compute CCDF** 参数，模块沿每个通道计算整个信号的平稳平均功率。在这种情况下，输出的大小为 1-by-*M*，其中 *M* 是输入信号中的通道数（列数）。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Average power` 或 `All`。

**数据类型：** `single` | `double`

### **Peak** — 峰值功率 标量 | 向量 | 矩阵

从仿真开始或从上次复位开始的电压信号的峰值功率，以标量、向量或矩阵形式返回。模块沿每个通道以 **Output power units** 参数指定的单位计算峰值功率。有关模块如何计算峰值功率的详细信息，请参阅 Peak Power。

如果您清除 **Compute CCDF** 参数，模块使用 Sliding Window Method 计算滑动峰值功率。

有关输出信号维度的详细信息，请参阅此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*-by-*M*，其中 *M* 是跳数（窗口长度 − 重叠长度）的整数倍 | (*P*/跳数)-by-*M* | *P*-by-*M* |
| 固定大小信号 | *P*-by-*M*，其中 *M* 不是跳数（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/跳数)-by-*M*  如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块将报错。 | *P*-by-*M* |
| 可变大小信号 | *P*-by-*M* | `ceil`(*P*/跳数)-by-*M* | *P*-by-*M* |

当输出的上限大小为 `ceil`(*P*/跳数)-by-*M* 时，在仿真期间，第一维的大小在此范围内变化，而第二维的大小保持不变。

如果您选择 **Compute CCDF** 参数，模块沿每个通道计算整个信号的平稳峰值功率。在这种情况下，输出的大小为 1-by-*M*，其中 *M* 是输入信号中的通道数（列数）。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Peak power` 或 `All`。

**数据类型：** `single` | `double`

### **PAPR** — 峰均功率比 标量 | 向量 | 矩阵

电压信号的峰值功率与平均功率之比（PAPR），以标量、向量或矩阵形式返回。模块沿每个通道计算峰均功率比。有关模块如何计算此测量值的详细信息，请参阅 Peak-to-Average Power Ratio。

如果您清除 **Compute CCDF** 参数，模块使用 Sliding Window Method 计算滑动峰均功率比。

有关输出信号维度的详细信息，请参阅此表。

| 输入信号 | 输入维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 出现时的输出维度 | 当 **Allow arbitrary frame length for fixed-size input signals** 未出现时的输出维度 |
| --- | --- | --- | --- |
| 固定大小信号 | *P*-by-*M*，其中 *M* 是跳数（窗口长度 − 重叠长度）的整数倍 | (*P*/跳数)-by-*M* | *P*-by-*M* |
| 固定大小信号 | *P*-by-*M*，其中 *M* 不是跳数（窗口长度 − 重叠长度）的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时为 `ceil`(*P*/跳数)-by-*M*  如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，模块将报错。 | *P*-by-*M* |
| 可变大小信号 | *P*-by-*M* | `ceil`(*P*/跳数)-by-*M* | *P*-by-*M* |

当输出的上限大小为 `ceil`(*P*/跳数)-by-*M* 时，在仿真期间，第一维的大小在此范围内变化，而第二维的大小保持不变。

如果您选择 **Compute CCDF** 参数，模块沿每个通道计算整个信号的平稳峰均功率比。在这种情况下，输出的大小为 1-by-*M*，其中 *M* 是输入信号中的通道数（列数）。

PAPR 应小于 100 dB 以获得准确的 CCDF 测量值。如果 PAPR 高于 100 dB，模块仅显示最高的 100 dB 功率水平。

#### 依赖关系

要启用此端口，请将 **Measurement** 设置为 `Peak-to-average power ratio` 或 `All`。

**数据类型：** `single` | `double`

### **RelPwr** — 相对功率 *N*-by-*M* 矩阵

相对功率（高于平均功率的 dB 值），以 *N*-by-*M* 矩阵形式返回，其中：

- *M* 是输入信号中的通道数（列数）。
- 当您将 **CCDF output** 设置为 `Relative power (dB above average power)` 时，*N* 等于您在 **Specify probability (%) for relative power output** 参数中指定的列向量的长度。
- 当您将 **CCDF output** 设置为 `Relative power and probability (whole CCDF curve)` 时，*N* 等于 `ceil`(**Power range (dB)**/**Power resolution (dB)**) + 1。

相对功率是瞬时信号功率以 **Prob** 的概率（以百分比表示）高于平均信号功率的 dB 值。有关模块如何计算相对功率的详细信息，请参阅 Relative Power。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 参数，然后将 **CCDF output** 参数设置为 `Relative power (dB above average power)` 或 `Relative power and probability (whole CCDF curve)`。

**数据类型：** `single` | `double`

### **Prob** — 概率（百分比） *N*-by-*M* 矩阵

概率（百分比），以 *N*-by-*M* 矩阵形式返回，其中：

- *M* 是输入信号中的通道数（列数）。
- 当您将 **CCDF output** 设置为 `Probability (%)` 时，*N* 等于您在 **Specify relative power (dB) for probability output** 参数中指定的列向量的长度。
- 当您将 **CCDF output** 设置为 `Relative power and probability (whole CCDF curve)` 时，*N* 等于 `ceil`(**Power range (dB)**/**Power resolution (dB)**) + 1。

**Prob**(*i*)/100 是第 *j* 个通道的瞬时信号功率以 **RelPwr**(*i*,*j*) dB 高于其平均信号功率的概率。

#### 依赖关系

要启用此端口，请选择 **Compute CCDF** 参数，然后将 **CCDF output** 参数设置为 `Probability (%)` 或 `Relative power and probability (whole CCDF curve)`。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Measurement
  summary: 期望的功率测量值 Average power（默认）| Peak power | Peak-to-average power ratio | All
  group: ''
- name: Reference load (ohms)
  summary: 参考负载（欧姆） 1（默认）| 以欧姆为单位的正标量
  group: ''
- name: Output power units
  summary: 测量功率值的单位 dBm（默认）| dBW | Watts
  group: ''
- name: Compute CCDF
  summary: 启用 CCDF 计算 off（默认）| on
  group: ''
- name: Window length
  summary: 窗口长度 256（默认）| 正整数
  group: ''
- name: Overlap length
  summary: 窗口之间的重叠长度 255（默认）| 非负整数
  group: ''
- name: Allow arbitrary frame length for fixed-size input signals
  summary: 允许固定大小输入信号的任意帧长度 off（默认）| on
  group: ''
- name: Power range (dB)
  summary: 功率范围（dB） 50（默认）| 正标量
  group: ''
- name: Power resolution (dB)
  summary: 功率分辨率（dB） 0.1（默认）| 正标量
  group: ''
- name: CCDF output
  summary: CCDF 输出 Relative power (dB above average power)（默认）| Probability (%) | Relative power and probability (whole CCDF
    curve)
  group: ''
- name: Specify probability (%) for relative power output
  summary: 为相对功率输出指定概率（%） [10;1;0.1;0.01;0.001;0.0001]（默认）| 列向量
  group: ''
- name: Specify relative power (dB) for probability output
  summary: 为概率输出指定相对功率 [0;3;6;9;12]（默认）| 列向量
  group: ''
- name: Reset port
  summary: 启用复位端口 关（默认）| 开
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Measurement** — 期望的功率测量值 `Average power`（默认）| `Peak power` | `Peak-to-average power ratio` | `All`

将期望的功率测量值指定为以下之一：

- `Average power`（默认）
- `Peak power`
- `Peak-to-average power ratio`
- `All`

有关模块如何计算这些测量值的详细信息，请参阅 Algorithms。

### **Reference load (ohms)** — 参考负载（欧姆） `1`（默认）| 以欧姆为单位的正标量

将功率计用于计算功率值的参考负载指定为以欧姆为单位的实数正标量。

**可调：** 是

**数据类型：** `single` | `double`

### **Output power units** — 测量功率值的单位 `dBm`（默认）| `dBW` | `Watts`

将测量功率值的单位指定为以下之一：

- `dBm`
- `dBW`
- `Watts`

### **Compute CCDF** — 启用 CCDF 计算 off（默认）| on

选择 **Compute CCDF** 参数以使模块能够计算电压信号功率的 CCDF。CCDF 测量值包括相对功率和概率（百分比）。相对功率是瞬时信号功率高于平均信号功率的 dB 值。概率（百分比）是指瞬时信号功率以相对功率 dB 值高于平均信号功率的概率。

这些测量值提供了一种定性方式来查看输入信号幅度值随时间的功率分布。CCDF 曲线（概率百分比对相对功率 dB 的图）是信号动态范围的有用指标。

当您选择 **Compute CCDF** 时：

- 模块使用从仿真开始或从 **Rst** 端口上的复位信号开始的所有输入样本计算统计量。功率测量值是平稳的。
- 您可以指定可变大小输入信号。

当您清除 **Compute CCDF** 时，

- 模块不计算 CCDF 测量值，并使用 Sliding Window Method 计算功率测量值。
- 仅当您选择 **Allow arbitrary frame length for fixed-size input signals** 参数时，模块才接受任意帧长度的输入信号。

### **Window length** — 窗口长度 `256`（默认）| 正整数

将模块计算测量值所依据的窗口长度指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 复选框。当您选择 **Compute CCDF** 时，**Window length** 变为 `Inf`。

**数据类型：** `single` | `double`

### **Overlap length** — 窗口之间的重叠长度 `255`（默认）| 非负整数

将滑动窗口之间的重叠长度指定为非负整数。重叠长度的值在 [0, **Window length** − 1] 范围内变化。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 复选框。当您选择 **Compute CCDF** 时，**Overlap length** 变为 `0`。

**数据类型：** `single` | `double`

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 off（默认）| on

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，即帧长度不必是跳数的整数倍。跳数定义为 **Window length** − **Overlap length**。模块仅对固定大小输入信号使用此参数设置，如果输入为可变大小，则忽略此参数。

当输入信号为可变大小信号时，信号可以具有任意帧长度，即帧长度不必是跳数的整数倍。

对于固定大小输入信号，如果您：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，信号的帧长度不必是跳数的整数倍。如果输入不是跳数的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，模块还必须支持可变大小操作，您可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，输入帧长度必须是跳数的整数倍。

#### 依赖关系

要启用此参数，请清除 **Compute CCDF** 参数。

### **Power range (dB)** — 功率范围（dB） `50`（默认）| 正标量

将 CCDF 曲线的 *x* 轴范围指定为以 dB 为单位的正标量。CCDF 曲线结束于最大相对功率，即信号的 PAPR，并起始于 PAPR − **Power range (dB)**。在 Power Meter 模块的 CCDF 功能中，相对功率是瞬时信号功率高于平均信号功率的 dB 值。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

**数据类型：** `single` | `double`

### **Power resolution (dB)** — 功率分辨率（dB） `0.1`（默认）| 正标量

将 CCDF 曲线的 *x* 轴分辨率指定为以 dB 为单位的正标量。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

**数据类型：** `single` | `double`

### **CCDF output** — CCDF 输出 `Relative power (dB above average power)`（默认）| `Probability (%)` | `Relative power and probability (whole CCDF curve)`

指定模块输出：

- **RelPwr** –– 相对功率（高于平均功率的 dB 值）。这是瞬时信号功率高于平均功率的 dB 值。
- **Prob** –– 概率（百分比）。这是瞬时信号功率以相对功率 dB 值高于平均信号功率的概率。
- **RelPwr** 和 **Prob** 两者。

#### 依赖关系

要启用此参数，请选择 **Compute CCDF** 复选框。

### **Specify probability (%) for relative power output** — 为相对功率输出指定概率（%） [`10`;`1`;`0.1`;`0.01`;`0.001`;`0.0001`]（默认）| 列向量

将相对功率输出的概率（百分比）指定为列向量。此向量的长度决定了 **RelPwr** 端口处相对功率输出的行数。

#### 依赖关系

要启用此参数，请选中 **Compute CCDF** 复选框，并将 **CCDF output** 参数设置为 `Relative power
(dB above average power)`。

这也会启用 **RelPwr** 输出端口。

**数据类型：** `single` | `double`

### **Specify relative power (dB) for probability output** — 为概率输出指定相对功率 [`0`;`3`;`6`;`9`;`12`]（默认）| 列向量

以列向量的形式为概率输出指定相对功率（以 dB 为单位）。该向量的长度决定了 **Prob** 端口处概率输出的行数。

#### 依赖关系

要启用此参数，请选中 **Compute CCDF** 复选框，并将 **CCDF output** 参数设置为 `Probability
(%)`。

这也会启用 **Prob** 输出端口。

**数据类型：** `single` | `double`

### **Reset port** — 启用复位端口 关（默认）| 开

选中此参数可启用接受布尔信号的输入端口 **Rst**。如果 **Rst** 端口处的值为 `true`，则模块在处理当前输入之前会清除内部直方图和统计数据。

#### 依赖关系

要启用此参数，请选中 **Compute CCDF** 复选框。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
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

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此变更，模块默认使用 MATLAB 解释器进行仿真。

### R2022b：新增 **Overlap length** 参数

从 R2022b 开始，当模块不计算 CCDF 测量值时，您可以使用 **Overlap length** 参数指定滑动窗口之间的重叠长度。

### R2022b：支持任意输入帧长度

Power Meter 模块在以下情况下支持具有任意帧长度的输入信号：

- 输入信号为固定大小信号（帧长度在仿真期间不变），并且您选中了 **Allow arbitrary frame length for fixed-size input signals** 参数（如果已启用）。
- 输入信号为可变大小信号（帧长度在仿真期间变化）。

当此模块支持任意帧长度输入信号时，输入帧长度不必是跳数大小的整数倍。

## 描述

测量 Simulink 中电压信号的功率和功率的 CCDF

Power Meter 模块计算电压信号的功率测量值。当您选中 **Compute CCDF** 参数时，该模块还会计算电压信号功率的互补累积分布函数（CCDF）。模块输出的 CCDF 测量值为相对功率和概率（以百分比表示）。功率测量值包括平均功率、峰值功率和峰均功率比。

有关模块如何计算功率测量值和 CCDF 测量值的更多详细信息，请参阅算法。
