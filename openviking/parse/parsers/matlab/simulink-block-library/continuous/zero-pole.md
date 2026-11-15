---
type: simulink-block
title: 'Zero-Pole'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'zeropole'
---

# Zero-Pole

Model system using zero-pole-gain transfer function

## 中文

使用零极点增益传递函数进行系统建模

### 所属库

Simulink / Continuous

### 描述

Zero-Pole 模块可以通过指定零点、极点和拉普拉斯域传递函数增益定义的系统进行建模。您可以使用此模块对单输入单输出 (SISO) 和单输入多输出 (SIMO) 系统进行建模。

Zero-Pole 模块有以下要求：

- 传递函数的形式必须为

  H(s)=KZ(s)P(s)=K(s−Z(1))(s−Z(2))…(s−Z(m))(s−P(1))(s−P(2))…(s−P(n)),

  其中 *Z* 表示零点，*P* 表示极点，*K* 表示传递函数的增益。
- 极点数必须大于或等于零点数。
- 复极点和复零点必须为复共轭对组。
- 对于多输出系统，所有传递函数必须具有相同的极点。零点的值可以不同，但每个传递函数的零点数必须相同。

**提示**

要对一个多输出系统建模（其中传递函数具有不同的零点数或者每个传递函数只有一个零点），请使用多个 Zero-Pole 模块。

#### 对单输出系统建模

一个单输出系统具有标量时域输入和输出信号。要对这种类型的系统建模，请执行以下操作：

1. 在**零点**字段中输入传递函数的零点向量。
2. 在**极点**字段中输入传递函数的极点向量。
3. 在**增益**字段中输入传递函数的增益标量。

#### 对多输出系统建模

一个多输出系统具有一个标量时域输入信号和一个向量时域输出信号。向量输出中的每个元素均为该系统的一个输出。要对这种类型的系统建模，请执行以下操作：

1. 在**零点**字段中输入全零矩阵。

   矩阵的每一列包含一个传递函数（将系统输入信号与输出信号中的一个元素相关联）的零点。
2. 在**极点**字段中输入对系统的所有传递函数都通用的极点向量。
3. 在**增益**字段中输入增益向量。

   每个元素代表对应的传递函数在零点矩阵中的增益。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量

系统的标量时域输入信号。

**数据类型:** `double`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

系统的输出建模为一个零极点增益传递函数，以标量或向量信号形式提供。

- 对单输出系统建模时，模块生成标量时域信号。
- 当对多输出系统建模时，模块生成向量，其中向量的每个元素均为系统的输出。

**数据类型:** `double`

### 参数

#### **零点** — 零点矩阵 `[1]` (默认) | 向量 | 矩阵

定义零点矩阵。

- 对于单输出系统，输入传递函数的零点向量。
- 对于多输出系统，输入矩阵。此矩阵的每列包含一个传递函数的零点，该传递函数将系统输入与输出向量的一个元素相关联。
- 要对不带零点的系统建模，请输入 `[]`。

##### 编程用法

|  |
| --- |
| **模块参数：**`Zeros` |
| **类型：**字符串 | 字符向量 |
| **值：**向量 | 矩阵 |
| **默认值：**`'[1]'` |

#### **极点** — 极点向量 `[0 -1]` (默认) | 向量

定义极点向量。

- 对于单输出系统，输入传递函数的极点向量。
- 对于多输出系统，输入对系统的所有传递函数通用的极点向量。

##### 编程用法

|  |
| --- |
| **模块参数：**`Poles` |
| **类型：**字符串 | 字符向量 |
| **值：**向量 |
| **默认值：**`'[0 -1]'` |

#### **增益** — 增益向量 `[1]` (默认) | 向量

定义增益向量。

- 对于单输出系统，输入传递函数的 1×1 增益向量。
- 对于多输出系统，输入增益向量。每个元素代表对应的传递函数在零点矩阵中的增益。

##### 编程用法

|  |
| --- |
| **模块参数：**`Gain` |
| **类型：**字符串 | 字符向量 |
| **值：**向量 |
| **默认值：**`'[1]'` |

#### **参数可调性** — 代码中模块参数的可调表示 `Auto` (默认) | `Optimized` | `Unconstrained`

指定零点、极点和增益在加速和快速加速仿真以及使用 Simulink® Compiler™ 部署的仿真中是否可调。

- **自动** - 软件确定参数可调性的级别。
- **优化** - 软件为加速仿真、快速加速仿真和部署的仿真生成零点、极点和增益的优化表示。优化表示中的零点、极点和增益值不可调。
- **无约束** - **零点**、**极点**和**增益**参数的值在加速仿真、快速加速仿真和部署的仿真之间可调。

##### 编程用法

|  |
| --- |
| **模块参数：**`ParameterTunability` |
| **类型：**字符串 | 字符向量 |
| **值**：`'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **默认值：**`'Auto'` |

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

由于嵌入式系统中常见的资源限制以及对速度和内存的限制，不建议用于生产代码。生成的代码可以包含：

- 内存的动态分配和释放
- 递归
- 额外的内存开销
- 差异很大的执行时间

虽然代码在功能上有效并且在资源丰富的环境中可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，**在控制系统**下，点击**模型离散化器**。

对于 Second-Order Integrator 模块，模型离散化器产生近似离散化。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Continuous

## Description

The Zero-Pole block models a system that you define by specifying the zeros,
poles, and gain of a Laplace-domain transfer function. You can use this block to model
single-input single-output (SISO) and single-input multiple-output (SIMO)
systems.

The Zero-Pole block has these requirements:

- The transfer function must have the form

  H(s)=KZ(s)P(s)=K(s−Z(1))(s−Z(2))…(s−Z(m))(s−P(1))(s−P(2))…(s−P(n)),

  where *Z* represents the zeros, *P*
  represents the poles, and *K* represents the gain of the
  transfer function.
- The number of poles must be greater than or equal to the number of
  zeros.
- Complex poles and zeros must be complex-conjugate pairs.
- For a multiple-output system, all transfer functions must have the same
  poles. The zeros can differ in value, but the number of zeros for each
  transfer function must be the same.

**Tip**

To model a multiple-output system in which the transfer functions have different
numbers of zeros or a single zero each, use multiple Zero-Pole
blocks.

### Model Single-Output Systems

A single-output system has scalar time-domain input and output signals. To model this type
of system:

1. Enter a vector for the zeros of the transfer function
   in the **Zeros** field.
2. Enter a vector for the poles of the transfer function
   in the **Poles** field.
3. Enter a scalar for the gain of the transfer function in the
   **Gain** field.

### Model Multiple-Output Systems

A multiple-output system has a scalar time-domain input signal and a vector time-domain
output signal. Each element in the vector output is an output of the system. To
model this type of system:

1. Enter a matrix of zeros in the **Zeros** field.

   Each column of the matrix contains the zeros of a transfer function that relates the
   system input signal to one of the elements in the output signal.
2. Enter a vector for the poles common to all transfer
   functions of the system in the **Poles** field.
3. Enter a vector of gains in the **Gain** field.

   Each element is the gain of the corresponding transfer function in the zeros
   matrix.

## Ports

### Input

### **Port\_1** — Input signal scalar

The scalar time-domain input signal for the system.

**Data Types:** `double`
### Output

### **Port\_1** — Output signal scalar | vector

Output of the system modeled as a zero-pole-gain transfer function,
provided as a scalar or vector signal.

- When modeling a single-output system, the block produces a
  scalar time-domain signal.
- When modeling a multiple-output system, the block produces a
  vector, where each element of the vector is an output of the
  system.

**Data Types:** `double`

## Parameters

### **Zeros** — Matrix of zeros `[1]` (default) | vector | matrix

Define the matrix of zeros.

- For a single-output system, enter a vector for the zeros of the
  transfer function.
- For a multiple-output system, enter a matrix. Each column of this
  matrix contains the zeros for a transfer function that relates the
  system input to an element of the output vector.
- To model a system without zeros, enter
  `[]`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Zeros` |
| **Type:** string | character vector |
| **Value:** vector | matrix |
| **Default:** `'[1]'` |

### **Poles** — Vector of poles `[0 -1]` (default) | vector

Define the vector of poles.

- For a single-output system, enter a vector for the poles of the
  transfer function.
- For a multiple-output system, enter a vector for the poles common
  to all transfer functions of the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Poles` |
| **Type:** string | character vector |
| **Value:** vector |
| **Default:** `'[0 -1]'` |

### **Gain** — Vector of gains `[1]` (default) | vector

Define the vector of gains.

- For a single-output system, enter a 1-by-1 vector for the gain of
  the transfer function.
- For a multiple-output system, enter a vector of gains. Each
  element is the gain of the corresponding transfer function in the
  zeros matrix.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Gain` |
| **Type:** string | character vector |
| **Value:** vector |
| **Default:** `'[1]'` |

### **Parameter tunability** — Tunable representation of block parameters in code `Auto` (default) | `Optimized` | `Unconstrained`

Specify whether the zeros, poles, and gains are tunable in accelerator and rapid
accelerator simulations and in simulations deployed using Simulink®
Compiler™.

- `Auto` — The software determines the
  level of parameter tunability.
- `Optimized` — The software generates an
  optimized representation of the zeros, poles, and gain for
  accelerator, rapid accelerator, and deployed simulations. The zeros,
  poles, and gain values in the optimized representation are not
  tunable.
- `Unconstrained` — The values of the
  **Zeros**, **Poles**, and
  **Gain** parameters are tunable between
  accelerator, rapid accelerator, and deployed simulations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ParameterTunability` |
| **Type:** string | character vector |
| **Values:** `'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **Default:** `'Auto'` |

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

Not recommended for production code, due to resource limits and restrictions on speed and
memory often found in embedded systems. The generated code can contain:

- Dynamic allocation and freeing of memory
- Recursion
- Additional memory overhead
- Widely-varying execution times

While the code is functionally valid and acceptable in resource-rich environments,
smaller embedded targets often cannot support such code.

In general, consider using the Model Discretizer to map continuous blocks to discrete
equivalents that support production code generation. To start the Model Discretizer,
in the Simulink Editor, on the **Apps** tab, under **Control
Systems**, click **Model Discretizer**.

For the Second-Order Integrator block, the Model Discretizer
produces an approximate discretization.

## Version History

**Introduced before R2006a**
