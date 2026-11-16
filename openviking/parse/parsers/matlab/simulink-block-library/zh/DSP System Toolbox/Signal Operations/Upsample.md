---
type: simulink-block
title: 'Upsample'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'upsample'
documentation_source_path: '../dsp/ref/upsample.html'
language: zh-CN
chinese_source: worker-translation
---

# Upsample

## 端口

### 输入

### **in** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为实数或复数值的标量、向量或矩阵信号。

当将 **Input processing** 设置为 `Columns as channels (frame based)` 并将 **Rate options** 设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。当输入为可变大小信号时，信号的帧大小（行数）和通道数（列数）可以在仿真期间变化。

在将 **Upsample factor source** 设置为 `Input port` 之前，此端口未命名。*（自 R2023a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### **L** — 上采样因子 正整数 ≤ *Lmax*

*自 R2023a 起*

将上采样因子 *L* 指定为小于或等于 **Maximum upsample factor, Lmax** 参数中指定值的正整数。

#### 依赖关系

要启用此端口，请将 **Upsample factor source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 上采样信号 标量 | 向量 | 矩阵

Upsample 模块输出的信号与输入信号具有相同的数据类型和复数性。输出大小取决于上采样因子的值以及在 **Rate options** 参数中选择的选项。

如果将 **Upsample factor, L** 设置为 *L*，并将 **Rate options** 设置为：

- `Enforce single-rate processing` –– 模块通过将输出帧大小增大 *L* 倍来保持输入采样率。
- `Allow multirate processing` –– 模块对信号进行重采样，使输出采样率比输入采样率快 *L* 倍。输出信号与输入信号具有相同的帧大小。

当通过输入端口 **L** 输入上采样因子时，**Rate options** 参数会自动设置为 `Enforce single-rate processing`。在这种情况下，模块通过将输出帧大小增大 *L* 倍来在输出端保持输入采样率。*（自 R2023a 起）*

当满足以下一个或两个条件时，输出为可变大小信号：

- 输入为可变大小信号。
- 上采样因子通过端口 **L** 输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

### **Upsample factor source** — 指定上采样因子的模式 `Dialog parameter`（默认） | `Input port`

*自 R2023a 起*

通过以下选项之一指定上采样因子：

- `Dialog parameter` –– 模块在模块对话框中启用 **Upsample factor, L** 参数。
- `Input port` –– 模块启用输入端口 **L**，通过该端口可以指定上采样因子。

### **Upsample factor, L** — 上采样因子 `3`（默认） | 正整数

将用于提高输入采样率的上采样因子 *L* 指定为正整数。

#### 依赖关系

要启用此参数，请将 **Upsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

### **Sample offset (0 to L−1)** — 采样偏移 `0`（默认） | [0, *L*−1] 范围内的整数

将采样偏移 *D* 指定为 [0, *L*−1] 范围内的整数。

使用 **Sample offset (0 to L−1)** 参数将输出采样延迟特定数量的采样周期。这样做可以选择 *L* 个可能输出相位中的任意一个。在 **Sample offset (0 to L−1)** 参数中指定的值必须是范围 0≤D<(L−1) 内的整数。

当通过输入端口 **L** 输入上采样因子时，**Sample offset (0 to L−1)** 参数在模块对话框中未启用。在这种情况下，采样偏移 *D* 会自动设置为 0。*（自 R2023a 起）*

#### 依赖关系

要启用此参数，请将 **Upsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

### **Maximum upsample factor, Lmax** — 最大上采样因子 `16`（默认） | 正整数 ≥ 1

*自 R2023a 起*

将最大上采样因子 *Lmax* 指定为大于或等于 `1` 的正整数。通过输入端口 **L** 指定的上采样因子必须小于或等于 *Lmax*。

#### 依赖关系

要启用此参数，请将 **Upsample factor source** 设置为 `Input port`。

### **Input processing** — 处理输入信号的方法 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

指定模块应如何处理输入。可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)` — 选择此选项时，模块将输入的每一列视为单独通道。在此模式下，模块可以执行单速率或多速率处理。
- `Elements as channels (sample based)` — 选择此选项时，模块将输入的每个元素视为单独通道。在此模式下，模块始终执行多速率处理。

#### 依赖关系

要启用此参数，请将 **Upsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当将 **Upsample factor source** 设置为 `Input port` 时，**Input processing** 参数会自动设置为 `Columns as channels (frame based)`。*（自 R2023a 起）*

### **Rate options** — 对输入进行上采样的方法 `Enforce single-rate processing`（默认） | `Allow multirate processing`

指定模块用于对输入进行上采样的方法。可以选择以下选项之一：

- `Enforce single-rate processing` — 选择此选项时，模块通过将输出帧大小增大 *L* 倍来保持输入采样率。要选择此选项，必须将 **Input processing** 参数设置为 `Columns as channels (frame based)`。
- `Allow multirate processing` — 选择此选项时，模块对信号进行重采样，使输出采样率比输入采样率快 *L* 倍。

#### 依赖关系

要启用此参数，请将 **Upsample factor source** 设置为 `Dialog parameter`。*（自 R2023a 起）*

当将 **Upsample factor source** 设置为 `Input port` 时，**Rate options** 参数会自动设置为 `Enforce single-rate processing`。*（自 R2023a 起）*

### **Initial conditions** — 初始条件 `0`（默认） | 标量 | 向量 | 矩阵

将模块在非零延迟情况下初始化所使用的值指定为标量、向量或矩阵。标量值在输出中作为采样 *D*+1 出现。如果将此参数设置为向量或矩阵，则此参数的大小应与输入的大小相同。仅当将模块配置为执行多速率处理时，此参数才出现。

#### 依赖关系

要启用此参数，请将 **Rate options** 设置为 `Allow multirate processing`。

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

生成的代码在某些情况下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**最佳实践**

考虑模型是否可以使用 Repeat 模块代替 Upsample 模块。Repeat 模块使用更少的硬件资源，因此最佳实践是仅当算法需要零填充上采样时才使用 Upsample 模块。

另请参阅 Multirate Model Requirements for HDL Code Generation (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 不支持将 **Input processing** 设置为 `Columns as channels (frame based)`。
- 不支持将 **Upsample factor source** 设置为 `Input port`。

**复数数据支持**

此模块支持针对复信号进行代码生成。

## 版本历史

**R2006a 之前引入**

### R2025a：在 HDL 代码生成期间支持时钟速率流水线

从 R2025a 开始，当使用时钟速率流水线优化时，Upsample 模块不再充当该优化的障碍。因此，时钟速率流水线通过减少以前可能发生的大量延迟和不平衡延迟，更有效地优化多速率设计。例如，在以前的版本中，启用时钟速率流水线时，带有反馈环路的多速率设计可能会生成延迟平衡错误。在 R2025a 中，这些设计不会生成延迟平衡错误。

### R2023a：通过输入端口调整上采样因子

现在，当 Upsample 模块在单速率基于帧的处理模式下运行时，可以通过输入端口指定上采样因子。通过输入端口指定上采样因子时，可以在仿真期间更改该因子。

### R2022b：支持可变大小输入信号

从 R2022b 开始，当将 **Input processing** 设置为 `Columns as channels (frame based)` 并将 **Rate options** 设置为 `Enforce single-rate processing` 时，输入可以是可变大小信号。也就是说，信号的帧大小（行数）和通道数（列数）可以在仿真期间变化。

当输入为可变大小信号时，输出也是可变大小信号。

## 描述

通过插入零以更高率对输入进行重采样

Upsample 模块通过在连续采样之间插入 *L*−1 个零，以比输入采样率快 *L* 倍的速率对 *M*i-by-*N* 输入的每个通道进行重采样。在 **Upsample factor, L** 参数中或通过输入端口 **L** 指定整数 *L*。

当将 **Rate options** 参数设置为 `Enforce single-rate processing` 时，可以在触发子系统内使用此模块。
