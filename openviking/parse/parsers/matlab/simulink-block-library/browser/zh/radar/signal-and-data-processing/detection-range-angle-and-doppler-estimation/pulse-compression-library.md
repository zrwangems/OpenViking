---
type: simulink-block
title: 'Pulse Compression Library'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'pulsecompressionlibrary'
documentation_source_path: 'ref/pulsecompressionlibrary.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Compression Library

## 端口

### 输入

### **X** — 输入信号 复数值 *K*-by-*L* 矩阵 | 复数值 *K*-by-*N* 矩阵 | 复数值 *K*-by-*N*-by-*L* 数组

输入信号，指定为复数值 *K*-by-*L* 矩阵、复数值 *K*-by-*N* 矩阵或复数值 *K*-by-*N*-by-*L* 数组。*K* 表示快时间样本数，*L* 表示脉冲数，*N* 表示通道数。通道可以是阵元或波束。

**Data Types:** `double`
**Complex Number Support:** Yes

### **Idx** — 处理规格的索引 正整数

脉冲压缩库中处理规格的索引，指定为正整数。

**Data Types:** `double`
### 输出

### **Y** — 输出信号 复数值 *K*-by-*L* 矩阵 | 复数值 *K*-by-*N* 矩阵 | 复数值 *K*-by-*N*-by-*L* 数组

输出信号，返回为复数值 *M*-by-*L* 矩阵、复数值 *M*-by-*N* 矩阵或复数值 *M*-by-*N*-by-*L* 数组。*M* 表示快时间样本数，*L* 表示脉冲数，*N* 表示通道数。通道可以是阵元或波束。`Y` 的维度数与 `X` 的维度数一致。

当执行匹配滤波时，*M* 等于 `X` 的行数。当执行拉伸处理且您为 `RangeFFTLength` 名称-值对指定值时，*M* 设置为 `RangeFFTLength` 的值。当您未指定 `RangeFFTLength` 时，*M* 等于 `X` 的行数。

**Data Types:** `double`
**Complex Number Support:** Yes

### **Range** — 样本距离 实数值长度-*M* 向量

样本距离，返回为实数值长度-*M* 向量，其中 *M* 是 `Y` 的行数。该向量的元素表示对应于 `Y` 各行的距离。

**Data Types:** `double`

## 参数

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**Example:** `3e8`

**Data Types:** `double`

### **Specification of each waveform in the library** — 库中脉冲波形的规格 `{{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}` (默认) | 元胞数组

脉冲波形，指定为元胞数组。数组的每个元胞包含一个波形的规格。每个波形规格也是一个包含该波形参数的元胞数组。

```
{{Waveform 1 Specification},{Waveform 2 Specification},{Waveform 3 Specification}, ...}
```

此模块支持四种内置波形，也允许您指定自定义波形。每个内置波形说明符由一个波形标识符后跟若干名称-值对组成，用于设置该波形的属性。

**内置波形**

|  |  |  |
| --- | --- | --- |
| 波形类型 | 波形标识符 | 波形名称-值对参数 |
| Linear FM | `'LinearFM'` | 参见 Linear FM Waveform Arguments |
| Phase coded | `'PhaseCoded'` | 参见 Phase-Coded Waveform Arguments |
| Rectangular | `'Rectangular'` | 参见 Rectangular Waveform Arguments |
| Stepped FM | `'SteppedFM'` | 参见 Stepped FM Waveform Arguments |

您可以使用用户自定义函数创建自定义波形。函数的第一个输入参数必须是采样率。在波形规格的第一个元胞中使用函数句柄代替波形标识符。其余元胞包含除采样率之外的所有函数输入参数。按传入函数的顺序指定所有输入参数。该函数必须至少有一个输出参数，以列向量形式返回每个脉冲的样本。仅当您将 **Simulate using** 设置为 `Interpreted Execution` 时，才能创建自定义波形。

### **Pulse compression specifications** — 指定脉冲压缩类型 `{{'MatchedFilter','SpectrumWindow','None'},{'StretchProcessor','RangeSpan',200,'ReferenceRange',5e3,'RangeWindow','None'}}` (默认) | 元胞数组

波形处理类型和参数，指定为处理规格的元胞数组。每个处理规格本身是一个包含处理类型和处理参数的元胞数组。

```
{{Processing 1 Specification},{Processing 2 Specification},{Processing 3 Specification}, ...}
```

每个处理规格指示要应用于波形的处理类型以及处理所需的参数。

```
{processtype,Name,Value,...}
```

`processtype` 的值为 `'MatchedFilter'` 或 `'StretchProcessor'`。

- `'MatchedFilter'` – 名称-值对参数为

  - `'Coefficients'`,`coeff` – 将匹配滤波器系数 `coeff` 指定为列向量。未指定时，系数根据 `WaveformSpecification` 属性计算。对于包含多个脉冲的 Stepped FM 波形，`coeff` 对应于每个脉冲，直到脉冲索引 `idx` 改变。
  - `'SpectrumWindow'`,`sw` – 指定应用于波形的频谱加权窗 `sw`。窗值为 `'None'`、`'Hamming'`、`'Chebyshev'`、`'Hann'`、`'Kaiser'` 和 `'Taylor'` 之一。默认值为 `'None'`。
  - `'SidelobeAttenuation'`,`slb` – 将 Chebyshev 或 Taylor 窗的旁瓣衰减 `slb` 指定为正标量。默认值为 30。当您将 `'SpectrumWindow'` 设置为 `'Chebyshev'` 或 `'Taylor'` 时，此参数适用。
  - `'Beta'`,`beta` – 将确定 Kaiser 窗旁瓣衰减的参数 `beta` 指定为非负标量。默认值为 0.5。当您将 `'SpectrumWindow'` 设置为 `'Kaiser'` 时，此参数适用。
  - `'Nbar'`,`nbar` – 将 Taylor 窗中邻近主瓣的近似恒定电平旁瓣数 `nbar` 指定为正整数。默认值为 4。当您将 `'SpectrumWindow'` 设置为 `'Taylor'` 时，此参数适用。
  - `'SpectrumRange'`,`sr` – 将应用频谱窗的频谱区域 `sr` 指定为形式为 `[StartFrequency EndFrequency]` 的 1-by-2 向量。默认值为 [0 1.0e5]。当您将 `'SpectrumWindow'` 设置为除 'None' 之外的任何值时，此参数适用。单位为 Hz。

    `StartFrequency` 和 `EndFrequency` 均在基带区域 [-*Fs*/2 *Fs*/2] 内测量。*Fs* 是由 `SampleRate` 属性指定的采样率。`StartFrequency` 不能大于 `EndFrequency`。
- `'StretchProcessor'` – 名称-值对参数为

  - `'ReferenceRange'`,`refrng` – 将感兴趣距离的中心 `refrng` 指定为正标量。`refrng` 必须在一个脉冲的非模糊距离内。默认值为 5000。单位为米。
  - `'RangeSpan'`,`rngspan` – 指定感兴趣距离的跨度 `rngspan`，为正标量。距离跨度以 `'ReferenceRange'` 参数中指定的距离值为中心。默认值为 500。单位为米。
  - `'RangeFFTLength'`,`len` – 将距离域中的 FFT 长度 `len` 指定为正整数。如果未指定，默认值与输入数据长度相同。
  - `'RangeWindow'`,`rw` 指定用于距离处理的窗 `rw`，为 `'None'`、`'Hamming'`、`'Chebyshev'`、`'Hann'`、`'Kaiser'` 和 `'Taylor'` 之一。默认值为 `'None'`。

**Data Types:** `cell`

### **Inherit sample rate** — 从上游模块继承采样率 on (默认) | off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**Data Types:** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6` (默认) | 正实数值标量

将信号采样率指定为正标量。单位为 Hz。

#### Dependencies

要启用此参数，请清除 **Inherit sample rate** 复选框。

**Data Types:** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

解释执行在开发和调优模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

## 所属库

Radar Toolbox

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## 版本历史

**Introduced in R2021a**

## 描述

脉冲压缩规格库

Pulse Compression Library 模块使用脉冲压缩执行距离处理。脉冲压缩技术包括匹配滤波和拉伸处理。该模块允许您创建不同脉冲压缩规格的库。输出是滤波器响应，由矩阵或三维数组组成，其行表示距离门。
