---
type: simulink-block
title: 'ClassificationTree Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Classification Trees'
documentation_page: 'classificationtreepredict'
documentation_source_path: 'classificationtreepredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationTree Predict

## 端口

### 输入

### **x** — 预测变量数据行向量 | 列向量

预测变量数据，指定为一个观测值的行向量或列向量。

**x** 中的变量必须与训练由 **选择训练好的机器学习模型** 指定的模型所用的预测变量顺序相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测的类别标签标量

预测的类别标签，以标量形式返回。预测类别是使预期分类成本最小的类别。有关详细信息，请参阅 `predict` 函数参考页的“更多信息”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测的类别分数或后验概率行向量

预测的类别分数或后验概率，以大小为 1×*k* 的行向量形式返回，其中 *k* 是树模型中的类别数。

叶节点的分类分数是该节点处分类的后验概率。节点处分类的后验概率是导致该节点且具有该分类的训练观测数，除以导致该节点的训练观测数。

要检查类别的顺序，请使用由 **选择训练好的机器学习模型** 指定的树模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为预测的类别分数添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **选择训练好的机器学习模型** — 分类树模型 `treeMdl`（默认）| `ClassificationTree` 对象 | `CompactClassificationTree` 对象

指定包含 `ClassificationTree` 对象或 `CompactClassificationTree` 对象的工作区变量名称。

使用 `fitctree` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须是数值型（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型前使用 `dummyvar` 预处理它们。
- `ScoreTransform` 名称-值参数的值不能为 `'invlogit'` 或匿名函数。
- 不能使用代理分割；也就是说，`Surrogate` 名称-值参数的值必须为 `'off'`（默认）。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationTree` 对象 | `CompactClassificationTree` 对象 |
| **默认：** `'treeMdl'` |

### **为预测的类别分数添加输出端口** — 添加用于预测的类别分数的第二个输出端口 `off`（默认）| `on`

选中该复选框可在 ClassificationTree Predict 模块中包含第二个输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩膜字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作方法 `off`（默认）| `on`

指定溢出是饱和还是绕回。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 你的模型可能发生溢出，并且你希望在生成的代码中显式提供饱和保护。 | 溢出会饱和到数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出在 127 处饱和。同样，模块输出在最小输出值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 你希望优化生成代码的效率。你希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误 (Simulink)。 | 溢出会绕回到数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖你为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

#### 数据类型

### **标签数据类型** — 标签输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于由 **选择训练好的机器学习模型** 指定的模型中所使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

当你选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **标签数据类型**（请参阅数据类型传播 (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设由 **选择训练好的机器学习模型** 指定的工作区变量名为 `myMdl`，类别标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类别标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助你设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认**：`"Inherit: Inherit via back propagation"`（对于数值和逻辑标签）| `"Inherit: auto"`（对于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**标签数据类型最小值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择训练好的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **标签数据类型最大值** — 用于范围检查的标签输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**标签数据类型最大值** 参数不会饱和或裁剪实际的 **label** 输出信号。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择训练好的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **分数数据类型** — 分数输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助你设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**：`"Inherit: auto"` |

### **分数数据类型最小值** — 用于范围检查的分数输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**分数数据类型最小值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **分数数据类型最大值** — 用于范围检查的分数输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**分数数据类型最大值** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认**：`"[]"` |

### **Raw score data type** — 未变换的分数数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换分数的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（例如 `Simulink.NumericType`）。

当您选择 `Inherit: auto` 时，模块使用一条继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用 `"none"`（默认值，与 `"identity"` 相同）以外的分数变换时，才能指定此参数。

- 如果模型不使用分数变换（`"none"` 或 `"identity"`），则可以使用 **Score data type** 指定分数数据类型。
- 如果模型使用的分数变换不是 `"none"` 或 `"identity"`，则可以使用此参数指定未变换的原始分数的数据类型。要指定变换后分数的数据类型，请使用 **Score data type**。

您可以在训练期间指定 `ScoreTransform` 名称-值参量，或在训练后修改 `ScoreTransform` 属性，以更改分数变换选项。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreDataTypeStr` |
| **类型**: 字符向量 |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Raw score data type Minimum** — 用于范围检查的未变换分数最小值 `[]`（默认）| 标量

指定 Simulink 检查的未变换分数范围的下限值。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Minimum** 参数不会对实际的未变换分数信号进行饱和或限幅。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMin` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Raw score data type Maximum** — 用于范围检查的未变换分数最大值 `[]`（默认）| 标量

指定 Simulink 检查的未变换分数范围的上限值。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Maximum** 参数不会对实际的未变换分数信号进行饱和或限幅。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMax` |
| **类型**: 字符向量 |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

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

**在 R2021a 中引入**

## 描述

使用决策树分类器对观测值进行分类

ClassificationTree Predict 模块使用分类树对象（`ClassificationTree` 或 `CompactClassificationTree`）对观测值进行分类，以进行多类分类。

通过指定包含训练好的分类对象的工作区变量名称，将该对象导入模块中。输入端口 **x** 接收一个观测值（预测变量数据），输出端口 **label** 返回该观测值的预测类标签。您可以添加可选的输出端口 **score**，它返回预测的类分数或后验概率。
