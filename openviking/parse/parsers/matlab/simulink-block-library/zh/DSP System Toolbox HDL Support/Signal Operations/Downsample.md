---
type: simulink-block
title: 'Downsample'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'downsample'
documentation_source_path: '../dsp/ref/downsample.html'
language: zh-CN
chinese_source: worker-translation
---

# Downsample

## 端口

### 输入

### **in** — 数据输入 列向量 | 矩阵 | *N* 维数组

要降低采样率的输入数据，指定为列向量或矩阵。

当您将 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，输入可以是 *N* 维数组。

当您将 **Input processing** 设置为 `Columns as channels (frame based)` 并将 **Rate options** 设置为 `Enforce single-rate processing` 时，该模块支持可变大小输入信号，因此帧长度（行数）和通道数（列数）可以在仿真期间变化。当该模块接受可变大小输入信号时，这些信号可以具有任意帧长度，也就是说，输入帧长度不必是下采样因子的倍数。当您指定固定大小信号时，帧长度在某些条件下可以是任意的。有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

在您将 **Downsample factor source** 设置为 `Input port` 之前，此端口未命名。*（自 R2023a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **M** — 下采样因子 positive integer

*自 R2023a 起*

将下采样因子 *M* 指定为正整数。

#### 依赖关系

要启用此端口，请将 **Downsample factor source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 下采样输出 列向量 | 矩阵

下采样输出，其采样率为输入采样率的 1/*M*，以列向量或矩阵形式返回。

当您将 **Rate options** 设置为：

- `Enforce single-rate processing` —— 该模块保持输入采样率，并通过将输出帧大小除以 *M* 来对信号进行下采样。

  对于大小为 *P*×*Q* 的输入，输出大小上限为 `ceil`(*P*/*M*)×*Q*。
- `Allow multirate processing` —— 该模块对信号进行下采样，使输出采样率比输入采样率慢 *M* 倍。

  输出帧大小与输入帧大小相同。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

当满足以下任一条件时，输出为可变大小信号：

- 输入是可变大小信号。
- 输入是固定大小信号，并且已选中 **Allow arbitrary frame length for fixed-size input signals** 参数。
- 下采样因子通过端口 **M** 输入 *（自 R2023a 起）*

当输出为可变大小信号时，该模块在连续数据帧之间保持相位。有关更多详细信息，请参阅相位连续性。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

### **Downsample factor source** — 下采样因子来源 `Dialog parameter`（默认）| `Input port`

*自 R2023a 起*

通过以下选项之一指定下采样因子：

- `Dialog parameter` —— 该模块在模块对话框中启用 **Downsample factor, M** 参数。
- `Input port` —— 该模块启用输入端口 **M**，您可以通过该端口指定下采样因子。

### **Downsample factor, M** — 下采样因子 `2`（默认）| positive integer

指定用于降低输入采样率的整数因子 *M*。

#### 依赖关系

要启用此参数，请将 **Downsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

### **Sample offset (0 to M−1)** — 采样偏移 `0`（默认）| integer

**Sample offset (0 to M−1)** 参数将输出采样延迟整数个采样周期 *D*，其中 0 ≤ *D* ≤ (*M*–1)，因此您可以选择 *M* 个可能的输出相位中的任意一个。例如，当您以因子 4 对序列 1, 2, 3, ... 进行下采样时，可以从四个相位中进行选择。

| 输入序列 | Sample Offset, *D* | 输出序列 (*M* = 4) |
| --- | --- | --- |
| `1,2,3,...` | 0 | `1,5,9,13,17,21,25,29,...` |
| `1,2,3,...` | 1 | `0,2,6,10,14,18,22,26,...` |
| `1,2,3,...` | 2 | `0,3,7,11,15,19,23,27,...` |
| `1,2,3,...` | 3 | `0,4,8,12,16,20,24,28,...` |

表中最后三个输出序列开头的零是由于 **Initial conditions** 参数设置为其默认值 0 所致。有关 **Initial conditions** 参数的更多信息，请参阅延迟。

当您通过输入端口 **M** 输入下采样因子时，**Sample offset (0 to M−1)** 参数在模块对话框中不可启用。在这种情况下，采样偏移 *D* 自动设置为 0。*（自 R2023a 起）*

#### 依赖关系

要启用此参数，请将 **Downsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

### **Input processing** — 处理输入的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定输入处理方法：

- `Columns as channels (frame based)` —— 当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，该模块将 *Q* 个输入列中的每一列视为一个单独通道，其中包含 *Pi* 个连续时间采样。该模块通过丢弃在其输出的每一行之后的 *M*–1 行输入矩阵，独立地对每个通道进行下采样。

  有关更多信息，请参阅什么是基于帧的处理？。
- `Elements as channels (sample based)` —— 当您将 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，输入可以是 *Q* 维数组。Downsample 模块将输入的每个元素视为单独通道，并随时间对输入的每个通道重新采样。该模块通过丢弃其传递到输出的每个采样之后的 *M*–1 个采样，对输入数组进行下采样。Downsample 模块的输入和输出大小相同。

  有关更多信息，请参阅什么是基于采样的处理？。

#### 依赖关系

要启用此参数，请将 **Downsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将 **Downsample factor source** 设置为 `Input port` 时，**Input processing** 参数会自动设置为 `Columns as channels (frame based)`。*（自 R2023a 起）*

### **Rate options** — 强制单速率或允许多速率处理 `Enforce single-rate processing`（默认）| `Allow multirate processing`

指定该模块调整输出端口速率以适配减少的采样数的方法。该模块执行单速率还是多速率处理，取决于您将 **Input processing** 参数设置为 `Elements as channels (sample based)`（基于采样的处理模式）还是 `Columns as channels (frame based)`（基于帧的处理模式）。

- `Elements as channels (sample based)`

  - `Enforce single-rate processing`

    该模块通过在输出端将每第 *M* 个输入采样重复 *M* 次，强制输出采样率与输入采样率匹配（*Tso* = *Tsi*）。在此模式下，该模块的行为类似于 Sample and Hold 模块，其重复触发事件的周期为 *MTsi*。
  - `Allow multirate processing`

    输出的采样周期比输入采样周期长 *M* 倍（*Tso* = *MTsi*）。

  有关更多详细信息，请参阅基于采样的处理。
- `Columns as channels (frame based)`

  - `Enforce single rate processing`

    该模块使用比输入按比例更小的帧 *大小*，以较慢的（下采样）速率生成输出。输出的大小上限为 `ceil`(*P*/*M*)，其中 *P* 是输入帧长度，*M* 是下采样因子。输入和输出帧速率相等。有关更多详细信息，请参阅基于帧的处理。有关示例，请参阅 Downsample Signal in Single-Rate Frame-Based Processing Mode。
  - `Allow multirate processing`

    该模块通过使用输出端口处比输入端口处按比例更长的帧 *周期*，以较慢的（下采样）速率生成输出。对于按因子 *M* 进行下采样，输出帧周期比输入帧周期长 *M* 倍（*Tfo* = *MTfi*），但输入和输出帧大小相等。有关更多详细信息，请参阅基于帧的处理。有关示例，请参阅 Downsample Signal In Multirate Frame-Based Processing Mode。

#### 依赖关系

要启用此参数，请将 **Downsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将 **Downsample factor source** 设置为 `Input port` 时，**Rate options** 参数会自动设置为 `Enforce single-rate processing`。*（自 R2023a 起）*

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号使用任意帧长度 on（默认）| off

指定固定大小输入信号（大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是下采样因子的倍数。该模块仅对固定大小输入信号使用此参数设置，如果输入大小可变，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，也就是说，帧长度不必是抽取因子的倍数。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是下采样因子的倍数。如果输入不是下采样因子的倍数，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小运算，您可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该功能。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是下采样因子的倍数。

#### 依赖关系

要启用此参数，请设置：

- **Downsample factor source** 为 `Dialog parameter`。*（自 R2023a 起）*
- **Input processing** 为 `Columns as channels (frame based)`。
- **Rate options** 为 `Enforce single-rate processing`。

### **Initial conditions** — 初始值 `0`（默认）| real scalar | array

用于非零延迟情况的初始模块值。您可以指定标量或与输入大小相同的数组。

#### 依赖关系

当 **Input processing** 设置为 `Columns as channels (frame based)` 并且 **Rate options** 设置为 `Enforce single-rate processing` 时，此参数不显示。

## 所属库

DSP System Toolbox / Signal Operations DSP System Toolbox HDL Support / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了会影响 HDL 实现和综合逻辑的附加配置选项。

**最佳实践**

最佳实践是在 Downsample 模块之后接一个单位延迟。这样做可以防止代码生成器在 HDL 代码中插入额外的旁路寄存器。

另请参阅 Multirate Model Requirements for HDL Code Generation (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

**限制**

- 不支持将 **Input processing** 设置为 `Columns as channels (frame based)`。
- 对于将 **Input processing** 设置为 `Elements as channels (sample based)` 的情况，请选择 `Allow multirate processing`。使用此设置时，如果 **Sample offset** 设置为 0，则 **Initial conditions** 对生成的代码没有影响。

## 版本历史

**R2006a 之前引入**

### R2023a：通过输入端口调整下采样因子

现在，当 Downsample 模块在单速率基于帧的处理模式下运行时，您可以通过输入端口指定下采样因子。当您通过输入端口指定下采样因子时，可以在仿真期间更改该因子。

### R2022b：支持任意输入帧长度和可变输入帧大小

从 R2022b 开始，此模块在以下情况下支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（信号维度在仿真期间不变），并且该模块允许多速率处理
- 输入信号是固定大小信号，该模块强制单速率处理，并且您选中 **Allow arbitrary frame length for fixed-size input signals** 参数（如果启用）
- 输入信号是可变大小信号（信号维度在仿真期间变化）

当此模块支持任意帧长度输入信号时，输入帧长度不必是下采样因子的倍数。

有关更多详细信息，请参阅基于帧的处理和基于采样的处理。

## 描述

通过删除采样以较低速率对输入重新采样

Downsample 模块通过删除采样来降低输入的采样率。当该模块执行基于帧的处理时，它会独立地对 *Pi*×*Q* 输入矩阵的每一列中的数据进行重新采样。当该模块执行基于采样的处理时，它会将输入的每个元素视为单独通道，并随时间对输入数组的每个通道进行重新采样。重新采样率比输入采样率低 *M* 倍，其中 *M* 是下采样因子的值。Downsample 模块通过丢弃在输出的每个采样之后的 *M*–1 个连续采样来对输入进行重新采样。

当您将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，此模块支持触发子系统。
