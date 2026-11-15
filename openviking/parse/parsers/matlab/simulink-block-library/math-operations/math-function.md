---
type: simulink-block
title: 'Math Function'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'mathfunction'
---

# Math Function

Perform mathematical function

## 中文

执行数学函数

### 所属库

Simulink / Math Operations HDL Coder / Math Operations

### 描述

Math Function 模块执行许多常见的数学函数。

可以从 Math Function 模块中的**函数**参数列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 | MATLAB® 等效函数 |
| --- | --- | --- | --- |
| `exp` | 指数 | `eu` | `exp` |
| `log` | 自然对数 | `ln u` | `log` |
| `2^u` | 以 2 为底的幂 | `2u` | `2.^u`  （请参见`power`） |
| `10^u` | 以 10 为底的幂 | `10u` | `10.^u`  （请参见 `power`） |
| `log10` | 常用（以 10 为底）对数 | `log u` | `log10` |
| `magnitude^2` | 复数模量 | `|u|2` | `real(u).^2 + imag(u).^2`   （请参见 `real`、`imag` 和 `power`） |
| `square` | 2 次幂 | `u2` | `u.^2`  （请参见 `power`） |
| `pow` | 幂 | - 在**有符号幂**处于选中状态且**输出信号类型**设置为**实数**时，表达式为 `sign(u)*|u|v`。 - 在**有符号幂**处于清除状态或**输出信号类型**设置为**复数**时，表达式为 `uv`。 - 当**输出信号类型**设置为 `auto` 时，表达式取决于软件编译的复/实性类型。 | `power` |
| `conj` | 复共轭 | `ū` | `conj` |
| 使用精确法的 `reciprocal` | 倒数 | `1/u` | `1./u`  （请参见 `rdivide`） |
| 使用牛顿-拉夫逊方法的 `reciprocal` | 倒数 | 请参阅 牛顿-拉夫逊倒数算法方法。 | 无 |
| `hypot` | 平方和的平方根 | `(u2+v2)0.5` | `hypot` |
| `rem` | 除后的余数 | — | `rem` |
| `mod` | 除后的模数 | — | `mod` |
| `transpose` | 转置 | `uT` | `u.'`  （请参见数组与矩阵运算） |
| `hermitian` | 复共轭转置 | `uH` | `u'`  （请参见数组与矩阵运算） |

**提示**

要执行平方根计算，请使用 Sqrt 模块。

模块输出是对一个或多个输入执行函数运算的结果。这些函数支持以下类型的运算。

| 函数 | 标量运算 | 按元素的向量和矩阵运算 | 向量和矩阵运算 |
| --- | --- | --- | --- |
| `exp` | 是 | 是 | 不适用 |
| `log` | 是 | 是 | 不适用 |
| `2^u` | 是 | 是 | 不适用 |
| `10^u` | 是 | 是 | 不适用 |
| `log10` | 是 | 是 | 不适用 |
| `magnitude^2` | 是 | 是 | 不适用 |
| `square` | 是 | 是 | 不适用 |
| `pow` | 是 | 是 | 不适用 |
| `conj` | 是 | 是 | 不适用 |
| 使用精确法的 `reciprocal` | 是 | 是 | 不适用 |
| 使用牛顿-拉夫逊方法的 `reciprocal` | 是 | 是 | 不适用 |
| `hypot` | 是，对两个输入均执行 | 是，对两个输入均执行（大小相同的两个向量或两个矩阵、一个标量和一个向量，或者一个标量和一个矩阵） | — |
| `rem` | 是，对两个输入均执行 | 是，对两个输入均执行（大小相同的两个向量或两个矩阵、一个标量和一个向量，或者一个标量和一个矩阵） | 不适用 |
| `mod` | 是，对两个输入均执行 | 是，对两个输入均执行（大小相同的两个向量或两个矩阵、一个标量和一个向量，或者一个标量和一个矩阵） | 不适用 |
| `transpose` | 是 | — | 是 |
| `hermitian` | 是 | — | 是 |

函数名称和适当的输入端口数出现在模块上。

**提示**

当需要向量或矩阵输出时，使用 Math Function 模块。

#### 牛顿-拉夫逊倒数算法方法

具有牛顿-拉夫逊算法方法的 `reciprocal` 函数通过使用牛顿-拉夫逊逼近方法来计算倒数。该函数使用递归逼近来求实数值函数根的更佳逼近。

实数 a 的倒数定义为函数的零值：

f(x)=1x−a.

Simulink® 选择 0<x0<2a 范围内的一个初始估计值，因为这是函数的收敛域。

要连续计算函数的根，请指定**迭代次数**参数。该过程按如下方式重复执行：

xi+1=xi−f(xi)f'(xi)=xi+(xi−axi2)=xi.(2−axi)

f'(x) 是函数 f(x) 的导数。

#### 数据类型支持

下表列出了该模块的每个函数可以支持的输入数据类型。

| 函数 | 单精度 | 双精度 | 半精度\* | 布尔 | 内置整数 | 定点 |
| --- | --- | --- | --- | --- | --- | --- |
| `exp` | 是 | 是 | 是 | — | — | — |
| `log` | 是 | 是 | 是 | — | — | — |
| `2^u` | 是 | 是 | 是 | — | — | — |
| `10^u` | 是 | 是 | 是 | — | — | — |
| `log10` | 是 | 是 | 是 | — | — | — |
| `magnitude^2` | 是 | 是 | 是 | — | 是 | 是 |
| `square` | 是 | 是 | 是 | — | 是 | 是 |
| `pow` | 是 | 是 | 是 | — | — | — |
| `conj` | 是 | 是 | 是 | — | 是 | 是 |
| 使用精确法的 `reciprocal` | 是 | 是 | 是 | — | 是 | 是 |
| 使用牛顿-拉夫逊方法的 `reciprocal`（有关详细信息，请参阅输出） | 是 | 是 | — | — | 是 | 是 |
| `hypot` | 是 | 是 | 是 | — | — | — |
| `rem` | 是 | 是 | 是 | — | 是 | — |
| `mod` | 是 | 是 | 是 | — | 是 | — |
| `transpose` | 是 | 是 | 是 | 是 | 是 | 是 |
| `hermitian` | 是 | 是 | 是 | — | 是 | 是 |

有关半精度算术运算的详细信息，请参阅 The Half-Precision Data Type in Simulink (Fixed-Point Designer)。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。受支持的模式同时接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。请参阅描述。

##### 依赖关系

此模块的数据类型支持取决于您选择的**函数**和输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_2** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。受支持的模式同时接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。

##### 依赖关系

要启用此端口，请将**函数**设置为 **hypot**、**rem** 或 **mod**。

此模块的数据类型支持取决于您选择的**函数**和输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 对一个或多个输入执行函数运算的结果 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。模块输出的维度取决于您选择的**函数**和输入的大小。模块输出是实数还是复数取决于您的**输出信号类型**选项。请参阅描述。

##### 使用牛顿-拉夫逊方法的 `reciprocal`

使用牛顿-拉夫逊方法的 `reciprocal` 的输出数据类型取决于输入数据类型：

| 输入数据类型 | 输出数据类型 |
| --- | --- |
| 单精度 | 单精度 |
| 双精度 | 双精度 |
| 内置整数 | 内置整数 |
| 内置定点 | 内置定点 |
| `fi` (*value*, 0, *word\_length*, *fraction\_length*) | `fi` (*value*, 0, *word\_length*, *word\_length*–*fraction\_length*–1) |
| `fi` (*value*, 1, *word\_length*, *fraction\_length*) | `fi` (*value*, 1, *word\_length*, *word\_length*–*fraction\_length*–2) |

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **函数** — 数学函数 **exp** (默认) | **log** | **2^u** | **10^u** | **log10** | **magnitude^2** | **方波** | **pow** | **conj** | **倒数** | **hypot** | **rem** | **mod** | **转置** | **hermitian**

指定数学函数。有关此参数的选项的详细信息，请参阅描述。

##### 依赖关系

将**函数**设置为 **pow** 会启用**有符号幂**参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型：**字符向量 |
| **值**：`'exp' | 'log' | '2^u' | '10^u' | 'log10' | 'magnitude^2' | 'square' | 'pow' | 'conj' | 'reciprocal' | 'hypot' | 'rem' | 'mod' | 'transpose' | 'hermitian'` |
| **默认值：**`'exp'` |

#### **算法方法** — `reciprocal` 函数的算法方法 **完全** (默认) | **牛顿-拉夫逊**

`reciprocal` 函数的算法方法，指定为**完全**或**牛顿-拉夫逊**。要使用牛顿-拉夫逊逼近方法计算倒数，请选择**牛顿-拉夫逊**。否则，请选择**完全**。

##### 依赖关系

将**函数**设置为**倒数**会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`AlgorithmType` |
| **类型：**字符向量 |
| **值：**`'Exact' | 'Newton-Raphson'` |
| **默认值**：`'Exact'` |

#### **有符号幂** — 幂的符号性 on (默认) | off

计算幂时（指定为开或关），考虑输入信号的符号。Math Function 仅在输出信号为实数时使用此参数。

- on - 通过将输入信号绝对值乘以输入信号的符号来计算幂。
- off - 计算实际输入值的幂。如果第一个输入为负数，第二个输入不是整数，且输出信号为实数，则函数返回 `NaN`。

##### 依赖关系

将**函数**设置为 **pow** 会启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数**：`SignedPower` |
| **类型：**字符向量 |
| **值：**`'on' | 'off' |` |
| **默认值：**`'on'` |

#### **输出信号类型** — 输出信号的复/实性 **自动** (默认) | **实数** | **复**

将 Math Function 模块的输出信号类型指定为 `auto`、`real` 或 `complex`。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| 自动 | 实数 | 复数 |
| `exp`, `log`, `2^u`, `10^u`, `log10`, `square`, `pow`, `reciprocal`, `conjugate`, `transpose`, `hermitian` | `real`  `complex` | `real`  `complex` | `real`  `error` | `complex`  `complex` |
| `magnitude squared` | `real`  `complex` | `real`  `real` | `real`  `real` | `complex`  `complex` |
| `hypot`, `rem`, `mod` | `real`  `complex` | `real`  `error` | `real`  `error` | `complex`  `error` |

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputSignalType` |
| **类型：**字符向量 |
| **值：**`'auto' | 'real' | 'complex'` |
| **默认值：**`'auto'` |

#### **迭代次数** — 牛顿-拉夫逊迭代次数 3 (默认) | 标量

牛顿-拉夫逊迭代次数，指定为标量。

##### 依赖关系

要启用此参数，请进行如下设置：

- **函数**设置为**倒数**。
- **算法方法**设置为**牛顿-拉夫逊**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Iterations` |
| **类型：**字符向量 |
| **值：**`'3' | scalar` |
| **默认值：**`'3'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

#### 信号属性

#### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出数据类型** — 指定输出数据类型 `Inherit: Same as first input` (默认) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 通过反向传播继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

- 要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。
- 对于 **magnitude^2** 和 **square**，当输入是小于单精度的浮点数据类型时，**Inherit: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Same as first input'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

##### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

#### **对整数溢出进行饱和处理** — 选择发生整数溢出时的行为 `on` (默认) | 布尔

| 操作 | 理由 | 溢出 | 示例 |
| --- | --- | --- | --- |
| 选中**对整数溢出进行饱和处理**复选框。 | 您的模型可能有溢出，并且您希望在生成的代码中具有显式饱和保护。 | 将溢出饱和处理为数据类型能够表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。如果选中此复选框，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。 |
| 不选中**对整数溢出进行饱和处理**复选框。 | 您需要优化所生成代码的效率。  您希望避免过度地指定信号超出范围时的处理方式。有关详细信息，请参阅信号范围错误故障排除。 | 溢出会绕回到由数据类型表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框时，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。 |

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。代码生成过程可以检测何时不会发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**、**conj**、**倒数**或 **hermitian**。

##### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 函数 | 架构 | 描述 |
| --- | --- | --- |
| `conj` | **ComplexConjugate** | 计算复共轭。 |
| `hermitian` | **hermitian** | 计算 hermitian。 |
| `transpose` | **转置** | 计算数组转置。请参阅 Simulink 文档中的Math Function。 |
| `mod`  `rem` | **ShiftAdd** | 通过使用非还原除法算法对内置整数类型输入执行模数或余数运算，该算法执行多次移位相加运算来计算 `mod` 和 `rem` 运算。  **ShiftAdd** 是一种流水线实现，它可能会在生成的代码中引入额外的延迟。使用这种架构，您还可以通过设置 **LatencyStrategy** 参数来设置延迟策略。 |

**倒数架构**

当**算法方法**设置为**精确**时，您可以在此模块的 HDL 模块属性中选择此选项。

| 架构 | 参数 | 额外的延迟周期 | 描述 |
| --- | --- | --- | --- |
| **ShiftAdd(默认值)** | 无 | 有符号输入：（输入字长 + 4）  无符号输入：（输入字长 + 4）  有关模块的浮点延迟，请参阅Latency Values of Floating-Point Operators (HDL Coder)。 | 通过使用非还原除法算法对定点或浮点输入执行倒数运算，该算法执行多次移位相加运算来计算倒数。与牛顿-拉夫逊逼近方法相比，这种架构提高了精度。  使用定点数据类型时，必须满足以下标准才能生成 HDL 代码：  - 输入字长 (`WL`) 必须小于或等于 63。 - `[WL input + Abs(FL Sum)]` 必须小于或等于 63。其中， `FL Sum` 由下式给出：  `FL sum = FL input + FL output` |

您可以在 **ShiftAdd** 架构中对 Math Function Reciprocal 模块应用共享优化。有关详细信息，请参阅Resource Sharing (HDL Coder)。

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

对于 `reciprocal` 函数，HDL 代码生成还支持牛顿-拉夫逊算法方法。选择**算法方法**为**牛顿-拉夫逊**，以将这些架构用于 Math Function 模块中的 `reciprocal` 函数。

| 架构 | 额外的延迟周期 | 描述 |
| --- | --- | --- |
| **ReciprocalNewton**（默认值） | `Iterations` + 1 | 使用牛顿迭代法的多速率实现。选择此选项可优化设计区域。  `Iterations` 的默认值为 3。  `Iterations` 的推荐值为 2 到 10。如果 `Iterations` 的值超出建议的范围，HDL Coder 将显示一条消息。 |
| **ReciprocalNewtonSingleRate** | (`Iterations` \* 2) + 1 | 使用单频率流水线牛顿法。要为您的设计优化速度或需要单速率实现，请选择此选项。  `Iterations` 的默认值为 3。  `Iterations` 的建议值介于 2 到 10 之间。如果 `Iterations` 值超出建议的范围，HDL Coder 将显示一条消息。 |
| ReciprocalRsqrtBasedNewtonSingleRate | 有符号输入：(`Iterations` \* 4) + 8  无符号输入：(`Iterations` \* 4) + 6 | 使用单频率流水线牛顿法。要优化速度或需要单速率实现，请选择此选项。  `Iterations` 的默认值为 3。  `Iterations` 的推荐值为 2 到 10。如果 `Iterations` 超出推荐范围，代码生成器会生成一条消息。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要启用此属性，请将 HDL 架构设置为 **ShiftAdd**。对于定点类型，指定是将设计中的模块映射到 `MAX`、`Min`、`CUSTOM` 还是 `ZERO` 延迟。默认值为 **MAX**。另请参阅LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 要启用此属性，请将 HDL 架构设置为 **ShiftAdd**。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅LatencyStrategy (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **CheckResetToZero** | 将此属性用于 Math Function 模块的 `mod` 和 `rem` 函数。如果两个数 `a` 和 `b` 的商 `a/b` 接近整数，则此设置将 `a` 视为 `b` 的整数倍且 `rem(a,b)` = 0。该结果在数值上是精确的，并且与仿真结果相匹配。计算该结果会使用额外的资源，并会增加目标 FPGA 设备上的占用面积。有关详细信息，请参阅 CheckResetToZero (HDL Coder)。 |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会增加延迟，其值等于您为 **NFPCustomLatency** 设置指定的值。另请参阅NFPCustomLatency (HDL Coder)。 |
| **MaxIterations** | 将此属性用于 Math Function 模块的 `mod` 和 `rem` 函数。如果您的两个数 `a` 和 `b` 是非常大的整数，您可以增大 **MaxIterations** 以匹配仿真结果。计算该结果会使用额外的资源，并会增加目标 FPGA 设备上的占用面积。有关详细信息，请参阅 MaxIterations (HDL Coder)。 |
| **IterationsPerPipeline** | 将此属性用于 Math Function 模块的 `reciprocal` 函数。要启用此属性，请将**算法方法**参数设置为**精确**。当 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线阶段的迭代次数。有关详细信息，请参阅Reciprocal (HDL Coder)。 |

**支持原生浮点的数据类型和函数**

Math Function 模块支持标量、向量或矩阵数据类型。此模块支持以下使用原生浮点的函数。

| 数学函数 | 支持的浮点数据类型 | | | 定点数据类型支持 | 复数数据支持 |
| --- | --- | --- | --- | --- | --- |
| 半精度 | 单精度 | 双精度 |
| `exp` | 否 | 是 | 否 | 否 | 否 |
| `log` | 否 | 是 | 是 | 否 | 否 |
| `2^u` | 否 | 是 | 否 | 否 | 否 |
| `10^u` | 否 | 是 | 否 | 否 | 否 |
| `log10` | 否 | 是 | 否 | 否 | 否 |
| `magnitude^2` | 否 | 是 | 是 | 是 | 是 |
| `square` | 否 | 是 | 否 | 是 | 是 |
| `pow` | 否 | 是 | 否 | 否 | 否 |
| `conj` | 否 | 是 | 否 | 是 | 是 |
| `reciprocal` | 是 | 是 | 是 | 是 | 否 |
| `hypot` | 否 | 是 | 否 | 否 | 否 |
| `rem` | 否 | 是 | 否 | 否 | 否 |
| `mod` | 否 | 是 | 否 | 否 | 否 |
| `transpose` | 是 | 是 | 是 | 是 | 是 |
| `hermitian` | 否 | 是 | 否 | 是 | 是 |

**限制**

当您使用**倒数**实现时：

- 输入必须为标量，并且必须具有整数或定点（有符号或无符号）数据类型。
- 输出必须为标量，并且具有整数或定点（有符号或无符号）数据类型。
- 必须对模块选择**对整数溢出进行饱和处理**选项。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

Math Function 模块只支持某些配置中的定点转换。有关详细信息，请参阅 Block Support Table。

### 版本历史记录

**在 R2006a 之前推出**

#### R2023a: `Math Function` 模块支持 2^u

Math Function 模块现在支持 `2^u` 函数。MATLAB 等效形式是 `2.^u`（请参阅 `power`）。

## Libraries

Simulink / Math Operations HDL Coder / Math Operations

## Description

The Math Function block performs many common mathematical functions.

You can select one of these functions from the **Function** parameter list
in Math Function block.

| Function | Description | Mathematical Expression | MATLAB® Equivalent |
| --- | --- | --- | --- |
| `exp` | Exponential | `eu` | `exp` |
| `log` | Natural logarithm | `ln u` | `log` |
| `2^u` | Power of base 2 | `2u` | `2.^u`  (see `power`) |
| `10^u` | Power of base 10 | `10u` | `10.^u`  (see `power`) |
| `log10` | Common (base 10) logarithm | `log u` | `log10` |
| `magnitude^2` | Complex modulus | `|u|2` | `real(u).^2 + imag(u).^2`   (see `real`, `imag`, and `power`) |
| `square` | Power 2 | `u2` | `u.^2`  (see `power`) |
| `pow` | Power | - With **Signed power** selected and   **Output signal type** set to   `real`, the expression is   `sign(u)*|u|v`. - With **Signed power** cleared or   **Output signal type** set to   `complex`, the expression is   `uv`. - When **Output signal type** is set to   `auto`, the expression depends on the   complexity type that the software compiles. | `power` |
| `conj` | Complex conjugate | `ū` | `conj` |
| `reciprocal` with Exact method | Reciprocal | `1/u` | `1./u`  (see `rdivide`) |
| `reciprocal` with Newton-Raphson method | Reciprocal | See Newton-Raphson Reciprocal Algorithm Method | None |
| `hypot` | Square root of sum squares | `(u2+v2)0.5` | `hypot` |
| `rem` | Remainder after division | — | `rem` |
| `mod` | Modulus after division | — | `mod` |
| `transpose` | Transpose | `uT` | `u.'`  (see Array vs. Matrix Operations) |
| `hermitian` | Complex conjugate transpose | `uH` | `u'`  (see Array vs. Matrix Operations) |

**Tip**

To perform square root calculations, use the Sqrt block.

The block output is the result of the operation of the function on the input or inputs. The
functions support these types of operations.

| Function | Scalar Operations | Element-Wise Vector and Matrix Operations | Vector and Matrix Operations |
| --- | --- | --- | --- |
| `exp` | Yes | Yes | Not applicable |
| `log` | Yes | Yes | Not applicable |
| `2^u` | Yes | Yes | Not applicable |
| `10^u` | Yes | Yes | Not applicable |
| `log10` | Yes | Yes | Not applicable |
| `magnitude^2` | Yes | Yes | Not applicable |
| `square` | Yes | Yes | Not applicable |
| `pow` | Yes | Yes | Not applicable |
| `conj` | Yes | Yes | Not applicable |
| `reciprocal` with Exact method | Yes | Yes | Not applicable |
| `reciprocal` with Newton-Raphson method | Yes | Yes | Not applicable |
| `hypot` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | — |
| `rem` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | Not applicable |
| `mod` | Yes, on two inputs | Yes, on two inputs (two vectors or two matrices of the same size, a scalar and a vector, or a scalar and a matrix) | Not applicable |
| `transpose` | Yes | — | Yes |
| `hermitian` | Yes | — | Yes |

The name of the function and the appropriate number of input ports appear on the block.

**Tip**

Use the Math Function block when you want vector or matrix output.

### Newton-Raphson Reciprocal Algorithm Method

The `reciprocal` function that has the Newton-Raphson algorithm method
calculates the reciprocal by using the Newton-Raphson approximation method. The
function uses recursive approximation to find better approximations to the roots of
a real-value function.

The reciprocal of a real number a is defined as a zero of the function:

f(x)=1x−a.

Simulink® chooses an initial estimate in the range 0<x0<2a, because this is the domain of convergence for the
function.

To successively calculate the roots of the function, specify the **Number of
iterations** parameter. The process is repeated as follows:

xi+1=xi−f(xi)f'(xi)=xi+(xi−axi2)=xi.(2−axi)

f'(x) is the derivative of the function f(x).

### Data Type Support

This table lists the input data types that each function of the block can support.

| Function | Single | Double | Half\* | Boolean | Built-In Integer | Fixed Point |
| --- | --- | --- | --- | --- | --- | --- |
| `exp` | Yes | Yes | Yes | — | — | — |
| `log` | Yes | Yes | Yes | — | — | — |
| `2^u` | Yes | Yes | Yes | — | — | — |
| `10^u` | Yes | Yes | Yes | — | — | — |
| `log10` | Yes | Yes | Yes | — | — | — |
| `magnitude^2` | Yes | Yes | Yes | — | Yes | Yes |
| `square` | Yes | Yes | Yes | — | Yes | Yes |
| `pow` | Yes | Yes | Yes | — | — | — |
| `conj` | Yes | Yes | Yes | — | Yes | Yes |
| `reciprocal` with Exact method | Yes | Yes | Yes | — | Yes | Yes |
| `reciprocal` with Newton-Raphson method (for more information, see Output) | Yes | Yes | — | — | Yes | Yes |
| `hypot` | Yes | Yes | Yes | — | — | — |
| `rem` | Yes | Yes | Yes | — | Yes | — |
| `mod` | Yes | Yes | Yes | — | Yes | — |
| `transpose` | Yes | Yes | Yes | Yes | Yes | Yes |
| `hermitian` | Yes | Yes | Yes | — | Yes | Yes |

For more information on half-precision arithmetic operations, see The Half-Precision Data Type in Simulink (Fixed-Point Designer).

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix. Supported modes accept real and
complex inputs, except for `reciprocal`, which does not
accept complex fixed-point inputs. See Description.

#### Dependencies

Data type support for this block depends on the **Function** that you
select and the size of the inputs. For more information, see Data Type Support.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — Input signal scalar | vector | matrix

Input signal specified as a scalar, vector, or matrix. Supported modes accept real and
complex inputs, except for `reciprocal`, which does not
accept complex fixed-point inputs.

#### Dependencies

To enable this port, set **Function** to
`hypot`,
`rem`, or
`mod`.

Data type support for this block depends on the **Function** that you
select, and the size of the inputs. For more information, see Data Type Support.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Result of the operation of the function on the input or inputs scalar | vector | matrix

Output signal specified as a scalar, vector, or matrix. The dimensions of the block
output depend on the **Function** that you select and
the size of the inputs. The block output is real or complex, depending
on what you select for **Output signal type**. See
Description.

#### `reciprocal` with Newton-Raphson Method

The `reciprocal` with Newton-Raphson method
output data type depends on the input data type:

| Input Data Type | Output Data Type |
| --- | --- |
| single | single |
| double | double |
| built-in integer | built-in integer |
| built-in fixed-point | built-in fixed-point |
| `fi` (*value*, 0, *word\_length*, *fraction\_length*) | `fi` (*value*, 0, *word\_length*, *word\_length*–*fraction\_length*–1) |
| `fi` (*value*, 1, *word\_length*, *fraction\_length*) | `fi` (*value*, 1, *word\_length*, *word\_length*–*fraction\_length*–2) |

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Function** — Math function `exp` (default) | `log` | `2^u` | `10^u` | `log10` | `magnitude^2` | `square` | `pow` | `conj` | `reciprocal` | `hypot` | `rem` | `mod` | `transpose` | `hermitian`

Specify the mathematical function. For more information about the options for this
parameter, see Description.

#### Dependency

Setting **Function** to
`pow` enables the **Signed
power** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Operator` |
| **Type:** character vector |
| **Values:** `'exp' | 'log' | '2^u' | '10^u' | 'log10' | 'magnitude^2' | 'square' | 'pow' | 'conj' | 'reciprocal' | 'hypot' | 'rem' | 'mod' | 'transpose' | 'hermitian'` |
| **Default:** `'exp'` |

### **Algorithm method** — Algorithm method for `reciprocal` function `Exact` (default) | `Newton-Raphson`

Algorithm method for `reciprocal` function, specified
as `Exact` or
`Newton-Raphson`. To calculate reciprocal
with the Newton-Raphson approximation method, select
`Newton-Raphson`. Otherwise, select
`Exact`.

#### Dependency

Setting **Function** to
`reciprocal` enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AlgorithmType` |
| **Type:** character vector |
| **Values:** `'Exact' | 'Newton-Raphson'` |
| **Default:** `'Exact'` |

### **Signed power** — Power signedness on (default) | off

When calculating power, specified as on or off, take into account sign of the input
signal. Math Function uses this parameter only when the
output signal is real.

- on — Calculate power of the absolute value of the input,
  multiplied by the sign of the input.
- off — Calculate power of the actual input value. If the first
  input is negative, the second input is not an integer, and the
  output signal is real, the function returns
  `NaN`.

#### Dependency

Setting **Function** to
`pow` enables this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignedPower` |
| **Type:** character vector |
| **Values:** `'on' | 'off' |` |
| **Default:** `'on'` |

### **Output signal type** — Complexity of output signal `auto` (default) | `real` | `complex`

Specify the output signal type of the Math Function block as
`auto`, `real`, or
`complex`.

| Function | Input Signal Type | Output Signal Type | | |
| --- | --- | --- | --- | --- |
| Auto | Real | Complex |
| `exp`, `log`, `2^u`, `10^u`, `log10`, `square`, `pow`, `reciprocal`, `conjugate`, `transpose`, `hermitian` | `real`  `complex` | `real`  `complex` | `real`  `error` | `complex`  `complex` |
| `magnitude squared` | `real`  `complex` | `real`  `real` | `real`  `real` | `complex`  `complex` |
| `hypot`, `rem`, `mod` | `real`  `complex` | `real`  `error` | `real`  `error` | `complex`  `error` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSignalType` |
| **Type:** character vector |
| **Values:** `'auto' | 'real' | 'complex'` |
| **Default:** `'auto'` |

### **Number of iterations** — Number of Newton-Raphson iterations 3 (default) | scalar

Number of Newton-Raphson iterations, specified as a scalar.

#### Dependencies

To enable this parameter, set:

- **Function** to
  `reciprocal`.
- **Algorithm method** to
  `Newton-Raphson`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Iterations` |
| **Type:** character vector |
| **Values:** `'3' | scalar` |
| **Default:** `'3'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### Signal Attributes

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Specify the output data type `Inherit: Same as first input` (default) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

- To enable this parameter, set the
  **Function** to
  `magnitude^2`,
  `square`, or
  `reciprocal`.
- For the `magnitude^2` and
  `square`, when input is a
  floating-point data type smaller than single precision, the
  `Inherit: Inherit via internal
  rule` output data type depends on the
  setting of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than
  single-precision when the number of bits needed to encode
  the data type is less than the 32 bits needed to encode the
  single precision data type. For example,
  `half` and `int16` are
  smaller than single precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Same as first input'` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding
the **Output** data type you specify on the block. For
more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`, or
`reciprocal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Rounding mode for fixed-point operations. For more information, see
Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function into the mask field.

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`, or
`reciprocal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Choose the behavior when integer overflow occurs `on` (default) | boolean

| Action | Rationale | Overflows | Example |
| --- | --- | --- | --- |
| Select **Saturate on integer overflow** check box. | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box selected, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of -128. |
| Do not select **Saturate on integer overflow** check box. | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Overflows wrap to the appropriate value that is representable by the data type. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box cleared, the software interprets the overflow-causing value as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8`, is -126. |

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. The code generation process can
detect when overflow is not possible. In this case, the code generator
does not produce saturation code.

#### Dependencies

To enable this parameter, set the **Function** to
`magnitude^2`,
`square`,
`conj`,
`reciprocal`, or
`hermitian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Function | Architecture | Description |
| --- | --- | --- |
| `conj` | `ComplexConjugate` | Calculate complex conjugate. |
| `hermitian` | `Hermitian` | Calculate hermitian. |
| `transpose` | `Transpose` | Calculate array transpose. See Math Function in the Simulink documentation. |
| `mod`  `rem` | `ShiftAdd` | Perform modulus or remainder operation on a built-in integer types input by using a non-restoring division algorithm that performs multiple shift and add operations to compute the `mod` and `rem` operations.  `ShiftAdd` is a pipelined implementation, and it can introduce additional latency in the generated code. Using this architecture, you can also set the latency strategy by setting the **LatencyStrategy** parameter. |

**Reciprocal Architecture**

When you set the **Algorithm method** to
`Exact`, you can select this options in HDL Block
properties of this block.

| Architecture | Parameters | Additional Cycles of Latency | Description |
| --- | --- | --- | --- |
| `ShiftAdd(default)` | None | Signed input: (Input word length + 4)  Unsigned input: (Input word length + 4)  For floating-point latency of the block, see Latency Values of Floating-Point Operators (HDL Coder). | Perform reciprocal operation on a fixed-point or floating point input by using a non-restoring division algorithm that performs multiple shift and add operations to compute the reciprocal. This architecture provides improved accuracy compared to the Newton-Raphson approximation method.  When you use fixed-point data types, following criteria must be satisfied for generating the HDL code:  - Input word length (`WL`) must be   less than or equal to 63. - `[WL input + Abs(FL Sum)]` must   be less than or equal to 63. Where, `FL   Sum` is given by,  `FL sum = FL input + FL   output` |

You can apply sharing optimization for Math Function Reciprocal block in
`ShiftAdd` architecture. For more information, see
Resource Sharing (HDL Coder).

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

HDL code generation also supports the Newton-Raphson algorithm method for
`reciprocal` function. Select the **Algorithm
method** as `Newton-Raphson` to use these
architectures for `reciprocal` function in the Math
Function block.

| Architecture | Additional Cycles of Latency | Description |
| --- | --- | --- |
| `ReciprocalNewton` (default) | `Iterations` + 1 | Use the multirate implementation of the iterative Newton method. Select this option to optimize area for your design.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is from 2 through 10. If `Iterations` value is outside the recommended range, HDL Coder displays a message. |
| `ReciprocalNewtonSingleRate` | (`Iterations` \* 2) + 1 | Use the single rate pipelined Newton method. Select this option to optimize speed for your design, or if you want a single rate implementation.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is between 2 and 10. If `Iterations` value is outside the recommended range, HDL Coder displays a message. |
| ReciprocalRsqrtBasedNewtonSingleRate | Signed input: (`Iterations` \* 4) + 8  Unsigned input: (`Iterations` \* 4) + 6 | Use the single rate pipelined Newton method. Select this option to optimize speed, or if you want a single rate implementation.  The default value for `Iterations` is 3.  The recommended value for `Iterations` is from 2 through 10. If `Iterations` is outside the recommended range, the coder generates a message. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | To enable this property, set HDL architecture to `ShiftAdd`. Specify whether to map the blocks in your design to `MAX`, `Min`, `CUSTOM`, or `ZERO` latency for fixed-point types. The default is `MAX`. See also LatencyStrategy (HDL Coder). |
| **CustomLatency** | To enable this property, set HDL architecture to `ShiftAdd`. When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **CheckResetToZero** | Use this property for the `mod` and `rem` functions of the Math Function block. If you have numbers `a` and `b` such that the quotient `a/b` is close to an integer, this setting treats `a` as an integral multiple of `b`, and `rem(a,b)` = 0. This result is numerically accurate and matches the simulation results. Calculating this result uses additional resources and increases the area footprint on the target FPGA device. For more information, see CheckResetToZero (HDL Coder). |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |
| **MaxIterations** | Use this property for the `mod` and `rem` functions of the Math Function block. If you have numbers `a` and `b` that are significantly large integers, you can increase **MaxIterations** to match the simulation results. Calculating this result uses additional resources and increases the area footprint on the target FPGA device. For more information, see MaxIterations (HDL Coder). |
| **IterationsPerPipeline** | Use this property for the `reciprocal` function of the Math Function block. To enable this property, set **Algorithm method** parameter to `Exact`. When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages. For more information, see Reciprocal (HDL Coder). |

**Supported Datatypes and Functions in Native Floating-Point**

The Math Function block supports scalar, vector, or matrix data types. This
block supports these functions with Native Floating-Point.

| Math Functions | Supported Floating-Point Datatypes | | | Fixed-Point Datatype Support | Complex Data Support |
| --- | --- | --- | --- | --- | --- |
| Half | Single | Double |
| `exp` | No | Yes | No | No | No |
| `log` | No | Yes | Yes | No | No |
| `2^u` | No | Yes | No | No | No |
| `10^u` | No | Yes | No | No | No |
| `log10` | No | Yes | No | No | No |
| `magnitude^2` | No | Yes | Yes | Yes | Yes |
| `square` | No | Yes | No | Yes | Yes |
| `pow` | No | Yes | No | No | No |
| `conj` | No | Yes | No | Yes | Yes |
| `reciprocal` | Yes | Yes | Yes | Yes | No |
| `hypot` | No | Yes | No | No | No |
| `rem` | No | Yes | No | No | No |
| `mod` | No | Yes | No | No | No |
| `transpose` | Yes | Yes | Yes | Yes | Yes |
| `hermitian` | No | Yes | No | Yes | Yes |

**Restrictions**

When you use a `reciprocal` implementation:

- Input must be scalar and must have integer or fixed-point (signed or
  unsigned) data type.
- The output must be scalar and have integer or fixed-point (signed or
  unsigned) data type.
- The **Saturate on integer overflow** option on the
  block must be selected.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

The Math Function block only supports fixed-point conversion in certain
configurations. For more information, see the Block Support Table.

## Version History

**Introduced before R2006a**

### R2023a: `Math Function` Block Supports 2^u

The Math Function block now supports the
`2^u` function. The MATLAB equivalent is `2.^u` (see `power`).
