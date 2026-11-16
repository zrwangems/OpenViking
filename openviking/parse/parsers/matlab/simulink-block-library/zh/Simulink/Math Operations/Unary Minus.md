---
type: simulink-block
title: 'Unary Minus'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'unaryminus'
documentation_source_path: '../simulink/slref/unaryminus.html'
language: zh-CN
chinese_source: official
---

# Unary Minus

## 端口

### 输入

### **Port\_1** — 要求反的信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Port\_1** — 输入信号的求反 标量 | 向量 | 矩阵 | N 维数组

输入信号的求反。输出具有与输入相同的数据类型和维度。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`

## 参数

### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

选中可实现整数溢出饱和。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

对于有符号整数数据类型，最负值的一元减法无法用该数据类型表示。在这种情况下，由**对整数溢出进行饱和处理**复选框控制模块的行为：

| 参数设置 | 模块行为 | 示例 |
| --- | --- | --- |
| **对整数溢出进行饱和处理** = `on` | 值饱和处理为该整数数据类型的最大正值 | - 对于 8 位有符号整数，-128 对应为 127。 - 对于 16 位有符号整数，-32768 对应为 32767。 - 对于 32 位有符号整数，-2147483648 对应为 2147483647。 |
| **对整数溢出进行饱和处理** = `off` | 值绕回到该整数数据类型的最小负值 | - 对于 8 位有符号整数，-128 依然是 -128。 - 对于 16 位有符号整数，-32768 依然是 -32768。 - 对于 32 位有符号整数，-2147483648 依然是 -2147483648。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

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

此模块仅支持有符号定点数据类型。

## 版本历史

**在 R2006a 之前推出**

## 描述

对输入求反

Unary Minus 模块对输入进行求反。
