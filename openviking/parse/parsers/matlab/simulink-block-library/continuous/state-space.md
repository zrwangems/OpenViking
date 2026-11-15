---
type: simulink-block
title: 'State-Space'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'statespace'
---

# State-Space

Implement linear state-space system

## 中文

实现线性状态空间系统

### 所属库

Simulink / Continuous

### 描述

State-Space 模块可实现具有您定义的如下行为的系统：

x˙=Ax+Buy=Cx+Dux|t=t0=x0,

其中 *x* 是状态向量，*u* 是输入向量，*y* 是输出向量，*x0* 是状态向量的初始条件。A、B、C、D 矩阵可以指定为稀疏矩阵或稠密矩阵。矩阵系数必须具有以下特征：

- *A* 必须是 *n*×*n* 矩阵，其中 *n* 是状态的数量。
- *B* 必须是 *n*×*m* 矩阵，其中 *m* 是输入数目。
- *C* 必须是 *r*×*n* 矩阵，其中 *r* 是输出数目。
- *D* 必须是 *r*×*m* 矩阵。

一般情况下，模块有一个输入端口和一个输出端口。C 或 D 矩阵中的行数与输出端口的宽度相同。B 或 D 矩阵中的列数与输入端口的宽度相同。如果您要建立不带任何输入端口的自治线性系统模型，请将 B 和 D 设置为空矩阵。在这种情况下，模块相当于没有输入端口但有一个输出端口的源模块，并实现以下系统：

x˙=Axy=Cxx|t=t0=x0.

Simulink® 软件可将包含零值的矩阵转换为稀疏矩阵，以提高乘法运算的效率。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

`double` 类型的实数值输入向量，其宽度等于 **B** 和 **D** 矩阵中的列数。有关详细信息，请参阅描述。

**数据类型:** `double`
#### 输出

#### **Port\_1** — 输出向量 标量 | 向量

数据类型为 `double` 的实数值输出向量，其宽度等于 **C** 和 **D** 矩阵中的行数。有关详细信息，请参阅描述。

**数据类型:** `double`

### 参数

#### **A** — 矩阵系数，A `1` (默认) | 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 `A` 指定为实数值 *n*×*n* 矩阵，其中 *n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数：**`A` |
| **类型：**字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 | 稀疏矩阵 |
| **默认值：**`'1'` |

#### **B** — 矩阵系数，B `1` (默认) | 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 `B` 指定为实数值 *n*×*m* 矩阵，其中 *n* 是状态的数量，*m* 是输入数目。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数：**`B` |
| **类型：**字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 | 稀疏矩阵 |
| **默认值：**`'1'` |

#### **C** — 矩阵系数 C `1` (默认) | 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 **C** 指定为实数值 *r*×*n* 矩阵，其中 *r* 是输出数目，*n* 是状态的数量。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数：**`C` |
| **类型：**字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 | 稀疏矩阵 |
| **默认值：**`'1'` |

#### **D** — 矩阵系数 D `1` (默认) | 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 **D** 指定为实数值 *r*×*m* 矩阵，其中 *r* 是输出数目，*m* 是输入数目。有关矩阵系数的详细信息，请参阅描述。

##### 编程用法

|  |
| --- |
| **模块参数：**`D` |
| **类型：**字符向量、字符串 |
| **值：** 标量 | 向量 | 矩阵 | 稀疏矩阵 |
| **默认值：**`'1'` |

#### **初始条件** — 初始状态向量 `0` (默认) | 标量 | 向量

指定初始状态向量。

##### 限制

此模块的初始条件不能为 `inf` 或 `NaN`。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialCondition` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

此外，还可以使用 `X0`。

#### **参数可调性** — 选择模块参数的可调表示 `Auto` (默认) | `Optimized` | `Unconstrained`

使用 Simulink Compiler™ 的加速仿真模式和部署仿真的状态空间矩阵（A、B、C 和 D）的可调性级别。当设置为**自动**时，Simulink 会选择适当的参数可调性级别。

对于稀疏矩阵系数，将参数设置为**优化**允许对非零元素进行调整，同时保持非零元素的模式和数量不变。将此参数设置为**无约束**则允许对所有元素进行调整，前提是非零元素的数量保持不变，即您可以更改稀疏矩阵的模式。

对于稠密矩阵系数，选择**优化**允许对所有矩阵元素进行调整，前提是矩阵中最初指定的非零元素数量保持不变。将此参数设置为**无约束**允许对所有矩阵元素进行全部调整。

**注意**

当 D = 0 时，要调整模块的 **D** 矩阵，则必须启用**允许最初指定为零的 D 矩阵具有非零值**参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`ParameterTunability` |
| **类型：**字符向量 | 字符串 |
| **值**：`'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **默认值：**`'Auto'` |

#### **允许最初指定为零的 D 矩阵具有非零值** — 当 D = 0 时允许调整 D 矩阵 `off` (默认) | `on`

启用此参数将支持对 **D** 进行调整，即使 D = 0 也是如此。

**注意**

启用此参数会启用 State-Space 模块的直接馈通。

##### 编程用法

|  |
| --- |
| **模块参数：**`AllowTunableDMatrix` |
| **类型：**字符向量 | 字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **绝对容差** — 用于计算模块状态的绝对容差 `auto` (默认) | 标量 | 向量

变步长求解器在选择步长时使用绝对和相对容差来确定状态计算中的误差是否可接受。

要从**绝对容差**配置参数继承绝对容差，请将此参数值指定为 `auto` 或 `-1`。

要为此模块指定一个绝对容差来覆盖为**绝对容差**配置参数指定的值，请执行以下操作：

- 输入用于计算所有模块状态的正实数标量值。
- 输入实数向量，其维度与模块的连续状态的维度匹配。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `AbsoluteTolerance` |
| **值:** | `'auto'` (默认) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",AbsoluteTolerance="-1")`

#### **状态名称(例如，'position')** — 用于为各状态指定唯一名称的选项 `''` (默认) | 字符向量 | 字符向量元胞数组 | MATLAB® 变量 | ...

使用此参数可选择为此模块的状态指定名称。您指定的名称仅应用于此模块的状态。

- 要使用默认状态名称，请将此字段留空 (`''`)。
- 要为单个状态分配单个名称，请输入名称并用引号引起来。例如，要命名单一状态 `position`，请输入 `'position'`。
- 要为多个状态指定名称，请将此参数值指定为字符向量元胞数组。元胞数组中的每个名称必须唯一。例如，要指定名称 `a`、`b` 和 `c`，请输入 `{'a','b','c'}`。
- 要使用 MATLAB 变量指定名称，请输入不带引号的变量名称。例如，要使用变量 `names` 来指定状态名称，请输入 `names`。

您指定的名称数量可以少于模块中的状态数量。在这种情况下，状态名称用于多个状态，状态的数量必须能够被状态名称的数量均分。例如，当您为具有四个状态的模块指定两个名称时，第一个名称用于前两个状态，第二个名称用于后两个状态。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ContinuousStateAttributes` |
| **值:** | `''` (默认) | valid MATLAB variable name |
| **数据类型:** | `char` | `string` | `cell` |

**示例:** `set_param("MyModel/Descriptor State-Space",ContinuousStateAttributes={'position','velocity'})`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Continuous

## Description

The State-Space block implements a system whose behavior you
define as

x˙=Ax+Buy=Cx+Dux|t=t0=x0,

where *x* is the state vector, *u* is the input vector,
*y* is the output vector, and *x0* is the initial
condition of the state vector. The A, B, C, and D matrices can be specified as either
sparse matrices or dense matrices. The matrix coefficients must have these
characteristics:

- *A* must be an *n*-by-*n*
  matrix, where *n* is the number of states.
- *B* must be an *n*-by-*m*
  matrix, where *m* is the number of inputs.
- *C* must be an *r*-by-*n*
  matrix, where *r* is the number of outputs.
- *D* must be an *r*-by-*m*
  matrix.

In general, the block has one input port and one output port. The number of rows in C or D matrix is the same as the width of the output port. The number of columns in the B or D matrix are the same as the width of the input port. If you want to model an autonomous linear system with no inputs, set the B and D matrices to empty. In this case, the block acts as a source block with no input port and one output port, and implements the following system:

x˙=Axy=Cxx|t=t0=x0.

Simulink® software converts a matrix containing zeros to a sparse matrix for efficient multiplication.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Real-valued input vector of type `double`, where the
width equals the number of columns in the **B** and
**D** matrices. For more information, see Description.

**Data Types:** `double`
### Output

### **Port\_1** — Output vector scalar | vector

Real-valued output vector of data type `double`, with
width equal to the number of rows in the **C** and
**D** matrices. For more information, see Description.

**Data Types:** `double`

## Parameters

### **A** — Matrix coefficient, A `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient `A`, as a real-valued
*n*-by-*n* matrix, where
*n* is the number of states. For more information on
the matrix coefficients, see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `A` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **B** — Matrix coefficient, B `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient `B`, as a real-valued
*n*-by-*m* matrix, where
*n* is the number of states and *m* is
the number of inputs. For more information on the matrix coefficients, see
Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `B` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **C** — Matrix coefficient, C `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient **C** as a real-valued
*r*-by-*n* matrix, where
*r* is the number of outputs and *n*
is the number of states. For more information on the matrix coefficients,
see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `C` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **D** — Matrix coefficient, D `1` (default) | scalar | vector | matrix | sparse matrix

Specify the matrix coefficient **D** as a real-valued
*r*-by-*m* matrix, where
*r* is the number of outputs and *m*
is the number of inputs. For more information on the matrix coefficients,
see Description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `D` |
| **Type:** character vector, string |
| **Values:** scalar | vector | matrix | sparse matrix |
| **Default:** `'1'` |

### **Initial conditions** — Initial state vector `0` (default) | scalar | vector

Specify the initial state vector.

#### Limitations

The initial conditions of this block cannot be `inf`
or `NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialCondition` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

Alternatively, use
`X0`.

### **Parameter tunability** — Choose tunable representation of block parameters `Auto` (default) | `Optimized` | `Unconstrained`

Tunability level of the state-space matrices (A,B,C, and D ) for accelerated simulation
modes and deployed simulations using the Simulink
Compiler™. When set to `Auto`, Simulink chooses the appropriate parameter tunability level.

For sparse matrix coefficients, set the parameter to
`Optimized` to allow tunability of non-zero
elements while keeping the pattern and number of non-zero elements constant.
Set this parameter to `Unconstrained` to allow all
elements to be tunable, so long as the number of non-zero elements is kept
constant, that is, you can change the pattern of the sparse matrix.

For dense matrix coefficients, select `Optimized` to allow
tunability of all matrix elements, provided the number of non-zero elements
initially specified in the matrix is kept constant. Set this parameter to
`Unconstrained` to allow full tunability of all
matrix elements.

**Note**

To tune the **D** matrix of the block when D = 0, you
must enable the **Allow non-zero values for D matrix initially
specified as zero** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ParameterTunability` |
| **Type:** character vector | string |
| **Values:** `'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **Default:** `'Auto'` |

### **Allow non-zero values for D matrix initially specified as zero** — Allow tunability of D matrix when D = 0 `off` (default) | `on`

Enable this parameter to support tunability of **D** even when D = 0.

**Note**

Enabling this parameter enables direct feedthrough for the
State-Space block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowTunableDMatrix` |
| **Type:** character vector | string |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Absolute tolerance** — Absolute tolerance for computing block states `auto` (default) | scalar | vector

Variable-step solvers use absolute and relative tolerances when choosing the step size to
determine whether the error in state calculations is acceptable.

To inherit the absolute tolerance from the **Absolute tolerance** configuration parameter, specify this parameter
value as `auto` or `-1`.

To specify an absolute tolerance for this block that overrides the value specified for
the **Absolute tolerance** configuration parameter:

- Enter a real, positive scalar value to use to compute all block
  states.
- Enter a real vector with dimensions that match the dimensions of the
  continuous states for the block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AbsoluteTolerance` |
| **Values:** | `'auto'` (default) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",AbsoluteTolerance="-1")`

### **State Name (e.g., 'position')** — Option to assign unique names to states `''` (default) | character vector | cell array of character vectors | MATLAB® variable | ...

Use this parameter to optionally assign names to the states of this block. The
names you assign apply only to the states of this block.

- To use default state names, leave this field blank
  (`''`).
- To assign a single name to a single state, enter the
  name between quotes. For example, to name a single
  state `position`, enter
  `'position'`.
- To assign names to multiple states, specify this
  parameter value as a cell array of character
  vectors. Each name in the cell array must be unique.
  For example, to assign the names
  `a`, `b`, and
  `c`, enter
  `{'a','b','c'}`.
- To specify the names using a MATLAB variable, enter the name of the
  variable without quotes. For example, to use the
  variable `names` to specify the
  state names, enter `names`.

You can specify a number of names that is less than the number of states in
the block. In this case, the state names are used for multiple states, and
the number of states must divide evenly into the number of state names. For
example, when you specify two names for a block that has four states, the
first name is used for the first two states, and the second name is used for
the last two states.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ContinuousStateAttributes` |
| **Values:** | `''` (default) | valid MATLAB variable name |
| **Data Types:** | `char` | `string` | `cell` |

**Example:** `set_param("MyModel/Descriptor
State-Space",ContinuousStateAttributes={'position','velocity'})`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into discrete equivalents that support production code generation. To start the Model Discretizer, in the Simulink Editor, on the **Apps** tab, under **Apps**, under **Control Systems**, click **Model Discretizer**. One exception is the Second-Order Integrator block because, for this block, the Model Discretizer produces an approximate discretization.

## Version History

**Introduced before R2006a**
