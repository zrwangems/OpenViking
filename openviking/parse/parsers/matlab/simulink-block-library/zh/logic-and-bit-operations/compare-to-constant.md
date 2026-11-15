---
type: simulink-block
title: 'Compare To Constant'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetoconstant'
language: zh-CN
chinese_source: official
---

# Compare To Constant

确定信号与指定常量的比较方式

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 描述

Compare To Constant 模块用于将输入信号与常量进行比较。在**常量值**参数中指定常量。使用**运算符**参数指定输入与常量值的比较方式。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号（指定为标量、向量或矩阵）与常量进行比较。该模块首先将其**常量值**参数转换为输入数据类型，然后执行指定的运算。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 0 | 1 | 向量 | 矩阵

如果比较结果为 false，输出为 `0`；如果比较结果为 true，输出为 `1`。

**数据类型:** `uint8` | `Boolean`

## 参数

### **运算符** — 逻辑运算符 <= (默认) | == | ~= | < | >= | >

此参数可以具有以下值：

- `==` - 确定输入是否等于指定的常量。
- ~`=` - 确定输入是否不等于指定的常量。
- `<` - 确定输入是否小于指定的常量。
- `<=` - 确定输入是否小于或等于指定的常量。
- `>` - 确定输入是否大于指定的常量。
- `>=` - 确定输入是否大于或等于指定的常量。

#### 编程用法

|  |
| --- |
| **模块参数**：`relop` |
| **类型**：字符向量 |
| **值**：`'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **默认值**：`'<='` |

### **常量值** — 要与之比较的常量 常量

指定与输入进行比较的常量值。

#### 编程用法

|  |
| --- |
| **模块参数**：`const` |
| **类型**：字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值**：`'3.0'` |

### **输出数据类型** — 输出的数据类型 **boolean** (默认) | **uint8**

指定输出的数据类型，`boolean` 或 `uint8`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'boolean'` | `'uint8'` |
| **默认值**：`'boolean'` |

### **启用过零检测** — 选择此项以启用过零检测 `'on'` (默认) | `'off'`

选择此项以启用过零检测。有关详细信息，请参阅 中的过零检测。

#### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史记录

**在 R2006a 之前推出**
