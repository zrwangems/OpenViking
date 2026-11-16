---
type: simulink-block
title: 'Channelizer'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'channelizer'
documentation_source_path: 'ref/channelizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Channelizer

## 端口

### 输入

### **data** — 输入数据，实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。

向量大小必须是 2 的幂，并且在 [2, 64] 范围内，且不大于通道数（FFT 长度）。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

该模块不接受 `uint64` 数据。

**数据类型：** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `single` | `double`
**复数支持：** 是

### **valid** — 指示有效输入数据的标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1` (`true`) 时，该模块捕获来自输入 **data** 端口的值。当 **valid** 为 `0` (`false`) 时，该模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### **reset** — 清除内部状态的标量

控制信号，用于清除内部状态。当 **reset** 为 `1` (`true`) 时，该模块停止当前计算并清除内部状态。当 **reset** 为 `0` (`false`) 且输入 **valid** 为 `1` (`true`) 时，该模块捕获数据以进行处理。

有关更多复位注意事项，请参阅硬件控制信号页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 频率通道输出数据向量

- 如果将 **Output vector size** 设置为 `Same as number of frequency bands`（默认），则输出数据是 1×*M* 向量，其中 *M* 是 FFT 长度。
- 如果将 **Output vector size** 设置为 `Same as input size`，则输出数据是 *M*×1 向量，其中 *M* 是输入向量大小。

对于任一输出大小，输出顺序均为位自然序。
输出数据类型是 **Filter output** 和 FFT 中为避免溢出所需的位增长的结果。

### **valid** — 指示有效输出数据的标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1` (`true`) 时，该模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0` (`false`) 时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **start** — 指示输出帧第一个有效周期的标量

控制信号，指示输出帧的第一个有效周期。

当 **start** 为 `1` (`true`) 时，该模块从输出 **data** 端口返回帧的第一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 上选择 **Enable start output port** 参数。

**数据类型：** `Boolean`

### **end** — 指示输出帧最后一个有效周期的标量

控制信号，指示输出帧的最后一个有效周期。

当 **end** 为 `1` (`true`) 时，该模块从输出 **data** 端口返回帧的最后一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 上选择 **Enable end output port** 参数。

**数据类型：** `Boolean`

## 参数

### 主

### **Filter coefficients** — 多相滤波器系数 `[ -0.032, 0.121, 0.318, 0.482, 0.546, 0.482, 0.318, 0.121, -0.032 ]` (默认) | 实数或复数数值向量

如果系数数量不是 **Number of frequency bands (FFT length)** 的倍数，该模块会用零填充此向量。默认滤波器规格是升余弦 FIR 滤波器，`rcosdesign(0.25,2,4,'sqrt')`。您可以指定系数向量或返回系数值的滤波器设计函数调用。默认情况下，该模块将系数转换为与输入相同的数据类型。

### **Filter structure** — HDL 滤波器架构 `Direct form transposed` (默认) | `Direct form systolic`

将 HDL 滤波器架构指定为以下结构之一：

- `Direct form transposed` — 此架构是全并行实现，适用于 FPGA 和 ASIC 应用。有关架构和性能详细信息，请参阅 Fully Parallel Transposed Architecture。
- `Direct form systolic` — 此架构提供全并行滤波器实现，可高效利用 Intel® 和 Xilinx® DSP 模块。有关架构和性能详细信息，请参阅 Fully Parallel Systolic Architecture。

### **Number of frequency bands (FFT length)** — FFT 长度 `8` (默认) | 2 的整数次幂

对于 HDL 代码生成，FFT 长度必须是 2 的幂，从 22 到 216。

### **Complex multiplication** — 复数乘法器的 HDL 实现 `Use 4 multipliers and 2 adders` (默认) | `Use 3 multipliers and 5 adders`

复数乘法器的 HDL 实现，指定为 `'Use 4 multipliers and 2 adders'` 或 `'Use 3 multipliers and 5 adders'`。根据您的综合工具和目标器件，一种选项可能更快或更小。

### **Output vector size** — 输出数据大小 `Same as number of frequency bands` (默认) | `Same as input size`

输出数据是包含 *M* 个元素的向量。对于任一输出大小，输出顺序均为位自然序。

- `Same as number of frequency bands` — 输出数据是 1×*M* 向量，其中 *M* 是 FFT 长度。
- `Same as input size` — 输出数据是 *M*×1 向量，其中 *M* 是输入向量大小。

### **Divide butterfly outputs by two** — FFT 缩放 on (默认) | off

当您选择此参数时，FFT 通过将每个流水线级的结果缩放 2 来实现总体 1/*N* 缩放因子。此调整使 FFT 的输出保持在与输入相同的幅度范围内。如果禁用缩放，FFT 通过在每个级将字长增加 1 位来避免溢出。

### 数据类型

### **Rounding mode** — 用于内部定点计算的舍入方法 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

请参阅舍入模式。当输入为任何整数或定点数据类型时，该模块使用定点算术进行内部计算。当输入为 `single` 或 `double` 时，此选项不适用。每个 FFT 级在旋转因子乘法之后、蝶形之前进行舍入。将系数和多相滤波器的输出转换为指定的数据类型时，也可能发生舍入。

### **Saturate on integer overflow** — 内部定点计算的溢出处理 off (默认) | on

请参阅溢出处理。当输入为任何整数或定点数据类型时，该模块使用定点算术进行内部计算。当输入为 `single` 或 `double` 时，此选项不适用。此选项适用于将系数和多相滤波器的输出转换为指定的数据类型。

FFT 算法通过以下方式避免溢出：缩放每个级的输出（`Normalize` 启用），或在每个级将字长增加 1 位（`Normalize` 禁用）。

### **Coefficients** — 滤波器系数的数据类型 `Inherit: Same word length as input` (默认) | 数据类型表达式

该模块使用您指定的舍入和溢出设置，将多相滤波器系数转换为此数据类型。当您选择 `Inherit: Same word length as input` (默认) 时，该模块使用 `fi()` 最佳精度规则选择二进制小数点。

### **Filter output** — 多相滤波器输出的数据类型 `Inherit: Same word length as input` (默认) | `Inherit: via internal rule` | 数据类型表达式

该模块使用您指定的舍入和溢出设置，将多相滤波器的输出（FFT 的输入）转换为此数据类型。当您选择 `Inherit: via internal rule` 时，该模块通过考虑滤波器系数的值和输入数据类型的范围，选择最佳精度二进制小数点。

默认情况下，FFT 逻辑不修改数据类型。当您禁用 **Divide butterfly outputs by two** 时，FFT 在每个级将字长增加 1 位以避免溢出。

### 控制端口

### **Enable reset input port** — 可选复位信号 off (默认) | on

当您选择此参数时，**reset** 端口会显示在模块图标上。当 **reset** 输入为 `true` 时，该模块停止计算并清除所有内部状态。

### **Enable start output port** — 指示数据开始的可选控制信号 off (默认) | on

当您选择此参数时，**start** 端口会显示在模块图标上。**start** 信号在帧中输出数据的第一个周期为 true。

### **Enable end output port** — 指示数据结束的可选控制信号 off (默认) | on

当您选择此参数时，**end** 端口会显示在模块图标上。**end** 信号在帧中输出数据的最后一个周期为 true。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017a 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 Channelizer HDL Optimized，并包含在 DSP System Toolbox™ **DSP System Toolbox HDL Support** 库中。

### R2022a：FFT 长度为 4

现在可以将 FFT 长度设置为 4 (22)。在以前的版本中，FFT 长度必须是 2 的幂，从 8 (23) 到 216。

### R2022a：支持 Direct form systolic 滤波器结构

此模块现在支持全并行脉动架构。要使用此架构，请将 **Filter structure** 参数设置为 `Direct form systolic`。

## 描述

多相滤波器组和快速傅里叶变换

Channelizer 模块将宽带输入信号分离为多个窄带输出信号。它为流数据应用提供硬件速度和面积优化。该模块接受实数或复数数据的标量或向量输入，提供硬件友好的控制信号，并具有可选的输出帧控制信号。使用向量输入，可以实现每秒千兆采样 (GSPS) 吞吐量，也称为超采样率。该模块实现一个多相滤波器，每个输入向量元素对应一个子滤波器。硬件实现交错子滤波器，从而使每个滤波器乘法器共享 (*FFT Length* / *Input Size*) 次。FFT 实现使用与 FFT 模块相同的流水线 Radix 2^2 FFT 算法。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
