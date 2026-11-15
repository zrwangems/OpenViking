---
type: simulink-block
title: 'Sum'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'sum'
---

# Sum

Add or subtract inputs

## 中文

输入信号的加减运算

### 所属库

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / Math Operations

### 描述

Sum 模块对输入信号执行加减运算。Add、Subtract、Sum of Elements 和 Sum 模块是同一模块的替代配置。此模块可对标量、向量或矩阵输入执行加减运算。它还可以缩减信号的元素并执行求和。

您可以使用**符号列表**参数以及加号 (`+`)、减号 (`-`) 和分隔符 (`|`) 指定模块的运算。

- `+` 和 `-` 字符的个数等于输入的个数。例如，`+-+` 需要三个输入。模块从第一个（顶部）输入信号中减去第二个（中间）输入信号，然后加上第三个（底部）输入信号。
- 分隔符在模块图标上的端口之间产生额外空间。
- 如果仅执行加法，则可以使用一个与输入个数相等的数值。
- 如果只有一个输入端口，则一个 `+` 或 `-` 会在所有维度上或在指定的维度中加上或减去元素。

Sum 模块首先将输入数据类型转换为其累加器数据类型，然后执行指定的运算。最后，模块使用指定的舍入和溢出模式，将计算结果转换为输出数据类型。

#### 模块输出的计算

Sum 模块的输出计算取决于模块输入的个数和输入端口的符号。

| Sum 模块的输入端口的数量 | 输入端口符号 | 模块输出计算公式 | 输出公式变量 |
| --- | --- | --- | --- |
| 一个输入端口 | 输入端口符号为 + 号 | y = e[0] + e[1] + e[2] ... + e[m] | `e[i]` 是输入 u 的第 *i* 个元素 |
| 输入端口符号为 – 号 | y = 0.0 – e[0] – e[1] – e[2] ... – e[m] |
| 两个或更多输入端口 | 所有输入端口符号均为 – 号 | y = 0.0 – u[0] – u[1] – u[2] ... – u[n] | `u[i]` 是第 *i* 个输入端口的输入 |
| 第*k* 个输入端口是第一个符号为 + 号的端口 | y = u[k] – u[0] – u[1] – u[2] – u[k–1] (+/–) u[k+1] ... (+/–) u[n] |

### 端口

#### 输入

输入可以具有不同的数据类型，除非您选中了**要求所有输入具有相同的数据类型**。

#### **Port\_1** — 第一个输入操作数信号 标量 | 向量 | 矩阵

用于加法或减法运算的输入信号。如果只有一个输入信号，则对所有维度或指定维度中的元素执行加法或减法。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_n** — 第 *n* 个输入操作数信号 标量 | 向量 | 矩阵

运算的第 *n* 个输入信号。输入的个数与**符号列表**参数中的符号个数相匹配。模块按照列出的顺序将运算应用于输入。您还可以使用一个与输入端口个数相等的数值作为**符号列表**参数。模块创建输入端口并将加法应用于所有输入。例如，如果为**符号列表**参数赋值 `5`，则模块创建 `5` 个输入端口并将它们相加以产生输出。

所有的非标量输入信号必须具有相同的维度。标量输入将扩展为与其他输入具有相同的维度。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

加法和/或减法运算产生的输出信号。输出信号具有与输入信号相同的维度。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **图标形状** — 模块图标形状 **矩形** | **舍入**

将模块的图标形状指定为矩形或圆形。

默认值取决于模块配置。

- **舍入**默认值 - Sum 模块
- **矩形**默认值 - Add、Subtract 和 Sum of Element 模块

对于矩形模块，第一个输入端口是顶部端口。对于一个圆形 Sum 模块，第一个输入端口最接近 12 点钟位置，按逆时针方向围绕模块。类似地，其他输入端口也按逆时针方向围绕模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconShape` |
| **类型**：字符向量 |
| **值**：`'rectangular'` | `'round'` |

#### **符号列表** — 对输入执行的运算 `+` | `-` | `|` | 整数

输入对输入信号执行的加法和减法运算。为每个运算创建一个输入端口。分隔符 (`|`) 在模块图标上的输入端口之间产生额外空间。加法是默认运算。如果您只想将输入信号相加，请键入输入端口的个数。各项运算按所列顺序执行。

默认值取决于模块配置。

- `|++` 默认值 - Sum 模块
- `++` 默认值 - Add 模块
- `+-` 默认值 - Subtract 模块
- `+` 默认值 - Sum of Element 模块

当您仅输入一个符号时，模块会启用**应用于**参数。对于一个向量输入，`+` 或 `-` 会在所有维度上或在指定的维度中加上或减去元素。

##### 提示

您可以通过在**符号列表**参数中的符号之间插入分隔符 (`|`) 来控制输入端口在模块上的位置。例如，“`++|--`”将在第二个和第三个输入端口之间留出额外空间。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型**：字符向量 |
| **值**：`'+'` | `'-'` | `|` | 整数 |

#### **应用于** — 如何沿指定维度应用函数 **所有维度** (默认) | **指定的维度**

指定如何沿指定维度应用函数。

- **所有维度** - 对所有维度的所有输入值应用函数。

  例如，在此模型中，**符号列表**设置为 `+`，**应用于**设置为**所有维度**。该模块返回所有维度的所有输入值的总和。

  2D matrix with Constant block value [1 2 3 4 5 6] as input to Sum block configured for all dimensions

  选择配置参数**使用针对行优先数组布局优化的算法**时，软件为仿真启用行优先算法。要生成行优先代码，请将配置参数**数组布局 (Simulink Coder)**设置为**行优先**，并选择**使用针对行优先数组布局优化的算法**。列优先算法和行优先算法仅在求和顺序上不同。在某些情况下，由于对同一数据集的运算顺序不同，列优先算法和行优先算法的输出可能存在微小的数值差异。
- **指定维度** - 对指定维度的所有输入值应用函数。

##### 依赖关系

要启用此参数，请在**符号列表**参数中仅输入一个符号。

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseMode` |
| **类型**：字符向量 |
| **值**：`'All dimensions'` | `'Specified dimension'` |
| **默认值**：`'All dimensions'` |

#### **维度** — 要沿其应用求和的维度 `1` (默认) | 正整数

将沿其应用求和的维度指定为正整数。

模块遵循的求和规则与 MATLAB® 中的 `sum` 函数相同。有关详细信息，请参阅算法。

例如，在此模型中，**符号列表**设置为 `+`，**应用于**设置为**指定的维度**，**维度**设置为 `2`。该模块返回每行的输入值的总和。

2D matrix with Constant block value [1 2 3;4 5 6] as input to Sum block configured for dimension 2

如果指定的维度大于输入的维度，则会显示错误消息。

##### 依赖关系

要启用此参数，请将**应用于**设置为**指定的维度**。

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseDim` |
| **类型**：字符向量 |
| **值**：整数 |
| **默认值**：`'1'` |

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

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

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

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: Keep MSB** | **继承: Keep LSB** | **继承: 通过反向传播继承** | **继承: 与第一个输入相同** | **继承: 与累加器相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType` 对象。

当您选择继承的选项时，模块的行为如下所示：

- **继承:从内部规则继承** - 软件在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。

  **注意**

  累加器内部规则的优点是数值更准确，而代价可能是生成的代码效率低下。要获取相同的输出精度，请将输出数据类型设置为 **Inherit: Inherit same as accumulator**。

  **注意**

  当输入是小于单精度的浮点数据类型时，**继承: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当对数据类型进行编码所需的位数小于对单精度数据类型编码所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。
- **继承:保留 MSB** - 软件选择一种能够保持运算的完整范围的数据类型，然后将输出精度降低到适合嵌入式目标硬件的大小。

  **提示**

  要获得更高效的生成代码，请将**累加器数据类型**设置为**继承:通过内部规则继承**，并清除**对整数溢出进行饱和处理**。

  此规则从不产生溢出。
- **继承:保留 LSB** - 软件选择一种保持运算精度的数据类型，但如果完整类型不适合嵌入式目标硬件，则会缩小范围。

  **提示**

  要获得更高效的生成代码，请将**累加器数据类型**设置为**继承:通过内部规则继承**，并清除**对整数溢出进行饱和处理**。

  此规则可能产生溢出。

  如果更改了嵌入式目标的设置，则依这些内部规则选择的数据类型可能会发生变化。有时软件不能同时满足优化代码效率和保证数值准确性这两个需求。如果这些规则不能满足您对数值准确性或性能的特定需求，请使用下列选项之一：

  - 显式指定输出数据类型。
  - 使用简单的选项**继承: 与第一个输入相同**。
  - 显式指定默认数据类型（例如 `fixdt(1,32,16)`），然后使用定点工具为您的模型提供数据类型建议。有关详细信息，请参阅 `fxptdlg` (Fixed-Point Designer)。
  - 要指定您自己的继承规则，请使用**继承: 通过反向传播继承**，然后使用 Data Type Propagation 模块。有关如何使用此模块的示例说明，请参阅 Signal Attributes 模块库中的 Data Type Propagation Examples 模块。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。
- **继承: 与第一个输入相同** - 使用第一个输入信号的数据类型。
- **继承: Inherit same as accumulator** - 使用累加器的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule` | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'`|`'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **累加器数据类型** — 累加器的数据类型 **继承: 从内部规则继承** (默认) | **继承: 与第一个输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

选择累加器的数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。如果您选择 **继承: 从内部规则继承**，Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。

##### 编程用法

|  |
| --- |
| **模块参数**： `AccumDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **要求所有输入具有相同的数据类型** — 要求所有输入具有相同的数据类型 `off` (默认) | `on`

指定输入信号是否必须全部具有相同的数据类型。如果启用此参数，则在输入信号类型不同时，仿真过程中会发生错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **锁定数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此选项可锁定数据类型设置，防止使用定点工具和定点顾问进行更改。有关详细信息，请参阅Lock the Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

|  |
| --- |
| **模块参数：**`LockScale` |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB 舍入函数输入表达式。

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

**Sum、Add 和 Subtract 模块的 HDL 架构**

默认的**线性**架构为 N 个输入生成包含 N 个运算（加法器）的运算链。

**Sum of Elements 模块的 HDL 架构**

对于 Sum of Elements 模块，HDL Coder 支持对单个向量输入具有多个元素的 Sum of Elements 模块使用**树**架构。

此模块具有多周期实现，这会在生成的代码中引入额外的延迟。要查看增加的延迟，请查看生成的模型或验证模型。请参阅Generated Model and Validation Model (HDL Coder)。

| 架构 | 额外的延迟周期 | 描述 |
| --- | --- | --- |
| **线性** | 0 | 生成线性加法器链来计算乘积之和。  对于具有不同位宽的多个输入，**Linear** 架构会对加法器进行多级实现并用流水线串联各级，以优化资源利用率。每级的输出是根据该级的输入宽度来计算的。 |
| **树** | 0 | 生成加法器树形结构来计算乘积之和。 |

**HDL 模块属性**

**注意**

要使用“HDL 模块属性”对话框的**原生浮点**选项卡中的 **LatencyStrategy** 设置，请指定**线性**或**树**作为 HDL 架构。

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**注意**

Sum of Elements 模块不支持原生浮点模式下双精度数据类型的 HDL 代码生成。

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min`、`Zero` 或 `Custom`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |
| **NFPCustomLatency** | 要指定值，请将 **LatencyStrategy** 设置为 `Custom`。HDL Coder 会增加延迟，其值等于您为 **NFPCustomLatency** 设置指定的值。另请参阅NFPCustomLatency (HDL Coder)。 |

**复数数据支持**

默认的**线性**实现支持复数数据。

**树**实现支持**符号列表**模块参数为 `+` 的复数数据。借助原生浮点支持，**树**实现支持**符号列表**为 `+` 和 `-` 的复数数据。

**限制和注意事项**

要为混合使用标量和向量输入的多输入 Sum 模块生成 HDL 代码，您必须在 Sum 模块的前两个输入之一上指定向量输入。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: 使用**应用于**参数指定如何应用函数（该参数从**求和维度**更名为现名称）

当您为**符号列表**仅输入一个符号时，模块会启用**应用于**参数。对于一个向量输入，`+` 或 `-` 会在所有维度上或在指定的维度中加上或减去元素。

为了更好地反映支持的行为，**求和维度**参数现在更名为**应用于**。

## Libraries

Simulink / Commonly Used Blocks Simulink / Math Operations HDL Coder / Commonly Used Blocks HDL Coder / Math Operations

## Description

The Sum block performs addition or subtraction on its inputs. The
Add, Subtract, Sum of Elements, and
Sum blocks are alternative configurations of the same block. This
block can add or subtract scalar, vector, or matrix inputs. It can also collapse the
elements of a signal and perform a summation.

You specify the operations of the block with the **List of signs**
parameter with plus signs (`+`), minus signs (`-`),
and spacers (`|`).

- The number of `+` and `-` characters equals
  the number of inputs. For example, `+-+` requires three inputs.
  The block subtracts the second (middle) input from the first (top) input, and
  then adds the third (bottom) input.
- A spacer character creates extra space between ports on the block icon.
- If performing only addition, you can use a numerical value equal to the number
  of inputs.
- If there is only one input port, one `+` or
  `-` adds or subtracts the elements over all dimensions or
  in the specified dimension.

The Sum block first converts the input data type to its accumulator
data type, then performs the specified operations. The block converts the result to its
output data type using the specified rounding and overflow modes.

### Calculation of Block Output

Output calculation for the Sum block depends on the number of block
inputs and the sign of input ports.

| Number of Sum Block Input Ports | Input Port Signs | Block Output Calculation Formula | Output Formula Variables |
| --- | --- | --- | --- |
| One input port | The input port sign is + | y = e[0] + e[1] + e[2] ... + e[m] | `e[i]` is the *i*th element of input u |
| The input port sign is – | y = 0.0 – e[0] – e[1] – e[2] ... – e[m] |
| Two or more input ports | All input port signs are – | y = 0.0 – u[0] – u[1] – u[2] ... – u[n] | `u[i]` is the input to the *i*th input port |
| The *k*th input port is the first port where the sign is + | y = u[k] – u[0] – u[1] – u[2] – u[k–1] (+/–) u[k+1] ... (+/–) u[n] |

## Ports

### Inputs

The inputs can be of different data types unless you select **Require all
inputs to have the same data type**.

### **Port\_1** — First input operand signal scalar | vector | matrix

Input signal to the addition or subtraction operation. If there is
only one input signal, then addition or subtraction is performed on the
elements over all dimensions or the specified dimension.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_n** — *n*th input operand signal scalar | vector | matrix

*n*th input signal to the operations. The number of
inputs matches the number of signs in the **List of
signs** parameter. The block applies the operations to the
inputs in the order listed. You can also use a numerical value equal to
the number of input ports as the **List of signs**
parameter. The block creates the input ports and applies addition to all
inputs. For example, if you assign `5` for the
**List of signs** parameter, the block creates
`5` input ports and adds them together to produce
the output.

All nonscalar inputs must have the same dimensions. Scalar inputs are
expanded to have the same dimensions as other inputs.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal resulting from addition and/or subtraction operations.
The output signal has the same dimension as the input signals.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Icon shape** — Block icon shape `rectangular` | `round`

Designate the icon shape of the block as rectangular or round.

The default value depends on the block configuration.

- `round` default —
  Sum block
- `rectangular` default —
  Add, Subtract, and
  Sum of Element blocks

For a rectangular block, the first input port is the top port. For a
round Sum block, the first input port is the port closest
to the 12 o'clock position going in a counterclockwise direction around
the block. Similarly, other input ports appear in counterclockwise order
around the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IconShape` |
| **Type**: character vector |
| **Values**: `'rectangular'` | `'round'` |

### **List of signs** — Operations performed on inputs `+` | `-` | `|` | integer

Enter addition and subtraction operations performed on the inputs. An
input port is created for each operation. A spacer
(`|`) creates extra space between the input ports on
the block icon. Addition is the default operation. If you only want to
add the inputs, enter the number of input ports. The operations are
performed in the order listed.

The default value depends on the block configuration.

- `|++` default — Sum
  block
- `++` default — Add
  block
- `+-` default — Subtract
  block
- `+` default — Sum of
  Element block

When you enter only one sign, the block enables the **Apply
over** parameter. For a vector input, `+`
or `-` adds or subtracts the elements over all
dimensions or in the specified dimension.

#### Tips

You can manipulate the positions of the input ports on the block
by inserting spacers (`|`) between the signs in the
**List of signs** parameter. For
example, “`++|--`” creates an extra
space between the second and third input ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Inputs` |
| **Type**: character vector |
| **Values**: `'+'` | `'-'` | `|` | integer |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply function along specified dimensions.

- `All dimensions` — Apply function for
  all input values for all dimensions.

  For example, in this model, **List of
  signs** is set to `+`, and
  **Apply over** is set to `All
  dimensions`. The block returns the sum of all
  input values from all dimensions.

  2D matrix with Constant block value [1 2 3 4 5 6] as input to Sum block configured for all dimensions

  When you select configuration parameter **Use algorithms optimized for row-major array
  layout**, the software enables row-major
  algorithms for simulation. To generate row-major code, set the
  configuration parameter **Array layout (Simulink Coder)** to
  `Row-major`, and select
  **Use algorithms optimized for row-major array
  layout**. The column-major and row-major algorithms
  differ only in the summation order. In some cases, due to
  different operation order on the same data set, you might
  experience minor numeric differences in the outputs of
  column-major and row-major algorithms.
- `Specified dimensions` — Apply
  function for all input values for specified dimension.

#### Dependencies

To enable this parameter, enter only one sign in the
**List of signs** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CollapseMode` |
| **Type**: character vector |
| **Values**: `'All dimensions'` | `'Specified dimension'` |
| **Default**: `'All dimensions'` |

### **Dimension** — Dimension along which to apply summation `1` (default) | positive integer

Specify the dimension along which to apply the summation as a positive
integer.

The block follows the same summation rules as the MATLAB®
`sum` function. For more information, see Algorithms.

For example, in this model, **List of signs** is
set to `+`, **Apply over** is set to
`Specified dimension`, and
**Dimension** is set to `2`. The
block returns the sum of the input values of each row.

2D matrix with Constant block value [1 2 3;4 5 6] as input to Sum block configured for dimension 2

If the specified dimension is greater than the dimension of the input,
an error message appears.

#### Dependencies

To enable this parameter, set **Apply over** to
`Specified dimension`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CollapseDim` |
| **Type**: character vector |
| **Value**: integer |
| **Default**: `'1'` |

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

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

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

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as a
`Simulink.NumericType` object.

When you select an inherited option, the block behaves as follows:

- `Inherit: Inherit via internal
  rule` — The software chooses a data type to
  balance numerical accuracy, performance, and generated code
  size, while taking into account the properties of the
  embedded target hardware.

  **Note**

  The accumulator internal rule favors greater numerical
  accuracy, possibly at the cost of less efficient
  generated code. To get the same accuracy for the output,
  set the output data type to `Inherit:
  Inherit same as accumulator`.

  **Note**

  When input is a floating-point data type smaller than
  single precision, the `Inherit: Inherit via
  internal rule` output data type depends
  on the setting of the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than
  single precision when the number of bits needed to
  encode the data type is less than the 32 bits needed to
  encode the single-precision data type. For example,
  `half` and `int16`
  are smaller than single precision.
- `Inherit: Keep MSB` – The
  software chooses a data type that maintains the full range
  of the operation, then reduces the precision of the output
  to a size appropriate for the embedded target hardware.

  **Tip**

  For more efficient generated code, set
  **Accumulator data type** to
  `Inherit: Inherit via internal
  rule`, and clear **Saturate
  on integer overflow**.

  This rule never produces overflows.
- `Inherit: Keep LSB`– The software
  chooses a data type that maintains the precision of the
  operation, but reduces the range if the full type does not
  fit on the embedded target hardware.

  **Tip**

  For more efficient generated code, set
  **Accumulator data type** to
  `Inherit: Inherit via internal
  rule`, and clear **Saturate
  on integer overflow**.

  This rule can produce overflows.

  If you change the embedded target settings, the data type
  selected by these internal rules might change. It is not
  always possible for the software to optimize code efficiency
  and numerical accuracy at the same time. If the rules do not
  meet your specific needs for numerical accuracy or
  performance, use one of the following options:

  - Specify the output data type
    explicitly.
  - Use the simple choice of `Inherit:
    Same as first input`.
  - Explicitly specify a default data type such as
    `fixdt(1,32,16)` and then use the
    Fixed-Point Tool to propose data types for your
    model. For more information, see `fxptdlg` (Fixed-Point Designer).
  - To specify your own inheritance rule, use
    `Inherit: Inherit via back
    propagation` and then use a Data Type
    Propagation block. Examples of how to use
    this block are available in the Signal Attributes
    library Data Type Propagation
    Examples block.
- `Inherit: Inherit via back
  propagation` — Use data type of the driving
  block.
- `Inherit: Same as first input` —
  Use data type of the first input signal.
- `Inherit: Inherit same as
  accumulator`— Use data type of the
  accumulator.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule` | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'`|`'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Accumulator data type** — Data type of the accumulator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type of the accumulator. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`. When you choose
`Inherit: Inherit via internal
rule`, Simulink® chooses a data type to balance numerical accuracy,
performance, and generated code size, while taking into account the
properties of the embedded target hardware.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**:  `AccumDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'`, `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

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

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select to lock data type settings of this block against changes by the
Fixed-Point Tool and the Fixed-Point Advisor. For more information,
see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function into the mask field.

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

**HDL Architecture of Sum, Add, and Subtract Blocks**

The default `Linear` architecture generates a chain
of N operations (adders) for N inputs.

**HDL Architecture of Sum of Elements Block**

For the Sum of Elements block, HDL Coder supports `Tree` architectures for Sum of
Elements blocks that have a single vector input with multiple elements.

This block has multi-cycle implementations that introduce additional
latency in the generated code. To see the added latency, view the
generated model or validation model. See Generated Model and Validation Model (HDL Coder).

| Architecture | Additional cycles of latency | Description |
| --- | --- | --- |
| `Linear` | 0 | Generates a linear chain of adders to compute the sum of products.  For multiple inputs that have different bit widths, the `Linear` architecture optimizes the resource utilization by implementing adders in multiple stages with pipelines in between the stages. The output of each stage is calculated based on the width of the inputs to that stage. |
| `Tree` | 0 | Generates a tree structure of adders to compute the sum of products. |

**HDL
Block Properties**

**Note**

To use the **LatencyStrategy** setting in the **Native
Floating Point** tab of the HDL Block Properties dialog box, specify
`Linear` or `Tree` as the HDL
Architecture.

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Note**

The Sum of Elements block does not support HDL code generation with double data types
in the Native Floating Point mode.

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Complex Data Support**

The default `Linear` implementation
supports complex data.

The `Tree`  implementation supports complex data with
`+` for the **List of signs** block parameter. With
native floating point support, the `Tree`  implementation supports
complex data with both `+` and `-` for **List of
signs**.

**Limitations and Considerations**

To generate HDL code for multi-input Sum block that has mixed
scalar and vector inputs, you must specify vector input at one of the first two
inputs of the Sum block.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Specify how to apply function using **Apply over** parameter, renamed from **Sum over**

When you enter only one sign for **List of signs**, the block
enables the **Apply over** parameter. For a vector input,
`+` or `-` adds or subtracts the elements over
all dimensions or in the specified dimension.

To better reflect the supported behavior, the **Sum over**
parameter is now called **Apply over**.
