---
type: simulink-block
title: 'Selector'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'selector'
documentation_source_path: 'slref/selector.html'
language: zh-CN
chinese_source: worker-translation
---

# Selector

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | 多维

输入信号，以及要输出元素的来源。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **IndxN** — 第 `N` 个索引信号 标量 | 向量 | 矩阵

外部端口，用于指定索引以选择相应的输出元素。

您可以指定自定义宽度的整数（例如，15 位整数或 23 位整数）作为索引信号值。配置整数宽度时，必须将 **Mode** 指定为 `Fixed point`，**Word length** 小于或等于 65,535，**Slope** 等于 1，并且 **Bias** 等于 0。有关指定定点数据类型的详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用外部索引端口，请在 **Index Option** 表的相应行中，将 **Index Option** 设置为 `Index vector (port)`、`Starting index (port)` 或 `Starting and ending indices (port)`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | 多维

由输入信号中选定或重新排序的元素生成的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### **Number of input dimensions** — 输入信号的维度数 `1`（默认）| 整数

指定输入信号的维度数。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfDimensions` |
| **类型：** character vector |
| **值：** `integer` |
| **默认：** `'1'` |

### **Index mode** — 索引模式 `One-based`（默认）| `Zero-based`

指定索引模式。如果选择 `One-based`，索引 1 指定输入向量的第一个元素。如果选择 `Zero-based`，索引 0 指定输入向量的第一个元素。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexMode` |
| **类型：** character vector |
| **值：** `'One-based' | 'Zero-based'` |
| **默认：** `'One-based'` |

### **Index Option** — 元素的索引方法 `Index vector (dialog)`（默认）| `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)` | `Starting and ending indices (port)`

按维度定义如何对信号元素进行索引。从列表中选择：

- `Select all`

  无需进一步配置。选择所有元素。
- `Index vector (dialog)`

  启用 **Index** 列。输入元素索引向量。
- `Index vector (port)`

  无需进一步配置。
- `Starting index (dialog)`

  启用 **Index** 和 **Output Size** 列。在 **Index** 列中输入要选择的元素范围的起始索引，在 **Output Size** 列中输入要选择的元素数量。
- `Starting index (port)`

  启用 **Output Size** 列。在 **Output Size** 列中输入要选择的元素数量。
- `Starting and ending indices (port)`

  无需进一步配置。

  使用此选项会生成可变大小输出信号。更新时，输出维度设置为与输入信号维度相同。执行期间，输出维度根据馈送到索引的信号更新。

  记录输出信号数据时，未选择的信号用 NaN 值填充。

**Index** 和 **Output Size** 列根据需要显示。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexOptionArray` |
| **类型：** cell array of character vectors |
| **值：** `{'Select all'}` | `{'Index vector (dialog)'}` | `{'Index vector (port)'}` | `{'Starting index (dialog)'}` | `{'Starting index (port)'}` | `{'Starting and ending indices (port)'}` |
| **默认：** `{'Index vector (dialog)'}` |

如果要使用 character vector 而不是 cell array of character vectors，请使用 `IndexOptions`。

### **Index** — 元素索引 `[1 3]`（默认）| 整数

当 **Index Option** 为 `Index vector (dialog)` 时，输入您感兴趣的每个元素的索引。

当 **Index Option** 为 `Starting index (dialog)` 时，输入要选择的元素范围的起始索引。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexParamArray` |
| **类型：** cell array of character vectors |
| **值：** 整数 |
| **默认：** `{'[1 3]'}` |

如果要使用 character vector 而不是 cell array of character vectors，请使用 `Indices`。

### **Output Size** — 模块输出信号的宽度 `1`（默认）| 整数

指定模块输出信号的宽度。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputSizeArray` |
| **类型：** cell array of character vectors |
| **值：** 整数 |
| **默认：** `{'1'}` |

如果要使用 character vector 而不是 cell array of character vectors，请使用 `OutputSizes`。

### **Input port size** — 输入信号的宽度 `3`（默认）| 整数

为 1-D 信号指定模块输入信号的宽度。输入 `-1` 以从驱动模块继承。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputPortWidth` |
| **类型：** character vector |
| **值：** `integer` |
| **默认：** `'3'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 引号中的标量或向量 |

### **Check for out-of-range index in accelerated simulation** — 在加速仿真模式下检查超出范围的索引值的选项 `off`（默认）| `on`

选中此复选框，使 Simulink® 在 accelerator 或 rapid accelerator 模式下仿真期间检查是否有任何索引值超出输入信号相关维度的有效索引范围。如果索引超出范围，Simulink 会停止仿真并显示错误消息。

**注意**

如果不选中此复选框，超出范围的索引值可能会导致 accelerator 或 rapid accelerator 模式仿真期间出现未定义行为。

无论是否选中此复选框，Simulink 都会在 normal 模式仿真期间执行此检查。

#### 编程用法

|  |
| --- |
| **参数：** `RuntimeRangeChecks` |
| **类型：** character vector |
| **值：** `'Off'` | `'On'` |
| **默认：** `'Off'` |

## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 本机浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port1** | 标量  向量  矩阵（最多 2-D） | Yes | Half  Single  Double | No | Yes | Yes | Yes | Yes |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* 是一种面积优化，其中 HDL Coder 识别多个功能等效资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *Streaming* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为多个较小大小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*（或寄存器重定时）是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* 优化创建带寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**早于 R2006a 引入**

### R2023a：索引信号支持自定义宽度的整数

从 R2023a 开始，您可以自定义用于为 Selector 模块指定索引信号值的整数宽度。

### R2023a：作为 **Index Option** 的 `Index vector (dialog)` 和 `Starting index (dialog)` 支持可变大小信号

从 R2023a 开始，配置为接受 1-D 可变大小输入信号的 Selector 模块支持将 `Index vector (dialog)` 和 `Starting index (dialog)` 作为 **Index Option**。

此增强功能允许您在将 Selector 模块配置为接受 1-D 可变大小输入信号时，从所有可用的 **Index Option** 设置中进行选择。

## 描述

从向量、矩阵或多维信号中选择输入元素

Selector 模块根据指定的索引提取输入向量、矩阵或多维信号的选定元素。提取的信号可以与输入信号以不同方式分组。

根据为 **Number of input dimensions** 参数输入的值，会显示一个索引设置表。表的每一行对应于 **Number of input dimensions** 中的一个输入维度。对于每个维度，定义要处理的信号元素。将向量信号指定为 1-D 信号，将矩阵信号指定为 2-D 信号。当您为多维信号操作配置 Selector 模块时，模块图标会更改。

例如，假设一个采用 one-based 索引模式的 6-D 信号。Selector 模块对话框的表会更改，为每个维度包含一行。如果按下表所示定义维度，则输出为 `Y = U(1:end,2:6,[1 3 5],Idx4:Idx4+7,Idx5,Idx6(1):Idx6(2))`，其中 `Idx4`、`Idx5` 和 `Idx6` 是维度 4、5 和 6 的索引端口。有关详细信息，请参阅 Select Elements from Multidimensional Array Using Selector Block。

| 行 | Index Option | Index | Output Size |
| --- | --- | --- | --- |
| 1 | `Select all` |  |  |
| 2 | `Starting index (dialog)` | `2` | `5` |
| 3 | `Index vector (dialog)` | `[1 3 5]` |  |
| 4 | `Starting index (port)` |  | `8` |
| 5 | `Index vector (port)` |  |  |
| 6 | `Starting and ending indices (port)` |  |  |

您可以将总线数组用作 Selector 模块的输入信号。有关定义和使用总线数组的详细信息，请参阅 Group Nonvirtual Buses in Arrays of Buses。

**注意**

Selector 模块不会更改输入信号的维度数（维数）。如果需要将信号的维度更改为指定的维度，请使用 Reshape 模块。
