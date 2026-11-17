---
type: simulink-block
title: 'LSTM Projected Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Sequence Layers'
documentation_page: 'lstmprojectedlayer'
documentation_source_path: 'ref/lstmprojectedlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# LSTM Projected Layer

## 端口

### 输入

### **Port\_1** — 输入数据二维数组

输入数据。数据必须具有两个维度，依次对应通道和时间步。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据二维数组

投影 LSTM 运算的结果。输出数据具有两个维度，依次对应通道和时间步。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认）| `lstmProjectedLayer` 对象

指定包含来自已训练网络的 `lstmProjectedLayer` 对象的工作区变量名称。LSTM Projected Layer 模块通过使用该对象的属性来配置自身，并通过使用该对象的可学习参数来计算模块输出。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `lstmProjectedLayer` 对象 |
| **默认值：** `'layerObject'` |

### **Data format** — 输入数据的格式 `CT`（默认）

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持批量（`B`）维度，而是假定观测数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` |
| **默认值：** `'CT'` |

### **Stateful prediction** — 是否使用有状态预测 on（默认）| off

是否使用有状态预测，指定为布尔值。如果为 `true`，模块在时间步之间保持单元状态和隐藏状态。如果为 `false`，模块通过在每个时间步开始时将单元状态和隐藏状态重置为其初始值来执行无状态预测。对于基于帧的处理，其中 Simulink 步进时间表示帧周期且网络在每个时间步处理多个样本时，请使用无状态预测。有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StatefulPrediction` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### 数据类型

### **Activation approximation method** — 计算激活函数输出的近似方法 `None`（默认）| `CORDIC` | `Lookup`

如果作为 **Layer** 参数值传递的对象使用 `tanh` 状态激活函数或 `sigmoid` 门激活函数，则模块使用您指定的近似方法来计算层输出。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您仅处理浮点数据。 |
| `CORDIC` | 浮点（double 和 single）以及 **Bias** 值为 `0` 且 **Slope** 值为 2 的幂的定点 | 您处理定点数据并希望部署到 FPGA 硬件。 |
| `Lookup` | 浮点和定点 | 您处理定点数据并希望生成 C/C++ 代码。 |

有关 CORDIC 近似方法的详细信息，请参阅 `cordictanh` (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None'` | `'CORDIC'` | `'Lookup'` |
| **默认值：** `'None'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Inherit: Inherit via internal rule` 以外的值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Inherit: Inherit via internal rule` 以外的值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会在考虑嵌入式目标硬件属性的同时，选择一种数据类型以平衡数值精度、性能和生成的代码大小。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，表示为 `int8` 的模块结果 130（二进制 1000 0010）为 –126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还可以帮助您避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 当您选择此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Input weights** — 输入权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `InputWeights` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Recurrent weights** — 循环权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `RecurrentWeights` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RecurrentWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Bias** — 偏置的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `Bias` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BiasDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Input projector weights** — 输入投影权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `InputProjector` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关详细信息，请参阅 LSTM Projected Layer。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InputProjectorWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Output projector weights** — 输出投影权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `OutputProjector` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关详细信息，请参阅 LSTM Projected Layer。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputProjectorWeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Initial cell state** — 初始单元状态的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `CellState` 属性的值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

此参数仅影响初始单元状态 *c*0。要转换后续的单元状态值，请使用 **Cell state** 参数。有关详细信息，请参阅 Long Short-Term Memory Layer

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TODODataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Cell state** — 单元状态的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Sum 模块
`ForIteratorSubsystem/LSTMProjectedCore/CellAdd` 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Sum 模块计算
单元状态 *c**t* 为 *c**t*=*f**t*⊙*c**t*-1+*i**t*⊙*g**t*，其中 *i*、*f* 和
*g* 分别表示输入门、遗忘门和单元候选门，
⊙ 表示 Hadamard 积（向量的逐元素乘法）。有关详细信息，请参阅 Long Short-Term Memory Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CellStateDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Initial hidden state** — 初始隐藏状态的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

该模块将通过 **Layer** 参数指定的对象的 `HiddenState` 属性值
转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

此参数仅影响初始隐藏状态 *h*0。要转换后续的隐藏状态值，请使用 **Hidden
state** 参数。有关详细信息，请参阅 Long Short-Term Memory Layer

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitialHiddenStateDataTypeStr` |
| **值**：| `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Hidden state** — 隐藏状态的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Product 模块
`ForIteratorSubsystem/LSTMProjectedCore/HiddenStateProduct` 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算
隐藏状态 *h**t* 为 *h**t*=*o**t*⊙*σ**c*(*c**t*)，其中 *o* 表示输出门，*σ**c* 表示
状态激活函数，⊙ 表示 Hadamard 积（向量的逐元素
乘法）。有关详细信息，请参阅 Long Short-Term Memory Layer 和 LSTM Projected Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `HiddenStateDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Input weights matrix multiply output** — 输入权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Product 模块
`InputWeightsMatrixMultiply/W*x` 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算
输入权重（*W*）与时间步 *t* 的投影输入（*x**t*）的乘积。有关
详细信息，请参阅 Long Short-Term Memory Layer 和 LSTM Projected Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputWeightsMatrixMulitplyOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Recurrent weights matrix multiply output** — 循环权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Product 模块
`ForIteratorSubsystem/LSTMProjectedCore/RecurrentWeightsMatrixMultiply/R*h_t-1`
输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算
循环权重（*R*）与上一时间步的投影隐藏
状态（*h**t*-1）的乘积。有关
详细信息，请参阅 Long Short-Term Memory Layer 和 LSTM Projected Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RecurrentWeightsMatrixMulitplyOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Input projector weights matrix multiply output** — 输入投影权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Product 模块
`InputWeightsMatrixMultiply/x'*Q_in` 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

Product 模块计算转置输入
（*x*T）与输入投影权重
（*Q*in）的乘积。有关详细信息，请参阅 LSTM Projected Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Output projector weights matrix multiply output** — 输出投影权重矩阵乘法输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Product 模块
`ForIteratorSubsystem/LSTMProjectedCore/RecurrentWeightsMatrixMultiply/h_t-1'*Q_out`
输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算
转置的上一隐藏状态
（*h**t*-1T）
与输出投影权重（*Q*out）的乘积。有关
详细信息，请参阅 LSTM Projected Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutputProjectorWeightsMatrixMultiplyOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Linear gate accumulator** — 线性门累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Sum 模块
`ForIteratorSubsystem/LSTMProjectedCore/LinearGateAdd/Wx+Rh+b`
累加器的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

Sum 模块计算和 *W**QinT**x*+*R**QoutT**h*t+*b*，其中 *W* 表示输入权重，
*Qin* 表示输入投影矩阵，
*x* 表示输入，*R* 表示循环
权重，*Qout* 表示输出投影
矩阵，*h**t* 表示
时间步 *t* 的隐藏状态，*b* 表示
偏置。有关详细信息，请参阅 Long Short-Term Memory Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LinearGateAccumDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as first input'` | `<data type expression>` |

### **Linear gate add output** — 线性门求和的数据类型 `Inherit: Same as first input`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Inherit via internal rule` | `Inherit: Same as accumulator` | `<data type expression>`

选择 LSTM Projected Layer 模块内 Sum 模块
`ForIteratorSubsystem/LSTMProjectedCore/LinearGateAdd/Wx+Rh+b`
输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

Sum 模块计算和 *W**QinT**x*+*R**QoutT**h*t+*b*，其中 *W* 表示输入权重，
*Qin* 表示输入投影矩阵，
*x* 表示输入，*R* 表示循环
权重，*Qout* 表示输出投影
矩阵，*h**t* 表示
时间步 *t* 的隐藏状态，*b* 表示
偏置。有关详细信息，请参阅 Long Short-Term Memory Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LinearGateAddOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Gate activation output** — 门激活输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `<data type expression>`

选择门激活函数输出的数据类型。有关门激活函数的详细信息，请参阅 **GateActivationFunction**。有关 LSTM 层如何使用激活函数的详细信息，请参阅 Long Short-Term Memory Layer。

该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `GateActivationoutDataTypeStr` |
| **值**：| `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `<data type expression>` |

### **State activation output** — 状态激活输出的数据类型 `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as first input'` | `<data type expression>`

选择状态激活函数输出的数据类型。有关状态激活函数的详细信息，请参阅 **StateActivationFunction**。有关 LSTM 层如何使用激活函数的详细信息，请参阅 Long Short-Term Memory Layer。

该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，以在数值精度、性能和生成代码
大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `StateActivationOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as first input'` | `<data type expression>` |

### **Cell state product output** — 单元状态乘积输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 LSTM 投影层模块内部 Product 模块
`ForIteratorSubsystem/LSTMProjectedCore/f*c_t-1` 和
`ForIteratorSubsystem/LSTMProjectedCore/i*g` 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会在兼顾数值精度、性能和生成代码大小的前提下选择数据类型，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Product 模块计算
Hadamard 乘积（向量逐元素乘法，记为 ⊙）*f*t⊙*c**t*-1 和 *i**t*⊙*g**t*，其中 *f* 表示遗忘门，
*c* 表示单元状态，*i* 表示输入门，*g* 表示候选单元。有关详细信息，请参阅
Long Short-Term Memory Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CellStateProductOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Cell state accumulator** — 单元状态累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `<data type expression>`

选择 LSTM 投影层模块内部 Sum 模块
`ForIteratorSubsystem/LSTMProjectedCore/CellAdd` 累加器的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会在兼顾数值精度、性能和生成代码大小的前提下选择数据类型，同时考虑嵌入式目标硬件的属性。

对于时间步 *t*，Sum 模块计算
单元状态 *c**t* 如下

|  |  |
| --- | --- |
| *c**t*=*f**t*⊙*c**t*-1+*i**t*⊙*g**t* | **(1)** |

，

其中 *i*、*f* 和 *g* 分别表示
输入门、遗忘门和候选单元门，⊙ 表示
Hadamard 乘积（向量逐元素乘法）。有关详细信息，请参阅
Long Short-Term Memory Layer。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CellStateProductOutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as first input'` | `<data type expression>` |

### Execution

### **Sample time** — 指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，
请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **值**：`'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Sequence Layers

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在之前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink 并依赖于名称为 `'layer'` 的变量，请更新您的代码，使该变量的名称为 `'layerObject'`。

### R2025a：**Gate activation output** 和 **State activation output** 参数

新增的 **Gate activation output** 和 **State activation
output** 参数用于控制门激活和状态激活的数据类型
outputs.

### R2025a：**Linear gate add output** 参数默认值为 `Inherit: Same as first input`

**Linear gate add output** 的默认值现在为
`Inherit: Same as first input`.

## 描述

Long short-term memory (LSTM) projected layer for recurrent neural network (RNN)

LSTM Projected Layer 模块表示一个循环神经网络 (RNN)
层，该层通过使用投影可学习权重，学习 `CT` 格式（两个维度分别对应通道和时间步，按此顺序）的时间序列和序列数据中
时间步之间的长期依赖关系。

要压缩深度学习网络，您可以使用*投影层*。投影层是一种深度学习层，通过减少存储的可学习参数数量来实现压缩。该层引入可学习投影矩阵
*Q*，将形如 Wx 的乘法（其中 *W* 是可学习矩阵）替换为乘法 WQQ⊤x，并存储 *Q* 和 W′=WQ 而不是存储 *W*。使用 *Q* 将 *x*
投影到低维空间通常需要更少的内存来存储可学习参数，并且可以具有同样强的预测精度。

通过投影 LSTM 层而不是减少 LSTM 层的隐藏单元数量来减少可学习参数数量，可以保持该层的输出大小，
进而保持下游层的大小，这可以获得更好的预测精度。

`exportNetworkToSimulink` 函数生成此模块以表示 `lstmProjectedLayer`
对象。
