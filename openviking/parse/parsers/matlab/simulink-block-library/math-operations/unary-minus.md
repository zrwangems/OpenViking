---
type: simulink-block
title: 'Unary Minus'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'unaryminus'
---

# Unary Minus

Negate input

## 中文

对输入求反

### 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

### 描述

Unary Minus 模块对输入进行求反。

### 端口

#### 输入

#### **Port\_1** — 要求反的信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
#### 输出

#### **Port\_1** — 输入信号的求反 标量 | 向量 | 矩阵 | N 维数组

输入信号的求反。输出具有与输入相同的数据类型和维度。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

### 参数

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

选中可实现整数溢出饱和。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

对于有符号整数数据类型，最负值的一元减法无法用该数据类型表示。在这种情况下，由**对整数溢出进行饱和处理**复选框控制模块的行为：

| 参数设置 | 模块行为 | 示例 |
| --- | --- | --- |
| **对整数溢出进行饱和处理** = `on` | 值饱和处理为该整数数据类型的最大正值 | - 对于 8 位有符号整数，-128 对应为 127。 - 对于 16 位有符号整数，-32768 对应为 32767。 - 对于 32 位有符号整数，-2147483648 对应为 2147483647。 |
| **对整数溢出进行饱和处理** = `off` | 值绕回到该整数数据类型的最小负值 | - 对于 8 位有符号整数，-128 依然是 -128。 - 对于 16 位有符号整数，-32768 依然是 -32768。 - 对于 32 位有符号整数，-2147483648 依然是 -2147483648。 |

##### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块仅支持有符号定点数据类型。 | |

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

此模块仅支持有符号定点数据类型。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Description

The
Unary
Minus
block negates the input.

## Ports

### Input

### **Port\_1** — Signal to negate scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Port\_1** — Negation of input signal scalar | vector | matrix | N-D array

Negation of the input signal. The output has the same data type and
dimensions as the input.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## Parameters

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Select to have integer overflows saturate. Otherwise, overflows
wrap.

When you select this check box, saturation applies to every internal
operation on the block, not just the output, or result. In general, the code
generation process can detect when overflow is not possible. In this case,
the code generator does not produce saturation code.

For signed-integer data types, the unary minus of the most negative value
is not representable by the data type. In this case, the **Saturate
on integer overflow** check box controls the behavior of the
block:

| Parameter Setting | Block Behavior | Examples |
| --- | --- | --- |
| **Saturate on integer overflow** = `on` | Values saturate to the most positive value of the integer data type | - For 8-bit signed integers, -128 maps to   127. - For 16-bit signed integers, -32768 maps to   32767. - For 32-bit signed integers, -2147483648 maps   to 2147483647. |
| **Saturate on integer overflow** = `off` | Values wrap to the most negative value of the integer data type | - For 8-bit signed integers, -128 remains   -128. - For 16-bit signed integers, -32768 remains   -32768. - For 32-bit signed integers, -2147483648   remains -2147483648. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed fixed-point data types. | |

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

This block only supports signed fixed-point data types.

## Version History

**Introduced before R2006a**
