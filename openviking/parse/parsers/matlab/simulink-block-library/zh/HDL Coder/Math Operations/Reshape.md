---
type: simulink-block
title: 'Reshape'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'reshape'
documentation_source_path: '../simulink/slref/reshape.html'
language: zh-CN
chinese_source: worker-translation
---

# Reshape

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，其维度根据 **Output dimensionality** 参数进行更改。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，其维度由 **Output dimensionality** 参数指定。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Output dimensionality** — 输出信号的维度 `1-D array`（默认） | `Column vector (2-D)` | `Row vector (2-D)` | `Customize` | `Derive from reference input port`

指定输出信号的维度。

| 输出维度 | 描述 |
| --- | --- |
| 1-D array | 将多维数组转换为向量（一维数组）信号。输出向量由输入矩阵的第一列组成，后跟第二列，依此类推。（此选项使向量输入保持不变。） |
| Column vector | 将向量、矩阵或多维输入信号转换为列矩阵，即 *M*×1 矩阵，其中 *M* 是输入信号中的元素数。对于矩阵，转换按列主序进行。对于多维数组，转换沿第一个维度进行。 |
| Row vector | 将向量、矩阵或多维输入信号转换为行矩阵，即 1×*N* 矩阵，其中 *N* 是输入信号中的元素数。对于矩阵，转换按列主序进行。对于多维数组，转换沿第一个维度进行。 |
| Customize | 使用 **Output dimensions** 参数将输入信号转换为指定维度的输出信号。此选项不支持可变大小输入信号。 |
| Derive from reference input port | 在模块上创建第二个输入端口 **Ref**。从输入到 Ref 输入端口的信号维度推导输出信号的维度。选择此选项将禁用 **Output dimensions** 参数。选择此参数时，两个输入端口 **U** 和 **Ref** 的输入信号必须具有相同的采样模式（基于采样或基于帧）。此选项不支持可变大小输入信号。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputDimensionality` |
| **类型**：字符向量 |
| **值**：`'1-D array'` | `'Column vector (2-D)'` | `'Row vector (2-D)'` | `'Customize'` | `'Derive from reference input port'` |
| **默认值**：`'1-D array'` |

### **Output dimensions** — 输出信号的自定义维度 `[1,1]`（默认） | `[integer]` | `[integer,integer]`

指定输出信号的维度。该值可以是单元素或多元素向量。值为 `[N]` 时输出大小为 `N` 的向量。值为 `[M N]` 时输出 `M`×`N` 矩阵。输入信号的元素数必须与 **Output dimensions** 参数指定的元素数匹配。对于多维数组，转换沿第一个维度进行。

#### 依赖关系

要启用此参数，请将 **Output dimensionality** 设置为 `Customize`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputDimensions` |
| **类型**：字符向量 |
| **值**：`'[1,1]'` | `'integer'` | `'[integer,integer]'` |
| **默认值**：`'[1,1]'` |

## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**FOR-GENERATE 循环支持**

对于此模块，HDL Coder 使用 `FOR-GENERATE` 循环生成代码。

当目标语言为 Verilog® 时，生成循环展开代码。有关更多信息，请参阅 Unroll For-Generate Loops (HDL Coder)

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

更改信号的维度

Reshape 模块使用 **Output dimensionality** 参数将输入信号的维度更改为您指定的维度。例如，您可以使用该模块将 *N* 元素向量更改为 1×*N* 或 *N*×1 矩阵信号。
