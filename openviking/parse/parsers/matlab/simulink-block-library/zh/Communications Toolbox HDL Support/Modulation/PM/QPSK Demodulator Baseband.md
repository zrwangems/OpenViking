---
type: simulink-block
title: 'QPSK Demodulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'qpskdemodulatorbaseband'
documentation_source_path: '../comm/ref/qpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# QPSK Demodulator Baseband

## 端口

### 输入

### **In** — 输入 QPSK 调制信号 标量 | 向量

输入 QPSK 调制信号，指定为包含 QPSK 调制信号基带表示的复值标量或向量。当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅软判决 QPSK 解调以了解解调判决类型的注意事项。

在启用 **Var** 端口之前，此端口在模块上未命名。

**数据类型：** `double` | `single` | `fixed point`
**复数支持：** 是

### **Var** — 噪声方差估计 正标量

噪声方差估计，指定为正标量。

当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅软判决 QPSK 解调以了解解调判决类型的注意事项。

#### 依赖关系

此参数在将 **Noise variance source** 设置为 `Port` 时适用。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出信号 标量 | 列向量

输出信号，以标量或列向量形式返回。输出是 PSK 调制输入信号 **In** 的解调版本。

- 当将 **Output type** 设置为 `Integer` 时，返回的输出信号元素为范围 [0, 3] 内的整数。
- 当将 **Output type** 设置为 `Bit` 时，返回的输出信号包含具有偶数个元素的向量，因为 QPSK 每符号有 2 个比特。

此端口在模块上未命名。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Output type** — 整数或比特对输出指示符 `Integer`（默认）| `Bit`

整数或比特对输出指示符，指定为 `Integer` 或 `Bit`。

- 当将 **Output type** 设置为 `Integer` 且将 **Constellation ordering** 设置为 `Binary` 时，模块将点 e(jϕ + jπm/2) 映射到 *m*，其中 ϕ 是以弧度为单位的相位偏移（**Phase offset (rad)**），*m* 为 0、1、2 或 3。
- 当将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Hard decision` 时，输出包含二进制值对。最高有效位（向量中最顶部的位）是模块输出的第一个比特。
- 当将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，输出分别包含逐位 LLR 或近似 LLR 值。

### **Decision type** — 解调器输出 `Hard decision`（默认）| `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调器输出，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。LLR 和近似 LLR 输出与支持软判决输入的错误解码器（如 Viterbi Decoder）配合使用，以实现更优的性能。有关详细信息，请参阅算法。

`Log-likelihood ratio` 和 `Approximate log-likelihood ratio` 判决类型的输出值与输入值具有相同的数据类型。

#### 依赖关系

此参数在将 **Output type** 设置为 `Bit` 时适用。

### **Noise variance source** — 噪声方差估计的来源 `Dialog`（默认）| `Port`

噪声方差估计的来源，指定为以下选项之一：

- 要使用 **Noise variance** 参数定义噪声方差，请将此参数设置为 `Dialog`。
- 要使用 **Var** 端口定义噪声方差，请将此参数设置为 `Port`。

#### 依赖关系

此参数在将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时适用。

### **Noise variance** — 噪声方差估计 `1`（默认）| 正标量

噪声方差估计，指定为正标量。

当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅软判决 QPSK 解调以了解解调判决类型的注意事项。

此参数在普通模式、加速模式和快速加速模式下可调。如果使用 Simulink Coder™ 快速仿真 (RSIM) 目标构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。避免重新编译对于蒙特卡洛仿真非常有用，在此类仿真中，您需要使用不同的噪声量多次运行仿真（可能在多台计算机上）。

**可调：** 是

#### 依赖关系

此参数在将 **Noise variance source** 设置为 `Dialog` 时适用。

### **Constellation ordering** — 符号映射 `Gray`（默认）| `Binary`

整数或比特对输出的符号映射，指定为 `Gray` 或 `Binary`。

- 要使用格雷编码排序映射符号，请将此参数设置为 `Gray`。
- 要使用二进制编码排序映射符号，请将此参数设置为 `Binary`。

### **Phase offset (rad)** — 第零点的相位偏移 `pi/4`（默认）| 标量

信号星座图第零点的相位（以弧度为单位），指定为标量。

### 数据类型

### **Output** — 输出数据类型 `Same as input`

输出数据类型与输入数据类型相同。

#### 依赖关系

此设置适用于将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 的情况。

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

解调信号的输出数据类型，指定为以下选项之一：

- 对于整数输出，输出数据类型可以设置为 `'Inherit via internal rule'`、`'Smallest unsigned integer'`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`。
- 对于比特输出，当将 **Decision type** 设置为 `Hard decision` 时，输出数据类型可以设置为 `'Inherit via internal rule'`、`'Smallest unsigned integer'`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

当将此参数设置为 `'Inherit via internal rule'` 时，模块从输入端口继承输出数据类型。

- 如果输入为浮点类型（`single` 或 `double`），则输出数据类型与输入数据类型相同。
- 如果输入数据类型为定点，则输出数据类型的行为如同将此参数设置为 `'Smallest unsigned integer'`。

当将此参数设置为 `'Smallest unsigned integer'` 时，输出数据类型基于模型配置参数对话框中 **Hardware Implementation** 窗格中使用的设置。

- 如果在 **Hardware Implementation** 窗格中选择了 `ASIC/FPGA`，且将 **Output type** 设置为 `Bit`，则输出数据类型为理想的最小一位大小（`ufix(1)`）。对于所有其他选择，它是具有足以容纳 1 位的最小可用字长的无符号整数，通常对应于 char 的大小（例如 `uint8`）。
- 如果在 **Hardware Implementation** 窗格中选择了 `ASIC/FPGA`，且将 **Output type** 设置为 `Integer`，则输出数据类型为理想的最小两位大小（`ufix(2)`）。对于所有其他选择，它是具有足以容纳 2 位的最小可用字长的无符号整数，通常对应于 char 的大小（例如 `uint8`）。

有关指定数据类型的信息，请参阅数据类型助手。

#### 依赖关系

此参数在将 **Output type** 设置为 `Integer`，或将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Hard decision` 时适用。

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
| a 定点输入必须为有符号类型。  b 当在 Hardware Implementation 窗格中选择 ASIC/FPGA 时，比特输出的输出为 ufix(1)，整数输出的输出为 ufix(ceil(log2(M)))。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 QPSK 调制数据

QPSK Demodulator Baseband 模块解调使用正交相移键控方法 (QPSK) 调制的信号。输入是调制信号的基带表示。

输入必须为复信号。此模块接受标量或列向量输入信号。有关数据类型的信息，请参阅支持的数据类型。
