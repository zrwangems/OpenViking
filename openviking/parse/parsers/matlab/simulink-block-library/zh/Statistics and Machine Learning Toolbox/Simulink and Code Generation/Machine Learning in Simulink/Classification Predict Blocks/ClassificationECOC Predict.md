---
type: simulink-block
title: 'ClassificationECOC Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Support Vector Machine Classification'
documentation_page: 'classificationecocpredict'
documentation_source_path: 'classificationecocpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationECOC Predict

## 端口

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量必须与训练 **选择训练好的机器学习模型** 所指定模型的预测变量具有相同的顺序。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **label** — 预测的类标签 标量

预测的类标签，以标量形式返回。**label** 是得分最高的类。有关更多详细信息，请参阅 `predict` 对象函数的 `label` 参数。

该模块支持两种解码方案，这些方案指定模块如何聚合二值损失以计算分类分数，以及模块如何确定每个观测的预测类。有关详细信息，请参阅 **解码方案** 和 二值损失和解码方案。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测的类分数或后验概率 行向量

预测的类分数（取负的平均二值损失）或后验概率，以大小为 1×*K* 的行向量形式返回，其中 *K* 是 ECOC 模型中的类数。

要检查类的顺序，请使用 **选择训练好的机器学习模型** 所指定模型的 `ClassNames` 属性。

#### 依赖关系

- 要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为预测的类分数添加输出端口** 复选框。
- 该模块支持两种解码方案，这些方案指定模块如何聚合二值损失以计算分类分数，以及模块如何确定每个观测的预测类。有关详细信息，请参阅 **解码方案** 和 二值损失和解码方案。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **pbscore** — 二值学习器的正类分数 行向量

二值学习器的正类分数，以大小为 1×*B* 的行向量形式返回，其中 *B* 是 ECOC 模型中的二值学习器数量。

要检查二值学习器的类分配代码，请使用 **选择训练好的机器学习模型** 所指定模型的 `CodingMatrix` 属性。有关更多详细信息，请参阅 `ClassificationECOC` 对象的编码设计。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为二值学习器的正类分数添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **选择训练好的机器学习模型** — ECOC 分类模型 `ecocMdl`（默认）| `ClassificationECOC` 对象 | `CompactClassificationECOC` 对象

指定包含 `ClassificationECOC` 或 `CompactClassificationECOC` 模型对象的工作区变量的名称。

使用 `fitcecoc` 训练模型时，以下限制适用：

- 必须使用 SVM 学习器或线性学习器训练 ECOC 模型。

  - 对于 SVM 学习器，可以将 `Learners` 名称-值参数指定为 `"svm"`、使用 `templateSVM` 创建的 SVM 模板对象，或 SVM 模板对象元胞数组。
  - 对于线性学习器，可以将 `Learners` 名称-值参数指定为 `"linear"`、使用 `templateLinear` 创建的线性模板对象，或线性模板对象元胞数组。模板对象的 `Lambda` 值（正则化项强度）必须是数值标量。
- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须是数值类型（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationECOC` 对象 | `CompactClassificationECOC` 对象 |
| **默认值：** `'ecocMdl'` |

### **为预测的类分数（取负的平均二值损失）添加输出端口** — 添加第二个输出端口 `off`（默认）| `on`

选中该复选框可在 ClassificationECOC Predict 模块中包含第二个输出端口 **score**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **为二值学习器的正类分数添加输出端口** — 添加第三个输出端口 `off`（默认）| `on`

选中该复选框可在 ClassificationECOC Predict 模块中包含第三个输出端口 **pbscore**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputPBScore` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **二值学习器损失函数** — 二值学习器损失函数 `hinge`（默认）| `binodeviance` | `exponential` | `hamming` | `linear` | `logit` | `quadratic`

将二值学习器损失函数指定为 `binodeviance`、`exponential`、`hamming`、`hinge`、`linear`、`logit` 或 `quadratic`。

推荐的二值损失函数取决于二值学习器返回的分数范围。下表列出了一些常见情况：

| 描述 | 推荐函数 |
| --- | --- |
| 所有二值学习器均为逻辑回归学习器的线性分类模型。 | `quadratic` |
| 所有二值学习器均为 SVM 或 SVM 学习器的线性分类模型。 | `hinge` |
| 训练 ECOC 模型时，通过设置 `FitPosterior=true` 指定预测类后验概率。 | `quadratic` |

有关损失函数的定义，请参阅二值损失和解码方案。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BinaryLoss` |
| **类型：** 字符向量 |
| **值：** `'binodeviance'` | `'exponential'` | `'hamming'` | `'hinge'` | `'linear'` | `'logit'` | `'quadratic'` |
| **默认值：** `'hinge'` |

### **解码方案** — 解码方案 `lossweighted`（默认）| `lossbased`

指定将二值损失聚合为 `lossweighted` 或 `lossbased` 的解码方案。

**score** 值的定义取决于 **解码方案** 值。

- 如果指定 `lossweighted`，则 **score** 中的第 *k* 个元素是第 *k* 个类的二值损失之和除以该类的二值学习器数量。
- 如果指定 `lossbased`，则 **score** 中的第 *k* 个元素是二值损失之和除以二值学习器总数。

有关更多详细信息，请参阅二值损失和解码方案。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Decoding` |
| **类型：** 字符向量 |
| **值：** `'lossweighted'` | `'lossbased'` |
| **默认值：** `'lossweighted'` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作方法 `off`（默认）| `on`

指定溢出时饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 模型可能发生溢出，并且您希望在生成的代码中显式提供饱和保护。 | 溢出饱和到数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理越界信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **标签数据类型** — 标签输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以是继承的、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **选择训练好的机器学习模型** 所指定模型中使用的标签。

- 如果模型使用数值或逻辑标签，则支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、fixed point 以及数据类型对象。
- 如果模型使用非数值标签，则支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **标签数据类型**（请参阅 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **选择训练好的机器学习模型** 指定的工作区变量名为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，相应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签） | `"Inherit: auto"`（对于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**标签数据类型最小值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择训练好的机器学习模型** 所指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **标签数据类型最大值** — 用于范围检查的标签输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**标签数据类型最大值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择训练好的机器学习模型** 所指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Score 数据类型** — score 输出的数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化用法

|  |
| --- |
| **模块参数**: `ScoreDataTypeStr` |
| **类型**: 字符向量或字符串 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **Score 数据类型最小值** — 用于范围检查的 score 输出最小值 `[]` (默认) | 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score 数据类型最小值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 程序化用法

|  |
| --- |
| **模块参数**: `ScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **Score 数据类型最大值** — 用于范围检查的 score 输出最大值 `[]` (默认) | 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score 数据类型最大值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 程序化用法

|  |
| --- |
| **模块参数**: `ScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **正类得分数据类型** — 正类得分数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **pbscore** 输出的数据类型。此数据类型还确定二分类学习器分类得分的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化用法

|  |
| --- |
| **模块参数**: `PBScoreDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **正类得分数据类型最小值** — 用于范围检查的 `pbscore` 输出最小值 `[]` (默认) | 标量

指定 Simulink 检查的 **pbscore** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**正类得分数据类型最小值** 参数不会饱和或裁剪实际的 **pbscore** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 程序化用法

|  |
| --- |
| **模块参数**: `PBScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **正类得分数据类型最大值** — 用于范围检查的 `pbscore` 输出最大值 `[]` (默认) | 标量

指定 Simulink 检查的 **pbscore** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**正类得分数据类型最大值** 参数不会饱和或裁剪实际的 **pbscore** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 程序化用法

|  |
| --- |
| **模块参数**: `PBScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **核数据类型** — 二分类学习器核计算数据类型 `double` (默认) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于二分类学习器核计算的参数的数据类型。该类型可以直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当 **选择训练好的机器学习模型** 指定的模型使用 SVM 学习器时，才能指定此参数。如果模型使用线性学习器，则改为指定 **内积数据类型**。

**核数据类型** 参数根据指定的 SVM 学习器的核函数类型，指定不同参数的数据类型。您使用 `templateSVM` 函数的 `KernelFunction` 名称-值参数来指定核函数类型。必须将 `templateSVM` 的输出作为 `fitcecoc` 函数的 `Learners` 名称-值参数的值传递。

| `KernelFunction` 值 | 数据类型 |
| --- | --- |
| `'gaussian'` 或 `'rbf'` | 该参数指定高斯核 G(x,s)=exp(−D2) 的平方距离 D2=‖x−s‖2 的数据类型，其中 *x* 是观测的预测变量数据，*s* 是支持向量。 |
| `'linear'` | 该参数指定线性核函数 G(x,s)=xs' 的输出的数据类型，其中 *x* 是观测的预测变量数据，*s* 是支持向量。 |
| `'polynomial'` | 该参数指定多项式核函数 G(x,s)=(1+xs')p 的输出的数据类型，其中 *x* 是观测的预测变量数据，*s* 是支持向量，*p* 是多项式核函数阶数。 |

#### 程序化用法

|  |
| --- |
| **模块参数**: `KernelDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认**: `'double'` |

### **核数据类型最小值** — 用于范围检查的核计算最小值 `[]` (默认) | 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**核数据类型最小值** 参数不会饱和或裁剪实际的核计算值信号。

#### 程序化用法

|  |
| --- |
| **模块参数**: `KernelOutMin` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **核数据类型最大值** — 用于范围检查的核计算最大值 `[]` (默认) | 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**核数据类型最大值** 参数不会饱和或裁剪实际的核计算值信号。

#### 程序化用法

|  |
| --- |
| **模块参数**: `KernelOutMax` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **内积数据类型** — 二分类学习器的内积数据类型 `Inherit: Inherit via internal rule` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二分类学习器分类得分的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定输出数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当 **选择训练好的机器学习模型** 指定的模型使用线性学习器时，才能指定此参数。如果模型使用 SVM 学习器，则改为指定 **核数据类型**。

对于线性分类学习器，将观测 *x* 分类为正类的分类得分定义为

*f*(*x*) = *x**β*+*b*。

*β* 是估计的系数列向量，*b* 是估计的标量偏置。ECOC 模型对象中的每个线性分类学习器分别在 `Beta` 和 `Bias` 属性中包含系数和偏置。

如果模型由逻辑回归学习器组成，则软件对二分类学习器的分类得分应用 `'logit'` 得分变换。将 *x* 分类为负类的分类得分为 –*f*(*x*)。软件将观测分类到对每个二分类学习器产生正得分的类。

使用 **内积数据类型** 确定 *x**β* 的数据类型，并使用 **正类得分数据类型** 确定二分类学习器分类得分的数据类型。

#### 程序化用法

|  |
| --- |
| **模块参数**: `InnerProductDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认**: `'Inherit: Inherit via internal rule'` |

### **内积数据类型最小值** — 用于范围检查的内积项最小值 `[]` (默认) | 标量

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可移除算法代码并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最小值** 参数不会饱和或裁剪实际的内积值。

#### 程序化用法

|  |
| --- |
| **模块参数**: `InnerProductOutMin` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **Inner product data type Maximum** — 用于范围检查的内积项最大值 `[]`（默认）| scalar

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用该最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Maximum** 参数不会对实际内积值进行饱和或裁剪。

#### 编程使用

|  |
| --- |
| **模块参数**: `InnerProductOutMax` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认值**: `'[]'` |

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

**在 R2023a 中引入**

## 描述

使用纠错输出码 (ECOC) 分类模型对观测进行分类

ClassificationECOC Predict 模块使用纠错输出码 (ECOC) 分类模型（`ClassificationECOC` 或 `CompactClassificationECOC`）对观测进行分类，用于多类分类。

通过指定包含已训练分类对象的工作区变量名称，将训练好的分类对象导入模块。输入端口 **x** 接收观测（预测变量数据），输出端口 **label** 返回该观测的预测类标签。您可以添加可选输出端口 **score** 和 **pbscore**，其中 **score** 返回预测类分数（取负的平均二值损失），**pbscore** 返回二值学习器的正类分数。
