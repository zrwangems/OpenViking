---
type: simulink-block
title: 'IncrementalClassificationECOC Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Support Vector Machine Classification'
documentation_page: 'incrementalclassificationecocpredict'
documentation_source_path: 'incrementalclassificationecocpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationECOC Predict

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型（`incrementalClassificationECOC`），指定为总线信号（请参阅 `Composite Signals` (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。变量和观测的方向由 **预测变量数据观测维度** 指定。默认方向为 `rows`，表示预测变量数据中的观测沿 **x** 的行方向排列。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **label** — 预测类标签块 列向量

预测类标签块，以列向量形式返回。标签 `label(i)` 表示使观测 **x**(`i`) 获得最高分数的类。有关更多详细信息，请参阅 `predict` 对象函数的 `Label` 参数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测的类分数或后验概率矩阵

预测的类分数（取负的平均二元损失）或后验概率，以矩阵形式返回。要检查类的顺序，请使用 **选择初始机器学习模型** 所指定模型的 `ClassNames` 属性。

#### 依赖关系

- 要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为预测的类分数添加输出端口** 对应的复选框。
- 该模块支持两种解码方案，这些方案指定模块如何聚合二元损失以计算分类分数，以及模块如何为每个观测确定预测类。有关详细信息，请参阅 **解码方案** 和二元损失和解码方案。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **pbscore** — 二元学习器的正类分数矩阵

二元学习器的正类分数，以矩阵形式返回。要检查二元学习器的类分配代码，请使用 **选择训练后的机器学习模型** 所指定模型的 `CodingMatrix` 属性。有关更多详细信息，请参阅 `ClassificationECOC` 对象的编码设计。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为二元学习器的正类分数添加输出端口** 对应的复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **选择初始机器学习模型** — 初始增量分类 ECOC 模型 `ecocMdl`（默认） | `incrementalClassificationECOC` 模型对象

指定包含已配置的 `incrementalClassificationECOC` 模型对象的工作区变量名称。初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中预测变量的数量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 工作区变量 |
| **值：** `incrementalClassificationECOC` 模型对象 |
| **默认：** `"ecocMdl"` |

### **为预测的类分数添加输出端口** — 添加第二个输出端口 `off`（默认） | `on`

选中该复选框可在 incrementalClassificationECOC Predict 模块中包含输出端口 **score**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **为二元学习器的正类分数添加输出端口** — 添加第三个输出端口 `off`（默认） | `on`

选中该复选框可在 incrementalClassificationECOC Predict 模块中包含第三个输出端口 **pbscore**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowOutputPBScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **二元学习器损失函数** — 二元学习器损失函数 `hinge`（默认） | `binodeviance` | `exponential` | `hamming` | `linear` | `logit` | `quadratic`

将二元学习器损失函数指定为 `binodeviance`、`exponential`、`hamming`、`hinge`、`linear`、`logit` 或 `quadratic`。

推荐的二元损失函数取决于二元学习器返回的分数范围。下表列出了一些常见情况：

| 描述 | 推荐函数 |
| --- | --- |
| 所有二元学习器都是逻辑回归学习器的线性分类模型。 | `quadratic` |
| 所有二元学习器都是 SVM 或 SVM 学习器的线性分类模型。 | `hinge` |
| 通过训练 ECOC 模型时设置 `FitPosterior=true` 来指定预测类后验概率。 | `quadratic` |

有关损失函数的定义，请参阅二元损失和解码方案。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BinaryLoss` |
| **类型：** 字符向量 |
| **值：** `"binodeviance"` | `"exponential"` | `"hamming"` | `"hinge"` | `"linear"` | `"logit"` | `"quadratic"` |
| **默认：** `"hinge"` |

### **解码方案** — 解码方案 `lossweighted`（默认） | `lossbased`

指定将二元损失聚合为 `lossweighted` 或 `lossbased` 的解码方案。

**score** 值的定义取决于 **解码方案** 的值。

- 如果指定 `lossweighted`，则 **score** 中的第 *k* 个元素是二元损失之和除以第 *k* 类的二元学习器数量。
- 如果指定 `lossbased`，则 **score** 中的第 *k* 个元素是二元损失之和除以二元学习器总数。

有关更多详细信息，请参阅二元损失和解码方案。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Decoding` |
| **类型：** 字符向量 |
| **值：** `"lossweighted"` | `"lossbased"` |
| **默认：** `"lossweighted"` |

### **预测变量数据观测维度** — 预测变量数据的观测维度 `rows`（默认） | `columns`

指定预测变量数据的观测维度。默认值为 `rows`，表示预测变量数据中的观测沿 **x** 的行方向排列。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ObservationsIn` |
| **类型：** 字符向量 |
| **值：** `"rows" | "columns"` |
| **默认：** `"rows"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，IncrementalClassificationECOC Predict 模块根据该模块在模型中的上下文继承采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出时是饱和还是绕回。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中显式提供饱和保护。 | 溢出会饱和到该数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅排查信号范围错误 (Simulink)。 | 溢出会绕回到该数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

#### 数据类型

### **标签数据类型** — **label** 输出的数据类型 `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **选择初始机器学习模型** 所指定模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、fixed point 以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **标签数据类型**（请参阅数据类型传播 (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **选择初始机器学习模型** 指定的工作区变量名为 `myMdl`，类别标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类别标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: Inherit via back propagation"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认**：`"Inherit: Inherit via back propagation"` |

### **标签数据类型最小值** — 用于范围检查的 **label** 输出最小值 `[]`（默认） | 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**标签数据类型最小值** 参数不会饱和或裁剪实际的 **label** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择初始机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **标签数据类型最大值** — 用于范围检查的 **label** 输出最大值 `[]`（默认） | 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**标签数据类型最大值** 参数不会饱和或裁剪实际的 **label** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择初始机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **分数数据类型** — score 输出的数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreDataTypeStr` |
| **类型**: 字符向量或字符串 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **分数数据类型最小值** — 用于范围检查的 score 输出最小值 `[]` (默认) | 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**分数数据类型最小值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **分数数据类型最大值** — 用于范围检查的 score 输出最大值 `[]` (默认) | 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**分数数据类型最大值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **正类分数数据类型** — 正类分数数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **pbscore** 输出的数据类型。此数据类型还确定二分类学习器的分类分数的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `PBScoreDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **正类分数数据类型最小值** — 用于范围检查的 `pbscore` 输出最小值 `[]` (默认) | 标量

指定 Simulink 检查的 **pbscore** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**正类分数数据类型最小值** 参数不会饱和或裁剪实际的 **pbscore** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PBScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **正类分数数据类型最大值** — 用于范围检查的 `pbscore` 输出最大值 `[]` (默认) | 标量

指定 Simulink 检查的 **pbscore** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**正类分数数据类型最大值** 参数不会饱和或裁剪实际的 **pbscore** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PBScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认**: `'[]'` |

### **二分类学习器分数数据类型** — 二分类学习器分数数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 `IncrementalClassificationECOC Predict` 模块内部二分类学习器分数的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryScoreDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: auto"` |

### **二分类学习器分数数据类型最小值** — 用于范围检查的二分类学习器分数最小值 `[]` (默认) | 标量

指定 Simulink 检查的二分类学习器分数输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **二分类学习器分数数据类型最大值** — 用于范围检查的二分类学习器分数最大值 `[]` (默认) | 标量

指定 Simulink 检查的二分类学习器分数输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **二分类学习器核数据类型** — 二分类学习器核计算数据类型 `double` (默认) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二分类学习器核计算的参数数据类型。该类型可以直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用 SVM 学习器时，才能指定此参数。如果模型使用线性学习器，则改为指定 **内积数据类型**。

IncrementalClassificationECOC Predict 模块仅支持线性核。**二分类学习器核数据类型** 参数指定线性核函数 G(x,s)=xs' 的输出的数据类型，其中 *x* 是观测的预测子数据，*s* 是支持向量。您通过 `templateSVM` 函数的 `KernelFunction` 名称-值参数指定核函数类型。必须将 `templateSVM` 的输出作为 `fitcecoc` 的 `Learners` 名称-值参数的值传递。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryKernelDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"uint64"` | `"int64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"double"` |

### **二分类学习器核数据类型最小值** — 用于范围检查的核计算最小值 `[]` (默认) | 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二分类学习器核数据类型最小值** 参数不会饱和或裁剪实际的核计算值信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryKernelOutMin` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

### **二分类学习器核数据类型最大值** — 用于范围检查的核计算最大值 `[]` (默认) | 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二分类学习器核数据类型最大值** 参数不会饱和或裁剪实际的核计算值信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `BinaryKernelOutMax` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认**: `"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / ECOC

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

**在 R2024a 中引入**

## 描述

使用增量 ECOC 分类模型对观测进行分类

IncrementalClassificationECOC Predict 模块使用训练好的纠错输出码 (ECOC) 分类模型对观测进行分类，该模型作为 IncrementalClassificationECOC Fit 模块的输出返回。

通过指定包含对象的工作区变量名称，将初始 ECOC 分类模型对象导入模块。输入端口 **mdl** 接收表示拟合到流数据的增量学习模型的总线信号。输入端口 **x** 接收预测子数据（观测）的块，输出端口 **label** 返回该块的预测类标签。您可以添加可选输出端口 **score** 和 **pbscore**，其中 **score** 返回预测类分数（取反的平均二分类损失），**pbscore** 返回二分类学习器的正类分数。
