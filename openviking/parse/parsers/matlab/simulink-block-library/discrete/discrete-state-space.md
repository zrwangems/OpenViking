---
type: simulink-block
title: 'Discrete State-Space'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretestatespace'
---

# Discrete State-Space

Implement discrete state-space system

## 中文

实现离散状态空间系统

### 所属库

Simulink / Discrete Simulink / Quick Insert / Discrete HDL Coder / RCP and HIL

### 描述

#### 非空矩阵的模块行为

Discrete State-Space 模块实现由以下方程所描述的系统：

x(n+1)=Ax(n)+Bu(n)y(n)=Cx(n)+Du(n),

其中 *u* 表示输入，*x* 表示状态，*y* 表示输出。矩阵系数必须具有这些特征，如下图所示：

- **A** 必须是 *n*×*n* 矩阵，其中 *n* 是状态的数量。
- **B** 必须是 *n*×*m* 矩阵，其中 *m* 是输入数目。
- **C** 必须是 *r*×*n* 矩阵，其中 *r* 是输出数目。
- **D** 必须是 *r*×*m* 矩阵。

此模块接受一个输入并生成一个输出。输入向量的宽度是 **B** 和 **D** 矩阵中的列数。输出向量的宽度是 **C** 和 **D** 矩阵中的行数。要定义初始状态向量，请使用**初始条件**参数。

要为 **A**、**B**、**C**、**D** 或**初始条件**指定全零向量或全零矩阵，请使用 `zeros` 函数。

#### 空矩阵的模块行为

当矩阵 **A**、**B** 和 **C** 为空时（例如 `[]`），模块的功能将变成 `y(n) = Du(n)`。如果**初始条件**向量也为空，模块将使用全零初始状态向量。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

输入向量，其宽度等于 **B** 和 **D** 矩阵中的列数。有关详细信息，请参阅描述。

**提示**

对于整数和定点输入信号，请使用 Fixed-Point State-Space 模块。

**数据类型:** `single` | `double`
#### 输出

#### **Port\_1** — 输出向量 标量 | 向量

输出向量，其宽度等于 **C** 和 **D** 矩阵中的行数。有关详细信息，请参阅描述。

**数据类型:** `single` | `double`

### 参数

#### 常设

#### **A** — 矩阵系数 A `1` (默认) | 标量 | 向量 | 矩阵

将矩阵系数 `A` 指定为实数值 *n*×*n* 矩阵，其中 *n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`A` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'1'` |

#### **B** — 矩阵系数 B `1` (默认) | 标量 | 向量 | 矩阵

将矩阵系数 `B` 指定为实数值 *n*×*m* 矩阵，其中 *n* 是状态的数量，*m* 是输入数目。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`B` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'1'` |

#### **C** — 矩阵系数 C `1` (默认) | 标量 | 向量 | 矩阵

将矩阵系数 **C** 指定为实数值 *r*×*n* 矩阵，其中 *r* 是输出数目，*n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`C` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'1'` |

#### **D** — 矩阵系数 D `1` (默认) | 标量 | 向量 | 矩阵

将矩阵系数 **D** 指定为实数值 *r*×*m* 矩阵，其中 *r* 是输出数目，*m* 是输入数目。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数**：`D` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'1'` |

#### **初始条件** — 初始状态向量 0 (默认) | 标量 | 向量

将初始状态向量指定为标量或向量。初始状态向量不能包括 `inf` 或 `NaN` 值。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

#### 状态属性

#### **状态名称** — 模块状态的唯一名称 `''` (默认) | 字母数字字符串

使用此参数为模块状态指定唯一名称。默认值为 `' '`。如果此字段为空，则表示未指定任何名称。使用此参数时，请记住以下注意事项：

- 有效的标识符以字母或下划线字符开始，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击**应用**时，此参数将启用**状态名称必须解析为 Simulink 信号对象**。

有关详细信息，请参阅模型接口元素的 C 数据代码接口配置 (Simulink Coder)。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateName` |
| **类型：**字符向量 |
| **值：**唯一名称 |
| **默认值：**`''` |

#### **状态名称必须解析为 Simulink 信号对象** — 要求将状态名称解析为信号对象 `off` (默认) | `on`

选中此复选框会要求将状态名称解析为 Simulink® 信号对象。

##### 依赖关系

要启用此参数，请为**状态名称**指定值。仅当将模型配置参数**信号解析**设置为除**无**以外的值时，才会显示此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`string.h`)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discrete Simulink / Quick Insert / Discrete HDL Coder / RCP and HIL

## Description

### Block Behavior for Non-Empty Matrices

The Discrete State-Space block implements the system described by

x(n+1)=Ax(n)+Bu(n)y(n)=Cx(n)+Du(n),

where *u* is the input, *x* is the state, and
*y* is the output. The matrix coefficients must have these
characteristics, as illustrated in the following diagram:

- **A** must be an
  *n*-by-*n* matrix, where
  *n* is the number of states.
- **B** must be an
  *n*-by-*m* matrix, where
  *m* is the number of inputs.
- **C** must be an
  *r*-by-*n* matrix, where
  *r* is the number of outputs.
- **D** must be an
  *r*-by-*m* matrix.

The block accepts one input and generates one output. The width of the input
vector is the number of columns in the **B** and
**D** matrices. The width of the output vector is the number of
rows in the **C** and **D** matrices. To define
the initial state vector, use the **Initial conditions**
parameter.

To specify a vector or matrix of zeros for **A**,
**B**, **C**, **D**, or
**Initial conditions**, use the `zeros` function.

### Block Behavior for Empty Matrices

When the matrices **A**, **B**,
and **C** are empty (for example, `[]`),
the functionality of the block becomes `y(n) = Du(n)`.
If the **Initial conditions** vector is also empty, the block uses an initial state vector of zeros.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input vector, where the width equals the number of columns in the
**B** and **D** matrices. For more
information, see Description.

**Tip**

For integer and fixed-point input signals, use the Fixed-Point
State-Space block.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output vector scalar | vector

Output vector, with width equal to the number of rows in the
**C** and **D** matrices. For
more information, see Description.

**Data Types:** `single` | `double`

## Parameters

### Main

### **A** — Matrix coefficient A `1` (default) | scalar | vector | matrix

Specify the matrix coefficient `A`, as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **B** — Matrix coefficient B `1` (default) | scalar | vector | matrix

Specify the matrix coefficient `B`, as a real-valued
*n*-by-*m* matrix, where
*n* is the number of states, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **C** — Matrix coefficient, C `1` (default) | scalar | vector | matrix

Specify the matrix coefficient **C**, as a real-valued
*r*-by-*n* matrix, where
*r* is the number of outputs, and
*n* is the number of states. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **D** — Matrix coefficient, D `1` (default) | scalar | vector | matrix

Specify the matrix coefficient **D**, as a real-valued
*r*-by-*m* matrix, where
*r* is the number of outputs, and
*m* is the number of inputs. For more information
on the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix |
| **Default:** `'1'` |

### **Initial conditions** — Initial state vector 0 (default) | scalar | vector

Specify the initial state vector as a scalar or vector. The initial state vector cannot
include `inf` or `NaN` values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Sample time (–1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

### State Attributes

### **State name** — Unique name for block state `''` (default) | alphanumeric string

Use this parameter to assign a unique name to the block state. The default is `' '`. When this field is blank, no name is assigned. When using this parameter, remember these considerations:

- A valid identifier starts with an alphabetic or underscore character, followed by alphanumeric or underscore characters.
- The state name applies only to the selected block.

This parameter enables **State name must resolve to Simulink signal object** when you click **Apply**.

For more information, see C Data Code Interface Configuration for Model Interface Elements (Simulink Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateName` |
| **Type:** character vector |
| **Values:** unique name |
| **Default:** `''` |

### **State name must resolve to Simulink signal object** — Require state name resolve to a signal object `off` (default) | `on`

Select this check box to require that the state name resolves to a Simulink® signal object.

#### Dependencies

To enable this parameter, specify a value for **State name**. This parameter appears only if you set the model configuration parameter **Signal resolution** to a value other than `None`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateMustResolveToSignalObject` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on `memcpy` or `memset`
functions (`string.h`) under certain conditions.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

By default, the following HDL block property is available.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**
