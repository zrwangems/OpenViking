---
type: simulink-block
title: 'AWGN Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'awgnchannel'
documentation_source_path: 'ref/awgnchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# AWGN Channel

## 端口
```yaml
ports:
- name: In
  summary: 输入数据信号 向量 | 矩阵
  direction: input
  data_types: double | single
- name: Var
  summary: 加性高斯白噪声的方差 正标量 | 向量
  direction: input
  data_types: double
- name: Out
  summary: 输出数据信号 向量 | 矩阵
  direction: output
```

### 输入

### **In** — 输入数据信号 向量 | 矩阵

输入数据信号，指定为 *N*S×1 向量或 *N*S×*N*C 矩阵。*N*S 表示输入信号中的样本数。*N*C 表示信道数，由输入信号矩阵的列数确定。*N*S 和 *N*C 均可等于 `1`。

该模块将长度为 *N*S 的高斯噪声帧添加到 *N*C 个信道中的每一个，每个信道使用不同的随机分布。

在添加 **Var** 端口之前，该端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### **Var** — 加性高斯白噪声的方差 正标量 | 向量

加性高斯白噪声的方差，指定为正标量或 1×*N*C 向量。*N*C 表示信道数，由输入信号矩阵的列数确定。有关详细信息，请参阅直接或间接指定方差。

#### 依赖关系

要启用此端口，请将 **Mode** 设置为 `Variance`，并将 **Noise variance source** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Out** — 输出数据信号 向量 | 矩阵

AWGN 信道的输出数据信号，以向量或矩阵形式返回。**Out** 的数据类型和维度与输入信号 **In** 匹配。该端口在模块上未命名。
## 参数
```yaml
parameters:
- name: Mode
  summary: 方差模式 Signal to noise ratio (SNR)（默认）| Signal to noise ratio (Eb/No) | Signal to noise ratio (Es/No) | Variance
  group: ''
- name: SNR (dB)
  summary: 信号功率与噪声功率之比 10（默认）| 标量 | 向量
  group: ''
- name: Eb/No (dB)
  summary: 每符号信息比特能量与噪声功率谱密度之比 10（默认）| 标量 | 向量
  group: ''
- name: Es/No (dB)
  summary: 每符号信息符号能量与噪声功率谱密度之比 10（默认）| 标量 | 向量
  group: ''
- name: Number of bits per symbol
  summary: 每个输入符号中的比特数 1（默认）| 标量 | 向量
  group: ''
- name: Input signal power, referenced to 1 ohm (watts)
  summary: 输入的均方功率 1（默认）| 标量 | 向量
  group: ''
- name: Specify symbol duration in seconds
  summary: 以秒为单位指定符号持续时间 off（默认）| on
  group: ''
- name: Samples per symbol
  summary: 每符号样本数 1（默认）| 正整数 | 正整数向量
  group: ''
- name: Symbol period (s)
  summary: 符号周期，以秒为单位 [1 2 4]（默认）| 正标量 | 向量
  group: ''
- name: Noise variance source
  summary: 噪声方差来源 Parameter（默认）| Input port
  group: ''
- name: Noise variance
  summary: 白高斯噪声的方差 1（默认）| 标量 | 向量
  group: ''
- name: Random number source
  summary: 随机数来源 Global stream（默认）| mt19937ar with seed
  group: ''
- name: Initial seed
  summary: 噪声发生器初始种子 67（默认）| 非负整数
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Mode** — 方差模式 `Signal to noise ratio (SNR)`（默认）| `Signal to noise ratio (Eb/No)` | `Signal to noise ratio (Es/No)` | `Variance`

方差模式，指定为 `Signal to noise ratio (Eb/No)`、`Signal to noise ratio (Es/No)`、`Signal to noise ratio (SNR)` 或 `Variance`。有关详细信息，请参阅 Eb/No、Es/No 和 SNR 模式之间的关系以及直接或间接指定方差。

### **SNR (dB)** — 信号功率与噪声功率之比 `10`（默认）| 标量 | 向量

信号功率与噪声功率之比，以分贝为单位，指定为标量或向量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (SNR)`。

### **Eb/No (dB)** — 每符号信息比特能量与噪声功率谱密度之比 `10`（默认）| 标量 | 向量

每符号信息比特能量与噪声功率谱密度之比，以分贝为单位，指定为标量或向量。信息比特能量是未经信道编码的幅度。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)`。

### **Es/No (dB)** — 每符号信息符号能量与噪声功率谱密度之比 `10`（默认）| 标量 | 向量

每符号信息符号能量与噪声功率谱密度之比，以分贝为单位，指定为标量或向量。信息符号能量是未经信道编码的幅度。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Es/No)`。

### **Number of bits per symbol** — 每个输入符号中的比特数 1（默认）| 标量 | 向量

每个输入符号中的比特数，指定为标量或向量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)`。

### **Input signal power, referenced to 1 ohm (watts)** — 输入的均方功率 `1`（默认）| 标量 | 向量

输入的均方功率，以瓦特为单位，指定为标量或向量。

- 当 **Mode** 为 `Signal to noise ratio (Eb/No)` 或 `Signal to noise ratio (Es/No)` 时，该参数为输入符号的均方功率。
- 当 **Mode** 为 `Signal to noise ratio (SNR)` 时，该参数为输入样本的均方功率。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)`、`Signal to noise ratio (Es/No)` 或 `Signal to noise ratio (SNR)`。

### **Specify symbol duration in seconds** — 以秒为单位指定符号持续时间 `off`（默认）| `on`

选择此参数以以秒为单位指定符号持续时间。

- 选择此参数时，设置 **Symbol period (s)** 参数以以秒为单位指定符号周期。
- 未选择此参数时，设置 **Samples per symbol** 参数以以样本为单位指定每符号样本数。

该模块在模型运行时确定采样时间和要添加的适当噪声。

有关详细信息，请参阅 Eb/No、Es/No 和 SNR 模式之间的关系。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)` 或 `Signal to noise ratio (Es/No)`。

### **Samples per symbol** — 每符号样本数 `1`（默认）| 正整数 | 正整数向量

每符号样本数，以样本为单位，指定为正整数标量或向量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)` 或 `Signal to noise ratio (Es/No)`，并且不要选择 **Specify symbol duration in seconds**。

### **Symbol period (s)** — 符号周期，以秒为单位 `[1 2 4]`（默认）| 正标量 | 向量

符号周期，以秒为单位，指定为正标量或向量。使用此参数时，该模块在模型运行时确定采样时间和要添加的适当噪声。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Signal to noise ratio (Eb/No)` 或 `Signal to noise ratio (Es/No)`，并选择 **Specify symbol duration in seconds**。

### **Noise variance source** — 噪声方差来源 `Parameter`（默认）| `Input port`

噪声方差来源，指定为 `Parameter` 或 `Input port`。有关详细信息，请参阅直接或间接指定方差。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Variance`。

### **Noise variance** — 白高斯噪声的方差 `1`（默认）| 标量 | 向量

白高斯噪声的方差，指定为标量或向量。有关详细信息，请参阅直接或间接指定方差。

**可调：** 是

#### 依赖关系

要启用此端口，请将 **Mode** 设置为 `Variance`，并将 **Noise variance source** 设置为 `Parameter`。

#### 随机化

### **Random number source** — 随机数来源 `Global stream`（默认）| `mt19937ar with seed`

随机数来源，指定为 `Global stream` 或 `mt19937ar with seed`。如果使用 `parsim` (Simulink) 函数，请参阅提示。

### **Initial seed** — 噪声发生器初始种子 `67`（默认）| 非负整数

mt19937ar 算法的噪声发生器初始种子，指定为非负整数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Random number source** 设置为 `mt19937ar with seed`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
## 所属库

Communications Toolbox / Channels

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2025a：以秒为单位指定符号持续时间

在 R2025a 中，此模块添加了 **Specify symbol duration in seconds** 参数。当您选择 **Specify symbol duration in seconds** 时，您需要指定 **Symbol period (s)** 参数值。该模块在模型运行时确定采样时间和要添加的适当噪声。有关详细信息，请参阅直接或间接指定方差。

### R2023b：方差计算更新

在 R2023b 中，使用 Upgrade Advisor (Simulink) 更新 R2023a 之前模型中的 AWGN Channel 模块实例。除了 R2023a 的更新之外，对于此配置还会发生以下 AWGN Channel 模块更新：

- 如果 **Mode** 参数设置为 `Signal to noise ratio (Eb/No)` 或 `Signal to noise ratio (Es/No)`，并且 **Symbol period (s)** 与模块采样时间一起导致非整数每符号样本数，则在升级后的模块中 **Mode** 会设置为 `Signal to noise ratio (SNR)`。
- **SNR (db)** 参数会设置为适当的 SNR 设置。

在 R2023a 中，如果 **Symbol period (s)** 参数值与模块采样时间的组合导致非整数每符号样本数，则使用 Upgrade Advisor (Simulink) 更新 AWGN Channel 模块会生成方差值不正确的噪声。

如果您已在 R2023a 中更新了模块：

1. 在模型中选择 AWGN Channel 模块。
2. 在命令行运行 `set_param(gcb,'LegacyMode','on')` 以还原更新。
3. 重新运行 Upgrade Advisor。

### R2023a：可变大小支持

此支持使您能够在仿真中每次模块执行时改变输入信号的长度。

### R2023a：随机数生成器更新

AWGN Channel 模块更新了随机数生成器 (RNG) 来源，允许选择 `Global stream` 或 `mt19937ar with seed`。

新的 RNG 提供更好的随机数统计特性。对于 R2023a 之前创建的仿真，该模块默认使用旧模式，采用先前的 RNG（Ziggurat 方法 - V5 RANDN 算法）。在此模式下，该模块使用 Random Source 模块生成噪声。随机数使用 Ziggurat 方法（V5 RANDN 算法）生成。每次重新运行仿真时，该模块都会重用相同的初始种子，因此每次运行仿真时该模块输出相同的信号。为了改善统计特性，建议对使用 AWGN Channel 模块的 R2023a 之前的仿真运行 **Update Model**。

### R2023a：代码生成

代码生成默认启用。有关详细信息，请参阅 **Simulate using**。

## 描述

向输入信号添加白高斯噪声

AWGN Channel 模块向输入信号添加白高斯噪声。它从输入信号继承采样时间。
