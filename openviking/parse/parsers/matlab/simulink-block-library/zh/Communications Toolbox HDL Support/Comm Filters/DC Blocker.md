---
type: simulink-block
title: 'DC Blocker'
family: 'signal-operations'
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

### **Input** — 输入信号 scalar | vector | matrix

将包含 DC 分量的输入信号指定为标量、向量或矩阵。

如果输入为定点数据，则它必须是有符号整数，或斜率为 2 的幂且偏置为零的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`  
**复数支持：** 是

### 输出

### **Output** — 不含 DC 分量的输出信号 scalar | vector | matrix

已去除 DC 分量的输出信号。当输出为定点数据时，它只能是有符号值。

输出信号的大小、数据类型和复数性与输入信号相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`  
**复数支持：** 是

## 参数

### **Algorithm for estimating DC offset** — 用于估计 DC 偏移的算法 `IIR` (默认) | `FIR` | `CIC` | `Subtract mean`

指定用于估计 DC 偏移的算法。可从以下选项中选择：

- `IIR` 使用基于窄带低通椭圆滤波器的递归估计。与 FIR 相比，此算法通常占用更少的内存，并且效率更高。
- `FIR` 使用非递归移动平均估计。与 IIR 相比，此算法通常占用更多的内存，并且效率较低。
- `CIC` 使用不采用任何乘法器的低通滤波器。如果算法为 `CIC`，则必须将定点数据输入到 DC Blocker。
- `Subtract mean` 计算输入矩阵各列的均值，并从输入中减去这些均值。此方法不会在输入之间保留状态。例如，如果输入为 `[1 2 3 4; 3 4 5 6]`，则处于 `Subtract mean` 模式的 DC Blocker 模块输出 `[-1 -1 -1 -1; 1 1 1 1]`。

### **Normalized bandwidth of lowpass IIR or CIC filter** — 归一化带宽 `0.001` (默认) | 范围 (0 1) 内的实数标量

将滤波器的归一化带宽指定为大于 0 且小于 1 的实数标量。

#### 依赖关系

仅当估计算法设置为 `IIR` 或 `CIC` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Order of lowpass IIR elliptic filter** — 低通 IIR 椭圆滤波器的阶数 `6` (默认) | 大于 3 的整数

将低通 IIR 椭圆滤波器的滤波器阶数指定为大于 3 的整数。

#### 依赖关系

仅当估计算法设置为 `IIR` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Number of past input samples for FIR algorithm** — FIR 算法的过去输入采样点数 `50` (默认) | 正整数

当估计算法设置为 `FIR` 时，将要使用的过去输入采样点的数量指定为正整数。

#### 依赖关系

仅当估计算法设置为 `FIR` 时，DC Blocker 才使用此参数。

**数据类型：** `single` | `double`

### **View Filter Response** — 用于可视化频率响应的按钮

打开 `fvtool`，并显示 DC Blocker 的幅度响应。该响应基于模块参数。对这些参数所做的更改会更新 `fvtool`。

要在 `fvtool` 运行时更新幅度响应，请修改模块参数，然后点击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

指定要运行的仿真类型。可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器对模型进行仿真。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码对模型进行仿真。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型未更改，后续仿真就会重用该 C 代码。此选项需要额外的启动时间，但后续仿真速度更快。

## 所属库

DSP System Toolbox / Signal Operations  
Communications Toolbox / Comm Filters  
Communications Toolbox / RF Impairments Correction  
DSP System Toolbox HDL Support / Signal Operations

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
| a 不包括用于估计 DC 偏移的 CIC 算法。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当输入信号的数据类型为 `single` 或 `double` 时，DC Blocker 模块支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成。

SIMD 技术可显著提高生成代码的性能。有关详细信息，请参阅 SIMD 代码生成。要从此模块生成 SIMD 代码，请参阅使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

对于针对 HDL 代码生成而优化的 DC Blocker，请参阅 High Performance DC Blocker for FPGA (DSP HDL Toolbox)。DSP HDL Toolbox™ 模块提供了采用硬件友好型控制信号的 HDL 优化算法，并在 Simulink 中仿真 HDL 算法的延迟。

HDL Coder™ 提供了影响 HDL 实现和综合后逻辑的其他配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持针对复数信号的代码生成。

## 版本历史

**在 R2014a 中引入**

### R2024a：**Simulate using** 参数的默认值发生更改

**Simulate using** 参数的默认值现为 `Interpreted execution`。进行此更改后，模块默认使用 MATLAB 解释器进行仿真。

## 描述

阻隔 DC 分量

DC Blocker 模块用于去除输入信号中的 DC 分量。

此模块支持 C/C++ 代码生成和 SIMD 代码生成。有关详细信息，请参阅代码生成。
