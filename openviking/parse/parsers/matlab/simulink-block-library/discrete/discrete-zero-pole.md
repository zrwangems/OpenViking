---
type: simulink-block
title: 'Discrete Zero-Pole'
family: discrete
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretezeropole'
---

# Discrete Zero-Pole

Model system defined by zeros and poles of discrete transfer function

## 中文

对由离散传递函数的零极点定义的系统建模

### 所属库

Simulink / Discrete

### 描述

Discrete Zero-Pole 模块对由 *z* 域传递函数的零点、极点和增益定义的离散系统建模。此模块假定传递函数具有以下形式：

H(z)=KZ(z)P(z)=K(z−Z1)(z−Z2)...(z−Zm)(z−P1)(z−P2)...(z−Pn),

其中 *Z* 表示零点向量，*P* 表示极点向量，*K* 表示增益。极点数必须大于或等于零点数 (*n* ≥ *m*)。如果零极点为复数，它们必须是复共轭对组。

该模块根据参数的指定方式显示传递函数。有关详细信息，请参阅 Zero-Pole。

#### 为单输出系统建模

对于单输出系统，模块的输入和输出是标量时域信号。要为此系统建模，请执行以下操作：

1. 在**零点**字段中输入传递函数的零点向量。
2. 在**极点**字段中输入传递函数的极点向量。
3. 在**增益**字段中输入传递函数的 1×1 增益向量。

#### 为多输出系统建模

对于多输出系统，模块输入为标量，输出为向量，其中每个元素都是系统的一个输出。要为此系统建模，请执行以下操作：

1. 在**零点**字段中输入全零矩阵。

   此矩阵的每一*列*包含一个传递函数（将系统输入与一个输出相关联）的零点。
2. 在**极点**字段中输入对系统的所有传递函数都通用的极点向量。
3. 在**增益**字段中输入增益向量。

   每个元素代表对应的传递函数在**零点**中的增益。

输出向量的每个元素对应于**零点**中的一列。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量

输入信号，指定为实数值标量。

**数据类型:** `single` | `double`
#### 输出

#### **Port\_1** — 离散系统模型 标量 | 向量

由离散传递函数的零点、极点和增益定义的系统的模型。输出的宽度等于**零点**矩阵中的列数，如果**零点**是向量，则为 1。

**数据类型:** `single` | `double`

### 参数

#### 常设

#### **零点** — 零点矩阵 `[1]` (默认) | 向量 | 矩阵

指定全零向量或全零矩阵。零点数量必须小于或等于极点数量。如果零极点为复数，它们必须是复共轭对组。

- 对于单输出系统，输入传递函数的零点向量。
- 对于多输出系统，输入矩阵。矩阵的每一列包含一个传递函数（将系统输入与一个输出相关联）的零点。

##### 编程用法

|  |
| --- |
| **模块参数**：`Zeros` |
| **类型：**字符向量 |
| **值：**向量 |
| **默认值：**`'[1]'` |

#### **极点** — 极点向量 `[0 0.5]` (默认) | 向量

指定极点向量。极点数必须大于或等于零点数。如果零极点为复数，它们必须是复共轭对组。

- 对于单输出系统，输入传递函数的极点向量。
- 对于多输出系统，输入对系统的所有传递函数通用的极点向量。

##### 编程用法

|  |
| --- |
| **模块参数**：`Poles` |
| **类型：**字符向量 |
| **值：**向量 |
| **默认值：**`'[0 0.5]'` |

#### **增益** — 增益值 `1` (默认) | 标量 | 向量

指定由增益值构成的向量。

- 对于单输出系统，输入一个标量或 1×1 向量作为传递函数的增益。
- 对于多输出系统，输入增益向量。每个元素代表对应的传递函数在**零点**中的增益。

##### 编程用法

|  |
| --- |
| **模块参数**：`Gain` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'1'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` | 标量 | 向量

指定采样时间间隔。有关详细信息，请参阅指定采样时间。

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

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discrete

## Description

The Discrete Zero-Pole block models a discrete system defined by the zeros,
poles, and gain of a *z*-domain transfer function. This block assumes
that the transfer function has the following form:

H(z)=KZ(z)P(z)=K(z−Z1)(z−Z2)...(z−Zm)(z−P1)(z−P2)...(z−Pn),

where *Z* represents the zeros vector, *P* the poles
vector, and *K* the gain. The number of poles must be greater than or
equal to the number of zeros (*n* ≥ *m*). If
the poles and zeros are complex, they must be complex conjugate pairs.

The block displays the transfer function depending on how the
parameters are specified. See Zero-Pole for more information.

### Modeling a Single-Output System

For a single-output system, the input and the output of the block are scalar
time-domain signals. To model this system:

1. Enter a vector for the zeros of the transfer function in the
   **Zeros** field.
2. Enter a vector for the poles of the transfer function in the
   **Poles** field.
3. Enter a 1-by-1 vector for the gain of the transfer function in the
   **Gain** field.

### Modeling a Multiple-Output System

For a multiple-output system, the block input is a scalar and the output is a
vector, where each element is an output of the system. To model this system:

1. Enter a matrix of zeros in the **Zeros** field.

   Each *column* of this matrix contains the zeros of a
   transfer function that relates the system input to one of the
   outputs.
2. Enter a vector for the poles common to all transfer functions of the
   system in the **Poles** field.
3. Enter a vector of gains in the **Gain** field.

   Each element is the gain of the corresponding transfer function in
   **Zeros**.

Each element of the output vector corresponds to a column in
**Zeros**.

## Ports

### Input

### **Port\_1** — Input signal scalar

Input signal specified as a real-valued scalar.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Model of discrete system scalar | vector

Model of system as defined by zeros, poles, and gain of discrete
transfer function. The width of the output is equal to the number of
columns in the **Zeros** matrix, or one if
**Zeros** is a vector.

**Data Types:** `single` | `double`

## Parameters

### Main

### **Zeros** — Matrix of zeros `[1]` (default) | vector | matrix

Specify the vector or matrix of zeros. The number of zeros must be
less than or equal to the number of poles. If the poles and zeros are
complex, they must be complex conjugate pairs.

- For a single-output system, enter a vector for the zeros of
  the transfer function.
- For a multiple-output system, enter a matrix. Each column of
  the matrix contains the zeros of a transfer function that
  relates the system input to one of the outputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Zeros` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[1]'` |

### **Poles** — Vector of poles `[0 0.5]` (default) | vector

Specify the vector of poles. The number of poles must be greater than or equal to the
number of zeros. If the poles and zeros are complex, they must be
complex conjugate pairs.

- For a single-output system, enter a vector for the poles of
  the transfer function.
- For a multiple-output system, enter a vector for the poles
  common to all transfer functions of the system.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Poles` |
| **Type:** character vector |
| **Values:** vector |
| **Default:** `'[0 0.5]'` |

### **Gain** — Gain value `1` (default) | scalar | vector

Specify vector of gain values.

- For a single-output system, enter a scalar or 1-by-1 vector
  for the gain of the transfer function.
- For a multiple-output system, enter a vector of gains. Each
  element is the gain of the corresponding transfer function in
  **Zeros**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Gain` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` | scalar | vector

Specify the time interval between samples. For more information, see
Specifying Sample Time.

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

Generated code relies on `memcpy` or `memset` functions
(`string.h`) under certain conditions.

## Version History

**Introduced before R2006a**
