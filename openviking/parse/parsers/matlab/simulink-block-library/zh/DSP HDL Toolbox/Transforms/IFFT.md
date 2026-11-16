---
type: simulink-block
title: 'IFFT'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'ifft'
documentation_source_path: 'ref/ifft.html'
language: zh-CN
chinese_source: worker-translation
---

# IFFT

## 端口

### 输入

### **data** — 输入数据，实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。
向量输入在 `Streaming Radix 2^2`
架构下受支持，在使用可变 FFT 长度时不受支持。向量大小必须是
2 的幂，范围为 1 到 64，并且小于或等于 FFT
长度。

软件支持 `double` 和
`single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型:** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `single` | `double`
**复数支持:** Yes

### **valid** — 指示有效输入数据的标量

控制信号，指示输入数据是否有效。当
**valid** 为 `1` (`true`) 时，
模块从输入 **data** 端口捕获值。当
**valid** 为 `0` (`false`) 时，
模块忽略输入 **data** 端口的值。

当您将 **Architecture** 参数设置为 `Burst
Radix 2`，或将 **FFT length source** 参数
设置为 `Input port` 时，必须仅在
**ready** 背压信号为 `1`
(`true`) 时施加输入数据。当 **ready** 为
`0` (`false`) 时，模块忽略输入 **data** 和
**valid** 信号。

**数据类型:** `Boolean`

### **log2FFTLen** — FFT 长度的 Log2 值，标量

*自 R2025a 起*

以
`log2(FFTLength)` 形式提供 FFT 大小。例如，如果 FFT 长度为 32，则在该端口指定 `5`。对于 HDL
代码生成，FFT 长度必须是 2 的幂，介于
2^2 和 2^16 之间，因此端口值
必须在 2 到 16 范围内。如果该值小于 2，模块使用 FFT
长度 4。如果该值大于 16，模块使用 FFT 长度
2^16。

要向模块通知新的 FFT 长度，请在
**log2FFTLen** 上使用新值，并将 **loadFFTLen** 设置为
`1` (`true`) 至少一个周期。

当您使用可变 FFT 长度时，您的输入数据必须遵守
**ready** 背压信号。您可以在处理帧期间指定新的 FFT 长度。模块在完成当前帧时将 **ready** 设置为
`0` (`false`)，然后将 **ready** 设置为 `1` (`true`)
以指示它已准备好处理下一帧。模块将新的 FFT 长度用于
下一个输入帧。如果在没有帧正在处理时将 **loadFFTLen** 设置为 `1`
(`true`)，模块会在更新内部逻辑时将
**ready** 设置为 `0` (`false`)
持续四个周期。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为
`Input port`。

**数据类型:** `fixdt(0,M,0) where 1<M<6`

### **loadFFTLen** — 指示有效 FFT 大小的标量

*自 R2025a 起*

控制信号，指示输入 FFT 大小是否有效。当
**loadFFTLen** 为 `1` (`true`) 时，
模块从输入 **log2FFTLen** 端口捕获值。当
**loadFFTLen** 为 `0` (`false`) 时，
模块忽略输入 **log2FFTLen**
端口的值。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为
`Input port`。

**数据类型:** `Boolean`

### **reset** — 清除内部状态的标量

控制信号，用于清除内部状态。当 **reset** 为
`1` (`true`) 时，模块停止当前
计算并清除内部状态。当 **reset** 为
`0` (`false`) 且输入
**valid** 为 `1` (`true`) 时，
模块捕获数据以进行处理。

有关更多复位注意事项，请参阅硬件控制信号页面上的复位信号部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择
**Enable reset input port** 参数。

**数据类型:** `Boolean`
### 输出

### **data** — 频率通道输出数据，实数或复数值的标量或列向量

输出数据，以实数或复数值的标量或列向量形式返回。
当输入为定点数据类型且启用缩放时，输出数据类型
与输入数据类型相同。当输入为整数类型且启用缩放时，
输出为定点类型，其字长与输入整数相同。默认情况下，输出顺序为
位反转顺序。如果禁用缩放，则输出字长会增加以避免溢出。有关更多
信息，请参阅 **Divide butterfly outputs by two**
参数。

**数据类型:** `fixed point` | `double` | `single`
**复数支持:** Yes

### **valid** — 指示有效输出数据的标量

控制信号，指示输出数据
是否有效。当 **valid** 为
`1` (`true`) 时，模块从输出
**data** 端口返回有效数据。当 **valid** 为
`0` (`false`) 时，输出
**data** 端口的值无效。

**数据类型:** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据的标量

控制信号，指示模块已准备好在
下一个周期接收新的输入数据样本。当 **ready** 为 `1`
(`true`) 时，您可以为下一个时间步指定 **data**
和 **valid** 输入。当
**ready** 为 `0`
(`false`) 时，模块忽略下一个时间
步中的任何输入数据。

有关显示此协议的波形，请参阅控制信号
一节中的时序图。

#### 依赖关系

要启用此端口，请将 **Architecture** 参数设置为
`Burst Radix 2`，或者在
**Architecture** 设置为 `Streaming Radix
2^2` 时，将 **FFT length source** 参数设置为
`Input port`。

**数据类型:** `Boolean`

### **start** — 指示输出帧第一个有效周期的标量

控制信号，指示输出帧的第一个有效周期。当
**start** 为 `1` (`true`) 时，
模块在输出 **data** 端口返回帧的第一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择
**Enable start output port** 参数。

**数据类型:** `Boolean`

### **end** — 指示输出帧最后一个有效周期的标量

控制信号，指示输出帧的最后一个有效周期。当
**end** 为 `1` (`true`) 时，
模块在输出 **data** 端口返回帧的最后一个有效样本。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择
**Enable end output port** 参数。

**数据类型:** `Boolean`

## 参数

### 主要

### **Architecture** — 硬件实现 `Streaming Radix 2^2`（默认）| `Burst Radix 2`

指定 IFFT 的硬件实现。

- `Streaming Radix 2^2` — 低延迟
  架构。使用向量输入时，此架构支持 GSPS 吞吐量。
  自 R2025a 起，此架构支持可变 FFT 长度。当您使用
  可变 FFT 长度时，您的输入数据必须遵守
  **ready** 背压信号。
- `Burst Radix 2` — 最小资源
  架构。此架构不支持向量输入。当您使用此
  架构时，您的输入数据必须遵守 **ready**
  背压信号。此架构仅支持固定 FFT 长度。

有关这些架构的更多详细信息，请参阅算法。

### **FFT length source** — FFT 长度的来源 `Property`（默认）| `Input port`

*自 R2025a 起*

您可以将恒定 FFT 长度作为参数输入，或通过输入端口提供时变 FFT
长度。当您选择 `Input port` 时，
**log2FFTLen**、**loadFFTLen** 和
**ready** 端口会出现在模块上。

#### 依赖关系

仅当您将 **Architecture**
设置为 `Streaming Radix 2^2` 时，此参数才可用。

当您选择 `Input port` 时，**Output in
bit-reversed order** 和 **Input in bit-reversed order**
参数将被禁用。模块使用自然输入顺序和位反转输出
顺序。

### **FFT length** — 用于一次 FFT 计算的数据点数量 `1024`（默认）

指定用于一次 IFFT 计算的数据点数量。对于 HDL 代码
生成，FFT 长度必须是 2 的幂，介于 2^2
和 2^16 之间。

#### 依赖关系

当您将 **Architecture** 设置为
`Burst Radix 2`，或将 **FFT length
source** 参数设置为 `Property` 时，此参数可用。

### **Maximum FFT length** — 预期从输入端口获得的最大 FFT 长度 `1024`（默认）

*自 R2025a 起*

指定用于一次 FFT 计算的最大数据点数量。此
参数有助于限制可变大小 FFT 设计所需的硬件资源。
对于 HDL 代码生成，FFT 长度必须是 2 的幂，介于
2^3 到 2^16 之间。

如果在复位后提供输入帧，但未从端口设置 FFT 长度，
模块将使用 **Maximum FFT length** 参数
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

选中此复选框时，输出元素相对于
输入顺序为位反转顺序。要按线性顺序返回输出元素，请清除此
复选框。

IFFT 算法按与输入相反的顺序计算输出。如果您
指定输出与输入顺序相同，算法将执行
额外的反转操作。有关更多信息，请参阅线性输出顺序和位反转输出顺序。

#### 依赖关系

当您将 **FFT length source** 参数设置为
`Input port` 时，**Output in bit-reversed
order** 和 **Input in bit-reversed order** 参数
将被禁用。模块使用自然输入顺序和位反转输出顺序。

### **Input in bit-reversed order** — 输入数据的预期顺序 off（默认）| on

选中此复选框时，模块期望输入数据为位反转
顺序。默认情况下，此复选框已清除，并期望输入为线性
顺序。

IFFT 算法按与输入相反的顺序计算输出。如果您
指定输出与输入顺序相同，算法将执行
额外的反转操作。有关更多信息，请参阅线性输出顺序和位反转输出顺序。

#### 依赖关系

当您将 **FFT length source** 参数设置为
`Input port` 时，**Output in bit-reversed
order** 和 **Input in bit-reversed order** 参数
将被禁用。模块使用自然输入顺序和位反转输出顺序。

### **Divide butterfly outputs by two** — FFT 缩放 on（默认）| off

选中此参数时，IFFT 通过将每个蝶形乘法输出除以二来实现总体
1/*FFTLength* 比例因子。此调整使 IFFT 的输出保持与其输入
相同的幅度范围。如果禁用缩放，模块会在每次蝶形乘法后将字长增加 1 位来避免溢出。两种架构的位增长相同。

### 数据类型

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于内部定点计算的舍入模式。当输入为任意
整数或定点数据类型时，此模块使用定点算术进行内部
计算。当输入数据为
`single` 或 `double` 类型时，此选项不适用。舍入应用于
旋转因子乘法和缩放操作。有关舍入模式的更多信息，请参阅舍入模式。

### 控制端口

### **Enable reset input port** — 可选复位信号 off（默认）| on

在模块上启用输入 **reset** 端口。

### **Enable start output port** — 指示数据开始的可选控制信号 off（默认）| on

在模块上启用输出 **start** 端口。此输出信号
指示输出数据帧的第一个样本。

### **Enable end output port** — 指示数据结束的可选控制信号 off（默认）| on

在模块上启用输出 **end** 端口。此输出信号
指示输出数据帧的最后一个样本。

## 所属库

DSP HDL Toolbox / Transforms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速器和快速加速器模式以及 DPI 组件生成进行 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 不能在 Enabled Subsystem (Simulink) 内为此模块生成 HDL 代码。

## 版本历史

**在 R2014a 中引入**

### R2025a: 可变 FFT 长度

您现在可以通过使用输入端口指定时变 FFT 长度。仅当您将 **Architecture** 设置为 `Streaming
Radix 2^2` 并且使用标量输入数据时，才支持此功能。

将 **FFT length source** 参数设置为 `Input
port`，然后在 **log2FFTLen**
端口以 `log2(FFTLength)` 形式指定 FFT 长度。例如，如果 FFT 长度为 32，则在该端口指定 `5`。将
**loadFFTLen** 端口设置为 `1` (`true`) 至少一个周期，以从输入 **log2FFTLen**
端口捕获值。

当您使用可变 FFT 长度时，必须仅在
**ready** 背压信号为 `1`
(`true`) 时发送输入数据。如果在处理一帧数据时提供了新的 FFT 长度，模块会将 **ready** 信号设置为
`0` (`false`)。当模块完成一帧输出数据并已为下一个输入帧更新 FFT 长度时，会将 **ready** 信号设置为
`1` (`true`)。

要限制可变大小 FFT 实现中使用的硬件资源，请将
**Maximum FFT length** 参数设置为预期的最大输入大小。

### R2022a: 从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 IFFT HDL Optimized，并包含在
DSP System Toolbox™
**DSP System Toolbox HDL Support** 库中。

### R2022a: FFT 长度为 4

您现在可以将 FFT 长度设置为 4 (2^2)。在以前
版本中，FFT 长度必须是 2 的幂，从 8 (2^3) 到
2^16。

## 描述

计算逆快速傅里叶变换 (IFFT)

IFFT 模块提供两种架构，为
FPGA 和 ASIC 应用实现该算法。您可以选择针对吞吐量或面积优化的架构。

- `Streaming Radix 2^2` — 将此架构用于
  高吞吐量应用。此架构支持标量或向量输入数据。使用向量输入时，您可以实现每秒千兆样本 (GSPS) 吞吐量，也称为超采样率。
  自 2025a 起，当您使用标量输入数据时，此架构还支持通过输入端口指定 FFT 大小。
- `Burst Radix 2` — 将此架构用于最小
  资源实现，尤其是在大型快速傅里叶变换 (FFT) 大小下。您的
  系统必须能够容忍突发数据和更高延迟。此架构仅支持
  标量输入数据。

此模块接受实数或复数数据，提供硬件友好的控制信号以及
可选的输出帧控制信号。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此硬件优化算法生成 HDL 代码，而无需创建
Simulink® 模型。该应用
提供与 Simulink 模块相同的接口和配置选项。
