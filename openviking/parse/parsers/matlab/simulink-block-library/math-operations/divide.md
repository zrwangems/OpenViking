---
type: simulink-block
title: 'Divide'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'divide'
---

# Divide

Divide one input by another

## 中文

一个输入除以另一个输入

### 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

### 描述

Divide 模块输出其第一个输入除以第二个输入的结果。输入可以是两个标量、一个标量和一个非标量或者具有相同维度的两个非标量。当所有端口都具有相同的单精度或双精度数据类型时，此模块的除法端口仅支持复数输入值。

Divide 模块在功能上是预设了两个模块参数值的 Product 模块：

- **乘法 -** **按元素(.\*)**
- **输入数目 -** **\*/**

将这两个参数之一设置为非默认值即可将 Divide 模块更改为在功能上等效于 Product 模块或 Product of Elements 模块。

### 端口

#### 输入

#### **X** — 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组

要与其他输入相乘的输入信号。

##### 依赖关系

要启用一个或多个 **X** 端口，请为**输入数目**参数指定一个或多个 `*` 字符，并将**乘法**参数设置为**按元素(.\*)**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **÷** — 要进行除法或逆运算的输入信号 标量 | 向量 | 矩阵 | N 维数组

要进行除法或逆运算的输入信号。

##### 依赖关系

要启用一个或多个 **÷** 端口，请为**输入数目**参数指定一个或多个 `/` 字符，并将**乘法**参数设置为**按元素(.\*)**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_1** — 要进行乘法或除法运算的第一个输入 标量 | 向量 | 矩阵 | N 维数组

要进行乘法或除法运算的第一个输入，作为标量、向量、矩阵或 N 维数组提供。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_N** — 要进行乘法或除法运算的第 N 个输入 标量 | 向量 | 矩阵 | N 维数组

要进行乘法或除法运算的第 N 个输入，作为标量、向量、矩阵或 N 维数组提供。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **\*** — 要相乘的输入信号 标量 | 向量 | 矩阵 | N 维数组

要与其他输入相乘的输入信号。

##### 依赖关系

要启用一个或多个 **\*** 端口，请为**输入数目**参数指定一个或多个 `*` 字符，并将**乘法**参数设置为**矩阵(\*)**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Inv** — 要进行除法或逆运算的输入信号 标量 | 向量 | 矩阵 | N 维数组

要进行除法或逆运算的输入信号。

##### 依赖关系

要启用一个或多个 **Inv** 端口，请为**输入数目**参数指定一个或多个 `/` 字符，并将**乘法**参数设置为**矩阵(\*)**。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 通过对输入进行乘法、除法或逆运算来计算得出输出 标量 | 向量 | 矩阵 | N 维数组

通过对输入进行乘法、除法或逆运算来计算得出输出。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **输入数目** — 控制输入数目和运算的类型 `*/` (默认) | 正整数标量 | 对每个输入端口应用 `*` 或 `/`

控制模块的两个属性：

- 模块上的输入端口数
- 是乘以还是除以每个输入来得到输出

如果您指定：

- **`1` 或 `*` 或 `/`**

  模块有一个输入端口。在按元素模式下，模块按照 Product of Elements 模块说明处理输入。在矩阵模式下，如果参数值为 `1` 或 `*`，则模块将输出输入值。如果值为 `/`，则输入必须为方阵（包括作为简并情况的标量），模块将输出逆矩阵。有关详细信息，请参阅按元素模式和矩阵模式。
- **大于 1 的整数值**

  模块的输入数目由整数值指定。输入依**乘法**参数指定的按元素模式或矩阵模式相乘。有关详细信息，请参阅按元素模式和矩阵模式。
- **不带引号的含有两个或更多 `*` 和 `/` 字符的字符串**

  模块的输入数目由字符向量长度指定。乘以与 `*` 字符相对应的每个输入来得到输出。除以与 `/` 字符相对应的每个输入来得到输出。依**乘法**参数指定的按元素模式或矩阵模式进行运算。有关详细信息，请参阅按元素模式和矩阵模式。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**`'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **默认值：**`'*/'` |

#### **乘法** — 按元素 (.\*) 或矩阵 (\*) 乘法 **按元素(.\*)** (默认) | **矩阵(\*)**

指定模块是执行**按元素(.\*)** 还是**矩阵(\*)** 乘法。

##### 编程用法

|  |
| --- |
| **模块参数**：`Multiplication` |
| **类型：**字符向量 |
| **值：**`'Element-wise(.*)' | 'Matrix(*)'` |
| **默认值：**`'Element-wise(.*)'` |

#### **应用于** — 如何沿指定维度应用函数 **所有维度** (默认) | **指定的维度**

指定如何沿指定维度应用函数。

- **所有维度** - 对所有维度的所有输入值应用函数。
- **指定维度** - 对指定维度的所有输入值应用函数。

例如，在此模型中，将**乘法**设置为**按元素方式(.\*)**，将**应用于**设置为**所有维度**。该模块返回所有维度的所有值的乘积。

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for all dimensions

##### 依赖关系

要启用此参数，请将**输入数目**设置为 `*` 并将**乘法**设置为**按元素(.\*)**。

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseMode` |
| **类型：**字符向量 |
| **值：**`'All dimensions' | 'Specified dimension'` |
| **默认值：**`'All dimensions'` |

#### **维度** — 要沿其相乘的维度 `1` (默认) | 正整数

指定要沿其相乘的维度，值为正整数。例如，对于二维矩阵，`1` 将函数应用于每列，`2` 将函数应用于每行。

例如，在此模型中，将**乘法**设置为**按元素方式(.\*)**，将**应用于**设置为**指定的维度**，将**维度**设置为 `2`。该模块返回每行中所有值的乘积。

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for dimension 2

##### 依赖关系

要启用此参数，请进行如下设置：

- 将**输入数目**设置为 `*`
- 将**乘法**设置为**按元素(.\*)**
- 将**应用于**设置为**指定的维度**

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseDim` |
| **类型：**字符向量 |
| **值：**`'1' | '2' | ...` |
| **默认值：**`'1'` |

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

#### **要求所有输入具有相同的数据类型** — 要求所有输入具有相同的数据类型 `off` (默认) | `on`

指定输入信号是否必须全部具有相同的数据类型。如果启用此参数，则在输入信号类型不同时，仿真过程中会发生错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

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

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **继承: 与第一个输入相同** | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。有关详细信息，请参阅 控制信号的数据类型。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。例如，如果该模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 **ASIC/FPGA** 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定**未指定(假定通用 32 位)**（即通用 32 位微处理器）为目标硬件，则输出数据类型为 `int32`。如果目标微处理器不能提供适应输出范围的字长，Simulink 软件将在诊断查看器中显示错误。

  有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果内部规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 使用简单的选项**继承: 与输入相同**。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。
- **继承: 与第一个输入相同** - 使用第一个输入信号的数据类型。

##### 依赖关系

当输入是小于单精度的浮点数据类型时，**继承: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当对数据类型进行编码所需的位数小于对单精度数据类型编码所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

选择定点运算的舍入模式。您可以选择：

**向上**
:   朝正无穷方向舍入正数和负数。等同于 MATLAB® `ceil` 函数。

**收敛**
:   将数值舍入到最邻近的可表示值。如果出现结值，则舍入到最邻近的偶数整数。等同于 Fixed-Point Designer™ `convergent` 函数。

**向下**
:   朝负无穷方向舍入正数和负数。等同于 MATLAB `floor` 函数。

**最邻近值**
:   将数值舍入到最邻近的可表示值。如果出现结值，则朝正无穷方向舍入。等同于 Fixed-Point Designer `nearest` 函数。

**舍入**
:   将数值舍入到最邻近的可表示值。如果出现结值，则将正数朝正无穷方向舍入，将负数朝负无穷方向舍入。等同于 Fixed-Point Designer `round` 函数。

**最简**
:   在向负无穷大方向舍入和向零舍入之间选择，以生成尽可能有效的舍入代码。这种舍入模式受**硬件实现**窗格中的以下配置参数的影响。

    - 如果**有符号整数除法舍入方式**参数设置为**零**或**未定义**，则**最简**解析为零。
    - 如果**有符号整数除法舍入方式**参数设置为**向下**，则**最简**解析为 `floor`。

**零**
:   将数值向零舍入。等同于 MATLAB `fix` 函数。

有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

##### 编程用法

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型：**字符向量 |
| **值：**`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：**`'Floor'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

#### **模式** — 选择数据类型模式 `Inherit` (默认) | `Built in` | `Fixed Point`

选择要指定的数据类别。

- **继承** - 数据类型的继承规则。选择 `Inherit` 将在右侧启用另一个菜单/文本框，您可以在其中选择继承模式。
- **内置** - 内置数据类型。选择 `Built in` 将在右侧启用另一个菜单/文本框，您可以在其中选择内置数据类型。
- **定点** - 定点数据类型。选择**定点**将启用可用于指定定点数据类型的其他参数。
- **表达式** - 计算结果为数据类型的表达式。选择 `Expression` 将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请点击**显示数据类型助手**按钮。

#### **数据类型覆盖** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 **inherit** 时，Simulink 从信号的上下文（即：从 Simulink 中使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）中继承数据类型覆盖设置。
- 当您选择 **off** 时，Simulink 忽略信号上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Simulink 文档中的使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**内置**或**定点**。

##### 提示

由于能够关闭单个数据类型的数据类型覆盖，您可以在应用数据类型覆盖时更好地控制模型中的数据类型。例如，您可以使用此选项确保数据类型满足下游模块的要求，而忽略数据类型覆盖设置。

#### **符号性** — 指定有符号或无符号 `Signed` (默认) | `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，无符号数据只表示正值。

- **有符号**，将定点数据指定为有符号数据。
- **无符号**，将定点数据指定为无符号数据。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为 `Fixed point`。

#### **字长** — 存储量化整数的字的位大小 `16` (默认) | 从 0 到 32 的整数

指定存储量化整数的字的位大小。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **小数长度** — 指定定点数据类型的小数长度 `0` (默认) | 整数标量

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**二进制小数点**。

#### **定标** — 定标定点数据的方法 **最佳精度** (默认) | **二进制小数点** | **斜率和偏置**

指定定点数据的定标方法，以避免发生溢出情况并最大限度地减少量化误差。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**模式**设置为**定点**。

#### **斜率** — 指定定点数据类型的斜率。 `2^0` (默认) | 正实数值标量

指定定点数据类型的斜率。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

#### **偏置** — 指定定点数据类型的偏置。 `0` (默认) | 实数值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**斜率和偏置**。

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

**仿真与代码生成之间的预期差异**

这些条件可能在仿真和生成的代码之间产生不同结果：

- Divide 模块输入包含 `NaN` 或 `inf` 值
- 在执行过程中，Divide 模块生成 `NaN` 或 `inf`

这种差异是由非有限 `NaN` 或 `inf` 值引起的。在这种情况下，请检查模型配置，并消除产生 `NaN` 或 `inf` 的条件。

**代码优化**

Simulink Coder™ 编译过程为矩阵求逆和除法运算提供了高效率代码。下表说明了其主要优势以及每种优势的适用场景。

| 优势 | 小型矩阵  （2×2 到 5×5） | 中型矩阵  （6×6 到 20×20） | 大型矩阵  （大于 20×20） |
| --- | --- | --- | --- |
| 与 R2011a 及更早版本相比，代码执行时间更短 | 是 | 否 | 是 |
| 与 R2011a 及更早版本相比，减少了对 ROM 和 RAM 的使用 | 是（对于实数值） | 是（对于实数值） | 是（对于实数值） |
| 重用变量 | 是 | 是 | 是 |
| 死代码消除 | 是 | 是 | 是 |
| 常量折叠 | 是 | 是 | 是 |
| 表达式折叠 | 是 | 是 | 是 |
| 与 MATLAB Coder 结果一致 | 是 | 是 | 是 |

对于具有不同维度的三个或更多输入的模块，代码可能包含额外的缓冲区来存储中间结果的临时变量。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

要执行针对 HDL 进行了优化的除法运算，请将 Product 模块连接到倒数模式的 Divide 模块。

**HDL 架构**

Divide 模块与**输入数目**设置为 `*/` 的 Product 模块相同。

| 架构 | 描述 |
| --- | --- |
| **ShiftAdd(默认值)** | 通过使用非还原除法算法执行除法运算，该算法执行多次移位相加运算来计算商。  使用定点数据类型时，必须满足以下标准才能生成 HDL 代码：  - 输入字长 (`WL`) 必须小于 63。 - `[Max(WL input1, WL input2) + Abs(FL Difference)]`  必须小于 63。其中，小数长度 (FL) 差由下式给出：  `FL Difference = FL input1 - (FL input2 + FL output)` |

**倒数模式**

当**输入数目**设置为 `/` 时，Divide 模块处于倒数模式。

| 架构 | 描述 |
| --- | --- |
| **ShiftAdd(默认值)** | 通过使用非还原除法算法执行倒数运算，该算法执行多次移位相加运算来计算倒数。  使用定点数据类型时，必须满足以下标准才能生成 HDL 代码：  - 输入字长 (`WL`) 必须小于或等于 63。 - `[WL input + Abs(FL Sum)]` 必须小于或等于 63。其中， `FL Sum` 由下式给出：  `FL sum = FL input + FL output` |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 要启用此属性，请将 HDL 架构设置为 **ShiftAdd**。对于定点和浮点类型，指定是将设计中的模块映射到 `MAX`、`Min`、`Custom` 还是 `ZERO` 延迟。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。  您可以通过将 **LatencyStrategy** 设置为 `Custom(PerIterations)` 来控制迭代算法的流水线阶段。有关详细信息，请参阅Divide (HDL Coder)。 |
| **CustomLatency** | 要启用此属性，请将 HDL 架构设置为 **ShiftAdd**。当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅LatencyStrategy (HDL Coder)。 |
| **IterationsPerPipeline** | 当 **LatencyStrategy** 设置为 `Custom(PerIterations)` 时，使用此设置指定每个流水线阶段的迭代次数。  有关详细信息，请参阅Divide (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同设置，您可以控制目标 FPGA 设备上 DSP 的使用。默认值为 **inherit**。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |
| **DivisionAlgorithm** | 指定是使用 Radix-2 还是 Radix-4 算法来执行浮点除法。Radix-2 模式提供延迟和频率之间的折衷。Radix-4 模式提供延迟和资源使用量之间的折衷。有关详细信息，请参阅 DivisionAlgorithm (HDL Coder)。 |

**延迟详细信息**

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

**原生浮点延迟**

| 运算符 | 浮点类型 | 延迟策略 | 延迟（周期数） | 自定义延迟支持 |
| --- | --- | --- | --- | --- |
| 除法 | 双精度 | 最小值 | 31 | 是 |
| 最大值 | 61 |
| 单精度 | 最小值 | 17 |
| 最大值 | 32 |
| 半精度 | 最小值 | 10 |
| 最大值 | 19 |
| 倒数 | 双精度 | 最小值 | 6 | 是 |
| 最大值 | 9 |
| 单精度 | 最小值 | 6 |
| 最大值 | 8 |
| 半精度 | 最小值 | 4 |
| 最大值 | 7 |

**定点延迟**

| 运算符 | 额外的延迟周期 | 延迟策略支持 | 自定义延迟支持 |
| --- | --- | --- | --- |
| 除法 | 取决于输入和输出的字长和小数长度。有关详细信息，请参阅 `HDLMathLib` Divide (HDL Coder)。 | 是 | 是 |
| 倒数 | 取决于输入和输出的字长和小数长度。有关详细信息，请参阅 `HDLMathLib` Reciprocal (HDL Coder)。 | 是 | 是 |

**模块参数配置**

HDL 代码生成支持 **ShiftAdd** 中 `divide (*/)` 和 `reciprocal (/)` 运算的不同输出数据类型。您可以对模块使用下列输出数据类型：

- **继承: 从内部规则继承**
- **继承: Keep MSB**
- **继承: Match scaling**
- **继承: 通过反向传播继承**​
- **继承: 与第一个输入相同**
- **整数类型(uint8,int8,uint16,int16,uint32,int32,uint64,int64)**
- **定点类型**
- **浮点类型**

您可以对该模块使用以下整数舍入模式：

| 模块 | 整数舍入模式 |
| --- | --- |
| 除法 | - **零** - **最简** - **向上** *(自 R2025a 起)* - **收敛** *(自 R2025a 起)* - **向下** *(自 R2025a 起)* - **最邻近值** *(自 R2025a 起)* - **舍入** *(自 R2025a 起)* |
| 倒数 | - **零** - **向上** *(自 R2025a 起)* - **收敛** *(自 R2025a 起)* - **向下** *(自 R2025a 起)* - **最邻近值** *(自 R2025a 起)* - **舍入** *(自 R2025a 起)* - **最简** *(自 R2025a 起)* |

**注意**

在将生成的 HDL 代码部署到目标硬件时，请确保在“配置参数”对话框的**硬件实现**窗格中将**有符号整数除法舍入方式**参数设置为**零**或**向下**。

**复数数据支持**

此模块不支持复信号除法的代码生成。

**优化**

您可以使用以下 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 确定多个在功能上等效的资源，并用单个资源替换它们。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，其中 HDL Coder 将向量数据路径变换为标量数据路径（或多个较小的向量数据路径）。 |

您可以使用 **ShiftAdd** 架构对 Divide 和 Reciprocal 模块应用共享或流优化。

| 模块输入 | 资源复用 | 流式传输 |
| --- | --- | --- |
| 除法（/\* 或 \*/） | 是 | 是 |
| 倒数 (/) | 是 | 否 |

在这些模块上使用共享优化时，请确保将该模块包含在原子子系统中，并将**默认参数行为**配置参数设置为**内联**。

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。  对于 Divide 和 Reciprocal 模块，HDL Coder 在模块周围（而不是在模块内）分布流水线寄存器。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**I/O 优化**

| 优化 | 描述 |
| --- | --- |
| 帧到采样的转换 (HDL Coder) | 要优化您的设计所需的 I/O，请使用帧到采样的转换。这种优化将基于帧的向量或矩阵输入转换为更小的采样或像素，以便 HDL 代码生成到基于流的目标硬件，并减小处理大输入和输出信号所需的 FPGA I/O。 |

**HDL 建模规范**

有关使用该模块的最佳做法，请参阅：

- Design Considerations for Matrices and Vectors (HDL Coder)
- Modeling Efficient Multiplication and Division Operations for FPGA Targeting (HDL Coder)
- Guidelines for Using Rounding and Saturation Settings for Fixed-Point Data Types (HDL Coder)

**限制**

当您在倒数模式下使用 Divide 模块时，存在以下限制：

- 当使用定点类型时，输入和输出必须为标量。要使用向量输入，请使用浮点类型输入和输出。
- 您必须为模块选择**对整数溢出进行饱和处理**选项。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Description

The Divide block outputs the result of dividing its first input by its
second. The inputs can be scalars, a scalar and a nonscalar, or two nonscalars that have
the same dimensions. This block supports only complex input values at division ports
when all ports have the same single or double data type.

The Divide block is functionally a Product block that has two block
parameter values preset:

- **Multiplication —**
  `Element-wise(.*)`
- **Number of Inputs —**
  `*/`

Setting nondefault values for either of those parameters can change a Divide
block to be functionally equivalent to a Product block or a Product of Elements block.

## Ports

### Input

### **X** — Input signal to multiply scalar | vector | matrix | N-D array

Input signal to be multiplied with other inputs.

#### Dependencies

To enable one or more **X** ports, specify one or
more `*` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Element-wise(.*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **÷** — Input signal to divide or invert scalar | vector | matrix | N-D array

Input signal for division or inversion operations.

#### Dependencies

To enable one or more **÷** ports, specify one or
more `/` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Element-wise(.*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_1** — First input to multiply or divide scalar | vector | matrix | N-D array

First input to multiply or divide, provided as a scalar, vector,
matrix, or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — Nth input to multiply or divide scalar | vector | matrix | N-D array

Nth input to multiply or divide, provided as a scalar, vector, matrix,
or N-D array.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **\*** — Input signal to multiply scalar | vector | matrix | N-D array

Input signal to be multiplied with other inputs.

#### Dependencies

To enable one or more **\*** ports, specify one or
more `*` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Matrix(*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Inv** — Input signal to divide or invert scalar | vector | matrix | N-D array

Input signal for division or inversion operations.

#### Dependencies

To enable one or more **Inv** ports, specify one
or more `/` characters for the **Number of
inputs** parameter and set the
**Multiplication** parameter to
`Matrix(*)`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output computed by multiplying, dividing, or inverting inputs scalar | vector | matrix | N-D array

Output computed by multiplying, dividing, or inverting inputs.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Number of inputs** — Control number of inputs and type of operation `*/` (default) | positive integer scalar | `*` or `/` for each input port

Control two properties of the block:

- The number of input ports on the block
- Whether each input is multiplied or divided into the
  output

When you specify:

- **`1` or
  `*` or
  `/`**

  The block has one input port. In element-wise mode, the block
  processes the input as described for the Product of
  Elements block. In matrix mode, if the parameter
  value is `1` or `*`, the block
  outputs the input value. If the value is `/`,
  the input must be a square matrix (including a scalar as a
  degenerate case) and the block outputs the matrix inverse. See
  Element-Wise Mode and Matrix Mode for more
  information.
- **Integer value > 1**

  The block has the number of inputs given by the integer value.
  The inputs are multiplied together in element-wise mode or
  matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.
- **Unquoted string of two or more
  `*` and `/`
  characters**

  The block has the number of inputs given by the length of the
  character vector. Each input that corresponds to a
  `*` character is multiplied into the
  output. Each input that corresponds to a `/`
  character is divided into the output. The operations occur in
  element-wise mode or matrix mode, as specified by the **Multiplication** parameter. See Element-Wise Mode and Matrix Mode for more
  information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** `'2' | '*' | '**' | '*/' | '*/*' | ...` |
| **Default:** `'*/'` |

### **Multiplication** — Element-wise (.\*) or Matrix (\*) multiplication `Element-wise(.*)` (default) | `Matrix(*)`

Specify whether the block performs `Element-wise(.*)` or
`Matrix(*)` multiplication.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Multiplication` |
| **Type:** character vector |
| **Values:** `'Element-wise(.*)' | 'Matrix(*)'` |
| **Default:** `'Element-wise(.*)'` |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply the function along specified dimensions.

- `All dimensions` — Apply function for all input
  values for all dimensions.
- `Specified dimension` — Apply function for all input
  values for specified dimension.

For example, in this model, **Multiplication** is set to
`Element-wise(.*)`, and **Apply over**
is set to `All dimensions`. The block returns the product of
all values from all dimensions.

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for all dimensions

#### Dependencies

To enable this parameter, set **Number of inputs** to
`*` and **Multiplication** to
`Element-wise (.*)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseMode` |
| **Type:** character vector |
| **Values:** `'All dimensions' | 'Specified dimension'` |
| **Default:** `'All dimensions'` |

### **Dimension** — Dimension along which to multiply `1` (default) | positive integer

Specify the dimension along which to multiply, as a
positive integer. For example, for a 2-D matrix, `1`
applies the function to each column, and `2` applies
the function to each row.

For example, in this model,
**Multiplication** is set to
`Element-wise(.*)`,
**Apply over** is set to
`Specified dimension`,
and **Dimension** is set to
`2`. The block returns the
product of all values from each row.

2D matrix with Constant block value [1 2 3;7 6 4] as input to Product block configured for dimension 2

#### Dependencies

To enable this parameter:

- Set **Number of inputs** to
  `*`
- Set **Multiplication** to
  `Element-wise
  (.*)`
- Set **Apply over** to
  `Specified
  dimension`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseDim` |
| **Type:** character vector |
| **Values:** `'1' | '2' | ...` |
| **Default:** `'1'` |

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

### **Require all inputs to have the same data type** — Require that all inputs have the same data type `off` (default) | `on`

Specify if input signals must all have the same data type. If you enable
this parameter, then an error occurs during simulation if the input
signal types are different.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`. For more information, see
Control Data Types of Signals.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal rule`
  — Simulink® chooses a data type to balance numerical
  accuracy, performance, and generated code size, while taking
  into account the properties of the embedded target hardware.
  If you change the embedded target settings, the data type
  selected by the internal rule might change. For example, if
  the block multiplies an input of type
  `int8` by a gain of
  `int16` and
  `ASIC/FPGA` is specified as
  the targeted hardware type, the output data type is
  `sfix24`. If
  `Unspecified (assume 32-bit
  Generic)`, in other words, a generic
  32-bit microprocessor, is specified as the target hardware,
  the output data type is `int32`. If none of
  the word lengths provided by the target microprocessor can
  accommodate the output range, Simulink software displays an error in the Diagnostic
  Viewer.

  It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If the
  internal rule doesn’t meet your specific needs for numerical
  accuracy or performance, use one of the following options:

  - Specify the output data type
    explicitly.
  - Use the simple choice of
    `Inherit: Same as
    input`.
  - Explicitly specify a default data type such
    as `fixdt(1,32,16)` and then use
    the Fixed-Point Tool to propose data types for
    your model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use data type of the
  driving block.
- `Inherit: Same as first input` — Use
  data type of first input signal.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting
of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
precision when the number of bits needed to encode the data type is
less than the 32 bits needed to encode the single-precision data
type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Same as first input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding mode for fixed-point operations. You can
select:

`Ceiling`
:   Rounds positive and negative numbers toward positive
    infinity. Equivalent to the MATLAB®
    `ceil` function.

`Convergent`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds to the nearest even integer. Equivalent to
    the Fixed-Point Designer™
    `convergent` function.

`Floor`
:   Rounds positive and negative numbers toward negative
    infinity. Equivalent to the MATLAB
    `floor` function.

`Nearest`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds toward positive infinity. Equivalent to the
    Fixed-Point Designer
    `nearest` function.

`Round`
:   Rounds number to the nearest representable value. If a tie
    occurs, rounds positive numbers toward positive infinity and
    rounds negative numbers toward negative infinity. Equivalent
    to the Fixed-Point Designer
    `round` function.

`Simplest`
:   Chooses between rounding toward floor and rounding toward
    zero to generate rounding code that is as efficient as
    possible. This rounding mode is affected by these
    configuration parameters on the **Hardware
    Implementation** pane.

    - If the **Signed integer division rounds
      to** parameter is set to
      `Zero` or
      `Undefined`,
      `Simplest` resolves to
      zero.
    - If the **Signed integer division rounds
      to** parameter is set to
      `Floor`,
      `Simplest` resolves to
      `floor`.

`Zero`
:   Rounds number toward zero. Equivalent to the MATLAB
    `fix` function.

For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function into the mask field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

### **Mode** — Select data type mode `Inherit` (default) | `Built in` | `Fixed Point`

Select the category of data to specify.

- `Inherit` — Inheritance rules for data types.
  Selecting `Inherit` enables a second menu/text box to the right
  where you can select the inheritance mode.
- `Built in` — Built-in data types. Selecting
  `Built in` enables a second menu/text box to the right
  where you can select a built-in data type.
- `Fixed point` — Fixed-point data types. Selecting
  `Fixed point` enables additional parameters that
  you can use to specify a fixed-point data type.
- `Expression` — Expressions that evaluate to data
  types. Selecting `Expression` enables a second menu/text box to
  the right, where you can enter the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

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

**Expected Differences Between Simulation and Code Generation**

These conditions may yield different results between simulation and the
generated code:

- The Divide block inputs contain a
  `NaN` or `inf` value
- The Divide block generates `NaN` or
  `inf` during execution

This difference is due to the nonfinite `NaN` or
`inf` values. In such cases, inspect your model
configuration and eliminate the conditions that produce `NaN`
or `inf`.

**Code Optimizations**

The Simulink
Coder™ build process provides efficient code for matrix inverse and
division operations. This table describes the benefits and when each benefit is
available.

| Benefit | Small Matrices  (2-by-2 to 5-by-5) | Medium Matrices  (6-by-6 to 20-by-20) | Large Matrices  (larger than 20-by-20) |
| --- | --- | --- | --- |
| Faster code execution time, compared to R2011a and earlier releases | Yes | No | Yes |
| Reduced ROM and RAM usage, compared to R2011a and earlier releases | Yes, for real values | Yes, for real values | Yes, for real values |
| Reuse of variables | Yes | Yes | Yes |
| Dead code elimination | Yes | Yes | Yes |
| Constant folding | Yes | Yes | Yes |
| Expression folding | Yes | Yes | Yes |
| Consistency with MATLAB Coder results | Yes | Yes | Yes |

For blocks that have three or more inputs of different dimensions, the code
might include an extra buffer to store temporary variables for intermediate
results.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

To perform an HDL-optimized divide operation, connect a Product block to a Divide
block and set the **Number of Inputs parameter** of the Divide
block to `/`.

**HDL Architecture**

The Divide block is the same as a Product block
with **Number of Inputs** set to `*/`.

| Architecture | Description |
| --- | --- |
| `ShiftAdd` (Default) | Perform divide operations by using a non-restoring division algorithm that performs multiple shift and add operations to compute the quotient.  When **Architecture** is set to `ShiftAdd`, the block uses pipelined architecture that breaks the computation into stages. This pipelined design introduces latency in HDL implementation. You can specify the latency by using the **LatencyStrategy** HDL block property. By default, **LatencyStrategy** is set to `Max`. To implement the block without latency, set **LatencyStrategy** to `Zero`. |

**Reciprocal Mode**

When **Number of Inputs** is set to `/`, the
Divide block is in reciprocal mode.

| Architectures | Description |
| --- | --- |
| `ShiftAdd` (Default) | Perform reciprocal operation by using a non-restoring division algorithm that performs multiple shift and add operations to compute the reciprocal. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **LatencyStrategy** | To enable this property, set HDL architecture to `ShiftAdd`. Specify whether to map the blocks in your design to `MAX`, `Min`, `Custom`, or `ZERO` latency for fixed-point and floating-point types. The default is `inherit`. See also LatencyStrategy (HDL Coder).  You can control the pipeline stages for the iterative algorithm by setting the **LatencyStrategy** to `Custom(PerIterations)`. For more information, see Divide (HDL Coder). |
| **CustomLatency** | To enable this property, set HDL architecture to `ShiftAdd`. When **LatencyStrategy** is set to `CUSTOM`, use this property to specify a custom latency value between `ZERO` and `MAX` for fixed-point types. See also LatencyStrategy (HDL Coder). |
| **IterationsPerPipeline** | When you set **LatencyStrategy** to `Custom(PerIterations)`, use this setting to specify the number of iterations per pipeline stages.  For more information, see Divide (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |
| **DivisionAlgorithm** | Specify whether to use the Radix-2 or Radix-4 algorithm to perform the floating-point division. The Radix-2 mode offers a tradeoff between latency and frequency. The Radix-4 mode offers a tradeoff between latency and resource usage. For more information, see DivisionAlgorithm (HDL Coder). |

**Latency Details**

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

**Native Floating-Point Latency**

| Operator | Floating-Point Type | Latency Strategy | Latency (in cycles) | Custom Latency Support |
| --- | --- | --- | --- | --- |
| Divide | Double | Min | 31 | Yes |
| Max | 61 |
| Single | Min | 17 |
| Max | 32 |
| Half | Min | 10 |
| Max | 19 |
| Reciprocal | Double | Min | 6 | Yes |
| Max | 9 |
| Single | Min | 6 |
| Max | 8 |
| Half | Min | 4 |
| Max | 7 |

**Fixed-Point Latency**

| Operator | Additional cycles of latency | Latency Strategy Support | Custom Latency Support |
| --- | --- | --- | --- |
| Divide | Depends on word-length and fractional-length of input and output. For more information, see `HDLMathLib` Divide (HDL Coder). | Yes | Yes |
| Reciprocal | Depends on word-length and fractional-length of input and output. For more information, see `HDLMathLib` Reciprocal (HDL Coder). | Yes | Yes |

**Block Parameter Configuration**

HDL code generation supports different output data types for `divide
(*/)` and `reciprocal (/)` operations in
`ShiftAdd`. You can use these output data types for
the blocks:

- `Inherit: Inherit via internal
  rule`
- `Inherit: Keep MSB​`
- `Inherit: Match scaling​`
- `Inherit: Inherit via back
  propagation`​
- `Inherit: Same as first input​`
- `Integer types
  (uint8,int8,uint16,int16,uint32,int32,uint64,int64)​`
- `Fixed point types​`
- `Floating-point types`

You can use these integer rounding modes for the block:

| Blocks | Integer Rounding Modes |
| --- | --- |
| Divide | - `Zero` - `Simplest` - `Ceiling` *(since R2025a)* - `Convergent` *(since R2025a)* - `Floor` *(since R2025a)* - `Nearest` *(since R2025a)* - `Round` *(since R2025a)* |
| Reciprocal | - `Zero` - `Ceiling` *(since R2025a)* - `Convergent` *(since R2025a)* - `Floor` *(since R2025a)* - `Nearest` *(since R2025a)* - `Round` *(since R2025a)* - `Simplest` *(since R2025a)* |

**Note**

When you deploy the generated HDL code onto the target hardware, make sure
that you set the **signed integer division rounds to**
parameter in the **Hardware Implementation** pane of the
Configuration Parameters dialog box to `Zero` or
`Floor`.

**Complex Data Support**

This block does not support code generation for division with
complex signals.

**Optimizations**

You can use these HDL Coder optimizations to optimize the speed, area, and
I/Os.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

You can apply the sharing or streaming optimizations for Divide and Reciprocal
blocks using `ShiftAdd` architecture.

| Block (Inputs) | Resource Sharing | Streaming |
| --- | --- | --- |
| Divide(/\* or \*/) | Yes | Yes |
| Reciprocal (/) | Yes | No |

When you use sharing optimization on these blocks, make sure to enclose the
block in the atomic subsystem and set the **Default parameter
behavior** configuration parameter to
`Inlined`.

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior.  For the Divide and Reciprocal blocks, HDL Coder distributes pipeline registers around the blocks instead of within them. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**I/O Optimization**

| Optimization | Description |
| --- | --- |
| Frame to Sample Conversion (HDL Coder) | To optimize the I/O needed for your design, use frame-to-sample conversion. This optimization converts frame-based vector or matrix inputs to smaller-sized samples or pixels for HDL code generation to target stream-based hardware and reduce the FPGA I/O needed to handle large input and output signals. |

**HDL Modeling Guidelines**

For best practices of using the block, see:

- Design Considerations for Matrices and Vectors (HDL Coder)
- Modeling Efficient Multiplication and Division Operations for FPGA Targeting (HDL Coder)
- Guidelines for Using Rounding and Saturation Settings for Fixed-Point Data Types (HDL Coder)

**Restrictions**

When you use the Divide block in reciprocal mode, the following
restrictions apply:

- When you use fixed-point types, the input and output must be scalar.
  To use vector inputs, use floating-point types input and output.
- You must select the **Saturate on integer overflow**
  option on the block.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Divide and Reciprocal blocks use ShiftAdd as default architecture

The **Architecture** HDL block property is now
`ShiftAdd` by default for the Divide and Reciprocal
blocks. The code generated with the `ShiftAdd` setting is
more hardware-friendly than the other existing architectures.

These architecture settings were removed from the
**Architecture** HDL block property in the Divide and
Reciprocal blocks:

| Blocks | Architecture Settings |
| --- | --- |
| Divide | `Linear` |
| Reciprocal | `Linear`  `ReciprocalRsqrtBasedNewtonSingleRate` |

The linear architecture was using division operator (/) for implementing the
block, which did not support pipelining. This results to long combinational paths
and lower performance. The shift-add architecture uses pipelined architecture that
breaks the computation into stages. This pipelined design introduces latency in HDL
implementation. To implement the block without latency, set
**LatencyStrategy** to `Zero`.
