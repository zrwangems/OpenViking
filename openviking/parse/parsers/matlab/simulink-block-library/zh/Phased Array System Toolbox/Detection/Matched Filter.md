---
type: simulink-block
title: 'Matched Filter'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'matchedfilter'
documentation_source_path: 'ref/matchedfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Matched Filter

## 端口

### 输入

### **X** — 输入信号 *M*×*N* 复值矩阵

输入信号，指定为 *M*×*N* 复值矩阵。匹配滤波沿第一维度应用。输入 `X` 和输出 `Y` 具有相同的维度。初始瞬态从滤波结果中移除。

输入矩阵第一维度的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数 *M* 长度复值列向量

匹配滤波器系数，指定为 *M* 长度复值列向量。

#### 依赖关系

要启用此端口，请将 **Source of coefficients** 下拉菜单设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 匹配滤波器输出 *M*×*N* 复值矩阵

匹配滤波器输出，返回为 *M*×*N* 复值矩阵。`Y` 的维度与 `X` 的维度相同。

**数据类型：** `double`

### **G** — 匹配滤波器增益 *N* 长度实值

匹配滤波器增益，返回为 *N* 实值矩阵。增益针对 `X` 的每一列计算。单位为 dB。

#### 依赖关系

要启用此端口，请选中 **Enable SNR gain output** 复选框。

**数据类型：** `double`

## 参数

### **Source of coefficients** — 匹配滤波器系数来源 `Property`（默认）| `Input port`

指定匹配滤波器系数来自 **Coefficients** 还是来自输入端口。

|  |  |
| --- | --- |
| `Property` | 匹配滤波器系数由 **Coefficients** 指定。 |
| `Input port` | 匹配滤波器系数通过输入端口 `Coeff` 指定。 |

### **Coefficients** — 匹配滤波器系数 `[1;1]`（默认）

将匹配滤波器系数指定为列向量。当您将 **Source of coefficients** 设置为 `Property` 时，此参数出现。

### **Spectrum window** — 频谱加权窗 `None`（默认）| `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

指定用于频谱加权的窗，使用以下之一

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

频谱加权通常与线性调频波形一起使用，以降低时域中的旁瓣电平。该模块内部计算窗长度以匹配 FFT 长度。

### **Spectrum window range (Hz)** — 频谱窗覆盖区域 `[0, 1e5]`（默认）

指定频谱窗应用的频谱区域（以赫兹为单位），为 1×2 向量，形式为 `[StartFrequency,EndFrequency]`。

请注意，`StartFrequency` 和 `EndFrequency` 均以基带测量。也就是说，它们位于 `[-Fs/2,Fs/2]` 范围内，其中 `Fs` 是在任何波形库模块中指定的采样率。参数 `StartFrequency` 必须小于 `EndFrequency`。

#### 依赖关系

当您将 **Spectrum window** 参数设置为除 `None` 以外的任何值时，此参数出现。

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。**Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **值：**正标量 |
| **默认：**`1e6` |

### **Sidelobe attenuation level** — 窗旁瓣衰减电平 `30`（默认值）

将 Chebyshev 或 Taylor 窗的旁瓣衰减电平（以 dB 为单位）指定为正标量。

#### 依赖关系

当您将 **Spectrum window** 设置为 `Chebyshev` 或 `Taylor` 时，此参数出现。

### **Kaiser shape parameter** — Kaiser 形状参数 `0.5`（默认值）

将影响 Kaiser 窗旁瓣衰减的参数指定为非负标量。有关详细信息，请参阅函数 `kaiser`。

#### 依赖关系

当您将 **Spectrum window** 参数设置为 `Kaiser` 时，此参数出现。

### **Number of constant level sidelobes** — Taylor 窗中近似恒定旁瓣的数量 `4`（默认值）

将 Taylor 窗中与主瓣相邻的近似恒定电平旁瓣的数量指定为正整数。

#### 依赖关系

当您将 **Spectrum window** 参数设置为 `Taylor` 时，此参数出现。

### **Enable SNR gain output** — 启用 SNR 增益输出 off（默认值）| on

选中此复选框可通过输出端口 `G` 获取匹配滤波器 SNR 增益。仅当选中此复选框时，输出端口才会出现。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认值）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

匹配滤波器

Matched Filter 模块实现输入信号的匹配滤波。匹配滤波是一种 FIR 滤波操作，其系数等于发射信号的时间反转采样。该滤波器可以在检测前提高 SNR。
