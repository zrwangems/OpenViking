---
type: simulink-block
title: 'Assignment'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'assignment'
documentation_source_path: '../simulink/slref/assignment.html'
language: zh-CN
chinese_source: worker-translation
---

# Assignment

## 端口
```yaml
ports:
- name: Y0
  summary: 输出信号的初始值 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | Boolean |
    enumerated | bus
- name: U
  summary: 输入数据端口 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | Boolean |
    enumerated | bus
- name: IndxN
  summary: 第 *N* 个索引信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Y
  summary: 具有已赋值元素的输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | enumerated
    | bus
```

### 输入

### **Y0** — 输出信号的初始值 标量 | 向量

输出信号的初始值。如果输入数据端口（**U**）指定的信号未被赋予与初始值不同的值，则端口 **Y** 处的输出信号值与初始值匹配。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

### **U** — 输入数据端口 标量 | 向量

在指定时赋值给输出元素的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `Boolean` | `enumerated` | `bus`

### **IndxN** — 第 *N* 个索引信号 标量 | 向量

外部端口，用于指定对应输出元素赋值的索引。

您可以将自定义宽度的整数（例如，15 位整数或 23 位整数）指定为索引信号值。配置整数宽度时，必须将 **Mode** 指定为 `Fixed point`，**Word length** 小于或等于 65,535，**Slope** 等于 1，**Bias** 等于 0。有关指定定点数据类型的详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖

要启用外部索引端口，请在 **Index Option** 表的对应行中，将 **Index Option** 设置为 `Index vector (port)` 或 `Starting index (port)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Y** — 具有已赋值元素的输出信号 标量 | 向量

具有指定元素已赋值的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Number of output dimensions
  summary: 输出信号的维度数 1（默认）| 整数
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
  values: '''Zero-based'' | ''One-based'''
  default: '''One-based'''
- name: Index Option
  summary: 元素的索引方法 Index vector (dialog)（默认）| Assign all | Index vector (port) | Starting index (dialog) | Starting index
    (port)
  group: ''
  block_parameter: IndexOptionArray
  type: cell array of character vectors
  values: '{''Assign all''} | {''Index vector (dialog)''} | {''Index vector (port)''} | {''Starting index (dialog)''} | {''Starting
    index (port)''}'
  default: '{''Index vector (dialog)''}'
- name: Index
  summary: 元素的索引 1（默认）| 整数
  group: ''
  block_parameter: IndexParamArray
  type: cell array of character vectors
  values: integers
  default: '{''1''}'
- name: Output Size
  summary: 模块输出信号的宽度 1（默认）| 整数
  group: ''
  block_parameter: OutputSizeArray
  type: cell array of character vectors
  values: integers
  default: '{''1''}'
- name: Initialize output (Y)
  summary: 如何初始化输出信号 Initialize using input port <Y0>（默认）| Specify size for each dimension in the table
  group: ''
  block_parameter: OutputInitialize
  type: character vector
  values: '''Initialize using input port <Y0>'' | ''Specify size for each dimension in table'''
  default: '''Initialize using input port <Y0>'''
- name: Action if any output element is not assigned
  summary: 产生警告或错误的选项 Warning（默认）| Error | None
  group: ''
  block_parameter: DiagnosticForDimensions
  type: character vector
  values: '''Error'' | ''Warning'' | ''None'''
  default: '''Warning'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Check for out-of-range index in accelerated simulation
  summary: 在加速器和快速加速器仿真模式下检查超出范围的索引值的选项 off（默认）| on
  group: ''
  block_parameter: RuntimeRangeChecks
  type: character vector
  values: '''Off'' | ''On'''
  default: '''Off'''
```

### **Number of output dimensions** — 输出信号的维度数 `1`（默认）| 整数

输入输出信号的维度数。

#### 编程使用

|  |
| --- |
| **Parameter:** `NumberOfDimensions` |
| **类型**：character vector |
| **值**：integer |
| **默认值**：`'1'` |

### **Index mode** — 索引模式 `One-based`（默认）| `Zero-based`

选择索引模式。如果选择 `One-based`，索引 1 指定输入向量的第一个元素。如果选择 `Zero-based`，索引 0 指定输入向量的第一个元素。

#### 编程使用

|  |
| --- |
| **Parameter:** `IndexMode` |
| **类型**：character vector |
| **值**：`'Zero-based'` | `'One-based'` |
| **默认值**：`'One-based'` |

### **Index Option** — 元素的索引方法 `Index vector (dialog)`（默认）| `Assign all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)`

按维度定义信号的元素如何被索引。从列表中选择：

| 菜单项 | 操作 |
| --- | --- |
| `Assign all` | 所有元素都被赋值。 |
| `Index vector (dialog)` | 启用 **Index** 列。输入元素的索引。 |
| `Index vector (port)` | 索引端口定义元素的索引。 |
| `Starting index (dialog)` | 启用 **Index** 列。输入要赋值的元素范围的起始索引。 |
| `Starting index (port)` | 索引端口定义要赋值的元素范围的起始索引。 |

如果您为表中任一维度选择 `Index vector (port)` 或 `Starting index (port)`，则可以为 **Initialize output (Y)** 参数指定以下值之一：

- `Initialize using input port <Y0>`
- `Specify size for each dimension in table`

否则，`Y0` 始终初始化输出端口 `Y`。

**Index** 和 **Output Size** 列在相关时显示。

#### 编程使用

|  |
| --- |
| **Parameter:** `IndexOptionArray` |
| **类型**：cell array of character vectors |
| **值**：`{'Assign all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` |
| **默认值**：`{'Index vector (dialog)'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `IndexOptions`。

### **Index** — 元素的索引 `1`（默认）| 整数

如果 **Index Option** 为 `Index vector (dialog)`，请输入您感兴趣的每个元素的索引。

如果 **Index Option** 为 `Starting index (dialog)`，请输入要选择的元素范围的起始索引。从起始点开始的元素数量由 `U` 处该维度的大小决定。

#### 编程使用

|  |
| --- |
| **Parameter:** `IndexParamArray` |
| **类型**：cell array of character vectors |
| **值**：integers |
| **默认值**：`{'1'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `Indices`。

### **Output Size** — 模块输出信号的宽度 `1`（默认）| 整数

输入模块输出信号的宽度。

#### 依赖

要启用此列，请将 **Initialize output (Y)** 设置为 `Specify size for each dimension in table`。

#### 编程使用

|  |
| --- |
| **Parameter:** `OutputSizeArray` |
| **类型**：cell array of character vectors |
| **值**：integers |
| **默认值**：`{'1'}` |

如需使用字符向量而非字符向量元胞数组，请使用 `OutputSizes`。

### **Initialize output (Y)** — 如何初始化输出信号 `Initialize using input port <Y0>`（默认）| `Specify size for each dimension in the table`

指定如何初始化输出信号。

- `Initialize using input port <Y0>` – 输入端口 `Y0` 处的信号初始化输出。
- `Specify size for each dimension in table` – 要求您在 **Output Size** 参数中指定模块输出信号的宽度。如果输出有未赋值的元素，这些元素的值是未定义的。

#### 依赖

要启用此参数，请为一个或多个维度将 **Index Option** 设置为 `Index vector (port)` 或 `Starting index (port)`。

#### 编程使用

|  |
| --- |
| **Parameter:** `OutputInitialize` |
| **类型**：character vector |
| **值**：`'Initialize using input port <Y0>'` | `'Specify size for each dimension in table'` |
| **默认值**：`'Initialize using input port <Y0>'` |

### **Action if any output element is not assigned** — 产生警告或错误的选项 `Warning`（默认）| `Error` | `None`

指定在未赋值所有输出元素时是否产生警告或错误。选项包括：

- `Warning` — Simulink 显示警告并继续仿真。
- `Error` — Simulink 终止仿真并显示错误。
- `None` — Simulink 不采取任何操作。

#### 依赖

要启用此参数，请为一个或多个维度将 **Index Option** 设置为 `Index vector (port)` 或 `Starting index (port)`。然后，将 **Initialize output (Y)** 设置为 `Specify size for each dimension in table`。

#### 编程使用

|  |
| --- |
| **Parameter:** `DiagnosticForDimensions` |
| **类型**：character vector |
| **值**：`'Error'` | `'Warning'` | `'None'` |
| **默认值**：`'Warning'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### **Check for out-of-range index in accelerated simulation** — 在加速器和快速加速器仿真模式下检查超出范围的索引值的选项 `off`（默认）| `on`

选中此复选框，使 Simulink 在加速器或快速加速器模式下仿真期间检查是否有任何索引值超出输入信号相关维度的有效索引范围。如果索引超出范围，Simulink 停止仿真并显示错误消息。

**注意**

如果您不选中此复选框，超出范围的索引值可能导致加速器或快速加速器模式仿真期间出现未定义行为。

无论是否选中此复选框，Simulink 在正常模式仿真期间都会执行此检查。

#### 编程使用

|  |
| --- |
| **Parameter:** `RuntimeRangeChecks` |
| **类型**：character vector |
| **值**：`'Off'` | `'On'` |
| **默认值**：`'Off'` |
## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL Architecture**

此模块有一个默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**Complex Data Support**

此模块支持复数信号的代码生成。

**Restrictions**

- 代码生成不支持可变大小信号。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023a: Index signal supports integer of custom width

从 R2023a 开始，您可以自定义用于为 Assignment 模块指定索引信号值的整数宽度。

## 描述

为信号的指定元素赋值

Assignment 模块为信号的指定元素赋值。您可以通过在模块对话框中输入索引，或将外部索引源连接到模块，来指定要赋值的元素的索引。模块数据端口 `U` 处的信号指定要赋给 `Y` 的值。模块用数据信号中的元素替换 `Y` 的指定元素。

根据您为 **Number of output dimensions** 参数输入的值，将显示一个索引选项表。表的每一行对应 **Number of output dimensions** 中的一个输出维度。对于每个维度，您可以定义要处理的信号元素。将向量信号指定为一维信号，将矩阵信号指定为二维信号。要启用外部索引端口，请在表的对应行中，将 **Index Option** 设置为 `Index vector (port)` 或 `Starting index (port)`。

例如，假设一个 5 维信号，使用基于 1 的索引模式。Assignment 模块对话框中的表将变为包含每个维度一行。如果您使用以下条目定义每个维度：

| 行 | Index Option | Index |
| --- | --- | --- |
| 1 | `Assign all` |  |
| 2 | `Index vector (dialog)` | `[1 3 5]` |
| 3 | `Starting index (dialog)` | `4` |
| 4 | `Starting index (port)` |  |
| 5 | `Index vector (port)` |  |

赋值的元素为 `Y(1:end,[1 3 5],4:3+size(U,3),Idx4:Idx4+size(U,4)-1,Idx5)=U`，其中 `Idx4` 和 `Idx5` 是维度 4 和 5 的输入端口。

在正常模式下使用 Assignment 模块时，即使模型未显式初始化模块输出，Simulink® 也会将模块输出初始化为零。在加速器模式下，Simulink 将模型转换为 S-Function。这涉及代码生成。生成的代码可能不会隐式初始化模块输出。在这种情况下，您必须显式初始化模型输出。

您可以使用该模块为向量、矩阵或多维信号赋值。

您可以使用总线数组作为 Assignment 模块的输入信号。

### 条件子系统中的 Assignment 模块

如果将 Assignment 模块放在条件子系统模块中，在许多情况下会插入一个隐藏的信号缓冲区（相当于 Signal Conversion 模块），并且将来自具有部分写入的 Assignment 模块的信号合并可能导致错误。

但是，如果您为条件子系统 Outport 模块选中 **Ensure outport is virtual** 参数，则支持此类情况，并且可以使用 Assignment 模块对数组进行部分写入。请参阅 Ensure Output Port Is Virtual。
