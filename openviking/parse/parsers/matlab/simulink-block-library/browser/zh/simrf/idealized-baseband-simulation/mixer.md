---
type: simulink-block
title: 'Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'mixeridealizedbaseband'
documentation_source_path: 'ref/mixeridealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Mixer

## 端口

### 输入

### **Port\_1** — 时变输入信号 实标量 | 实列 | 复标量 | 复列

时变输入信号，指定为实标量、实列、复标量或复列。列表示连续时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 时变输出信号 复标量 | 复列

时变输出信号，返回为复标量或复列。输出时变信号的大小等于输入时变信号的大小。

**数据类型：** `double` | `single`

## 参数

### Main 选项卡

### **Mixer type** — 混频器类型 `mod` (默认) | `demod` | `iqmod` | `iqdemod`

Mixer 模块中可用的混频器，指定为以下之一：

- `mod` — 调制器
- `demod` — 解调器
- `iqmod` — IQ 调制器
- `iqdemod` — IQ 解调器

有关详细信息，请参阅 Mixer 架构和设计方程。

### **Sideband** — 混频器的边带 `upper` (默认) | `lower`

混频器的边带，指定为以下之一：

- `lower`
- `upper`

有关详细信息，请参阅 Mixer 边带。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `mod`。

### **RF (Hz)** — RF 载波频率 `1e9` (默认) | 实数

*自 R2024b 起*

混频器模型的 RF 载波频率，指定为以 Hz 为单位的实数。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `mod`、`demod`、`iqdemod`。

### **LO (Hz)** — 本振频率 `1e8` (默认) | 实数

*自 R2024b 起*

混频器模型的本振频率，指定为以 Hz 为单位的实数。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `mod`、`demod`、`iqmod`。

### **Gain (dB)** — 混频器的转换增益 `0` (默认) | 实数

混频器模型的转换增益，指定为以 dB 为单位的实数。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

要运行的仿真类型，指定为以下之一：

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比 `Code generation` 更慢。在此模式下，您可以调试模块的源代码。

### Impairments 选项卡

### **LO phase offset (deg)** — LO 相位偏移 `0` (默认) | 实数

LO 相位偏移，指定为以 deg 为单位的实数。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `mod` 或 `demod`。

### **I/Q gain imbalance (dB)** — IQ 增益不平衡 `0` (默认) | 非负实数

IQ 增益不平衡，指定为以 dB 为单位的非负实数。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `iqmod` 或 `iqdemod`。

### **I/Q phase imbalance (deg)** — IQ 相位不平衡 `0` (默认) | 实数

IQ 相位不平衡，指定为以 deg 为单位的实数。

#### 依赖关系

要启用此参数，请将 **Mixer type** 设置为 `iqmod` 或 `iqdemod`。

### **Non-Linearity** — 三阶非线性类型 `OIP3` (默认) | `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

三次多项式模型中的三阶非线性类型，指定为 `IIP3`、`OIP3`、`IP1dB`、`OP1dB`、`IPsat` 或 `OPsat`。

有关详细信息，请参阅 Idealized Baseband Mixer 模块中的非线性。

### **IIP3 (dBm)** — 输入三阶截点 `Inf` (默认) | 正实数

输入三阶截点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `IIP3`。

### **OIP3 (dBm)** — 输出三阶截点 `Inf` (默认) | 正实数

输出三阶截点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `OIP3`。

### **IP1dB (dBm)** — 输入 1 dB 压缩点 `Inf` (默认) | 正实数

输入 1 dB 压缩点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `IP1dB`。

### **OP1dB (dBm)** — 输出 1 dB 压缩点 `Inf` (默认) | 正实数

输出 1 dB 压缩点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `OP1dB`。

### **IPsat (dBm)** — 输入饱和点 `Inf` (默认) | 正实数

输入饱和点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `IPsat`。

### **OPsat (dBm)** — 输出饱和点 `Inf` (默认) | 正实数

输出饱和点，指定为以 dBm 为单位的正实数。

#### 依赖关系

要启用此参数，请将 **Type of Non-Linearity** 设置为 `OPsat`。

### **Plot power characteristics** — 绘制功率特性按钮

此按钮根据您在 **Main** 选项卡的 Gain (dB) 参数中指定的值以及 **Impairments** 选项卡中的 Non-Linearity 绘制功率特性。绘制功率特性时，模块会忽略所有其他损伤值。

有关详细信息，请参阅绘制功率特性。

### Noise 选项卡

### **Include mixer noise** — 向系统添加混频器噪声 `off` (默认) | `on`

选择此参数可向输入信号添加混频器噪声。选择此参数后，将显示与 **Include mixer noise** 关联的参数，并且模块图标中的混频器组件会显示为灰色。

有关详细信息，请参阅 Mixer (System) 噪声仿真。

### **Mixer noise type** — 噪声表示形式 `NF` (默认) | `noise-temperature` | `noise-factor`

噪声类型，指定为以下之一：

- `noise-temperature` — 噪声温度
- `NF` — 噪声系数
- `noise-factor` — 噪声因数

有关详细信息，请参阅 Mixer (System) 噪声仿真。

#### 依赖关系

要启用此参数，请选择 **Include mixer noise**。

### **Noise temperature (K)** — 用于对混频器噪声建模的噪声温度 `290` (默认) | 非负实数

用于对混频器噪声建模的噪声温度，指定为以 K 为单位的非负实数。

#### 依赖关系

要启用此参数，请选择 **Include mixer noise** 并将 **Mixer noise type** 设置为 `noise-temperature`。

### **Noise figure (dB)** — 用于对混频器噪声建模的噪声系数 `10 * log10( 2 )` (默认) | 非负实数

用于对混频器噪声建模的噪声系数，指定为以 dB 为单位的非负实数。

#### 依赖关系

要启用此参数，请选择 **Include mixer noise** 并将 **Mixer noise type** 设置为 `NF`。

### **Noise factor** — 用于对混频器噪声建模的噪声因数 `2` (默认) | 大于或等于 `1` 的正整数标量

用于对混频器噪声建模的噪声因数，指定为大于或等于 `1` 的正整数标量

#### 依赖关系

要启用此参数，请选择 **Include mixer noise** 并将 **Mixer noise type** 设置为 `noise-factor`。

### **Seed source, mixer noise** — 初始种子的来源 `auto` (默认) | `user`

用于准备高斯随机数噪声生成器的初始种子来源，指定为以下之一：

- `auto` — 当您将 **Seed source, mixer noise** 设置为 `auto` 时，将使用随机数生成器为每个混频器实例生成种子。实例的重置方法不起作用。
- `user` — 当您将 **Seed source, mixer noise** 设置为 `user` 时，将使用 **Seed for mixer noise** 中提供的值初始化随机数生成器，并且重置方法使用 **Seed for mixer noise** 属性值重置随机数生成器。

#### 依赖关系

要启用此参数，请选择 **Include mixer noise**。

### **Seed for mixer noise** — 随机数生成器的种子 `67987` (默认) | 小于 2^32 的非负整数

随机数生成器的种子，指定为小于 2^32 的非负整数。使用此值初始化随机数生成器。

#### 依赖关系

要启用此参数，请选择 **Include mixer noise** 并将 **Seed source, mixer noise** 参数设置为 `user`。

### **Include phase noise** — 向 LO 信号添加 LO 相位噪声 `off` (默认) | `on`

选择此参数可向 LO 信号添加与频率相关的 LO 相位噪声。选择此参数后，将显示与 **Include phase noise** 关联的参数，并且模块图标内的 LO 源会显示为灰色。

有关详细信息，请参阅 Mixer 模块中的相位噪声。

### **Phase noise level (dBc/Hz)** — 相对于载波的相位噪声电平 `[-145 -150]` (默认) | 负实数标量 | 负实数向量

相对于载波的相位噪声电平，指定为以 dBc/Hz 为单位的负实数标量或向量。

**注意**

**Phase noise level (dBc/Hz)** 参数中列出的项数必须等于 Frequency offset (Hz) 字段中的项数。

#### 依赖关系

要启用此参数，请选择 **Include phase noise** 参数。

**数据类型：** `double`

### **Frequency offset (Hz)** — 相位频率偏移 `[2000 20000]` (默认) | 正实数标量 | 正递增实数值向量

将频率偏移指定为以 Hz 为单位的 double 类型的正实数标量或正递增实数值向量。

**注意**

**Frequency offset (Hz)** 中列出的项数必须等于 Phase noise level (dBc/Hz) 字段中的项数。

#### 依赖关系

要启用此参数，请选择 **Include phase noise** 参数。

### **Automatic frequency resolution** — 自动确定频率 bin 的数量 `on` (默认) | `off`

选择此参数可自动确定双边相位噪声频谱中使用的频率 bin 数量。当您将 **Automatic frequency resolution** 参数设置为 `off` 时，也可以使用 **Number of signal samples** 和 **Sample rate (Hz)** 参数设置频率 bin 数量。

#### 依赖关系

要启用此参数，请点击 **Include phase noise**。

### **Number of signal samples** — 时域信号中的样本数 `0` (默认) | 小于或等于 `65536` 的实非负整数

时域信号中用于模块采样时间的样本数，或信号双边频谱中的频率线（bin）数，以实现指定 Frequency offset 所需的频率分辨率，指定为小于或等于 `65536` 的实非负整数。频率分辨率随 number of signal samples 值的增加而提高。

**注意**

此参数的值必须设置为 2 的幂。

#### 依赖关系

要启用此参数，请选择 **Include phase noise** 参数并取消选择 **Automatic frequency resolution**。

### **Seed source, phase noise** — 初始种子的来源 `auto` (默认) | `user`

用于准备高斯随机数 LO 相位噪声生成器的初始种子来源，指定为以下之一：

- `auto` — 当您将 **Seed source, phase noise** 设置为 `auto` 时，将使用随机数生成器为每个混频器实例生成种子。实例的重置方法不起作用。
- `user` — 当您将 **Seed source, phase noise** 设置为 `user` 时，将使用 **Seed for phase noise** 中提供的值初始化随机数生成器，并且重置方法使用 **Seed for phase noise** 属性值重置随机数生成器。

#### 依赖关系

要启用此参数，请选择 **Include phase noise** 参数。

### **Seed for phase noise** — 随机数生成器的种子 `67987` (默认) | 小于 2^32 的非负整数

随机数生成器的种子，指定为小于 2^32 的非负整数。使用此值初始化随机数生成器。

#### 依赖关系

要启用此参数，请选择 **Include phase noise** 并将 **Seed source, phase noise** 参数设置为 `user`。

### **Plot phase characteristics** — 绘制相位特性按钮

此按钮根据 **Noise** 选项卡上指定的参数，以及执行仿真时的模块采样时间或根据 Frequency offset (Hz) 参数值估算的值，来绘制相位特性。

有关详细信息，请参阅绘制相位噪声特性。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024b：Idealized Baseband 库中 Mixer 模块的参数已重命名

Idealized Baseband 库中 Mixer 模块的以下参数已重命名。

| R2024b 之前的参数名 | R2024b 起的参数名 |
| --- | --- |
| **Mixer sideband** | **Sideband** |
| **Conversion gain (dB)** | **Gain (dB)** |
| **Type of Non-linearity** | **Non-linearity** |

Idealized Baseband 库中 Mixer 模块的以下参数值已更改：

| 参数 | R2024b 之前的值 | R2024b 起值 |
| --- | --- | --- |
| **Mixer type** | `Modulator` | `mod` |
| `Demodulator` | `demod` |
| `IQ Demodulator` | `iqdemod` |
| `IQ Modulator` | `iqmod` |
| **Mixer noise type** | `Noise figure` | `NF` |
| `Noise temperature` | `noise-temperature` |
| `Noise factor` | `noise-factor` |
| **Sideband** | `Upper` | `upper` |
| `Lower` | `lower` |
| **Seed source, phase noise** | `Auto` | `auto` |
| `User specified` | `user` |
| **Seed source, mixer noise** | `Auto` | `auto` |
| `User specified` | `user` |

Idealized Baseband 库中 Mixer 模块的以下默认值已更改：

| 参数 | R2024b 之前的默认值 | R2024b 起的默认值 |
| --- | --- | --- |
| **Non-linearity** | `IIP3` | `OIP3` |
| **Mixer noise type** | `Noise temperature` | `NF` |

当您打开在 R2024b 之前创建的包含 Mixer 模块的模型时，软件会按表中所示替换参数名和值。

### R2024b：Input carrier frequency greater than LO frequency 参数已替换

**Input carrier frequency greater than LO frequency** 参数已由 **RF (Hz)** 和 **LO(Hz)** 参数替换。

当您打开在 R2024b 之前创建的包含 Mixer 模块的模型时，软件会将 **Input carrier frequency greater than LO frequency** 替换为 **RF (Hz)** 和 **LO(Hz)** 参数。

### R2023a：Mixer 模块的相位噪声特性已更改

从此版本开始，Mixer 模块中指定 1/f^3 的第一个频率点以下的推断低频相位噪声现在为 30 dB/decade，而不是 3 dB/decade。

当您打开一个在 R2023a 之前创建的包含 Mixer 模块的模型，并点击 **Plot Phase Characteristics** 按钮时，软件会在相位噪声幅度响应图中对 y 轴上的相位噪声电平（以 dBc/Hz 为单位）进行缩放。

例如，打开 Mixer 模块并选择 **Include Phase Noise**。将 **Number of signal samples** 设置为 `2^10`，然后点击 **Apply** 按钮。点击 **Plot Phase Characteristics** 按钮以绘制相位噪声幅度响应，并观察 Mixer 模块中指定 1/f^3 的第一个频率点被缩放为 30 dB/decade。

相位噪声幅度响应，其中 Mixer 模块中指定 1/f^3 的第一个频率点被缩放为 30 dB/decade

### R2021a：Idealized Baseband 库中 Mixer 模块支持的 Mixer 模型和噪声已更改

从 R2021a 开始，Mixer 模块支持带有损伤和噪声的调制器、解调器、IQ 调制器和 IQ 解调器混频器。当 **Mixer type** 参数设置为 `Modulator` 时，新的 Mixer 模块使您能够使用 R2021a 之前的功能。

当您打开一个来自之前版本的模型，其中包含来自 Idealized Baseband 库的 Mixer 模块时，该模块的 R2021a 之前版本会自动替换为带有损伤和噪声的 R2021a 版本。

## 描述

对带有损伤和噪声的 RF 和 IQ 调制器以及 RF 和 IQ 解调器进行建模

Mixer 模块对四个复基带混频器进行建模，并带有损伤和噪声。该模块建模的四种混频器类型为 Modulator、Demodulator、IQ Modulator 和 IQ Demodulator。损伤包括适当的 IQ 增益和相位失配，而噪声包括系统相位噪声和 LO 相位噪声。

**注意**

- Idealized Baseband 库模块假设输入和输出端口是匹配的。有关端口信号功率的详细信息，请参阅 RF Blockset 中的 Power Ports and Signal Power Measurement。
- Idealized Baseband 库模块是单载波的，并假设了载波频率值。因此，Ideal Baseband Mixer 模块只能产生单边带输出。
- Mixer 模块掩码图标是动态的，并指示当前应用的噪声参数集。有关详细信息，请参阅 Mixer Block Icons。
