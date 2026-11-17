---
type: simulink-block
title: 'FFT'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'fft'
documentation_source_path: 'ref/fft.html'
language: zh-CN
chinese_source: worker-translation
---

# FFT

## 端口

### 输入

### **data** — 输入数据 实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。
向量输入在 `Streaming Radix 2^2`
架构下受支持，在可变 FFT 长度下不受支持。向量大小必须是 2 的幂，
范围从 1 到 64，且小于或等于 FFT
长度。

该软件支持 `double` 和
`single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `single` | `double`
**复数支持：** 是

### **valid** — 指示输入数据有效 标量

控制信号，指示输入数据是否有效。当
**valid** 为 `1`（`true`）时，
模块从输入 **data** 端口捕获值。当
**valid** 为 `0`（`false`）时，
模块忽略输入 **data** 端口的值。

当您将 **Architecture** 参数设置为 `Burst
Radix 2`，或将 **FFT length source** 参数
设置为 `Input port` 时，您必须仅在
**ready** 背压信号为 `1`
（`true`）时施加输入数据。当 **ready** 为
`0`（`false`）时，模块忽略输入 **data** 和
**valid** 信号。

**数据类型：** `Boolean`

### **log2FFTLen** — FFT 长度的 Log2 标量

*自 R2025a 起*

以
`log2(FFTLength)` 形式提供 FFT 大小。例如，如果 FFT 长度为 32，则在该端口指定 `5`。对于 HDL
代码生成，FFT 长度必须是 2 的幂，介于
2² 和 2¹⁶ 之间，因此端口值
必须在 2 到 16 的范围内。如果该值小于 2，模块使用 FFT
长度 4。如果该值大于 16，模块使用 FFT 长度
2¹⁶。

要通知模块新的 FFT 长度，请将 **loadFFTLen** 设置为
`1`（`true`）至少一个周期，同时在 **log2FFTLen** 上提供新
值。

当您使用可变 FFT 长度时，您的输入数据必须遵守
**ready** 背压信号。您可以在帧处理期间指定新的 FFT 长度。模块在完成当前帧时将 **ready** 设置为
`0`（`false`），然后将 **ready** 设置为 `1`（`true`）
以指示它已准备好处理下一帧。模块对
下一个输入帧使用新的 FFT 长度。如果您在没有帧处理时将 **loadFFTLen** 设置为 `1`
（`true`），模块会将
**ready** 设置为 `0`（`false`）
四个周期，同时更新内部逻辑。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为
`Input port`。

**数据类型：** `fixdt(0,M,0) where 1<M<6`

### **loadFFTLen** — 指示有效 FFT 大小 标量

*自 R2025a 起*

控制信号，指示输入 FFT 大小是否有效。当
**loadFFTLen** 为 `1`（`true`）时，
模块从输入 **log2FFTLen** 端口捕获值。当
**loadFFTLen** 为 `0`（`false`）时，
模块忽略输入 **log2FFTLen**
端口的值。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为
`Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为
`1`（`true`）时，模块停止当前
计算并清除内部状态。当 **reset** 为
`0`（`false`）且输入
**valid** 为 `1`（`true`）时，
模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选中
**Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 频率通道输出数据 实数或复数值的标量或列向量

输出数据，以实数或复数值的标量或列向量形式返回。当
输入为定点数据类型且启用缩放时，输出数据类型与
输入数据类型相同。当输入为整数类型且启用缩放时，
输出为定点类型，其字长与输入整数相同。输出顺序默认按位反转。如果禁用缩放，输出字
长会增加以避免溢出。有关更多信息，请参阅 **Divide
butterfly outputs by two** 参数。

**数据类型：** `fixed point` | `double` | `single`
**复数支持：** 是

### **valid** — 指示输出数据有效 标量

控制信号，指示输出数据是否有效。当
**valid** 为 `1`（`true`）时，
模块从输出 **data** 端口返回有效数据。当
**valid** 为 `0`（`false`）时，
输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据 标量

控制信号，指示模块已准备好在
下一个周期接收新的输入数据样本。当 **ready** 为 `1`
（`true`）时，您可以为下一个时间步指定 **data**
和 **valid** 输入。当
**ready** 为 `0`
（`false`）时，模块在下一个时间步忽略任何输入数据。

有关显示此协议的波形，请参阅 Control Signals 部分中的时序图。

#### 依赖关系

要启用此端口，请将 **Architecture** 参数设置为
`Burst Radix 2`，或者在
**Architecture** 设置为 `Streaming Radix
2^2` 时，将 **FFT length source** 参数设置为
`Input port`。

**数据类型：** `Boolean`

### **start** — 指示输出帧的第一个有效周期 标量

控制信号，指示输出帧的第一个有效周期。当
**start** 为 `1`（`true`）时，
模块在输出
**data** 端口返回帧的第一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选中
**Enable start output port** 参数。

**数据类型：** `Boolean`

### **end** — 指示输出帧的最后一个有效周期 标量

控制信号，指示输出帧的最后一个有效周期。当
**end** 为 `1`（`true`）时，
模块在输出
**data** 端口返回帧的最后一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选中
**Enable end output port** 参数。

**数据类型：** `Boolean`

## 参数

### 主要

### **Architecture** — 硬件实现 `Streaming Radix 2^2`（默认）| `Burst Radix 2`

指定 FFT 的硬件实现。

- `Streaming Radix 2^2` — 低延迟
  架构。当您使用向量输入时，此架构支持 GSPS 吞吐量。自 R2025a 起，此架构支持可变 FFT 长度。当您使用
  可变 FFT 长度时，您的输入数据必须遵守
  **ready** 背压信号。
- `Burst Radix 2` — 最小资源
  架构。此架构不支持向量输入。当您使用此
  架构时，您的输入数据必须遵守 **ready**
  背压信号。此架构仅支持固定 FFT 长度。

有关这些架构的更多详细信息，请参阅 Algorithms。

### **FFT length source** — FFT 长度来源 `Property`（默认）| `Input port`

*自 R2025a 起*

您可以将常量 FFT 长度作为参数输入，或通过输入端口提供时变 FFT
长度。当您选择 `Input port` 时，
**log2FFTLen**、**loadFFTLen** 和
**ready** 端口会出现在模块上。

#### 依赖关系

此参数仅在您将 **Architecture**
设置为 `Streaming Radix 2^2` 时可用。

当您选择 `Input port` 时，**Output in
bit-reversed order** 和 **Input in bit-reversed order**
参数被禁用。模块使用自然输入顺序和按位反转输出
顺序。

### **FFT length** — 用于一次 FFT 计算的数据点数 `1024`（默认）

指定用于一次 FFT 计算的数据点数。对于 HDL 代码
生成，FFT 长度必须是 2 的幂，介于 2²
和 2¹⁶ 之间。

#### 依赖关系

当您将 **Architecture** 设置为
`Burst Radix 2` 或将 **FFT length
source** 参数设置为 `Property` 时，此参数可用。

### **Maximum FFT length** — 预期从输入端口获得的最高 FFT 长度 `1024`（默认）

*自 R2025a 起*

指定用于一次 FFT 计算的最大数据点数。此
参数有助于限制可变大小 FFT 设计所需的硬件资源。
**Maximum FFT length** 必须是 2 的幂，介于
2³ 到 2¹⁶ 之间。

如果您在复位后提供输入帧而未从
端口设置 FFT 长度，模块使用 **Maximum FFT length** 参数
值。

#### 依赖关系

当您将 **FFT length
source** 参数设置为 `Input port` 时，此参数可用。

### **Complex multiplication** — 复数乘法器的硬件实现 `Use 4 multipliers and 2 adders`（默认）| `Use 3 multipliers and 5 adders`

指定复数乘法器的硬件实现。每个乘法
使用 `Use 4 multipliers and 2 adders`
或 `Use 3 multipliers and 5 adders` 实现。根据您的
综合工具和目标器件，某个选项可能更快或更小。

### **Output in bit-reversed order** — 输出数据的顺序 on（默认）| off

当您选中此复选框时，输出元素相对于
输入顺序按位反转。要以线性顺序返回输出元素，请清除此复选框。

FFT 算法以与输入相反的顺序计算输出。如果您
指定输出与输入顺序相同，算法会执行额外的
反转操作。有关更多信息，请参阅 Linear and Bit-Reversed Output Order。

#### 依赖关系

当您将 **FFT length source** 参数设置为
`Input port` 时，**Output in bit-reversed
order** 和 **Input in bit-reversed order** 参数
被禁用。模块使用自然输入顺序和按位反转输出顺序。

### **Input in bit-reversed order** — 输入数据的预期顺序 off（默认）| on

当您选中此复选框时，模块期望输入数据按位反转
顺序。默认情况下，该复选框被清除，输入期望为线性
顺序。

FFT 算法以与输入相反的顺序计算输出。如果您
指定输出与输入顺序相同，算法会执行额外的
反转操作。有关更多信息，请参阅 Linear and Bit-Reversed Output Order。

#### 依赖关系

当您将 **FFT length source** 参数设置为
`Input port` 时，**Output in bit-reversed
order** 和 **Input in bit-reversed order** 参数
被禁用。模块使用自然输入顺序和按位反转输出顺序。

### **Divide butterfly outputs by two** — FFT 缩放 off（默认）| on

当您选中此参数时，FFT 通过将每个蝶形
乘法的输出除以二来实现总体
1/*FFTLength* 缩放因子。此调整使 FFT 的输出保持在与输入相同的
幅度范围内。如果您禁用缩放，FFT 通过在每次蝶形乘法后将字长增加 1 位来
避免溢出。两种架构的位
增长相同。

### 数据类型

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于内部定点计算的舍入模式。当输入为任何
整数或定点数据类型时，此模块使用定点算术进行内部
计算。当输入数据为
`single` 或 `double` 类型时，此选项不适用。舍入适用于
旋转因子乘法和缩放操作。有关舍入模式的更多信息，请参阅 Rounding Modes。

### 控制端口

### **Enable reset input port** — 可选复位信号 off（默认）| on

启用模块上的输入 **reset** 端口。

### **Enable start output port** — 指示数据开始的可选控制信号 off（默认）| on

启用模块上的输出 **start** 端口。此输出信号
指示输出数据帧的第一个样本。

### **Enable end output port** — 指示数据结束的可选控制信号 off（默认）| on

启用模块上的输出 **end** 端口。此输出信号
指示输出数据帧的最后一个样本。

## 所属库

DSP HDL Toolbox / Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 您不能在 Enabled Subsystem (Simulink) 内为此模块生成 HDL 代码。

## 版本历史

**在 R2014a 中引入**

### R2025a：可变 FFT 长度

您现在可以通过输入端口指定时变 FFT 长度。此功能仅在您将 **Architecture** 设置为 `Streaming
Radix 2^2` 且使用标量输入数据时受支持。

将 **FFT length source** 参数设置为 `Input
port`，然后在 **log2FFTLen**
端口以 `log2(FFTLength)` 形式指定 FFT 长度。例如，如果 FFT 长度为 32，则在该端口指定 `5`。将
**loadFFTLen** 端口设置为 `1`（`true`）至少一个周期，以从输入 **log2FFTLen**
端口捕获值。

当您使用可变 FFT 长度时，必须仅在
**ready** 背压信号为 `1`
（`true`）时发送输入数据。如果在处理一帧数据时提供了新的 FFT 长度，模块会将 **ready** 信号设置为
`0`（`false`）。当模块完成一帧输出
数据并已更新下一输入帧的 FFT 长度时，会将 **ready** 信号设置为
`1`（`true`）。

要限制可变大小 FFT 实现中使用的硬件资源，请将
**Maximum FFT length** 参数设置为您预期的最大输入大小。

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 FFT HDL Optimized，包含在
DSP System Toolbox™
**DSP System Toolbox HDL Support** 库中。

### R2022a：FFT 长度为 4

您现在可以将 FFT 长度设置为 4（2²）。在之前的
版本中，FFT 长度必须是 2 的幂，从 8（2³）到
2¹⁶。

## 描述

计算快速傅里叶变换（FFT）

FFT 模块提供两种架构，用于实现面向 FPGA 和 ASIC 应用的算法。您可以选择针对吞吐量或面积进行优化的架构。

- `Streaming Radix 2^2` — 将此架构用于高吞吐量应用。此架构支持标量或向量输入数据。使用向量输入时，您可以实现每秒千兆采样（GSPS）吞吐量，也称为超采样率。从 2025a 开始，当您使用标量输入数据时，此架构还支持通过输入端口指定 FFT 大小。
- `Burst Radix 2` — 将此架构用于最小资源实现，尤其是在大型快速傅里叶变换（FFT）大小的情况下。您的系统必须能够容忍突发数据和更高的延迟。此架构仅支持标量输入数据。

该模块接受实数或复数数据，提供硬件友好的控制信号，以及可选的输出帧控制信号。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
