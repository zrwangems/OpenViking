---
type: simulink-block
title: 'Data Type Propagation'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypepropagation'
---

# Data Type Propagation

Set data type and scaling of propagated signal based on information from reference signals

## 中文

基于参考信号的信息设置传播信号的数据类型和缩放

### 库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Data Type Propagation 模块允许您控制模型中信号的数据类型和缩放。您可以将此模块与定点模块一起使用，这些定点模块的 **输出数据类型** 参数配置为 `Inherit: Inherit via back propagation`。

该模块有三个输入：**Ref1** 和 **Ref2** 是参考输入，而 **Prop** 输入反向传播从参考输入收集的数据类型和缩放信息。然后，该信息会传递给其他定点模块。

该模块提供了许多用于传播数据类型和缩放信息的选择。例如，您可以使用：

- 来自 **Ref1** 参考信号的位数或来自最宽参考信号的位数
- 来自 **Ref2** 参考信号的范围或具有最大范围的参考信号的范围
- 零偏置，无论参考信号使用的偏置是什么
- 精度最低的参考信号的精度

您使用 **传播的数据类型** 参数指定数据类型信息的传播方式：

- 如果选择 `Specify via dialog`，则通过 **传播的数据类型** 编辑字段手动指定数据类型。
- 如果选择 `Inherit via propagation rule`，则必须使用参数中描述的参数。

您使用 **传播的缩放** 参数指定缩放信息的传播方式：

- 如果选择 `Specify via dialog`，则通过 **传播的缩放** 编辑字段手动指定缩放。
- 如果选择 `Inherit via propagation rule`，则必须使用参数中描述的参数。

使用参考信号的信息后，您可以对数据类型和缩放应用第二级调整。为此，请使用单独的乘法和加法调整。这种灵活性有多种用途。例如，如果您面向 DSP，则可以配置该模块，使与乘加 (MAC) 运算关联的位数是输入信号的两倍宽，并为其添加特定数量的保护位。

Data Type Propagation 模块还提供了一种机制，用于将计算出的位数强制为有用的值。例如，如果您面向 16 位微处理器，则目标 C 编译器可能只支持 8 位、16 位和 32 位的大小。该模块强制使用这三种选择。例如，假设该模块计算出数据类型大小为 24 位。由于目标芯片无法直接使用 24 位，因此信号被强制提升到 32 位，这是本机支持的。

还有一种处理浮点参考信号的方法。此方法使创建易于在定点芯片和浮点芯片之间重新定向的设计变得更加容易。

Data Type Propagation 模块允许您建立有用的子系统库，这些子系统会根据所连接的信号进行正确配置。如果没有此数据类型传播过程，库中的子系统很可能无法按预期处理大多数整数或定点信号。将需要手动干预来配置数据类型和缩放。在许多情况下，此模块可以消除手动干预。

#### 优先级规则

对话框参数的优先级从上到下递减。此外：

- 双精度参考输入优先于所有其他数据类型。
- 单精度参考输入优先于整数和定点数据类型。
- 乘法调整在加法调整之前执行。
- 位数在从参考输入继承精度或正范围之前确定。
- `PosRange` 比信号的精确最大正范围高一位。
- 计算出的位数会提升到大于或等于计算结果的最小允许值。如果不存在，则该模块返回错误。

### 端口

#### 输入

#### **Ref1** — 第一参考信号 标量 | 向量 | 矩阵 | N 维数组

第一参考信号，用于收集数据类型和缩放信息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Ref2** — 第二参考信号 标量 | 向量 | 矩阵 | N 维数组

第二参考信号，用于收集数据类型和缩放信息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Prop** — 传播的数据类型和缩放 数据类型和缩放

数据类型和缩放信息，反向传播到模型。该模块从参考信号收集数据类型和缩放信息后，您可以对数据类型和缩放应用第二级调整。为此，请在该模块对话框中指定单独的乘法和加法调整。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### 传播类型

#### **1. 传播的数据类型** — 指定传播的数据类型的模式 `Inherit via propagation rule` (默认) | `Specify via dialog`

指定是通过对话框传播数据类型，还是从参考信号继承数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `PropDataTypeMode` |
| **类型：** character vector |
| **值：** `'Specify via dialog' | 'Inherit via propagation rule'` |
| **默认：** `'Inherit via propagation rule'` |

#### **1.1. 传播的数据类型（例如 fixdt(1,16), fixdt('single')）** — 传播的数据类型 `fixdt(1,16)` (默认) | 数据类型字符串

指定要传播的数据类型。

#### 依赖

要启用此参数，请将 **1. 传播的数据类型** 设置为 `Specify via dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `PropDataType` |
| **类型：** character vector |
| **值：** `'fixdt(1, 16)'` | 带引号的数据类型字符串 |
| **默认：** `'fixdt(1, 16)'` |

#### **1.1 如果任一参考输入为 double，则输出为** — 当参考输入为 double 时的输出数据类型 `double` (默认) | `single`

将输出数据类型指定为 `single` 或 `double`。此参数使创建易于在定点芯片和浮点芯片之间重新定向的设计变得更加容易。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `IfRefDouble` |
| **类型：** character vector |
| **值：** `'double' | 'single'` |
| **默认：** `'double'` |

#### **1.2 如果任一参考输入为 single，则输出为** — 当参考输入为 single 时的输出数据类型 `single` (默认) | `double`

将输出数据类型指定为 `single` 或 `double`。此参数使创建易于在定点芯片和浮点芯片之间重新定向的设计变得更加容易。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `IfRefSingle` |
| **类型：** character vector |
| **值：** `'double' | 'single'` |
| **默认：** `'single'` |

#### **1.3 是否有符号** — 传播的数据类型的有符号性 `IsSigned1 or IsSigned2` (默认) | `IsSigned1` | `IsSigned2` | `TRUE` | `FALSE`

将 **Prop** 的符号指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `IsSigned1` | 如果 **Ref1** 是有符号数据类型，则 **Prop** 是有符号数据类型。 |
| `IsSigned2` | 如果 **Ref2** 是有符号数据类型，则 **Prop** 是有符号数据类型。 |
| `IsSigned1 or IsSigned2` | 如果 **Ref1** 或 **Ref2** 任一为有符号数据类型，则 **Prop** 是有符号数据类型。 |
| `TRUE` | 忽略 **Ref1** 和 **Ref2**，Prop 始终是有符号数据类型。 |
| `FALSE` | 忽略 **Ref1** 和 **Ref2**，Prop 始终是无符号数据类型。 |

例如，如果 **Ref1** 信号为 `ufix(16)`，**Ref2** 信号为 `sfix(16)`，并且 **是否有符号** 参数为 `IsSigned1 or IsSigned2`，则 **Prop** 被强制为有符号数据类型。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `IsSigned` |
| **类型：** character vector |
| **值：** `'IsSigned1' | 'IsSigned2' | 'IsSigned1 or IsSigned2' | 'TRUE' | 'FALSE'` |
| **默认：** `'IsSigned1 or IsSigned2'` |

#### **1.4.1 位数：基础** — 传播数据类型基础的位数 `max([NumBits1 NumBits2])` (默认) | `NumBits1` | `NumBits2` | `min([NumBits1 NumBits2])` | `NumBits1+NumBits2`

将 **Prop** 用于基础数据类型的位数指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `NumBits1` | **Prop** 的位数由 **Ref1** 的位数给出。 |
| `NumBits2` | **Prop** 的位数由 **Ref2** 的位数给出。 |
| `max([NumBits1 NumBits2])` | **Prop** 的位数由位数最多的参考信号给出。 |
| `min([NumBits1 NumBits2])` | **Prop** 的位数由位数最少的参考信号给出。 |
| `NumBits1+NumBits2` | **Prop** 的位数由参考信号位数之和给出。 |

有关基础数据类型的详细信息，请参阅 Targeting an Embedded Processor (Fixed-Point Designer)。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBitsBase` |
| **类型：** character vector |
| **值：** `'NumBits1' | 'NumBits2' | 'max([NumBits1 NumBits2])' | 'min([NumBits1 NumBits2])' | 'NumBits1+NumBits2'` |
| **默认：** `'max([NumBits1 NumBits2])'` |

#### **1.4.2 位数：乘法调整** — 传播数据类型的乘法调整的位数 `1` (默认) | 正整数

通过包含使用 `double` 数据类型的乘法调整，指定 **Prop** 使用的位数。例如，假设您要确保与乘加 (MAC) 运算关联的位数是输入信号的两倍宽。为此，请将此参数设置为 `2`。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBitsMult` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认：** `'1'` |

#### **1.4.3 位数：加法调整** — 传播数据类型的加法调整的位数 `0` (默认) | 正整数

通过包含使用 `double` 数据类型的加法调整，指定 **Prop** 使用的位数。例如，如果您在 MAC 运算期间执行多个加法，结果可能会溢出。为防止溢出，您可以将保护位与传播数据类型关联。要关联四个保护位，请指定值 `4`。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBitsAdd` |
| **类型：** character vector |
| **值：** 标量 |
| **默认：** `'0'` |

#### **1.4.4 位数：允许的最终值** — 传播数据类型中允许的位数 `'-1'` (默认) | 正整数标量或向量

将 **Prop** 使用的计算位数强制为有用的值。例如，如果您面向仅支持 8 位、16 位和 32 位的处理器，则将此参数配置为 `[8,16,32]`。该模块始终传播符合条件的最小指定值。如果要允许所有定点数据类型，请指定值 `-1`。

#### 依赖

要启用此参数，请将 **传播的数据类型** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBitsAllowFinal` |
| **类型：** character vector |
| **值：** 正整数标量或向量 |
| **默认：** `'-1'` |

#### 传播的缩放

#### **2. 传播的缩放** — 传播的缩放模式 `Inherit via propagation rule` (默认) | `Specify via dialog` | `Obtain via best precision`

选择通过对话框传播缩放、从参考信号继承缩放，或计算缩放以获得最佳精度。

#### 编程用法

|  |
| --- |
| **模块参数：** `PropScalingMode` |
| **类型：** character vector |
| **值：** `'Inherit via propagation rule'` | `'Specify via dialog'` | `'Obtain via best precision'` |
| **默认：** `'Inherit via propagation rule'` |

#### **2.1. 传播的缩放（斜率，例如 2^-9 或 [Slope Bias]，例如 [1.25 3]）** — 斜率或斜率和偏置 `2^-10` | 斜率 | 方括号中的斜率和偏置

将缩放指定为斜率，或者斜率和偏置。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Specify via dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `PropScaling` |
| **类型：** character vector |
| **值：** 斜率 | 方括号中的斜率和偏置 |
| **默认：** `'2^-10'` |

#### **2.1. 用于确定最佳精度缩放的值** — 用于约束精度的值 `[5 -7]` (默认)

指定用于约束精度的任何值，例如传播输入的上限和下限。根据数据类型，该模块选择一种缩放，使得这些值可以在无溢出误差且量化误差最小的情况下表示。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Obtain via best precision`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ValuesUsedBestPrec` |
| **类型：** character vector |
| **值：** 值向量 |
| **默认：** `'[5 -7]'` |

#### **2.1.1. 斜率：基础** — 传播数据类型基础的斜率 `min([Slope1 Slope2])` (默认) | `Slope1` | `Slope2` | `min([Slope1 Slope2])` | `max([Bias1 Bias2])` | `Slope1*Slope2` | `Slope1/Slope2` | `PosRange1` | `PosRange2` | `max([PosRange1 PosRange2])` | `min([PosRange1 PosRange2])` | `PosRange1*PosRange2` | `PosRange1/PosRange2`

将 **Prop** 用于基础数据类型的斜率指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `Slope1` | **Prop** 的斜率由 **Ref1** 的斜率给出。 |
| `Slope2` | **Prop** 的斜率由 **Ref2** 的斜率给出。 |
| `max([Slope1 Slope2])` | **Prop** 的斜率由参考信号的最大斜率给出。 |
| `min([Slope1 Slope2])` | **Prop** 的斜率由参考信号的最小斜率给出。 |
| `Slope1*Slope2` | **Prop** 的斜率由参考信号斜率的乘积给出。 |
| `Slope1/Slope2` | **Prop** 的斜率由 **Ref1** 斜率与 **Ref2** 斜率的比值给出。 |
| `PosRange1` | **Prop** 的范围由 **Ref1** 的范围给出。 |
| `PosRange2` | **Prop** 的范围由 **Ref2** 的范围给出。 |
| `max([PosRange1 PosRange2])` | **Prop** 的范围由参考信号的最大范围给出。 |
| `min([PosRange1 PosRange2])` | **Prop** 的范围由参考信号的最小范围给出。 |
| `PosRange1*PosRange2` | **Prop** 的范围由参考信号范围的乘积给出。 |
| `PosRange1/PosRange2` | **Prop** 的范围由 **Ref1** 范围与 **Ref2** 范围的比值给出。 |

您使用 `Slope1` 和 `Slope2` 控制 **Prop** 的精度，并使用 `PosRange1` 和 `PosRange2` 控制 **Prop** 的范围。此外，`PosRange1` 和 `PosRange2` 比相关参考信号的最大正范围高一位。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SlopeBase` |
| **类型：** character vector |
| **值：** `'Slope1' | 'Slope2' | 'max([Slope1 Slope2])' | 'min([Slope1 Slope2])' | 'Slope1*Slope2' | 'Slope1/Slope2' | 'PosRange1' | 'PosRange2' | 'max([PosRange1 PosRange2])' | 'min([PosRange1 PosRange2])' | 'PosRange1*PosRange2' | 'PosRange1/PosRange2'` |
| **默认：** `'min([Slope1 Slope2])'` |

#### **2.1.2. 斜率：乘法调整** — 传播数据类型的乘法调整的斜率 `1` (默认) | 标量

通过包含使用 `double` 数据类型的乘法调整，指定 **Prop** 使用的斜率。例如，如果您希望增加 3 位精度（并相应减小范围），则乘法调整为 `2^-3`。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SlopeMult` |
| **类型：** character vector |
| **值：** 标量 |
| **默认：** `'1'` |

#### **2.1.3. 斜率：加法调整** — 传播数据类型的加法调整的斜率 `0` (默认) | 标量

通过包含使用 `double` 数据类型的加法调整，指定 **Prop** 使用的斜率。通常不需要加法斜率调整。最可能的用法是将乘法调整设置为 `0`，并设置加法调整以将最终斜率强制为指定值。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SlopeAdd` |
| **类型：** character vector |
| **值：** 标量 |
| **默认：** `'0'` |

#### **2.2.1. 偏置：基础** — **Prop** 的基础偏置 `Bias1` (默认) | `Bias2` | `max([Bias1 Bias2])` | `min([Bias1 Bias2])` | `Bias1*Bias2` | `Bias1/Bias2` | `Bias1+Bias2` | `Bias1-Bias2`

指定 **Prop** 用于基础数据类型的偏置。参数值描述如下：

| 参数值 | 描述 |
| --- | --- |
| `Bias1` | **Prop** 的偏置由 **Ref1** 的偏置给出。 |
| `Bias2` | **Prop** 的偏置由 **Ref2** 的偏置给出。 |
| `max([Bias1 Bias2])` | **Prop** 的偏置由参考信号的最大偏置给出。 |
| `min([Bias1 Bias2])` | **Prop** 的偏置由参考信号的最小偏置给出。 |
| `Bias1*Bias2` | **Prop** 的偏置由参考信号偏置的乘积给出。 |
| `Bias1/Bias2` | **Prop** 的偏置由 **Ref1** 偏置与 **Ref2** 偏置的比值给出。 |
| `Bias1+Bias2` | **Prop** 的偏置由参考偏置的和给出。 |
| `Bias1-Bias2` | **Prop** 的偏置由参考偏置的差给出。 |

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BiasBase` |
| **类型：** character vector |
| **值：** `'Bias1' | 'Bias2' | 'max([Bias1 Bias2])' | 'min([Bias1 Bias2])' | 'Bias1*Bias2' | 'Bias1/Bias2' | 'Bias1+Bias2' | 'Bias1-Bias2'` |
| **默认：** `'Bias1'` |

#### **2.2.2. 偏置：乘法调整** — 传播数据类型的乘法偏置 `1` (默认) | 标量

通过包含使用 `double` 数据类型的乘法调整，指定 Prop 使用的偏置。

仅当您将 **传播的缩放** 设置为 `Inherit via propagation rule` 时，此参数才可见。

#### 编程用法

|  |
| --- |
| **模块参数：** `BiasMult` |
| **类型：** character vector |
| **值：** 标量 |
| **默认：** `'1'` |

#### **2.3.2. 偏置：加法调整** — 传播数据类型的加法偏置 `0` (默认) | 标量

通过包含使用 `double` 数据类型的加法调整，指定 **Prop** 使用的偏置。

如果要确保与 **Prop** 关联的偏置为零，请将乘法调整和加法调整都配置为 `0`。

#### 依赖

要启用此参数，请将 **传播的缩放** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BiasAdd` |
| **类型：** character vector |
| **值：** 标量 |
| **默认：** `'0'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块可用于控制生成 HDL 代码的子系统中的信号的缩放和数据类型，但不包含在硬件实现中。

**限制**

当此模块位于封装子系统内部时，该模块在模型生成中会被忽略。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2006a 之前引入**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Data Type Propagation block allows you to control the data type and
scaling of signals in your model. You can use this block along with fixed-point blocks
that have their **Output data type** parameter configured to
`Inherit: Inherit via back propagation`.

The block has three inputs: **Ref1** and **Ref2** are the
reference inputs, while the **Prop** input back-propagates the data
type and scaling information gathered from the reference inputs. This information is
then passed on to other fixed-point blocks.

The block provides many choices for propagating data type and scaling information. For
example, you can use:

- The number of bits from the **Ref1** reference signal or the
  number of bits from widest reference signal
- The range from the **Ref2** reference signal or the range of
  the reference signal with the greatest range
- A bias of zero, regardless of the biases used by the reference signals
- The precision of the reference signal with the least precision

You specify how data type information is propagated using the **Propagated data
type** parameter:

- If you select `Specify via dialog`, then you manually specify
  the data type via the **Propagated data type** edit field.
- If you select `Inherit via propagation rule`, then you must
  use the parameters described in Parameters.

You specify how scaling information is propagated using the **Propagated
scaling** parameter:

- If you select `Specify via dialog`, then you manually specify
  the scaling via the **Propagated scaling** edit field.
- If you select `Inherit via propagation rule`, then you must
  use the parameters described in Parameters.

After you use the information from the reference signals, you can apply a second level of
adjustments to the data type and scaling. To do so, use individual multiplicative and
additive adjustments. This flexibility has various uses. For example, if you are
targeting a DSP, then you can configure the block so that the number of bits associated
with a multiply and accumulate (MAC) operation is twice as wide as the input signal, and
has a specific number of guard bits added to it.

The Data Type Propagation block also provides a mechanism to force the
computed number of bits to a useful value. For example, if you are targeting a 16-bit
micro, then the target C compiler is likely to support sizes of only 8 bits, 16 bits,
and 32 bits. The block forces these three choices to be used. For example, suppose that
the block computes a data type size of 24 bits. Since 24 bits is not directly usable by
the target chip, the signal is forced up to 32 bits, which is natively supported.

There is also a method for dealing with floating-point reference signals. This method makes
it easier to create designs that are easily retargeted between fixed-point chips and
floating-point chips.

The Data Type Propagation block allows you to set up libraries of useful
subsystems that are properly configured based on the connected signals. Without this
data type propagation process, subsystems from a library are unlikely to work as desired
with most integer or fixed-point signals. Manual intervention would be required to
configure the data type and scaling. In many situations, this block can eliminate the
manual intervention.

### Precedence Rules

The precedence of the dialog box parameters decreases from top to bottom. Also:

- Double-precision reference inputs have precedence over all other data types.
- Single-precision reference inputs have precedence over integer and fixed-point data types.
- Multiplicative adjustments are carried out before additive adjustments.
- The number of bits is determined before the precision or positive range is inherited from the reference inputs.
- `PosRange` is one bit higher than the exact maximum
  positive range of the signal.
- The computed number-of-bits are promoted to the smallest allowable value
  that is greater than or equal to the computation. If none exists, then the
  block returns an error.

## Ports

### Input

### **Ref1** — First reference signal scalar | vector | matrix | N-D array

First reference signal, from which to gather data type and scaling
information.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Ref2** — Second reference signal scalar | vector | matrix | N-D array

Second reference signal from which to gather data type and scaling
information.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Prop** — Propagated data type and scaling data type and scaling

Data type and scaling information, back-propagated to the model. After the block gathers
data type and scaling information from the reference signals, you can
apply a second level of adjustments to the data type and scaling. To do
so, specify individual multiplicative and additive adjustments in the
block dialog box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Propagated Type

### **1. Propagated data type** — Mode of specifying propagated data type `Inherit via propagation rule` (default) | `Specify via dialog`

Specify whether to propagate the data type via the dialog box, or inherit the data type
from the reference signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropDataTypeMode` |
| **Type:** character vector |
| **Values:** `'Specify via dialog' | 'Inherit via propagation rule'` |
| **Default:** `'Inherit via propagation rule'` |

### **1.1. Propagated data type (e.g. fixdt(1,16), fixdt('single'))** — Propagated data type `fixdt(1,16)` (default) | data type string

Specify the data type to propagate.

#### Dependencies

To enable this parameter, set **1. Propagated data
type** to `Specify via
dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropDataType` |
| **Type:** character vector |
| **Values:** `'fixdt(1, 16)'` | data type string in quotes |
| **Default:** `'fixdt(1, 16)'` |

### **1.1 If any reference input is double, output is** — Output data type when a reference input is double `double` (default) | `single`

Specify the output data type as `single` or
`double`. This parameter makes it easier to create
designs that are easily retargeted between fixed-point chips and
floating-point chips.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IfRefDouble` |
| **Type:** character vector |
| **Values:** `'double' | 'single'` |
| **Default:** `'double'` |

### **1.2 If any reference input is single, output is** — Output data type when a reference input is single `single` (default) | `double`

Specify the output data type as `single` or
`double`. This parameter makes it easier to create
designs that are easily retargeted between fixed-point chips and
floating-point chips.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IfRefSingle` |
| **Type:** character vector |
| **Values:** `'double' | 'single'` |
| **Default:** `'single'` |

### **1.3 Is-Signed** — Signedness of propagated data type `IsSigned1 or IsSigned2` (default) | `IsSigned1` | `IsSigned2` | `TRUE` | `FALSE`

Specify the sign of **Prop** as one of the following
values.

| Parameter Value | Description |
| --- | --- |
| `IsSigned1` | **Prop** is a signed data type if **Ref1** is a signed data type. |
| `IsSigned2` | **Prop** is a signed data type if **Ref2** is a signed data type. |
| `IsSigned1 or IsSigned2` | **Prop** is a signed data type if either **Ref1** or **Ref2** are signed data types. |
| `TRUE` | **Ref1** and **Ref2** are ignored, and Prop is always a signed data type. |
| `FALSE` | **Ref1** and **Ref2** are ignored, and Prop is always an unsigned data type. |

For example, if the **Ref1** signal is
`ufix(16)`, the **Ref2** signal is
`sfix(16)`, and the **Is-Signed**
parameter is `IsSigned1 or IsSigned2`, then
**Prop** is forced to be a signed data type.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsSigned` |
| **Type:** character vector |
| **Values:** `'IsSigned1' | 'IsSigned2' | 'IsSigned1 or IsSigned2' | 'TRUE' | 'FALSE'` |
| **Default:** `'IsSigned1 or IsSigned2'` |

### **1.4.1 Number-of-bits: Base** — Number of bits for the base of the propagated data type `max([NumBits1 NumBits2])` (default) | `NumBits1` | `NumBits2` | `min([NumBits1 NumBits2])` | `NumBits1+NumBits2`

Specify the number of bits used by **Prop** for the
base data type as one of the following values.

| Parameter Value | Description |
| --- | --- |
| `NumBits1` | The number of bits for **Prop** is given by the number of bits for **Ref1**. |
| `NumBits2` | The number of bits for **Prop** is given by the number of bits for **Ref2**. |
| `max([NumBits1 NumBits2])` | The number of bits for **Prop** is given by the reference signal with largest number of bits. |
| `min([NumBits1 NumBits2])` | The number of bits for **Prop** is given by the reference signal with smallest number of bits. |
| `NumBits1+NumBits2` | The number of bits for **Prop** is given by the sum of the reference signal bits. |

For more information about the base data type, refer to Targeting an Embedded
Processor (Fixed-Point Designer).

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBitsBase` |
| **Type:** character vector |
| **Values:** `'NumBits1' | 'NumBits2' | 'max([NumBits1 NumBits2])' | 'min([NumBits1 NumBits2])' | 'NumBits1+NumBits2'` |
| **Default:** `'max([NumBits1 NumBits2])'` |

### **1.4.2 Number-of-bits: Multiplicative adjustment** — Number of bits for multiplicative adjustment of propagated data type `1` (default) | positive integer

Specify the number of bits used by **Prop** by
including a multiplicative adjustment that uses a data type of
`double`. For example, suppose that you want to
guarantee that the number of bits associated with a multiply and
accumulate (MAC) operation is twice as wide as the input signal. To do
this, set this parameter to `2`.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBitsMult` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:** `'1'` |

### **1.4.3 Number-of-bits: Additive adjustment** — Number of bits for additive adjustment of propagated data type `0` (default) | positive integer

Specify the number of bits used by **Prop** by
including an additive adjustment that uses a data type of
`double`. For example, if you are performing
multiple additions during a MAC operation, the result could overflow. To
prevent overflow, you can associate guard bits with the propagated data
type. To associate four guard bits, you specify the value
`4`.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBitsAdd` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **1.4.4 Number-of-bits: Allowable final values** — Allowable number of bits in propagated data type `'-1'` (default) | scalar or vector of positive integers

Force the computed number of bits used by **Prop** to a useful value.
For example, if you are targeting a processor that supports only 8 bits,
16 bits, and 32 bits, then you configure this parameter to
`[8,16,32]`. The block always propagates the
smallest specified value that fits. If you want to allow all fixed-point
data types, you would specify the value `-1`.

#### Dependencies

To enable this parameter, set **Propagated data
type** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumBitsAllowFinal` |
| **Type:** character vector |
| **Values:** scalar or vector of positive integers |
| **Default:** `'-1'` |

### Propagated Scaling

### **2. Propagated scaling** — Propagated scaling mode `Inherit via propagation rule` (default) | `Specify via dialog` | `Obtain via best precision`

Choose to propagate the scaling via the dialog box, inherit the
scaling from the reference signals, or calculate the scaling to obtain
best precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropScalingMode` |
| **Type:** character vector |
| **Values:** `'Inherit via propagation rule'` | `'Specify via dialog'` | `'Obtain via best precision'` |
| **Default:** `'Inherit via propagation rule'` |

### **2.1. Propagated scaling (Slope, e.g. 2^-9 or [Slope Bias], e.g. [1.25 3])** — Slope or slope and bias `2^-10` | slope | slope and bias in square brackets

Specify the scaling as either a slope or a slope and bias.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Specify via
dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropScaling` |
| **Type:** character vector |
| **Values:** slope | slope and bias in square brackets |
| **Default:** `'2^-10'` |

### **2.1. Values used to determine best precision scaling** — Values to constrain precision `[5 -7]` (default)

Specify any values to be used to constrain the precision, such as the
upper and lower limits on the propagated input. Based on the data type,
the block selects a scaling such that these values can be represented
with no overflow error and minimum quantization error.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Obtain via best
precision`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ValuesUsedBestPrec` |
| **Type:** character vector |
| **Values:** vector of values |
| **Default:** `'[5 -7]'` |

### **2.1.1. Slope: Base** — Slope for base of the propagated data type `min([Slope1 Slope2])` (default) | `Slope1` | `Slope2` | `min([Slope1 Slope2])` | `max([Bias1 Bias2])` | `Slope1*Slope2` | `Slope1/Slope2` | `PosRange1` | `PosRange2` | `max([PosRange1 PosRange2])` | `min([PosRange1 PosRange2])` | `PosRange1*PosRange2` | `PosRange1/PosRange2`

Specify the slope used by **Prop** for the base data
type as one of the following values.

| Parameter Value | Description |
| --- | --- |
| `Slope1` | The slope of **Prop** is given by the slope of **Ref1**. |
| `Slope2` | The slope of **Prop** is given by the slope of **Ref2**. |
| `max([Slope1 Slope2])` | The slope of **Prop** is given by the maximum slope of the reference signals. |
| `min([Slope1 Slope2])` | The slope of **Prop** is given by the minimum slope of the reference signals. |
| `Slope1*Slope2` | The slope of **Prop** is given by the product of the reference signal slopes. |
| `Slope1/Slope2` | The slope of **Prop** is given by the ratio of the **Ref1** slope to the **Ref2** slope. |
| `PosRange1` | The range of **Prop** is given by the range of **Ref1**. |
| `PosRange2` | The range of **Prop** is given by the range of **Ref2**. |
| `max([PosRange1 PosRange2])` | The range of **Prop** is given by the maximum range of the reference signals. |
| `min([PosRange1 PosRange2])` | The range of **Prop** is given by the minimum range of the reference signals. |
| `PosRange1*PosRange2` | The range of **Prop** is given by the product of the reference signal ranges. |
| `PosRange1/PosRange2` | The range of **Prop** is given by the ratio of the **Ref1** range to the **Ref2** range. |

You control the precision of **Prop** with
`Slope1` and `Slope2`, and you
control the range of **Prop** with
`PosRange1` and `PosRange2`. Also,
`PosRange1` and `PosRange2` are
one bit higher than the maximum positive range of the associated
reference signal.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SlopeBase` |
| **Type:** character vector |
| **Values:** `'Slope1' | 'Slope2' | 'max([Slope1 Slope2])' | 'min([Slope1 Slope2])' | 'Slope1*Slope2' | 'Slope1/Slope2' | 'PosRange1' | 'PosRange2' | 'max([PosRange1 PosRange2])' | 'min([PosRange1 PosRange2])' | 'PosRange1*PosRange2' | 'PosRange1/PosRange2'` |
| **Default:** `'min([Slope1 Slope2])'` |

### **2.1.2. Slope: Multiplicative adjustment** — Slope of multiplicative adjustment of propagated data type `1` (default) | scalar

Specify the slope used by **Prop** by including a
multiplicative adjustment that uses a data type of
`double`. For example, if you want 3 bits of
additional precision (with a corresponding decrease in range), the
multiplicative adjustment is `2^-3`.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SlopeMult` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **2.1.3. Slope: Additive adjustment** — Slope of additive adjustment of propagated data type `0` (default) | scalar

Specify the slope used by **Prop** by including an
additive adjustment that uses a data type of `double`.
An additive slope adjustment is often not needed. The most likely use is
to set the multiplicative adjustment to `0`, and set
the additive adjustment to force the final slope to a specified
value.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SlopeAdd` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **2.2.1. Bias: Base** — Base bias for **Prop** `Bias1` (default) | `Bias2` | `max([Bias1 Bias2])` | `min([Bias1 Bias2])` | `Bias1*Bias2` | `Bias1/Bias2` | `Bias1+Bias2` | `Bias1-Bias2`

Specify the bias used by **Prop** for the base data
type. The parameter values are described as follows:

| Parameter Value | Description |
| --- | --- |
| `Bias1` | The bias of **Prop** is given by the bias of **Ref1**. |
| `Bias2` | The bias of **Prop** is given by the bias of **Ref2**. |
| `max([Bias1 Bias2])` | The bias of **Prop** is given by the maximum bias of the reference signals. |
| `min([Bias1 Bias2])` | The bias of **Prop** is given by the minimum bias of the reference signals. |
| `Bias1*Bias2` | The bias of **Prop** is given by the product of the reference signal biases. |
| `Bias1/Bias2` | The bias of **Prop** is given by the ratio of the **Ref1** bias to the **Ref2** bias. |
| `Bias1+Bias2` | The bias of **Prop** is given by the sum of the reference biases. |
| `Bias1-Bias2` | The bias of **Prop** is given by the difference of the reference biases. |

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BiasBase` |
| **Type:** character vector |
| **Values:** `'Bias1' | 'Bias2' | 'max([Bias1 Bias2])' | 'min([Bias1 Bias2])' | 'Bias1*Bias2' | 'Bias1/Bias2' | 'Bias1+Bias2' | 'Bias1-Bias2'` |
| **Default:** `'Bias1'` |

### **2.2.2. Bias: Multiplicative adjustment** — Multiplicative bias for propagated data type `1` (default) | scalar

Specify the bias used by Prop by including a multiplicative adjustment
that uses a data type of `double`.

This parameter is visible only when you set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BiasMult` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **2.3.2. Bias: Additive adjustment** — Additive bias for propagated data type `0` (default) | scalar

Specify the bias used by **Prop** by including an
additive adjustment that uses a data type of
`double`.

If you want to guarantee that the bias associated with
**Prop** is zero, configure both the multiplicative
adjustment and the additive adjustment to `0`.

#### Dependencies

To enable this parameter, set **Propagated
scaling** to `Inherit via propagation
rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BiasAdd` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block can be used to control scaling and
data types of signals that are part of subsystems that generate HDL code, but is
not included in the hardware implementation.

**Limitations**

When this block is present inside the masked subsystem, the block is ignored
in model generation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
