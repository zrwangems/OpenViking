---
type: simulink-block
title: 'FIR Interpolator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'firinterpolator'
documentation_source_path: 'ref/firinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Interpolator

## 端口

### 输入

### **data** — 输入数据，实数或复数标量或向量

输入数据，指定为实数或复数标量或向量。向量大小必须小于或等于 64。

当输入数据类型为整数类型或 fixed-point 类型时，模块使用定点算术进行内部计算，并在 **数据类型** 选项卡上提供参数以自定义数据类型。当输入数据类型为浮点类型时，模块使用该输入浮点类型进行内部计算和输出数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** Yes

### **valid** — 指示输入数据有效的标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块捕获来自输入 **data** 端口的值。当 **valid** 为 `0`（`false`）时，模块忽略来自输入 **data** 端口的值。

**数据类型：** `Boolean`

### **coeff** — 滤波器系数，实数或复数行向量

*自 R2025a 起*

滤波器系数，指定为实数或复数值的行向量。您可以随时更改输入系数。系数向量的大小必须与 **Coefficients prototype** 参数中指定的样本系数大小匹配。原型指定一个样本系数向量，该向量代表预期输入系数的零值位置。模块使用该原型通过移除零值系数的乘法器来优化滤波器。

如果输入 **data** 是 fixed point 类型，则 **coeff** 值也必须是 fixed point 类型。如果输入 **data** 是浮点数据类型，则 **coeff** 值必须为相同数据类型。

软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **reset** — 清除内部状态的标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable reset input port**。

**数据类型：** `Boolean`
### 输出

### **data** — 插值输出数据，实数或复数标量或向量

插值输出数据，以实数或复数标量或向量的形式返回。向量大小为 *InputSize* \* *InterpolationFactor*。当 *NumCycles* 大于 *InterpolationFactor* 时，标量输出样本之间间隔 `floor(NumCycles/InterpolationFactor)` 个无效周期，输出 **valid** 信号指示插值后哪些样本有效。

当输入数据类型为浮点类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或 fixed-point 类型时，**数据类型** 选项卡上的 **Output** 参数控制输出数据类型。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** Yes

### **valid** — 指示输出数据有效的标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新输入数据的标量

控制信号，指示模块已准备好在下个周期接收新的输入数据样本。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块在下一个时间步忽略任何输入数据。

**数据类型：** `Boolean`

## 参数

### 主

### **Coefficient source** — 滤波器系数的来源 `Property`（默认） | `Input port (Parallel interface)`

*自 R2025a 起*

您可以将常量滤波器系数作为参数输入，也可以通过输入端口提供时变滤波器系数。

当您选择 `Input port (Parallel interface)` 时，模块上会出现 **coeff** 端口。

选择 `Input port (Parallel interface)` 会启用 **Coefficients prototype** 参数。指定原型以使模块能够根据系数值优化滤波器实现。

当您将可编程系数与基于帧的输入一起使用时，系数值更改后的输出可能与标量情况下的输出不完全匹配。出现此差异的原因是，与标量实现相比，子滤波器计算相对于输入系数值在不同时间执行。

### **Coefficients** — FIR 滤波器系数 `fir1(35,0.4)`（默认） | 实数值或复数值向量

FIR 滤波器系数，指定为实数值或复数值向量。您可以将该向量指定为工作区变量或滤波器设计函数的调用。当输入数据类型为浮点类型时，模块将系数转换为与输入相同的数据类型。当输入数据类型为整数类型或 fixed-point 类型时，请在 **数据类型** 选项卡上设置系数的数据类型。

**示例：** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0 0])` 使用线性相位滤波器设计函数定义系数。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

**复数支持：** Yes

### **Coefficients prototype** — 原型滤波器系数 `[]`（默认） | 实数或复数向量

*自 R2025a 起*

原型滤波器系数，指定为实数或复数值向量。原型指定一个样本系数向量，该向量代表预期输入系数的零值位置。如果所有输入系数向量都具有相同的零值系数位置，请将 **Coefficients prototype** 设置为其中一个向量。模块使用该原型通过移除零值系数的乘法器来优化滤波器。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Input port (Parallel interface)`。

### **Filter structure** — HDL 滤波器架构 `Direct form systolic`（默认） | `Direct form transposed`

将 HDL 滤波器架构指定为以下结构之一：

- `Direct form systolic` — 此架构提供并行或部分串行滤波器实现，可高效利用 Intel 和 Xilinx DSP HDL 模块。对于部分串行实现，请为 **Minimum number of cycles between valid input samples** 参数指定大于 1 的值。您不能将基于帧的输入与部分串行架构一起使用。
- `Direct form transposed` — 此架构是完全并行实现，适用于 FPGA 和 ASIC 应用。

模块使用 Discrete FIR Filter 模块实现多相分解滤波器。在系数和串行选项允许的情况下，每个滤波器相位在内部共享资源。有关架构详细信息，请参阅 FIR Filter Architectures for FPGAs and ASICs。当您使用部分串行 systolic 架构且 **Minimum number of cycles between valid input samples** 大于滤波器长度除以插值因子时，模块将每个系数相位交错到单个 FIR 滤波器上，以在各相位之间共享资源。

### **Interpolation factor** — 插值因子 2（默认） | 大于二的整数

指定大于二的整数插值因子。输出向量大小为 *InputSize* \* *InterpolationFactor*。输出向量大小必须小于 64 个样本。

### **Minimum number of cycles between valid input samples** — 输入时序的串行化要求 `1`（默认） | 正整数

输入时序的串行化要求，指定为正整数。此参数表示 *N*，即有效输入样本之间的最小周期数。当您将 **Minimum number of cycles between valid input samples** 设置为大于滤波器长度 *L*，且输入和系数均为实数时，滤波器使用单个乘法器。

由于模块在串行化之前应用系数优化，最终滤波器的共享因子可能低于您指定的周期数。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form systolic`。

您不能将基于帧的输入与大于 1 的 **Minimum number of cycles between valid input samples** 一起使用。

### **Optimize symmetric coefficients** — 为对称系数共享乘法器 on（默认） | off

*自 R2024b 起*

启用在多相滤波器架构中跨对称系数共享乘法器。此优化可减少延迟并将乘法器数量减半。

对称滤波器系数的多相分解不会在每个多相分支中产生对称性。例如，如果滤波器系数为 `[1 2 3 4 4 3 2 1]`，分解后的两个多相分支为 `[1 3 4 2]` 和 `[2 4 3 1]`。对称对优化会重构系数，以恢复多相分支上的对称性。该实现包含一个后置加法器，用于合并重构后的多相分支的输出样本。滤波器输出与非优化实现的输出相同。

#### 依赖关系

要启用此参数，请将 **Coefficients source** 设置为 `Property`。

### 数据类型

### **Rounding mode** — 用于对输出进行类型转换的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

用于将输出类型转换为 **Output** 参数指定的数据类型的舍入模式。当输入数据类型为浮点类型时，模块忽略此参数。有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 用于对输出进行类型转换的溢出处理 `off`（默认） | `on`

用于将输出类型转换为 **Output** 参数指定的数据类型的溢出处理。当输入数据类型为浮点类型时，模块忽略此参数。有关更多详细信息，请参阅 Overflow Handling。

### **Coefficients** — 滤波器系数的数据类型 `Inherit: Same word length as input`（默认） | `<data type expression>`

当输入为 fixed-point 或整数类型时，模块使用此参数中的规则或数据类型转换滤波器系数。量化舍入到最接近的可表示值，并在溢出时饱和。当输入数据类型为浮点类型时，模块忽略此参数，所有内部算术使用与输入相同的数据类型。

此参数推荐的数据类型为 `Inherit: Same word length as input`。

如果出现以下任一情况，模块将返回警告或错误。

- 系数数据类型没有足够的小数长度来准确表示系数。
- 系数数据类型为无符号，且系数包含负值。

### **Output** — 滤波器输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same word length as input` | `<data type expression>`

当输入为 fixed-point 或整数类型时，模块使用此参数中的规则或数据类型转换滤波器输出。量化使用 **Rounding mode** 和 **Overflow mode** 参数的设置。当输入数据类型为浮点类型时，模块忽略此参数，并以与输入相同的数据类型返回输出。

模块在每个滤波器抽头内增加字长以实现全精度，并将最终输出转换为指定类型。最大最终内部数据类型 (*WF*) 取决于输入数据类型 (*WI*)、系数数据类型 (*WC*) 和系数数量 (*L*)，公式为

`WF = WI + WC + ceil(log2(L))`。

由于系数值限制了潜在增长，通常实际全精度内部字长小于 *WF*。

### 控制端口

### **Enable reset input port** — 启用复位输入端口的选项 `off`（默认） | `on`

选中此复选框以启用 **reset** 输入端口。复位信号实现数据路径寄存器的局部同步复位。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认） | `on`

选中此复选框以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观，也不会修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步的，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022a 中引入**

### R2025a：可编程系数

模块提供可选的 **coeff** 端口，以允许随时更改系数。将 **Coefficient source** 参数设置为 `Input port`，并将滤波器系数指定为实数或复数值的行向量。

您可以指定 **Coefficients prototype** 来指示一致的零值系数位置，例如，如果所有输入系数都是半带滤波器。给定原型后，模块会移除零值系数的乘法器。

### R2024b：优化对称系数

使用 **Optimize symmetric coefficients** 参数启用在多相滤波器架构中优化对称系数乘法器。此优化可减少延迟并将乘法器数量减半。

### R2022b：增加资源共享

当 **Minimum number of cycles between valid input samples** 大于滤波器长度时，模块交错系数以在多相分支之间共享乘法器。要使用最少乘法器数量实现滤波器，请将 **Minimum number of cycles between valid input samples** 设置为 `Inf`。

在 R2022a 中，部分串行 FIR 插值器可使用的最小乘法器数量为 *InterpolationFactor* 个乘法器，这发生在 **Minimum number of cycles between valid input samples** 等于滤波器长度时。将 **Minimum number of cycles between valid input samples** 增加到滤波器长度以上不会带来额外的资源共享。

## 描述

有限脉冲响应（FIR）插值滤波器

FIR Interpolator 模块实现一个针对 HDL 代码生成优化的单速率多相 FIR 插值滤波器。该模块提供带有输入和输出控制信号的硬件友好接口。为了提供生成 HDL 代码的周期精确仿真，该模块对架构延迟进行建模，包括流水线寄存器和资源共享。

该模块接受标量或向量输入，并根据插值因子和输入样本之间的周期数输出标量或向量。该模块使用 *InterpolationFactor* 个子滤波器实现多相分解。如果输入样本之间存在规则间隔，滤波器可以实现串行架构。

该模块提供两种滤波器结构。direct form systolic 架构提供一种实现，可高效利用 Intel® 和 Xilinx® DSP 模块。此架构可以是完全并行或串行的。要使用串行架构，输入样本之间必须以规则数量的无效周期隔开。direct form transposed 架构是完全并行实现，适用于 FPGA 和 ASIC 应用。对于使乘法器、流水线寄存器和前置加法器与 FPGA 供应商的 DSP 配置匹配的滤波器实现，请在生成 HDL 代码时指定目标器件。

所有滤波器结构都通过为对称或反对称滤波器共享乘法器，以及移除零值系数（例如半带滤波器和希尔伯特变换中）的乘法器来优化硬件资源。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此外部优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
