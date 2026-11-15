---
type: simulink-block
title: 'Fixed-Point State-Space'
family: additional-math-and-discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Additional Math and Discrete'
documentation_page: 'fixedpointstatespace'
---

# Fixed-Point State-Space

Implement discrete-time state space

## 中文

实现离散时间状态空间

### 所属库

Simulink / Additional Math & Discrete / Additional Discrete

### 描述

Fixed-Point State-Space 模块实现由以下方程所描述的系统：

y(n)=Cx(n)+Du(n)

x(n+1)=Ax(n)+Bu(n)

其中 *u* 表示输入，*x* 表示状态，*y* 表示输出。这两个方程具有相同的数据类型。

- **A** 必须是 *n*×*n* 矩阵，其中 *n* 是状态的数量。
- **B** 必须是 *n*×*m* 矩阵，其中 *m* 是输入数目。
- **C** 必须是 *r*×*n* 矩阵，其中 *r* 是输出数目。
- **D** 必须是 *r*×*m* 矩阵。

此外：

- 状态 x 必须为 *n*×1 向量。
- 输入 u 必须为 *m*×1 向量。
- 输出 y 必须为 *r*×1 向量。

此模块接受一个输入并生成一个输出。输入向量的宽度是 **B** 和 **D** 矩阵中的列数。输出向量的宽度是 **C** 和 **D** 矩阵中的行数。要定义初始状态向量，请使用**初始条件**参数。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入向量，其宽度等于 **B** 和 **D** 矩阵中的列数。有关详细信息，请参阅描述。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，其宽度等于 **C** 和 **D** 矩阵中的行数。有关详细信息，请参阅描述。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **状态矩阵 A** — 状态矩阵 `[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]` (默认) | 标量 | 向量 | 矩阵

将状态矩阵指定为实数值或复数值 *n*×*n* 矩阵，其中 *n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`A` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]'` |

#### **输入矩阵 B** — 输入的列向量 `[ 1; 0; 0]` (默认) | 标量 | 向量 | 矩阵

将输入的列向量指定为实数或复数值 *n*×*m* 矩阵，其中 *n* 是状态的数量，而 *m* 是输入的个数。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`B` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值**：`'[ 1; 0; 0]'` |

#### **输出矩阵 C** — 输出的列向量 `[0.0184 0.0024 0.0055]` (默认) | 标量 | 向量 | 矩阵

将输出的列向量指定为实数值或复数值 *r*×*n* 矩阵，其中 *r* 是输出的个数，而 *n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`C` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值**：`'[0.0184 0.0024 0.0055]'` |

#### **直接馈通矩阵 D** — 直接馈通矩阵 `[0.0033]` (默认) | 标量 | 向量 | 矩阵

将直接馈通矩阵指定为实数值或复数值 *r*×*m* 矩阵，其中 *r* 为输出的个数，*m* 为输入的个数。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`D` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值**：`'[0.0033]'` |

#### **状态的初始条件** — 初始状态向量 `0.0` (默认) | 标量 | 向量 | 矩阵

指定状态的初始条件。

##### 限制

初始状态不能为 `inf` 或 `NaN`。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0.0'` |

此外，还可以使用 `X0`。

#### 信号属性

#### **内部计算的数据类型** — 内部计算的数据类型 `fixdt('double')` (默认) | 数据类型字符串

指定模块用于内部计算的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InternalDataType` |
| **类型：**字符向量 |
| **值：**数据类型字符串 |
| **默认值**：`'fixdt('double')'` |

#### **状态方程 AX+BU 的定标** — 状态方程的定标 `2^0` (默认) | 标量

指定状态方程 **AX+BU** 的定标。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateEqScaling` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值**：`'2^0'` |

#### **输出方程 CX+DU 的定标** — 输出方程的定标 `2^0` (默认) | 标量

指定输出方程 **CX+DU** 的定标。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputEqScaling` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值**：`'2^0'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此选项将锁定此模块的输出数据类型设置，从而防止通过定点工具和定点顾问进行更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

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
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 建议不要将此模块用于布尔信号。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| 常规 | |
| --- | --- |
| **SharingFactor** | 使用 SharingFactor 指定要映射到单个共享资源的功能等效的资源的数量。默认值为 0。请参阅Resource Sharing (HDL Coder)。 |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Additional Math & Discrete / Additional Discrete

## Description

The Fixed-Point State-Space block implements the system described by

y(n)=Cx(n)+Du(n)

x(n+1)=Ax(n)+Bu(n)

where *u* is the input, *x* is the state, and
*y* is the output. Both equations have the same data type.

- **A** must be an *n*-by-*n*
  matrix, where *n* is the number of states.
- **B** must be an *n*-by-*m*
  matrix, where *m* is the number of inputs.
- **C** must be an *r*-by-*n*
  matrix, where *r* is the number of outputs.
- **D** must be an *r*-by-*m*
  matrix.

In addition:

- The state x must be an *n*-by-1 vector.
- The input u must be an *m*-by-1 vector.
- The output y must be an *r*-by-1 vector.

The block accepts one input and generates one output. The width of the input vector is
the number of columns in the **B** and **D** matrices.
The width of the output vector is the number of rows in the **C** and
**D** matrices. To define the initial state vector, use the
**Initial conditions** parameter.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input vector, where the width equals the number of columns in the
**B** and **D** matrices. For more
information, see Description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal, with width equal to the number of rows in the
**C** and **D** matrices. For more
information, see Description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **State Matrix A** — Matrix of states `[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]` (default) | scalar | vector | matrix

Specify the matrix of states as an
*n*-by-*n* matrix of real or
complex values, where *n* is the number of states. For
more information on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]'` |

### **Input Matrix B** — Column vector of inputs `[ 1; 0; 0]` (default) | scalar | vector | matrix

Specify the column vector of inputs as an
*n*-by-*m* matrix of real or
complex values, where *n* is the number of states, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[ 1; 0; 0]'` |

### **Output Matrix C** — Column vector of outputs `[0.0184 0.0024 0.0055]` (default) | scalar | vector | matrix

Specify the column vector of outputs as an
*r*-by-*n* matrix of real or
complex values, where *r* is the number of outputs, and
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[0.0184 0.0024 0.0055]'` |

### **Direct Feedthrough Matrix D** — Matrix for direct feedthrough `[0.0033]` (default) | scalar | vector | matrix

Specify the matrix for direct feedthrough as an
*r*-by-*m* matrix of real or
complex values, where *r* is the number of outputs, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'[0.0033]'` |

### **Initial condition for state** — Initial state vector `0.0` (default) | scalar | vector | matrix

Specify the initial condition for the state.

#### Limitations

The initial state cannot be `inf` or
`NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'0.0'` |

Alternatively, use `X0`.

### Signal Attributes

### **Data type for internal calculations** — Data type for internal calculations `fixdt('double')` (default) | data type string

Specify the data type the block uses for internal calculations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalDataType` |
| **Type:** character vector |
| **Values:** data type string |
| **Default:** `'fixdt('double')'` |

### **Scaling for State Equation AX+BU** — Scaling for state equations `2^0` (default) | scalar

Specify the scaling for the state equation
**AX+BU**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateEqScaling` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'2^0'` |

### **Scaling for Output Equation CX+DU** — Scaling for output equations `2^0` (default) | scalar

Specify the scaling for the output equation
**CX+DU**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputEqScaling` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'2^0'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock the output data type setting of this block against changes
by the Fixed-Point Tool and the Fixed-Point Advisor. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LockScale` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

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
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block is not recommended for use with Boolean signals. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| General | |
| --- | --- |
| **SharingFactor** | Use SharingFactor to specify the number of functionally equivalent resources to map to a single shared resource. The default is 0. See Resource Sharing (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
