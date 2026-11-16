---
type: simulink-block
title: 'FIR Rate Converter'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'firrateconverter'
documentation_source_path: 'ref/firrateconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Rate Converter

## 端口

### 输入

### **data** — 输入数据样本 标量 | 行向量

输入数据样本，指定为标量，或指定为行向量，其中每个元素表示一个独立通道。该模块接受实数或复数数据。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

控制信号，用于指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，模块忽略来自输入 **data** 端口的值。

您可以每隔 `ceiling(L/M)` 个时间步应用一个有效数据样本。

**数据类型：** `Boolean`
### 输出

### **data** — 输出数据样本 标量 | 行向量

输出数据样本，返回为标量或行向量，其中每个元素表示一个独立通道。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，用于指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，用于指示模块已准备好在下一个周期接收新的输入数据样本。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，模块会忽略下一个时间步中的任何输入数据。

#### 依赖项

要启用此端口，请选中 **启用 ready 输出端口** 复选框。

**数据类型：** `Boolean`

## 参数

### 主要

### **插值因子** — 插值因子 `3`（默认） | 正整数

指定模块对输入数据样本进行插值的因子。

### **抽取因子** — 抽取因子 `2`（默认） | 正整数

指定模块对输入数据样本进行抽取的因子。

### **FIR 滤波器系数** — FIR 滤波器系数 `firpm(70, [0 0.28 0.32 1],[1 1 0 0])`（默认） | 行向量

指定按 *z-1* 的降幂排列的系数行向量。

您还可以将系数指定为工作区变量，或指定为对 Signal Processing Toolbox™ 滤波器设计函数（例如 `fir1`）的调用。设计归一化截止频率不大于 `min(1/L,1/M)` 的低通滤波器。该模块将内部滤波器状态初始化为零。

当输入数据类型为浮点类型时，模块将系数强制转换为与输入相同的数据类型。当输入数据类型为整数类型或定点类型时，请在 **数据类型** 选项卡上设置系数的数据类型。

### 数据类型

### **舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

选择定点运算的舍入模式。有关详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出是饱和还是绕回。

- `off` — 溢出绕回到该数据类型可以表示的相应值。例如，由于 130 无法容纳在有符号 8 位整数中，因此它会绕回到 -126。
- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。例如，与有符号 8 位整数关联的溢出可以饱和到 -128 或 127。

### **系数** — FIR 滤波器系数数据类型 `fixdt(1,16,16)`（默认）

FIR 滤波器系数数据类型，指定为具有 `signedness`、`word length` 和 `fractional length` 属性的 `fixdt(s,wl,fl)` 对象。当输入为定点或整数类型时，模块使用此参数中的规则或数据类型来强制转换滤波器系数。量化会舍入到最接近的可表示值，并在溢出时饱和。当输入数据类型为浮点类型时，模块忽略此参数，并且所有内部算术都使用与输入相同的数据类型。

### **输出** — 输出数据样本的数据类型 `Inherit: Same word length as input`（默认） | `Inherit via internal rule` | `fixdt(s,wl,fl)`

当输入为定点或整数类型时，模块使用此参数中的规则或数据类型来强制转换滤波器的输出。量化使用 **舍入模式** 和 **溢出模式** 参数的设置。当输入数据类型为浮点类型时，模块忽略此参数，并以与输入相同的数据类型返回输出。

### 控制端口

### **启用 ready 输出端口** — 用于启用 ready 控制信号的选项 `off`（默认） | `on`

选择此参数以启用 **ready** 端口。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持为 Simulink 加速器和快速加速器模式以及 DPI 组件生成进行 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015b 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 FIR Rate Conversion HDL Optimized，并且包含在 DSP System Toolbox™ **DSP System Toolbox HDL Support** 库中。

### R2022a：移除 request 端口

在之前的版本中，该模块提供可选的 **request** 端口。此端口不再可用。有关在模型中控制数据速率的替代方法，请参阅使用 ready 信号控制数据速率。

### R2022a：同步 ready 信号

**ready** 信号现在在模块输出处流水线化。在之前的版本中，**ready** 输出信号是直接馈通，没有输出流水线寄存器。

## 描述

对输入信号进行上采样、滤波和下采样

FIR Rate Converter 模块对输入信号进行上采样、滤波和下采样。它针对 HDL 代码生成进行了优化，并且每次对每个通道的一个样本进行操作。该模块实现多相架构，以避免不必要的算术运算和高中间采样率。

高层速率转换器架构

该模块按整数因子 *L* 对输入信号进行上采样，将其应用于 FIR 滤波器，并按整数因子 *M* 对输入信号进行下采样。

您可以使用输入和输出控制端口来控制样本流。在默认配置中，该模块使用输入和输出 **valid** 控制信号。为了实现额外的流控制，您可以启用 **ready** 输出信号。

**ready** 输出端口指示该模块可以在下一个时间步接受新的输入数据样本。当 *L* ≥ *M* 时，您可以使用 **ready** 信号来实现连续输出数据样本。如果在每次模块将 **ready** 信号返回为 `1` 后应用新输入样本，则该模块会在每个时间步返回一个输出 **valid** 信号设置为 `1` 的数据输出样本。

当您禁用 **ready** 端口时，只能每隔 `ceil(L/M)` 个时间步应用一个有效数据样本。例如，如果：

- *L*/*M* = 4/5，则可以在每个时间步应用新输入样本。
- *L*/*M* = 3/2，则可以在每隔一个时间步应用新输入样本。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建 Simulink® 模型。该应用提供与 Simulink 模块相同的接口和配置选项。
