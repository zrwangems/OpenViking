---
type: simulink-block
title: 'Demodulator'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Systems'
documentation_page: 'demodulator'
documentation_source_path: 'ref/demodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Demodulator

## 端口

R2025b 中未记录。

## 参数

### 主

### **转换增益来源** — 转换增益的来源参数 `Available power gain`（默认）| `Open circuit voltage gain` | `Polynomial coefficients`

转换增益的来源参数，指定为以下之一：

- `Available power gain` —
  将输出端单边带（SSB）的功率与输入功率之比相关联。此计算假设负载和源端接匹配。
- `Open circuit voltage gain`
  — 开路电压增益参数的值，作为多项式压控电压源（VCVS）的线性电压增益项。
- `Polynomial coefficients`
  — 根据您指定的多项式实现非线性电压增益。

### **可用功率增益** — 输出端 SSB 功率与输入功率之比 `0 dB`（默认）| 以 dB 为单位的标量或无单位比值

输出端 SSB 功率与输入功率之比，指定为以 dB 为单位的标量或无单位比值。对于无单位比值，选择 **None**。

#### 依赖关系

要启用此参数，请将 **转换增益来源** 设置为 `Available power gain`。

### **开路电压增益** — 开路电压增益 `0 dB`（默认）| 标量

开路电压增益，指定为以 dB 为单位的标量。

#### 依赖关系

要启用此参数，请将 **转换增益来源** 设置为 `Open circuit voltage gain`。

### **多项式系数** — 指定电压增益的多项式系数 `[0 1]`（默认）| 向量

多项式系数，指定为向量。

多项式的阶数必须小于或等于 9。系数必须按升幂排列。如果向量有 10 个系数，
`[a0,a1,a2,
... a9]`，
则它所表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

*a*1
表示线性增益项。

例如，向量
`[a0,a1,a2,a3]`
指定关系 *Vout* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3。末尾的零会被省略。因此，
`[a0,a1,a2]`
定义的多项式与
`[a0,a1,a2,
0]` 相同。

默认值为 `[0,1]`，对应于线性关系 *Vout* =
*Vin*。

#### 依赖关系

要启用此参数，请将 **转换增益来源** 设置为 `Polynomial coefficients`。

### **本振频率** — 本振（LO）频率 `0` `Hz`（默认）| 标量

本振（LO）频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。

### **输入阻抗 (Ohm)** — 解调器的输入阻抗 `50`（默认）| 标量

解调器的输入阻抗，指定为以欧姆为单位的标量。

### **输出阻抗 (Ohm)** — 解调器的输出阻抗 `50`（默认）| 标量

解调器的输出阻抗，指定为以欧姆为单位的标量。

### **添加镜像抑制滤波器** — 镜像抑制（IR）滤波器参数 `off`（默认）| `on`

选择以添加 **IR filter** 参数选项卡。
清除以移除该选项卡。

### **添加通道选择滤波器** — 通道选择（CS）滤波器参数 `off`（默认）| `on`

选择以添加 **CS filter** 参数选项卡。
清除以移除该选项卡。

### **接地并隐藏负端子** — 接地并隐藏负电路端子 `on`（默认）| `off`

选择以在内部接地并隐藏负端子。清除以暴露负端子。当端子暴露时，您可以将它们连接到模型的其它部分。

### **编辑系统** — 断开解调器模块链接并用适当的值替换内部变量 按钮

使用此按钮断开解调器与库的链接。内部变量将被其值替换，这些值使用解调器参数估算。Demodulator 将成为一个仅保留图标的简单子系统掩码。

使用 **Edit System** 在不展开子系统的情况下编辑内部变量。使用 **Expand System** 在 Simulink® 画布中展开子系统并编辑该子系统。

### 损伤

### **LO to In isolation** — 本振电压与输入端口（RF）泄漏电压之间的幅度比 `inf` `dB`（默认）| 标量

本振电压幅度与输入端口（RF）泄漏电压幅度之比，指定为以 dB 为单位的标量。

### **Noise figure (dB)** — 输出与输入之间的信噪比 `0`（默认）| 标量

混频器的单边带噪声系数，指定为以 dB 为单位的标量。

要在带有 Demodulator 模块的电路包络模型中建模噪声，必须在 Configuration 模块对话框中选中 **Simulate noise** 复选框。

### **Add phase noise** — 添加相位噪声 `off`（默认）| `on`

选择此参数以向解调器系统添加相位噪声。

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `1`（默认）| 标量 | 向量 | 矩阵

相位噪声频率偏移，指定为标量、向量或矩阵，每个元素单位为 Hz。

如果指定矩阵，每列对应 CW 源的一个非直流载波频率。频率偏移值约束仿真的包络带宽。有关详细信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `-Inf`（默认）| 标量 | 向量 | 矩阵

相位噪声电平，指定为标量、向量或矩阵，元素单位为 dBc/Hz。

如果指定矩阵，每列对应 CW 源的一个非直流载波频率。频率偏移值约束仿真的包络带宽。有关详细信息，请参阅 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择以自动估计相位噪声的冲激响应。清除以使用 **Impulse response duration** 指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于仿真相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 为单位的标量。

**Note**

相位噪声剖面在频率上的分辨率受用于仿真它的冲激响应持续时间的限制。增加此持续时间以提高相位噪声剖面的精度。如果相位噪声频率偏移分辨率对于给定的冲激响应持续时间过高，将出现警告消息。此消息还会指定适合所需分辨率的最小持续时间。

#### 依赖关系

要设置此参数，请先清除 **Automatically estimate impulse response duration**。

### **Plot phase noise characteristics** — 相位噪声幅度响应按钮

该模块根据 **Impairments** 选项卡上指定的参数以及 Configuration 模块中的 **Envelope bandwidth** 参数（如果可用）或 **Phase noise frequency offset (Hz)** 参数中指定的值来绘制相位噪声特性。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### Nonlinearity

在 **Main** 选项卡中为 **Source of conversion gain** 选择 `Polynomial coefficients` 会移除 **Nonlinearity** 参数。

### **Nonlinear polynomial type** — 多项式非线性 `Even and odd order`（默认）| `Odd order`

多项式非线性，指定为以下之一：

- `Even and odd order`：除线性项外，Demodulator 还可以产生二阶和三阶互调频率。
- `Odd order`：Demodulator 仅生成“奇阶”互调频率。

  线性增益决定线性 *a*1 项。该模块根据 **IP3**、**1-dB gain compression power**、**Output saturation power** 和 **Gain compression at saturation** 中指定的值计算其余项。您指定的约束数量决定模型的阶数。该图显示了非线性 Demodulator 参数的图形化定义。

  输出功率与输入功率关系图显示了非线性解调器参数。

### **Intercept points convention** — 截点约定 `Input`（默认）| `Output`

截点约定，指定为 `Input`（输入参考）或 `Output`（输出参考）。将此规范用于截点 **IP2**、**IP3**、**1-dB gain compression power** 和 **Output saturation power**。

### **IP2** — 二阶截点 `inf` `dBm`（默认）| 标量

二阶截点，指定为以 dBm、W、mW 或 dBW 为单位的标量。默认值 `inf dBm` 对应于未指定的点。

#### 依赖关系

要启用此参数，请将 **Nonlinear polynomial type** 设置为 `Even and odd order`。

### **IP3** — 三阶截点 `inf dBm`（默认）| 标量

三阶截点，指定为以 dBm、W、mW 或 dBW 为单位的标量。默认值 `inf dBm` 对应于未指定的点。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf dBM`（默认）| 标量

1-dB 增益压缩功率，指定为以 dBm、W、mW 或 dBW 为单位的标量。

#### 依赖关系

要设置此参数，请在 **Nonlinear polynomial type** 中选择 `Odd order`。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf dBM`（默认）| 标量

1-dB 增益压缩功率，指定为以 dBm、W、mW 或 dBW 为单位的标量。

#### 依赖关系

要设置此参数，请在 **Nonlinear polynomial type** 中选择 `Odd order`。

### **Gain compression at saturation** — 饱和时的增益压缩 `inf dBm`（默认）| 标量

饱和时的增益压缩，指定为以 dBm、W、mW 或 dBW 为单位的标量。

当 **Nonlinear polynomial type** 为 `Odd order` 时，指定饱和时的增益压缩。

#### 依赖关系

要设置此参数，请先在 **Nonlinear polynomial type** 中选择 `Odd order`。然后，更改 **Output saturation power** 的默认值。

### IR Filter

在 **Main** 选项卡中选择 **Add Image Reject filter** 以查看 **IR Filter** 参数选项卡。

### **Design method** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。模拟 **Filter type** 中指定类型以及 **Implementation** 中指定模型的理想、Butterworth 或 Chebyshev 滤波器。

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。模拟 **Design method** 中指定设计的低通、高通、带通或带阻滤波器类型。

### **Implementation** — 实现方式 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现方式，指定为以下之一：

- `LC Tee`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器进行建模。
- `LC Pi`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器进行建模。
- `Transfer Function`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟滤波器进行建模。
- `Constant per carrier`：对滤波器进行建模，在每个载波周围的整个包络频带内，将全传输或全反射设为常数。**设计方法**指定为 ideal。
- `Frequency Domain`：使用脉冲响应卷积对理想滤波器进行建模。**设计方法**指定为 ideal。脉冲响应针对每个载波频率独立计算，以捕获理想滤波响应。当理想滤波器的全传输与全反射之间的过渡发生在载波周围的包络频带内时，频域实现会按照**脉冲响应持续时间**中指定的频率分辨率正确捕获该过渡。

  **注意**

  由于因果性，反射信号和传输信号都会包含脉冲响应持续时间一半的延迟。当源电阻和负载电阻与滤波器参数中指定的值不同时，该延迟会损害滤波器性能。

默认情况下，对于理想滤波器，**Implementation** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，**Implementation** 为 `LC Tee`。

### **Passband edge frequency** — 通带边缘频率 `2 GHz`（默认）| 标量

通带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Ideal`，并将**滤波器类型**设置为 `Lowpass` 或 `Highpass`。

### **Implement using filter order** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`。

### **Filter order** — 滤波器阶数 `3`（默认）| 标量

滤波器阶数，指定为标量。对于 `Lowpass` 或 `Highpass` 的**滤波器类型**，滤波器阶数是集总储能元件的数量。对于 `Bandpass` 或 `Bandstop` 的**滤波器类型**，集总储能元件的数量是滤波器阶数的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，Tee 网络实现的电阻比 RloadRsource>Rratio，Pi 网络实现的电阻比 RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是以 dB 为单位的通带纹波。

#### 依赖关系

要启用此参数，请选择**Implement using filter order**，并将**设计方法**设置为 `Butterworth` 或 `Chebyshev`。

### **Passband frequency** — 低通和高通滤波器的通带频率 标量

低通和高通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。对于 `Lowpass` 滤波器，默认通带频率为 `1 GHz`；对于 `Highpass` 滤波器，默认通带频率为 `2 GHz`。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`，并将**滤波器类型**设置为 `Lowpass` 或 `Highpass`。

### **Passband frequencies** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 二元组向量

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元组向量。此选项不适用于带阻滤波器。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`，并将**滤波器类型**设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| 标量

通带衰减，指定为以 dB 为单位的标量。对于带通滤波器，该值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9]GHz`（默认）| 二元向量

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元向量。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`，并将 **Filter type** 设置为 `Bandstop`。

### **阻带边缘频率** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 二元向量

理想带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元向量。此选项不适用于理想带通滤波器。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`，并将 **Filter type** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| 标量

阻带衰减，指定为以 dB 为单位的标量。对于带阻滤波器，该值同等应用于阻带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`，并将 **Filter type** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| 标量

输入源电阻，指定为以 Ohm 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| 标量

输出负载电阻，指定为以 Ohm 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### **自动估计冲激响应持续时间** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此项可自动估计相位噪声的冲激响应。清除此项可使用 **Impulse response duration** 手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`，并将 **Implementation** 设置为 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10``s`（默认）| 标量

用于模拟相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 为单位的标量。如果放大器是非线性的，则无法指定冲激响应。

**注意**

相位噪声剖面在频率上的分辨率受用于模拟它的冲激响应持续时间的限制。增加此持续时间可提高相位噪声剖面的精度。如果相位噪声频率偏移分辨率对于给定的冲激响应持续时间过高，则会出现警告消息。该消息还会指定适合所需分辨率的最小持续时间。

#### 依赖关系

要启用此参数，请清除 **Automatically estimate impulse response duration**。

### **导出** — 将滤波器设计保存到文件 按钮

使用此按钮可将滤波器设计保存到文件。有效的文件类型为 `.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### CS Filter

在 **Main** 选项卡中选择 **Add Channel Select filters** 以查看 **CS Filter** 参数。

### **设计方法** — 仿真类型 `Ideal`（默认）| `Butterworth` | `Chebyshev`

仿真类型。模拟 **Filter type** 中指定类型以及 **Implementation** 中指定模型的理想、Butterworth 或 Chebyshev 滤波器。

### **滤波器类型** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器。模拟 **Design method** 中指定设计的低通、高通、带通或带阻滤波器类型。

### **Implementation** — 实现方式 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现方式，指定为以下之一：

- `LC Tee`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器进行建模。
- `LC Pi`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器进行建模。
- `Transfer Function`：当**设计方法**为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟滤波器进行建模。
- `Constant per carrier`：对每个载波周围的整个包络频带内设置为恒定全传输或全反射的滤波器进行建模。**设计方法**指定为 ideal。
- `Frequency Domain`：使用与冲激响应的卷积对滤波器进行建模。**设计方法**指定为 ideal。冲激响应针对每个载波频率独立计算，以捕获理想滤波响应。当理想滤波器的全传输与全反射之间的过渡发生在载波周围的包络频带内时，频域实现能够按照**冲激响应持续时间**中指定的频率分辨率正确捕获该过渡。

  **注意**

  由于因果性，反射信号和传输信号都会包含冲激响应持续时间一半的延迟。当源电阻和负载电阻与滤波器参数中指定的值不同时，该延迟会损害滤波器性能。

默认情况下，对于理想滤波器，**Implementation** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，**Implementation** 为 `LC Tee`。

### **Passband edge frequency** — 通带边缘频率 `2 GHz`（默认）| 标量

通带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Ideal`。

### **Implement using filter order** — 使用滤波器阶数实现 `on`（默认）| `off`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`。

### **Filter order** — 滤波器阶数 `3`（默认）| 标量

滤波器阶数，指定为标量。该阶数是 `lowpass` 或 `highpass` 中集总储能元件的数量。在 `bandpass` 或 `bandstop` 中，集总储能元件的数量是该值的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，Tee 网络实现的电阻比 RloadRsource>Rratio，Pi 网络实现的电阻比 RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- Rp 是以 dB 为单位的通带纹波。

#### 依赖关系

要启用此参数，请选择 **Implement using filter order**。

### **Passband frequency** — 低通和高通滤波器的通带频率 标量

低通和高通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。默认情况下，`Lowpass` 滤波器的通带频率为 `1 GHz`，`Highpass` 滤波器的通带频率为 `2 GHz`。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`，并将**滤波器类型**设置为 `Lowpass` 或 `Highpass`。

### **Passband frequencies** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 二元组向量

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元组向量。此选项不适用于带阻滤波器。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`，并将**滤波器类型**设置为 `Bandpass`。

### **Passband attenuation (dB)** — 通带衰减 `10*log10(2)`（默认）| 标量

通带衰减，指定为以 dB 为单位的标量。对于带通滤波器，该值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将**设计方法**设置为 `Butterworth` 或 `Chebyshev`。

### **Stopband frequencies** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2 元向量

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2 元向量。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`，并将 **Filter type** 设置为 `Bandstop`。

### **Stopband edge frequencies** — 理想带阻滤波器的阻带边缘频率 `[2.1 2.9] GHz`（默认）| 2 元向量

理想带阻滤波器的阻带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的 2 元向量。此选项不适用于理想带通滤波器。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`，并将 **Filter type** 设置为 `Bandstop`。

### **Stopband attenuation (dB)** — 阻带衰减 `40`（默认）| 标量

阻带衰减，指定为以 dB 为单位的标量。对于带阻滤波器，此值同等应用于阻带的两个边缘。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`，并将 **Filter type** 设置为 `Bandstop`。

### **Source impedance (Ohm)** — 输入源电阻 `50`（默认）| 标量

输入源电阻，指定为以 Ohm 为单位的标量。

### **Load impedance (Ohm)** — 输出负载电阻 `50`（默认）| 标量

输出负载电阻，指定为以 Ohm 为单位的标量。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认）| `off`

选择此项可自动估计相位噪声的冲激响应。清除此项可使用 **Impulse response duration** 指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`，并将 **Implementation** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10` `s`（默认）| 标量

用于模拟相位噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 为单位的标量。如果放大器是非线性的，则无法指定冲激响应。

**注意**

相位噪声剖面在频率上的分辨率受用于模拟它的冲激响应持续时间的限制。增加此持续时间可提高相位噪声剖面的精度。如果对于给定的冲激响应持续时间，相位噪声频率偏移分辨率过高，则会出现警告消息。该消息还会指定适合所需分辨率的最小持续时间。

#### 依赖关系

要设置此参数，请先清除 **Automatically estimate impulse response duration**。

### **Export** — 将滤波器设计保存到文件 按钮

使用此按钮可将滤波器设计保存到文件。有效的文件类型为 `.mat` 和 `.txt`。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

## 所属库

RF Blockset / Circuit Envelope / Systems

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

### R2022b：使用相位噪声偏移频率估计冲激响应持续时间

Deodulator 模块使用 **Phase noise frequency offset (Hz)** 参数估计冲激响应持续时间，并在您点击 **Plot phase noise characteristics** 按钮时可视化相位噪声特性。

### R2021b：Demodulator 模块图标已更新

从 R2021b 开始，Deodulator 模块图标已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Demodualtor 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对 RF 到 RF 解调器进行建模

Demodulator 模块对 RF 到 RF 解调器进行建模。Demodulator 模块掩码图标是动态的，并指示所应用噪声参数的当前状态。有关详细信息，请参阅 Demodulator Icons。
