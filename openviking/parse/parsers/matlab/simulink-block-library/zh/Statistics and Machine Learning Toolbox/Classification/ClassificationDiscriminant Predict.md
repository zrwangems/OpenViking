---
type: simulink-block
title: 'ClassificationDiscriminant Predict'
family: 'classification'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationdiscriminantpredict'
documentation_source_path: 'classificationdiscriminantpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationDiscriminant Predict

## 端口

### 输入

### **x** — 预测变量数据行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量顺序必须与训练由 **Select trained machine learning model** 指定的模型所用的预测变量相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签标量

预测类标签，以标量形式返回。预测类是最小化预期分类成本的类。有关详细信息，请参阅 `predict` 对象函数的“更多关于”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率行向量

预测类分数或后验概率，以大小为 1×*k* 的行向量返回，其中 *k* 是判别分析模型中的类数。分类分数 `Score(i)` 表示 **x** 中的观测属于类 `i` 的后验概率。

要检查类的顺序，请使用由 **Select trained machine learning model** 指定的判别分析模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **Main** 选项卡上选中 **Add output port for predicted class scores** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **cost** — 预期分类成本行向量

预期分类成本，以大小为 1×*k* 的行向量返回，其中 *k* 是判别分析模型中的类数。分类成本 `Cost(i)` 表示将 **x** 中的观测分类到类 `i` 的成本。

要检查类的顺序，请使用由 **Select trained machine learning model** 指定的判别分析模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **Main** 选项卡上选中 **Add output port for expected classification cost** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### Main

### **Select trained machine learning model** — 判别分析分类模型 `daMdl`（默认）| `ClassificationDiscriminant` 对象

指定包含 `ClassificationDiscriminant` 对象的工作区变量名称。

使用 `fitcdiscr` 训练模型时，以下限制适用：

- 预测变量数据不能包括分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果以表形式提供训练数据，则预测变量必须为数值（`double` 或 `single`）。要在模型中包括分类预测变量，请在拟合模型前使用 `dummyvar` 对其进行预处理。
- `ScoreTransform` 名称-值参数的值不能为 `"invlogit"` 或匿名函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationDiscriminant` 对象 |
| **默认值：** `"daMdl"` |

### **Add output port for predicted class scores** — 添加预测类分数的可选输出端口 `off`（默认）| `on`

选中此复选框以在 ClassificationDiscriminant Predict 模块中包括输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Add output port for expected classification cost** — 添加预期分类成本的可选输出端口 `off`（默认）| `on`

选中此复选框以在 ClassificationDiscriminant Predict 模块中包括输出端口 **cost**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputCost` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数将表达式输入到掩码字段中。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是绕回。

| 操作 | 原因 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能溢出，并且您希望生成的代码中具有显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出绕回到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Label data type** — **label** 输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **Select trained machine learning model** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点，以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>`，以及数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **Label data type**（请参阅 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **Select trained machine learning model** 指定的工作区变量名为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签） | `"Inherit: auto"`（对于非数值标签） |

### **Label data type Minimum** — 用于范围检查的 **label** 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Label data type Minimum** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Label data type Maximum** — 用于范围检查的 **label** 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Label data type Maximum** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Score data type** — **score** 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的 **score** 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Minimum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **score 数据类型最大值** — score 输出用于范围检查的最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**score 数据类型最大值** 参数不会饱和或裁剪实际的 **score** 输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **原始 score 数据类型** — 未变换的 score 数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换 score 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 控制信号的数据类型 (Simulink)。

点击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

仅当 **选择训练好的机器学习模型** 指定的模型使用 `"none"`（默认，与 `"identity"` 相同）以外的 score 变换时，才能指定此参数。

- 如果模型不使用 score 变换（`"none"` 或 `"identity"`），则可以使用 **score 数据类型** 指定 score 数据类型。
- 如果模型使用 `"none"` 或 `"identity"` 以外的 score 变换，则可以使用此参数指定未变换的原始 score 的数据类型。要指定变换后的 score 的数据类型，请使用 **score 数据类型**。

您可以在训练期间指定 `ScoreTransform` 名称-值参量，或在训练后修改 `ScoreTransform` 属性，以更改 score 变换选项。

#### 编程用法

|  |
| --- |
| **模块参数**：`RawScoreDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **原始 score 数据类型最小值** — 用于范围检查的未变换 score 的最小值 `[]`（默认）| 标量

指定 Simulink 检查的未变换 score 范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**原始 score 数据类型最小值** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`RawScoreOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **原始 score 数据类型最大值** — 用于范围检查的未变换 score 的最大值 `[]`（默认）| 标量

指定 Simulink 检查的未变换 score 范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**原始 score 数据类型最大值** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`RawScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **估计 cost 数据类型** — cost 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **cost** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 控制信号的数据类型 (Simulink)。

点击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`CostDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **估计 cost 数据类型最小值** — 用于范围检查的 cost 输出的最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**估计 cost 数据类型最小值** 参数不会饱和或裁剪实际的 **cost** 信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`CostOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **估计 cost 数据类型最大值** — 用于范围检查的 cost 输出的最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**估计 cost 数据类型最大值** 参数不会饱和或裁剪实际的 **cost** 信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`CostOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

#### 附加数据类型

### **马氏距离数据类型** — 距离度量的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定马氏距离度量的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

点击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

有关数据类型的详细信息，请参阅 控制信号的数据类型 (Simulink)。

**注意**

**马氏距离数据类型** 参数指定模块内部使用的距离度量的数据类型。有关详细信息，请参阅 `mahal`。

#### 编程用法

|  |
| --- |
| **模块参数**：`DistanceDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **马氏距离数据类型最小值** — 用于范围检查的距离的最小值 `[]`（默认）| 标量

指定 Simulink 检查的距离范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**马氏距离数据类型最小值** 参数不会饱和或裁剪实际的距离信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`DistanceOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **马氏距离数据类型最大值** — 用于范围检查的距离的最大值 `[]`（默认）| 标量

指定 Simulink 检查的距离范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（参阅 指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**马氏距离数据类型最大值** 参数不会饱和或裁剪实际的距离信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`DistanceOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

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

**在 R2024a 中引入**

## 描述

使用判别分析模型对观测值进行分类

ClassificationDiscriminant Predict 模块使用判别分析分类对象（`ClassificationDiscriminant`）对观测值进行多类分类。

通过指定包含该对象的工作区变量的名称，将训练好的分类对象导入模块。输入端口 **x** 接收观测值（预测变量数据），输出端口 **label** 返回该观测值的预测类标签。可选输出端口 **score** 返回预测的类分数或后验概率。可选输出端口 **cost** 返回预期分类成本。
