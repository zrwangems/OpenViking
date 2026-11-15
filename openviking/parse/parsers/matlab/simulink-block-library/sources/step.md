---
type: simulink-block
title: 'Step'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'step'
---

# Step

Generate step function

## 中文

生成阶跃函数

### 所属库

Simulink / Sources

### 描述

Step 可在指定时间在两个定义的电平之间进行阶跃。如果仿真时间小于**阶跃时间**参数值，模块输出将为**初始值**参数值。如果仿真时间大于或等于**阶跃时间**，输出则为**终值**参数值。

在标量扩展后，数值模块参数必须具有相同的维度。如果**将向量参数解释为一维向量**选项设置为 off，模块将输出与参数具有相同维度和维数的信号。如果**将向量参数解释为一维向量**选项设置为 on 且数值参数为行或列向量（即，单行或单列二维数组），模块将输出向量（一维数组）信号。否则，模块将输出与参数具有相同维度和维数的信号。

### 端口

#### 输出

#### **Port\_1** — 输出阶跃信号 标量 | 向量

由参数**阶跃时间**、**初始值**和**终值**定义的输出阶跃函数信号。

**数据类型:** `double` | `single`

### 参数

#### **阶跃时间** — 阶跃发生的时间 `1` (默认) | 标量

以秒为单位指定输出从**初始值**参数跳到**终值**参数的时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`Time` |
| **类型**：字符向量 |
| **值：**`'1'` | 实数值或复数值标量、向量或矩阵 |
| **默认值**：`'1'` |

#### **初始值** — 阶跃之前的输出值 `0` (默认) | 标量

指定仿真时间达到**阶跃时间**参数时的模块输出。

##### 编程用法

|  |
| --- |
| **模块参数**：`Before` |
| **类型**：字符向量 |
| **值：**`'1'` | 实数值或复数值标量、向量或矩阵 |
| **默认值**：`'0'` |

#### **终值** — 阶跃之后的输出值 `1` (默认) | 标量

指定仿真时间达到并超过**阶跃时间**参数时的模块输出。

##### 编程用法

|  |
| --- |
| **模块参数**：`After` |
| **类型**：字符向量 |
| **值：**`'1'` | 实数值或复数值标量、向量或矩阵 |
| **默认值**：`'1'` |

#### **采样时间** — 采样率 `0` (默认) | 标量

指定阶跃的采样率。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### **输出数据类型** — 输出数据类型 **double** (默认) | **继承: 通过反向传播继承** | **single** | `<data type expression>`

输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当选择 **Inherit: Inherit via back propagation** 时，模块使用驱动模块的数据类型。

点击**显示数据类型助手**按钮  以显示**数据类型助手**，帮助您设置数据类型属性。有关详细信息，请参阅 。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | <数据类型表达式> |
| **默认值：**`'double'` |

#### **模式** — 数据类型的类别 `Inherit` (默认) | `Built in` | `Expression`

数据类型的类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

点击**显示数据类型助手**按钮将启用此参数。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink® 从信号的上下文（即：从 Simulink 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮，并将**模式**设置为**内置**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Step block provides a step between two definable levels at a specified
time. If the simulation time is less than the **Step time** parameter
value, the block's output is the **Initial value** parameter value. For
simulation time greater than or equal to the **Step time**, the output
is the **Final value** parameter value.

The numeric block parameters must be of the same dimensions after scalar expansion. If the
**Interpret vector parameters as 1-D** option is off, the block
outputs a signal of the same dimensions and dimensionality as the parameters. If the
**Interpret vector parameters as 1-D** option is on and the numeric
parameters are row or column vectors (that is, single-row or column 2-D arrays), the
block outputs a vector (1-D array) signal. Otherwise, the block outputs a signal of the
same dimensionality and dimensions as the parameters.

## Ports

### Output

### **Port\_1** — Output step signal scalar | vector

Output step function signal defined by the parameters **Step time**,
**Initial value**, and **Final
value**.

**Data Types:** `double` | `single`

## Parameters

### **Step time** — Time when step occurs `1` (default) | scalar

Specify the time, in seconds, when the output jumps from the
**Initial value** parameter to the **Final
value** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Time` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'1'` |

### **Initial value** — Output value before step `0` (default) | scalar

Specify the block output until the simulation time reaches the
**Step time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Before` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'0'` |

### **Final value** — Output value after step `1` (default) | scalar

Specify the block output when the simulation time reaches and exceeds the
**Step time** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `After` |
| **Type**: character vector |
| **Values:** `'1'` | real- or complex-valued scalar, vector, or matrix |
| **Default**: `'1'` |

### **Sample time** — Sample rate `0` (default) | scalar

Specify the sample rate of step. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if the
**Constant value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector. For example,
  the block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **Output data type** — Output data type `double` (default) | `Inherit: Inherit via back propagation` | `single` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via back
propagation`, the block uses the data type of the driving
block.

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | <data type expression> |
| **Default:** `'double'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`,
`Built in`, or `Expression`. For more
information on using this parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink® inherits the data type override setting from its
  context, that is, from the block, `Simulink.Signal`
  object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type override setting of its
  context.

For more information, see Specify Data Types Using Data Type Assistant
in the Simulink
documentation.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set the **Mode**
to `Built in`.

#### Tips

The ability to turn off data type override for an individual data type
provides greater control over the data types in your model when you
apply data type override. For example, you can use this option to ensure
that data types meet the requirements of downstream blocks regardless of
the data type override setting.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced before R2006a**
