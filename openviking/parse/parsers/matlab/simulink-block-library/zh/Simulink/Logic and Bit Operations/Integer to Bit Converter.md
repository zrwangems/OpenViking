---
type: simulink-block
title: 'Integer to Bit Converter'
family: 'logic-and-bit-operations'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'integertobitconverter'
documentation_source_path: 'slref/integertobitconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer to Bit Converter

## 端口

### 输入

### **In** — 输入信号 整数 | 整数列向量

输入信号，指定为整数或长度为 *N* 的整数列向量。

如果 *M* 由 **每个整数的位数(M)** 参数指定：

- 当 **每个整数的位数** 参数设置为 `Unsigned` 时，输入值必须是 [0, (2*M* – 1)] 范围内的整数。
- 当 **每个整数的位数** 参数设置为 `Signed` 时，输入值必须是 [(–2*M*-1), (2*M* – 1 – 1)] 范围内的整数。

仿真期间，模块会执行运行时检查，并在任何输入值超出相应范围时发出错误。模块生成代码时，不会执行此运行时检查。

**数据类型：** `double`

### 输出

### **Out** — 输出信号 位标量 | 位列向量

输出信号，以标量或长度为 *M·N* 的位列向量形式返回。

## 参数

### **每个整数的位数(M)** — 每个整数的位数 `3`（默认）| [1, 32] 范围内的整数

输入中映射到每个整数的输入位数，指定为 [1, 32] 范围内的整数。

#### 编程使用

|  |
| --- |
| **模块参数**: `nbits` |
| **类型**: character vector |
| **值**: [1, 32] 范围内的整数 |
| **默认值**: `'3'` |

### **将输入值视为** — 将输入值视为 `Unsigned`（默认）| `Signed`

指定整数值输入范围应视为有符号还是无符号。

#### 编程使用

|  |
| --- |
| **模块参数**: `signedInputValues` |
| **类型**: character vector |
| **值**: `'Unsigned'` | `'Signed'` |
| **默认值**: `'Unsigned'` |

### **输出位顺序** — 输出位顺序 `MSB first`（默认）| `LSB first`

定义输出信号的第一个位是最高有效位 (MSB) 还是最低有效位 (LSB)。

#### 编程使用

|  |
| --- |
| **模块参数**: `bitOrder` |
| **类型**: character vector |
| **值**: `'MSB first'` | `'LSB first'` |
| **默认值**: `'MSB first'` |

### **输出数据类型** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定输出位的数据类型。您可以选择以下 **输出数据类型** 选项之一：

- `Inherit via internal rule` –– 模块根据输入数据类型确定输出数据类型。

  - 如果输入信号是浮点类型（`single` 或 `double`），则输出数据类型与输入数据类型相同。
  - 如果输入数据类型不是浮点类型，则输出数据类型的确定方式等同于将此参数设置为 `Smallest integer`。
- `Smallest integer` –– 模块根据“配置参数”对话框的“硬件实现”窗格中使用的设置选择输出数据类型。

  - 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型为理想的单比特大小 (ufix1)。
  - 对于所有其他设备供应商选项，输出数据类型为具有“硬件实现”设置中定义的最小可用字长的无符号整数（例如 uint8）。
- `Same as input`
- `double`
- `single`
- `uint8`
- `uint16`
- `uint32`

#### 编程使用

|  |
| --- |
| **模块参数**: `outDtype` |
| **类型**: character vector |
| **值**: `'Inherit via internal rule'` | `'Smallest unsigned integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`| `'boolean'` |
| **默认值**: `'Inherit via internal rule'` |

## 所属库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 仅当在“硬件实现”窗格中选择 ASIC/FPGA 时，输出才为 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的其他配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定针对浮点类型将设计中的模块映射到哪种延迟：`MAX`、`MIN`、`CUSTOM` 或 `ZERO`。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

对于 HDL 代码生成，该模块支持以下数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | Boolean | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量 | 是 | Single  Double | 是 | 是 | 是 | 否 |

**延迟详细信息**

此模块具有多周期实现，会在生成的代码中引入额外延迟。要查看添加的延迟，请查看生成的模型或验证模型。请参阅生成的模型和验证模型 (HDL Coder)。

**浮点延迟**

| 架构 | 浮点类型 | 延迟策略 | 延迟（以 cycles 为单位） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | 是 |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2006a 之前推出**

### R2022a：Integer to Bit Converter 模块已添加到 Simulink Logic and Bit Operations 库

Integer to Bit Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型仍可继续工作。

## 描述

将整数向量映射为位向量

Integer to Bit Converter 模块将输入向量中的每个整数（或定点值）映射为输出向量中的一组位。

此模块为单速率、单通道模块。该模块将每个整数值（或使用定点输入时的存储整数）映射为一组 *M* 位，并使用 **输出位顺序** 的所选设置来确定最高有效位。所得输出向量的长度为输入向量长度的 *M* 倍。
