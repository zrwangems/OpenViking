---
type: simulink-block
title: 'Gain'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'gain'
---

# Gain

Multiply input by constant

## 中文

将输入乘以常量

### 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

### 描述

Gain 模块将输入乘以一个常量值，即增益。输入和增益可以是标量、向量或矩阵。

在**增益**参数中指定增益的值。**乘法**参数用于指定按元素还是矩阵乘法。对于矩阵乘法，此参数还用于指示被乘数的阶。

通过舍入到最邻近整数和饱和操作将增益从双精度型离线转换为模块封装中指定的数据类型。然后将输入和增益相乘，结果通过指定的舍入和溢出模式转换为输出数据类型。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

Gain 模块接受实数或复数值标量、向量或矩阵输入。Gain 模块支持定点数据类型。如果 Gain 模块的输入为实数，增益为复数，则输出为复数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输入乘以增益 标量 | 向量 | 矩阵

Gain 模块的输出是输入乘以常量增益值的结果。当 Gain 模块的输入为实数且增益为复数时，输出为复数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持:** 是

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

#### 常设

#### **增益** — 要与输入相乘的值 `1` (默认) | 实数或复数值标量、向量或矩阵

指定要与输入相乘的值。增益可以是实数或复数值标量、向量或矩阵。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Gain` |
| **值:** | `'1'` (默认) | real or complex-valued scalar, vector, or matrix in quotes |

#### **乘法** — 指定乘法模式 **按元素(K.\*u)** (默认) | **矩阵(K\*u)** | **矩阵(u\*K)** | **矩阵(K\*u) (u 向量)**

指定下列乘法模式之一：

- **按元素(K.\*u)** - 输入的每个元素乘以增益的每个元素。如有必要，该模块会执行扩展，以使输入和增益具有相同的维度。
- **矩阵(K\*u)** - 输入和增益按矩阵乘法方式相乘，其中输入为第二个操作数。
- **矩阵(u\*K)** - 输入和增益按矩阵乘法方式相乘，其中输入为第一个操作数。
- **矩阵(K\*u) (u 向量)** - 输入和增益按矩阵乘法方式相乘，其中输入为第二个操作数。除了确定维度的方式，此模式与 `Matrix(K*u)` 相同。

  假设 `K` 是一个 `m-by-n` 矩阵。`Matrix(K*u)(u vector)` 将输入设置为长度为 `n` 的向量，将输出设置为长度为 `m` 的向量。相比之下，`Matrix(K*u)` 则是使用传播来确定输入和输出的维度。对于 `m-by-n` 增益矩阵，输入可以传播到 `n-by-q` 矩阵，并且输出变为 `m-by-q` 矩阵。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Multiplication` |
| **值:** | `'Element-wise(K.*u)'` (默认) | `'Matrix(K*u)'` | `'Matrix(u*K)'` | `'Matrix(K*u) (u vector)'` |

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

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: Keep MSB** | **继承: Match scaling** | **继承: 通过反向传播继承** | **继承: 与输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **int64** | **uint64** | **uint32** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - 软件在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。如果更改了嵌入式目标的设置，则依内部规则选择的数据类型可能会发生变化。例如，如果该模块将 `int8` 类型的输入乘以 `int16` 的增益，并且将 **ASIC/FPGA** 指定为目标硬件类型，则输出数据类型为 `sfix24`。如果指定**未指定(假定通用 32 位)**（即通用 32 位微处理器）为目标硬件，则输出数据类型为 `int32`。如果目标微处理器不能提供适应输出范围的字长，软件将在诊断查看器中显示错误。
- **继承: 保留 MSB** - 软件选择一种能够保持运算的完整范围的数据类型，然后将输出精度降低到适合嵌入式目标硬件的大小。

  **提示**

  要获得更高效的生成代码，请清除**对整数溢出进行饱和处理**。

  此规则从不产生溢出。
- **继承: 匹配定标** - 软件选择一种数据类型，其定标与输入类型的定标相匹配。如果该类型的完整范围不适合嵌入式目标硬件，则该范围会缩小，从而生成适合嵌入式目标硬件的类型。此规则可能产生溢出。

  有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果这些内部规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 使用简单的选项**继承: 与输入相同**。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**并使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。
- **继承: 与输入相同** - 使用输入信号的数据类型。

##### 依赖关系

当输入是小于单精度的浮点数据类型时，**继承:通过内部规则继承**输出数据类型取决于**继承小于单精度的浮点输出类型**配置参数的设置。当对数据类型进行编码所需的位数小于对单精度数据类型编码所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

#### **模式** — 选择数据类型模式 **继承** (默认) | **内置** | **定点**

选择要指定的数据类别。

- **继承** - 数据类型的继承规则。选择 `Inherit` 将在右侧启用另一个菜单/文本框，您可以在其中选择继承模式。
- **内置** - 内置数据类型。选择 `Built in` 将在右侧启用另一个菜单/文本框，您可以在其中选择内置数据类型。
- **定点** - 定点数据类型。选择**定点**将启用可用于指定定点数据类型的其他参数。
- **表达式** - 计算结果为数据类型的表达式。选择 `Expression` 将在右侧启用另一个菜单/文本框，您可以在其中输入表达式。

有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请点击显示数据类型助手按钮 。

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

#### **小数长度** — 指定定点数据类型的小数长度 `0` (默认) | 整数标量

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅指定定点数据类型。

##### 依赖关系

要启用此参数，请将**定标**设置为**二进制小数点**。

#### 参数属性

#### **参数最小值** — 指定增益的最小值 `[]` (默认) | 标量

指定增益的最小值。默认值为 `[]`（未指定）。软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ParamMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **参数最大值** — 指定增益的最大值 `[]` (默认) | 标量

指定增益的最大值。默认值为 `[]`（未指定）。软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ParamMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **参数数据类型** — 指定 Gain 参数的数据类型 **继承: 从内部规则继承** (默认) | **继承: 与输入相同** | **继承: 从 '增益' 继承** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定**增益**参数的数据类型。

将**参数数据类型**设置为**继承:通过内部规则继承**允许 Gain 模块基于内部启发式方法选择数据类型，该算法查看当前增益值，并提供全精度数据类型来表示当前增益值。当您更新图时，软件会推断出一种适用于增益值 `3` 的高精度且无范围损失的数据类型。例如，使用这种启发式方法，如果指定的增益值是 `3`，则 Gain 模块推断出 `sfix32_En29` 的所选数据类型。因此，这种推断出的数据类型无法保留大于 `4` 的值。在仿真期间，如果将增益值调节为 `6`，则所选数据类型中会发生溢出，并且该行为是非预期行为。

使用此**参数数据类型**设置调节参数时，请指定**参数最小值**和**参数最大值**参数。这些设置指定软件在仿真期间您需要的值的范围，并允许软件提供具有足够范围的全精度数据类型，以支持在指定范围内安全调节增益值。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ParamDataTypeStr` |
| **值:** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Same as input'` | `'Inherit: Inherit from 'Gain''` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

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

**可调参数**

您可以在 Gain 模块中使用可调参数，用于 HDL 代码生成。有关详细信息，请参阅Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

| `ConstMultiplierOptimization` | 描述 |
| --- | --- |
| `none`（*默认值*） | 默认情况下，HDL Coder 不执行 CSD 或 FCSD 优化。为 Gain 模块生成的代码会保留乘法器运算。 |
| `csd` | 当您指定此选项时，生成的代码会使用正则有符号数 (CSD) 方法减少模型使用的面积，同时保持或提高时钟速度。CSD 用加减运算取代乘法器运算。  CSD 使用尽可能少的非零位来表示二进制数，从而最大程度地减少常量乘法所需的加法运算次数。 |
| `fcsd` | 此选项使用分解的 CSD (FCSD) 方法，该方法使用对操作数的某些因子的移位相加/减运算来代替乘法器运算。这些因子通常是质数，但也可以是接近 2 的幂的数，这有利于面积缩减。您可以通过 FCSD 实现更大的面积缩减，但这会以降低时钟速度为代价。 |
| `auto` | 当您指定此选项时，代码生成器会在 CSD 或 FCSD 优化之间进行选择。代码生成器根据所需加法器的数量选择可产生最大面积效率实现的优化。当您指定 `auto` 时，代码生成器不使用乘法器，除非条件使得 CSD 或 FCSD 优化不可行（例如，当设计使用浮点算术时）。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为**无**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。另请参阅DSPStyle (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**注意**

对于**增益**参数的某些值，原生浮点以不同方式实现算法，而不是使用乘法器。例如，如果您将**增益**参数设置为 `1`，生成的模型使用一条线将输入传递给输出。如果您将**增益**参数设置为 `-1`，生成的模型会显示 Unary Minus 模块，该模块会反转输入信号的极性。此实现可减少目标平台上的延迟和资源使用量。

| 原生浮点 | |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 在设计中插入额外的逻辑来处理非正规数字。非正规数是大小非常小、必须使用包含前导零的尾数才能表示的浮点数。默认值为 **inherit**。另请参阅HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会增加延迟，其值等于您为 **NFPCustomLatency** 设置指定的值。另请参阅NFPCustomLatency (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同设置，您可以控制目标 FPGA 设备上 DSP 的使用。默认值为 **inherit**。另请参阅MantissaMultiplyStrategy (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## Description

The Gain block multiplies the input by a constant value, or gain. The input
and the gain can each be a scalar, vector, or matrix.

You specify the value of gain in the **Gain** parameter. The
**Multiplication** parameter lets you specify element-wise or
matrix multiplication. For matrix multiplication, this parameter also lets you indicate
the order of the multiplicands.

The gain is converted from doubles to the data type specified in the block mask offline
using round-to-nearest and saturation. The input and gain are then multiplied, and the
result is converted to the output data type using the specified rounding and overflow
modes.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

The Gain block accepts real or complex-valued scalar, vector, or matrix
input. The Gain block supports fixed-point data types. If
the input of the Gain block is real and gain is complex,
the output is complex.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Input multiplied by gain scalar | vector | matrix

The Gain block outputs the input multiplied by a constant gain value.
When the input to the Gain block is real and gain is
complex, the output is complex.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Gain** — Value by which to multiply the input `1` (default) | real or complex-valued scalar, vector, or matrix

Specify the value by which to multiply the input. The gain can be a real or
complex-valued scalar, vector, or matrix.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Gain` |
| **Values:** | `'1'` (default) | real or complex-valued scalar, vector, or matrix in quotes |

### **Multiplication** — Specify the multiplication mode `Element-wise(K.*u)` (default) | `Matrix(K*u)` | `Matrix(u*K)` | `Matrix(K*u) (u vector)`

Specify one of these multiplication modes:

- `Element-wise(K.*u)` — Each element
  of the input is multiplied by each element of the gain. The
  block performs expansions, if necessary, so that the input and
  gain have the same dimensions.
- `Matrix(K*u)` — The input and gain are matrix-multiplied with
  the input as the second operand.
- `Matrix(u*K)` — The input and gain are matrix-multiplied with
  the input as the first operand.
- `Matrix(K*u) (u vector)` — The input
  and gain are matrix multiplied with the input as the second
  operand. This mode is identical to
  `Matrix(K*u)`, except for how dimensions
  are determined.

  Suppose that `K` is an
  `m-by-n` matrix. `Matrix(K*u)(u
  vector)` sets the input to a vector of length
  `n` and the output to a vector of length
  `m`. In contrast,
  `Matrix(K*u)` uses propagation to determine
  dimensions for the input and output. For an
  `m-by-n` gain matrix, the input can
  propagate to an `n-by-q` matrix, and the output
  becomes an `m-by-q` matrix.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Multiplication` |
| **Values:** | `'Element-wise(K.*u)'` (default) | `'Matrix(K*u)'` | `'Matrix(u*K)'` | `'Matrix(K*u) (u vector)'` |

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule`
  — The software chooses a data type to balance numerical
  accuracy, performance, and generated code size, while taking
  into account the properties of the embedded target hardware. If
  you change the embedded target settings, the data type selected
  by the internal rule might change. For example, if the block
  multiplies an input of type `int8` by a gain of
  `int16` and
  `ASIC/FPGA` is specified as the
  targeted hardware type, the output data type is
  `sfix24`. If `Unspecified
  (assume 32-bit Generic)`, in other words, a
  generic 32-bit microprocessor, is specified as the target
  hardware, the output data type is `int32`. If
  none of the word lengths provided by the target microprocessor
  can accommodate the output range, the software displays an error
  in the Diagnostic Viewer.
- `Inherit: Keep MSB`– The software chooses a data type that
  maintains the full range of the operation, then reduces the
  precision of the output to a size appropriate for the embedded
  target hardware.

  **Tip**

  For more efficient generated code, clear
  **Saturate on integer
  overflow**.

  This rule never produces overflows.
- `Inherit: Match scaling` – The
  software chooses a data type whose scaling matches the scaling
  of the input types. If the full range of the type does not fit
  on the embedded target hardware, the range is reduced yielding a
  type appropriate for the embedded target hardware. This rule can
  produce overflows.

  It is not always possible for the software to optimize code
  efficiency and numerical accuracy at the same time. If these
  internal rules do not meet your specific needs for numerical
  accuracy or performance, use one of the following options:

  - Specify the output data type explicitly.
  - Use the simple choice of `Inherit:
    Same as input`.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your
    model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use the data type of the driving
  block.
- `Inherit: Same as input` — Use the
  data type of the input signal.

#### Dependencies

When the input is a floating-point data type smaller than single precision, the
`Inherit: Inherit via internal rule`
output data type depends on the setting of the **Inherit floating-point output type smaller than single
precision** configuration parameter. Data types are
smaller than single precision when the number of bits needed to
encode the data type is less than the 32 bits needed to encode the
single-precision data type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

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

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

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

- `Inherit` — Inheritance rules for
  data types. Selecting `Inherit` enables a
  second menu/text box to the right where you can select the
  inheritance mode.
- `Built in` — Built-in data types.
  Selecting `Built in` enables a second menu/text
  box to the right where you can select a built-in data
  type.
- `Fixed point` — Fixed-point data
  types. Selecting `Fixed point` enables
  additional parameters that you can use to specify a fixed-point
  data type.
- `Expression` — Expressions that
  evaluate to data types. Selecting `Expression`
  enables a second menu/text box to the right, where you can enter
  the expression.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, click the Show data type assistant
button .

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

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### Parameter Attributes

### **Parameter minimum** — Specify the minimum value of gain `[]` (default) | scalar

Specify the minimum value of gain. The default value is `[]`
(unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter maximum** — Specify the maximum value of gain `[]` (default) | scalar

Specify the maximum value of gain. The default value is `[]`
(unspecified). The software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
- Automatic scaling of fixed-point data types

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Parameter data type** — Specify the data type of the Gain parameter `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Inherit from 'Gain'` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the **Gain**
parameter.

Setting **Parameter data type** to
`Inherit: Inherit via internal rule` lets
the Gain block select a data type based on an internal
heuristic that looks at the current gain value and provides a full
precision data type to represent the current gain value. When you update
the diagram, the software deduces a data type to fit the gain value
`3` with high precision and no range loss. For
example, with this heuristic, if the specified gain value is
`3`, the Gain block deduces a
selected data type of `sfix32_En29`. Consequently, this
deduced data type cannot hold values greater than `4`.
During simulation, if you tune the gain value to `6`,
an overflow occurs in the selected data type and the behavior is
unexpected.

While tuning a parameter with this **Parameter data
type** setting, specify the **Parameter
Minimum** and **Parameter Maximum**
parameters. These settings tell the software about the range of values
you want during the simulation and allows the software to provide a full
precision data type with sufficient range to allow safe tuning of the
gain value within the specified range.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParamDataTypeStr` |
| **Values:** | `'Inherit: Inherit via internal rule'` (default) | `'Inherit: Same as input'` | `'Inherit: Inherit from 'Gain''` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

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

**Tunable Parameters**

You can use a tunable parameter in a Gain block intended for
HDL code generation. For details, see Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

| `ConstMultiplierOptimization` | Description |
| --- | --- |
| `none`(*Default*) | By default, HDL Coder does not perform CSD or FCSD optimizations. Code generated for the Gain block retains multiplier operations. |
| `csd` | When you specify this option, the generated code decreases the area used by the model while maintaining or increasing clock speed, using canonical signed digit (CSD) techniques. CSD replaces multiplier operations with add and subtract operations.  CSD minimizes the number of addition operations required for constant multiplication by representing binary numbers with a minimum count of nonzero digits. |
| `fcsd` | This option uses factored CSD (FCSD) techniques, which replace multiplier operations with shift and add/subtract operations on certain factors of the operands. These factors are generally prime but can also be a number close to a power of 2, which favors area reduction. You can achieve a greater area reduction with FCSD at the cost of decreasing clock speed. |
| `auto` | When you specify this option, the coder chooses between the CSD or FCSD optimizations. The coder chooses the optimization that yields the most area-efficient implementation, based on the number of adders required. When you specify `auto`, the coder does not use multipliers, unless conditions are such that CSD or FCSD optimizations are not possible (for example, if the design uses floating-point arithmetic). |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Note**

For certain values of the **Gain** parameter, native
floating point implements the algorithm differently instead of using
multipliers. For example, if you set the **Gain** parameter
to `1`, the generated model uses a wire to pass the input
to the output. If you set the **Gain** parameter to
`-1`, the generated model shows a Unary
Minus block that inverts the polarity of the input signal. This
implementation reduces the latency and resource usage on the target
platform.

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
