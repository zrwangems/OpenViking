---
type: simulink-block
title: 'MIMO Fading Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'mimofadingchannel'
documentation_source_path: 'ref/mimofadingchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# MIMO Fading Channel

## 端口

### 输入

### **in** — 输入数据信号向量

输入数据信号，指定为
*N*S×*N*T
或
*N*S×*N*ST
矩阵。

- *N*S 表示输入信号中的样本数。
- *N*T 表示发射天线数。
- *N*ST 表示选定的发射天线数。

当您将 **Antenna selection** 参数设置为 `Off` 时，此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### **Tx Sel** — 选择活动发射天线的二进制向量

选择活动发射天线，指定为
1×*N*T 二进制向量。
*N*T 表示发射天线数。
设置为 `1` 的元素标识选定的天线索引，
`0` 标识未选定的天线索引。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上将 **Antenna selection**
设置为 `Tx` 或 `Tx and Rx`。

**数据类型：** `double`

### **Rx Sel** — 选择活动接收天线的二进制向量

选择活动接收天线，指定为
1×*N*R 二进制向量。
*N*R 表示接收天线数。
设置为 `1` 的元素标识选定的天线索引，
`0` 标识未选定的天线索引。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上将 **Antenna selection**
设置为 `Rx` 或 `Tx and Rx`。

**数据类型：** `double`

### **Init Time** — 初始时间偏移 非负标量

衰落模型的初始时间偏移，以秒为单位，指定为非负标量。

**Init Time** 必须大于最后一帧的结束时间。当
**Init Time** 不是 `1`/**Sample Rate (Hz)** 的整数倍时，
它会被向上舍入到最近的样本位置。

#### 依赖关系

要启用此端口，请在 **Realization** 选项卡上将 **Initial time
source** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Out** — 衰落信道的输出数据信号 向量

衰落信道的输出数据信号，返回为
*N*S×*N*R
或
*N*S×*N*SR
矩阵。

- *N*S 表示输入信号中的样本数。
- *N*R 表示接收天线数。
- *N*SR 表示选定的接收天线数。

此端口在模块上未命名。

### **Gain** — 离散路径增益 4 维数组

底层衰落过程的离散路径增益，返回为
*N*S×*N*P×*N*T×*N*R 数组。

- *N*S 表示输入信号中的样本数。
- *N*P 表示信道路径数。
- *N*T 表示发射天线数。
- *N*R 表示接收天线数。

未选定路径的条目用 `NaN` 填充。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上选择 **Output channel path
gains**。

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### Main 选项卡

#### 多径参数（频率选择性）

### **Inherit sample rate from input** — 从输入继承采样率的选项 开（默认）| 关

选择此参数以在处理时使用输入信号的采样率。当
您选择 **Inherit sample rate from input** 时，采样率为
*N*S/*T*S。
*N*S 是输入样本数，*T*S 是模型采样时间。

### **Sample rate (Hz)** — 输入信号采样率 `1`（默认）| 正标量

输入信号采样率，以赫兹为单位指定为正标量。要匹配模型
设置，请将采样率设置为
*N*S/*T*S，
其中 *N*S 是输入样本数，*T*S 是模型采样时间。

#### 依赖关系

当未选择 **Inherit sample rate from
input** 时，此参数出现。

### **Discrete path delays (s)** — 每条离散路径的延迟 `0`（默认）| 非负标量 | 行向量

每条离散路径的延迟，以秒为单位，指定为非负标量或行向量。

- 当您将 **Discrete path delays (s)** 设置为标量时，MIMO
  信道是频率平坦的。
- 当您将 **Discrete path delays (s)** 设置为向量时，MIMO
  信道是频率选择性的。

### **Average path gains (dB)** — 每条离散路径的平均增益 `0`（默认）| 标量 | 行向量

每条离散路径的平均增益，以分贝为单位，指定为标量或行向量。
**Average path gains (dB)** 必须与 **Discrete path delays
(s)** 具有相同的大小。

### **Normalize average path gains to 0 dB** — 将平均路径增益归一化到 0 dB 的选项 开（默认）| 关

选择此参数以归一化衰落过程，使得路径增益的总功率（随时间平均）为 0 dB。

### **Fading distribution** — 信道的衰落分布 `Rayleigh`（默认）| `Rician`

选择信道的衰落分布，可以是
`Rayleigh` 或 `Rician`。

### **K-factors** — Rician 衰落信道的 K 因子 `3`（默认）| 正标量 | 非负值行向量

Rician 衰落信道的 K 因子，指定为正标量或
1×*N*P 非负值向量。
*N*P 等于 **Discrete path delays
(s)** 参数的值。

- 如果您将 **K-factors** 设置为标量，则第一条离散路径是具有 Rician K 因子 **K-factors** 的
  Rician 衰落过程。任何剩余的离散路径是独立的 Rayleigh 衰落过程。
- 如果您将 **K-factors** 设置为行向量，则对应于 **K-factors** 向量中正元素的离散路径是具有由该元素指定的 Rician K 因子的
  Rician 衰落过程。对应于 **K-factors** 向量中任何零值元素的离散路径
  是 Rayleigh 衰落过程。至少一个元素值必须非零。

#### 依赖关系

当您将 **Fading
distribution** 设置为 `Rician` 时，此参数出现。

### **LOS path Doppler shifts (Hz)** — 视距分量的多普勒频移 `0`（默认）| 标量 | 行向量

Rician 衰落信道视距分量的多普勒频移，以赫兹为单位，
指定为标量或行向量。此参数必须与 **K-factors** 具有相同的大小。

- 如果您将 **LOS path Doppler shifts (Hz)** 设置为标量，它
  表示第一条作为 Rician 衰落过程的离散路径的视距分量多普勒频移。
- 如果您将 **LOS path Doppler shifts (Hz)** 设置为行向量，则
  作为 Rician 衰落过程的离散路径的视距分量多普勒
  频移由 **LOS path Doppler shifts (Hz)** 中对应于 **K-factors**
  向量中正元素的元素指定。

#### 依赖关系

当您将 **Fading
distribution** 设置为 `Rician` 时，此参数出现。

### **LOS path initial phases (rad)** — 视距分量的初始相位 `0`（默认）| 标量 | 行向量

Rician 衰落信道视距分量的初始相位，以弧度为单位，
指定为标量或行向量。此参数必须与 **K-factors** 具有相同的大小。

- 如果您将 **LOS path initial phases (rad)** 设置为标量，它是
  第一条作为 Rician 衰落过程的离散路径的视距分量初始相位。
- 如果您将 **LOS path initial phases (rad)** 设置为行向量，则
  作为 Rician 衰落过程的离散路径的视距分量初始
  相位由 **LOS path initial phases (rad)** 中对应于 **K-factors**
  向量中正元素的元素指定。

#### 依赖关系

当您将 **Fading
distribution** 设置为 `Rician` 时，此参数出现。

#### 多普勒参数（时间色散）

### **Maximum Doppler shift (Hz)** — 所有信道路径的最大多普勒频移 `0.001`（默认）| 非负标量

所有信道路径的最大多普勒频移，以赫兹为单位，指定为非负
标量。

**Maximum Doppler shift (Hz)** 必须小于或等于
(**Sample Rate
(Hz)**/10)/*f*c（对于每条路径），其中
*f*c 是该路径的截止频率因子。有关
更多信息，请参阅 Cutoff Frequency Factor。

### **Doppler spectrum** — 所有信道路径的多普勒频谱形状 `doppler('Jakes')`（默认）| `doppler('Flat')` | `doppler('Rounded', ...)` | `doppler('Bell', ...)` | `doppler('Asymmetric Jakes', ...)` | `doppler('Restricted Jakes', ...)` | `doppler('Gaussian', ...)` | `doppler('BiGaussian', ...)`

所有信道路径的多普勒频谱形状，指定为由 `doppler` 函数返回的单个多普勒频谱
结构体，或此类结构体的
1×*N*P 元胞数组。此参数的默认
值是 Jakes 多普勒频谱（`doppler('Jakes')`）。

- 如果您分配对 `doppler` 的单个调用，所有路径具有相同的指定多普勒频谱。
- 如果您使用任何指定语法分配对 `doppler` 的
  1×*N*P 元胞数组调用，
  每条路径具有由数组中对应的多普勒频谱
  结构体指定的多普勒频谱。在这种情况下，*N*P 等于
  **Discrete path delays
  (s)** 参数的值。

#### 依赖关系

当 **Maximum Doppler shift
(Hz)** 大于零时，此参数适用。

如果您将 **Technique for generating
fading samples** 设置为 `Sum of sinusoids`，则 **Doppler spectrum**
必须为 `doppler('Jakes')`。

#### 天线参数（空间色散）

### **Specify spatial correlation** — 空间相关模式 `None`（默认）| `Separate Tx Rx` | `Combined`

选择空间相关模式：`None`、
`Separate Tx Rx` 或 `Combined`。

- 选择 `'None'` 以指定发射和接收
  天线数。
- 选择 `'Spatial Tx Rx'` 以分别指定发射和接收空间
  相关矩阵。发射
  (*N*T) 和接收
  (*N*R) 天线数分别从 **Transmit spatial
  correlation** 和 **Receive spatial
  correlation** 参数的维度
  导出。
- 选择 `'Combined'` 以指定整个信道的单个相关矩阵。
  *N*T 和
  *N*R 的乘积从 **Combined spatial
  correlation** 的维度导出。

### **Number of transmit antennas** — 发射天线数 `2`（默认）| 正整数

发射天线数，指定为正整数。

#### 依赖关系

当您将 **Specify spatial
correlation** 设置为 `None` 或 `Combined` 时，此参数出现。

### **Number of receive antennas** — 接收天线数 `2`（默认）| 正整数

接收天线数，指定为正整数。

#### 依赖关系

当您将 **Specify spatial
correlation** 设置为 `None` 时，此参数出现。

### **Transmit spatial correlation** — 发射机的空间相关性 `[1 0; 0 1]`（默认）| 矩阵 | 3 维数组

将发射机的空间相关性指定为
*N*T×*N*T
矩阵或
*N*T×*N*T×*N*P
复数或实数数组。*N*T 是发射
天线数，*N*P 等于
**Discrete path delays
(s)** 参数的值。

- 如果您将 **Discrete path delays (s)** 设置为标量，信道
  是频率平坦的，**Transmit spatial correlation** 是
  *N*T×*N*T
  埃尔米特矩阵。任何非对角元素的幅度不得大于两个对应对角元素的
  几何平均值。
- 如果您将 **Discrete path delays (s)** 设置为向量，信道
  是频率选择性的，您可以将 **Transmit spatial
  correlation** 指定为矩阵。每条路径具有相同的发射空间相关
  矩阵。
- 或者，您可以将 **Transmit spatial correlation** 指定为
  *N*T×*N*T×*N*P
  数组，其中每条路径可以有自己的不同发射空间相关
  矩阵。

#### 依赖关系

当您将 **Specify spatial
correlation** 设置为 `Separate Tx Rx` 时，此参数出现。

### **Receive spatial correlation** — 接收机的空间相关性 `[1 0; 0 1]`（默认）| 矩阵 | 3 维数组

将接收机的空间相关性指定为
*N*R×*N*R
矩阵或
*N*R×*N*R×*N*P
复数或实数数组。*N*R 是接收
天线数，*N*P 等于
**Discrete path delays
(s)** 参数的值。

- 如果您将 **Discrete path delays (s)** 设置为标量，信道
  是频率平坦的，**Receive spatial correlation** 是
  *N*R×*N*R
  埃尔米特矩阵。任何非对角元素的幅度不得大于两个对应对角元素的
  几何平均值。
- 如果您将 **Discrete path delays (s)** 设置为向量，信道
  是频率选择性的，您可以将 **Receive spatial
  correlation** 指定为矩阵。每条路径具有相同的接收空间相关
  矩阵。
- 或者，您可以将 **Receive spatial correlation** 指定为
  *N*R×*N*R×*N*P
  数组，其中每条路径可以有自己的不同接收空间相关
  矩阵。

#### 依赖关系

当您将 **Specify spatial
correlation** 设置为 `Separate Tx Rx` 时，此参数出现。

### **Combined spatial correlation** — 组合空间相关矩阵 `[1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]`（默认）| 矩阵 | 3 维数组

将组合空间相关矩阵指定为
*N*TR×*N*TR
矩阵或
*N*TR×*N*TR×*N*P
复数或实数数组。*N*TR =
(*N*T ✕
*N*R)，*N*P 等于由
**Discrete path delays
(s)** 参数指定的延迟路径数。

- 如果您将 **Discrete path delays
  (s)** 设置为标量，信道是频率平坦的，**Combined
  spatial correlation** 是
  *N*TR×*N*TR
  埃尔米特矩阵。任何非对角元素的幅度不得大于两个对应对角元素的
  几何平均值。
- 如果您将 **Discrete path delays
  (s)** 设置为向量，信道是频率选择性的，您可以将
  **Combined spatial correlation** 指定为矩阵。每条路径具有相同的
  空间相关矩阵。
- 或者，您可以将 **Combined spatial correlation** 指定为
  *N*TR×*N*TR×*N*P
  数组，其中每条路径可以有自己的不同组合空间相关
  矩阵。

#### 依赖关系

当您将 **Specify spatial
correlation** 设置为 `Combined` 时，此参数出现。

### **Normalize outputs by number of receive antennas** — 归一化信道输出 开（默认）| 关

选择此参数以按接收天线数归一化信道输出。

### **Simulate using** — 编译类型 `Interpreted execution`（默认）| `Code generation`

编译类型，指定为 `Interpreted execution` 或
`Code generation`。

### **Antenna selection scheme** — 天线选择方案 `Off`（默认）| `Tx` | `Rx` | `Tx and Rx`

天线选择方案，指定为 `Off`、
`Tx`、`Rx` 或 `Tx and
Rx`。您选择的天线模式对应于模块上的附加输入端口。此表显示了根据此
参数的设置添加到模块掩码的端口。

| **Antenna selection scheme** 设置 | 添加的输入端口 |
| --- | --- |
| `Off` | 无 |
| `Tx` | **Tx Sel** |
| `Rx` | **Rx Sel** |
| `Tx and Rx` | **Tx Sel**、**Rx Sel** |

### Realization 选项卡

### **Technique for generating fading samples** — 信道建模技术 `Filtered Gaussian noise`（默认）| `Sum of sinusoids`

选择信道建模技术，可以是 `Filtered Gaussian
noise` 或 `Sum of sinusoids`。

### **Number of sinusoids** — 使用的正弦波数量 `48`（默认）| 正整数

用于建模衰落过程的正弦波数量，指定为正整数。

#### 依赖关系

当您将 **Technique for generating
fading samples** 设置为 `Sum of sinusoids` 时，此参数出现。

### **Initial time source** — 初始时间偏移的来源 `Property`（默认）| `Input port`

指示衰落模型初始时间偏移的来源，可以是 `Property` 或 `Input port`。

- 当您将 **Initial time source** 设置为 `Property` 时，使用 **Initial time (s)** 设置初始时间偏移。
- 当您将 **Initial time source** 设置为 `Input port` 时，使用输入端口 **Init Time** 设置初始时间偏移。

#### 依赖关系

当您将 **Technique for generating fading samples** 设置为 `Sum of sinusoids` 时，此参数出现。

### **Initial time (s)** — 初始时间偏移 `0`（默认）| 非负标量

衰落模型的初始时间偏移，指定为非负标量。

当 **Initial time (s)** 不是 `1/`**Sample Rate (Hz)** 的整数倍时，它会被向上舍入到最近的采样位置。

#### 依赖关系

当您将 **Technique for generating fading samples** 设置为 `Sum of sinusoids` 并将 **Initial time source** 设置为 `Property` 时，此参数出现。

### **Initial seed** — 随机数生成器初始种子 `73`（默认）| 非负整数

此模块的随机数生成器初始种子，指定为非负整数。

### **Output channel path gains** — 输出信道路径增益的选项 off（默认）| on

选择此参数可向模块添加 **Gain** 输出端口，并输出底层衰落过程的信道路径增益。

### Visualization Tab

### **Channel visualization** — 选择信道可视化 `Off`（默认）| `Impulse response` | `Frequency response` | `Doppler spectrum` | `Impulse and frequency responses`

选择信道可视化：`Off`、`Impulse response`、`Frequency response`、`Doppler spectrum` 或 `Impulse and frequency responses`。当可视化开启时，所选信道特性（如冲激响应或多普勒频谱）会显示在单独的窗口中。有关详细信息，请参阅 Channel Visualization。

### **Antenna pair to display** — 要显示的发射-接收天线对 `[1,1]`（默认）| 向量

要显示的发射-接收天线对，指定为 1×2 向量，其中第一个元素对应所需的发射天线，第二个元素对应所需的接收天线。目前只能显示单一天线对。

#### 依赖关系

当 `Channel visualization` 不为 `Off` 时，此参数出现。

### **Percentage of samples to display** — 要显示的样本百分比 `25%`（默认）| `10%` | `50%` | `100%`

选择要显示的样本百分比：`10%`、`25%`、`50%` 或 `100%`。增加百分比可提高显示精度，但会降低仿真速度。

#### 依赖关系

当您将 **Channel visualization** 设置为 `Impulse response`、`Frequency response` 或 `Impulse and frequency responses` 时，此参数出现。

### **Path for Doppler spectrum display** — 显示多普勒频谱的路径 `1`（默认）| 正整数

显示多普勒频谱的路径，指定为从 1 到 *N*P 的正整数，其中 *N*P 等于 **Discrete path delays (s)** 参数的值。

#### 依赖关系

当您将 **Channel visualization** 设置为 `Doppler spectrum` 时，此参数出现。

## 所属库

Communications Toolbox / Channels Communications Toolbox / MIMO

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2022b：信道可视化显示的更新

信道可视化功能现在提供：

- 配置设置位于绘图窗口的底部工具栏中。
- 当您选择 `Impulse and frequency response` 信道可视化选项时，绘图并排显示在一个窗口中。

## 描述

通过 MIMO 多径衰落信道对输入信号进行滤波

MIMO Fading Channel 模块使用多输入/多输出（MIMO）多径衰落信道对输入信号进行滤波。此模块对 Rayleigh 和 Rician 衰落进行建模，并采用 Kronecker 模型对链路之间的空间相关性进行建模。有关处理详细信息，请参阅 Algorithms 部分。

### 信号维度

输入和输出端口信号的可用性和维度取决于：

- **Main** 选项卡上的 **Antenna selection** 参数设置
- **Realization** 选项卡上的 **Initial time source** 参数设置
- **Realization** 选项卡上的 **Output channel path gains** 选择

| 天线选择参数 | 信号输入（**in**） | 发射选择输入（**Tx Sel**） | 接收选择输入（**Rx Sel**） | 初始时间偏移输入（**Init Time**） | 信号输出（**Out1**） | 可选信道增益输出（**Gain**） |
| --- | --- | --- | --- | --- | --- | --- |
| `Off` | *N*S-by-*N*T | N/A | N/A | 非负标量 | *N*S-by-*N*R | *N*S-by-*N*P-by-*N*T-by-*N*R |
| `Tx` | *N*S-by-*N*ST | 1-by-*N*T | N/A | *N*S-by-*N*R |
| `Rx` | *N*S-by-*N*T | N/A | 1-by-*N*R | *N*S-by-*N*SR |
| `Tx and Rx` | *N*S-by-*N*ST | 1-by-*N*T | 1-by-*N*R | *N*S-by-*N*SR |

- *N*S 表示输入信号中的样本数。
- *N*T 表示发射天线数，由以下各项确定：

  - 当您将 **Specify spatial correlation** 设置为 `Separate Tx Rx` 时的 **Transmit spatial correlation**
  - 当您将 **Specify spatial correlation** 设置为 `None` 或 `Combined` 时的 **Number of transmit antennas**
- *N*R 表示接收天线数，由以下各项确定：

  - 当您将 **Specify spatial correlation** 设置为 `Separate Tx Rx` 时的 **Receive spatial correlation**
  - 当您将 **Specify spatial correlation** 设置为 `None` 时的 **Number of receive antennas**
  - 当您将 **Specify spatial correlation** 设置为 `Combined` 时的 **Combined spatial correlation** 和 **Number of transmit antennas**
- *N*P 表示信道路径数，由 **Discrete path delays (s)** 或 **Average path gains (dB)** 确定。
- *N*ST 表示所选发射天线数，由提供给 **Tx Sel** 输入端口的向量中设置为 `1` 的元素数量确定。
- *N*SR 表示所选接收天线数，由提供给 **Rx Sel** 输入端口的向量中设置为 `1` 的元素数量确定。
