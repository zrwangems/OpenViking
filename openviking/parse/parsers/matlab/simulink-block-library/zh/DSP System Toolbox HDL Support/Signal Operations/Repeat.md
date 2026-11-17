---
type: simulink-block
title: 'Repeat'
family: 'signal-operations'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'repeat'
documentation_source_path: '../dsp/ref/repeat.html'
language: zh-CN
chinese_source: worker-translation
---

# Repeat

## 端口

### 输入

### **in** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为实数或复数值标量、向量或矩阵。

当您将**输入处理**设置为 `Columns as channels (frame based)`，并将**速率选项**设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。当输入为可变大小信号时，信号的帧大小（行数）和通道数（列数）可以在仿真期间变化。

此端口在您将**重复计数源**设置为 `Input port` 之前未命名。*（自 R2023a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **L** — 重复计数 正整数 ≤ *Lmax*

*自 R2023a 起*

将重复计数 *L* 指定为小于或等于您在**最大重复计数, Lmax**参数 *Lmax* 中指定的值的正整数。

#### 依赖关系

要启用此端口，请将**重复计数源**参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

Repeat 模块输出一个信号，其数据类型和复/实性与输入信号 **in** 相同。输出的大小取决于重复计数的值以及您在**速率选项**参数中选择的选项。

如果您将**重复计数, L**设置为 *L*，并将**速率选项**设置为：

- `Enforce single-rate processing` –– 模块通过将输出帧大小增加 *L* 倍来保持输入采样率。
- `Allow multirate processing` –– 模块对信号进行重采样，使输出采样率比输入采样率快 *L* 倍。输出信号与输入信号具有相同的帧大小。

当您通过输入端口 **L** 输入重复计数时，**速率选项**参数会自动设置为 `Enforce single-rate processing`。在这种情况下，模块通过将输出帧大小增加 *L* 倍，在输出端保持输入采样率。*（自 R2023a 起）*

当满足以下一个或两个条件时，输出为可变大小信号：

- 输入为可变大小信号。
- 重复计数通过端口 **L** 输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

## 参数

### **重复计数源** — 指定重复计数的模式 `Dialog parameter`（默认） | `Input port`

*自 R2023a 起*

通过以下选项之一指定重复计数：

- `Dialog parameter` –– 模块在模块对话框中启用 **重复计数, L** 参数。
- `Input port` –– 模块启用输入端口 **L**，您通过该端口指定重复计数。

### **重复计数, L** — 重复计数 `5`（默认） | 正整数

将重复计数 *L* 指定为正整数。此值是模块重复输入值的次数。这是模块增加输出帧大小或采样率的因子。

#### 依赖关系

要启用此参数，请将**重复计数源**设置为 `Dialog parameter`。*（自 R2023a 起）*

### **最大重复因子, Lmax** — 最大重复计数 `16`（默认） | 正整数 ≥ 1

*自 R2023a 起*

将最大重复 *Lmax* 指定为大于或等于 `1` 的正整数。您通过输入端口 **L** 指定的重复计数必须小于或等于 *Lmax*。

#### 依赖关系

要启用此参数，请将**重复计数源**设置为 `Input port`。

### **输入处理** — 处理输入信号的方法 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

通过将此参数设置为以下选项之一，指定模块应如何处理输入：

- `Columns as channels (frame based)` — 选择此选项时，模块将输入的每一列视为单独的通道。在此模式下，模块可以执行单速率或多速率处理。
- `Elements as channels (sample based)` — 选择此选项时，模块将输入的每个元素视为单独的通道。在此模式下，模块始终执行多速率处理。

#### 依赖关系

要启用此参数，请将**重复计数源**设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将**重复计数源**设置为 `Input port` 时，**输入处理**参数会自动设置为 `Columns as channels (frame based)`。*（自 R2023a 起）*

### **速率选项** — 模块对输入进行上采样的方法 `Enforce single-rate processing`（默认） | `Allow multirate processing`

通过选择以下选项之一，指定模块对输入进行上采样的方法：

- `Enforce single-rate processing` — 选择此选项时，模块通过将输出帧大小增加 *L* 倍来保持输入采样率。要选择此选项，您必须将**输入处理**参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` — 选择此选项时，模块对信号进行重采样，使输出采样率比输入采样率快 *L* 倍。

#### 依赖关系

要启用此参数，请将**重复计数源**设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将**重复计数源**设置为 `Input port` 时，**速率选项**参数会自动设置为 `Enforce single-rate processing`。*（自 R2023a 起）*

### **初始条件** — 初始条件 `0`（默认） | 标量 | 矩阵

对于非零延迟的情况，将模块初始化值指定为标量或矩阵。

#### 依赖关系

要启用此参数，请将**速率选项**设置为 `Allow multirate processing`。

## 所属库

DSP System Toolbox / Signal Operations Communications Toolbox / Sequence Operations DSP System Toolbox HDL Support / Signal Operations

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**最佳实践**

与 Upsample 模块相比，Repeat 模块使用更少的硬件资源。如果您的算法不需要补零上采样，请使用 Repeat 模块。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不支持将**输入处理**设置为 `Columns as channels (frame based)`。

## 版本历史

**R2006a 之前引入**

### R2023a：通过输入端口调整重复计数

现在，当 Repeat 模块在单速率基于帧的处理模式下运行时，您可以通过输入端口指定重复计数。当您通过输入端口指定重复计数时，可以在仿真期间更改该值。

### R2022b：支持可变大小输入信号

从 R2022b 开始，当您将**输入处理**设置为 `Columns as channels (frame based)`，并将**速率选项**设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。也就是说，信号的帧大小（行数）和通道数（列数）可以在仿真期间变化。

当输入为可变大小信号时，输出也是可变大小信号。

## 描述

通过重复值以更高采样率对输入进行重采样

Repeat 模块将 *M*i-by-*N* 输入的每个通道上采样到比输入采样率高 *L* 倍的速率。为此，模块在输出端将每个连续输入样本重复 *L* 次。在**重复计数, L**参数中或通过输入端口 **L** 指定整数 *L*。

当您将**速率选项**参数设置为 `Enforce single-rate processing` 时，可以在触发子系统中使用 Repeat 模块。
