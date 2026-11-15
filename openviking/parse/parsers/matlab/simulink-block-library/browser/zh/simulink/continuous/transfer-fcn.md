---
type: simulink-block
title: 'Transfer Fcn'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Continuous'
documentation_page: 'transferfcn'
documentation_source_path: 'slref/transferfcn.html'
language: zh-CN
chinese_source: official
---

# Transfer Fcn

## 端口

### 输入

### **Port\_1** — 输入信号 标量

输入信号，指定为数据类型为 `double` 的标量。

仅当传递函数的分子为 `0` 时，此端口才有直接馈通。

**数据类型:** `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，是数据类型为 `double` 的标量或向量。

- 对于单输出系统，模块的输入和输出是标量时域信号。
- 对于多输出系统，输入为标量，输出为向量，其中每个元素都是系统的一个输出。

**数据类型:** `double`

## 参数

### **分子系数** — 分子系数的向量或矩阵 `[1]` (默认) | 向量 | 矩阵

定义传递函数的分子系数。

- 对于单输出系统，输入传递函数的分子系数向量。
- 对于多输出系统，输入矩阵。此矩阵的每一行包含确定一个模块输出的传递函数的分子系数。

#### 编程用法

|  |
| --- |
| **模块参数：**`Numerator` |
| **类型：**字符向量、字符串 |
| **值：**向量 | 矩阵 |
| **默认值：**`'[1]'` |

### **分母系数** — 分母系数的行向量 `[1 1]` (默认) | 向量

定义分母系数的行向量。

- 对于单输出系统，输入传递函数的分母系数向量。
- 对于多输出系统，输入包含对系统所有传递函数公分母系数的向量。

#### 编程用法

|  |
| --- |
| **模块参数：**`Denominator` |
| **类型：**字符向量 | 字符串 |
| **值：**向量 |
| **默认值：**`'[1 1]'` |

### **参数可调性** — 代码中模块参数的可调表示 `Auto` (默认) | `Optimized` | `Unconstrained`

使用 Simulink Compiler™ 的加速仿真模式和部署仿真的分子和分母系数的可调性级别。将此参数设置为**自动**将允许 Simulink 选择适当的参数可调性级别。

将此参数设置为**优化**可在为加速和部署仿真而生成的代码中生成为实现更好的仿真性能而优化的分子和分母系数表示。

将此参数设置为**无约束**可在为加速和部署仿真而生成的代码中生成分子和分母系数的完全可调（仿真之间）表示。要让 Simulink 确定适当的可调性级别，请选择**自动**。

#### 编程用法

|  |
| --- |
| **模块参数：**`ParameterTunability` |
| **类型：**字符向量、字符串 |
| **值**：`'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **默认值：**`'Auto'` |

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

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

## 版本历史

**在 R2006a 之前推出**

## 描述

将线性系统建模为传递函数

Transfer Fcn 模块通过拉普拉斯域变量 *`s`* 的传递函数为线性系统建模。此模块可为单输入单输出 (SISO) 和单输入多输出 (SIMO) 系统建模。

### 使用此模块的条件

Transfer Fcn 模块假定满足以下条件：

- 传递函数的格式为

  H(s)=y(s)u(s)=num(s)den(s)=num(1)snn−1+num(2)snn−2+…+num(nn)den(1)snd−1+den(2)snd−2+…+den(nd),

  其中 *u* 和 *y* 分别代表系统输入和输出，*nn* 和 *nd* 分别是分子和分母系数。*num(s)* 和 *den(s)* 包含分子和分母的 *s* 降幂系数。
- 分母的阶必须大于或等于分子的阶。
- 对于多输出系统，所有传递函数具有相同的分母，而所有分子具有相同的阶次。

### 为单输出系统建模

对于单输出系统，模块的输入和输出是标量时域信号。要为此系统建模，请执行以下操作：

1. 在**分子系数**字段中输入传递函数的分子系数向量。
2. 在**分母系数**字段中输入传递函数的分母系数向量。

### 为多输出系统建模

对于多输出系统，模块输入为标量，输出为向量，其中每个元素都是系统的一个输出。要为此系统建模，请执行以下操作：

1. 在**分子系数**字段中输入矩阵。

   此矩阵的每一*行*包含确定一个模块输出的传递函数的分子系数。
2. 在**分母系数**字段中输入系统所有传递函数的公分母系数向量。

### 指定初始条件

传递函数描述了输入和输出在拉普拉斯（频率）域中的关系。具体而言，它被定义为零初始条件的系统对冲激输入的响应（输出）的拉普拉斯变换。

传递函数的乘法和除法等运算依赖于零初始状态。例如，您可以将一个复杂的传递函数分解为一系列简单的传递函数。按顺序应用它们可获得与原始传递函数相同的响应。如果其中一个传递函数采用非零初始状态，结果将不正确。而且，一个传递函数有无限多个时域实现，大多数状态并没有任何物理意义。

由于这些原因，Simulink® 将 Transfer Fcn 模块的初始条件预设为零。要指定给定传递函数的初始条件，请使用 `tf2ss` 将传递函数转换为可控制的典型状态空间实现。然后，使用 State-Space 模块。`tf2ss` 实用工具为系统提供了 `A`、`B`、`C` 和 `D` 矩阵。

有关详细信息，请键入 `help tf2ss`，或者参阅 Control System Toolbox™ 文档。

### 传递函数在模块上的显示

Transfer Fcn 模块根据指定的分子和分母参数来显示传递函数。

- 如果这两个参数指定为表达式或向量，该模块将使用 *s* 的幂的指定系数显示传递函数。如果在括号中指定变量，模块将计算变量。

  例如，如果您将**分子系数**参数值指定为 `[3 2 1]`，将**分母系数**参数值指定为 `(den)`，其中 `den` 是工作区变量，其值为 `[7 5 3 1]`，则模块将使用指定的值显示方程。

  Transfer Fcn block that displays the numerator and denominator of the transfer function both as a polynomial function of s.

  **提示**

  当模块大小太小而无法容纳完整的分子或分母时，模块图标将分子显示为 `num(s)`，分母显示为 `den(s)`。

  A Transfer Fcn block that is not wide enough to display the equation.

  如果您要模块显示它实现的传递函数的方程，请通过拖动角来调整模块的大小。

  A pointer is positioned to drag the lower-right corner of the Transfer Fcn block, resizing the block so it is wide enough to display the equation that represents the transfer function.
- 如果将这两个参数指定为变量，模块将显示后跟 `(s)` 的变量名称。

  例如，如果将**分子系数**参数指定为 `num`，将**分母系数**参数指定为 `den`，则模块图标将传递函数的分子显示为 `num(s)`，分母显示为 `den(s)`。

  Transfer Fcn block with the Numerator coefficients parameter specified as num and the Denominator coefficients parameter specified as den.
