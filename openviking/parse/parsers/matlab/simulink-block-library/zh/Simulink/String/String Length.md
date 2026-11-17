---
type: simulink-block
title: 'String Length'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringlength'
documentation_source_path: 'slref/stringlength.html'
language: zh-CN
chinese_source: worker-translation
---

# String Length

## 端口

### 输入

### **Port\_1** — 输入字符串标量

输入字符串，指定为标量。

**数据类型：** `string`
### 输出

### **Port\_1** — 字符数标量

输入字符串中的字符数，指定为标量。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如
`Simulink.NumericType`。

当您选择继承选项时，该模块表现出以下行为：

- `Inherit: Inherit via internal rule` —
  Simulink® 选择一种数据类型以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。
- `Inherit: Inherit via back propagation` —
  使用驱动模块的数据类型。

点击 **Show data type assistant** 按钮以显示 **Data Type
Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅
使用数据类型助手指定数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | *`<data type expression>`* |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Mode** — 数据类型类别 `Inherit`（默认）| `Built in` | `Expression`

数据类型类别，指定为 `Inherit`、
`Built in` 或 `Expression`。有关使用此参数的更多
信息，请参阅 使用数据类型助手指定数据类型。

#### 依赖关系

点击 **Show data type assistant** 按钮
可启用此参数。

## 所属库

Simulink / String

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018a 中引入**

## 描述

输出输入字符串中的字符数

String Length 模块输出输入字符串中的字符数。例如，您可以使用 String Length 模块将关注焦点移动到
字符串中的特定位置。
