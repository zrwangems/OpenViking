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
```yaml
ports:
- name: In
  summary: 输入信号 位标量 | 位列向量
  direction: input
  data_types: double
- name: Out
  summary: 输出信号 整数 | 整数列向量
  direction: output
```

### 输入

### **In** — 输入信号 位标量 | 位列向量

输入信号，指定为标量或位列向量，其长度为 **Number of bits per integer(M)** 参数中指定值的倍数。输入必须是值为 0 或 1 的位。

**数据类型：** `double`
### 输出

### **Out** — 输出信号 整数 | 整数列向量

输出信号，以整数或整数列向量形式返回。**After bit packing, treat resulting integer values as** 参数指定输入位被视为无符号还是有符号。

- 当输入位被视为无符号时，每个整数输出在范围 [0, (2*M* – 1)] 内。
- 当输入位被视为有符号时，每个整数输出在范围 [(–2*M*-1), (2*M* – 1 – 1)] 内。
## 参数
```yaml
parameters:
- name: Number of bits per integer(M)
  summary: 每个整数对应的位数 3（默认）| [1, 32] 范围内的整数
  group: ''
  block_parameter: nbits
  type: character vector
  values: integer in the range [1, 32]
  default: '''3'''
- name: Input bit order
  summary: 输入位顺序 MSB first（默认）| LSB first
  group: ''
  block_parameter: bitOrder
  type: character vector
  values: '''MSB first'' | ''LSB first'''
  default: '''MSB first'''
- name: After bit packing, treat resulting integer values as
  summary: 位打包后所得整数值的符号标志 Unsigned（默认）| Signed
  group: ''
  block_parameter: signedOutputValues
  type: character vector
  values: '''Unsigned'' | ''Signed'''
  default: '''Unsigned'''
- name: Output data type
  summary: 输出数据类型 Inherit via internal rule（默认）| Smallest integer | Same as input | double | single | int8 | uint8 | int16
    | uint16 | int32 | uint32
  group: ''
  block_parameter: outDtype
  type: character vector
  values: '''Inherit via internal rule'' | ''Smallest integer'' | ''Same as input'' | ''double'' | ''single'' | ''int8'' |
    ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'''
  default: '''Inherit via internal rule'''
```

### **Number of bits per integer(M)** — 每个整数对应的位数 `3`（默认）| [1, 32] 范围内的整数

映射到输出中每个整数的输入位数，指定为 [1, 32] 范围内的整数。

#### 编程使用

|  |
| --- |
| **模块参数**：`nbits` |
| **类型**：character vector |
| **值**：integer in the range [1, 32] |
| **默认值**：`'3'` |

### **Input bit order** — 输入位顺序 `MSB first`（默认）| `LSB first`

输入位顺序，指定为 `'MSB first'` 或 `'LSB first'`。

- `'MSB first'` –– 输入信号的第一位是最高有效位（MSB）。
- `'LSB first'` –– 输入信号的第一位是最低有效位（LSB）。

#### 编程使用

|  |
| --- |
| **模块参数**：`bitOrder` |
| **类型**：character vector |
| **值**：`'MSB first'` | `'LSB first'` |
| **默认值**：`'MSB first'` |

### **After bit packing, treat resulting integer values as** — 位打包后所得整数值的符号标志 `Unsigned`（默认）| `Signed`

指定位打包后所得整数值被视为有符号还是无符号。此参数设置决定哪些 **Output data type** 选项可用。

**提示**

当此参数设置为 `Unsigned` 且模块发生溢出时，模块的行为如同 **After bit packing, treat resulting integer values as** 设置为 `Signed`。

#### 编程使用

|  |
| --- |
| **模块参数**：`signedOutputValues` |
| **类型**：character vector |
| **值**：`'Unsigned'` | `'Signed'` |
| **默认值**：`'Unsigned'` |

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest integer` | `Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

**Output data type** 选项根据输出的所需符号性而变化。

如果输出整数为 `Signed`，可以从以下 **Output data type** 选项中选择：

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

当参数设置为 `Inherit via internal rule` 时，模块根据输入数据类型确定输出数据类型。

- 如果输入信号为浮点型（`double` 或 `single`），则输出数据类型与输入数据类型相同。
- 如果输入数据类型不是浮点型，则输出数据类型的确定方式如同参数设置为 `Smallest integer`。

当参数设置为 `Smallest integer` 时，模块根据“配置参数”对话框的“硬件实现”窗格中使用的设置选择输出数据类型。

- 如果为设备供应商选择 `ASIC/FPGA`，则输出数据类型为基于 **Number of bits per integer(M)** 参数设置的最小理想整数或定点数据类型。
- 对于所有其他设备供应商选择，输出数据类型为足以容纳理想最小位长的最小可用（有符号或无符号）整数字长。

#### 编程使用

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
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 定点输入必须为 ufix(1)。  b 当在“硬件实现”窗格中选择 ASIC/FPGA 且输出数据类型设置为 (a) Smallest integer 或 (b) Inherit via internal rule 且同时输入为非浮点型时，为 ufix(N) 或 sfix(N)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点类型的 `MAX`、`MIN`、`CUSTOM` 或 `ZERO` 延迟。请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性指定 `ZERO` 和 `MAX` 之间的自定义延迟值。请参阅 NFPCustomLatency (HDL Coder)。 |

**数据类型支持**

此模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | Scalar  Vector | Yes | Single  Double | Yes | Yes | Yes | No |

**延迟详细信息**

此模块具有多周期实现，会在生成代码中引入额外延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

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

### R2022a：Bit to Integer Converter 模块已添加到 Simulink Logic and Bit Operations 库

Bit to Integer Converter 模块已从 **Communications Toolbox** > **Utility Blocks** 库添加到 **Simulink** > **Logic and Bit Operations** 库。所有现有模型继续正常工作。

## 描述

将位向量映射为对应的整数向量

Bit to Integer Converter 模块将输入向量中的位组映射为输出向量中的整数。

如果 *M* 由 **Number of bits per integer(M)** 参数指定：

- 对于无符号整数，模块将每组 *M* 位映射为范围 [0, (2*M* – 1)] 内的整数。因此，输出向量长度为输入向量长度的 1/*M* 倍。
- 对于有符号整数，模块将每组 *M* 位映射为范围 [(–2*M*-1), (2*M* – 1 – 1)] 内的整数。
