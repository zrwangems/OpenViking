---
type: simulink-block
title: 'Transfer Fcn Direct Form II Time Varying'
family: additional-math-and-discrete
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'transferfcndirectformiitimevarying'
---

# Transfer Fcn Direct Form II Time Varying

Implement time varying Direct Form II realization of transfer function

## 中文

实现传递函数的时变 Direct Form II 实现

### 库

Simulink / Additional Math & Discrete / Additional Discrete

### 描述

Transfer Fcn Direct Form II Time Varying 模块实现指定传递函数的 Direct Form II 实现。该模块仅支持单输入单输出 (SISO) 传递函数。

标记为 **Den No Lead** 的输入信号包含传递函数的分母系数。完整分母的首项系数为 1，但它从输入信号中排除。例如，要使用分母 `[1 -1.7 0.72]`，请指定值为 `[-1.7 0.72]` 的信号。标记为 **Num** 的输入信号包含分子系数。分子系数和分母系数的数据类型可以不同，但分子向量的长度和完整分母向量的长度必须相同。如果需要，用零填充分子向量。

该模块自动选择输出、系数以及任何临时变量的数据类型和定标。

### 端口

#### 输入

#### **u** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Num** — 分子系数 标量 | 向量

传递函数的分子系数，指定为标量或向量。

#### 依赖关系

分子系数和分母系数的数据类型可以不同，但分子向量的长度和完整分母向量的长度必须相同。如果需要，用零填充分子向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Den No Lead** — 分母系数 标量 | 向量

传递函数的分母系数，指定为标量或向量，不含首项系数 1。完整分母的首项系数为 1，但它从输入信号中排除。

**示例：** 对于分母系数 `[1 -1.7 0.72]`，指定值为 `[-1.7 0.72]` 的信号。

#### 依赖关系

分子系数和分母系数的数据类型可以不同，但分子向量的长度和完整分母向量的长度必须相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### 输出

#### **y** — 输出信号 标量 | 向量

输出信号，指定为标量或向量。

该模块自动选择输出以及任何临时变量的数据类型和定标。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **Initial condition** — 初始条件 `0.0`（默认）| scalar

将初始条件指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** character vector |
| **取值：** scalar |
| **默认：** `'0.0'` |

#### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **取值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

#### **Saturate to max or min when overflows occur** — 溢出操作方法 `off`（默认）| `on`

选中此复选框时，溢出会饱和到该数据类型能表示的最大值或最小值。否则，溢出会回绕。

选中此复选框时，饱和会应用于该模块中的每一个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测出何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** character vector |
| **取值：** `'off' | 'on'` |
| **默认：** `'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将此模块与 Boolean 信号一起使用。 | |

### 扩展功能

#### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成器不会在生成的代码中显式地对构成非原子掩码子系统模块的原始模块进行分组。这种灵活性允许更高效的代码生成。在某些情况下，可以通过配置掩码子系统模块以原子单元方式执行（选择 **Treat as atomic unit** 选项）来实现分组。

#### PLC 代码生成

使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

#### 定点转换

使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Additional Math & Discrete / Additional Discrete

## Description

The Transfer Fcn Direct Form II Time Varying block implements a Direct Form
II realization of the specified transfer function. The block supports only single
input-single output (SISO) transfer functions.

The input signal labeled **Den No Lead** contains the denominator
coefficients of the transfer function. The full denominator has a leading coefficient of
one, but it is excluded from the input signal. For example, to use a denominator of
`[1 -1.7 0.72]`, specify a signal with the value `[-1.7
0.72]`. The input signal labeled **Num** contains the
numerator coefficients. The data types of the numerator and denominator coefficients can
be different, but the length of the numerator vector and the full denominator vector
must be the same. Pad the numerator vector with zeros, if needed.

The block automatically selects the data types and scalings of the output, the coefficients, and any temporary variables.

## Ports

### Input

### **u** — Input signal scalar | vector

Input signal, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Num** — Numerator coefficients scalar | vector

Numerator coefficients of the transfer function, specified as a scalar
or vector.

#### Dependencies

The data types of the numerator and denominator coefficients can
be different, but the length of the numerator vector and the full
denominator vector must be the same. Pad the numerator vector with
zeros, if needed.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Den No Lead** — Denominator coefficients scalar | vector

Denominator coefficients of the transfer function, specified as a
scalar or vector, without the leading coefficient of one. The full
denominator has a leading coefficient of one, but it is excluded from
the input signal.

**Example:** For a denominator coefficient of `[1 -1.7
0.72]`, specify a signal with value `[-1.7
0.72]`.

#### Dependencies

The data types of the numerator and denominator coefficients can
be different, but the length of the numerator vector and the full
denominator vector must be the same.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **y** — Output signal scalar | vector

Output signal, specified as a scalar or vector.

The block automatically selects the data types and scalings of the
output and any temporary variables.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Initial condition** — Initial condition `0.0` (default) | scalar

Specify the initial condition as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vinit` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0.0'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.
For more information, see Rounding Modes (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block is not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The code generator does not explicitly group primitive blocks
that constitute a nonatomic masked subsystem block in the generated code. This
flexibility allows for more efficient code generation. In certain cases, you can
achieve grouping by configuring the masked subsystem block to execute as an atomic
unit by selecting the **Treat as atomic unit** option.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
