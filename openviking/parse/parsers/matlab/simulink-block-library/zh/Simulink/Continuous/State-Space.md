---
type: simulink-block
title: 'State-Space'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Linear'
documentation_page: 'statespace'
documentation_source_path: 'slref/statespace.html'
language: zh-CN
chinese_source: worker-translation
---

# State-Space

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

类型为 `double` 的实值输入向量，其宽度等于 **B** 和 **D** 矩阵的列数。有关详细信息，请参阅描述。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出向量 标量 | 向量

数据类型为 `double` 的实值输出向量，其宽度等于 **C** 和 **D** 矩阵的行数。有关详细信息，请参阅描述。

**数据类型：** `double`

## 参数

### **A** — 矩阵系数 A `1`（默认）| 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 `A` 指定为实值 *n*×*n* 矩阵，其中 *n* 是状态数。有关矩阵系数的详细信息，请参阅描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`A` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix | sparse matrix |
| **默认值**：`'1'` |

### **B** — 矩阵系数 B `1`（默认）| 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 `B` 指定为实值 *n*×*m* 矩阵，其中 *n* 是状态数，*m* 是输入数。有关矩阵系数的详细信息，请参阅描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`B` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix | sparse matrix |
| **默认值**：`'1'` |

### **C** — 矩阵系数 C `1`（默认）| 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 **C** 指定为实值 *r*×*n* 矩阵，其中 *r* 是输出数，*n* 是状态数。有关矩阵系数的详细信息，请参阅描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`C` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix | sparse matrix |
| **默认值**：`'1'` |

### **D** — 矩阵系数 D `1`（默认）| 标量 | 向量 | 矩阵 | 稀疏矩阵

将矩阵系数 **D** 指定为实值 *r*×*m* 矩阵，其中 *r* 是输出数，*m* 是输入数。有关矩阵系数的详细信息，请参阅描述。

#### 编程使用

|  |
| --- |
| **模块参数**：`D` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix | sparse matrix |
| **默认值**：`'1'` |

### **Initial conditions** — 初始状态向量 `0`（默认）| 标量 | 向量

指定初始状态向量。

#### 限制

此模块的初始条件不能为 `inf` 或 `NaN`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：character vector, string |
| **值**：scalar | vector |
| **默认值**：`'0'` |

或者，使用 `X0`。

### **Parameter tunability** — 选择模块参数的可调表示 `Auto`（默认）| `Optimized` | `Unconstrained`

状态空间矩阵（A、B、C 和 D）在加速仿真模式以及使用 Simulink Compiler™ 部署的仿真中的可调级别。当设置为 `Auto` 时，Simulink 会选择适当的参数可调级别。

对于稀疏矩阵系数，将参数设置为 `Optimized` 以允许非零元素可调，同时保持非零元素的模式和数量不变。将此参数设置为 `Unconstrained` 以允许所有元素可调，只要非零元素的数量保持不变，即您可以更改稀疏矩阵的模式。

对于稠密矩阵系数，选择 `Optimized` 以允许所有矩阵元素可调，前提是矩阵中最初指定的非零元素数量保持不变。将此参数设置为 `Unconstrained` 以允许所有矩阵元素完全可调。

**注意**

要在 D = 0 时调整模块的 **D** 矩阵，必须启用 **Allow non-zero values for D matrix initially specified as zero** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ParameterTunability` |
| **类型**：character vector | string |
| **值**：`'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **默认值**：`'Auto'` |

### **Allow non-zero values for D matrix initially specified as zero** — 当 D = 0 时允许 D 矩阵可调 `off`（默认）| `on`

启用此参数以支持 **D** 的可调性，即使 D = 0。

**注意**

启用此参数会为 State-Space 模块启用直接馈通。

#### 编程使用

|  |
| --- |
| **模块参数**：`AllowTunableDMatrix` |
| **类型**：character vector | string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Absolute tolerance** — 计算模块状态的绝对容差 `auto`（默认）| 标量 | 向量

变步长求解器在选择步长时使用绝对容差和相对容差来确定状态计算中的误差是否可接受。

要从 **Absolute tolerance** 配置参数继承绝对容差，请将此参数值指定为 `auto` 或 `-1`。

要为该模块指定覆盖 **Absolute tolerance** 配置参数所指定值的绝对容差：

- 输入一个实正标量值，用于计算所有模块状态。
- 输入一个实向量，其维度与模块连续状态的维度匹配。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AbsoluteTolerance` |
| **值**：| `'auto'` (default) | `'-1'` | positive real scalar number | vector of positive real scalar numbers |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",AbsoluteTolerance="-1")`

### **State Name (e.g., 'position')** — 为状态分配唯一名称的选项 `''`（默认）| 字符向量 | 字符向量元胞数组 | MATLAB® 变量 | ...

使用此参数可选地为该模块的状态分配名称。您分配的名称仅适用于该模块的状态。

- 要使用默认状态名称，请将此字段留空（`''`）。
- 要为单个状态分配单个名称，请在引号之间输入名称。例如，要将单个状态命名为 `position`，请输入 `'position'`。
- 要为多个状态分配名称，请将此参数值指定为字符向量元胞数组。元胞数组中的每个名称必须唯一。例如，要分配名称 `a`、`b` 和 `c`，请输入 `{'a','b','c'}`。
- 要使用 MATLAB 变量指定名称，请输入变量名（不带引号）。例如，要使用变量 `names` 指定状态名称，请输入 `names`。

您可以指定的名称数量少于模块中的状态数。在这种情况下，状态名称将用于多个状态，并且状态数必须能被状态名称数整除。例如，当您为一个具有四个状态的模块指定两个名称时，第一个名称用于前两个状态，第二个名称用于后两个状态。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ContinuousStateAttributes` |
| **值**：| `''` (default) | valid MATLAB variable name |
| **Data Types:** | `char` | `string` | `cell` |

**Example:** `set_param("MyModel/Descriptor
State-Space",ContinuousStateAttributes={'position','velocity'})`

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产质量代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。

通常，考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，请在 Simulink 编辑器的 **Apps** 选项卡上，在 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 会生成近似离散化。

## 版本历史

**在 R2006a 之前推出**

## 描述

实现线性状态空间系统

State-Space 模块实现一个系统，其行为定义为

x˙=Ax+Buy=Cx+Dux|t=t0=x0,

其中 *x* 是状态向量，*u* 是输入向量，*y* 是输出向量，*x0* 是状态向量的初始条件。A、B、C 和 D 矩阵可以指定为稀疏矩阵或稠密矩阵。矩阵系数必须具有以下特征：

- *A* 必须是 *n*×*n* 矩阵，其中 *n* 是状态数。
- *B* 必须是 *n*×*m* 矩阵，其中 *m* 是输入数。
- *C* 必须是 *r*×*n* 矩阵，其中 *r* 是输出数。
- *D* 必须是 *r*×*m* 矩阵。

通常，该模块有一个输入端口和一个输出端口。C 或 D 矩阵的行数与输出端口的宽度相同。B 或 D 矩阵的列数与输入端口的宽度相同。如果您要对没有输入的自治线性系统建模，请将 B 和 D 矩阵设置为空。在这种情况下，该模块充当没有输入端口和一个输出端的源模块，并实现以下系统：

x˙=Axy=Cxx|t=t0=x0.

Simulink® 软件将包含零的矩阵转换为稀疏矩阵，以实现高效乘法。
