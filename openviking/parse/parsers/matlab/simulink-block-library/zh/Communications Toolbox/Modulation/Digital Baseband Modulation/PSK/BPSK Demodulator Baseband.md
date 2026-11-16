---
type: simulink-block
title: 'BPSK Demodulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'bpskdemodulatorbaseband'
documentation_source_path: '../comm/ref/bpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# BPSK Demodulator Baseband

## 端口

### 输入

### **In** — BPSK 调制基带信号 标量 | 向量 | 矩阵

BPSK 调制基带信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列被视为独立通道。在启用 `Var` 端口之前，此端口未命名。当噪声方差或信号功率导致涉及极大正值或负值的计算时，请参阅 BPSK 软解调以了解解调判决类型注意事项。

**数据类型：** `double` | `single` | `fixed point`
**复数支持：** Yes

### **Var** — 噪声方差 正标量 | 正数值向量

噪声方差，指定为正标量或正数值向量。当噪声方差或信号功率导致涉及极大正值或负值的计算时，请参阅 BPSK 软解调以了解解调判决类型注意事项。

#### 依赖项

要启用此参数，请将 **噪声方差源** 参数设置为 `Port`。

**数据类型：** `double`
### 输出

### **Out** — 解调信号 标量 | 向量

解调信号，以标量或向量形式返回。如果输出为标量，则该值为整数。如果输出为向量，则其为整数值或二值向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要交互式编辑模块参数，请使用属性检查器。从 Simulink® 工具条，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### 主要

### **判决类型** — 判决类型 `Hard decision` (默认) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

判决类型，用于解调，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关更多信息，请参阅 BPSK 硬判决解调和 BPSK 软解调。

当 **判决类型** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，输出与输入值的数据类型匹配。

### **噪声方差源** — 噪声方差源 `Dialog` (默认) | `Port`

噪声方差源，指定为 `Dialog` 或 `Port`。

- `Dialog` — 使用 `Noise variance` 参数设置噪声方差。
- `Port` — 使用 `Var` 输入端口设置噪声方差。

### **噪声方差** — 噪声方差 `1` (默认) | 正标量 | 正数值向量

噪声方差，指定为正标量或正数值向量。

- 当指定为标量时，该值用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号的列数。每个噪声方差向量元素应用于输入信号中其对应的列。

当噪声方差或信号功率导致涉及极大正值或负值的计算时，请参阅 BPSK 软解调以了解解调判决类型注意事项。

此参数在普通模式、加速模式和快速加速模式中可调。如果您使用 Simulink Coder™ 快速仿真 (RSIM) 目标构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。这对于蒙特卡洛仿真很有用，在这些仿真中，您使用不同的噪声量多次运行仿真（可能是在多台计算机上）。

**可调：** Yes

#### 依赖项

要启用此参数，请将 `Decision type` 参数设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio`，并将 **噪声方差源** 参数设置为 `Dialog`。

### **相位偏移 (rad)** — 第零点的相位 `0` (默认) | 实数值标量

第零点的相位，指定为实数值标量。单位为弧度。

**示例：** `pi/4`

### 数据类型

### **输出数据类型** — 输出数据类型 `Inherit via internal rule` (默认) | `Smallest unsigned integer` | `double` | `single` | ...

输出数据类型，指定为以下选项之一

- 当您将 **判决类型** 参数设置为 **Hard decision** 时：

  - `Inherit via internal rule` — 模块从输入端口继承输出数据类型。如果输入是浮点类型（`single` 或 `double`），则输出数据类型与输入数据类型相同。如果输入数据类型是定点，则输出数据类型的行为就像您将此参数设置为 `Smallest unsigned integer` 一样。
  - `Smallest unsigned integer` — 模块根据模型的配置参数对话框的 **硬件实现** 窗格中使用的设置选择输出数据类型。如果您在 **硬件实现** 窗格中选择 `ASIC/FPGA`，则输出数据类型是理想的最小一位大小，即 `ufix(1)`。对于所有其他选择，输出数据类型是可用字长最小且足以容纳一位的无符号整数，通常对应于一个字符的大小（例如，`uint8`）。
  - `double`
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `boolean`
- 当您将 **判决类型** 参数设置为 **Log-likelihood ratio** 或 **Approximate log-likelihood ratio** 时 — 模块继承的输出数据类型与输入的数据类型匹配。

有关指定数据类型的信息，请参阅数据类型助手。

### **去旋转因子** — 去旋转因子 `Same word length as input` (默认) | `Specify word length`

去旋转因子，指定为 `Same word length as input` 或 `Specify word length`。

#### 依赖项

此参数仅在输入为定点且 **相位偏移 (rad)** 参数不是 π/2 的倍数时适用。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 定点输入必须为有符号。  b 仅当在硬件实现窗格中选择 ASIC/FPGA 时，输出才为 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 BPSK 调制数据

BPSK Demodulator Baseband 模块解调使用二进制相移键控 (BPSK) 方法调制的信号。输入是已调制信号的基带表示。此模块接受标量或列向量输入信号。输入信号必须是离散时间复信号。该模块将点 exp(jϕ) 或 -exp(jϕ) 分别映射为 0 和 1。`Phase offset (rad)` 参数指定 ϕ 的值。
