---
type: simulink-block
title: 'Data Type Propagation'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypepropagation'
documentation_source_path: 'slref/datatypepropagation.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Propagation

## 端口

### 输入

### **Ref1** — 第一参考信号 标量 | 向量 | 矩阵 | N 维数组

第一参考信号，用于从中收集数据类型和定标信息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Ref2** — 第二参考信号 标量 | 向量 | 矩阵 | N 维数组

第二参考信号，用于从中收集数据类型和定标信息。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Prop** — 传播的数据类型和定标 数据类型和定标

数据类型和定标信息，反向传播到模型。在模块从参考信号收集数据类型和定标信息后，您可以对数据类型和定标应用第二级调整。为此，请在模块对话框中指定各自的乘法和加法调整。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### Propagated Type

### **1. Propagated data type** — 指定传播数据类型的模式 `Inherit via propagation rule`（默认）| `Specify via dialog`

指定是通过对话框传播数据类型，还是从参考信号继承数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`PropDataTypeMode` |
| **类型**：character vector |
| **值**：`'Specify via dialog' | 'Inherit via propagation rule'` |
| **默认值**：`'Inherit via propagation rule'` |

### **1.1. Propagated data type (e.g. fixdt(1,16), fixdt('single'))** — 传播的数据类型 `fixdt(1,16)`（默认）| 数据类型字符串

指定要传播的数据类型。

#### 依赖关系

要启用此参数，请将 **1. Propagated data type** 设置为 `Specify via dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PropDataType` |
| **类型**：character vector |
| **值**：`'fixdt(1, 16)'` | data type string in quotes |
| **默认值**：`'fixdt(1, 16)'` |

### **1.1 If any reference input is double, output is** — 当参考输入为 double 时的输出数据类型 `double`（默认）| `single`

将输出数据类型指定为 `single` 或 `double`。此参数使创建易于在定点芯片和浮点芯片之间重新定位的设计变得更加容易。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IfRefDouble` |
| **类型**：character vector |
| **值**：`'double' | 'single'` |
| **默认值**：`'double'` |

### **1.2 If any reference input is single, output is** — 当参考输入为 single 时的输出数据类型 `single`（默认）| `double`

将输出数据类型指定为 `single` 或 `double`。此参数使创建易于在定点芯片和浮点芯片之间重新定位的设计变得更加容易。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IfRefSingle` |
| **类型**：character vector |
| **值**：`'double' | 'single'` |
| **默认值**：`'single'` |

### **1.3 Is-Signed** — 传播数据类型的符号性 `IsSigned1 or IsSigned2`（默认）| `IsSigned1` | `IsSigned2` | `TRUE` | `FALSE`

将 **Prop** 的符号指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `IsSigned1` | 如果 **Ref1** 是有符号数据类型，则 **Prop** 为有符号数据类型。 |
| `IsSigned2` | 如果 **Ref2** 是有符号数据类型，则 **Prop** 为有符号数据类型。 |
| `IsSigned1 or IsSigned2` | 如果 **Ref1** 或 **Ref2** 是有符号数据类型，则 **Prop** 为有符号数据类型。 |
| `TRUE` | 忽略 **Ref1** 和 **Ref2**，Prop 始终为有符号数据类型。 |
| `FALSE` | 忽略 **Ref1** 和 **Ref2**，Prop 始终为无符号数据类型。 |

例如，如果 **Ref1** 信号为 `ufix(16)`，**Ref2** 信号为 `sfix(16)`，且 **Is-Signed** 参数为 `IsSigned1 or IsSigned2`，则 **Prop** 被强制为有符号数据类型。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IsSigned` |
| **类型**：character vector |
| **值**：`'IsSigned1' | 'IsSigned2' | 'IsSigned1 or IsSigned2' | 'TRUE' | 'FALSE'` |
| **默认值**：`'IsSigned1 or IsSigned2'` |

### **1.4.1 Number-of-bits: Base** — 传播数据类型基数的位数 `max([NumBits1 NumBits2])`（默认）| `NumBits1` | `NumBits2` | `min([NumBits1 NumBits2])` | `NumBits1+NumBits2`

将 **Prop** 用于基数数据类型的位数指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `NumBits1` | **Prop** 的位数由 **Ref1** 的位数给出。 |
| `NumBits2` | **Prop** 的位数由 **Ref2** 的位数给出。 |
| `max([NumBits1 NumBits2])` | **Prop** 的位数由位数最多的参考信号给出。 |
| `min([NumBits1 NumBits2])` | **Prop** 的位数由位数最少的参考信号给出。 |
| `NumBits1+NumBits2` | **Prop** 的位数由参考信号位数之和给出。 |

有关基数数据类型的详细信息，请参阅 Targeting an Embedded Processor (Fixed-Point Designer)。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumBitsBase` |
| **类型**：character vector |
| **值**：`'NumBits1' | 'NumBits2' | 'max([NumBits1 NumBits2])' | 'min([NumBits1 NumBits2])' | 'NumBits1+NumBits2'` |
| **默认值**：`'max([NumBits1 NumBits2])'` |

### **1.4.2 Number-of-bits: Multiplicative adjustment** — 传播数据类型乘法调整的位数 `1`（默认）| 正整数

通过包含使用 `double` 数据类型的乘法调整来指定 **Prop** 使用的位数。例如，假设您要保证与乘法累加（MAC）操作相关的位数是输入信号的两倍宽。为此，请将此参数设置为 `2`。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumBitsMult` |
| **类型**：character vector |
| **值**：positive integer |
| **默认值**：`'1'` |

### **1.4.3 Number-of-bits: Additive adjustment** — 传播数据类型加法调整的位数 `0`（默认）| 正整数

通过包含使用 `double` 数据类型的加法调整来指定 **Prop** 使用的位数。例如，如果在 MAC 操作期间执行多次加法，结果可能会溢出。为防止溢出，您可以将保护位与传播数据类型关联。要关联四个保护位，请指定值 `4`。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumBitsAdd` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'0'` |

### **1.4.4 Number-of-bits: Allowable final values** — 传播数据类型中允许的位数 `'-1'`（默认）| 正整数标量或向量

将 **Prop** 使用的计算位数强制为有用的值。例如，如果您面向仅支持 8 位、16 位和 32 位的处理器，则将此参数配置为 `[8,16,32]`。模块始终传播适合的最小指定值。如果要允许所有定点数据类型，请指定值 `-1`。

#### 依赖关系

要启用此参数，请将 **Propagated data type** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumBitsAllowFinal` |
| **类型**：character vector |
| **值**：scalar or vector of positive integers |
| **默认值**：`'-1'` |

### Propagated Scaling

### **2. Propagated scaling** — 传播定标模式 `Inherit via propagation rule`（默认）| `Specify via dialog` | `Obtain via best precision`

选择通过对话框传播定标、从参考信号继承定标，或计算定标以获得最佳精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`PropScalingMode` |
| **类型**：character vector |
| **值**：`'Inherit via propagation rule'` | `'Specify via dialog'` | `'Obtain via best precision'` |
| **默认值**：`'Inherit via propagation rule'` |

### **2.1. Propagated scaling (Slope, e.g. 2^-9 or [Slope Bias], e.g. [1.25 3])** — 斜率或斜率和偏置 `2^-10` | 斜率 | 方括号中的斜率和偏置

将定标指定为斜率或斜率和偏置。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Specify via dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PropScaling` |
| **类型**：character vector |
| **值**：slope | slope and bias in square brackets |
| **默认值**：`'2^-10'` |

### **2.1. Values used to determine best precision scaling** — 用于约束精度的值 `[5 -7]`（默认）

指定用于约束精度的任何值，例如传播输入的上限和下限。根据数据类型，模块选择一种定标，使得这些值可以在无溢出误差且量化误差最小的情况下表示。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Obtain via best precision`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ValuesUsedBestPrec` |
| **类型**：character vector |
| **值**：vector of values |
| **默认值**：`'[5 -7]'` |

### **2.1.1. Slope: Base** — 传播数据类型基数的斜率 `min([Slope1 Slope2])`（默认）| `Slope1` | `Slope2` | `min([Slope1 Slope2])` | `max([Bias1 Bias2])` | `Slope1*Slope2` | `Slope1/Slope2` | `PosRange1` | `PosRange2` | `max([PosRange1 PosRange2])` | `min([PosRange1 PosRange2])` | `PosRange1*PosRange2` | `PosRange1/PosRange2`

将 **Prop** 用于基数数据类型的斜率指定为以下值之一。

| 参数值 | 描述 |
| --- | --- |
| `Slope1` | **Prop** 的斜率由 **Ref1** 的斜率给出。 |
| `Slope2` | **Prop** 的斜率由 **Ref2** 的斜率给出。 |
| `max([Slope1 Slope2])` | **Prop** 的斜率由参考信号的最大斜率给出。 |
| `min([Slope1 Slope2])` | **Prop** 的斜率由参考信号的最小斜率给出。 |
| `Slope1*Slope2` | **Prop** 的斜率由参考信号斜率的乘积给出。 |
| `Slope1/Slope2` | **Prop** 的斜率由 **Ref1** 斜率与 **Ref2** 斜率之比给出。 |
| `PosRange1` | **Prop** 的范围由 **Ref1** 的范围给出。 |
| `PosRange2` | **Prop** 的范围由 **Ref2** 的范围给出。 |
| `max([PosRange1 PosRange2])` | **Prop** 的范围由参考信号的最大范围给出。 |
| `min([PosRange1 PosRange2])` | **Prop** 的范围由参考信号的最小范围给出。 |
| `PosRange1*PosRange2` | **Prop** 的范围由参考信号范围的乘积给出。 |
| `PosRange1/PosRange2` | **Prop** 的范围由 **Ref1** 范围与 **Ref2** 范围之比给出。 |

您通过 `Slope1` 和 `Slope2` 控制 **Prop** 的精度，并通过 `PosRange1` 和 `PosRange2` 控制 **Prop** 的范围。此外，`PosRange1` 和 `PosRange2` 比相关参考信号的最大正范围高一位。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SlopeBase` |
| **类型**：character vector |
| **值**：`'Slope1' | 'Slope2' | 'max([Slope1 Slope2])' | 'min([Slope1 Slope2])' | 'Slope1*Slope2' | 'Slope1/Slope2' | 'PosRange1' | 'PosRange2' | 'max([PosRange1 PosRange2])' | 'min([PosRange1 PosRange2])' | 'PosRange1*PosRange2' | 'PosRange1/PosRange2'` |
| **默认值**：`'min([Slope1 Slope2])'` |

### **2.1.2. Slope: Multiplicative adjustment** — 传播数据类型乘法调整的斜率 `1`（默认）| 标量

通过包含使用 `double` 数据类型的乘法调整来指定 **Prop** 使用的斜率。例如，如果您想要额外 3 位的精度（范围相应减小），则乘法调整为 `2^-3`。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SlopeMult` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'1'` |

### **2.1.3. Slope: Additive adjustment** — 传播数据类型加法调整的斜率 `0`（默认）| 标量

通过包含使用 `double` 数据类型的加法调整来指定 **Prop** 使用的斜率。通常不需要加法斜率调整。最可能的用途是将乘法调整设置为 `0`，并设置加法调整以将最终斜率强制为指定值。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SlopeAdd` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'0'` |

### **2.2.1. Bias: Base** — **Prop** 的基数偏置 `Bias1`（默认）| `Bias2` | `max([Bias1 Bias2])` | `min([Bias1 Bias2])` | `Bias1*Bias2` | `Bias1/Bias2` | `Bias1+Bias2` | `Bias1-Bias2`

指定 **Prop** 用于基数数据类型的偏置。参数值描述如下：

| 参数值 | 描述 |
| --- | --- |
| `Bias1` | **Prop** 的偏置由 **Ref1** 的偏置给出。 |
| `Bias2` | **Prop** 的偏置由 **Ref2** 的偏置给出。 |
| `max([Bias1 Bias2])` | **Prop** 的偏置由参考信号的最大偏置给出。 |
| `min([Bias1 Bias2])` | **Prop** 的偏置由参考信号的最小偏置给出。 |
| `Bias1*Bias2` | **Prop** 的偏置由参考信号偏置的乘积给出。 |
| `Bias1/Bias2` | **Prop** 的偏置由 **Ref1** 偏置与 **Ref2** 偏置之比给出。 |
| `Bias1+Bias2` | **Prop** 的偏置由参考偏置之和给出。 |
| `Bias1-Bias2` | **Prop** 的偏置由参考偏置之差的给出。 |

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Inherit via propagation rule`。

#### 编程使用

|  |
| --- |
| **模块参数**：`BiasBase` |
| **类型**：character vector |
| **值**：`'Bias1' | 'Bias2' | 'max([Bias1 Bias2])' | 'min([Bias1 Bias2])' | 'Bias1*Bias2' | 'Bias1/Bias2' | 'Bias1+Bias2' | 'Bias1-Bias2'` |
| **默认值**：`'Bias1'` |

### **2.2.2. Bias: Multiplicative adjustment** — 传播数据类型的乘法偏置 `1`（默认）| 标量

通过包含使用 `double` 数据类型的乘法调整来指定 Prop 使用的偏置。

仅当您将 **Propagated scaling** 设置为 `Inherit via propagation rule` 时，此参数才可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`BiasMult` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'1'` |

### **2.3.2. Bias: Additive adjustment** — 传播数据类型 `0`（默认）| 标量的加性偏置

通过包含使用 `double` 数据类型的加性调整，指定 **Prop** 所使用的偏置。

如果要保证与 **Prop** 关联的偏置为零，请将乘性调整和加性调整都配置为 `0`。

#### 依赖关系

要启用此参数，请将 **Propagated scaling** 设置为 `Inherit via propagation rule`。

#### 编程用法

|  |
| --- |
| **模块参数：** `BiasAdd` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块可用于控制作为生成 HDL 代码的子系统一部分的信号的比例和数据类型，但不包含在硬件实现中。

**限制**

当此模块存在于掩码子系统内部时，该模块在模型生成中会被忽略。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

基于参考信号中的信息设置传播信号的数据类型和定标

Data Type Propagation 模块允许您控制模型中信号的数据类型和定标。您可以将此模块与 **Output data type** 参数配置为 `Inherit: Inherit via back propagation` 的定点模块一起使用。

该模块有三个输入：**Ref1** 和 **Ref2** 是参考输入，而 **Prop** 输入反向传播从参考输入收集的数据类型和定标信息。然后，此信息会传递到其他定点模块。

该模块为传播数据类型和定标信息提供了多种选择。例如，您可以使用：

- 来自 **Ref1** 参考信号的位数或来自最宽参考信号的位数
- 来自 **Ref2** 参考信号的范围或具有最大范围的参考信号的范围
- 偏置为零，无论参考信号使用的偏置是什么
- 精度最低的参考信号的精度

您使用 **Propagated data type** 参数指定数据类型信息的传播方式：

- 如果选择 `Specify via dialog`，则通过 **Propagated data type** 编辑字段手动指定数据类型。
- 如果选择 `Inherit via propagation rule`，则必须使用参数中所述的参数。

您使用 **Propagated scaling** 参数指定定标信息的传播方式：

- 如果选择 `Specify via dialog`，则通过 **Propagated scaling** 编辑字段手动指定定标。
- 如果选择 `Inherit via propagation rule`，则必须使用参数中所述的参数。

使用参考信号中的信息后，您可以对数据类型和定标应用第二级调整。为此，请使用单独的乘性和加性调整。这种灵活性有多种用途。例如，如果您的目标是 DSP，则可以将模块配置为与乘法累加（MAC）运算关联的位数是输入信号的两倍宽，并添加特定数量的保护位。

Data Type Propagation 模块还提供了一种机制，用于将计算出的位数强制为有用的值。例如，如果您的目标是 16 位微处理器，则目标 C 编译器可能仅支持 8 位、16 位和 32 位的大小。该模块强制使用这三种选择。例如，假设该模块计算出数据类型大小为 24 位。由于 24 位不能直接由目标芯片使用，因此信号会被强制提升到原生支持的 32 位。

还有一种处理浮点参考信号的方法。此方法使创建可在定点芯片和浮点芯片之间轻松重定向的设计变得更加容易。

Data Type Propagation 模块允许您建立有用子系统的库，这些子系统会根据所连接的信号进行正确配置。如果没有此数据类型传播过程，库中的子系统不太可能按预期与大多数整数或定点信号一起工作。将需要手动干预来配置数据类型和定标。在许多情况下，此模块可以消除手动干预。

### 优先级规则

对话框参数的优先级从上到下递减。此外：

- 双精度参考输入的优先级高于所有其他数据类型。
- 单精度参考输入的优先级高于整数和定点数据类型。
- 乘性调整在加性调整之前执行。
- 位数在从参考输入继承精度或正范围之前确定。
- `PosRange` 比信号的精确最大正范围高一位。
- 计算出的位数会被提升为大于或等于计算结果的最小允许值。如果不存在这样的值，则模块返回错误。
