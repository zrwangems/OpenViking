---
type: simulink-block
title: 'Compare To Constant'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'comparetoconstant'
documentation_source_path: 'slref/comparetoconstant.html'
language: zh-CN
chinese_source: worker-translation
---

# Compare To Constant

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵，与常量进行比较。该模块首先将其 **Constant value** 参数转换为输入数据类型，然后执行指定的运算。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 0 | 1 | 向量 | 矩阵

如果比较结果为假，则输出为 `0`；如果为真，则输出为 `1`。

**数据类型：** `uint8` | `Boolean`

## 参数

### **Operator** — 逻辑运算符 <= （默认） | == | ~= | < | >= | >

此参数可以具有以下值：

- `==` — 判断输入是否等于指定的常量。
- ~`=` — 判断输入是否不等于指定的常量。
- `<` — 判断输入是否小于指定的常量。
- `<=` — 判断输入是否小于或等于指定的常量。
- `>` — 判断输入是否大于指定的常量。
- `>=` — 判断输入是否大于或等于指定的常量。

#### 编程使用

|  |
| --- |
| **模块参数**：`relop` |
| **类型**：character vector |
| **值**：`'=='` | `'~='`| `'<'` |`'<='`| `'>='`| `'>'` |
| **默认值**：`'<='` |

### **Constant value** — 用于比较的常量 常量

指定与输入进行比较的常量值。

#### 编程使用

|  |
| --- |
| **模块参数**：`const` |
| **类型**：character vector |
| **Value:** scalar | vector | matrix | N-D array |
| **默认值**：`'3.0'` |

### **Output data type** — 输出的数据类型 `boolean` （默认） | `uint8`

指定输出的数据类型，`boolean` 或 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'boolean'` | `'uint8'` |
| **默认值**：`'boolean'` |

### **Enable zero-crossing detection** — 选择以启用零交叉检测 `'on'` （默认） | `'off'`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了额外的配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

确定信号如何与指定的常量进行比较

Compare To Constant 模块将输入信号与常量进行比较。在 **Constant value** 参数中指定常量。使用 **Operator** 参数指定输入与常量值的比较方式。
