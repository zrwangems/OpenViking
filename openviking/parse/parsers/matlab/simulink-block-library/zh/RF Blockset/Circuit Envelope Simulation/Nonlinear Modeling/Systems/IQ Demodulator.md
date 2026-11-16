---
type: simulink-block
title: 'IQ Demodulator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Nonlinear Modeling / Systems'
documentation_page: 'iqdemodulator'
documentation_source_path: 'ref/iqdemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# IQ Demodulator

## 端口

R2025b 中未记录。

## 参数

### Main

### **Source of conversion gain** — 转换增益的源参数 `Available power gain`（默认）| `Open circuit voltage gain` | `Polynomial coefficients`

转换增益的源参数，指定为以下之一：

- `Available power gain` —
  将输出 `I` 支路的单边带（SSB）功率与输入功率之比关联起来。
  如果不存在增益失配，则 `Q` 支路的增益与 `I` 支路的增益匹配。
- `Open circuit voltage gain`
  — 开路电压增益参数的值，作为多项式压控电压源（VCVS）的线性电压增益项。
- `Polynomial coefficients`
  — 根据您指定的多项式实现非线性电压增益。

### **Available power gain** — 输出 `I` 支路的 SSB 功率与输入功率之比 `0 dB`（默认）| dB 标量或无单位比值

输出 `I` 支路的 SSB 功率与输入功率之比，指定为 dB 标量或无单位比值。对于无单位比值，选择 `None`。

#### 依赖关系

要启用此参数，请将 **Source of conversion gain** 设置为 `Available power gain`。

### **Open circuit voltage gain** — 开路电压增益 `0 dB`（默认）| 标量

开路电压增益，指定为 dB 标量。

#### 依赖关系

要启用此参数，请将 **Source of conversion gain** 设置为 `Open circuit voltage gain`。

### **Polynomial coefficients** — 指定电压增益的多项式系数 `[0 1]`（默认）| 向量

多项式系数，指定为向量。

多项式的阶数必须小于或等于 9。系数必须按升幂排序。如果向量有 10 个系数，
`[a0,a1,a2,
... a9]`，
则它表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

*a*1
表示线性增益项。

例如，向量
`[a0,a1,a2,a3]`
指定关系 *Vout* = *a*0 + *a*1*V*1 + *a*2*V*12 + *a*3*V*13。尾随零被省略。因此
`[a0,a1,a2]`
定义的多项式与
`[a0,a1,a2,
0]` 相同。

默认情况下，值为 `[0,1]`，对应于线性关系 *Vout* =
*Vin*。

#### 依赖关系

要启用此参数，请将 **Source of conversion gain** 设置为 `Polynomial coefficients`。

### **Local oscillator frequency** — 本振（LO）频率 `0` `Hz`（默认）| 标量

本振（LO）频率，指定为 `Hz`、`kHz`、`MHz` 或 `GHz` 标量。

### **Input impedance (Ohm)** — IQ 解调器的输入阻抗 `50`（默认）| 标量

IQ 解调器的输入阻抗，指定为 Ohms 标量。

### **Output impedance (Ohm)** — IQ 解调器的输出阻抗 `50`（默认）| 标量

IQ 解调器的输出阻抗，指定为 Ohms 标量。

### **Add Image Reject filter** — 镜像抑制（IR）滤波器参数 `off`（默认）| `on`

选中以添加 **IR filter** 参数选项卡。
清除以移除该选项卡。

### **Add Channel Select filters** — 通道选择（CS）滤波器参数 `off`（默认）| `on`

选中以添加 **CS filter** 参数选项卡。
清除以移除该选项卡。

### **Ground and hide negative terminals** — 将电路端子接地并隐藏 `on`（默认）| `off`

选中以在内部将负端子接地并隐藏。清除以暴露负端子。当端子暴露时，可以将其连接到模型的其他部分。

### **Edit System** — 断开 IQ 解调器模块链接并用适当值替换内部变量 按钮

使用此按钮断开 IQ 调制器与库的链接。内部变量将替换为其值，这些值使用 IQ 调制器参数估算。IQ 调制器变为一个简单子系统，仅保留图标而进行封装。

使用 **Edit System** 编辑内部变量而不展开子系统。使用 **Expand System** 在 Simulink™ 画布中展开子系统并编辑该子系统。

### Impairments

### **I/Q gain mismatch** — `I` 和 `Q` 支路之间的增益差 `0` `dB`（默认）| 标量

`I` 和 `Q` 支路之间的增益差，指定为 dB 标量。增益失配假定为前向的，也就是说，该失配不影响从 LO 到 RF 的泄漏。

如果指定了增益失配，则值（Available   power gain+I/Q gain mismatch）将输出 `Q` 支路的单边带（SSB）功率与输入功率之比关联起来。

### **I/Q phase mismatch** — `I` 和 `Q` 支路之间的相位差 `0` `degrees`（默认）| 以度或弧度为单位的标量

`I` 和 `Q` 支路之间的相位差，指定为以 degrees 或 radians 为单位的标量。相位失配会影响从 LO 到输入 RF 的泄漏。

### **LO to RF isolation** — LO 电压与泄漏 RF 电压之间的幅度比 `inf dB`（默认）| 标量

LO 电压与泄漏 RF 电压之间的幅度比，指定为 dB 标量。从 LO 输入到内部 `I` 和 `Q` 混频器（在相移和相位失配之后）再到达 RF 的路径中的相位累积假定为零。

### **Noise figure (dB)** — 输出与输入之间的信噪比（SNR） `0`（默认）| 标量

混频器的单边带噪声系数，指定为标量。

要在电路包络模型中使用 Noise、Amplifier 或 Mixer、IQ Demodulator 模块对噪声建模，必须在 Configuration 模块对话框中选中 **Simulate noise** 复选框。

下表总结了用于指定 SSB 噪声的两种相互竞争的定义，其中镜像频率（IM）定义为
ωIM = ωLO + (ωLO – ωRF)。

| 噪声约定 | RF 频率处的信号 | IM 频率处的信号 | IQ Demodulator 模块是否支持此模型？ |
| --- | --- | --- | --- |
| 单边带噪声（SSB） | *S* + *N*，带噪声的信号 | *N*，仅噪声 | Yes |
| IEEE 单边带噪声定义（SSB*IEEE*） | *S* + *N*，带噪声的信号 | 无信号 | No；您可以使用由 S-parameters 模块创建的理想滤波器来创建等效模型。 |

### **Add phase noise** — 添加相位噪声 `off`（默认）| `on`

选择此参数以将相位噪声添加到您的 IQ 解调器系统。

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `1`（默认）| 标量 | 向量 | 矩阵

相位噪声频率偏移，指定为标量、向量或矩阵，每个元素的单位为 Hz。

如果指定矩阵，则每一列对应于 CW 源的一个非 DC 载波频率。频率偏移值约束仿真的包络带宽。有关更多信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `-Inf`（默认）| 标量 | 向量 | 矩阵

相位噪声电平，指定为标量、向量或矩阵，元素单位为 decibel per dBc/Hz。

如果指定矩阵，则每一列对应于 CW 源的一个非 DC 载波频率。频率偏移值约束仿真的包络带宽。有关更多信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选中以自动估计相位噪声的冲激响应。清除以使用 **Impulse response duration** 指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于仿真相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 为单位的标量。

**注意**

相位噪声剖面在频率上的分辨率受用于仿真它的冲激响应持续时间的限制。增大此持续时间可提高相位噪声剖面的精度。如果对于给定的冲激响应持续时间，相位噪声频率偏移分辨率过高，则会出现警告消息。此消息还会指定适用于所需分辨率的最小持续时间。

#### 依赖关系

要设置此参数，请清除 **Automatically estimate impulse response duration**。

### **Plot phase noise characteristics** — 相位噪声幅度响应 按钮

该模块根据 **Impairments** 选项卡上指定的参数，以及 Configuration 模块中的 **Envelope bandwidth** 参数（如果可用）或 **Phase noise frequency offset (Hz)** 参数中指定的值，绘制相位噪声特性。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### Nonlinearity

在 **Main** 选项卡中为 **Source of conversion gain** 选择 `Polynomial coefficients` 会移除 **Nonlinearity** 参数。

### **Nonlinear polynomial type** — 多项式非线性 `Even and odd order`（默认）| `Odd order`

多项式非线性，指定为以下之一：

- `Even and odd order`：除了线性项之外，IQ Demodulator 还可以产生二阶和三阶互调频率。
- `Odd order`：IQ Demodulator 仅产生“奇次阶”互调频率。

  线性增益确定线性 *a*1 项。该模块根据 **IP3**、**1-dB gain compression power**、**Output saturation power** 和 **Gain compression at saturation** 中指定的值计算其余项。您指定的约束数量决定模型的阶数。该图显示了非线性 IQ 解调器参数的图形定义。

  输出与输入功率图显示了非线性 IQ 解调器参数。

### **Intercept points convention** — 截点约定 `Input`（默认）| `Output`

截点约定，指定为 `Input`（输入参考）或 `Output`（输出参考）。将此规范用于截点 **IP2**、**IP3**、**1-dB gain compression power** 和 **Output saturation power**。

### **IP2** — 二阶截点 `inf` `dBm`（默认）| 标量

二阶截点，指定为 dBm、W、mW 或 dBW 标量。默认值
`inf` `dBm`
对应于未指定的点。

#### 依赖关系

要启用此参数，请将 **Nonlinear polynomial type** 设置为 `Even and odd order`。

### **IP3** — 三阶截点 `inf` `dBm`（默认）| 标量

三阶截点，指定为 dBm、W、mW 或 dBW 标量。默认值
`inf` `dBm`
对应于未指定的点。

#### 依赖关系

要启用此参数，请将 **Nonlinear polynomial type** 设置为 `Even and odd order`。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf``dBm`（默认）| 标量

1-dB 增益压缩功率，指定为 dBm、W、mW 或 dBW 标量。1-dB 增益压缩点必须小于输出饱和功率。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中设置 `Odd order`。

### **Output saturation power** — 输出饱和功率 `inf``dBm`（默认）| 标量

输出饱和功率，指定为标量。该模块使用此值计算非线性模型中使用的电压饱和点。在这种情况下，多项式的一阶导数为零，二阶导数为负。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中设置 `Odd order`。

### **Gain compression at saturation** — 饱和时的增益压缩 `inf``dBm`（默认）| 标量

饱和时的增益压缩，指定为标量。

#### 依赖关系

要启用此参数，请首先在 **Nonlinear polynomial type** 选项卡中选择 `Odd order`。然后更改 **Output saturation power** 的默认值。

### IR Filter

在 **Main** 选项卡中选择 **Add Image Reject filter** 以查看 **IR Filter** 参数选项卡。

### **Design method** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。模拟理想、Butterworth 或 Chebyshev 滤波器，其类型在 **Filter type** 中指定，模型在 **Implementation** 中指定。

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。模拟 **Design method** 中指定的设计的低通、高通、带通或带阻滤波器类型。

### **Implementation** — 实现 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现，指定为以下之一：

- `LC Tee`：当 **Design method** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi`：当 **Design method** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function`：当 **Design method** 为 Butterworth 或 Chebyshev 时，使用双端口 S-parameters 对模拟滤波器建模。
- `Constant per carrier`：对滤波器建模，将全传输或全反射设置为在每个载波周围的整个包络频带内恒定。**Design method** 指定为理想。
- `Filter Domain`：使用与冲激响应的卷积对滤波器建模。**Design method** 指定为理想。冲激响应针对每个载波频率独立计算，以捕获理想滤波响应。当理想滤波器的全传输与全反射之间的转换发生在载波周围的包络频带内时，频域实现会在 **Impulse response duration** 中指定的频率分辨率范围内正确捕获此转换。

  **注意**

  由于因果性，反射和传输信号都包含冲激响应持续时间一半的延迟。当 Source 和 Load 电阻与滤波器参数中指定的值不同时，此延迟会损害滤波器性能。

默认情况下，对于理想滤波器，**Implementation** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，**Implementation** 为 `LC Tee`。

### **Passband edge frequency** — 通带边缘频率 `2 GHz`（默认）| 标量

通带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`，并将 **Filter type** 设置为 `Lowpass` 或 `Highpass`。

### **Implement using filter order** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### **Filter order** — 滤波器阶数 `3`（默认）| 标量

滤波器阶数，指定为标量。对于 `Lowpass` 或 `Highpass` 的 **Filter type**，滤波器阶数是集总存储元件的数量。对于 `Bandpass` 或 `Bandstop` 的 **Filter type**，集总存储元件的数量是滤波器阶数的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，对于 Tee 网络实现，电阻比 RloadRsource>Rratio；对于 Pi 网络实现，RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是通带波纹，单位为 dB。

#### 依赖关系

要启用此参数，请选择 **Implement using filter order**。

### **Passband frequency** — 低通和高通滤波器的通带频率 标量

低通和高通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。对于 `Lowpass` 滤波器，默认值为 `1 GHz`；对于 `Highpass` 滤波器，默认值为 `2 GHz`。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`，并将 **Filter type** 设置为 `Lowpass` 或 `Highpass`。

### **通带频率** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 2-tuple vector

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于
带阻滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| scalar

通带衰减，指定为以 dB 为单位的 scalar。对于带通
滤波器，此值等量应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于
带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **阻带边缘频率** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于理想
带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Ideal`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| scalar

阻带衰减，指定为以 dB 为单位的 scalar。对于带阻
滤波器，此值等量应用于阻带的
两侧边缘。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| scalar

输入源电阻，指定为以 Ohms 为单位的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| scalar

输出负载电阻，指定为以 Ohms 为单位的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **自动估计冲激响应持续时间** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此选项可自动估计相位噪声的冲激响应。
清除此选项可使用 **冲激响应持续时间**
手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Ideal`，并将
**实现** 设置为 `Frequency
domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10``s`（默认）| scalar

用于仿真相位噪声的冲激响应持续时间，指定为
以 s、ms、us 或 ns 为单位的 scalar。如果
放大器是非线性的，则不能指定冲激响应。

**注意**

相位噪声分布在频率上的分辨率受用于仿真它的
冲激响应持续时间的限制。增加此
持续时间可提高相位噪声分布的精度。如果相位噪声频率偏移
分辨率对于给定冲激响应持续时间过高，则会出现
警告消息。此消息还会指定适合
所需分辨率的最小持续时间

#### 依赖关系

要启用此参数，请清除 **自动估计
冲激响应持续时间**。

### **导出** — 将滤波器设计保存到文件 button

使用此 button 将滤波器设计保存到文件。有效的文件类型为
`.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### CS Filter

在 **Main** 选项卡中选择 **Add Channel Select filters**，以查看 **CS Filter** 参数。

### **设计方法** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。根据 **滤波器类型** 中指定的类型以及 **实现** 中指定的模型，仿真理想、Butterworth 或 Chebyshev 滤波器。

### **滤波器类型** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。根据 **设计方法** 中指定的设计，仿真低通、高通、带通或带阻滤波器类型。

### **实现** — 实现 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现，指定为以下之一：

- `LC Tee`：当 **设计
  方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi`：当 **设计
  方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function`：当 **设计
  方法** 为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟
  滤波器建模。
- `Constant per carrier`：对每个
  载波周围的整个包络频带内设置为恒定全传输或全反射的
  滤波器建模。**设计方法** 指定为
  ideal。
- `Filter Domain`：使用
  与冲激响应的卷积对滤波器建模。**设计
  方法** 指定为 ideal。针对每个载波频率独立计算冲激
  响应，以捕获理想滤波响应。当理想滤波器的全传输和全反射之间的过渡发生在
  载波周围的包络频带内时，频域实现会正确捕获此过渡，直至
  **冲激响应
  持续时间** 中指定的频率分辨率。

  **注意**

  由于因果性，反射信号和传输信号都包含半个冲激响应
  持续时间的延迟。当源电阻和负载电阻不同于滤波器参数中指定的值时，此延迟会
  损害滤波器性能。

默认情况下，对于理想滤波器，**实现** 为
`Constant per carrier`；对于 Butterworth 或
Chebyshev，**实现** 为 `LC Tee`。

### **通带边缘频率** — 通带边缘频率 `2 GHz`（默认）| scalar

通带边缘频率，指定为以 Hz、kHz、MHz 或
GHz 为单位的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Ideal`。

### **使用滤波器阶数实现** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **滤波器阶数** — 滤波器阶数 `3`（默认）| scalar

滤波器阶数，指定为 scalar。此阶数是
`lowpass` 或
`highpass` 中集总储能元件的数量。在 `bandpass` 或
`bandstop` 中，集总储能元件的数量是该值的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，对于 Tee 网络实现，电阻比 RloadRsource>Rratio；对于 Pi 网络实现，电阻比 RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是
  通带波纹，单位为 dB。

#### 依赖关系

要启用此参数，请选择 **使用滤波器阶数
实现**。

### **通带频率** — 低通和高通滤波器的通带频率 scalar

低通和高通滤波器的通带频率，指定为
以 Hz、kHz、MHz 或 GHz 为单位的 scalar。默认情况下，对于 `Lowpass`
滤波器，通带频率为 `1 GHz`；对于
`Highpass` 滤波器，为 `2 GHz`。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Lowpass` 或
`Highpass`。

### **通带频率** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 2-tuple vector

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于
带阻滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| scalar

通带衰减，指定为以 dB 为单位的 scalar。对于带通
滤波器，此值等量应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于
带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **阻带边缘频率** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2-tuple
vector。此选项不适用于理想
带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Ideal`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| scalar

阻带衰减，指定为以 dB 为单位的 scalar。对于带阻
滤波器，此值等量应用于阻带的
两侧边缘。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`，并将 **滤波器
类型** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| scalar

输入源电阻，指定为以 Ohms 为单位的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| scalar

输出负载电阻，指定为以 Ohms 为单位的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

### **自动估计冲激响应持续时间** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此选项可自动估计相位噪声的冲激响应。
清除此选项可使用 **冲激响应持续时间** 指定冲激响应持续时间。

#### 依赖关系

将 **设计方法** 设置为
`Ideal`，并将
**实现** 设置为 `Frequency
domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10``s`（默认）| scalar

用于仿真相位噪声的冲激响应持续时间，指定为
以 seconds 为单位的 scalar。如果放大器
是非线性的，则不能指定冲激响应。

**注意**

相位噪声分布在频率上的分辨率受用于仿真它的
冲激响应持续时间的限制。增加此
持续时间可提高相位噪声分布的精度。如果相位噪声频率偏移
分辨率对于给定冲激响应持续时间过高，则会出现
警告消息。此消息还会指定适合
所需分辨率的最小持续时间

#### 依赖关系

要启用此参数，请清除 **自动估计
冲激响应持续时间**。

### **导出** — 将滤波器设计保存到文件 button

使用此 button 将滤波器设计保存到文件。有效的文件类型为
`.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **设计方法**
设置为 `Butterworth` 或
`Chebyshev`。

## 所属库

RF Blockset / Circuit Envelope / Systems

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

### R2022b：使用相位噪声偏移频率估计冲激响应持续时间

IQ Demodualtor 模块使用 **Phase noise
frequency offset (Hz)** 参数估计冲激响应持续时间，
并在您点击 **Plot phase noise
characteristics** 按钮时可视化相位噪声特性。

### R2021b：IQ Demodulator 模块图标已更新

从 R2021b 开始，IQ Demodulator 模块图标已更新。模块
图标现在是动态的，并显示噪声参数的当前状态。

当您打开一个在 R2021b 之前创建的、包含 IQ
Demodualtor 模块的模型时，软件会将模块图标替换为 R2021b
版本。

## 描述

将 RF 信号转换为基带信号

`IQ Demodulator` 将 RF 信号
转换为基带信号。`I` 表示信号的
同相分量，`Q` 表示信号的
正交相位分量。您可以使用 IQ Demodulator 来
设计直接转换接收机。

IQ Demodulator 模块掩码图标是动态的，并指示
所应用噪声参数的当前状态。有关详细信息，请参阅 IQ Demodulator Icons。
