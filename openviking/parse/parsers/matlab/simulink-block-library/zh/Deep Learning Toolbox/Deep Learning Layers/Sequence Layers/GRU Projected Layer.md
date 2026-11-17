---
type: simulink-block
title: 'GRU Projected Layer'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Sequence Layers'
documentation_page: 'gruprojectedlayer'
documentation_source_path: 'ref/gruprojectedlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# GRU Projected Layer

## 端口

### 输入

### **Port\_1** — 输入数据向量 | 二维数组

输入数据。数据必须具有两个维度，分别对应通道和时间步，按此顺序，或者一个维度对应通道。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 二维数组

将 GRU projected 操作应用于输入数据的结果。输出数据具有两个维度，分别对应通道和时间步，按此顺序。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。从 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应层对象 `layerObject`（默认）| `gruProjectedLayer` 对象

指定包含经过训练网络的 `gruProjectedLayer` 对象的工作区变量名称。GRU Projected Layer 模块使用该对象的属性自行配置，并使用该对象的可学习参数计算模块输出。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `gruProjectedLayer` 对象 |
| **默认：** `'layerObject'` |

### **Data format** — 输入数据的格式 `CT`（默认）

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假设观测数为 `1`。

#### 程序化用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` |
| **默认：** `'CT'` |

### **Stateful prediction** — 是否使用有状态预测 on（默认）| off

是否使用有状态预测，指定为布尔值。如果 `true`，模块在时间步之间保持隐藏状态。如果 `false`，模块通过在每个时间步开始时将隐藏状态重置为其初始值来执行无状态预测。将无状态预测用于基于帧的处理，其中 Simulink 步长时间表示帧周期，并且网络在每个时间步处理多个样本。有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 程序化用法

|  |
| --- |
| **模块参数：** `StatefulPrediction` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### 数据类型

### **Activation approximation method** — 计算激活函数输出的近似方法 `None`（默认）| `CORDIC` | `Lookup`

如果作为 **Layer** 参数值传递的对象使用 `tanh` 状态激活函数或 `sigmoid` 门激活函数，则模块使用您指定的近似方法计算层输出。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您仅处理浮点数据。 |
| `CORDIC` | 浮点（double 和 single）以及 **Bias** 值为 `0` 且 **Slope** 值为 2 的幂的定点 | 您处理定点数据并希望部署到 FPGA 硬件。 |
| `Lookup` | 浮点和定点 | 您处理定点数据并希望生成 C/C++ 代码。 |

有关 CORDIC 近似方法的详细信息，请参阅 `cordictanh` (Fixed-Point Designer)。

#### 程序化用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None'` | `'CORDIC'` | `'Lookup'` |
| **默认：** `'None'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Inherit: Inherit via internal rule` 以外的值。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 引号中的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Inherit: Inherit via internal rule` 以外的值。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 引号中的标量 |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `<data type expression>`

选择输出的数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 将输出数据类型设置为与隐藏状态相同的类型。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 当您选择此参数时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Input weights** — 输入权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `InputWeights` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Recurrent weights** — 循环权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `RecurrentWeights` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RecurrentWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Bias** — 偏置的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Bias` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BiasDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Input projector weights** — 输入投影权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `InputProjector` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关详细信息，请参阅 GRU Projected Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputProjectorWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Output projector weights** — 输出投影权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `OutputProjector` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关详细信息，请参阅 GRU Projected Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputProjectorWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Initial hidden state** — 初始隐藏状态的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `HiddenState` 属性的值转换为该数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

此参数仅影响初始隐藏状态 *h*0。要转换之后的隐藏状态值，请使用 **Hidden state** 参数。有关详细信息，请参阅 Gated Recurrent Unit Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialHiddenStateDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Hidden state** — 隐藏状态的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 GRU Projected Layer 模块内子系统 `ForIteratorSubsystem/HiddenState` 的输出的数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，该子系统计算隐藏状态 *h**t* 为

ht=(1−zt)⊙h˜t+zt⊙ht−1.

，其中 ⊙ 表示 Hadamard 积（向量的逐元素乘法）。有关详细信息，请参阅 Gated Recurrent Unit Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `HiddenStateDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Input weights matrix multiply output** — 输入权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 GRU Projected Layer 模块内 Product 模块 `InputWeightsMatrixMultiply/W*x` 的输出的数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算输入权重 (*W*) 与时间步输入 (*x**t*) 的乘积。有关详细信息，请参阅 Gated Recurrent Unit Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputWeightsMatrixMulitplyOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Recurrent weights matrix multiply output** — 循环权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 GRU Projected Layer 模块内这些子系统内 Matrix Multiply 模块的输出的数据类型。

- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_after-multiplication/R*h
  terms`
- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_before-multiplication/R*h
  terms`
- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_recurrent-bias-after-multiplication/R*h
  terms`

类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算循环权重 (*R*) 与上一时间步隐藏状态 (*h**t*-1) 的乘积。有关详细信息，请参阅 Gated Recurrent Unit Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RecurrentWeightsMatrixMulitplyOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Input projector weights matrix multiply output** — 输入投影权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 GRU Projected Layer 模块内 Product 模块 `InputWeightsMatrixMultiply/Q_in'*x_full` 的输出的数据类型。类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

Product 模块计算转置的输入投影权重 (*Q*inT) 与输入 (*x\_full*) 的乘积。有关详细信息，请参阅 GRU Projected Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Output projector weights matrix multiply output** — 输出投影权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 GRU Projected Layer 模块内这些子系统内 Matrix Multiply 模块的输出的数据类型。

- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_after-multiplication/R*h
  terms/ProjectHiddenState`
- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_before-multiplication/R*h
  terms/ProjectHiddenState`
- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_before-multiplication/R*h
  terms/ProjectHadamardProduct`
- `ForIteratorSubsystem/ResetGateMode/ResetGateMode_recurrent-bias-after-multiplication/R*h
  terms/ProjectHiddenState`

类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算转置的上一隐藏状态 (*h**t*-1T) 与输出投影权重 (*Q*out) 的乘积。有关详细信息，请参阅 GRU Projected Layer。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### 执行

### **Sample time** — 指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据模型中模块的上下文继承其采样时间。

#### 程序化用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Sequence Layers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

Gated recurrent unit (GRU) projected layer for recurrent neural network (RNN)

GRU Projected Layer 模块表示循环神经网络 (RNN) 层，该层通过使用投影可学习权重，学习 `CT` 格式（两个维度分别对应通道和时间步，按此顺序）的时间序列和序列数据中时间步之间的依赖关系。

要压缩深度学习网络，可以使用 *投影层*。投影层是一种深度学习层，通过减少存储的可学习参数数量实现压缩。该层引入可学习投影矩阵 *Q*，将形式为 Wx 的乘法（其中 *W* 是可学习矩阵）替换为乘法 WQQ⊤x，并存储 *Q* 和 W′=WQ，而不是存储 *W*。使用 *Q* 将 *x* 投影到低维空间通常需要更少内存来存储可学习参数，并且可以具有类似强的预测精度。

通过投影 GRU 层而不是减少 GRU 层的隐藏单元数量来减少可学习参数数量，会保持该层的输出大小，进而保持下游层的大小，这可以提高预测精度。

`exportNetworkToSimulink` 函数生成此模块以表示 `gruProjectedLayer` 对象。
