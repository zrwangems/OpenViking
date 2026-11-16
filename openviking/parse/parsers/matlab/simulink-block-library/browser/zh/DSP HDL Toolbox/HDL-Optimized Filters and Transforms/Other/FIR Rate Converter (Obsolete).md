---
type: simulink-block
title: 'FIR Rate Converter (Obsolete)'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms / Other'
documentation_page: 'firrateconverterobsolete'
documentation_source_path: 'ref/firrateconverterobsolete.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Rate Converter (Obsolete)

## 端口

### 输入

### **data** — 输入数据样本 标量 | 行向量

输入数据样本，指定为标量，或指定为行向量，其中每个元素表示一个独立通道。该模块接受实数或复数数据。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当 **valid** 为 `1`（`true`）时，该模块从输入 **data** 端口捕获值。当 **valid** 为 `0`（`false`）时，该模块忽略来自输入 **data** 端口的值。

您可以每隔 `ceiling(L/M)` 个时间步施加一个有效数据样本。

**数据类型：** `Boolean`

### **request** — 请求控制信号 标量

当 **request** 端口为 `1`，并且有输出数据样本可用时，在下一个周期，该模块在输出 **data** 端口上返回该输出数据样本，并将输出 **valid** 信号设置为 `1`。当没有新数据可用时，该模块将输出 **valid** 信号设置为 `0`。当 **request** 端口为 `0` 时，该模块保持可用数据，直到 **request** 端口设置为 `1`。

您可以将 **request** 输入端口连接到下游模块的 **ready** 输出端口。

**数据类型：** `Boolean`

### 输出

### **data** — 输出数据样本 标量 | 行向量

输出数据样本，以标量或行向量形式返回，其中每个元素表示一个独立通道。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出 **data** 端口的数据是否有效。当 **valid** 为 `1`（`true`）时，该模块从输出 **data** 端口返回有效数据。当 **valid** 为 `0`（`false`）时，来自输出 **data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，指示该模块已准备好在下一个周期接收新的输入数据样本。当 **ready** 为 `1`（`true`）时，您可以为下一个时间步指定 **data** 和 **valid** 输入。当 **ready** 为 `0`（`false`）时，该模块在下一个时间步忽略任何输入数据。

您可以将 **ready** 输出端口连接到上游模块的 **request** 输入端口。

#### 依赖项

要启用此端口，请选中 **启用 ready 输出端口** 复选框。

**数据类型：** `Boolean`

## 参数

### 主要

### **插值因子** — 插值因子 `3`（默认） | 正整数

指定一个因子，该模块按此因子对输入数据样本进行插值。

### **抽取因子** — 抽取因子 `2`（默认） | 正整数

指定一个因子，该模块按此因子对输入数据样本进行抽取。

### **FIR 滤波器系数** — FIR 滤波器系数 `firpm(70, [0 0.28 0.32 1],[1 1 0 0])`（默认） | 行向量

指定一个系数行向量，按 *z-1* 的降幂排列。

**注意**

您可以使用 Signal Processing Toolbox™ 滤波器设计函数（例如 `fir1`）生成滤波器系数。设计归一化截止频率不大于 `min(1/L,1/M)` 的低通滤波器。该模块将内部滤波器状态初始化为零。

### 数据类型

### **舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

选择定点运算的舍入模式。有关更多信息，请参阅 Rounding mode。

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出是饱和还是回绕。

- `off` — 溢出回绕到该数据类型可以表示的适当值。例如，由于 130 无法放入有符号 8 位整数，因此回绕为 -126。
- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。例如，与有符号 8 位整数关联的溢出可以饱和到 -128 或 127。

### **系数** — FIR 滤波器系数数据类型 `fixdt(1,16,16)`（默认）

FIR 滤波器系数数据类型，指定为具有 `signedness`、`word length` 和 `fractional length` 属性的 `fixdt(s,wl,fl)` 对象。

### **输出** — 输出数据样本的数据类型 `Inherit: Same word length as input`（默认） | `Inherit via internal rule` | `fixdt(s,wl,fl)`

指定输出数据样本的数据类型。

### 控制端口

### **启用 ready 输出端口** — 启用 ready 控制信号的选项 `off`（默认） | `on`

选择此参数以启用 **ready** 端口。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2015b 中引入**

### R2022a：从 DSP System Toolbox 移至 DSP HDL Toolbox

在 R2022a 之前，此模块名为 FIR Rate Conversion HDL Optimized，并且包含在 DSP System Toolbox™ 的 **DSP System Toolbox HDL Support** 库中。

### R2022a：在未来版本中移除 request 端口

FIR Rate Converter 模块上的 **request** 端口不再受支持。使用 **request** 端口的 FIR Rate Converter 模块现有实例将转发到此模块，此模块具有不可选的 request 端口。此模块将在未来版本中移除。

而应使用不带 **request** 端口的 FIR Rate Converter 模块，并通过在模块外使用 FIFO 控制输入数据速率。请参阅 Control Data Rate Using Ready Signal。

### R2022a：request 与 validOut 之间有一个周期延迟

此模块在 **request** 输入端口上有一个寄存器。此寄存器意味着将 **request** 设置为 `1`（`true`）与模块在 **dataOut** 和 **validOut** 端口上返回数据之间存在一个周期延迟。

## 描述

对输入信号进行上采样、滤波和下采样（带 request 端口）

FIR Rate Converter 模块对输入信号进行上采样、滤波和下采样。它针对 HDL 代码生成进行了优化，并且一次对每个通道的一个样本进行操作。该模块实现多相架构，以避免不必要的算术运算和高中间采样率。

高层速率转换器架构

该模块将输入信号上采样整数因子 *L*，将其应用于 FIR 滤波器，然后下采样整数因子 *M*。

您可以使用输入和输出控制端口来调节样本流。在默认配置中，该模块使用输入和输出 **valid** 控制信号。该模块具有一个 **request** 端口来控制输出速率。对于输入流控制，您可以启用 **ready** 输出信号。

显示 valid、ready 和 request 控制信号的架构图

**ready** 输出端口指示该模块可以在下一个时间步接受新的输入数据样本。当 *L* ≥ *M* 时，您可以使用 **ready** 信号获得连续输出数据样本。如果您在每次模块返回 **ready** 信号为 `1` 后施加新的输入样本，则该模块将在每个时间步返回一个输出 **valid** 信号设置为 `1` 的数据输出样本。

当您禁用 **ready** 端口时，您只能每隔 `ceil(L/M)` 个时间步施加一个有效数据样本。例如，如果：

- *L*/*M* = 4/5，则您可以每个时间步施加一个新的输入样本。
- *L*/*M* = 3/2，则您可以每隔一个时间步施加一个新的输入样本。

该模块在 **request** 信号为 `1` 且有效输出样本可用之后的一个周期返回下一个输出样本。当没有新数据可用时，模块将输出 **valid** 信号设置为 `0`。

您可以将 **request** 输入端口连接到下游模块的 **ready** 输出端口。
