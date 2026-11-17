---
type: simulink-block
title: 'Repeat'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'repeat'
documentation_source_path: 'ref/repeat.html'
language: zh-CN
chinese_source: worker-translation
---

# Repeat

## 端口
```yaml
ports:
- name: in
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: L
  summary: 重复次数 正整数 ≤ *Lmax*
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **in** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为实数或复数值的标量、向量或矩阵。

当您将 **Input processing** 设置为 `Columns as channels (frame based)`，并将 **Rate options** 设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。当输入为可变大小信号时，信号的帧大小（行数）和通道数（列数）可以在仿真期间发生变化。

在您将 **Repetition count source** 设置为 `Input port` 之前，此端口是未命名的。*（自 R2023a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **L** — 重复次数 正整数 ≤ *Lmax*

*自 R2023a 起*

将重复次数 *L* 指定为小于或等于您在 **Maximum repetition count, Lmax** 参数 *Lmax* 中指定的值的正整数。

#### 依赖关系

要启用此端口，请将 **Repetition count source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

Repeat 模块输出的信号具有与输入信号 **in** 相同的数据类型和复数性。输出的大小取决于重复次数的值以及您在 **Rate options** 参数中选择的选项。

如果您将 **Repetition count, L** 设置为 *L*，并将 **Rate options** 设置为：

- `Enforce single-rate processing` —— 该模块通过将输出帧大小增加 *L* 倍来保持输入采样率。
- `Allow multirate processing` —— 该模块对信号进行重采样，使得输出采样率比输入采样率快 *L* 倍。输出信号具有与输入信号相同的帧大小。

当您通过输入端口 **L** 输入重复次数时，**Rate options** 参数会自动设置为 `Enforce single-rate processing`。在这种情况下，该模块通过将输出帧大小增加 *L* 倍来在输出端保持输入采样率。*（自 R2023a 起）*

当满足以下一个或两个条件时，输出为可变大小信号：

- 输入为可变大小信号。
- 重复次数通过端口 **L** 输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Repetition count source
  summary: 指定重复次数的模式 Dialog parameter（默认）| Input port
  group: ''
- name: Repetition count, L
  summary: 重复次数 5（默认）| 正整数
  group: ''
- name: Maximum repetition factor, Lmax
  summary: 最大重复次数 16（默认）| 正整数 ≥ 1
  group: ''
- name: Input processing
  summary: 处理输入信号的方法 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
- name: Rate options
  summary: 模块对输入进行上采样的方法 Enforce single-rate processing（默认）| Allow multirate processing
  group: ''
- name: Initial conditions
  summary: 初始条件 0（默认）| 标量 | 矩阵
  group: ''
```

### **Repetition count source** — 指定重复次数的模式 `Dialog parameter`（默认）| `Input port`

*自 R2023a 起*

通过以下选项之一指定重复次数：

- `Dialog parameter` —— 该模块在模块对话框中启用 **Repetition count, L** 参数。
- `Input port` —— 该模块启用输入端口 **L**，您可以通过该端口指定重复次数。

### **Repetition count, L** — 重复次数 `5`（默认）| 正整数

将重复次数 *L* 指定为正整数。此值是模块重复输入值的次数。这是模块增加输出帧大小或采样率的因子。

#### 依赖关系

要启用此参数，请将 **Repetition count source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

### **Maximum repetition factor, Lmax** — 最大重复次数 `16`（默认）| 正整数 ≥ 1

*自 R2023a 起*

将最大重复次数 *Lmax* 指定为大于或等于 `1` 的正整数。您通过输入端口 **L** 指定的重复次数必须小于或等于 *Lmax*。

#### 依赖关系

要启用此参数，请将 **Repetition count source** 设置为 `Input port`。

### **Input processing** — 处理输入信号的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

通过将此参数设置为以下选项之一来指定模块应如何处理输入：

- `Columns as channels (frame based)` —— 当您选择此选项时，模块将输入的每一列视为单独的通道。在此模式下，模块可以执行单速率或多速率处理。
- `Elements as channels (sample based)` —— 当您选择此选项时，模块将输入的每个元素视为单独的通道。在此模式下，模块始终执行多速率处理。

#### 依赖关系

要启用此参数，请将 **Repetition count source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将 **Repetition count source** 设置为 `Input port` 时，**Input processing** 参数会自动设置为 `Columns as channels (frame based)`。*（自 R2023a 起）*

### **Rate options** — 模块对输入进行上采样的方法 `Enforce single-rate processing`（默认）| `Allow multirate processing`

通过选择以下选项之一来指定模块对输入进行上采样的方法：

- `Enforce single-rate processing` —— 当您选择此选项时，模块通过将输出帧大小增加 *L* 倍来保持输入采样率。要选择此选项，您必须将 **Input processing** 参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` —— 当您选择此选项时，模块对信号进行重采样，使得输出采样率比输入采样率快 *L* 倍。

#### 依赖关系

要启用此参数，请将 **Repetition count source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当您将 **Repetition count source** 设置为 `Input port` 时，**Rate options** 参数会自动设置为 `Enforce single-rate processing`。*（自 R2023a 起）*

### **Initial conditions** — 初始条件 `0`（默认）| 标量 | 矩阵

将模块在非零延迟情况下初始化时使用的值指定为标量或矩阵。

#### 依赖关系

要启用此参数，请将 **Rate options** 设置为 `Allow multirate processing`。
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

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**最佳实践**

Repeat 模块使用的硬件资源比 Upsample 模块少。如果您的算法不需要零填充上采样，请使用 Repeat 模块。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不支持将 **Input processing** 设置为 `Columns as channels (frame based)`。

## 版本历史

**在 R2006a 之前推出**

### R2023a：通过输入端口调整重复次数

当 Repeat 模块在单速率基于帧的处理模式下运行时，您现在可以通过输入端口指定重复次数。当您通过输入端口指定重复次数时，您可以在仿真期间更改该值。

### R2022b：支持可变大小输入信号

从 R2022b 开始，当您将 **Input processing** 设置为 `Columns as channels (frame based)`，并将 **Rate options** 设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。也就是说，信号的帧大小（行数）和通道数（列数）可以在仿真期间发生变化。

当输入为可变大小信号时，输出也是可变大小信号。

## 描述

通过重复值以更高采样率对输入进行重采样

Repeat 模块将 *M*i×*N* 输入的每个通道上采样到比输入采样率快 *L* 倍的速率。为此，该模块在输出端将每个连续输入样本重复 *L* 次。在 **Repetition count, L** 参数中或通过输入端口 **L** 指定整数 *L*。

当您将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，您可以在触发子系统（triggered subsystems）中使用 Repeat 模块。
