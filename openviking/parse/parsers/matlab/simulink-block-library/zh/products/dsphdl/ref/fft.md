---
type: simulink-block
title: 'FFT'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'fft'
documentation_source_path: 'ref/fft.html'
language: zh-CN
chinese_source: worker-translation
---

# FFT

## 端口

### 输入

### **data** — 输入数据：实数或复数值的标量或列向量

输入数据，指定为实数或复数值的标量或列向量。
向量输入在 `Streaming Radix 2^2` 架构下受支持，但在可变 FFT 大小下不受支持。向量大小必须是 2 的幂，范围为 1 到 64，并且小于或等于 FFT length。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `single` | `double`
**复数支持：** 是

### **valid** — 指示输入数据有效的标量

控制信号，用于指示输入数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0` (`false`) 时，模块忽略来自输入 **data** 端口的值。

当您将 **Architecture** 参数设置为 `Burst Radix 2`，或将 **FFT length source** 参数设置为 `Input port` 时，只有在 **ready** 背压信号为 `1` (`true`) 时才能施加输入数据。当 **ready** 为 `0` (`false`) 时，模块忽略输入 **data** 和 **valid** 信号。

**数据类型：** `Boolean`

### **log2FFTLen** — FFT length 的 Log2 标量

*自 R2025a 起*

将 FFT 大小提供为 `log2(FFTLength)`。例如，如果 FFT length 为 32，则在端口处指定 `5`。对于 HDL 代码生成，FFT length 必须是 2^2 到 2^16 之间的 2 的幂，因此端口值必须在 2 到 16 的范围内。如果该值小于 2，模块将使用 4 的 FFT length。如果该值大于 16，模块将使用 2^16 的 FFT length。

要将新的 FFT length 通知模块，请在至少一个周期内将 **loadFFTLen** 设置为 `1` (`true`)，同时在 **log2FFTLen** 上提供新值。

当您使用可变 FFT length 时，输入数据必须遵守 **ready** 背压信号。您可以在处理帧时指定新的 FFT length。模块在完成当前帧时将 **ready** 设置为 `0` (`false`)，然后将 **ready** 设置为 `1` (`true`) 以指示它已准备好接收下一帧。模块会将新的 FFT length 用于下一个输入帧。如果在没有帧正在处理时将 **loadFFTLen** 设置为 `1` (`true`)，模块会在更新内部逻辑时将 **ready** 设置为 `0` (`false`) 四个周期。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,M,0) where 1<M<6`

### **loadFFTLen** — 指示有效 FFT 大小的标量

*自 R2025a 起*

控制信号，用于指示输入 FFT 大小是否有效。当 **loadFFTLen** 为 `1` (`true`) 时，模块从输入 **log2FFTLen** 端口捕获值。当 **loadFFTLen** 为 `0` (`false`) 时，模块忽略来自输入 **log2FFTLen** 端口的值。

#### 依赖关系

要启用此端口，请将 **FFT length source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态的标量

控制信号，用于清除内部状态。当 **reset** 为 `1` (`true`) 时，模块停止当前计算并清除内部状态。当 **reset** 为 `0` (`false`) 且输入 **valid** 为 `1` (`true`) 时，模块捕获数据以进行处理。

有关更多 reset 注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`

### 输出

### **data** — 频率通道输出数据：实数或复数值的标量或列向量

输出数据，以实数或复数值的标量或列向量形式返回。当输入为定点数据类型且启用缩放时，输出数据类型与输入数据类型相同。当输入为整数类型且启用缩放时，输出为定点类型，其字长与输入整数相同。默认情况下，输出顺序为位反转。如果禁用缩放，输出字长会增加以避免溢出。有关详细信息，请参阅 **Divide butterfly outputs by two** 参数。

**数据类型：** `fixed point` | `double` | `single`
**复数支持：** 是

### **valid** — 指示输出数据有效的标量

控制信号，用于指示输出数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0` (`false`) 时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据的标量

控制信号，用于指示模块已准备好在下个周期接收新的输入数据采样。当 **ready** 为 `1` (`true`) 时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0` (`false`) 时，模块会忽略下一个时间步中的任何输入数据。

有关展示此协议的波形，请参阅 Control Signals 部分中的时序图。

#### 依赖关系

要启用此端口，请将 **Architecture** 参数设置为 `Burst Radix 2`，或者当 **Architecture** 设置为 `Streaming Radix 2^2` 时，将 **FFT length source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **start** — 指示输出帧第一个有效周期的标量

控制信号，用于指示输出帧的第一个有效周期。当 **start** 为 `1` (`true`) 时，模块在输出 **data** 端口上返回该帧的第一个有效采样。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable start output port** 参数。

**数据类型：** `Boolean`

### **end** — 指示输出帧最后一个有效周期的标量

控制信号，用于指示输出帧的最后一个有效周期。当 **end** 为 `1` (`true`) 时，模块在输出 **data** 端口上返回该帧的最后一个有效采样。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable end output port** 参数。

**数据类型：** `Boolean`

## 参数

### 主要

### **Architecture** — 硬件实现 `Streaming Radix 2^2`（默认） | `Burst Radix 2`

指定 FFT 的硬件实现。

- `Streaming Radix 2^2` — 低延迟架构。当您使用向量输入时，此架构支持 GSPS 吞吐量。自 R2025a 起，此架构支持可变 FFT length。当您使用可变 FFT length 时，输入数据必须遵守 **ready** 背压信号。
- `Burst Radix 2` — 最小资源架构。此架构不支持向量输入。当您使用此架构时，输入数据必须遵守 **ready** 背压信号。此架构仅支持固定 FFT length。

有关这些架构的更多详细信息，请参阅 Algorithms。

### **FFT length source** — FFT length 的来源 `Property`（默认） | `Input port`

*自 R2025a 起*

您可以将常量 FFT length 作为参数输入，也可以使用输入端口提供时变 FFT length。当您选择 `Input port` 时，模块上会出现 **log2FFTLen**、**loadFFTLen** 和 **ready** 端口。

#### 依赖关系

仅当您将 **Architecture** 设置为 `Streaming Radix 2^2` 时，此参数才可用。

当您选择 `Input port` 时，**Output in bit-reversed order** 和 **Input in bit-reversed order** 参数会被禁用。模块使用自然输入顺序和位反转输出顺序。

### **FFT length** — 一次 FFT 计算使用的数据点数 `1024`（默认）

指定一次 FFT 计算使用的数据点数。对于 HDL 代码生成，FFT length 必须是 2^2 到 2^16 之间的 2 的幂。

#### 依赖关系

当您将 **Architecture** 设置为 `Burst Radix 2`，或将 **FFT length source** 参数设置为 `Property` 时，此参数可用。

### **Maximum FFT length** — 输入端口预期的最高 FFT length `1024`（默认）

*自 R2025a 起*

指定一次 FFT 计算使用的最大数据点数。此参数可帮助限制可变大小 FFT 设计所需的硬件资源。**Maximum FFT length** 必须是 2^3 到 2^16 之间的 2 的幂。

如果您在 reset 后提供输入帧但未从端口设置 FFT length，模块将使用 **Maximum FFT length** 参数值。

#### 依赖关系

当您将 **FFT length source** 参数设置为 `Input port` 时，此参数可用。

### **Complex multiplication** — 复数乘法器的硬件实现 `Use 4 multipliers and 2 adders`（默认） | `Use 3 multipliers and 5 adders`

指定复数乘法器的硬件实现。每个乘法使用 `Use 4 multipliers and 2 adders` 或 `Use 3 multipliers and 5 adders` 实现。根据您的综合工具和目标器件，某个选项可能更快或更小。

### **Output in bit-reversed order** — 输出数据的顺序 on（默认） | off

当您选中此复选框时，输出元素相对于输入顺序为位反转。要按线性顺序返回输出元素，请清除此复选框。

FFT 算法按与输入相反的顺序计算输出。如果您指定输出与输入顺序相同，算法会执行额外的反转操作。有关详细信息，请参阅 Linear and Bit-Reversed Output Order。

#### 依赖关系

当您将 **FFT length source** 参数设置为 `Input port` 时，**Output in bit-reversed order** 和 **Input in bit-reversed order** 参数会被禁用。模块使用自然输入顺序和位反转输出顺序。

### **Input in bit-reversed order** — 输入数据的预期顺序 off（默认） | on

当您选中此复选框时，模块期望输入数据为位反转顺序。默认情况下，该复选框处于清除状态，并且期望输入为线性顺序。

FFT 算法按与输入相反的顺序计算输出。如果您指定输出与输入顺序相同，算法会执行额外的反转操作。有关详细信息，请参阅 Linear and Bit-Reversed Output Order。

#### 依赖关系

当您将 **FFT length source** 参数设置为 `Input port` 时，**Output in bit-reversed order** 和 **Input in bit-reversed order** 参数会被禁用。模块使用自然输入顺序和位反转输出顺序。

### **Divide butterfly outputs by two** — FFT 缩放 off（默认） | on

当您选择此参数时，FFT 通过将每个蝶形乘法运算的输出除以二来实现总体 1/*FFTLength* 缩放因子。此调整使 FFT 的输出保持与其输入相同的幅度范围。如果禁用缩放，FFT 会在每次蝶形乘法运算后将字长增加 1 位以避免溢出。两种架构的位增长相同。

### 数据类型

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于内部定点计算的舍入模式。当输入为任何整数或定点数据类型时，此模块使用定点算术进行内部计算。当输入数据为 `single` 或 `double` 类型时，此选项不适用。舍入适用于旋转因子乘法和缩放运算。有关舍入模式的更多信息，请参阅 Rounding Modes。

### 控制端口

### **Enable reset input port** — 可选 reset 信号 off（默认） | on

在模块上启用输入 **reset** 端口。

### **Enable start output port** — 可选的控制信号，指示数据开始 off（默认） | on

在模块上启用输出 **start** 端口。此输出信号指示输出数据帧的第一个采样。

### **Enable end output port** — 可选的控制信号，指示数据结束 off（默认） | on

在模块上启用输出 **end** 端口。此输出信号指示输出数据帧的最后一个采样。

## 所属库

DSP HDL Toolbox / Transforms

## 模块特性

未在 R2025b 中记录。

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 不能在 Enabled Subsystem (Simulink) 内为此模块生成 HDL 代码。

## 版本历史

**在 R2014a 中引入**

### R2025a: 可变 FFT length

您现在可以使用输入端口指定时变 FFT length。仅当您将 **Architecture** 设置为 `Streaming Radix 2^2` 且使用标量输入数据时，才支持此功能。

将 **FFT length source** 参数设置为 `Input port`，然后在 **log2FFTLen** 端口处将 FFT length 指定为 `log2(FFTLength)`。例如，如果 FFT length 为 32，则在端口处指定 `5`。将 **loadFFTLen** 端口设置为 `1` (`true`) 至少一个周期，以从输入 **log2FFTLen** 端口捕获值。

当您使用可变 FFT length 时，必须仅在 **ready** 背压信号为 `1` (`true`) 时发送输入数据。如果在处理一帧数据时提供了新的 FFT length，模块会将 **ready** 信号设置为 `0` (`false`)。当模块完成一帧输出数据并已为下一个输入帧更新 FFT length 后，会将 **ready** 信号设置为 `1` (`true`)。

要限制可变大小 FFT 实现中使用的硬件资源，请将 **Maximum FFT length** 参数设置为您预期的最大输入大小。

### R2022a: 从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 FFT HDL Optimized，并包含在 DSP System Toolbox™ **DSP System Toolbox HDL Support** 库中。

### R2022a: FFT length 为 4

您现在可以将 FFT length 设置为 4 (2^2)。在以前的版本中，FFT length 必须是 2 的幂，范围为 8 (2^3) 到 2^16。

## 描述

计算快速傅里叶变换 (FFT)

FFT 模块提供两种架构，用于实现面向 FPGA 和 ASIC 应用的算法。您可以选择一种架构，以针对吞吐量或面积进行优化。

- `Streaming Radix 2^2` — 将此架构用于高吞吐量应用。此架构支持标量或向量输入数据。使用向量输入时，您可以实现每秒千兆采样 (GSPS) 吞吐量，也称为超采样率。自 2025a 起，当您使用标量输入数据时，此架构还支持通过输入端口指定 FFT 大小。
- `Burst Radix 2` — 将此架构用于最小资源实现，尤其是在大型快速傅里叶变换 (FFT) 大小下。您的系统必须能够容忍突发数据和更高延迟。此架构仅支持标量输入数据。

该模块接受实数或复数数据，提供硬件友好的控制信号以及可选的输出帧控制信号。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
