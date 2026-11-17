---
type: simulink-block
title: 'DC Blocker'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'dcblocker'
documentation_source_path: '../comm/../dsp/ref/dcblocker.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Blocker

## 端口

### 输入

### **Input** — 输入信号 标量 | 向量 | 矩阵

指定包含直流分量的输入信号，可以是标量、向量或矩阵。

如果输入是定点类型，它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 去除直流分量后的输出信号 标量 | 向量 | 矩阵

去除直流分量后的输出信号。当输出为定点类型时，仅为有符号类型。

输出信号的大小、数据类型和复数特性与输入信号相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

## 参数

### **Algorithm for estimating DC offset** — 直流偏移估计算法 `IIR`（默认）| `FIR` | `CIC` | `Subtract mean`

指定用于估计直流偏移的算法。从以下选项中选择：

- `IIR` 使用基于窄带低通椭圆滤波器的递归估计。该算法通常比 FIR 使用更少的内存，并且更高效。
- `FIR` 使用非递归的滑动平均估计。该算法通常比 IIR 使用更多的内存，并且效率较低。
- `CIC` 使用不包含任何乘法器的低通滤波器。如果算法为 `CIC`，则必须向 DC Blocker 输入定点数据。
- `Subtract mean` 计算输入矩阵各列的均值，并从输入中减去这些均值。该方法不在输入之间保留状态。例如，如果输入为 `[1 2 3 4; 3 4 5 6]`，则处于 `Subtract mean` 模式的 DC Blocker 模块输出 `[-1 -1 -1 -1; 1 1 1 1]`。

### **Normalized bandwidth of lowpass IIR or CIC filter** — 归一化带宽 `0.001`（默认）| 范围 (0 1) 内的实标量

将归一化滤波器带宽指定为大于 0 且小于 1 的实标量。

#### 依赖关系

仅当估计算法设置为 `IIR` 或 `CIC` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Order of lowpass IIR elliptic filter** — 低通 IIR 椭圆滤波器的阶数 `6`（默认）| 大于 3 的整数

将低通 IIR 椭圆滤波器的滤波器阶数指定为大于 3 的整数。

#### 依赖关系

仅当估计算法设置为 `IIR` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Number of past input samples for FIR algorithm** — FIR 算法的过去输入样本数 `50`（默认）| 正整数

当估计算法设置为 `FIR` 时，将使用的样本数指定为正整数。

#### 依赖关系

仅当估计算法设置为 `FIR` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double`

### **View Filter Response** — 可视化频率响应 按钮

打开 `fvtool` 并显示 DC Blocker 的幅值响应。该响应基于模块参数。对这些参数所做的更改会更新 `fvtool`。

要在 `fvtool` 运行时更新幅值响应，请修改模块参数并点击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Signal Operations Communications Toolbox / Comm Filters Communications Toolbox / RF Impairments Correction DSP System Toolbox HDL Support / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不包括用于估计直流偏移的 CIC 算法。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当输入信号的数据类型为 `single` 或 `double` 时，DC Blocker 模块支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成。

SIMD 技术可显著提高生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

有关针对 HDL 代码生成优化的 DC Blocker，请参阅 High Performance DC Blocker for FPGA (DSP HDL Toolbox)。DSP HDL Toolbox™ 模块提供了一种 HDL 优化算法，具有硬件友好的控制信号，并在 Simulink 中仿真 HDL 算法的延迟。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

该模块支持复数信号的代码生成。

## 版本历史

**在 R2014a 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

阻断直流分量

DC Blocker 模块去除输入信号的直流分量。

该模块支持 C/C++ 代码生成和 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
