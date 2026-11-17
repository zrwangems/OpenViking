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

### **X** — 输入数据立方体 复值 *K*×1 列向量 | 复值 *K*×*L* 矩阵 | 复值 *K*×*N*×*L* 数组

输入数据立方体，指定为复值 *K*×1 列向量、复值 *K*×*L* 矩阵或复值 *K*×*N*×*L* 数组。

- *K* 是距离或时间采样数。
- *N* 是独立通道数，例如传感器或方向。
- *L* 是输入信号中的脉冲数或扫描数。

参见 Radar Data Cube Concept。

每个 *K* 元素列向量独立处理。

对于具有三角扫描的 FMCW 波形，扫描在正斜率和负斜率之间交替。然而，Range Response 设计用于处理相同斜率的连续扫描。要将 Range Response 模块应用于三角扫描系统，请使用以下方法之一：

- 指定正的 **Sweep slope** 参数值，其中 `X` 仅对应上扫。获得多普勒或速度值后，将其除以 2。
- 指定负的 **Sweep slope** 参数值，其中 `X` 仅对应下扫。获得多普勒或速度值后，将其除以 2。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Coeff** — 匹配滤波器系数 复值列向量

匹配滤波器系数，指定为复值列向量。向量的长度必须小于或等于输入数据的行数 *K*。

#### 依赖关系

要启用此端口，请将 **Range processing method** 设置为 `Matched filter`。

**数据类型：** `double`
**复数支持：** 是

### **XRef** — 参考信号 复值 *K*×1 列向量

用于对输入信号进行去啁啾的参考信号，指定为复值 *K*×1 列向量。行数必须等于 `X` 第一维的长度。

#### 依赖关系

要启用此端口，请将 **Range processing method** 设置为 `FFT` 并选中 **Dechirp input signal** 参数。

**数据类型：** `double`
**复数支持：** 是
### 输出

### **Resp** — 距离响应数据立方体 复值 *M* 元素列向量 | 复值 *M*×*L* 矩阵 | 复值 *M*×*N*×*L* 数组

距离响应数据立方体，返回为

- 复值 *M* 元素列向量
- 复值 *M*×*L* 矩阵
- 复值 *M*×*N*×*L* 数组

参见 Radar Data Cube Concept。*M* 的值取决于处理类型

| 距离处理方法 | 去啁啾输入信号 | *M* 的值 |
| --- | --- | --- |
| `FFT` | `off` | 如果将 **Source of FFT length in range processing** 设置为 `Auto`，则 *M = K*，即 `x` 第一维的长度。否则，*M* 等于 **FFT length in range processing** 参数的值。 |
| `on` | *M* 等于输入信号的行数 *K*。 |
| `Matched filter` | 不适用 | *M* 等于输入信号的行数 *K*。 |

**数据类型：** `double`
**复数支持：** 是

### **Range** — 沿距离维度的距离值 实值 *M*×1 列向量

沿 **Resp** 输出数据端口第一维度的距离值，指定为实值 *M*×1 列向量。此量定义了 `Resp` 输出端口数据第一维度的距离值。单位为米。

**数据类型：** `double`

## 参数

### **Measurement mode** — 测量模式 `Monostatic`（默认）| `Bistatic`

测量模式，指定为 `Monostatic` 或 `Bistatic`。当设置为 `Monostatic` 时，距离测量为单站距离。当设置为 `Bistatic` 时，距离测量为双站距离。

**示例：** `Bistatic`

**数据类型：** `char` | `string`

### **Range processing method** — 距离处理方法 `Matched filter`（默认）| `FFT`

距离处理方法，指定为 `Matched filter` 或 `FFT`。

|  |  |
| --- | --- |
| `Matched filter` | 该模块对输入信号应用匹配滤波器。此方法通常用于脉冲信号，其中匹配滤波器是发射信号的时间反转。 |
| `FFT` | 该模块对输入信号应用 FFT。此方法通常用于 FMCW 和线性调频脉冲信号。 |

**数据类型：** `char`

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **FM sweep slope (Hz/s)** — FM 扫频斜率 `1e9`（默认）| 标量

将线性 FM 扫频的斜率指定为标量。此参数必须与端口 `X` 中输入数据的实际扫频匹配。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `double`

### **Dechirp input signal** — 启用输入信号去啁啾 `on`（默认）| `off`

选择此参数以启用输入信号去啁啾。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `Boolean`

### **Source of FFT length in range processing** — 距离处理中 FFT 长度的来源 `Auto`（默认）| `Property`

距离处理中 FFT 长度的来源，指定为 `Auto` 或 `Property`

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入数据立方体的行数。 |
| `Property` | 在 **FFT length in range processing** 参数中指定 FFT 长度。 |

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `char`

### **FFT length in range processing** — 距离处理 FFT 长度 `1024`（默认）| 正整数

用于距离处理的 FFT 长度，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`，并将 **Source of FFT length in range processing** 设置为 `Property`。

**数据类型：** `double`

### **Range processing window** — 距离 FFT 加权窗 `None`（默认）| `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

距离 FFT 加权窗，指定为 `None`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor`。

如果将此属性设置为 `Taylor`，则生成的 Taylor 窗在主瓣旁边具有四个近似恒定的旁瓣。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`。

**数据类型：** `char`

### **Range sidelobe attenuation level** — 距离处理旁瓣衰减 `30`（默认）| 正标量

距离处理旁瓣衰减，指定为正标量。单位为 dB。

#### 依赖关系

要启用此参数，请将 **Range processing method** 设置为 `FFT`，并将 **Range processing window** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor`。

**数据类型：** `double`

### **Set reference range at center** — 在距离网格中心设置参考距离 `on`（默认）| `off`

在距离网格中心设置参考距离，指定为 `on` 或 `off`。选中此复选框后，可以将参考距离设置在距离网格的中心。否则，参考距离设置为距离网格的起始位置。

#### 依赖关系

要启用此属性，请将 **Range processing method** 设置为 `FFT`。

### **Reference range (m)** — 距离网格的参考距离 `0.0`（默认）| 非负标量

距离网格的参考距离，指定为非负标量。

- 如果将 **Range processing method** 参数设置为 `Matched filter`，则参考距离设置为距离网格的起始位置。
- 如果将 **Range processing method** 属性设置为 `FFT`，则参考距离取决于 **Set reference range at center** 复选框。

  - 选中 **Set reference range at center** 复选框时，参考距离设置为距离网格的中心。
  - 如果未选中 **Set reference range at center** 复选框，则参考距离设置为距离网格的起始位置。

  单位为米。

**示例：** `1000.0`

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

距离响应

距离响应模块对快时间（距离）数据执行距离滤波，使用匹配滤波器或基于 FFT 的算法。输出通常用作检测器的输入。匹配滤波可改善脉冲波形的 SNR。对于连续 FM 信号，FFT 处理可提取 FMCW 波形的拍频。拍频与距离直接相关。

该模块的输入是雷达数据立方体。数据立方体的组织遵循 Phased Array System Toolbox™ 约定。立方体的第一维表示接收信号的快时间采样或距离。第二维表示多个空间通道，例如不同传感器或波束。第三维，慢时间，表示脉冲。距离滤波沿立方体的快时间维度进行。不执行沿其他维度的处理。如果数据仅包含一个通道或脉冲，数据立方体可以包含少于三个维度。由于此对象不执行多普勒处理，您可以使用它来处理非相干雷达脉冲。

该模块的输出也是一个数据立方体，其维度数与输入相同。其第一维包含经过距离处理的数据，但其长度可以与输入数据立方体的第一维不同。
