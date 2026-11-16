---
type: simulink-block
title: 'Single-Band Parametric EQ'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'singlebandparametriceq'
documentation_source_path: 'ref/singlebandparametriceq.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Band Parametric EQ

## 端口

### 输入

### **x** — 输入信号矩阵 | 1-D 向量

- 矩阵输入 –– 输入的每一列被视为一个独立通道。
- 1-D 向量输入 –– 输入被视为一个信号通道。

除非指定其他输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **Fc** — 中心频率 (Hz) 标量

将中心频率指定为一个正标量，该标量小于输入信号采样率的一半。

#### 依赖项

要启用此端口，请为 **中心频率 (Hz)** 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **BW** — 带宽 (Hz) 标量

将滤波器带宽指定为一个正标量，该标量小于或等于输入信号采样率的一半和 20 kHz。

#### 依赖项

要启用此端口，请为 **滤波器设定** 选择 `Bandwidth and Center Frequency`，并为 **滤波器带宽 (Hz)** 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **GdB** — 峰值或陷波增益 (dB) 标量

将峰值或陷波增益以 dB 为单位指定为一个标量。

#### 依赖项

要启用此端口，请为 **峰值增益 (dB)** 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **Q** — 品质因数标量

将品质因数指定为一个正标量。

#### 依赖项

要启用此端口，请为 **滤波器设定** 选择 `Quality factor and center frequency`，并为 **品质因数** 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### 输出

### **Port\_1** — 输出信号矩阵

Single-Band Parametric EQ 模块输出与输入信号具有相同数据类型的信号。输出的大小取决于输入的大小：

- 矩阵输入 –– 该模块输出与输入信号大小和数据类型相同的矩阵。
- 1-D 向量输入 –– 该模块输出一个 *N*×1 矩阵（列向量），其中 *N* 是 1-D 向量中的元素数。

**数据类型：** `single` | `double`

## 参数

如果某个参数被列为可调，则可以在仿真期间更改其值。

### **滤波器阶数** — 滤波器的阶数 `2` (默认) | 正的偶数标量

**可调：** 否

### **滤波器设定** — 指定用于设计滤波器的参数 `Bandwidth and center frequency` (默认) | `Quality factor and center frequency`

- `Bandwidth and center frequency` –– 使用 **滤波器带宽 (Hz)**、**中心频率 (Hz)** 和 **峰值增益 (dB)** 设计滤波器。
- `Quality factor and center frequency` –– 使用 **中心频率 (Hz)**、**峰值增益 (dB)** 和 **品质因数** 设计滤波器。

**可调：** 否

### **中心频率 (Hz)** — 滤波器的中心频率 `11025` (默认) | 正标量

将中心频率指定为一个正标量，该标量小于输入信号采样率的一半。

要从输入端口指定 **中心频率 (Hz)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **滤波器带宽 (Hz)** — 滤波器的带宽 `2205` (默认) | [0, max(fs/2, 20,000)] 范围内的正标量

将滤波器带宽指定为一个正标量，该标量小于或等于输入信号采样率的一半或 20 kHz 中的较大者。

要从输入端口指定 **滤波器带宽 (Hz)**，请为该参数选择 **Specify from input port**。

**可调：** 是

#### 依赖项

要启用此参数，请将 **滤波器设定** 设置为 `Bandwidth and center frequency`。

### **品质因数** — 品质因数 `5` (默认) | [0.1, 20] 范围内的标量

将品质因数指定为 [0.1, 20] 范围内的标量。

要从输入端口指定 **品质因数**，请为该参数选择 **Specify from input port**。

**可调：** 是

#### 依赖项

要启用此参数，请将 **滤波器设定** 设置为 `Quality factor and center frequency`。

### **峰值增益 (dB)** — 滤波器的峰值或陷波增益 `6.0206` (默认) | [−30, 30] 范围内的标量

将峰值增益以 dB 为单位指定为 [−30, 30] 范围内的标量。

**可调：** 是

### **从输入继承采样率** — 指定输入采样率的来源 on (默认) | off

选中此参数时，该模块从输入信号继承其采样率。清除此参数时，在 **输入采样率 (Hz)** 中指定采样率。

**可调：** 否

### **输入采样率 (Hz)** — 输入的采样率 `44100` (默认) | 标量

**可调：** 是

#### 依赖项

要启用此参数，请清除 **从输入继承采样率** 参数。

### **仿真方式** — 指定要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。
- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但与 `Interpreted execution` 相比，后续仿真的速度更快。

**可调：** 否

## 所属库

Audio Toolbox / Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2022b：**输入采样率 (Hz)** 参数可调

您可以在仿真期间更改 **输入采样率 (Hz)** 参数的值。

## 描述

二阶参数均衡器滤波器

Single-Band Parametric EQ 模块使用指定的中心频率、带宽和峰值（陷波）增益对输入信号的每个通道随时间进行滤波。该模块提供可调滤波器设计参数，使您能够在仿真运行时调整滤波器特性。该滤波器使用 `designParamEQ` 设计，并使用 `dsp.SOSFilter` 实现。

该模块支持可变大小输入，使您能够在仿真期间更改通道长度。要启用可变大小输入，请清除 **从输入继承采样率** 参数。通道数必须保持不变。
