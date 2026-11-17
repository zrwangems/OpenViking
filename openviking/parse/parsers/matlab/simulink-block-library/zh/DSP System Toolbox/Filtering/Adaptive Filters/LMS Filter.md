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
```yaml
ports:
- name: Input
  summary: 输入信号 标量 | 列向量
  direction: input
  data_types: single | double | fixed point
- name: Desired
  summary: 期望信号 标量 | 列向量
  direction: input
  data_types: single | double | fixed point
- name: Step-size
  summary: 步长 标量
  direction: input
  data_types: single | double | fixed point
- name: Adapt
  summary: 更新滤波器权重 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | Boolean
- name: Reset
  summary: 重置滤波器权重 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | Boolean
- name: Output
  summary: 期望信号的估计 标量 | 列向量
  direction: output
  data_types: single | double | fixed point
- name: Error
  summary: 输出信号与期望信号之间的误差 标量 | 列向量
  direction: output
  data_types: single | double | fixed point
- name: Wts
  summary: 滤波器权重 标量 | 列向量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Input** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

当输入为定点时，它必须是有符号的。

当您将 **Algorithm** 参数设置为
`Sign—Error LMS`、
`Sign—Data LMS` 或
`Sign—Sign LMS` 时，通过 **Input** 端口输入的数据必须为实数。

**数据类型：** `single` | `double` | `fixed point`

### **Desired** — 期望信号 标量 | 列向量

期望信号，指定为标量或列向量。期望信号必须与
`Input` 信号具有相同的数据类型、复杂度和维度。

当 **Input** 为定点时，期望信号
必须为有符号定点。

当您将 **Algorithm** 参数设置为
`Sign—Error LMS`、
`Sign—Data LMS` 或
`Sign—Sign LMS` 时，通过 **Desired** 端口输入的数据必须为实数。

**数据类型：** `single` | `double` | `fixed point`

### **Step-size** — 步长 标量

输入步长 *μ*。为使归一化 LMS 方程收敛，0<*µ*<2。输入类型
必须与 `Input` 端口的类型匹配。

当 **Input** 为定点时，步长必须
为有符号定点。

#### 依赖关系

此端口仅在您将 `Specify step size via` 参数设置为
`Input port` 时出现。

**数据类型：** `single` | `double` | `fixed point`

### **Adapt** — 更新滤波器权重 标量

当此端口的输入大于零时，该模块
持续更新滤波器权重。当此端口的输入
小于或等于零时，滤波器权重保持其当前
值。

#### 依赖关系

此端口仅在您将 `Adapt port` 参数设置为
`on` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `Boolean`

### **Reset** — 重置滤波器权重 标量

用于将滤波器权重的值重置为其初始
值的信号，指定为标量。每当在 Reset 端口检测到重置事件时，该模块都会重置滤波器权重。重置信号
速率必须与数据信号输入的速率相同。

有关重置事件类型，请参阅 `Reset` 参数。

#### 依赖关系

此端口仅在您将 **Reset
port** 参数设置为 `Rising
edge`、`Falling edge`、
`Either edge` 或 `Non-zero
sample` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `Boolean`
### 输出

### **Output** — 期望信号的估计 标量 | 列向量

期望信号的估计，以标量或列
向量形式返回。其大小和复杂度与输入信号相同。

输出信号的数据类型与期望信号相同。

**数据类型：** `single` | `double` | `fixed point`

### **Error** — 输出信号与期望信号之间的误差 标量 | 列向量

输出信号与期望信号之间的误差，以标量或
列向量形式返回。此误差是将输出
信号从期望信号中减去的结果。

误差信号的数据类型与期望信号相同。

**数据类型：** `single` | `double` | `fixed point`

### **Wts** — 滤波器权重 标量 | 列向量

滤波器权重，以标量或列向量形式返回。对于每次
迭代，该模块从此端口输出当前更新后的滤波器权重。

对于浮点信号，权重的数据类型必须与 `Input`
端口的类型匹配。对于定点信号，遵循
`Weights` 参数。

#### 依赖关系

此端口仅在您将 `Output filter weights` 参数设置为
`On` 时出现。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Algorithm
  summary: 选择算法 LMS（默认）| Normalized LMS | Sign-Error LMS | Sign-Data LMS | Sign-Sign LMS
  group: 主选项卡
- name: Filter length
  summary: 滤波器长度 32（默认）| 标量
  group: 主选项卡
- name: Specify step size via
  summary: 通过以下方式指定步长 Dialog（默认）| Input port
  group: 主选项卡
- name: Step size (mu)
  summary: 步长 0.1（默认）| 正标量
  group: 主选项卡
- name: Leakage factor (0 to 1)
  summary: 泄漏因子 1.0（默认）| 标量
  group: 主选项卡
- name: Initial value of filter weights
  summary: 滤波器权重的初始值 0（默认）| 向量 | 标量
  group: 主选项卡
- name: Adapt port
  summary: 启用 Adapt 端口 off（默认）| on
  group: 主选项卡
- name: Reset port
  summary: 重置端口 None（默认）| Rising edge | Falling edge | Either edge | Non-zero sample
  group: 主选项卡
- name: Output filter weights
  summary: 输出滤波器权重 on（默认）| off
  group: 主选项卡
- name: Rounding mode
  summary: 舍入运算的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Parameters
  summary: 参数 Same word length as first input（默认）| Specify word length | Binary point scaling
  group: 数据类型选项卡
- name: Weights
  summary: 滤波器权重的字长和小数长度 Same as first input（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Product and quotient
  summary: 乘积和商的字长和小数长度 Same as first input（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Accumulator
  summary: 累加器的字长和小数长度 Same as first input（默认）| Binary point scaling
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Algorithm** — 选择算法 `LMS`（默认）| `Normalized LMS` | `Sign-Error LMS` | `Sign-Data LMS` | `Sign-Sign LMS`

选择用于计算滤波器权重的算法。

### **Filter length** — 滤波器长度 `32`（默认）| 标量

输入 FIR 滤波器权重向量的长度。

### **Specify step size via** — 通过以下方式指定步长 `Dialog`（默认）| `Input port`

- `Dialog` –– 通过
  使用 **Step size (mu)**
  参数指定步长。
- `Input port` –– 通过
  使用 `Step-size` 端口指定步长。

### **Step size (mu)** — 步长 `0.1`（默认）| 正标量

输入步长 *μ*。为使归一化 LMS 方程收敛，0<*µ*<2。

**可调：** 是

#### 依赖关系

此参数仅在您将 `Specify step size via` 参数设置为
`Dialog` 时出现。

### **Leakage factor (0 to 1)** — 泄漏因子 `1.0`（默认）| 标量

输入泄漏因子，0 < 1 – μα ≤ 1。

**可调：** 是

### **Initial value of filter weights** — 滤波器权重的初始值 `0`（默认）| 向量 | 标量

输入初始滤波器权重 **w**(0)
作为向量或标量。当您输入标量时，该模块使用该
标量值创建滤波器权重向量。此向量长度
等于滤波器长度，且其所有值都等于该标量
值。

### **Adapt port** — 启用 Adapt 端口 `off`（默认）| `on`

选中此复选框以启用 `Adapt` 输入端口。

### **Reset port** — 重置端口 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

当您想要将滤波器权重的值重置为其初始
值时，请使用 **Reset port** 参数。重置
信号必须与数据信号输入的速率相同。

选择 `None` 以禁用 `Reset` 端口。要启用 **Reset**
端口，请从列表中选择以下选项之一：

- `Rising edge` — 当 **Reset** 输入
  执行以下操作之一时触发
  重置操作：

  - 从负值上升到正值或
    零
  - 从零上升到正值，其中该上升
    不是从负值上升到
    零的延续（参见下图）

- `Falling edge` — 当 **Reset** 输入
  执行以下操作之一时触发
  重置操作：

  - 从正值下降到负值或
    零
  - 从零下降到负值，其中该下降
    不是从正值下降到
    零的延续（参见下图）
- `Either edge` — 当 **Reset** 输入为
  `Rising edge` 或
  `Falling edge` 时触发
  重置操作
- `Non-zero sample` — 在 Reset 输入不为
  零的每个采样时间触发
  重置操作

### **Output filter weights** — 输出滤波器权重 `on`（默认）| `off`

选择 **Output filter weights** 参数以
从 `Wts` 端口导出滤波器权重。对于每次迭代，该模块从此端口输出
当前更新后的滤波器权重。

### 数据类型选项卡

### **Rounding mode** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入
模式。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

当您选中此参数时，该模块会对其
定点运算的结果进行饱和处理。当您清除此参数时，该模块会
对其定点运算的结果进行回绕处理。有关
`saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出
模式。

### **Parameters** — 参数 `Same word length as first input`（默认）| `Specify word length` | `Binary point scaling`

选择如何指定泄漏因子和步长的字长和小数长度：

- `Same word length as first input` ––
  泄漏因子和步长的字长与
  模块的第一个输入匹配。在此模式下，泄漏因子和步长的小数
  长度会自动设置为仅二进制点缩放，从而在给定
  系数值和字长的情况下为您提供尽可能最佳的
  精度。
- `Specify word length` –– 您可以
  以位为单位输入泄漏因子和步长的字长。在此模式下，泄漏因子
  和步长的小数长度会自动设置为仅二进制点
  缩放，从而在给定
  系数值和字长的情况下为您提供尽可能最佳的
  精度。
- `Binary point scaling` –– 您可以
  以位为单位输入泄漏因子和步长的字长和小数长度。泄漏因子和步
  长必须具有相同的字长，但小数长度
  可以不同。

对于 `Specify
step size via` 参数，如果您选择 `Input
port`，则泄漏因子的字长与
`Step-size` 端口处步长输入的字长相同。泄漏因子
的小数长度会根据泄漏因子的
字长自动设置为尽可能最佳的精度。

#### 依赖关系

此参数仅在您将 **Specify
step size via** 参数设置为
`Dialog` 时可见

### **Weights** — 滤波器权重的字长和小数长度 `Same as first input`（默认）| `Binary point scaling`

选择如何指定模块滤波器权重的字长和小数长度：

- `Same as first input` –– 滤波器权重的字
  长和小数长度与模块的第一个输入匹配。
- `Binary point scaling` –– 您可以
  以位为单位输入滤波器权重的字长和小数长度。

### **Product and quotient** — 乘积和商的字长和小数长度 `Same as first input`（默认）| `Binary point scaling`

选择如何指定
**u'u**、**W'u**、μ⋅e、Q⋅u 以及商 Q 的字长和小数长度。这里，**u** 是输入向量，**W** 是滤波器权重向量，*μ*
是步长，*e* 是误差，
*Q* 是商，定义为 Q=μ⋅eu'u

- `Same as first input` –– 这些量的字
  长和小数长度与模块的第一个输入匹配。
- `Binary point scaling` –– 您可以
  以位为单位输入这些量的字长和小数长度。这些量的字长必须
  相同，但小数长度可以不同。

### **Accumulator** — 累加器的字长和小数长度 `Same as first input`（默认）| `Binary point scaling`

使用此参数指定您希望如何为 **u'u** 和 **W'u** 运算指定累加器的字长和
小数长度。

**注意**

请勿使用此参数为 Q⋅u 运算指定累加器的字长和小数
长度。此量的累加器数据类型会自动设置为
与乘积数据类型相同。此
累加器的最小值、最大值和溢出信息会作为乘积信息的一部分
记录。自动缩放将此乘积和累加器视为一种数据
类型。

- `Same as first input` –– 这些
  特性与模块的输入匹配。
- `Binary point scaling` –– 您可以
  以位为单位输入累加器的字长和小数长度。两个累加器的字长
  必须相同，但小数长度可以不同。

有关说明此模块中累加器数据类型使用的图示，请参阅定点数据类型和
乘法数据类型。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数以防止定点工具覆盖您在模块对话框中所指定的数据类型。
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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

**使用 Intel® AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

LMS Filter 模块在以下条件下支持使用
Intel AVX2 代码替换库生成 SIMD 代码：

- 您将 **Algorithm** 设置为
  `LMS` 或 `Normalized
  LMS`。
- 输入信号为实值。
- 输入信号的数据类型为 `single` 或
  `double`。

要使用此工作流从此模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

**通过
利用目标硬件指令集扩展生成 SIMD 代码** *(自 R2023b 起)*

**注意**

需要 Simulink®
Coder™ 或 Embedded Coder 许可证

您可以在所有
Intel 平台、ARM®
Cortex®-A 处理器和 Apple 芯片处理器上，通过使用模型配置参数
**Leverage target hardware instruction set extensions**，在
以下条件下为 LMS Filter 模块生成 SIMD 代码：

- 您将 **Algorithm** 设置为
  `Sign-Error LMS`、`Sign-Data
  LMS`、`Sign-Sign LMS`、
  `LMS` 或 `Normalized
  LMS`。
- 输入信号为实值且具有实滤波器系数
- 输入信号为复值且具有实或复滤波器
  系数。
- 输入信号的数据类型为 `single`
  （ARM
  Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或
  `double`（Intel 平台）

此外，请适当配置您的模型。在 Simulink 模型窗口的
**Modeling** 选项卡中，点击 **Model Settings**，并在 **Code Generation** 下配置
以下参数。

- 在 **Optimization** 窗格中：

  - 在
    **Leverage target hardware instruction set
    extensions** 参数中提供特定的指令集。
  - 选中 **Optimize reductions**
    参数。
  - 在 **Optimization levels** 下，将
    **Level** 设置为
    `Maximum`，并将
    **Priority** 设置为 `Maximize
    execution speed`。
- 在 **Interface** 窗格中，在 **Software
  environment** 下，清除 **non-finite
  numbers**。

要使用此工作流从此模块生成 SIMD 代码，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Intel Platforms、Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon 和 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for ARM Cortex-A Processors。

对于受支持模块上的计算密集型运算，SIMD 内建函数可以
显著提高生成代码在 Intel 平台上的性能。有关更多详细信息，请参阅 Optimize Code for Reduction Operations by Using SIMD (Simulink Coder)。

有关 DSP System Toolbox™ 中 SIMD 代码生成的更多信息，请参阅 SIMD Code Generation。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**注意**

对于具有硬件友好控制信号和 Simulink 中 HDL 延迟仿真的 LMS 滤波器，或者对于具有复系数的复数据，请使用 LMS Filter (DSP HDL Toolbox) 模块代替此模块。

**HDL 架构**

默认情况下，LMS Filter 实现使用线性求和作为滤波器的 FIR 部分。

LMS Filter 在以下条件下实现树形求和（具有更短的关键路径）：

- LMS Filter 与实数数据一起使用。
- 累加器 **W'u** 数据类型的字长至少比乘积 W'u 数据类型的字长宽 `ceil(log2(filter
  length))` 位。
- 累加器 **W'u** 数据类型与乘积 **W'u** 数据类型具有相同的小数长度。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

- HDL Coder 不支持 LMS Filter 的 `Normalized
  LMS` 算法。
- `Reset` 端口仅支持 `Boolean` 和 `unsigned` 输入。
- `Adapt` 端口仅支持 `Boolean` 输入。
- **Filter length** 必须大于或等于 2。

## 版本历史

**在 R2006a 之前引入**

### R2024b: 为 Apple silicon 处理器生成 SIMD 代码

在 R2024b 中，如果您拥有 Embedded Coder，您可以通过使用模型配置参数 **Leverage target hardware instruction set extensions** 为 Apple silicon 处理器生成 LMS Filter 模块的 SIMD 代码。有关更多信息，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon。

### R2023b: 为复数信号生成 SIMD 代码

在 R2023b 中，如果您拥有 Embedded Coder，当输入信号为复数值时，您可以通过使用模型配置参数 **Leverage target hardware instruction set extensions** 为 LMS Filter 模块生成 SIMD 代码。

## 描述

使用最小均方 (LMS) 自适应算法计算输出、误差和权重

LMS Filter 模块可以通过使用五种不同的算法来实现自适应 FIR 滤波器。该模块估计最小化输出信号 *y(n)* 与期望信号 *d(n)* 之间的误差 *e(n)* 所需的滤波器权重或系数。输出是滤波后的输入信号，即期望信号的估计值。Error 端口输出从期望信号中减去输出信号的结果。

在特定条件下，此模块还支持 SIMD 代码生成。有关详细信息，请参阅代码生成。
