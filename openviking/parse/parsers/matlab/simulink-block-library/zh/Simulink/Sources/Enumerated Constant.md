---
type: simulink-block
title: 'Enumerated Constant'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'enumeratedconstant'
documentation_source_path: 'slref/enumeratedconstant.html'
language: zh-CN
chinese_source: worker-translation
---

# Enumerated Constant

## 端口

### 输出

### **Port\_1** — 枚举常量标量 | 向量 | 矩阵

枚举常量值，指定为标量、向量或矩阵。

**数据类型：** `enumerated`

## 参数

### **Output data type** — 输出数据类型 `Enum: SlDemoSign`（默认）| `Enum:<ClassName>`

指定希望模块从中输出一个或多个值的枚举类型。初始值 `Enum:``SlDemoSign` 是一个虚拟枚举类型，用于防止新克隆的模块导致错误。要指定所需的枚举类型，请从下拉列表中选择它，或在 **Output data type** 字段中输入 `Enum:``ClassName`，其中 `ClassName` 是定义该类型的 MATLAB® 类的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Enum:<ClassName>'` |
| **默认值**：`'Enum: SlDemoSign'` |

### **Mode** — 要指定的数据类别 `Enumerated`（默认）

选择要指定的数据类别。

`Enumerated`
:   枚举数据类型。选择 `Enumerated` 会启用右侧的第二个菜单/文本框，您可以在其中输入类名。

### **Value** — 枚举值 `SlDemoSign.Positive`（默认）| `Enum:<ClassName.Value>`

指定模块输出的值或值集合。模块的输出具有与 **Value** 参数相同的维度和元素。初始值 `SlDemoSign.Positive` 是一个虚拟枚举值，用于防止新克隆的模块导致错误。

要指定所需的枚举值，请从下拉列表中选择，或输入任何求值结果为所需结果的 MATLAB 表达式，包括使用可调参数的表达式。所有指定的值都必须属于 **Output data type** 所指示的类型。要指定包含枚举类型中每个值的数组，请使用 `enumeration` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Value` |
| **类型**：character vector |
| **值**：`'SlDemoSign.Positive'` | `'SlDemoSign.Zero'` | `'SlDemoSign.Negative'` | `'Enum:<ClassName.Value>'` |
| **默认值**：`'SlDemoSign.Positive'` |

### **Sample time** — 采样时间 `inf`（默认）| 标量 | 向量

指定仿真期间模块输出可以变化的时间间隔（例如，由于调整 **Value** 参数）。默认值 `inf` 表示模块输出永远不会变化。采样时间为 `inf` 可避免重新计算模块输出，从而加速仿真和生成代码。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'inf'` |

## 所属库

Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `enumerated` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2009b 中引入**

## 描述

生成枚举常量值

Enumerated Constant 模块输出枚举值的标量、数组或矩阵。您也可以使用 Constant 模块输出枚举值，但它提供的模块参数不适用于枚举类型，例如 **Output minimum** 和 **Output maximum**。当您需要一个仅输出常量枚举值的模块时，请使用 Enumerated Constant 而不是 Constant。有关详细信息，请参阅 Simulink Enumerations。
