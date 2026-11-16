---
type: simulink-block
title: 'Descriptor State-Space'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Continuous'
documentation_page: 'descriptorstatespace'
documentation_source_path: 'slref/descriptorstatespace.html'
language: zh-CN
chinese_source: official
---

# Descriptor State-Space

## 端口

### 输入

### **Input 1** — 输入信号 标量 | 向量

隐式系统的实值标量或向量输入信号。输入信号数据类型必须为 `double`。对于向量输入信号，信号宽度必须与系统的 *B* 和 *D* 矩阵中的列数相匹配。

在以下情况下，此端口具有直接馈通：

- 将 **Direct Feedthrough** 参数设置为 **True**。
- 您将**直接馈通**参数设置为**自动**，软件就会确定该模块具有直接馈通。

**数据类型:** `double`
### 输出

### **Output 1** — 输出信号 标量 | 向量

隐式系统的输出信号。

**数据类型:** `double`

## 参数

### **E** — 隐式系统的质量矩阵 *E* `1` (默认) | 标量 | 矩阵

将质量矩阵 *E* 指定为实值 *n*×*n* 矩阵，其中 *n* 是系统中的状态数。质量矩阵可以是奇异的或非奇异的，并且必须具有与 *A* 矩阵相同的维度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `E` |
| **值:** | `'1'` (默认) | scalar | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",E="[1 2;3 4]")`

### **A** — 隐式系统的 *A* 矩阵 `1` (默认) | 标量 | 矩阵

将矩阵 *A* 指定为实值 *n*×*n* 矩阵，其中 *n* 是系统中的状态数。矩阵 *A* 必须具有与质量矩阵 *E* 相同的维度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `A` |
| **值:** | `'1'` (默认) | scalar | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",A="[1 2;3 4]")`

### **B** — 隐式系统的 *B* 矩阵 `1` (默认) | 标量 | 向量 | 矩阵

将矩阵 *B* 指定为实值 *n*×*m* 矩阵，其中 *n* 是系统中的状态数，*m* 是输入数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `B` |
| **值:** | `'1'` (默认) | scalar | vector | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",B="[1 2]")`

### **C** — 隐式系统的 *C* 矩阵 `1` (默认) | 标量 | 向量 | 矩阵

将矩阵 *C* 指定为实值 *r*×*n* 矩阵，其中 *n* 是系统中的状态数，*r* 是输出数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `C` |
| **值:** | `'1'` (默认) | scalar | vector | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",C="[3 4]")`

### **D** — 隐式系统的 *D* 矩阵 `1` (默认) | 标量 | 向量 | 矩阵

将矩阵 *D* 指定为实值 *r*×*m* 矩阵，其中 *r* 是系统输出的数量，*m* 是系统输入的数量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `D` |
| **值:** | `'1'` (默认) | scalar | vector | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",D="5")`

### **初始条件** — 初始状态值 `0` (默认) | 标量 | 向量 | 矩阵

指定隐式系统状态的初始值。状态不能具有 `Inf` 或 `NaN` 值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InitialCondition` |
| **值:** | `'0'` (默认) | scalar | vector | matrix |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",InitialCondition="[2 3]")`

### **直接馈通** — 输出信号值是否取决于输入信号值 **True** (默认) | **False** | **自动**

指定隐式系统是否具有直接馈通。当一个或多个输出信号的值直接取决于一个或多个输入信号的值时，该模块具有直接馈通。

- **True** - 输出信号值直接取决于输入信号值。
- **False** - 输出信号值不直接依赖于输入信号值。
- **自动** - 软件根据指定矩阵的特性确定输出信号值是否直接取决于输入信号值。

当此模块实现具有 500 个以上连续状态的系统时，将此参数指定为 **True** 或 **False** 可以加快仿真速度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `DirectFeedthrough` |
| **值:** | `'True'` (默认) | `'False'` | `'Auto'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",DirectFeedthrough="False")`

### **线性化为稀疏模型** — 将状态线性化为稀疏矩阵 `on` (默认) | `off`

对于 Simulink® Control Design™ 工作流，在线性化过程中将 Descriptor State-Space 模块表示的系统线性化为稀疏模型。

禁用此参数可将系统线性化为非稀疏显式状态空间模型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LinearizeToSparse` |
| **值:** | `'off'` (默认) | `'on'` |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",LinearizeToSparse="on")`

### **绝对容差** — 用于计算模块状态的绝对容差 `auto` (默认) | 标量 | 向量

变步长求解器在选择步长时使用绝对和相对容差来确定状态计算中的误差是否可接受。

要从**绝对容差**配置参数继承绝对容差，请将此参数值指定为 `auto` 或 `-1`。

要为此模块指定一个绝对容差来覆盖为**绝对容差**配置参数指定的值，请执行以下操作：

- 输入用于计算所有模块状态的正实数标量值。
- 输入实数向量，其维度与模块的连续状态的维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `AbsoluteTolerance` |
| **值:** | `'auto'` (默认) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Descriptor State-Space",AbsoluteTolerance="-1")`

### **状态名称(例如，'position')** — 用于为各状态指定唯一名称的选项 `''` (默认) | 字符向量 | 字符向量元胞数组 | MATLAB® 变量 | ...

使用此参数可选择为此模块的状态指定名称。您指定的名称仅应用于此模块的状态。

- 要使用默认状态名称，请将此字段留空 (`''`)。
- 要为单个状态分配单个名称，请输入名称并用引号引起来。例如，要命名单一状态 `position`，请输入 `'position'`。
- 要为多个状态指定名称，请将此参数值指定为字符向量元胞数组。元胞数组中的每个名称必须唯一。例如，要指定名称 `a`、`b` 和 `c`，请输入 `{'a','b','c'}`。
- 要使用 MATLAB 变量指定名称，请输入不带引号的变量名称。例如，要使用变量 `names` 来指定状态名称，请输入 `names`。

您指定的名称数量可以少于模块中的状态数量。在这种情况下，状态名称用于多个状态，状态的数量必须能够被状态名称的数量均分。例如，当您为具有四个状态的模块指定两个名称时，第一个名称用于前两个状态，第二个名称用于后两个状态。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ContinuousStateAttributes` |
| **值:** | `''` (默认) | valid MATLAB variable name |
| **数据类型:** | `char` | `string` | `cell` |

**示例:** `set_param("MyModel/Descriptor State-Space",ContinuousStateAttributes={'position','velocity'})`

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否a` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

*在 R2024b 之前的版本中: Descriptor State-Space 模块仅支持 C 代码生成，不支持 C++ 代码生成。*

考虑使用模型离散化器将连续模块（例如 Descriptor State-Space 模块）映射到支持代码生成的离散等效块。要打开模型离散化器，请在 **App** 选项卡中的**控制系统**下点击**模型离散化器**。

## 版本历史

**在 R2018b 中推出**

### R2024b: C++ 代码生成支持

您可以为具有质量矩阵的隐式系统生成 C++ 代码，例如使用 Descriptor State-Space 模块实现的系统。使用 **Language (Simulink Coder)** 参数指定代码生成的语言。

## 描述

模型线性隐式系统

Descriptor State-Space 模块允许您对隐式形式 Ex˙=Ax+Bu 描述的线性隐式系统进行建模，其中 *E* 是系统的质量矩阵。当 *E* 非奇异且因此可逆时，您可以用显式形式 x˙=E−1Ax+E−1Bu 描述系统，并使用 State-Space 模块对系统进行建模。

当质量矩阵 *E* 为奇异矩阵时，方程不包含系统中一个或多个因变量的导数。系统中的因变量也称为*代数变量*，含有代数变量的微分方程称为*微分代数方程*。由微分代数方程描述的系统的状态空间表示具有以下形式：

Ex˙=Ax+Buy=Cx+Du

其中：

- *x* 是状态向量。
- *u* 是输入向量。
- *y* 是输出向量。
