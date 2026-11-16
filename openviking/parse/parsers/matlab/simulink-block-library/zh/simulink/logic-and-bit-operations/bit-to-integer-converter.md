---
type: simulink-block
title: 'Bit to Integer Converter'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'bittointegerconverter'
documentation_source_path: 'slref/bittointegerconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit to Integer Converter

## 端口

### 输入

### **In** — 输入信号 位标量 | 位列向量

输入信号，指定为位标量或位列向量，其长度是 **每个整数的位数(M)** 参数中指定值的倍数。输入必须为值为 0 或 1 的位。

**数据类型：** `double`

### 输出

### **Out** — 输出信号 整数 | 整数列向量

输出信号，返回为整数或整数列向量。**位打包后，将得到的整数值视为** 参数指定输入位被视为无符号还是有符号。

- 当输入位被视为无符号时，每个整数输出都在范围 [0, (2*M* – 1)] 内。
- 当输入位被视为有符号时，每个整数输出都在范围 [(–2*M*-1), (2*M* – 1 – 1)] 内。

## 参数

### **每个整数的位数(M)** — 每个整数的位数 `3`（默认） | [1, 32] 范围内的整数

映射到输出中每个整数的输入位数，指定为 [1, 32] 范围内的整数。

#### 编程用法

|  |
| --- |
| **模块参数**：`nbits` |
| **类型**：character vector |
| **值**：范围 [1, 32] 内的整数 |
| **默认值**：`'3'` |

### **输入位顺序** — 输入位顺序 `MSB first`（默认） | `LSB first`

输入位顺序，指定为 `'MSB first'` 或 `'LSB first'`。

- `'MSB first'` –– 输入信号的第一个位是最高有效位（MSB）。
- `'LSB first'` –– 输入信号的第一个位是最低有效位（LSB）。

#### 编程用法

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：character vector |
| **值**：`'MSB first'` | `'LSB first'` |
| **默认值**：`'MSB first'` |

### **位打包后，将得到的整数值视为** — 位打包后有符号整数值的标志 `Unsigned`（默认） | `Signed`

指定位打包后得到的整数值被视为有符号还是无符号。此参数设置决定哪些 **输出数据类型** 选项可用。

**提示**

当此参数设置为 `Unsigned` 且模块发生溢出时，模块的行为就如同 **位打包后，将得到的整数值视为** 设置为 `Signed`。

#### 编程用法

|  |
| --- |
| **模块参数**：`signedOutputValues` |
| **类型**：character vector |
| **值**：`'Unsigned'` | `'Signed'` |
| **默认值**：`'Unsigned'` |

### **输出数据类型** — 输出数据类型 `Inherit via internal rule`（默认） | `Smallest integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**输出数据类型** 选项会根据输出的所需有符号性而变化。

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

当您将该参数设置为 `Inherit via internal rule` 时，模块会根据输入数据类型确定输出数据类型。

- 如果输入信号为浮点类型（`double` 或 `single`），则输出数据类型与输入数据类型相同。
- 如果输入数据类型不是浮点类型，则输出数据类型的确定方式如同将该参数设置为 `Smallest integer`。

当您将该参数设置为 `Smallest integer` 时，模块会根据配置参数对话框的 Hardware Implementation 窗格中使用的设置选择输出数据类型。

- 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型是最小的理想整数或定点数据类型，具体取决于 **每个整数的位数(M)** 参数的设置。
- 对于所有其他设备供应商选择，输出数据类型是能够容纳理想最小位大小的最小可用（有符号或无符号）整数字长。

#### 编程用法

|  |
| --- |
| **模块参数**：`outDtype` |
| **类型**：character vector |
| **值**：`'Inherit via internal rule'` | `'Smallest integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **默认值**：`'Inherit via internal rule'` |

## 所属库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **直通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 定点输入必须为 ufix(1)。  b 当在 Hardware Implementation 窗格中选择 ASIC/FPGA，且输出数据类型设置为 (a) Smallest integer，或 (b) Inherit via internal rule 并且同时输入为非浮点类型时，为 ufix(N) 或 sfix(N)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外的配置选项，会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将您设计中的模块映射为浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

该模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | Yes | Single  Double | Yes | Yes | Yes | No |

**延迟详细信息**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（周期数） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | Yes |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2006a 之前引入**

### R2022a: Bit to Integer Converter 模块已添加到 Simulink Logic and Bit Operations 库

Bit to Integer Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型继续正常工作。

## 描述

将位向量映射到对应的整数向量

Bit to Integer Converter 模块将输入向量中的位组映射到输出向量中的整数。

如果 *M* 由 **每个整数的位数(M)** 参数指定：

- 对于无符号整数，模块将每组 *M* 个位映射到范围 [0, (2*M* – 1)] 内的整数。因此，输出向量长度是输入向量长度的 1/*M* 倍。
- 对于有符号整数，模块将每组 *M* 个位映射到范围 [(–2*M*-1), (2*M* – 1 – 1)] 内的整数。
