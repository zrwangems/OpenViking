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
chinese_source: worker-translation
---

# Descriptor State-Space

## 端口

### 输入

### **Input 1** — 输入信号 标量 | 向量

隐式系统的实值标量或向量输入信号。输入信号的数据类型必须为 `double`。对于向量输入信号，信号宽度必须与系统中 *B* 和 *D* 矩阵的列数匹配。

此端口在以下情况下具有直接馈通：

- 将 **直接馈通** 参数设置为 `True`。
- 将 **直接馈通** 参数设置为 `Auto`，并且软件确定该模块具有直接馈通。

**数据类型：** `double`

### 输出

### **Output 1** — 输出信号 标量 | 向量

隐式系统的输出信号。

**数据类型：** `double`

## 参数

### **E** — 隐式系统的质量矩阵 *E* `1`（默认） | 标量 | 矩阵

将质量矩阵 *E* 指定为实值 *n*×*n* 矩阵，其中 *n* 是系统中的状态数。质量矩阵可以奇异或非奇异，并且必须与 *A* 矩阵具有相同的维度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `E` |
| **值：** | `'1'`（默认） | 标量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",E="[1 2;3 4]")`

### **A** — 隐式系统的 *A* 矩阵 `1`（默认） | 标量 | 矩阵

将矩阵 *A* 指定为实值 *n*×*n* 矩阵，其中 *n* 是系统中的状态数。矩阵 *A* 必须与质量矩阵 *E* 具有相同的维度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `A` |
| **值：** | `'1'`（默认） | 标量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",A="[1 2;3 4]")`

### **B** — 隐式系统的 *B* 矩阵 `1`（默认） | 标量 | 向量 | 矩阵

将矩阵 *B* 指定为实值 *n*×*m* 矩阵，其中 *n* 是系统中的状态数，*m* 是输入数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `B` |
| **值：** | `'1'`（默认） | 标量 | 向量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",B="[1 2]")`

### **C** — 隐式系统的 *C* 矩阵 `1`（默认） | 标量 | 向量 | 矩阵

将矩阵 *C* 指定为实值 *r*×*n* 矩阵，其中 *n* 是系统中的状态数，*r* 是输出数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `C` |
| **值：** | `'1'`（默认） | 标量 | 向量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",C="[3 4]")`

### **D** — 隐式系统的 *D* 矩阵 `1`（默认） | 标量 | 向量 | 矩阵

将矩阵 *D* 指定为实值 *r*×*m* 矩阵，其中 *r* 是系统输出数，*m* 是系统输入数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `D` |
| **值：** | `'1'`（默认） | 标量 | 向量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",D="5")`

### **初始条件** — 初始状态值 `0`（默认） | 标量 | 向量 | 矩阵

指定隐式系统状态的初始值。状态不能具有 `Inf` 或 `NaN` 值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialCondition` |
| **值：** | `'0'`（默认） | 标量 | 向量 | 矩阵 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",InitialCondition="[2 3]")`

### **直接馈通** — 输出信号值是否取决于输入信号值 `True`（默认） | `False` | `Auto`

指定隐式系统是否具有直接馈通。当一个或多个输出信号的值直接取决于一个或多个输入信号的值时，模块具有直接馈通。

- `True` — 输出信号值直接取决于输入信号值。
- `False` — 输出信号值不直接取决于输入信号值。
- `Auto` — 软件根据指定矩阵的特性确定输出信号值是否直接取决于输入信号值。

当此模块实现具有超过 500 个连续状态的系统时，将此参数指定为 `True` 或 `False` 可以加快仿真。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DirectFeedthrough` |
| **值：** | `'True'`（默认） | `'False'` | `'Auto'` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",DirectFeedthrough="False")`

### **线性化为稀疏模型** — 将状态线性化为稀疏矩阵 `on`（默认） | `off`

对于 Simulink® Control Design™ 工作流，在线性化期间将由 Descriptor State-Space 模块表示的系统线性化为稀疏模型。

禁用此参数可将系统线性化为非稀疏显式状态空间模型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LinearizeToSparse` |
| **值：** | `'off'`（默认） | `'on'` |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",LinearizeToSparse="on")`

### **绝对容差** — 用于计算模块状态的绝对容差 `auto`（默认） | 标量 | 向量

可变步长求解器在选择步长时使用绝对容差和相对容差，以确定状态计算中的误差是否可接受。

要从 **绝对容差** 配置参数继承绝对容差，请将此参数值指定为 `auto` 或 `-1`。

要为此模块指定一个绝对容差以覆盖为 **绝对容差** 配置参数指定的值：

- 输入一个实正标量值，用于计算所有模块状态。
- 输入一个实向量，其维度与此模块连续状态的维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AbsoluteTolerance` |
| **值：** | `'auto'`（默认） | `'-1'` | 正实标量数值 | 正实标量数值向量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("MyModel/Descriptor State-Space",AbsoluteTolerance="-1")`

### **状态名称（例如，'position'）** — 为状态分配唯一名称的选项 `''`（默认） | 字符向量 | 字符向量元胞数组 | MATLAB® 变量 | ...

使用此参数可选择性地为此模块的状态分配名称。您分配的名称仅适用于此模块的状态。

- 要使用默认状态名称，请将此字段留空（`''`）。
- 要为单个状态分配单个名称，请在引号之间输入该名称。例如，要将单个状态命名为 `position`，请输入 `'position'`。
- 要为多个状态分配名称，请将此参数值指定为字符向量元胞数组。元胞数组中的每个名称必须唯一。例如，要分配名称 `a`、`b` 和 `c`，请输入 `{'a','b','c'}`。
- 要使用 MATLAB 变量指定名称，请输入变量名称（不带引号）。例如，要使用变量 `names` 指定状态名称，请输入 `names`。

您可以指定的名称数量少于模块中的状态数。在这种情况下，状态名称将用于多个状态，并且状态数必须能被状态名称数整除。例如，当您为一个具有四个状态的模块指定两个名称时，第一个名称用于前两个状态，第二个名称用于后两个状态。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ContinuousStateAttributes` |
| **值：** | `''`（默认） | 有效的 MATLAB 变量名称 |
| **数据类型：** | `char` | `string` | `cell` |

**示例：** `set_param("MyModel/Descriptor State-Space",ContinuousStateAttributes={'position','velocity'})`

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `noa` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

*R2024b 之前：Descriptor State-Space 模块仅支持 C 代码生成，不支持 C++ 代码生成。*

考虑使用 Model Discretizer 将 Descriptor State-Space 模块等连续模块映射到支持代码生成的离散等效模块。要打开 Model Discretizer，请在 **应用** 选项卡中的 **控制系统** 下，点击 **Model Discretizer**。

## 版本历史

**R2018b 中引入**

### R2024b：支持 C++ 代码生成

您可以为具有质量矩阵的隐式系统（例如使用 Descriptor State-Space 模块实现的系统）生成 C++ 代码。使用 **Language (Simulink Coder)** 参数指定代码生成的语言。

## 描述

对线性隐式系统建模

Descriptor State-Space 模块允许您对以隐式形式 Ex˙=Ax+Bu 描述的线性隐式系统进行建模，其中 *E* 是系统的质量矩阵。当 *E* 非奇异因而可逆时，您可以将系统描述为显式形式 x˙=E−1Ax+E−1Bu，并使用 State-Space 模块对该系统进行建模。

当质量矩阵 *E* 奇异时，方程不包含系统中一个或多个因变量的导数。系统中的因变量也称为*代数变量*，包含代数变量的微分方程称为*微分代数方程*。由微分代数方程描述的系统，其状态空间表示具有以下形式：

Ex˙=Ax+Buy=Cx+Du

其中：

- *x* 是状态向量。
- *u* 是输入向量。
- *y* 是输出向量。
