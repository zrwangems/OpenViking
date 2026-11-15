---
type: simulink-block
title: 'Transfer Fcn Direct Form II'
family: additional-math-and-discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'transferfcndirectformii'
---

# Transfer Fcn Direct Form II

Implement Direct Form II realization of transfer function

## 中文

实现传递函数的直接 II 型实现

### 所属库

Simulink / Additional Math & Discrete / Additional Discrete

### 描述

Transfer Fcn Direct Form II 模块实现由**分子系数**和**不含首项的分母系数**参数指定的传递函数的直接 II 型实现。该模块仅支持单输入单输出 (SISO) 传递函数。

该模块自动选择输出的数据类型和定标、系数和任何临时变量。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

输出信号，指定为标量或向量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **分子系数** — 分子系数 `[0.2 0.3 0.2]` (默认) | 向量

将分子系数指定为向量。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumCoefVec` |
| **类型：**字符向量 |
| **值：**向量 |
| **默认值：**`'[0.2 0.3 0.2]'` |

#### **不含首项的分母系数** — 分母系数 `[-0.9 0.6]` (默认) | 向量

指定分母系数，不包括首项系数（必须为 `1.0`）。

##### 编程用法

|  |
| --- |
| **模块参数**：`DenCoefVec` |
| **类型：**字符向量 |
| **值：**向量 |
| **默认值：**`'[-0.9 0.6]'` |

#### **初始条件** — 初始条件 `0.0` (默认) | 标量

将初始条件指定为标量。

##### 编程用法

|  |
| --- |
| **模块参数**：`vinit` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0.0'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

#### **发生溢出时饱和处理为最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出将饱和处理为数据类型可表示的最大值或最小值。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

代码生成器不会在生成的代码中将构成非原子封装子系统模块的原始模块显式组合在一起。这种灵活性可以提高代码生成效率。在某些情况下，通过选择**视为原子单元**选项，可以通过将封装子系统模块配置为以原子单元执行来进行组合。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Additional Math & Discrete / Additional Discrete

## Description

The Transfer Fcn Direct Form II block implements a Direct Form II realization
of the transfer function that the **Numerator coefficients** and
**Denominator coefficients excluding lead** parameters specify. The
block supports only single input-single output (SISO) transfer functions.

The block automatically selects the data types and scalings of the output, the coefficients, and any temporary variables.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal, specified as a scalar or vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Numerator coefficients** — Numerator coefficients `[0.2 0.3 0.2]` (default) | vector

Specify the numerator coefficients as a vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumCoefVec` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0.2 0.3 0.2]'` |

### **Denominator coefficients excluding lead** — Denominator coefficient `[-0.9 0.6]` (default) | vector

Specify the denominator coefficients, excluding the leading coefficient,
which must be `1.0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DenCoefVec` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[-0.9 0.6]'` |

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
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

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
