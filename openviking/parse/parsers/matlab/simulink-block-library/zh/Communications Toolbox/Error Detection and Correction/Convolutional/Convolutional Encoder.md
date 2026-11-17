---
type: simulink-block
title: 'Convolutional Encoder'
family: 'error-detection-and-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'convolutionalencoder'
documentation_source_path: 'ref/convolutionalencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolutional Encoder

## 端口

### 输入

### **In** — 输入消息二进制列向量

输入消息，指定为二进制列向量。在启用第二个输入端口之前，此端口未命名。如果编码器接受 *K* 个输入比特流（即，它可以接收 2*K* 个可能的输入符号），则对于某个正整数 *L*，模块输入向量长度为 *L*×*K*。

**示例：** `[1 1 0 1 0 0 1 1]` 将消息指定为具有八个元素的二进制行向量。

**数据类型：** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufix1`

### **ISt** — 编码器寄存器的初始状态 非负整数

每个输入到模块的帧的编码器寄存器的初始状态，指定为非负整数。

#### 依赖项

要启用此端口，请将 **操作模式** 参数设置为 `Truncated (reset every frame)`，并选择 **通过输入端口指定初始状态**。

**数据类型：** `double` | `uint32`

### **Rst** — 编码器寄存器的复位状态 `scalar`

编码器寄存器的复位状态，指定为标量值。任何非零值都会强制复位编码器寄存器。

#### 依赖项

要启用此端口，请将 **操作模式** 参数设置为 `Reset on nonzero input via port`。

**数据类型：** `double` | `Boolean`

### 输出

### **Out** — 卷积编码后的码字二进制列向量

卷积编码后的码字，返回为二进制列向量。此端口在模块图标上未命名。如果编码器产生 *N* 个输出比特流（即，它可以产生 2*N* 个可能的输出符号），则对于某个正整数 *L*，模块输出向量长度为 *L*×*N*。此输出从其 `In` 输入继承数据类型。

**数据类型：** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufix1`

### **FSt** — 编码器寄存器的最终状态 非负整数

每个从模块输出的帧的编码器寄存器的最终状态，返回为非负整数。

#### 依赖项

仅当您将 **操作模式** 参数设置为 `Continuous`、`Truncated (reset every frame)` 或 `Reset on nonzero input via port`，并且选择 **输出最终状态** 参数时，此端口才显示。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用 **属性检查器**。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **网格结构** — 卷积码的网格描述 `poly2trellis(7, [171 133])` (default)

卷积码的网格描述，指定为包含速率 *K* ∕ *N* 码的网格描述的结构。*K* 是输入比特流的数量，*N* 是输出比特流的数量。

您可以使用 `poly2trellis` 函数创建网格结构，也可以手动创建。有关此结构的更多信息，请参阅卷积码的网格描述和 `istrellis` 函数。

网格结构包含以下字段。

### **numInputSymbols** — 输入到编码器的符号数 2*K*

输入到编码器的符号数，指定为等于 2*K* 的整数，其中 *K* 是输入比特流的数量。

### **numOutputSymbols** — 从编码器输出的符号数 2*N*

从编码器输出的符号数，指定为等于 2*N* 的整数，其中 *N* 是输出比特流的数量。

### **numStates** — 编码器中的状态数 2 的幂

编码器中的状态数，指定为 2 的幂。

### **nextStates** — 下一状态整数矩阵

所有当前状态和当前输入组合的下一状态，指定为整数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **outputs** — 八进制数输出矩阵

所有当前状态和当前输入组合的输出，指定为八进制数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **操作模式** — 编码帧的终止方法 `Continuous` (default) | `Truncated (reset every frame)` | `Terminate trellis by appending bits` | `Reset on nonzero input via port`

编码帧的终止方法，指定为以下模式值之一。

- `Continuous` — 模块在每个输入结束时保留编码器状态，以供下一帧使用。
- `Truncated (reset every frame)` — 模块独立处理每个输入。在每个输入帧开始时，编码器状态重置为全零状态；如果选择 **通过输入端口指定初始状态**，则重置为 `ISt` 端口指定的状态。
- `Terminate trellis by appending bits` — 模块独立处理每个输入。对于每个输入帧，使用额外比特在帧结束时将编码器状态设置为全零状态。输出长度由 y = N × (x + s) / K 给出，其中 *x* 是输入比特数，s = constraint length – 1（或者，在多个约束长度的情况下，s = sum(constraint length(i) – 1)）。

  **注意**

  此模块适用于 K ≥ 1 的情况，其中每个输入流中的约束长度具有相同值。例如，约束长度 [2 2] 或 [7 7] 可行，但 [5 4] 不可行。
- `Reset on nonzero input via port` — 模块有一个额外输入端口，标记为 `Rst`。当 `Rst` 输入非零时，编码器复位到全零状态。

**注意**

当此模块在仿真期间输出长度变化的序列，并且您将 **操作模式** 设置为 `Truncated (reset every frame)` 或 `Terminate trellis by appending bits` 时，模块的状态在每个输入时间步重置。

### **将复位操作延迟到下一时间步** — 将复位操作延迟到下一时间步的选项 `off` (default) | `on`

选择此参数以在计算编码数据后复位模块。复位操作中的延迟允许模块支持 HDL 代码生成。生成 HDL 代码需要 HDL Coder™ 软件。

#### 依赖项

仅当您将 **操作模式** 参数设置为 `Reset on nonzero input via port` 时，此参数才显示。

### **通过输入端口指定初始状态** — 通过输入端口指定初始状态的选项 `off` (default) | `on`

选择此参数以将 `ISt` 输入端口添加到模块。

#### 依赖项

仅当您将 **操作模式** 参数设置为 `Truncated (reset every frame)` 时，此参数才显示。

### **输出最终状态** — 输出最终寄存器状态的选项 `off` (default) | `on`

选择此参数以将 `FSt` 输出端口添加到模块。

#### 依赖项

仅当您将 **操作模式** 参数设置为 `Continuous`、`Truncated (reset every frame)` 或 `Reset on nonzero input via port` 时，此参数才显示。

### **删余码** — 启用码删余的选项 `off` (default) | `on`

选择此参数以查看并启用 **删余向量** 参数。

### **删余向量** — 删余模式 `[1; 1; 0; 1; 0; 1]` (default) | vector

删余模式，指定为向量。删余向量是由 `1` 和 `0` 组成的模式，其中 `0` 表示输出编码数据中被删余的比特。向量长度必须是 `length(In)`（输入消息向量长度）的整数除数。

有关特定速率和多项式的一些常用删余模式，请参阅 Yasuda [3]、Haccoun [4] 和 Begin [5] 参考文献。

#### 依赖项

仅当您选择 **删余码** 参数时，此参数才显示。

## 所属库

Communications Toolbox / Error Detection and Correction / Convolutional Communications Toolbox HDL Support / Error Detection and Correction / Convolutional

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

对于具有硬件友好控制信号的 HDL 优化卷积编码器，请使用 Convolutional Encoder (Wireless HDL Toolbox) 模块。Wireless HDL Toolbox™ 模块还在 Simulink 中仿真 HDL 算法的延迟。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 输入数据要求：

  - 必须为标量输入
  - 必须具有 `boolean` 或 `ufix1` 数据类型
- HDL Coder 仅支持以下编码速率：

  - ½ 到 1/7
  - 2/3
- HDL Coder 仅支持 3 到 9 的约束长度。
- 通过 `poly2trellis` 函数指定 **网格结构**。
- HDL Coder 支持以下 **操作模式** 设置：

  - `Continuous`
  - `Reset on nonzero input via port`

    如果选择此模式，则必须选择 **将复位操作延迟到下一时间步** 选项。当您选择此选项时，Convolutional Encoder 模块在执行复位之前完成其当前计算。
- 无法在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**早于 R2006a 引入**

## 描述

使用卷积编码方案对二进制数据进行编码

Convolutional Encoder 模块使用由网格结构指定的卷积编码方案对输入二进制消息进行编码。有关更多信息，请参阅卷积编码。

此模块可以接受在仿真期间长度变化的输入。有关可变大小信号的更多信息，请参阅可变大小信号基础知识 (Simulink) 主题。

这些图标显示已启用的可选模块端口。

启用了可选初始状态和最终状态端口的 Convolutional Encoder 模块

启用了可选复位和最终状态端口的 Convolutional Encoder 模块
