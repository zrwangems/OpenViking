---
type: simulink-block
title: 'Biquad Filter'
family: 'filtering'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'biquadfilter'
documentation_source_path: 'ref/biquadfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Biquad Filter

## 端口

### 输入

### **data** — 输入数据标量或实数列向量

输入数据，指定为标量或实数列向量。当输入具有整数或定点数据类型时，模块在内部计算中使用定点算术。

仅当将 **Filter structure** 设置为 `Pipelined feedback form` 时，才支持向量输入。模块接受最多 64 个样本的向量，但较大的向量大小可能使内部数据类型的计算变得困难。对于硬件实现，最多 16 个样本的向量大小是实用的。

当将 **Filter structure** 设置为 `Direct form I fully serial` 时，模块具有输出 **ready** 信号，用于指示模块何时准备好接收新输入。仅当输出 **ready** 信号为 `1` (`true`) 时，才应用输入数据。您的设计可以对 **ready** 信号作出反应以提供下一个输入样本，或者您可以在输入数据之间留出足够的周期来处理每个样本。模块图标显示处理一个样本所需的周期。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **valid** — 指示有效输入数据标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0` (`false`) 时，模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### 输出

### **data** — 滤波后的输出数据标量或实数列向量

滤波后的输出数据，以标量或实数列向量形式返回。输出维度与输入维度匹配。当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**Data Types** 选项卡上的 **Output** 参数控制输出数据类型。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **valid** — 指示有效输出数据标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1` (`true`) 时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0` (`false`) 时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据标量

控制信号，指示模块已准备好下一个周期的新输入数据样本。当 **ready** 为 `1` (`true`) 时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0` (`false`) 时，模块忽略下一个时间步中的任何输入数据。

使用全串行架构时，模块一次处理一个样本。如果您的设计等待此模块将 **ready** 返回为 `0` (`false`) 后再将输入 **valid** 设置为 `0` (`false`)，则一个额外的输入数据周期会到达端口。模块在处理当前数据时存储此额外数据，并且在您的模型处理完额外输入数据之前，不会将 **ready** 设置为 `1` (`true`)。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Direct form I fully serial`。

**数据类型：** `Boolean`

## 参数

### 主要

### **Filter structure** — HDL 滤波器架构 `Direct form II` (default) | `Direct form II transposed` | `Pipelined feedback form` | `Direct form I fully serial`

`Direct form II` 和 `Direct form II transposed` 架构均为流水线化并经过量化，以良好适配 FPGA DSP 模块。这些滤波器的输出与 DSP System Toolbox™ System 对象 `dsp.SOSFilter` 和 `dsp.FourthOrderSectionFilter` 的输出匹配。这些架构最小化滤波器使用的乘法器数量，但具有通过反馈环路的临界路径，有时无法达到更高的时钟速率。这些架构不支持向量输入。

`Pipelined feedback form` 实现了一种流水线架构，比任一直接型 II 结构使用更多乘法器，但在综合后可实现更高的时钟速率。仅当使用 `Pipelined feedback form` 时才支持向量输入。由于流水线滤波器级中应用数据样本的时序，流水线滤波器的输出与 DSP System Toolbox 函数 `dsp.SOSFilter` 和 `dsp.FourthOrderSectionFilter` 略有不同。

`Direct form I fully serial` 实现了一种全串行架构，仅使用一个乘法器。选择此选项时，模块将分子、分母和缩放值存储在同一 ROM 中。您可以使用 **Coefficients** 数据类型参数控制 ROM 的数据类型。选择此架构时，模块上会出现输出 **ready** 端口。**ready** 信号指示模块何时准备好接收新输入数据。仅当 **ready** 为 `1` (`true`) 时应用输入数据。此架构不支持向量输入。

### **Numerator coefficients of filter** — 分子系数 `[1,2,1]` (default) | *NumSections*-by-3 矩阵

将分子系数指定为 *NumSections*-by-3 值的矩阵。*NumSections* 是二阶滤波器节的数量。模块根据分子和分母系数的大小推断滤波器节的数量。分子系数矩阵和分母系数矩阵必须大小相同。默认滤波器有一个节。

### **Denominator coefficients of filter** — 分母系数 `[1,.1,.2]` (default) | *NumSections*-by-3 矩阵

将分母系数指定为 *NumSections*-by-3 值的矩阵。模块假定每个节的第一个分母系数为 `1.0`。*NumSections* 是二阶滤波器节的数量。模块根据分子和分母系数的大小推断节的数量。分子系数矩阵和分母系数矩阵必须大小相同。默认滤波器有一个节。

### **Scale values of filter** — 在二阶滤波器节之前和之后应用的增益值 `[1]` (default) | 1 到 *NumSections*+1 个值的向量

将增益值指定为最多 *NumSections*+1 个值的向量。*NumSections* 是二阶滤波器节的数量。模块根据分子和分母系数的大小推断节的数量。如果向量只有一个值，模块会在第一个节之前应用该增益。如果指定的值少于滤波器节的数量，模块会将其余节的增益值设置为一。该图显示了一个 3 节滤波器以及四个缩放值在各节之前和之后的位置。

在滤波器节外部实现这些增益因子可减少实现滤波器分子所需的乘法器。

### 数据类型

### **Rounding mode** — 用于对输出进行类型转换的舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于将输出和累加器值类型转换为由 **Output** 和 **Accumulator** 参数指定的数据类型的舍入模式。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 用于对输出进行类型转换的溢出处理 `off` (default) | `on`

用于将输出和累加器值类型转换为由 **Output** 和 **Accumulator** 参数指定的数据类型的溢出处理。当输入数据类型为浮点时，模块忽略此参数。有关更多详细信息，请参阅溢出处理。

### **Numerator** — 分子系数的数据类型 `Inherit: Same word length as input` (default) | `<data type expression>`

模块将分子系数转换为此数据类型。量化会舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点时，模块忽略此参数。

如果系数的数据类型没有足够的分数长度来准确表示系数，模块会返回警告。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form II transposed`、`Direct form II` 或 `Pipelined feedback form`。

### **Denominator** — 分母系数的数据类型 `Inherit: Same word length as input` (default) | `<data type expression>`

模块将分母系数转换为此数据类型。量化会舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点时，模块忽略此参数。

如果系数的数据类型没有足够的分数长度来准确表示系数，模块会返回警告。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form II transposed`、`Direct form II` 或 `Pipelined feedback form`。

### **ScaleValues** — 增益的数据类型 `Inherit: Same word length as input` (default) | `<data type expression>`

模块将缩放值转换为此数据类型。量化会舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点时，模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form II transposed`、`Direct form II` 或 `Pipelined feedback form`。

### **Coefficients** — 使用串行滤波器架构时系数存储器的数据类型 `Inherit: Same word length as input` (default) | `<data type expression>`

模块将分子、分母和缩放值转换为此数据类型，并将它们存储在具有此字长的八元素存储器中。量化会舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点时，模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form I fully serial`。

### **Accumulator** — 每个节内累加器信号的数据类型 `Inherit: Same as first input` (default) | `<data type expression>`

模块将内部累加器信号（如算法部分中的图所示）转换为此数据类型。量化使用 **Rounding mode** 和 **Saturate on integer overflow** 参数的设置。当输入数据类型为浮点时，模块忽略此参数。

### **Output** — 滤波器输出的数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

模块将滤波器的输出转换为此数据类型。量化使用 **Rounding mode** 和 **Saturate on integer overflow** 参数的设置。当输入数据类型为浮点时，模块忽略此参数。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022a 中引入**

### R2023a：最小资源架构

该模块现在可以选择将 **Filter structure** 参数设置为 `Direct form I fully serial`，以实现仅使用一个乘法器的全串行架构。选择此选项时，模块将分子、分母和缩放值存储在同一 ROM 中，并且您可以使用 **Coefficient** 数据类型参数控制 ROM 的数据类型。选择此架构时，模块具有输出 **ready** 信号，用于指示模块何时准备好接收新输入。仅当输出 **ready** 信号为 `1` (`true`) 时，才能应用输入数据。

## 描述

双二阶 IIR (SOS) 滤波器

双二阶滤波器是一种无限脉冲响应 (IIR) 滤波器，其中分子和分母被拆分为一系列通过增益模块连接的二阶节。此类滤波器可以替代使用不切实际硬件资源量的大型 FIR 滤波器。设计通常将双二阶滤波器用作 DC 阻断滤波器，或用于满足最初用模拟滤波器实现的规范，例如预加重滤波器。

**注意**

您还可以使用 DSP HDL IP Designer 应用生成此硬件优化算法的 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
