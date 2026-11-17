---
type: simulink-block
title: 'ClassificationNeuralNetwork Predict'
family: 'classification'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationneuralnetworkpredict'
documentation_source_path: 'classificationneuralnetworkpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationNeuralNetwork Predict

## 端口

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量必须与训练由 **选择训练好的机器学习模型** 指定的模型所使用的预测变量具有相同的顺序。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **label** — 预测类标签 标量

预测类标签，以标量形式返回。预测类是最小化预期分类成本的类。有关详细信息，请参阅 `predict` 函数参考页的“更多信息”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率 行向量

预测类分数或后验概率，以大小为 1×*k* 的行向量形式返回，其中 *k* 是神经网络模型中的类数。分类分数 `Score(i)` 表示 **x** 中的观测属于类 `i` 的后验概率。

要检查类的顺序，请使用由 **选择训练好的机器学习模型** 指定的神经网络模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“块参数”对话框的 **主要** 选项卡上选中 **添加预测类分数的输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **选择训练好的机器学习模型** — 神经网络分类模型 `nnetMdl`（默认）| `ClassificationNeuralNetwork` 对象 | `CompactClassificationNeuralNetwork` 对象

指定包含 `ClassificationNeuralNetwork` 对象或 `CompactClassificationNeuralNetwork` 对象的工作区变量的名称。

使用 `fitcnet` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果以表形式提供训练数据，则预测变量必须为数值（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- `ScoreTransform` 名称-值参数的值不能为 `'invlogit'` 或匿名函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationNeuralNetwork` 对象 | `CompactClassificationNeuralNetwork` 对象 |
| **默认值：** `'nnetMdl'` |

### **添加预测类分数的输出端口** — 添加用于预测类分数的第二个输出端口 `off`（默认）| `on`

选中此复选框可在 ClassificationNeuralNetwork Predict 模块中包含第二个输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### 数据类型

#### 定点操作参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 原因 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出会饱和到该数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误 (Simulink)。 | 溢出会回绕到该数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **标签数据类型** — 标签输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

支持的数据类型取决于由 **选择训练好的机器学习模型** 指定的模型中所使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、fixed point 以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **标签数据类型**（请参阅数据类型传播 (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设由 **选择训练好的机器学习模型** 指定的工作区变量名为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签） | `"Inherit: auto"`（对于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**标签数据类型最小值** 参数不会使实际 **label** 输出信号饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择训练好的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **标签数据类型最大值** — 用于范围检查的标签输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**标签数据类型最大值** 参数不会使实际 **label** 输出信号饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择训练好的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **分数数据类型** — 分数输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **分数数据类型最小值** — 用于范围检查的分数输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**分数数据类型最小值** 参数不会使实际 **score** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **分数数据类型最大值** — 用于范围检查的分数输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**分数数据类型最大值** 参数不会使实际 **score** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **原始分数数据类型** — 未变换的分数数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换分数的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

仅当由 **Select trained machine learning model** 指定的模型使用除 `"none"`（默认，与 `"identity"` 相同）之外的分数变换时，才能指定此参数。

- 如果模型不使用分数变换（`"none"` 或 `"identity"`），则可以使用 **Score data type** 指定分数数据类型。
- 如果模型使用除 `"none"` 或 `"identity"` 之外的分数变换，则可以使用此参数指定未变换原始分数的数据类型。要指定变换后分数的数据类型，请使用 **Score data type**。

您可以在训练期间指定 `ScoreTransform` 名称-值参数，或在训练后修改 `ScoreTransform` 属性，来更改分数变换选项。

#### 程序化使用

|  |
| --- |
| **模块参数**: `RawScoreDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **Raw score data type Minimum** — 用于范围检查的最小未变换分数 `[]`（默认）| scalar

指定 Simulink 检查的未变换分数范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Raw score data type Minimum** 参数不会饱和或裁剪实际的未变换分数信号。

#### 程序化使用

|  |
| --- |
| **模块参数**: `RawScoreOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

### **Raw score data type Maximum** — 用于范围检查的最大未变换分数 `[]`（默认）| scalar

指定 Simulink 检查的未变换分数范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Raw score data type Maximum** 参数不会饱和或裁剪实际的未变换分数信号。

#### 程序化使用

|  |
| --- |
| **模块参数**: `RawScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

### **Output layer data type** — 最终全连接层的数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出层的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定输出数据类型。该内部规则选择一种数据类型，以优化数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OutputLayerDataTypeStr` |
| **类型**: character vector |
| **值**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认**: `'Inherit: Inherit via internal rule'` |

### **Output layer data type Minimum** — 最终全连接层的最小值 `[]`（默认）| scalar

指定 Simulink 检查的输出层内部变量范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output layer data type Minimum** 参数不会饱和或裁剪输出层值信号。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OutputLayerOutMin` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

### **Output layer data type Maximum** — 最终全连接层的最大值 `[]`（默认）| scalar

指定 Simulink 检查的输出层内部变量范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output layer data type Maximum** 参数不会饱和或裁剪输出层值信号。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OutputLayerOutMax` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

### **Layer 1 data type** — 第一个全连接层的数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定第一层的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定数据类型。该内部规则选择一种数据类型，以优化数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 提示

训练后的神经网络可以有多个全连接层，不包括输出层。

- 您可以分别为前 10 层中的每一层指定数据类型。为每一层指定数据类型 **Layer n data type**。第一层的数据类型为 **Layer 1 data type**，第二层的数据类型为 **Layer 2 data type**，依此类推。
- 您可以使用数据类型 **Additional layer(s) data type** 为第 11 层到第 *k* 层（其中 *k* 是总层数）指定数据类型。**Additional layer(s) data type** 的 **模块参数** 是 `Layer11DataTypeStr`。
- 数据类型 **Layer n data type** 和 **Additional layer(s) data type** 可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。这些数据类型支持与 **Layer 1 data type** 相同的值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Layer1DataTypeStr` |
| **类型**: character vector |
| **值**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认**: `'Inherit: Inherit via internal rule'` |

### **Layer 1 data type Minimum** — 第一个全连接层的最小值 `[]`（默认）| scalar

指定 Simulink 检查的第一层内部变量范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Layer 1 data type Minimum** 参数不会饱和或裁剪第一层值信号。

#### 提示

训练后的神经网络可以有多个全连接层，不包括输出层。

- 您可以分别为前 10 层中的每一层指定 Simulink 检查的内部变量范围的下限值。为每一层指定下限值 **Layer n minimum**。第一层的最小值为 **Layer 1 minimum**，第二层的最小值为 **Layer 2 minimum**，依此类推。
- 您可以使用 **Additional layer(s) minimum** 为第 11 层到第 *k* 层（其中 *k* 是总层数）指定下限值。**Additional layer(s) minimum** 的 **模块参数** 是 `Layer11OutMin`。
- **Layer n minimum** 和 **Additional layer(s) minimum** 支持与 **Layer 1 minimum** 相同的值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Layer1OutMin` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

### **Layer 1 data type Maximum** — 第一个全连接层的最大值 `[]`（默认）| scalar

指定 Simulink 检查的第一层内部变量范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（请参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Layer 1 data type Maximum** 参数不会饱和或裁剪第一层值信号。

#### 提示

训练后的神经网络可以有多个全连接层，不包括输出层。

- 您可以分别为前 10 层中的每一层指定 Simulink 检查的内部变量范围的上限值。为每一层指定上限值 **Layer n maximum**。第一层的最大值为 **Layer 1 maximum**，第二层的最大值为 **Layer 2 maximum**，依此类推。
- 您可以使用 **Additional layer(s) maximum** 为第 11 层到第 *k* 层（其中 *k* 是总层数）指定上限值。**Additional layer(s) maximum** 的 **模块参数** 是 `Layer11OutMax`。
- **Layer n maximum** 和 **Additional layer(s) maximum** 支持与 **Layer 1 maximum** 相同的值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Layer1OutMax` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

## 所属库

Statistics and Machine Learning Toolbox / Classification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2021b 中引入**

## 描述

使用神经网络分类模型对观测进行分类

ClassificationNeuralNetwork Predict 模块使用神经网络分类对象（`ClassificationNeuralNetwork` 或 `CompactClassificationNeuralNetwork`）对观测进行分类，用于多类分类。

通过指定包含训练后分类对象的工作区变量名称，将训练后的分类对象导入模块。输入端口 **x** 接收一个观测（预测变量数据），输出端口 **label** 返回该观测的预测类标签。您可以添加可选输出端口 **score**，它返回预测类分数或后验概率。
