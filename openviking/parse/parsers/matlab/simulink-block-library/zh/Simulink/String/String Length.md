---
type: simulink-block
title: 'String Length'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / String'
documentation_page: 'stringlength'
documentation_source_path: 'slref/stringlength.html'
language: zh-CN
chinese_source: official
---

# String Length

## 端口

### 输入

### **Port\_1** — 输入字符串 标量

输入字符串，指定为标量。

**数据类型:** `string`
### 输出

### **Port\_1** — 字符数 标量

输入字符串中的字符数，指定为标量。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **输出数据类型** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | `<data type expression>`

输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。
- **继承:通过反向传播继承** - 使用驱动模块的数据类型。

点击**显示数据类型助手**按钮  以显示**数据类型助手**，帮助您设置数据类型属性。有关详细信息，请参阅 。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **默认值：**`'Inherit: Inherit via internal rule'` |

### **模式** — 数据类型的类别 `Inherit` (默认) | `Built in` | `Expression`

数据类型的类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

点击**显示数据类型助手**按钮将启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
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
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018a 中推出**

## 描述

输出输入字符串中的字符数

String Length 模块输出在输入字符串中的字符数。例如，您可以使用 String Length 模块将注意力焦点移至字符串中的特定位置。
