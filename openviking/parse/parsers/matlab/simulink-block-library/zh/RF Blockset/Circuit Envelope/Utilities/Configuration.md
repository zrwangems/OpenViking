---
type: simulink-block
title: 'Configuration'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'configuration'
documentation_source_path: 'ref/configuration.html'
language: zh-CN
chinese_source: worker-translation
---

# Configuration

## 端口

R2025b 中未记录。

## 参数

#### 主

### **Automatically select fundamental tones and harmonic order** — 自动选择基频音和谐波阶数 `on`（默认）| `off`

选择此参数可在更新模型时自动选择 **Fundamental tones** 和 **Harmonic order** 参数。自动选择并不总是返回尽可能小的仿真频率集。此方法使用保守数量的仿真频率来捕获系统的非线性行为。

要设置 **Fundamental tones** 和 **Harmonic order**，请清除此参数。较小的仿真频率集可减少仿真时间并降低内存需求。然而，仿真频率的减少可能会降低精度。

### **Fundamental tones** — 仿真频率集的基频音，以 Hz 为单位的正整数向量

仿真频率集的基频音，指定为以 Hz 为单位的正整数向量。

#### 依赖关系

要启用此参数，请清除 **Automatically select fundamental tones and harmonic order**。

### **Harmonic order** — 每个基频音的谐波阶数，正整数向量

每个基频音的谐波阶数，指定为正整数向量。您也可以指定一个标量，该值将应用于每个 **Fundamental tones**。

#### 依赖关系

要启用此参数，请清除 **Automatically select fundamental tones and harmonic order**。

### **Total simulation frequencies: Computed at simulation time** — 显示仿真频率数量的按钮

该模块根据基频音及其各自的谐波阶数确定仿真频率。求解器在每个仿真频率处计算网络的解，计算时间根据仿真频率的总数进行缩放。

基频音的组合决定了仿真频率集：[*m*\**f*1 + *n*\**f*2 + …]。在这种情况下，基频音由 [*fs*1,*f*2,…] 表示，整数 *m* 和 *n* 是由相应 **Harmonic order** 限定的整数，|*m*| ≦*h*1，|*n*| ≦*h*2，等等。仅考虑正频率。

点击 **View** 打开对话框，其中包含有关系统中仿真频率的附加信息。`Configuration` 模块显示非线性模型的仿真频率数量。对于线性模型，实际频率数量在仿真期间自动优化。

通过点击列出的仿真频率，您可以查看哪些基频音的线性或多次组合表示该频率。从对话框中，您还可以在数轴上绘制仿真频率。

考虑单个基频音 *f*1 = 2 GHz 及相应的谐波阶数 *h1* = 3。仿真频率集为：`[0, f1, 2f1, 3f1] = [0GHz, 2 GHz, 4 GHz, 6GHz]`。

考虑具有两个基频音 `[f1 = 2 GHz, f2 = 50 MHz]` 及相应谐波阶数 `h1 = h2 = 1` 的电路。此设置产生五个仿真频率，值为：`[0, f2, f1-f2, f1, f1+f2]`。

考虑具有两个基频音 `[f1 = 2 GHz, f2 = 3GHz]` 及相应谐波阶数 `h1 = 1` 和 `h2 = 3` 的电路。此设置产生 11 个仿真频率，值为：`[0, f2, f1-f2, f1, f1+f2, -f1+2f2, 2f2, -f1+3f2, f1+2f2, 3f2, f1+3f2]`。

仿真频率集必须包含 RF Blockset 子系统中指定的所有载波频率，例如 Inport、Outport 和源模块内的载波频率。

#### 依赖关系

要启用此参数，请选择 **Automatically select fundamental tones and harmonic order**。如果清除 **Automatically select fundamental tones and harmonic order**，该选项将变为 **Total simulation frequencies: N/A: Fundamental tones undefined**。

### **Step size** — 固定步长求解器配置的时间步长 `1e-6`（默认）| 以秒为单位的标量

固定步长求解器配置的时间步长，指定为以秒为单位的标量。时间步长的倒数决定了以每个仿真频率为中心的信号包络的仿真带宽。

电路包络仿真的时间步长应与相对信号带宽相称，而不是与载波频率的绝对值相称。

默认值（1e-6s）足以对带宽高达 1/*h* 或 1MHz 的包络信号进行建模。当仿真接近最大带宽时，仿真精度会降低。减小步长以对更大带宽的信号进行建模，或提高精度。

仿真速度与仿真步长成反比。较小的仿真步长对应于较宽的包络带宽和较慢的仿真。

当仿真白噪声时，每个仿真频率的噪声带宽等于 1/*h*。

### **Envelope bandwidth** — 最大仿真包络带宽 `1 MHz`（默认）| 以 Hz 为单位的标量

最大仿真包络带宽，以 Hz 为单位的标量返回。
配置模块使用 **Step size** 参数自动计算此值。使用的公式为：bandwidth=1(step  size)。

### **Simulate noise** — 全局启用或禁用噪声建模 `on`（默认）| `off`

选择此参数可全局启用 RF Blockset 电路中的噪声建模。
选中此复选框时：

- Amplifier 和 Mixer 模块使用其各自的 **Noise figure (dB)** 参数值。
- Amplifier 和 Mixer 模块在 **Temperature** 参数指定的温度下使用热噪声进行仿真。
- Resistor 模块使用 **Temperature** 参数对热噪声进行建模。
- Noise 模块将指定的噪声功率建模为电压或电流源。

要全局禁用噪声建模，请清除此参数。

### **Use default random number generator** — RF Blockset 源的默认伪随机噪声流 `on`（默认）| `off`

选择此参数可保留 RF Blockset 源的默认伪随机噪声流。清除此选项可为 RF Blockset 拓扑子系统指定独立的伪随机数流，并确定噪声流的种子。

#### 依赖关系

要显示此参数，请选择 **Simulate noise**。

### **Noise seed** — 独立伪随机数流的种子 `0`（默认）| 标量正整数

独立伪随机数流的种子，指定为标量正整数。

#### 依赖关系

要显示此参数，请清除 **Use default random number generator**。

### **Temperature** — 全局噪声温度 `290.0``K` | 以开尔文为单位的标量整数

全局噪声温度，指定为以开尔文为单位的标量整数。

### **Samples per frame** — Inport 模块输入信号每个通道中的样本数 `1` | 正标量整数

Inport 模块输入信号每个通道中的样本数，指定为小于或等于 `1024` 的正标量整数。一个通道对应于 Inport 模块中的一个输入频率。

**Note**

为提高系统性能，建议的 **Samples per frame** 最大值为 `1024`。要处理更大的帧，请考虑以下方法之一：

- 使用 `rfsystem` System object™，它支持基于帧处理的向量输入，且没有任何帧大小限制。
- 在 Circuit Envelope Inport 和 Outport 模块之前和之后使用 Buffer (DSP System Toolbox) 模块。有关详细信息，请参阅 Buffering and Frame-Based Processing (DSP System Toolbox)。

### **Normalize Carrier Power** — 归一化载波信号功率 `on`（默认）| `off`

选择此选项以归一化载波功率，使信号的平均功率为：

I2+  Q2

在这种情况下，该方程给出 ω 处对应的通带信号：

sk(t)=I(t)2cos(2πfkt) − Q(t)2sin(2πfkt)

其中：

- *I*(*t*) 是载波信号的同相部分。
- *Q*(*t*) 是载波信号的正交部分。
- *fk* 是载波频率。

清除此选项后，载波信号的平均功率为：

I2 +  Q22

在这种情况下，ω 处对应的通带信号由以下方程表示

sk(t)=I(t)cos(2πfkt) − Q(t)sin(2πfkt)

0 载波频率是一种特殊情况。其通带表示始终为 *I*，平均功率为 *I*2

### **Enable input interpolation filter** — 自动将较低速率基带信号插值到较高速率 RF 信号 `on`（默认）| `off`

选择此选项以启用输入插值滤波器，对输入信号速率进行上采样，以匹配 RF 求解器的采样率。现在您可以在更宽频带的电路中直接使用较低采样率的基带通信信号。此滤波器会在 RF 信号中引入延迟。**Filter delay (in samples)** 显示仿真模型后引入的延迟。

**注意**

当您启用此滤波器时，

- RF 与基带的采样率比必须为 2、4、6 或 8。
- RF Blockset 模型只能有一个 Inport 模块。

#### 高级

### **Transient analysis** — RF Blockset 环境的固定步长求解器 `Auto`（默认）| `NDF2` | `Trapezoidal Rule` | `Backward Euler`

RF Blockset 环境的固定步长求解器，指定为以下之一：

- `Auto`：当您不确定使用哪个求解器时，将此参数设置为 `Auto`。
- `NDF2`：将此参数设置为 `NDF2` 以平衡窄带和宽带精度。此求解器适用于系统中信号的频率内容相对于奈奎斯特速率未知的情况。
- `Trapezoidal Rule`：将此参数设置为 `Trapezoidal Rule` 以进行窄带仿真。频率扭曲和缺乏阻尼效应使此方法不适用于大多数宽带仿真。
- `Backward Euler`：将此参数设置为 `Backward Euler` 以仿真最大类别的系统和信号。阻尼效应使此求解器适用于宽带仿真，但整体精度较低。

RF Blockset 求解器是 Simscape™ 局部求解器的扩展。有关 Simscape 局部求解器的更多信息，请参阅 Solver Configuration 模块参考页。

### **Approximate transient as small signal** — 为瞬态小信号分析选择一小部分频率 `off`（默认）| `on`

选择此选项以为瞬态小信号分析选择一小部分频率。

### **Use all steady-state simulation frequencies for small signal analysis** — 选择所有稳态仿真频率 `on`（默认）| `off`

选择此选项以选择所有稳态仿真频率。清除此选项以指定小信号瞬态仿真的频率。

#### 依赖关系

要显示此参数，请选中 **Approximate transient as small signal**。

### **Small signal frequencies** — 小信号瞬态仿真的频率 标量 | 向量

小信号瞬态仿真的频率，指定为标量或向量。指定的频率包含在由 **Main** 选项卡中的 **Fundamental tones** 和 **Harmonic order** 确定的整个仿真频率集合中。

此框中的默认值和对应单位不是常量。这些值取决于首次清除 **Use all steady-state simulation frequencies for small signal analysis** 时配置对话框的状态。

#### 依赖关系

要显示此参数，请清除 **Use all steady-state simulation frequencies for small signal analysis**。

### **Populate Frequencies** — 用于选择小信号瞬态频率的按钮

用于选择小信号瞬态频率以填充 **Small signal frequencies** 的工具。所选频率是根据 **Main** 选项卡中的 **Fundamental tones** 和 **Harmonic order** 输入确定的仿真频率的子集。完整的仿真频率集合在对话框右侧的组合框中给出，所选频率会高亮显示。你可以通过在选择框中直接选择频率，或者在 **Small signal selection panel** 中选择所需的音调和谐波阶数，然后按 **Select** 来选择。组合框中的 **Tones(Hz)** 和 **Harmonic order** 值也会使用 **Main** 选项卡中的 **Fundamental tones** 和 **Harmonic order** 输入来填充。

选择小信号频率窗口

#### 依赖关系

要显示此参数，请清除 **Use all steady-state simulation frequencies for small signal analysis**。

### **Relative tolerance** — 系统变量的相对牛顿容差 `1e-3`（默认）| 实正有限标量

系统变量的相对牛顿容差，指定为实正有限标量。

### **Absolute tolerance** — 系统变量的绝对牛顿容差 `1e-6`（默认）| 实正有限标量

系统变量的绝对牛顿容差，指定为实正有限标量。

### **Maximum iterations** — 收敛所需的迭代次数 `10`（默认）| 实正整数标量

收敛所需的迭代次数，指定为实正整数标量。

### **Error estimation** — 检查系统变量中的收敛误差 `2-norm over all variables`（默认）| `Each variable separately`

检查系统变量中的收敛误差，指定为：

- `2-norm over all variables`：使用此选项计算所有状态变量的 2-范数，然后检查状态变量的收敛误差。
- `Each variable separately`：使用此选项分别检查每个变量的收敛误差。

### **Restore Default Settings** — 将牛顿求解器恢复为默认值 按钮

将牛顿求解器恢复为默认值，指定为按钮。

## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

### R2021b：Configuration 模块图标已更新

从 R2021b 开始，Configuration 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当你打开在 R2021b 之前创建的包含 Configuration 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

定义系统仿真设置

使用 Configuration 模块设置电路包络仿真的模型条件。该模块参数定义 RF 和求解器属性。RF 属性包括仿真频率、谐波阶数、包络带宽和热噪声等属性。求解器属性包括瞬态分析类型、容差和小信号近似。

小信号瞬态仿真执行完整的非线性谐波平衡稳态求解，以确定后续线性瞬态分析的工作点。此选项允许您捕获受大恒定（载波上）信号影响的小信号的正确频谱行为。

将每个拓扑上不同的 RF Blockset™ 子系统连接一个 Configuration 模块。每个 Configuration 模块定义所连接的 RF Blockset 子系统的参数。要查看模型中 Configuration 模块的示例，请在 MATLAB 命令窗口中输入 `RFNoiseExample`。

有关 RF 仿真的介绍，请参阅 Simulate High Frequency Components。

Configuration 模块掩码图标是动态的，显示所应用噪声参数的当前状态。下表显示了此模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: on | Simulate noise: off |
| --- | --- |
| Simulate noise 设置为 on 时的 Configuration 模块图标。 | Simulate noise 设置为 off 时的 Configuration 模块图标。 |
