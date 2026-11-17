---
type: simulink-block
title: 'Farrow Rate Converter'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'farrowrateconverter'
documentation_source_path: 'ref/farrowrateconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Farrow Rate Converter

## 端口

### 输入

### **data** — 输入数据 实数或复数标量

输入数据，指定为实数或复数标量。当输入数据类型为整数类型或定点类型时，模块使用定点算术进行内部计算。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **rate** — 速率变化因子 标量

将速率变化因子指定为正有理数值，即输入采样率与输出采样率之比 `Fin/Fout`。速率变化因子没有限制。

当此输入值变化时，模块会重置内部相位累加器。此重置意味着您可以将速率变化因子从抽取更改为插值。例如，您可以使用此模块来对齐具有相似但变化的采样时钟的数据流。

模块从此信号的数据类型推导内部累加器的数据类型。速率变化的数据类型必须至少有一位整数位和一位小数位。累加器数据类型为 `fixdt(1,fractionalWL+1,fractionalWL)`，其中 *fractionalWL* 是速率变化数据类型的小数长度。*fractionalWL* 决定相位时序的精度，但也会增加关键路径。当速率变化字长较大时，您可以通过将被乘数数据类型适配到 FPGA 上的 DSP 模块来限制硬件资源使用。

#### 依赖关系

要启用此端口，请将 **Rate change source** 参数设置为 `Input port`。

**数据类型：** `fixed point`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为 `1`（`true`）时，模块停止当前计算并清除内部状态。当 **reset** 为 `0`（`false`）且输入 **valid** 为 `1`（`true`）时，模块捕获数据以进行处理。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上选择 **Enable reset input port**。

**数据类型：** `Boolean`
### 输出

### **data** — 滤波后的输出数据 实数或复数标量

滤波后的输出数据，以实数或复数标量形式返回。当输入数据类型为浮点数据类型时，输出数据继承输入数据的数据类型。当输入数据类型为整数类型或定点类型时，**Data Types** 选项卡上的 **Output** 参数控制输出数据类型。

**数据类型：** `fixed point` | `single` | `double`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，指示模块已准备好在下一个周期接收新的输入数据样本。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块在下一个时间步忽略任何输入数据。

**数据类型：** `Boolean`

## 参数

### 主要

### **Rate change source** — 速率变化的来源 `Property`（默认）| `Input port`

您可以将恒定速率变化作为参数输入，或通过使用输入端口提供时变速率变化。

选择 `Input port` 会启用模块上的 **rate** 端口。

### **Rate change (fsin/fsout)** — 速率变化因子 `147/160`（默认）| 正实数标量

将速率变化因子指定为输入采样率与输出采样率之比 `Fin/Fout`，或提供正有理数值。速率变化因子没有限制。使用 **Data Types** 选项卡上的 **RateChange** 参数指定此值的数据类型。

#### 依赖关系

要启用此参数，请将 **Rate change source** 设置为 `Property`。

### **Coefficients matrix** — FIR 滤波器系数 `[-1/6 1/2 -1/3 0;1/2 -1 -1/2 1;-1/2 1/2 1 0;1/6 0 -1/6 0]`（默认）| 实数值矩阵

将 FIR 滤波器系数指定为 *M*×*N* 的实数值矩阵，其中 *N* 是滤波器数量，*M* 是每个滤波器中的系数数量。*N* 必须小于六。模块实现阶数为 *N* – 1 的多项式。默认值是特殊的闭式拉格朗日解，可实现大多数速率变化。

### **Filter structure** — HDL 滤波器架构 `Direct form systolic`（默认）| `Direct form transposed`

此模块使用与 Discrete FIR Filter 模块相同的架构来实现 FIR 滤波器级。将 HDL 滤波器架构指定为以下结构之一：

- `Direct form systolic` — 此架构提供完全并行的滤波器实现，可高效利用 Intel® 和 Xilinx® DSP 模块。有关架构详细信息，请参阅 Fully Parallel Systolic Architecture。
- `Direct form transposed` — 此架构是适用于 FPGA 和 ASIC 应用的完全并行实现。有关架构和性能详细信息，请参阅 Fully Parallel Transposed Architecture。

所有实现都共享对称和反对称系数的乘法器，并移除零值系数的乘法器。

### **Minimum number of cycles between valid input samples** — 输入时序的串行化要求 `1`（默认）| 正整数

输入时序的串行化要求，指定为正整数。此参数表示 *N*，即有效输入样本之间的最小周期数。要实现完全串行架构，请将 **Minimum number of cycles between valid input samples** 设置为大于滤波器长度 *L*，或设置为 `Inf`。

当此参数大于 1 时，模块将每个 FIR 子滤波器实现为部分串行架构，在时间上共享乘法器。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form systolic`。

### 数据类型

### **Rounding mode** — 输出类型转换的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

将输出类型转换为 **Output** 参数指定的数据类型时的舍入模式。当输入数据类型为浮点数据类型时，模块忽略此参数。有关更多详细信息，请参阅 Rounding Modes。

### **Saturate on integer overflow** — 输出类型转换的溢出处理 `off`（默认）| `on`

将输出类型转换为 **Output** 参数指定的数据类型时的溢出处理。当输入数据类型为浮点数据类型时，模块忽略此参数。有关更多详细信息，请参阅 Overflow Handling。

### **Coefficients** — 滤波器系数的数据类型 `Inherit: Same word length as input`（默认）| `<data type expression>`

模块将滤波器系数转换为此数据类型。量化舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点数据类型时，模块忽略此参数。

此参数的推荐数据类型为 `Inherit: Same word length as input`。选择此数据类型时，请考虑目标 FPGA 上 DSP 模块支持的尺寸。

### **RateChange** — 速率变化因子的数据类型 `fixdt(0,16)`（默认）| `<data type expression>`

模块将 **Rate change (fsin/fsout)** 参数值转换为此数据类型，并使用此数据类型推导内部累加器的数据类型。累加器数据类型为 `fixdt(0,fractionalWL+1,fractionalWL)`，其中 *fractionalWL* 是速率变化数据类型的小数长度。量化舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点数据类型时，模块忽略此参数。

此数据类型必须有足够的整数位来表示 `fsIn/fsOut` 值。如果指定的数据类型没有足够的整数位，模块将返回错误。默认设置未指定小数位数，因此模块可以计算必要的整数位。此数据类型必须至少有一位整数位和一位小数位。此数据类型的小数部分决定相位时序的精度，但也会增加关键路径。当速率变化字长较大时，您可以通过将被乘数数据类型适配到 FPGA 上的 DSP 模块来限制硬件资源。

#### 依赖关系

要启用此参数，请将 **Rate change source** 设置为 `Property`。

### **Multiplicand** — 被乘数的数据类型 `Inherit: Inherit via internal rule`（默认）| `<data type expression>`

模块将累加器的输出转换为此数据类型。量化舍入到最近的可表示值，并在溢出时饱和。当输入数据类型为浮点数据类型时，模块忽略此参数。当速率变化字长较大时，您可以通过控制被乘数数据类型来限制硬件资源使用。选择此数据类型时，请考虑目标 FPGA 上 DSP 模块支持的尺寸。

### **Output** — 滤波器输出的数据类型 `Inherit: Same as first input`（默认）| `<data type expression>`

模块将每个滤波器级的输出转换为此数据类型。量化使用 **Rounding mode** 和 **Overflow mode** 参数的设置。当输入数据类型为浮点数据类型时，模块忽略此参数。

### 控制端口

### **Enable reset input port** — 启用复位输入端口的选项 `off`（默认）| `on`

选中此复选框以启用 **reset** 输入端口。复位信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认）| `on`

选中此复选框以将生成的 HDL 全局复位信号连接到数据路径寄存器。此参数不会更改模块的外观，也不会修改 Simulink 中的仿真行为。当您清除此复选框时，生成的 HDL 全局复位仅清除控制路径寄存器。生成的 HDL 全局复位可以是同步或异步的，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅 Hardware Control Signals 页面上的 Reset Signal 部分。

## 所属库

DSP HDL Toolbox / Signal Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022a 中引入**

### R2022b：部分串行滤波器架构

此模块现在具有 **Minimum number of cycles between valid input samples** 参数，可通过部分串行 systolic 架构实现资源共享。每个滤波器级的内部 FIR 滤波器使用您指定的共享因子以部分串行 systolic 滤波器实现。

## 描述

多项式采样率转换器

Farrow Rate Converter 模块通过使用 FIR 滤波器实现多项式 sinc 近似来转换信号的采样率。当速率转换因子是大整数抽取和插值因子之比时，Farrow 滤波器是一种高效的速率转换器。通过提供输入采样率和所需的输出采样率来指定速率转换因子。您可以将速率转换因子作为固定参数或时变输入信号提供。

对于大多数速率转换，您可以将此模块与默认系数一起使用。默认系数是拉格朗日插值，与 DSP System Toolbox™ 中的 Farrow Rate Converter 模块匹配。或者，如果默认值不满足您的规格要求，您可以指定自定义系数集。

该模块提供具有输入和输出控制信号的硬件友好接口。为了提供生成 HDL 代码的周期精确仿真，该模块对架构延迟（包括流水线寄存器和乘法器优化）进行建模。

**注意**

您还可以使用 DSP HDL IP Designer 应用为此硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
