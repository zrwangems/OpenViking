---
type: simulink-block
title: 'IncrementalClassificationNaiveBayes Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Incremental Learning'
documentation_page: 'incrementalclassificationnaivebayespredict'
documentation_source_path: 'incrementalclassificationnaivebayespredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationNaiveBayes Predict

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型（`incrementalClassificationNaiveBayes`），指定为总线信号（参见 `Composite Signals` (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。

该模块仅支持数值输入预测变量数据。如果输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，串联所有虚拟变量矩阵以及任何其他数值预测变量。有关更多详细信息，请参阅虚拟变量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签块 列向量

预测类标签块，以列向量形式返回。预测类是使预期分类成本最小的类。有关更多详细信息，请参阅 `predict` 对象函数的“更多信息”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率矩阵

预测类分数或后验概率，返回为 *n* 乘 `numel(mdl.ClassNames)` 矩阵，其中 *n* 是 **x** 中的观测值数。分类分数 `score(j,k)` 表示 **x** 中的观测值 *j* 属于类 *k* 的后验概率。

要检查类的顺序，请使用由 **选择初始训练机器学习模型** 指定的朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在模块参数对话框的 **主要** 选项卡上选中 **为预测类分数添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **cost** — 预期误分类成本矩阵

预期误分类成本，返回为 *n* 乘 `numel(mdl.ClassNames)` 矩阵，其中 *n* 是 **x** 中的观测值数。分类成本 `Cost(j,k)` 表示 **x** 的第 *j* 行中的观测值被分类到类 *k* 的成本。

要检查类的顺序，请使用由 **选择初始训练机器学习模型** 指定的朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在模块参数对话框的 **主要** 选项卡上选中 **为预期分类成本添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **CanPredict** — 模型状态 `0` (`false`) | `1`(`true`)

用于预测的模型状态，返回为数值或逻辑 `0` (`false`) 或 `1` (`true`)。

**注意**

如果指定的模型未训练，则 IncrementalClassificationNaiveBayes Predict 无法预测响应，模型状态为 `0` (`false`)。

#### 依赖关系

要启用此端口，请在模块参数对话框的 **主要** 选项卡上选中 **为已训练机器学习模型的状态添加输出端口** 复选框。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，从 **准备** 库中选择 **属性检查器**。

### 主要

### **选择初始机器学习模型** — 初始增量朴素贝叶斯分类模型 `nbMdl`（默认） | `incrementalClassificationNaiveBayes` 模型对象

指定包含已配置的 `incrementalClassificationNaiveBayes` 模型对象的工作区变量名称。

以下限制适用：

- 预测变量数据不能包括分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须为数值（`double` 或 `single`）。要在模型中包括分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `ScoreTransform` 属性不能为 `"invlogit"` 或匿名函数。
- `DistributionNames` 名称-值参数的值不能为 `"mn"` 或 `"mvmn"`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `incrementalClassificationNaiveBayes` 对象名称 |
| **默认值：** `"nbMdl"` |

### **为预测类分数添加输出端口** — 为预测类分数添加输出端口 `off`（默认） | `on`

选中此复选框可在 IncrementalClassificationNaiveBayes Predict 模块中包括用于预测类分数的输出端口 **score**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **为预期分类成本添加输出端口** — 为预期分类成本添加可选输出端口 `off`（默认） | `on`

选中此复选框可在 IncrementalClassificationNaiveBayes Predict 模块中包括输出端口 **cost**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputCost` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **为已训练机器学习模型的状态添加输出端口** — 为模型状态添加第二个输出端口 `off`（默认） | `on`

选中此复选框可在 IncrementalClassificationNaiveBayes Predict 模块中包括输出端口 **CanPredict**。如果在创建 IncrementalClassificationNaiveBayes Predict 模块时，工作区中已包含名为 `nbMdl` 且能够进行预测的增量朴素贝叶斯分类模型，则此复选框不会出现。或者，您可以在 Simulink 工作区中选择 IncrementalClassificationNaiveBayes Predict 模块，并在 MATLAB 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")`，以指定包括输出端口 **CanPredict**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **采样时间（–1 表示继承）** — 指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalClassificationNaiveBayes Predict 模块根据模型内该模块的上下文继承采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出是饱和还是回绕。

| 操作 | 原理 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成的代码的效率。您希望避免过度指定模块处理超出范围信号的方式。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **标签数据类型** — label 输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承，指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

支持的数据类型取决于由 **选择初始训练机器学习模型** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，则支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点，以及数据类型对象。
- 如果模型使用非数值标签，则支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **标签数据类型**（参见 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设由 **选择初始训练机器学习模型** 指定的工作区变量名称为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **显示数据类型助手** 按钮  以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签） | `"Inherit: auto"`（对于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的 label 输出最小值 `[]`（默认） | 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**标签数据类型最小值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择初始训练机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **标签数据类型最大值** — 用于范围检查的 label 输出最大值 `[]`（默认） | 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**标签数据类型最大值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择初始训练机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Score data type** — score 输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的 score 输出最小值 `[]`（默认） | scalar

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score data type Minimum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Score data type Maximum** — 用于范围检查的 score 输出最大值 `[]`（默认） | scalar

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Raw score data type** — 未变换 score 的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换 score 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 依赖关系

仅当由 **Select initial trained machine learning model** 指定的模型使用非 `"none"`（默认，与 `"identity"` 相同）的 score 变换时，才能指定此参数。

- 如果模型不使用 score 变换（`"none"` 或 `"identity"`），则可以使用 **Score data type** 指定 score 数据类型。
- 如果模型使用非 `"none"` 或 `"identity"` 的 score 变换，则可以使用此参数指定未变换原始 score 的数据类型。要指定变换后的 score 的数据类型，请使用 **Score data type**。

您可以在训练期间通过指定 `ScoreTransform` 名称-值参数，或在训练后通过修改 `ScoreTransform` 属性来更改 score 变换选项。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **Raw score data type Minimum** — 用于范围检查的未变换 score 最小值 `[]`（默认） | scalar

指定 Simulink 检查的未变换 score 范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Minimum** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Raw score data type Maximum** — 用于范围检查的未变换 score 最大值 `[]`（默认） | scalar

指定 Simulink 检查的未变换 score 范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Maximum** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Estimated cost data type** — cost 输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **cost** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **Estimated cost data type Minimum** — 用于范围检查的 cost 输出最小值 `[]`（默认） | scalar

指定 Simulink 检查的 **cost** 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Estimated cost data type Minimum** 参数不会饱和或裁剪实际的 **cost** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Estimated cost data type Maximum** — 用于范围检查的 cost 输出最大值 `[]`（默认） | scalar

指定 Simulink 检查的 **cost** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Estimated cost data type Maximum** 参数不会饱和或裁剪实际的 **cost** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

#### 附加数据类型

### **Likelihood data type** — likelihood 输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 likelihood 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **Likelihood data type Minimum** — 用于范围检查的 likelihood 输出最小值 `[]`（默认） | scalar

指定 Simulink 检查的 likelihood 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Likelihood data type Minimum** 参数不会饱和或裁剪实际 likelihood 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Likelihood data type Maximum** — 用于范围检查的 likelihood 输出最大值 `[]`（默认） | scalar

指定 Simulink 检查的 likelihood 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Likelihood data type Maximum** 参数不会饱和或裁剪实际 likelihood 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认**：`"[]"` |

### **Posterior data type** — 后验概率输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定后验概率的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PosteriorDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **Posterior data type Minimum** — 用于范围检查的后验概率输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的下限值。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

参数 **Posterior data type Minimum** 不会对实际后验概率进行饱和或限幅。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PosteriorOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Posterior data type Maximum** — 用于范围检查的后验概率输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的上限值。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

参数 **Posterior data type Maximum** 不会对实际后验概率进行饱和或限幅。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PosteriorOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / NaiveBayes

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

**在 R2025a 中引入**

## 描述

使用增量朴素贝叶斯分类模型对观测值进行分类

IncrementalClassificationNaiveBayes Predict 模块使用由 IncrementalClassificationNaiveBayes Fit 模块输出返回的训练后的朴素贝叶斯分类模型对观测值进行分类。

通过指定包含模型对象的工作区变量名称，将初始朴素贝叶斯分类模型对象导入该模块。输入端口 **mdl** 接收表示拟合到流式数据的增量学习模型的总线信号。输入端口 **x** 接收预测变量数据（观测值）的数据块，输出端口 **label** 返回该数据块的预测类标签。可选输出端口 **score** 返回预测类得分或后验概率。可选输出端口 **cost** 返回预期分类成本。可选输出端口 **CanPredict** 返回训练模型的预测状态。
