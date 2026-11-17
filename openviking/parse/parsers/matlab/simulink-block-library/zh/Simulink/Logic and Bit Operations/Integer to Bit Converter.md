---
type: simulink-block
title: 'Integer to Bit Converter'
family: 'hdlcoder'
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
```yaml
ports:
- name: In
  summary: 输入信号 整数 | 整数列向量
  direction: input
  data_types: double
- name: Out
  summary: 输出信号 位标量 | 位列向量
  direction: output
```

### 输入

### **In** — 输入信号 整数 | 整数列向量

输入信号，指定为整数或长度为 *N* 的整数列向量。

如果 **Number of bits per integer(M)** 参数指定了 *M*：

- 当 **Number of bits per integer** 参数设置为 `Unsigned` 时，输入值必须是范围 [0, (2*M* – 1)] 内的整数。
- 当 **Number of bits per integer** 参数设置为 `Signed` 时，输入值必须是范围 [(–2*M*-1), (2*M* – 1 – 1)] 内的整数。

在仿真期间，该模块执行运行时检查，如果任何输入值超出适当的范围，则发出错误。当该模块生成代码时，它不执行此运行时检查。

**数据类型：** `double`
### 输出

### **Out** — 输出信号 位标量 | 位列向量

输出信号，返回为标量或长度为 *M·N* 的位列向量。
## 参数
```yaml
parameters:
- name: Number of bits per integer(M)
  summary: 每个整数的位数 3（默认）| 范围 [1, 32] 内的整数
  group: ''
  block_parameter: nbits
  type: character vector
  values: integer in the range [1, 32]
  default: '''3'''
- name: Treat input values as
  summary: 将输入值视为 Unsigned（默认）| Signed
  group: ''
  block_parameter: signedInputValues
  type: character vector
  values: '''Unsigned'' | ''Signed'''
  default: '''Unsigned'''
- name: Output bit order
  summary: 输出位顺序 MSB first（默认）| LSB first
  group: ''
  block_parameter: bitOrder
  type: character vector
  values: '''MSB first'' | ''LSB first'''
  default: '''MSB first'''
- name: Output data type
  summary: 输出数据类型 Inherit via internal rule（默认）| Smallest unsigned integer | Same as input | double | single | int8 | uint8
    | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: outDtype
  type: character vector
  values: '''Inherit via internal rule'' | ''Smallest unsigned integer'' | ''Same as input'' | ''double'' | ''single'' | ''int8''
    | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''| ''boolean'''
  default: '''Inherit via internal rule'''
```

### **Number of bits per integer(M)** — 每个整数的位数 `3`（默认）| 范围 [1, 32] 内的整数

映射到输入中每个整数的输入位数，指定为范围 [1, 32] 内的整数。

#### 编程使用

|  |
| --- |
| **模块参数**：`nbits` |
| **类型**：character vector |
| **值**：integer in the range [1, 32] |
| **默认值**：`'3'` |

### **Treat input values as** — 将输入值视为 `Unsigned`（默认）| `Signed`

指示整数值输入范围应被视为有符号还是无符号。

#### 编程使用

|  |
| --- |
| **模块参数**：`signedInputValues` |
| **类型**：character vector |
| **值**：`'Unsigned'` | `'Signed'` |
| **默认值**：`'Unsigned'` |

### **Output bit order** — 输出位顺序 `MSB first`（默认）| `LSB first`

定义输出信号的第一位是最高有效位（MSB）还是最低有效位（LSB）。

#### 编程使用

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：character vector |
| **值**：`'MSB first'` | `'LSB first'` |
| **默认值**：`'MSB first'` |

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定输出位的数据类型。您可以选择以下 **Output data type** 选项之一：

- `Inherit via internal rule` –– 该模块根据输入数据类型确定输出数据类型。

  - 如果输入信号是浮点类型（`single` 或 `double`），则输出数据类型与输入数据类型相同。
  - 如果输入数据类型不是浮点类型，则输出数据类型的确定方式与参数设置为 `Smallest integer` 时相同。
- `Smallest integer` –– 该模块根据“配置参数”对话框的“硬件实现”窗格中使用的设置选择输出数据类型。

  - 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型为理想的单比特大小（ufix1）。
  - 对于所有其他设备供应商选择，输出数据类型为具有最小可用字长的无符号整数，如“硬件实现”设置中所定义（例如 uint8）
- `Same as input`
- `double`
- `single`
- `uint8`
- `uint16`
- `uint32`

#### 编程使用

|  |
| --- |
| **模块参数**：`outDtype` |
| **类型**：character vector |
| **值**：`'Inherit via internal rule'` | `'Smallest unsigned integer'` | `'Same as input'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'`| `'boolean'` |
| **默认值**：`'Inherit via internal rule'` |
## 所属库

Simulink / Logic and Bit Operations Communications Toolbox / Utility Blocks HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 仅当在“硬件实现”窗格中选择 ASIC/FPGA 时，输出端才为 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector | Yes | Single  Double | Yes | Yes | Yes | No |

**延迟详细信息**

该模块具有多周期实现，会在生成代码中引入额外延迟。要查看添加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**浮点延迟**

| Architecture | Floating-Point Type | Latency Strategy | Latency (in cycles) | Custom Latency Support |
| --- | --- | --- | --- | --- |
| `default` | Single | Min | 6 | Yes |
| Max | 6 |
| Double | Min | 3 |
| Max | 6 |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2006a 之前引入**

### R2022a：Integer to Bit Converter 模块添加到 Simulink Logic and Bit Operations 库

Integer to Bit Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型继续正常工作。

## 描述

将整数向量映射为位向量

Integer to Bit Converter 模块将输入向量中的每个整数（或定点值）映射到输出向量中的一组位。

该模块是单速率和单通道的。该模块将每个整数值（或使用定点输入时的存储整数）映射到一组 *M* 位，使用 **Output bit order** 的选择来确定最高有效位。结果输出向量长度是输入向量长度的 *M* 倍。
