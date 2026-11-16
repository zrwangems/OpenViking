---
type: simulink-block
title: 'Enumerated Constant'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'enumeratedconstant'
documentation_source_path: '../simulink/slref/enumeratedconstant.html'
language: zh-CN
chinese_source: official
---

# Enumerated Constant

## 端口

### 输出

### **Port\_1** — 枚举常量 标量 | 向量 | 矩阵

枚举常量值，指定为标量、向量或矩阵。

**数据类型:** `enumerated`

## 参数

### **输出数据类型** — 输出数据类型 `Enum: SlDemoSign` (默认) | `Enum:<ClassName>`

指定您要模块输出的一个或多个值的枚举类型。初始值 `Enum:``SlDemoSign` 是虚拟枚举类型，可防止新克隆的模块导致错误。要指定所需的枚举类型，请从下拉列表中选择它，或在**输出数据类型**字段中输入 `Enum:``ClassName`，其中 `ClassName` 是定义类型的 MATLAB® 类的名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Enum:<ClassName>'` |
| **默认值**：`'Enum: SlDemoSign'` |

### **模式** — 要指定的数据的类别 **枚举** (默认)

选择要指定的数据类别。

**枚举**
:   枚举数据类型。选择**枚举**将启用右侧的另一个菜单/文本框，您可以在其中输入类名称。

### **值** — 枚举值 `SlDemoSign.Positive` (默认) | `Enum:<ClassName.Value>`

指定模块输出的值。模块的输出与**值**参数具有相同的维度和元素。初始值 `SlDemoSign.Positive` 是虚拟枚举值，可防止新克隆的模块导致错误。

要指定所需的枚举值，请从下拉列表中选择或者输入任何可以计算为所需结果的 MATLAB 表达式，其中包括使用可调参数的表达式。所有指定的值必须是由**输出数据类型**指示的类型。要指定包含枚举类型中每个值的数组，请使用 `enumeration` 函数。

#### 编程用法

|  |
| --- |
| **模块参数**：`Value` |
| **类型**：字符向量 |
| **值**：`'SlDemoSign.Positive'` | `'SlDemoSign.Zero'` | `'SlDemoSign.Negative'` | `'Enum:<ClassName.Value>'` |
| **默认值**：`'SlDemoSign.Positive'` |

### **采样时间** — 采样时间 `inf` (默认) | 标量 | 向量

指定仿真过程中该模块输出可以更改（例如，由于调整了**值**参数）的时间间隔。默认值 `inf` 表示模块输出永不更改。采样时间 `inf` 可通过避免重新计算模块输出，加快仿真和代码生成速度。有关详细信息，请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'inf'` |

## 所属库

Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `enumerated` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
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
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2009b 中推出**

## 描述

生成枚举常量值

Enumerated Constant 模块输出枚举值的标量、数组或矩阵。您也可以使用 Constant 模块输出枚举值，但它提供不适用于枚举类型的模块参数，如**输出最小值**和**输出最大值**。当您需要只输出常量枚举值的模块时，请使用 Enumerated Constant 而不是 Constant。有关详细信息，请参阅 Simulink 枚举。
