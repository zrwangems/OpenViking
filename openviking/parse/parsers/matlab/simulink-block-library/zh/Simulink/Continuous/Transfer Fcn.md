---
type: simulink-block
title: 'Transfer Fcn'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Linear'
documentation_page: 'transferfcn'
documentation_source_path: 'slref/transferfcn.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Fcn

## 端口

### 输入

### **Port\_1** — 输入信号 标量

输入信号，指定为数据类型为 `double` 的标量。

仅当传递函数的分子为 `0` 时，此端口才具有直接馈通。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，提供为数据类型为 `double` 的标量或向量。

- 对于单输出系统，模块的输入和输出为标量时域信号。
- 对于多输出系统，输入为标量，输出为向量，其中每个元素为系统的一个输出。

**数据类型：** `double`

## 参数

### **Numerator coefficients** — 分子系数向量或矩阵 `[1]`（默认）| 向量 | 矩阵

定义传递函数的分子系数。

- 对于单输出系统，输入传递函数分子系数的向量。
- 对于多输出系统，输入一个矩阵。此矩阵的每一行包含确定模块其中一个输出的传递函数的分子系数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Numerator` |
| **类型**：character vector, string |
| **值**：vector | matrix |
| **默认值**：`'[1]'` |

### **Denominator coefficients** — 分母系数行向量 `[1 1]`（默认）| 向量

定义分母系数的行向量。

- 对于单输出系统，输入传递函数分母系数的向量。
- 对于多输出系统，输入一个向量，其中包含系统所有传递函数共用的分母系数。

#### 编程使用

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型**：character vector | string |
| **值**：vector |
| **默认值**：`'[1 1]'` |

### **Parameter tunability** — 代码中模块参数的可调表示 `Auto`（默认）| `Optimized` | `Unconstrained`

分子和分母系数在加速仿真模式以及使用 Simulink Compiler™ 部署的仿真中的可调性级别。将此参数设置为 `Auto`，以允许 Simulink 选择适当的参数可调性级别。

将此参数设置为 `Optimized`，以在生成的代码中为加速和部署仿真生成针对更好仿真性能优化的分子和分母系数表示。

将此参数设置为 `Unconstrained`，以在生成的代码中为加速和部署仿真生成完全可调（仿真之间）的分子和分母系数表示。若要允许 Simulink 确定适当的可调性级别，请选择 `Auto`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ParameterTunability` |
| **类型**：character vector, string |
| **值**：`'Auto'` | `'Optimized'` | `'Unconstrained'` |
| **默认值**：`'Auto'` |

### **Absolute tolerance** — 计算模块状态的绝对容差 `auto`（默认）| 标量 | 向量

变步长求解器在选择步长时使用绝对容差和相对容差，以确定状态计算中的误差是否可接受。

若要从 **Absolute tolerance** 配置参数继承绝对容差，请将此参数值指定为 `auto` 或 `-1`。

若要为此模块指定覆盖 **Absolute tolerance** 配置参数所指定值的绝对容差：

- 输入用于计算所有模块状态的实正标量值。
- 输入一个实向量，其维度与模块连续状态的维度匹配。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AbsoluteTolerance` |
| **值**：| `'auto'`（默认）| `'-1'` | 正实标量数值 | 正实标量数值向量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Descriptor
State-Space",AbsoluteTolerance="-1")`

### **State Name (e.g., 'position')** — 为状态分配唯一名称的选项 `''`（默认）| 字符向量 | 字符向量元胞数组 | MATLAB® 变量 | ...

使用此参数可选地为该模块的状态分配名称。您分配的名称仅适用于该模块的状态。

- 若要使用默认状态名称，请将此字段留空（`''`）。
- 若要为单个状态分配单个名称，请在引号之间输入名称。例如，若要将单个状态命名为 `position`，请输入 `'position'`。
- 若要为多个状态分配名称，请将此参数值指定为字符向量元胞数组。元胞数组中的每个名称必须唯一。例如，若要分配名称 `a`、`b` 和 `c`，请输入 `{'a','b','c'}`。
- 若要使用 MATLAB 变量指定名称，请输入不带引号的变量名称。例如，若要使用变量 `names` 指定状态名称，请输入 `names`。

您可以指定的名称数量少于模块中的状态数量。在这种情况下，状态名称将用于多个状态，并且状态数量必须能整除状态名称数量。例如，当您为具有四个状态的模块指定两个名称时，第一个名称用于前两个状态，第二个名称用于后两个状态。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ContinuousStateAttributes` |
| **值**：| `''`（默认）| 有效的 MATLAB 变量名称 |
| **Data Types:** | `char` | `string` | `cell` |

**Example:** `set_param("MyModel/Descriptor
State-Space",ContinuousStateAttributes={'position','velocity'})`

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `noa` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 此模块的直接馈通特性取决于模块参数值。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产质量代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然该代码在功能上有效，并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常无法支持此类代码。

通常，请考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。若要启动 Model Discretizer，请在 Simulink Editor 中的 **Apps** 选项卡上，在 **Apps** 下、**Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 会生成近似离散化。

## 版本历史

**在 R2006a 之前推出**

## 描述

将线性系统建模为传递函数

Transfer Fcn 模块通过 Laplace 域变量 *`s`* 的传递函数对线性系统建模。该模块可以对单输入单输出（SISO）和单输入多输出（SIMO）系统建模。

### 使用此模块的条件

Transfer Fcn 模块假定以下条件：

- 传递函数具有以下形式

  H(s)=y(s)u(s)=num(s)den(s)=num(1)snn−1+num(2)snn−2+…+num(nn)den(1)snd−1+den(2)snd−2+…+den(nd),

  其中 *u* 和 *y* 分别是系统输入和输出，*nn* 和 *nd* 分别是分子和分母系数的数量。*num(s)* 和 *den(s)* 包含按 *s* 的降幂排列的分子和分母系数。
- 分母的阶数必须大于或等于分子的阶数。
- 对于多输出系统，所有传递函数具有相同的分母，并且所有分子具有相同的阶数。

### 对单输出系统建模

对于单输出系统，模块的输入和输出为标量时域信号。若要对此系统建模：

1. 在 **Numerator coefficients** 字段中输入传递函数分子系数的向量。
2. 在 **Denominator coefficients** 字段中输入传递函数分母系数的向量。

### 对多输出系统建模

对于多输出系统，模块输入为标量，输出为向量，其中每个元素为系统的一个输出。若要对此系统建模：

1. 在 **Numerator coefficients** 字段中输入一个矩阵。

   此矩阵的每一*行*包含确定模块其中一个输出的传递函数的分子系数。
2. 在 **Denominator coefficients** 字段中输入系统所有传递函数共用的分母系数向量。

### 指定初始条件

传递函数描述 Laplace（频率）域中输入和输出之间的关系。具体而言，它定义为具有零初始条件的系统对脉冲输入的响应（输出）的 Laplace 变换。

传递函数的乘法和除法等运算依赖于零初始状态。例如，您可以将单个复杂传递函数分解为一系列更简单的传递函数。依次应用它们以获得与原始传递函数等效的响应。如果其中一个传递函数假定非零初始状态，则这将不正确。此外，传递函数具有无限多个时域实现，其中大多数状态没有任何物理意义。

由于这些原因，Simulink® 将 Transfer Fcn 模块的初始条件预设为零。若要为给定传递函数指定初始条件，请使用 `tf2ss` 将传递函数转换为其可控规范状态空间实现。然后，使用 State-Space 模块。`tf2ss` 实用工具提供系统的 `A`、`B`、`C` 和 `D` 矩阵。

有关详细信息，请键入 `help tf2ss` 或参阅 Control System Toolbox™ 文档。

### 模块上的传递函数显示

Transfer Fcn 模块根据您指定分子和分母参数的方式显示传递函数。

- 如果您将每个参数指定为表达式或向量，则模块使用为 *s* 的幂指定的系数显示传递函数。如果您在括号中指定变量，则模块会计算该变量。

  例如，如果您将 **Numerator coefficients** 参数值指定为 `[3 2 1]`，并将 **Denominator coefficients** 参数值指定为 `(den)`，其中 `den` 是值为 `[7 5 3 1]` 的工作区变量，则模块使用指定值显示方程。

  Transfer Fcn 模块将传递函数的分子和分母都显示为 s 的多项式函数。

  **提示**

  当模块大小太小而无法容纳完整分子或分母时，模块图标会将分子显示为 `num(s)`，将分母显示为 `den(s)`。

  宽度不足以显示方程的 Transfer Fcn 模块。

  如果您希望模块显示其实现的传递函数方程，请通过拖动角来调整模块大小。

  指针位于 Transfer Fcn 模块右下角以进行拖动，调整模块大小，使其足够宽以显示表示传递函数的方程。
- 如果您将每个参数指定为变量，则模块显示变量名称后跟 `(s)`。

  例如，如果您将 **Numerator coefficients** 参数指定为 `num`，并将 **Denominator coefficients** 参数指定为 `den`，则模块图标会将传递函数的分子显示为 `num(s)`，将分母显示为 `den(s)`。

  Transfer Fcn 模块的 Numerator coefficients 参数指定为 num，Denominator coefficients 参数指定为 den。
