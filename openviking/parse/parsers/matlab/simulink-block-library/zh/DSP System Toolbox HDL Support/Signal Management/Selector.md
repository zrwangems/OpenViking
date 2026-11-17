---
type: simulink-block
title: 'Selector'
family: 'hdlcoder'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'selector'
documentation_source_path: '../dsp/../simulink/slref/selector.html'
language: zh-CN
chinese_source: worker-translation
---

# Selector

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | 多维
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: IndxN
  summary: 第 N 个索引信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵 | 多维
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | 多维

输入信号，也是输出信号元素的来源。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **IndxN** — 第 `N` 个索引信号 标量 | 向量 | 矩阵

外部端口，用于指定选择对应输出元素的索引。

您可以将自定义宽度的整数（例如，15 位整数或 23 位整数）指定为索引信号值。配置整数宽度时，必须将 **Mode** 指定为 `Fixed point`，**Word length** 小于或等于 65,535，**Slope** 等于 1，**Bias** 等于 0。有关指定定点数据类型的详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用外部索引端口，请在 **Index Option** 表的对应行中，将 **Index Option** 设置为 `Index vector (port)`、`Starting index (port)` 或 `Starting and ending indices (port)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | 多维

由输入信号的选定或重排元素生成的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Number of input dimensions
  summary: 输入信号的维度数 1（默认）| 整数
  group: ''
  block_parameter: NumberOfDimensions
  type: character vector
  values: integer
  default: '''1'''
- name: Index mode
  summary: 索引模式 One-based（默认）| Zero-based
  group: ''
  block_parameter: IndexMode
  type: character vector
  values: '''One-based'' | ''Zero-based'''
  default: '''One-based'''
- name: Index Option
  summary: 元素的索引方法 Index vector (dialog)（默认）| Select all | Index vector (port) | Starting index (dialog) | Starting index
    (port) | Starting and ending indices (port)
  group: ''
  block_parameter: IndexOptionArray
  type: cell array of character vectors
  values: '{''Select all''} | {''Index vector (dialog)''} | {''Index vector (port)''} | {''Starting index (dialog)''} | {''Starting
    index (port)''} | {''Starting and ending indices (port)''}'
  default: '{''Index vector (dialog)''}'
- name: Index
  summary: 元素的索引 [1 3]（默认）| 整数
  group: ''
  block_parameter: IndexParamArray
  type: cell array of character vectors
  values: integers
  default: '{''[1 3]''}'
- name: Output Size
  summary: 模块输出信号的宽度 1（默认）| 整数
  group: ''
  block_parameter: OutputSizeArray
  type: cell array of character vectors
  values: integers
  default: '{''1''}'
- name: Input port size
  summary: 输入信号的宽度 3（默认）| 整数
  group: ''
  block_parameter: InputPortWidth
  type: character vector
  values: integer
  default: '''3'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Check for out-of-range index in accelerated simulation
  summary: 在加速器和快速加速器仿真模式下检查越界索引值的选项 off（默认）| on
  group: ''
  block_parameter: RuntimeRangeChecks
  type: character vector
  values: '''Off'' | ''On'''
  default: '''Off'''
```

### **Number of input dimensions** — 输入信号的维度数 `1`（默认）| 整数

指定输入信号的维度数。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberOfDimensions` |
| **类型**：character vector |
| **值**：`integer` |
| **默认值**：`'1'` |

### **Index mode** — 索引模式 `One-based`（默认）| `Zero-based`

指定索引模式。如果选择 `One-based`，索引 1 指定输入向量的第一个元素。如果选择 `Zero-based`，索引 0 指定输入向量的第一个元素。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndexMode` |
| **类型**：character vector |
| **值**：`'One-based' | 'Zero-based'` |
| **默认值**：`'One-based'` |

### **Index Option** — 元素的索引方法 `Index vector (dialog)`（默认）| `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)` | `Starting and ending indices (port)`

按维度定义信号元素的索引方式。从列表中选择：

- `Select all`

  无需进一步配置。选择所有元素。
- `Index vector (dialog)`

  启用 **Index** 列。输入元素的索引向量。
- `Index vector (port)`

  无需进一步配置。
- `Starting index (dialog)`

  启用 **Index** 和 **Output Size** 列。在 **Index** 列中输入要选择的元素范围的起始索引，在 **Output Size** 列中输入要选择的元素数量。
- `Starting index (port)`

  启用 **Output Size** 列。在 **Output Size** 列中输入要选择的元素数量。

- `Starting and ending indices (port)`

  无需进一步配置。

  使用此选项会产生可变大小输出信号。更新时，输出维度设置为与输入信号维度相同。执行期间，输出维度根据馈送索引的信号进行更新。

  记录输出信号数据时，未选择的信号用 NaN 值填充。

**Index** 和 **Output Size** 列根据需要显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndexOptionArray` |
| **类型**：cell array of character vectors |
| **值**：`{'Select all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` | `{'Starting and ending indices (port)'}` |
| **默认值**：`{'Index vector (dialog)'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `IndexOptions`。

### **Index** — 元素的索引 `[1 3]`（默认）| 整数

当 **Index Option** 为 `Index vector (dialog)` 时，输入您感兴趣的每个元素的索引。

当 **Index Option** 为 `Starting index (dialog)` 时，输入要选择的元素范围的起始索引。

#### 编程使用

|  |
| --- |
| **模块参数**：`IndexParamArray` |
| **类型**：cell array of character vectors |
| **值**：integers |
| **默认值**：`{'[1 3]'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `Indices`。

### **Output Size** — 模块输出信号的宽度 `1`（默认）| 整数

指定模块输出信号的宽度。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputSizeArray` |
| **类型**：cell array of character vectors |
| **值**：integers |
| **默认值**：`{'1'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `OutputSizes`。

### **Input port size** — 输入信号的宽度 `3`（默认）| 整数

指定一维信号的模块输入信号宽度。输入 `-1` 以从驱动模块继承。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputPortWidth` |
| **类型**：character vector |
| **值**：`integer` |
| **默认值**：`'3'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### **Check for out-of-range index in accelerated simulation** — 在加速器和快速加速器仿真模式下检查越界索引值的选项 `off`（默认）| `on`

选中此复选框，使 Simulink® 在加速器或快速加速器模式下仿真期间检查是否有任何索引值超出输入信号相关维度的有效索引范围。如果索引越界，Simulink 停止仿真并显示错误消息。

**注意**

如果您不选中此复选框，越界索引值可能导致加速器或快速加速器模式仿真期间出现未定义行为。

无论您是否选中此复选框，Simulink 在正常模式仿真期间都会执行此检查。

#### 编程使用

|  |
| --- |
| **Parameter:** `RuntimeRangeChecks` |
| **类型**：character vector |
| **值**：`'Off'` | `'On'` |
| **默认值**：`'Off'` |
## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | No | Yes | Yes | Yes | Yes |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* 是一种面积优化，HDL Coder 在其中识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *Streaming* 是一种面积优化，HDL Coder 在其中将向量数据路径转换为标量数据路径（或转换为若干较小尺寸的向量数据路径）。 |

**速度优化**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*，即寄存器重定时，是一种速度优化，它在设计中移动现有延迟以减少关键路径，同时保持功能行为。 |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* 优化创建带寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2023a: 索引信号支持自定义宽度的整数

从 R2023a 开始，您可以自定义用于为 Selector 模块指定索引信号值的整数宽度。

### R2023a: 当 **Index Option** 为 `Index vector (dialog)` 和 `Starting index (dialog)` 时支持可变大小信号

从 R2023a 开始，配置为接受一维可变大小输入信号的 Selector 模块支持 `Index vector (dialog)` 和 `Starting index (dialog)` 作为 **Index Option**。

此增强功能允许您在将 Selector 模块配置为接受一维可变大小输入信号时，从所有可用的 **Index Option** 设置中进行选择。

## 描述

从向量、矩阵或多维信号中选择输入元素

Selector 模块根据指定的索引提取输入向量、矩阵或多维信号的选定元素。提取的信号可以以不同于输入信号的方式分组。

根据您为 **Number of input dimensions** 参数输入的值，将显示索引设置表。表的每一行对应 **Number of input dimensions** 中的一个输入维度。对于每个维度，您定义要处理的信号元素。将向量信号指定为一维信号，将矩阵信号指定为二维信号。当您为多维信号操作配置 Selector 模块时，模块图标会发生变化。

例如，假设一个 6 维信号，使用基于一的索引模式。Selector 模块对话框的表变为每个维度包含一行。如果您按下表定义维度，则输出为 `Y = U(1:end,2:6,[1 3 5],Idx4:Idx4+7,Idx5,Idx6(1):Idx6(2))`，其中 `Idx4`、`Idx5` 和 `Idx6` 是维度 4、5 和 6 的索引端口。有关更多信息，请参阅 Select Elements from Multidimensional Array Using Selector Block。

| Row | Index Option | Index | Output Size |
| --- | --- | --- | --- |
| 1 | `Select all` |  |  |
| 2 | `Starting index (dialog)` | `2` | `5` |
| 3 | `Index vector (dialog)` | `[1 3 5]` |  |
| 4 | `Starting index (port)` |  | `8` |
| 5 | `Index vector (port)` |  |  |
| 6 | `Starting and ending indices (port)` |  |  |

您可以将总线数组用作 Selector 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。

**注意**

Selector 模块不改变输入信号的维度数（维数）。如果您需要将信号的维数更改为您指定的维度，请使用 Reshape 模块。
