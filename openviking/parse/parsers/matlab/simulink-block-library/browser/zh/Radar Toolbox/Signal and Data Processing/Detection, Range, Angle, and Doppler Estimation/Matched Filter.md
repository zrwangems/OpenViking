---
type: simulink-block
title: 'Matched Filter'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'matchedfilter'
documentation_source_path: '../phased/ref/matchedfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Matched Filter

## 端口

### 输入

### **X** — 输入信号 *M*×*N* 复数值矩阵

输入信号，指定为 *M*×*N* 复数值矩阵。
匹配滤波沿第一个维度应用。输入
`X` 和输出 `Y` 具有相同的维度。初始瞬态从滤波结果中移除。

输入矩阵第一个维度的大小可以变化，以模拟变化的信号长度。
例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数，长度为 *M* 的复数列向量

匹配滤波器系数，指定为长度为 *M* 的复数列向量。

#### 依赖项

要启用此端口，请将 **系数来源** 下拉菜单设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 匹配滤波器输出 *M*×*N* 复数值矩阵

匹配滤波器输出，返回为 *M*×*N* 复数值矩阵。
`Y` 的维度与 `X` 的维度相同。

**数据类型：** `double`

### **G** — 匹配滤波器增益，长度为 *N* 的实数值

匹配滤波器增益，返回为长度为 *N* 的实数值矩阵。针对 `X` 的每一列计算增益。
单位是 dB。

#### 依赖项

要启用此端口，请选中 **启用 SNR 增益输出** 复选框。

**数据类型：** `double`

## 参数

### **系数来源** — 匹配滤波器系数的来源 `Property` (default) | `Input port`

指定匹配滤波器系数来自 **系数** 还是来自输入端口。

|  |  |
| --- | --- |
| `Property` | 匹配滤波器系数由 **系数** 指定。 |
| `Input port` | 匹配滤波器系数通过输入端口 `Coeff` 指定。 |

### **系数** — 匹配滤波器系数 `[1;1]` (default)

将匹配滤波器系数指定为列向量。当您将 **系数来源** 设置为 `Property` 时，此参数将出现。

### **频谱窗** — 用于频谱加权的窗 `None` (default) | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

使用以下项之一指定用于频谱加权的窗

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

频谱加权通常与线性 FM 波形一起使用，以降低时域中的旁瓣电平。该模块在内部计算窗长度以匹配 FFT 长度。

### **频谱窗范围 (Hz)** — 频谱窗覆盖区域 `[0, 1e5]` (default)

以赫兹为单位，将应用频谱窗的频谱区域指定为 1×2 向量，形式为 `[StartFrequency,EndFrequency]`。

请注意，`StartFrequency` 和 `EndFrequency` 均在基带中测量。也就是说，它们位于 `[-Fs/2,Fs/2]` 内，其中 `Fs` 是在任何波形库模块中指定的采样率。参数 `StartFrequency` 必须小于 `EndFrequency`。

#### 依赖项

当您将 **频谱窗** 参数设置为除 `None` 以外的任何值时，此参数将出现。

### **继承采样率** — 从上游模块继承采样率 on (default) | off

选择此参数以从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **采样率 (Hz)** — 输出波形的采样率 `1e6` (default) | 正标量

输出波形的采样率，指定为正标量。**采样率 (Hz)** 与 **脉冲重复频率 (Hz)** 向量中每个元素的比值必须为整数。此限制等效于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **旁瓣衰减电平** — 窗的旁瓣衰减电平 `30` (default)

将 Chebyshev 或 Taylor 窗的旁瓣衰减电平（以 dB 为单位）指定为正标量。

#### 依赖项

当您将 **频谱窗** 设置为 `Chebyshev` 或 `Taylor` 时，此参数将出现。

### **Kaiser 形状参数** — Kaiser 形状参数 `0.5` (default)

将影响 Kaiser 窗旁瓣衰减的参数指定为非负标量。有关更多详细信息，请参阅函数 `kaiser`。

#### 依赖项

当您将 **频谱窗** 参数设置为 `Kaiser` 时，此参数将出现。

### **恒定电平旁瓣数量** — Taylor 窗中几乎恒定旁瓣的数量 `4` (default)

将 Taylor 窗中与主瓣相邻的几乎恒定电平旁瓣的数量指定为正整数。

#### 依赖项

当您将 **频谱窗** 参数设置为 `Taylor` 时，此参数将出现。

### **启用 SNR 增益输出** — 启用 SNR 增益输出 off (default) | on

选中此复选框以通过输出端口 `G` 获取匹配滤波器 SNR 增益。仅当选中此复选框时，输出端口才会出现。

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (default) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层的 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行该模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
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

Matched Filter 模块实现输入信号的匹配滤波。匹配滤波是一种 FIR 滤波操作，其系数等于发射信号的时间反转样本。该滤波器可以在检测前提高 SNR。
