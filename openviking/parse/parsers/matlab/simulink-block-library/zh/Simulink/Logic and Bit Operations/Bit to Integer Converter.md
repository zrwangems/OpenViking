---
type: simulink-block
title: 'Bit to Integer Converter'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bittointegerconverter'
documentation_source_path: '../simulink/slref/bittointegerconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit to Integer Converter

## 端口

### 输入

### **In** — 输入信号，位标量 | 位列向量

输入信号，指定为标量或位列向量，其长度为 **每个整数的位数(M)** 参数所指定值的整数倍。输入必须是值为 0 或 1 的位。

**数据类型：** `double`
### 输出

### **Out** — 输出信号，整数 | 整数列向量

输出信号，返回为整数或整数列向量。**位打包后，将生成的整数值视为** 参数指定将输入位视为无符号还是有符号。

- 当输入位被视为无符号时，每个整数输出都在 [0,
  (2*M* – 1)] 范围内。
- 当输入位被视为有符号时，每个整数输出都在
  [(–2*M*-1),
  (2*M* – 1 –
  1)] 范围内。

## 参数

### **每个整数的位数(M)** — 每个整数的位数 `3` (默认) | [1, 32] 范围内的整数

映射到输出中每个整数的输入位数，指定为 [1, 32] 范围内的整数。

#### 编程用法

|  |
| --- |
| **模块参数**: `nbits` |
| **类型**: character vector |
| **值**: [1, 32] 范围内的整数 |
| **默认值**: `'3'` |

### **输入位顺序** — 输入位顺序 `MSB first` (默认) | `LSB first`

输入位顺序，指定为 `'MSB first'` 或 `'LSB first'`。

- `'MSB first'` –– 输入信号的第一位是最高有效位 (MSB)。
- `'LSB first'` –– 输入信号的第一位是最低有效位 (LSB)。

#### 编程用法

|  |
| --- |
| **模块参数**: `bitOrder` |
| **类型**: character vector |
| **值**: `'MSB first'` | `'LSB first'` |
| **默认值**: `'MSB first'` |

### **位打包后，将生成的整数值视为** — 位打包后有符号整数值的标志 `Unsigned` (默认) | `Signed`

指定位打包后生成的整数值被视为有符号还是无符号。此参数设置决定哪些 **输出数据类型** 选项可用。

**提示**

当此参数设置为 `Unsigned` 且模块发生溢出时，模块的行为如同 **位打包后，将生成的整数值视为** 设置为 `Signed`。

#### 编程用法

|  |
| --- |
| **模块参数**: `signedOutputValues` |
| **类型**: character vector |
| **值**: `'Unsigned'` | `'Signed'` |
| **默认值**: `'Unsigned'` |

### **输出数据类型** — 输出数据类型 `Inherit via internal rule` (默认) | `Smallest integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**输出数据类型** 选项会根据所需的输出有符号性而变化。

如果输出整数为 `Signed`，可以从以下 **输出数据类型** 选项中选择：

- `Inherit via internal rule`
- `Smallest integer`
- `double`
- `single`
- `int8`
- `int16`
- `int32`

如果输出整数为 `Unsigned`，除了 `Signed` 选项外，还可以从以下选项中选择：

- `Same as input`
- `uint8`
- `uint16`
- `uint32`

当将参数设置为 `Inherit via internal rule` 时，模块会根据输入数据类型确定输出数据类型。

- 如果输入信号是浮点信号（`double` 或 `single`），则输出数据类型与输入数据类型相同。
- 如果输入数据类型不是浮点类型，则输出数据类型的确定方式与将参数设置为 `Smallest integer` 时相同。

当将参数设置为 `Smallest integer` 时，模块会根据 Configuration Parameters 对话框的 Hardware Implementation 窗格中使用的设置来选择输出数据类型。

- 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型是根据 **每个整数的位数(M)** 参数的设置确定的最小理想整数或定点数据类型。
- 对于所有其他设备供应商选择，输出数据类型是最小的可用（有符号或无符号）整数字长，该字长足以容纳理想最小位大小。

#### 编程用法

|  |
| --- |
| **模块参数**: `outDtype` |
| **类型**: character vector |
| **值**: `'Inherit via internal rule'` | `'Smallest integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **默认值**: `'Inherit via internal rule'` |

## 所属库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 定点输入必须为 ufix(1)。  b 当在 Hardware Implementation 窗格中选择 ASIC/FPGA，并且输出数据类型设置为 (a) Smallest integer，或 (b) Inherit via internal rule 且输入同时为非浮点时，为 ufix(N) 或 sfix(N)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点类型，是否将设计中的模块映射为 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔值 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | 是 | Single  Double | 是 | 是 | 是 | 否 |

**延迟详细信息**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看添加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（单位：cycles） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | 是 |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2006a 之前推出**

### R2022a: Bit to Integer Converter 模块添加到 Simulink Logic and Bit Operations 库

Bit to Integer Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型仍可继续工作。

## 描述

将位向量映射为对应的整数向量

Bit to Integer Converter 模块将输入向量中的位组映射为输出向量中的整数。

如果 *M* 由 **每个整数的位数(M)** 参数指定：

- 对于无符号整数，该模块将每组 *M* 位映射为 [0,
  (2*M* – 1)] 范围内的整数。因此，输出向量长度为输入向量长度的 1/*M* 倍。
- 对于有符号整数，该模块将每组 *M* 位映射为
  [(–2*M*-1),
  (2*M* – 1 – 1)] 范围内的整数。
