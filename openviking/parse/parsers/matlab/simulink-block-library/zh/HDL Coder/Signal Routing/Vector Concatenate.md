---
type: simulink-block
title: 'Vector Concatenate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'vectorconcatenate'
documentation_source_path: '../simulink/slref/vectorconcatenate.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Concatenate

## 端口
```yaml
ports:
- name: Port_1
  summary: 要串联的第一个输入 标量 | 向量 | 矩阵 | 数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_N
  summary: 要串联的第 *N* 个输入 标量 | 向量 | 矩阵 | 数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: Port_1
  summary: 输入信号的串联 标量 | 向量 | 矩阵 | 数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 要串联的第一个输入 标量 | 向量 | 矩阵 | 数组

要串联的第一个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当将 **Mode** 设置为 `Multidimensional
  array` 时，才支持矩阵和数组输入。

当数据类型为 `Simulink.Bus` 对象时，输入必须为非虚拟总线。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — 要串联的第 *N* 个输入 标量 | 向量 | 矩阵 | 数组

要串联的第 *N* 个输入，指定为标量、向量、矩阵或数组。

- 输入必须具有相同的数据类型。
- 仅当将 **Mode** 设置为 `Multidimensional
  array` 时，才支持矩阵和数组输入。

#### 依赖关系

要添加输入端口，请将 **Number of inputs** 设置为大于或等于 2 的整数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### 输出

### **Port\_1** — 输入信号的串联 标量 | 向量 | 矩阵 | 数组

沿指定维度对输入信号进行串联。输出与输入具有相同的数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 输入端口数量 2（默认）| 正整数
  group: ''
  block_parameter: NumInputs
  values: '''2''（默认）| 带引号的正整数'
- name: Mode
  summary: 串联类型 Vector | Multidimensional array
  group: ''
  block_parameter: Mode
  values: '''Vector'' | ''Multidimensional array'''
- name: Concatenate dimension
  summary: 沿其串联输入数组的输出维度 标量整数
  group: ''
  block_parameter: ConcatenateDimension
  values: 带引号的标量整数
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property
Inspector**。

### **Number of inputs** — 输入端口数量 `2`（默认）| 正整数

将模块的输入数量指定为小于或等于 65536 的实值正整数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumInputs` |
| **值：** | `'2'`（默认）| 带引号的正整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'NumInputs','3')`

### **Mode** — 串联类型 `Vector` | `Multidimensional array`

选择模块以向量还是多维数组串联模式运行。Vector Concatenate 模块的默认 **Mode** 为 `Vector`。Matrix Concatenate 模块的默认 **Mode** 为 `Multidimensional array`。

- 当选择 `Vector` 时，模块执行向量串联。
- 当选择 `Multidimensional array` 时，模块执行矩阵串联。

| **Mode** 设置 | 输入信号 | 输出信号 |
| --- | --- | --- |
| `Vector` | - 向量 - 行向量（1×*M* 矩阵） - 列向量（*M*×1 矩阵） - 向量与行向量或列向量的组合 | 当所有输入均为向量时，输出为向量。如果任一输入为行向量或列向量，则输出分别为行向量或列向量。 |
| `Multidimensional array` | 任意维度的信号（标量、向量和矩阵） | 输出始终为数组。对于较低维度的输入，末尾维度假定为 `1`。例如，如果输出为 4 维而输入为 `[2x3]`（2 维），则此模块将输入视为 `[2x3x1x1]`。串联在通过 **Concatenate dimension** 参数指定的维度上进行。 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Mode` |
| **值：** | `'Vector'` | `'Multidimensional array'` |

**示例：** `set_param(gcb,'Mode','Vector')`

### **Concatenate dimension** — 沿其串联输入数组的输出维度 标量整数

指定沿其串联输入数组的输出维度。

- `1` — 垂直串联输入。垂直矩阵串联将输入矩阵在输出矩阵中上下堆叠。当插入 Vector Concatenate 模块并将 **Mode** 设置为 `Multidimensional array` 时，默认值为 `1`。
- `2` — 水平串联输入。水平矩阵串联将输入矩阵在输出矩阵中并排放置。当插入 Matrix Concatenate 模块时，默认值为 `2`。
- `3` 或更大 — 对输入执行多维串联。

输入矩阵必须具有兼容的大小才能进行串联。垂直串联要求输入矩阵具有相同的列数。水平串联要求输入矩阵具有相同的行数。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Multidimensional array`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ConcatenateDimension` |
| **值：** | 带引号的标量整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'ConcatenateDimension','3')`
## 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations Simulink / Signal Routing HDL Coder / Math Operations HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**FOR-GENERATE 循环支持**

对于此模块，HDL Coder 使用 `FOR-GENERATE` 循环生成代码。有关更多信息，请参阅 Unroll For-Generate Loops (HDL Coder)

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2009b 中引入**

## 描述

将相同数据类型的输入向量串联以进行迭代处理

Vector Concatenate 模块串联输入信号以创建非标量信号，您可以使用子系统（例如 for-each、while-iterator 或 for-iterator 子系统）对其进行迭代处理。

您可以使用多个 Vector Concatenate 模块分阶段创建输出信号，但结果是扁平的，就像使用单个模块串联信号一样。

输出信号中的信号按照模块输入信号的相同顺序出现。有关各种模块方向的端口顺序说明，请参阅 Identify Port Location on Rotated or Flipped Block。

您必须使用 Vector Concatenate 或 Matrix Concatenate 模块来定义总线数组。有关更多信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。
