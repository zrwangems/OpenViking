---
type: simulink-block
title: 'SISO Fading Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'sisofadingchannel'
documentation_source_path: 'ref/sisofadingchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# SISO Fading Channel

## 端口

### 输入

### **in** — 输入数据信号向量

输入数据信号，指定为 *N*S×1 向量。*N*S 表示输入信号中的样本数。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out1** — 衰落信道的输出数据信号向量

衰落信道的输出数据信号，以 *N*S×1 向量形式返回。
*N*S 表示输入信号中的样本数。

### **Gain** — 离散路径增益矩阵

底层衰落过程的离散路径增益，以 *N*S×*N*P 矩阵形式返回。

- *N*S 表示输入信号中的样本数。
- *N*P 表示信道路径数。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选择 **Output channel path gains**。

### **Delay** — 信道滤波器延迟标量

信道滤波器延迟，以标量形式返回。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选择 **Output channel filter delay**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### Main 选项卡

#### 多径参数（频率选择性）

### **Inherit sample rate from input** — 从输入继承采样率的选项 on（默认）| off

选择此参数以在处理时使用输入信号的采样率。当您选择 **Inherit sample rate from input** 时，采样率为 *N*S/*T*S，其中 *N*S 是输入样本数，*T*S 是模型采样时间。

### **Sample rate (Hz)** — 输入信号采样率 `1`（默认）| 正标量

输入信号采样率，以赫兹为单位，指定为正标量。要匹配模型设置，请将采样率设置为 *N*S/*T*S，其中 *N*S 是输入样本数，*T*S 是模型采样时间。

#### 依赖关系

当未选择 **Inherit sample rate from input** 时，此参数出现。

### **Discrete path delays (s)** — 每条离散路径的延迟 `0`（默认）| 非负标量 | 行向量

每条离散路径的延迟，以秒为单位，指定为非负标量或行向量。

- 当您将 **Discrete path delays (s)** 设置为标量时，SISO 信道为频率平坦。
- 当您将 **Discrete path delays (s)** 设置为向量时，SISO 信道为频率选择性。

### **Average path gains (dB)** — 每条离散路径的平均增益 `0`（默认）| 标量 | 行向量

每条离散路径的平均增益，以分贝为单位，指定为标量或行向量。**Average path gains (dB)** 的大小必须与 **Discrete path delays (s)** 相同。

### **Normalize average path gains to 0 dB** — 将平均路径增益归一化到 0 dB 的选项 on（默认）| off

选择此参数以归一化衰落过程，使路径增益的总功率（随时间平均）为 0 dB。

### **Fading distribution** — 信道的衰落分布 `Rayleigh`（默认）| `Rician`

选择信道的衰落分布，可以是 `Rayleigh` 或 `Rician`。

### **K-factors** — Rician 衰落信道的 K 因子 `3`（默认）| 正标量 | 非负值行向量

Rician 衰落信道的 K 因子，指定为正标量或 1×*N*P 非负值向量。*N*P 等于 **Discrete path delays (s)** 参数的值。

- 如果您将 **K-factors** 设置为标量，则第一条离散路径是具有 **K-factors** 的 Rician K 因子的 Rician 衰落过程。任何剩余的离散路径都是独立的 Rayleigh 衰落过程。
- 如果您将 **K-factors** 设置为行向量，则对应于 **K-factors** 向量中正元素的离散路径是具有由该元素指定的 Rician K 因子的 Rician 衰落过程。对应于 **K-factors** 向量中任何零值元素的离散路径是 Rayleigh 衰落过程。至少一个元素值必须非零。

#### 依赖关系

当您将 **Fading distribution** 设置为 `Rician` 时，此参数出现。

### **LOS path Doppler shifts (Hz)** — 视距分量的多普勒频移 `0`（默认）| 标量 | 行向量

Rician 衰落信道视距分量的多普勒频移，以赫兹为单位，指定为标量或行向量。此参数的大小必须与 **K-factors** 相同。

- 如果您将 **LOS path Doppler shifts (Hz)** 设置为标量，它表示第一条作为 Rician 衰落过程的离散路径的视距分量多普勒频移。
- 如果您将 **LOS path Doppler shifts (Hz)** 设置为行向量，则作为 Rician 衰落过程的离散路径的视距分量多普勒频移由 **LOS path Doppler shifts (Hz)** 中对应于 **K-factors** 向量中正元素的元素指定。

#### 依赖关系

当您将 **Fading distribution** 设置为 `Rician` 时，此参数出现。

### **LOS path initial phases (rad)** — 视距分量的初始相位 `0`（默认）| 标量 | 行向量

Rician 衰落信道视距分量的初始相位，以弧度为单位，指定为标量或行向量。此参数的大小必须与 **K-factors** 相同。

- 如果您将 **LOS path initial phases (rad)** 设置为标量，它是第一条作为 Rician 衰落过程的离散路径的视距分量初始相位。
- 如果您将 **LOS path initial phases (rad)** 设置为行向量，则作为 Rician 衰落过程的离散路径的视距分量初始相位由 **LOS path initial phases (rad)** 中对应于 **K-factors** 向量中正元素的元素指定。

#### 依赖关系

当您将 **Fading distribution** 设置为 `Rician` 时，此参数出现。

#### 多普勒参数（时间色散）

### **Maximum Doppler shift (Hz)** — 所有信道路径的最大多普勒频移 `0.001`（默认）| 非负标量

所有信道路径的最大多普勒频移，以赫兹为单位，指定为非负标量。

**Maximum Doppler shift (Hz)** 必须小于或等于每条路径的 (*f*s/10)/*f*c。*f*s 是此模块输入的采样率。*f*c 是路径的截止频率因子。有关详细信息，请参阅 Cutoff Frequency Factor。

### **Doppler spectrum** — 所有信道路径的多普勒频谱形状 `doppler('Jakes')`（默认）| `doppler('Flat')` | `doppler('Rounded', ...)` | `doppler('Bell', ...)` | `doppler('Asymmetric Jakes', ...)` | `doppler('Restricted Jakes', ...)` | `doppler('Gaussian', ...)` | `doppler('BiGaussian', ...)`

所有信道路径的多普勒频谱形状，指定为从 `doppler` 函数返回的单个多普勒频谱结构或此类结构的 1×*N*P 元胞数组。此参数的默认值是 Jakes 多普勒频谱（`doppler('Jakes')`）。

- 如果您分配对 `doppler` 的单个调用，则所有路径具有相同的指定多普勒频谱。
- 如果您使用任何指定语法分配对 `doppler` 的 1×*N*P 元胞数组调用，则每条路径具有由数组中对应的多普勒频谱结构指定的多普勒频谱。在这种情况下，*N*P 等于 **Discrete path delays (s)** 参数的值。

#### 依赖关系

当您将 **Maximum Doppler shift (Hz)** 设置为大于零的值时，此参数适用。

#### 其他参数

### **Initial seed** — 随机数生成器初始种子 `73`（默认）| 非负整数

此模块的随机数生成器初始种子，指定为非负整数。

### **Output channel path gains** — 输出信道路径增益的选项 off（默认）| on

选择此参数以将 **Gain** 输出端口添加到此模块，并输出底层衰落过程的信道路径增益。

### **Output channel filter delay** — 输出信道滤波器延迟的选项 off（默认）| on

选择此参数以将 **Delay** 输出端口添加到此模块，并输出底层衰落过程的信道滤波器延迟。

### **Simulate using** — 编译类型 `Interpreted execution`（默认）| `Code generation`

编译类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但提供比 `Interpreted execution` 更快的仿真速度。

### Visualization 选项卡

### **Channel visualization** — 选择信道可视化 `Off`（默认）| `Impulse response` | `Frequency response` | `Doppler spectrum` | `Impulse and frequency responses`

选择信道可视化：`Off`、`Impulse response`、`Frequency response`、`Doppler spectrum` 或 `Impulse and frequency responses`。当可视化开启时，所选信道特性（如冲激响应或多普勒频谱）显示在单独的窗口中。有关详细信息，请参阅 Channel Visualization。

### **Percentage of samples to display** — 要显示的样本百分比 `25%`（默认）| `10%` | `50%` | `100%`

选择要显示的样本百分比：`10%`、`25%`、`50%` 或 `100%`。增加百分比会提高显示精度，但会降低仿真速度。

#### 依赖关系

当您将 **Channel visualization** 设置为 `Impulse response`、`Frequency response` 或 `Impulse and frequency responses` 时，此参数出现。

### **Path for Doppler spectrum display** — 显示多普勒频谱的路径 `1`（默认）| 正整数

显示多普勒频谱的路径，指定为从 1 到 *N*P 的正整数，其中 *N*P 等于 **Discrete path delays (s)** 参数的值。

#### 依赖关系

当您将 **Channel visualization** 设置为 `Doppler spectrum` 时，此参数出现。

## 所属库

Communications Toolbox / Channels

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2022b：信道可视化显示的更新

信道可视化功能现在提供：

- 绘图窗口底部工具栏中的配置设置。
- 当您选择 `Impulse and frequency response` 信道可视化选项时，在一个窗口中并排显示绘图。

## 描述

通过 SISO 多径衰落信道对输入信号进行滤波

SISO Fading Channel 模块使用单输入/单输出（SISO）多径衰落信道对输入信号进行滤波。此模块对 Rayleigh 和 Rician 衰落进行建模。有关处理详细信息，请参阅算法部分。
