---
type: simulink-block
title: 'Reshape'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'reshape'
documentation_source_path: 'slref/reshape.html'
language: zh-CN
chinese_source: official
---

# Reshape

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，其维度根据**输出维度**参数而更改。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

使用**输出维度**参数中指定的维度创建的输出信号。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **输出维度** — 输出信号的维度 **一维数组** (默认) | **列向量(二维)** | **行向量(二维)** | **自定义** | **从引用输入端口派生**

指定输出信号的维度。

| 输出维度 | 描述 |
| --- | --- |
| 一维数组 | 将多维数组转换为向量（1 维数组）数组信号。输出向量包含输入矩阵的第一列，后接第二列，以此类推。（此选项会保留向量输入不变。） |
| 列向量 | 将向量、矩阵或多维输入信号转换为列矩阵，即一个 *M*×1 矩阵，其中 *M* 是输入信号中的元素数。对于矩阵，转换是按列优先顺序进行的。对于多维数组，转换从第一个维度开始进行。 |
| 行向量 | 将向量、矩阵或多维输入信号转换为行矩阵，即一个 1×*N* 矩阵，其中 *N* 是输入信号中的元素数。对于矩阵，转换是按列优先顺序进行的。对于多维数组，转换从第一个维度开始进行。 |
| 自定义 | 将输入信号转换为输出信号，其维度可使用**输出维度**参数来指定。此选项不支持可变大小的输入信号。 |
| 从引用输入端口派生 | 在模块中创建另一个输入端口 **Ref**。输出信号的维度派生自 Ref 输入端口的输入信号的维度。选择此选项将禁用**输出维度**参数。如果选择此参数，**U** 和 **Ref** 这两个输入端口的输入信号必须具有相同的采样模式（基于采样或基于帧）。此选项不支持可变大小的输入信号。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputDimensionality` |
| **类型**：字符向量 |
| **值**：`'1-D array'` | `'Column vector (2-D)'` | `'Row vector (2-D)'` | `'Customize'` | `'Derive from reference input port'` |
| **默认值**：`'1-D array'` |

### **输出维度** — 输出信号的自定义维度 `[1,1]` (默认) | `[integer]` | `[integer,integer]`

指定输出信号的维度。该值可以是一元素或多元素向量。值为 `[N]` 将输出大小为 `N` 的向量。值为 `[M N]` 将输出 `M`×`N` 矩阵。输入信号中的元素数必须与**输出维度**参数指定的元素数相匹配。对于多维数组，转换从第一个维度开始进行。

#### 依赖关系

要启用此参数，请将**输出维度**设置为**自定义**。

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
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

**FOR-GENERATE 循环支持**

对于此模块，HDL Coder 使用 `FOR-GENERATE` 循环生成代码。

当目标语言为 Verilog® 时，会生成循环展开的代码。有关详细信息，请参阅Unroll For-Generate Loops (HDL Coder)

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

更改信号的维度

Reshape 模块可以使用**输出维度**参数，将输入信号的维度更改为您指定的维度。例如，您可以使用该模块将 *N* 元素向量更改为 1×*N* 或 *N*×1 矩阵信号。
