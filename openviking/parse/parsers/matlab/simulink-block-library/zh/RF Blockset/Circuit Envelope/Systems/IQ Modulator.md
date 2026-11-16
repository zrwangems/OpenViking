---
type: simulink-block
title: 'IQ Modulator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Systems'
documentation_page: 'iqmodulator'
documentation_source_path: 'ref/iqmodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# IQ Modulator

## 端口

R2025b 中未记录。

## 参数

### Main

### **Source of conversion gain** — 转换增益的来源参数 `Available power gain`（默认）| `Open circuit voltage gain` | `Polynomial coefficients`

转换增益的来源参数，指定为以下选项之一：

- `Available power gain` —
  将输出中单边带（SSB）的功率与 `I`
  支路输入功率之比相关联。此假设无增益失配，且
  Q 支路的输入为
  *Q*in = -
  j.*I*in
- `Open circuit voltage gain`
  — 开路电压增益参数的值，作为多项式
  压控电压源（VCVS）的线性电压增益项。
- `Polynomial coefficients`
  — 根据您指定的多项式实现非线性电压增益。

### **Available power gain** — 输出中 SSB 功率与 `I` 处输入功率之比 `0 dB`（默认）| 以 dB 为单位的标量或无量纲比值

输出中 SSB 的功率与 `I`
支路输入功率之比，指定为以 dB 为单位的标量或
无量纲比值。对于无量纲比值，选择
`None`。

#### 依赖关系

要启用此参数，请将 **Source of conversion
gain** 设置为 `Available power
gain`。

### **Open circuit voltage gain** — 开路电压增益 `0 dB`（默认）| 以 dB 为单位的标量或无量纲比值

IQ 调制器的开路电压，指定为以 dB 为单位的标量或
无量纲比值。对于无量纲比值，选择
`None`。

#### 依赖关系

要启用此参数，请将 **Source of conversion
gain** 设置为 `Open circuit voltage
gain`。

### **Polynomial coefficients** — 指定电压增益的多项式系数 `[0 1]`（默认）| 向量

多项式系数，指定为向量。

多项式的阶数必须小于或等于 9。系数必须
按升幂排列。如果向量有 10
个系数，
`[a0,a1,a2,
... a9]`，
则其表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

*a*1
表示线性增益项。

例如，向量
`[a0,a1,a2,a3]`
指定关系 *Vout* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3。末尾的零被省略。因此
`[a0,a1,a2]`
定义的多项式与
`[a0,a1,a2,
0]` 相同。

默认情况下，值为 [0,1]，对应于线性关系
*Vout* =
*Vin*。

#### 依赖关系

要启用此参数，请将 **Source of conversion
gain** 设置为 `Polynomial
coefficients`。

### **Local oscillator frequency** — 本地振荡器（LO）频率 `0` `Hz`（默认）| 标量

本地振荡器（LO）频率，指定为以 Hz、kHz、
MHz 或 GHz 为单位的标量。

### **Input impedance (Ohm)** — IQ 调制器的输入阻抗 `50`（默认）| 标量

IQ 调制器的输入阻抗，指定为以欧姆为单位的标量。

### **Output impedance (Ohm)** — IQ 调制器的输出阻抗 `50`（默认）| 标量

IQ 调制器的输出阻抗，指定为以欧姆为单位的
标量。

### **Add Image Reject filters** — 镜像抑制（IR）滤波器参数 `off`（默认）| `on`

选择以添加 **IR filter** 参数选项卡。
清除以移除该选项卡。

### **Add Channel Select filter** — 通道选择（CS）滤波器参数 `off`（默认）| `on`

选择以添加 **CS filter** 参数选项卡。
清除以移除该选项卡。

### **Ground and hide negative terminals** — 接地并隐藏负端子 `on`（默认）| `off`

选择以在内部接地并隐藏负端子。清除以
暴露负端子。当端子暴露时，您可以将
它们连接到模型的其它部分。

### **Edit System** — 断开 IQ 调制器模块链接并用适当的值替换内部变量 按钮

使用此按钮断开 IQ 调制器与库的链接。
内部变量被替换为其值，这些值使用 IQ 调制器参数
进行估计。IQ Modulator 变为一个
仅保留图标的简单子系统掩码。

使用 **Edit System** 编辑内部变量
而不展开子系统。使用 **Expand
System** 在
Simulink™ 画布中展开子系统并编辑
子系统。

### Impairments

### **I/Q gain mismatch** — `I` 和 `Q` 支路之间的增益差 `0` `dB`（默认）| 标量

`I` 和 `Q`
支路之间的增益差，指定为以 dB 为单位的标量，或无量纲比值。增益
失配假定为前向的，即失配不会
影响从 LO 到 RF 的泄漏。

如果指定了增益失配，则值（Available  power gain+I/Q gain mismatch）将
`Q` 输入支路的单边带（SSB）功率与输出
功率之比相关联。

### **I/Q phase mismatch** — `I` 和 `Q` 支路之间的相位差 `0` `degrees`（默认）| 以度或弧度为单位的标量

`I` 和 `Q`
支路之间的相位差，指定为以度或弧度为单位的标量。此失配
影响 LO 到输入 RF 泄漏。

### **LO to RF isolation** — LO 电压与泄漏 RF 电压之间的幅度比 `inf dB`（默认）| 标量

LO 电压与泄漏 RF 电压之间的幅度比，指定
为以 dB 为单位的标量，或无量纲比值。对于无量纲比值，选择
`None`。

### **Noise floor (dBm/Hz)** — 单边噪声功率谱分布 `-inf`（默认）| 以 dBm/Hz 为单位的标量

单边噪声功率谱分布，指定为以 dBm/Hz 为单位的标量。
此模块假定 `I` 和 `Q` 支路
均有 -174dBm/Hz 的噪声输入。

### **Add phase noise** — 添加相位噪声 `off`（默认）| `on`

选择此参数以向您的 IQ 调制器
系统添加相位噪声。

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `1`（默认）| 标量 | 向量 | 矩阵

相位噪声频率偏移，指定为标量、向量或矩阵，
每个元素的单位为 Hz。

如果指定矩阵，每一列对应于 CW 源的非直流载波
频率。频率偏移值约束
仿真的包络带宽。有关更多信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase
noise**。

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `-Inf`（默认）| 标量 | 向量 | 矩阵

相位噪声电平，指定为标量、向量或矩阵，
元素单位为 dBc/Hz。

如果指定矩阵，每一列对应于 CW 源的非直流载波
频率。频率偏移值约束
仿真的包络带宽。有关更多信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase
noise**。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择以自动估计相位噪声的冲激响应。
清除以使用 **Impulse
response duration** 指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请选择 **Add phase
noise**。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于仿真相位噪声的冲激响应持续时间，指定为
以 s、ms、us 或 ns 为单位的标量。

**注意**

相位噪声剖面在频率上的分辨率受用于仿真它的冲激响应
持续时间限制。增加此
持续时间以提高相位噪声剖面的精度。如果相位噪声频率偏移
分辨率对于给定的冲激响应持续时间过高，
将出现警告消息。此
消息还会指定适合所需分辨率的最小持续时间。

#### 依赖关系

要设置此参数，请清除 **Automatically estimate
impulse response duration**。

### **Plot phase noise characteristics** — 相位噪声幅度响应 按钮

该模块根据 **Impairments**
选项卡上指定的参数以及
Configuration 模块中的 **Envelope
bandwidth** 参数（如果可用）或
**Phase
noise frequency offset (Hz)** 参数中指定的值，绘制相位噪声特性。

#### 依赖关系

要启用此参数，请选择 **Add phase
noise**。

### Nonlinearity

在 **Main** 选项卡中为
**Source of conversion gain** 选择 `Polynomial coefficients`
将移除
**Nonlinearity** 参数。

### **Nonlinear polynomial type** — 多项式非线性 `Even and odd order`（默认）| `Odd order`

多项式非线性，指定为以下选项之一：

- `Even and odd order`：IQ
  Modulator 除线性项外，还可以产生二阶和三阶
  互调频率。
- `Odd order`：IQ
  Modulator 仅生成“奇阶”互调
  频率。

  线性增益确定线性
  *a*1 项。该模块
  根据 **IP3**、**1-dB gain compression
  power**、**Output saturation
  power** 和 **Gain compression at
  saturation** 中指定的值计算其余项。您指定的约束数量
  决定模型的阶数。图中显示了
  非线性 IQ 调制器参数的图形定义。

  输出与输入功率图显示了非线性 IQ 调制器参数。

### **Intercept points convention** — 截点约定 `Output`（默认）| `Input`

截点约定，指定为
`Input`（输入参考）或
`Output`（输出参考）。将此
规范用于截点 **IP2**、
**IP3**、**1-dB gain compression
power** 和 **Output saturation
power**。

### **IP2** — 二阶截点 `inf` `dBm`（默认）| 标量

二阶截点，指定为以 dBm、W、mW 或
dBW 为单位的标量。默认值
`inf` `dBm`
对应于未指定的点。

#### 依赖关系

要启用此参数，请将 **Nonlinear polynomial
type** 设置为 `Even and odd
order`。

### **IP3** — 三阶截点 `inf` `dBm`（默认）| 标量

三阶截点，指定为以 dBm、W、mW 或
dBW 为单位的标量。默认值
`inf` `dBm`
对应于未指定的点。

#### 依赖关系

要启用此参数，请将 **Nonlinear polynomial
type** 设置为 `Even and odd
order`。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf``dBm`（默认）| 标量

1-dB 增益压缩功率，指定为以 dBm、W、mW 或
dBW 为单位的标量。1-dB 增益压缩点必须小于输出
饱和功率。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中设置 `Odd order`。

### **Output saturation power** — 输出饱和功率 `inf``dBm`（默认）| 标量

输出饱和功率，指定为标量。该模块使用此
值计算非线性模型中使用的电压饱和点。在这种情况下，多项式的一阶导数为零，而
二阶导数为负。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中设置 `Odd order`。

### **Gain compression at saturation** — 饱和时的增益压缩 `inf``dBm`（默认）| 标量

饱和时的增益压缩，指定为标量。

#### 依赖关系

要启用此参数，请先在 **Nonlinear polynomial
type** 选项卡中选择 `Odd
order`。然后更改
**Output saturation power** 的默认值。

### IR Filter

在 **Main** 选项卡中选择 **Add Image Reject filters** 以查看 **IR
Filter** 参数选项卡。

### **Design method** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。仿真 **Filter type** 中指定类型以及 **Implementation** 中指定模型的理想、Butterworth 或 Chebyshev 滤波器。

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。仿真 **Design
method** 中指定设计的低通、高通、带通或带阻滤波器
类型

### **Implementation** — 实现 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现，指定为以下选项之一：

- `LC Tee`：当 **Design
  method** 为 Butterworth 或 Chebyshev 时，使用
  LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi`：当 **Design
  method** 为 Butterworth 或 Chebyshev 时，使用
  LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function`：当 **Design
  method** 为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟
  滤波器建模。
- `Constant per carrier`：对每个
  载波周围整个包络频带内设置为常数的全传输或全反射
  滤波器建模。**Design method** 指定为
  ideal。
- `Filter Domain`：使用与冲激响应的卷积对滤波器建模。**Design
  method** 指定为 ideal。冲激
  响应针对每个载波频率独立计算，以
  捕获理想滤波响应。当理想滤波器的全传输与全反射之间的过渡发生在
  载波周围的包络频带内时，频域
  实现会将此过渡正确捕获到 **Impulse response
  duration** 中指定的频率分辨率。

  **注意**

  由于因果性，反射和传输
  信号都包含冲激响应持续时间一半的延迟。当
  源电阻和负载电阻不同于滤波器参数中指定的值时，此延迟会损害滤波器性能。

默认情况下，对于理想滤波器，**Implementation** 为
`Constant per carrier`；对于 Butterworth 或
Chebyshev，**Implementation** 为 `LC Tee`。

### **Passband edge frequency** — 通带边缘频率 `2 GHz`（默认）| 标量

通带边缘频率，指定为以 Hz、kHz、MHZ 或
GHz 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Ideal`，并将 **Filter
type** 设置为 `Lowpass` 或
`Highpass`。

### **Implement using filter order** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`。

### **Filter order** — 滤波器阶数 `3`（默认）| 标量

滤波器阶数，指定为标量。对于 **Filter
type** 为 `Lowpass` 或
`Highpass`，滤波器阶数是
集总储能元件的数量。对于 **Filter type** 为
`Bandpass` 或
`Bandstop`，集总储能
元件数量是滤波器阶数的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，Tee 网络实现的电阻比 RloadRsource>Rratio，Pi 网络实现的电阻比 RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是以 dB 为单位的
  通带纹波。

#### 依赖关系

要启用此参数，请选择 **Implement using filter
order**。

### **Passband frequency** — 低通和高通滤波器的通带频率 标量

低通和高通滤波器的通带频率，指定为
以 Hz、kHz、MHz 或 GHz 为单位的标量。对于 `Lowpass` 滤波器，默认值为 `1
GHz`；对于 `Highpass`
滤波器，默认值为 `2 GHz`。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Lowpass` 或
`Highpass`。

### **Passband frequencies** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 二元向量

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元
向量。此选项不适用于
带阻滤波器。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Bandpass`。

### **Passband attenuation (dB)** — 通带衰减 `10*log10(2)`（默认）| 标量

通带衰减，指定为以 dB 为单位的标量。对于带通
滤波器，此值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 2-tuple vector。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **阻带边缘频率** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 2-tuple vector。此选项不适用于理想带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`，并将 **滤波器类型** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| scalar

阻带衰减，指定为以 dB 表示的 scalar。对于带阻滤波器，此值同等应用于阻带的两条边缘。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| scalar

输入源电阻，指定为以 Ohms 表示的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| scalar

输出负载电阻，指定为以 Ohms 表示的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **自动估计冲激响应持续时间** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此选项可自动估计相位噪声的冲激响应。清除此选项可使用 **冲激响应持续时间** 手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`，并将 **实现** 设置为 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10``s`（默认）| scalar

用于仿真相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 表示的 scalar。如果放大器是非线性的，则不能指定冲激响应。

**注意**

相位噪声剖面在频率上的分辨率受用于仿真它的冲激响应持续时间的限制。增加此持续时间可提高相位噪声剖面的精度。如果对于给定的冲激响应持续时间，相位噪声频率偏移分辨率过高，则会出现警告消息。此消息还会指定适合所需分辨率的最小持续时间

#### 依赖关系

要启用此参数，请清除 **自动估计冲激响应持续时间**。

### **导出** — 将滤波器设计保存到文件 按钮

使用此按钮将滤波器设计保存到文件。有效的文件类型为 `.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### CS Filter

在 **Main** 选项卡中选择 **添加通道选择滤波器**，以查看 **CS Filter** 参数。

### **设计方法** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。根据 **滤波器类型** 中指定的类型和 **实现** 中指定的模型，仿真理想、Butterworth 或 Chebyshev 滤波器。

### **滤波器类型** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。根据 **设计方法** 中指定的设计，仿真低通、高通、带通或带阻滤波器类型。

### **实现** — 实现 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现，指定为以下之一：

- `LC Tee`：当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi`：当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function`：当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用双端口 S 参数对模拟滤波器建模。
- `Constant per carrier`：对在每个载波周围的整个包络频带内将全传输或全反射设置为常数的滤波器进行建模。**设计方法** 指定为 ideal。
- `Filter Domain`：使用与冲激响应的卷积对滤波器建模。**设计方法** 指定为 ideal。针对每个载波频率独立计算冲激响应，以捕获理想滤波响应。当理想滤波器的全传输与全反射之间的过渡发生在载波周围的包络频带内时，频域实现会正确捕获此过渡，直到 **冲激响应持续时间** 中指定的频率分辨率。

  **注意**

  由于因果性，反射信号和传输信号都包含半个冲激响应持续时间的延迟。当源电阻和负载电阻与滤波器参数中指定的值不同时，此延迟会损害滤波器性能。

默认情况下，对于理想滤波器，**实现** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，**实现** 为 `LC Tee`。

### **通带边缘频率** — 通带边缘频率 `2 GHz`（默认）| scalar

通带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`。

### **使用滤波器阶数实现** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **滤波器阶数** — 滤波器阶数 `3`（默认）| scalar

滤波器阶数，指定为 scalar。此阶数是 `lowpass` 或 `highpass` 中集总储能元件的数量。在 `bandpass` 或 `bandstop` 中，集总储能元件的数量是该值的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，对于 Tee 网络实现，电阻比 RloadRsource>Rratio；对于 Pi 网络实现，RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是
  通带纹波，单位为 dB。

#### 依赖关系

要启用此参数，请选择 **使用滤波器阶数实现**。

### **通带频率** — 低通和高通滤波器的通带频率 scalar

低通和高通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 scalar。默认情况下，对于 `Lowpass` 滤波器，通带频率为 `1 GHz`；对于 `Highpass` 滤波器，通带频率为 `2 GHz`。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Lowpass` 或 `Highpass`。

### **通带频率** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 2-tuple vector

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 2-tuple vector。此选项不适用于带阻滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| scalar

通带衰减，指定为以 dB 表示的 scalar。对于带通滤波器，此值同等应用于通带的两条边缘。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 2-tuple vector。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **阻带边缘频率** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 表示的 2-tuple vector。此选项不适用于理想带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`，并将 **滤波器类型** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| scalar

阻带衰减，指定为以 dB 表示的 scalar。对于带阻滤波器，此值同等应用于阻带的两条边缘。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| scalar

输入源电阻，指定为以 Ohms 表示的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| scalar

输出负载电阻，指定为以 Ohms 表示的 scalar。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **自动估计冲激响应持续时间** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此选项可自动估计相位噪声的冲激响应。清除此选项可使用 **冲激响应持续时间** 指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`，并将 **实现** 设置为 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10``s`（默认）| scalar

用于仿真相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 表示的 scalar。如果放大器是非线性的，则不能指定冲激响应。

**注意**

相位噪声剖面在频率上的分辨率受用于仿真它的冲激响应持续时间的限制。增加此持续时间可提高相位噪声剖面的精度。如果对于给定的冲激响应持续时间，相位噪声频率偏移分辨率过高，则会出现警告消息。此消息还会指定适合所需分辨率的最小持续时间

#### 依赖关系

要设置此参数，请清除 **自动估计冲激响应持续时间**。

### **导出** — 将滤波器设计保存到文件 按钮

使用此按钮将滤波器设计保存到文件。有效的文件类型为 `.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

## 所属库

RF Blockset / Circuit Envelope / Systems

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2017a 中引入**

### R2022b：使用相位噪声偏移频率估计冲激响应持续时间

IQ Modulator 模块使用 **相位噪声频率偏移 (Hz)** 参数估计冲激响应持续时间，并在您点击 **绘制相位噪声特性** 按钮时可视化相位噪声特性。

### R2021b：IQ Modulator 模块图标已更新

从 R2021b 开始，IQ Modulator 模块图标已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的、包含 IQ Modualtor 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

将基带信号转换为 RF 信号

`IQ Modulator` 将基带信号转换为 RF 信号，并对带有损伤的 IQ 调制器进行建模。`I` 表示信号的同相分量，`Q` 表示信号的正交相位分量。您可以使用 IQ Modulator 设计直接变频发射机。

IQ Modulator 模块的封装图标是动态的，并指示所应用噪声参数的当前状态。有关详细信息，请参阅 IQ Modulator 图标。
