---
type: simulink-block
title: 'LMS Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Adaptive Filters'
documentation_page: 'lmsfilter'
documentation_source_path: 'ref/lmsfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# LMS Filter

## 端口

### 输入

### **Input** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

当输入为定点时，它必须是有符号的。

当您将 **Algorithm** 参数设置为 `Sign—Error LMS`、`Sign—Data LMS` 或 `Sign—Sign LMS` 时，通过 **Input** 端口输入的数据必须为实数。

**数据类型：** `single` | `double` | `fixed point`

### **Desired** — 期望信号 标量 | 列向量

期望信号，指定为标量或列向量。期望信号必须与 `Input` 信号具有相同的数据类型、复杂度和维度。

当 **Input** 为定点时，期望信号必须是有符号定点。

当您将 **Algorithm** 参数设置为 `Sign—Error LMS`、`Sign—Data LMS` 或 `Sign—Sign LMS` 时，通过 **Desired** 端口输入的数据必须为实数。

**数据类型：** `single` | `double` | `fixed point`

### **Step-size** — 步长 标量

输入步长 *μ*。对于归一化 LMS 方程的收敛，0<*µ*<2。输入类型必须与 `Input` 端口的类型匹配。

当 **Input** 为定点时，步长必须是有符号定点。

#### 依赖关系

仅当您将 `Specify step size via` 参数设置为 `Input port` 时，此端口才会出现。

**数据类型：** `single` | `double` | `fixed point`

### **Adapt** — 更新滤波器权重 标量

当此端口的输入大于零时，模块会持续更新滤波器权重。当此端口的输入小于或等于零时，滤波器权重保持其当前值。

#### 依赖关系

仅当您将 `Adapt port` 参数设置为 `on` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `Boolean`

### **Reset** — 重置滤波器权重 标量

用于将滤波器权重的值重置为其初始值的信号，指定为标量。每当在 Reset 端口检测到重置事件时，模块都会重置滤波器权重。重置信号速率必须与数据信号输入的速率相同。

有关重置事件类型，请参阅 `Reset` 参数。

#### 依赖关系

仅当您将 **Reset port** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `Boolean`

### 输出

### **Output** — 期望信号的估计 标量 | 列向量

期望信号的估计，以标量或列向量形式返回。其大小和复杂度与输入信号相同。

输出信号的数据类型与期望信号相同。

**数据类型：** `single` | `double` | `fixed point`

### **Error** — 输出与期望信号之间的误差 标量 | 列向量

输出与期望信号之间的误差，以标量或列向量形式返回。此误差是从期望信号中减去输出信号的结果。

误差信号的数据类型与期望信号相同。

**数据类型：** `single` | `double` | `fixed point`

### **Wts** — 滤波器权重 标量 | 列向量

滤波器权重，以标量或列向量形式返回。对于每次迭代，模块从此端口输出当前更新后的滤波器权重。

对于浮点信号，权重的数据类型必须与 `Input` 端口的类型匹配。对于定点信号，遵循 `Weights` 参数。

#### 依赖关系

仅当您将 `Output filter weights` 参数设置为 `On` 时，此端口才会出现。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 主选项卡

### **Algorithm** — 选择算法 `LMS`（默认） | `Normalized LMS` | `Sign-Error LMS` | `Sign-Data LMS` | `Sign-Sign LMS`

选择用于计算滤波器权重的算法。

### **Filter length** — 滤波器长度 `32`（默认） | 标量

输入 FIR 滤波器权重向量的长度。

### **Specify step size via** — 指定步长的方式 `Dialog`（默认） | `Input port`

- `Dialog` –– 使用 **Step size (mu)** 参数指定步长。
- `Input port` –– 使用 `Step-size` 端口指定步长。

### **Step size (mu)** — 步长 `0.1`（默认） | 正标量

输入步长 *μ*。对于归一化 LMS 方程的收敛，0<*µ*<2。

**可调：** Yes

#### 依赖关系

仅当您将 `Specify step size via` 参数设置为 `Dialog` 时，此参数才会出现。

### **Leakage factor (0 to 1)** — 泄漏因子 `1.0`（默认） | 标量

输入泄漏因子，0 < 1 – μα ≤ 1。

**可调：** Yes

### **Initial value of filter weights** — 滤波器权重的初始值 `0`（默认） | 向量 | 标量

输入初始滤波器权重 **w**(0)，以向量或标量形式。当您输入标量时，模块使用该标量值创建滤波器权重向量。此向量长度等于滤波器长度，且其所有值都等于该标量值。

### **Adapt port** — 启用 Adapt 端口 `off`（默认） | `on`

选中此复选框以启用 `Adapt` 输入端口。

### **Reset port** — Reset 端口 `None`（默认） | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当您想要将滤波器权重的值重置为其初始值时，请使用 **Reset port** 参数。重置信号必须与数据信号输入的速率相同。

选择 `None` 以禁用 `Reset` 端口。要启用 **Reset** 端口，请从列表中选择以下项之一：

- `Rising edge` — 当 **Reset** 输入执行以下操作之一时触发重置操作：

  - 从负值上升为正值或零
  - 从零上升为正值，其中该上升不是从负值上升为零的延续（参见下图）

- `Falling edge` — 当 **Reset** 输入执行以下操作之一时触发重置操作：

  - 从正值下降为负值或零
  - 从零下降为负值，其中该下降不是从正值下降为零的延续（参见下图）

- `Either edge` — 当 **Reset** 输入为 `Rising edge` 或 `Falling edge` 时触发重置操作
- `Non-zero sample` — 在 Reset 输入不为零的每个采样时间触发重置操作

### **Output filter weights** — 输出滤波器权重 `on`（默认） | `off`

选择 **Output filter weights** 参数以从 `Wts` 端口导出滤波器权重。对于每次迭代，模块从此端口输出当前更新后的滤波器权重。

### 数据类型选项卡

### **Rounding mode** — 舍入操作的方法 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认） | on

选中此参数时，模块会对其定点运算的结果进行饱和处理。清除此参数时，模块会对其定点运算的结果进行环绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Parameters** — 参数 `Same word length as first input`（默认） | `Specify word length` | `Binary point scaling`

选择如何指定泄漏因子和步长的字长与小数长度：

- `Same word length as first input` –– 泄漏因子和步长的字长与模块第一个输入的字长匹配。在此模式下，泄漏因子和步长的小数长度自动设置为仅二进制点缩放，该缩放根据系数的值和字长为提供可能的最佳精度。
- `Specify word length` –– 您可以输入泄漏因子和步长的字长，以位为单位。在此模式下，泄漏因子和步长的小数长度自动设置为仅二进制点缩放，该缩放根据系数的值和字长为提供可能的最佳精度。
- `Binary point scaling` –– 您可以输入泄漏因子和步长的字长和小数长度，以位为单位。泄漏因子和步长必须具有相同的字长，但小数长度可以不同。

对于 `Specify step size via` 参数，如果您选择 `Input port`，则泄漏因子的字长与 `Step-size` 端口处步长输入的字长相同。泄漏因子的小数长度会根据泄漏因子的字长自动设置为可能的最佳精度。

#### 依赖关系

仅当您将 **Specify step size via** 参数设置为 `Dialog` 时，此参数才可见。

### **Weights** — 滤波器权重的字长和小数长度 `Same as first input`（默认） | `Binary point scaling`

选择如何指定模块的滤波器权重的字长和小数长度：

- `Same as first input` –– 滤波器权重的字长和小数长度与模块第一个输入的字长和小数长度匹配。
- `Binary point scaling` –– 您可以输入滤波器权重的字长和小数长度，以位为单位。

### **Product and quotient** — 乘积和商的字长与小数长度 `Same as first input`（默认） | `Binary point scaling`

选择如何指定 **u'u**、**W'u**、μ⋅e、Q⋅u 以及商 Q 的字长和小数长度。这里，**u** 是输入向量，**W** 是滤波器权重向量，*μ* 是步长，*e* 是误差，*Q* 是商，其定义为 Q=μ⋅eu'u

- `Same as first input` –– 这些量的字长和小数长度与模块第一个输入的字长和小数长度匹配。
- `Binary point scaling` –– 您可以输入这些量的字长和小数长度，以位为单位。这些量的字长必须相同，但小数长度可以不同。

### **Accumulator** — 累加器的字长和小数长度 `Same as first input`（默认） | `Binary point scaling`

使用此参数指定希望如何为 **u'u** 和 **W'u** 运算的累加器指定字长和小数长度。

**注意**

不要使用此参数为 Q⋅u 运算的累加器指定字长和小数长度。此量的累加器数据类型会自动设置为与乘积数据类型相同。此累加器的最小值、最大值和溢出信息会作为乘积信息的一部分记录。自动缩放将此乘积和累加器视为一种数据类型。

- `Same as first input` –– 这些特性与模块输入的特性匹配。
- `Binary point scaling` –– 您可以输入累加器的字长和小数长度，以位为单位。两个累加器的字长必须相同，但小数长度可以不同。

有关此模块中累加器数据类型用法的图示，请参阅定点数据类型和乘法数据类型。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选中此参数可防止定点工具覆盖您在模块对话框框中指定的数据类型。

## 所属库

DSP System Toolbox / Filtering / Adaptive Filters DSP System Toolbox HDL Support / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

**使用 Intel® AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

在以下条件下，LMS Filter 模块支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- 您将 **Algorithm** 设置为 `LMS` 或 `Normalized LMS`。
- 输入信号为实数值。
- 输入信号的数据类型为 `single` 或 `double`。

要使用此工作流从此模块生成 SIMD 代码，请参阅使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码。

**通过利用目标硬件指令集扩展生成 SIMD 代码** *（自 R2023b 起）*

**注意**

需要 Simulink® Coder™ 或 Embedded Coder 许可证

在以下条件下，您可以通过使用模型配置参数 **Leverage target hardware instruction set extensions**，为 LMS Filter 模块在所有 Intel 平台、ARM® Cortex®-A 处理器和 Apple silicon 处理器上生成 SIMD 代码：

- 您将 **Algorithm** 设置为 `Sign-Error LMS`、`Sign-Data LMS`、`Sign-Sign LMS`、`LMS` 或 `Normalized LMS`。
- 输入信号为实数值，且滤波器系数为实数
- 输入信号为复数值，且滤波器系数为实数或复数。
- 输入信号的数据类型为 `single`（ARM Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或 `double`（Intel 平台）

此外，请适当配置您的模型。在 Simulink 模型窗口的 **Modeling** 选项卡中，点击 **Model Settings**，并在 **Code Generation** 下配置这些参数。

- 在 **Optimization** 窗格中：

  - 在 **Leverage target hardware instruction set extensions** 参数中提供特定的指令集。
  - 选择 **Optimize reductions** 参数。
  - 在 **Optimization levels** 下，将 **Level** 设置为 `Maximum`，将 **Priority** 设置为 `Maximize execution speed`。
- 在 **Interface** 窗格中，在 **Software environment** 下，清除 **non-finite numbers**。

要使用此工作流从此模块生成 SIMD 代码，请参阅使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Intel 平台）、使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Apple silicon）和使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 ARM Cortex-A 处理器）。

对于受支持模块上的计算密集型运算，SIMD 内建函数可以显著提高生成代码在 Intel 平台上的性能。有关更多详细信息，请参阅使用 SIMD 优化归约运算的代码 (Simulink Coder)。

有关 DSP System Toolbox™ 中 SIMD 代码生成的更多信息，请参阅 SIMD 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**注意**

对于具有硬件友好控制信号且要在 Simulink 中仿真 HDL 延迟的 LMS 滤波器，或者对于具有复数系数的复数数据，请使用 LMS Filter (DSP HDL Toolbox) 模块而非此模块。

**HDL 架构**

默认情况下，LMS Filter 实现会对滤波器的 FIR 部分使用线性和。

在以下条件下，LMS Filter 实现树状求和（其关键路径更短）：

- LMS Filter 与实数数据一起使用。
- Accumulator **W'u** 数据类型的字长至少比 Product W'u 数据类型的字长宽 `ceil(log2(filter length))` 位。
- Accumulator **W'u** 数据类型与 Product **W'u** 数据类型具有相同的小数长度。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持针对复数信号的代码生成。

**限制**

- HDL Coder 不支持 LMS Filter 的 `Normalized LMS` 算法。
- `Reset` 端口仅支持 `Boolean` 和 `unsigned` 输入。
- `Adapt` 端口仅支持 `Boolean` 输入。
- **Filter length** 必须大于或等于 2。

## 版本历史

**在 R2006a 之前引入**

### R2024b：为 Apple silicon 处理器生成 SIMD 代码

在 R2024b 中，如果您拥有 Embedded Coder，则可以使用模型配置参数 **Leverage target hardware instruction set extensions** 为 Apple silicon 处理器生成 LMS Filter 模块的 SIMD 代码。有关更多信息，请参阅使用目标硬件指令集扩展从 Simulink 模块生成 SIMD 代码（适用于 Apple silicon）。

### R2023b：为复数信号生成 SIMD 代码

在 R2023b 中，如果您拥有 Embedded Coder，则可以使用模型配置参数 **Leverage target hardware instruction set extensions**，在输入信号为复数值时为 LMS Filter 模块生成 SIMD 代码。

## 描述

使用最小均方（LMS）自适应算法计算输出、误差和权重

LMS Filter 模块可以使用五种不同的算法实现自适应 FIR 滤波器。该模块估计最小化输出信号 *y(n)* 与期望信号 *d(n)* 之间误差 *e(n)* 所需的滤波器权重或系数。输出是滤波后的输入信号，即期望信号的估计。Error 端口输出从期望信号中减去输出信号的结果。

在特定条件下，此模块还支持 SIMD 代码生成。有关详细信息，请参阅代码生成。
