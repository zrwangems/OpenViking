---
type: simulink-block
title: 'Compare To Zero'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetozero'
---

# Compare To Zero

Determine how signal compares to zero

## 中文

确定信号与零的比较方式

### 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

### 描述

Compare To Zero 模块将输入信号与零进行比较。使用**运算符**参数指定输入与零的比较方式。

如果比较结果为 false，输出为 `0`；如果比较结果为 true，输出为 `1`。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号（指定为标量、向量或矩阵）与零进行比较。如果输入数据类型不能表示零，将发生参数溢出。要检测此溢出，请转到“配置参数”对话框的**诊断 > 数据有效性**窗格，并将**参数 > 检测上溢**设置为**警告**或**错误**。

在这种情况下，模块将输入信号与输入数据类型的*接地值*进行比较。例如，如果输入信号的类型为 `fixdt(0,8,2^0,10)`，由于偏置为 10，输入数据类型可以表示从 10 到 265 的无符号 8 位整数。接地值为 10，而不是 0。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 0 | 1 | 标量 | 向量 | 矩阵

如果比较结果为 false，输出为 `0`；如果比较结果为 true，输出为 `1`。

模块输出为 `uint8` 或 `boolean`，具体取决于您为**输出数据类型**参数所做的选择。

**数据类型:** `uint8` | `Boolean`

### 参数

#### **运算符** — 逻辑运算符 <= (默认) | == | ~= | < | >= | >

此参数可以具有以下值：

- `==` - 确定输入是否等于零。
- ~`=` - 确定输入是否不等于零。
- `<` - 确定输入是否小于零。
- `<=` - 确定输入是否小于或等于零。
- `>` - 确定输入是否大于零。
- `>=` - 确定输入是否大于或等于零。

##### 编程用法

|  |
| --- |
| **模块参数**：`relop` |
| **类型**：字符向量 |
| **值**：`'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **默认值**：`'<='` |

#### **输出数据类型** — 输出的数据类型 **boolean** (默认) | **uint8**

指定输出的数据类型，`boolean` 或 `uint8`。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'boolean'` | `'uint8'` |
| **默认值**：`'boolean'` |

#### **启用过零检测** — 选择此项以启用过零检测 on (默认) | off

选择此项以启用过零检测。有关详细信息，请参阅 中的过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

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

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Compare To Zero block compares an input signal to zero. Specify how the input is
compared to zero with the **Operator** parameter.

The output is `0` if the comparison is false, and
`1` if it is true.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal, specified as scalar, vector, or matrix, is compared with
zero. If the input data type cannot represent zero, parameter overflow
occurs. To detect this overflow, go to the **Diagnostics >
Data Validity** pane of the Configuration Parameters dialog
box and set **Parameters > Detect overflow** to
`warning` or
`error`.

In this case, the block compares the input signal to the
*ground value* of the input data type. For
example, if you have an input signal of type
`fixdt(0,8,2^0,10)`, the input data type can
represent unsigned 8-bit integers from 10 to 265 due to a bias of 10.
The ground value is 10, instead of 0.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal 0 | 1 | scalar | vector | matrix

The output is `0` if the comparison is false, and
`1` if it is true.

The block output is `uint8` or
`boolean`, depending on your selection for the
**Output data type** parameter.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Operator** — Logical operator <= (default) | == | ~= | < | >= | >

This parameter can have the following values:

- `==` — Determine whether the input is
  equal to zero.
- ~`=` — Determine whether the input is not
  equal to zero.
- `<` — Determine whether the input is
  less than zero.
- `<=` — Determine whether the input is
  less than or equal to zero.
- `>` — Determine whether the input is
  greater than zero.
- `>=` — Determine whether the input is
  greater than or equal to zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `relop` |
| **Type**: character vector |
| **Values**: `'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **Default**: `'<='` |

### **Output data type** — Data type of the output `boolean` (default) | `uint8`

Specify the data type of the output, `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**:`'boolean'` | `'uint8'` |
| **Default**: `'boolean'` |

### **Enable zero-crossing detection** — Select to enable zero-crossing detection on (default) | off

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
