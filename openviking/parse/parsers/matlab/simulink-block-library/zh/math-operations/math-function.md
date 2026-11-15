---
type: simulink-block
title: 'Math Function'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'mathfunction'
language: zh-CN
chinese_source: official
---

# Math Function

执行数学函数

## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 描述

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

### 牛顿-拉夫逊倒数算法方法

具有牛顿-拉夫逊算法方法的 `reciprocal` 函数通过使用牛顿-拉夫逊逼近方法来计算倒数。该函数使用递归逼近来求实数值函数根的更佳逼近。

实数 a 的倒数定义为函数的零值：

f(x)=1x−a.

Simulink® 选择 0<x0<2a 范围内的一个初始估计值，因为这是函数的收敛域。

要连续计算函数的根，请指定**迭代次数**参数。该过程按如下方式重复执行：

xi+1=xi−f(xi)f'(xi)=xi+(xi−axi2)=xi.(2−axi)

f'(x) 是函数 f(x) 的导数。

### 数据类型支持

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

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。受支持的模式同时接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。请参阅描述。

#### 依赖关系

此模块的数据类型支持取决于您选择的**函数**和输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_2** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。受支持的模式同时接受实数和复数输入，但 `reciprocal` 除外，它不接受复数定点输入。

#### 依赖关系

要启用此端口，请将**函数**设置为 **hypot**、**rem** 或 **mod**。

此模块的数据类型支持取决于您选择的**函数**和输入的大小。有关详细信息，请参阅数据类型支持。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 对一个或多个输入执行函数运算的结果 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。模块输出的维度取决于您选择的**函数**和输入的大小。模块输出是实数还是复数取决于您的**输出信号类型**选项。请参阅描述。

#### 使用牛顿-拉夫逊方法的 `reciprocal`

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

## 参数

### 常设

### **函数** — 数学函数 **exp** (默认) | **log** | **2^u** | **10^u** | **log10** | **magnitude^2** | **方波** | **pow** | **conj** | **倒数** | **hypot** | **rem** | **mod** | **转置** | **hermitian**

指定数学函数。有关此参数的选项的详细信息，请参阅描述。

#### 依赖关系

将**函数**设置为 **pow** 会启用**有符号幂**参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`Operator` |
| **类型：**字符向量 |
| **值**：`'exp' | 'log' | '2^u' | '10^u' | 'log10' | 'magnitude^2' | 'square' | 'pow' | 'conj' | 'reciprocal' | 'hypot' | 'rem' | 'mod' | 'transpose' | 'hermitian'` |
| **默认值：**`'exp'` |

### **算法方法** — `reciprocal` 函数的算法方法 **完全** (默认) | **牛顿-拉夫逊**

`reciprocal` 函数的算法方法，指定为**完全**或**牛顿-拉夫逊**。要使用牛顿-拉夫逊逼近方法计算倒数，请选择**牛顿-拉夫逊**。否则，请选择**完全**。

#### 依赖关系

将**函数**设置为**倒数**会启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`AlgorithmType` |
| **类型：**字符向量 |
| **值：**`'Exact' | 'Newton-Raphson'` |
| **默认值**：`'Exact'` |

### **有符号幂** — 幂的符号性 on (默认) | off

计算幂时（指定为开或关），考虑输入信号的符号。Math Function 仅在输出信号为实数时使用此参数。

- on - 通过将输入信号绝对值乘以输入信号的符号来计算幂。
- off - 计算实际输入值的幂。如果第一个输入为负数，第二个输入不是整数，且输出信号为实数，则函数返回 `NaN`。

#### 依赖关系

将**函数**设置为 **pow** 会启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`SignedPower` |
| **类型：**字符向量 |
| **值：**`'on' | 'off' |` |
| **默认值：**`'on'` |

### **输出信号类型** — 输出信号的复/实性 **自动** (默认) | **实数** | **复**

将 Math Function 模块的输出信号类型指定为 `auto`、`real` 或 `complex`。

| 函数 | 输入信号类型 | 输出信号类型 | | |
| --- | --- | --- | --- | --- |
| 自动 | 实数 | 复数 |
| `exp`, `log`, `2^u`, `10^u`, `log10`, `square`, `pow`, `reciprocal`, `conjugate`, `transpose`, `hermitian` | `real`  `complex` | `real`  `complex` | `real`  `error` | `complex`  `complex` |
| `magnitude squared` | `real`  `complex` | `real`  `real` | `real`  `real` | `complex`  `complex` |
| `hypot`, `rem`, `mod` | `real`  `complex` | `real`  `error` | `real`  `error` | `complex`  `error` |

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputSignalType` |
| **类型：**字符向量 |
| **值：**`'auto' | 'real' | 'complex'` |
| **默认值：**`'auto'` |

### **迭代次数** — 牛顿-拉夫逊迭代次数 3 (默认) | 标量

牛顿-拉夫逊迭代次数，指定为标量。

#### 依赖关系

要启用此参数，请进行如下设置：

- **函数**设置为**倒数**。
- **算法方法**设置为**牛顿-拉夫逊**。

#### 编程用法

|  |
| --- |
| **模块参数**：`Iterations` |
| **类型：**字符向量 |
| **值：**`'3' | scalar` |
| **默认值：**`'3'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

### 信号属性

### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

#### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

#### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

### **输出数据类型** — 指定输出数据类型 `Inherit: Same as first input` (默认) | `Inherit: Inherit via internal rule` | `Inherit: Inherit via back propagation` | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定输出数据类型。可以将其设置为：

- 继承数据类型的规则，例如**继承: 通过反向传播继承**
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

- 要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。
- 对于 **magnitude^2** 和 **square**，当输入是小于单精度的浮点数据类型时，**Inherit: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Same as first input'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。

#### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

#### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**或**倒数**。

#### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

### **对整数溢出进行饱和处理** — 选择发生整数溢出时的行为 `on` (默认) | 布尔

| 操作 | 理由 | 溢出 | 示例 |
| --- | --- | --- | --- |
| 选中**对整数溢出进行饱和处理**复选框。 | 您的模型可能有溢出，并且您希望在生成的代码中具有显式饱和保护。 | 将溢出饱和处理为数据类型能够表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。如果选中此复选框，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。 |
| 不选中**对整数溢出进行饱和处理**复选框。 | 您需要优化所生成代码的效率。  您希望避免过度地指定信号超出范围时的处理方式。有关详细信息，请参阅信号范围错误故障排除。 | 溢出会绕回到由数据类型表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框时，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。 |

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。代码生成过程可以检测何时不会发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 依赖关系

要启用此参数，请将**函数**设置为 **magnitude^2**、**方波**、**conj**、**倒数**或 **hermitian**。

#### 编程用法

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

Math Function 模块只支持某些配置中的定点转换。有关详细信息，请参阅 Block Support Table。

## 版本历史记录

**在 R2006a 之前推出**

### R2023a: `Math Function` 模块支持 2^u

Math Function 模块现在支持 `2^u` 函数。MATLAB 等效形式是 `2.^u`（请参阅 `power`）。
