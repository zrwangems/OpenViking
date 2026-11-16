---
type: simulink-block
title: 'Range Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'rangeresponse'
documentation_source_path: 'ref/rangeresponse.html'
language: zh-CN
chinese_source: worker-translation
---

# Range Response

## 端口

### 输入

### **X** — 输入数据立方体 复值 *K*-by-1 列向量 | 复值 *K*-by-*L* 矩阵 | 复值 *K*-by-*N*-by-*L* 数组

输入数据立方体，指定为复值 *K*-by-1 列向量、复值 *K*-by-*L* 矩阵或复值 *K*-by-*N*-by-*L* 数组。

- *K* 是距离采样数或时间采样数。
- *N* 是独立通道数，例如传感器或方向。
- *L* 是输入信号中的脉冲数或扫频数。

参见 Radar Data Cube Concept。

每个包含 *K* 个元素的列向量均独立处理。

对于采用三角形扫频的 FMCW 波形，扫频在正斜率和负斜率之间交替。但是，Range Response 旨在处理斜率相同的连续扫频。要将 Range Response 模块应用于三角形扫频系统，请使用以下方法之一：

- 将 **Sweep slope** 参数值指定为正值，并使 `X` 仅对应于上扫频。获得多普勒值或速度值后，将其除以 2。
- 将 **Sweep slope** 参数值指定为负值，并使 `X` 仅对应于下扫频。获得多普勒值或速度值后，将其除以 2。

输入矩阵第一个维度的大小可以变化，以仿真不断变化的信号长度。例如，在脉冲重复频率可变的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Coeff** — 匹配滤波器系数 复值列向量

匹配滤波器系数，指定为复值列向量。该向量的长度必须小于或等于输入数据的行数 *K*。

#### 依赖关系

要启用此端口，请将 **Range processing method** 设置为 `Matched filter`。

**数据类型：** `double`
**复数支持：** 是

### **XRef** — 参考信号 复值 *K*-by-1 列向量

用于对输入信号进行去斜处理的参考信号，指定为复值 *K*-by-1 列向量。行数必须等于 `X` 第一个维度的长度。

#### 依赖关系

要启用此端口，请将 **Range processing method** 设置为 `FFT`，并选中 **Dechirp input signal** 参数。

**数据类型：** `double`
**复数支持：** 是

### 输出

### **Resp** — 距离响应数据立方体 复值 *M* 元素列向量 | 复值 *M*-by-*L* 矩阵 | 复值 *M*-by-*N* by-*L* 数组

距离响应数据立方体，返回为以下形式之一：

- 复值 *M* 元素列向量
- 复值 *M*-by-*L* 矩阵
- 复值 *M*-by-*N* by-*L* 数组

参见 Radar Data Cube Concept。*M* 的值取决于处理类型。

| Range processing method | Dechirp input signal | *M* 的值 |
| --- | --- | --- |
| `FFT` | `off` | 如果将 **Source of FFT length in range processing** 设置为 `Auto`，则 *M = K*，即 `x` 第一个维度的长度。否则，*M* 等于 **FFT length in range processing** 参数的值。 |
| `on` | *M* 等于输入信号的行数 *K*。 |
| `Matched filter` | N/A | *M* 等于输入信号的行数 *K*。 |

**数据类型：** `double`
**复数支持：** 是

### **Range** — 沿距离维度的距离值 实值 *M*-by-1 列向量

沿 **Resp** 输出数据端口第一个维度的距离值，指定为实值 *M*-by-1 列向量。该量定义了 `Resp` 输出端口数据第一个维度上的距离值。单位为米。

**数据类型：** `double`

## 参数

### **Measurement mode** — 测量模式 `Monostatic`（默认）| `Bistatic`

测量模式，指定为 `Monostatic` 或 `Bistatic`。设置为 `Monostatic` 时，距离测量值为单基地距离。设置为 `Bistatic` 时，距离测量值为双基地距离。

**示例：** `Bistatic`

**数据类型：** `char` | `string`

### **Range processing method** — 距离处理方法 `Matched filter`（默认）| `FFT`

距离处理方法，指定为 `Matched filter` 或 `FFT`。

|  |  |
| --- | --- |
| `Matched filter` | 模块对输入信号应用匹配滤波器。这种方法通常用于脉冲信号，其中匹配滤波器是发射信号的时间反转。 |
| `FFT` | 模块对输入信号应用 FFT。这种方法通常用于 FMCW 信号和线性调频脉冲信号。 |

**数据类型：** `char`

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选中此参数可从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **FM sweep slope (Hz/s)** — 调频扫频斜率 `1e9`（默认）| 标量

将线性调频扫频的斜率指定为标量。此参数必须与端口 `X` 中输入数据的实际扫频相匹配。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `double`

### **Dechirp input signal** — 启用输入信号的去斜处理 `on`（默认）| `off`

选中此参数可启用输入信号的去斜处理。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `Boolean`

### **Source of FFT length in range processing** — 距离处理的 FFT 长度来源 `Auto`（默认）| `Property`

距离处理的 FFT 长度来源，指定为 `Auto` 或 `Property`。

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入数据立方体的行数。 |
| `Property` | 在 **FFT length in range processing** 参数中指定 FFT 长度。 |

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `char`

### **FFT length in range processing** — 距离处理的 FFT 长度 `1024`（默认）| 正整数

距离处理的 FFT 长度，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`，并将 **Source of FFT length in range processing** 设置为 `Property`。

**数据类型：** `double`

### **Range processing window** — 距离 FFT 加权窗 `None`（默认）| `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

距离 FFT 加权窗，指定为 `None`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor`。

如果将此属性设置为 `Taylor`，生成的 Taylor 窗在主瓣旁边具有四个几乎恒定的旁瓣。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `char`

### **Range sidelobe attenuation level** — 距离处理的旁瓣衰减 `30`（默认）| 正标量

距离处理的旁瓣衰减，指定为正标量。单位为 dB。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`，并将 **Range processing window** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor`。

**数据类型：** `double`

### **Set reference range at center** — 将参考距离设置在距离网格中心 `on`（默认）| `off`

将参考距离设置在距离网格中心，指定为 `on` 或 `off`。选中此复选框后，可以将参考距离设置在距离网格的中心。否则，参考距离设置为距离网格的起始位置。

#### 依赖关系

要启用此属性，请将 **Range processing method** 设置为 `FFT`。

### **Reference range (m)** — 距离网格的参考距离 `0.0`（默认）| 非负标量

距离网格的参考距离，指定为非负标量。

- 如果将 **Range processing method** 参数设置为 `Matched filter`，则参考距离设置为距离网格的起始位置。
- 如果将 **Range processing method** 属性设置为 `FFT`，则参考距离取决于 **Set reference range at center** 复选框。

  - 当选中 **Set reference range at center** 复选框时，参考距离设置为距离网格的中心。
  - 如果未选中 **Set reference range at center** 复选框，则参考距离设置为距离网格的起始位置。

  单位为米。

**示例：** `1000.0`

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真方式，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行速度更快。

解释执行在开发和调整模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。对于长时间仿真，使用生成代码比解释执行运行得更快。您可以在不重新编译的情况下重复运行，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，通过 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块均被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未提供相关文档。

## 扩展功能

R2025b 中未提供相关文档。

## 版本历史

**在 R2017a 中引入**

## 描述

距离响应

Range Response 模块使用匹配滤波器或基于 FFT 的算法，对快时间（距离）数据执行距离滤波。其输出通常用作检测器的输入。匹配滤波可提高脉冲波形的 SNR。对于连续调频信号，FFT 处理可提取 FMCW 波形的拍频。拍频与距离直接相关。

模块的输入是雷达数据立方体。数据立方体的组织方式遵循 Phased Array System Toolbox™ 约定。立方体的第一个维度表示接收信号的快时间采样或距离。第二个维度表示多个空间通道，例如不同的传感器或波束。第三个维度为慢时间，表示脉冲。距离滤波沿立方体的快时间维度执行，不沿其他维度进行处理。如果数据仅包含一个通道或脉冲，则数据立方体的维度可以少于三个。由于此对象不执行多普勒处理，因此可以用它处理非相干雷达脉冲。

模块的输出也是数据立方体，其维度数与输入相同。其第一个维度包含距离处理后的数据，但长度可能不同于输入数据立方体的第一个维度。
