---
type: simulink-block
title: 'ClassificationNaiveBayes Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationnaivebayespredict'
documentation_source_path: 'classificationnaivebayespredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationNaiveBayes Predict

## 端口

### 输入

### **x** — 预测变量数据行向量 | 列向量

预测变量数据，指定为一个观测值的行向量或列向量。

**x** 中的变量必须与由 **Select trained machine learning model** 指定的训练模型的预测变量顺序相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签标量

预测类标签，以标量形式返回。预测类是最小化预期分类代价的类。有关更多详细信息，请参阅 `predict` 对象函数的“更多信息”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率行向量

预测类分数或后验概率，以大小为 1×*k* 的行向量返回，其中 *k* 是朴素贝叶斯模型中的类数。分类分数 `Score(i)` 表示 **x** 中的观测值属于类 `i` 的后验概率。

要检查类的顺序，请使用由 **Select trained machine learning model** 指定的朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“块参数”对话框的 **Main** 选项卡上选中 **Add output port for predicted class scores** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **cost** — 预期分类代价行向量

预期分类代价，以大小为 1×*k* 的行向量返回，其中 *k* 是朴素贝叶斯模型中的类数。分类代价 `Cost(i)` 表示将 **x** 中的观测值分类到类 `i` 的代价。

要检查类的顺序，请使用由 **Select trained machine learning model** 指定的朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“块参数”对话框的 **Main** 选项卡上选中 **Add output port for expected classification cost** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### Main

### **Select trained machine learning model** — 朴素贝叶斯分类模型 `nbMdl`（默认）| `ClassificationNaiveBayes` 对象

指定包含 `ClassificationNaiveBayes` 对象的工作区变量名称。

当使用 `fitcnb` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果以表形式提供训练数据，预测变量必须为数值（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型前使用 `dummyvar` 对其进行预处理。
- `ScoreTransform` 名称-值参数的值不能为 `"invlogit"` 或匿名函数。
- `DistributionNames` 名称-值参数的值不能为 `"mn"`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationNaiveBayes` 对象 |
| **默认值：** `"nbMdl"` |

### **Add output port for predicted class scores** — 为预测类分数添加可选输出端口 `off`（默认）| `on`

选中此复选框以在 ClassificationNaiveBayes Predict 模块中包含输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Add output port for expected classification cost** — 为预期分类代价添加可选输出端口 `off`（默认）| `on`

选中此复选框以在 ClassificationNaiveBayes Predict 模块中包含输出端口 **cost**。

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

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是绕回。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中显式提供饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框后，模块输出饱和为 127。类似地，模块输出饱和为最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块处理超范围信号的方式。有关更多信息，请参阅排查信号范围错误 (Simulink)。 | 溢出绕回到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 阻止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Label data type** — label 输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以被继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于由 **Select trained machine learning model** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、fixed point，以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **Label data type**（请参阅数据类型传播 (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设由 **Select trained machine learning model** 指定的工作区变量名称为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签）| `"Inherit: auto"`（对于非数值标签） |

### **Label data type Minimum** — 用于范围检查的 label 输出的最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Label data type Minimum** 参数不会使实际 **label** 输出信号饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Label data type Maximum** — 用于范围检查的 label 输出的最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Label data type Maximum** 参数不会使实际 **label** 输出信号饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Score data type** — score 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以被继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的 score 输出的最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score data type Minimum** 参数不会使实际 **score** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Score data type Maximum** — 用于范围检查的 score 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Raw score data type** — 未变换的 score 数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换 score 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用非 `"none"`（默认，与 `"identity"` 相同）的 score 变换时，才能指定此参数。

- 如果模型不使用 score 变换（`"none"` 或 `"identity"`），则可以使用 **Score data type** 指定 score 数据类型。
- 如果模型使用非 `"none"` 或 `"identity"` 的 score 变换，则可以使用此参数指定未变换的原始 score 的数据类型。要指定变换后 score 的数据类型，请使用 **Score data type**。

您可以在训练期间指定 `ScoreTransform` 名称-值参数，或在训练后修改 `ScoreTransform` 属性，来更改 score 变换选项。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Raw score data type Minimum** — 用于范围检查的最小未变换 score `[]`（默认）| 标量

指定 Simulink 检查的未变换 score 范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Minimum** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Raw score data type Maximum** — 用于范围检查的最大未变换 score `[]`（默认）| 标量

指定 Simulink 检查的未变换 score 范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Raw score data type Maximum** 参数不会饱和或裁剪实际的未变换 score 信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Estimated cost data type** — cost 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **cost** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `CostDataTypeStr` |
| **类型**: character vector or string |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Estimated cost data type Minimum** — 用于范围检查的 cost 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Estimated cost data type Minimum** 参数不会饱和或裁剪实际的 **cost** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `CostOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Estimated cost data type Maximum** — 用于范围检查的 cost 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Estimated cost data type Maximum** 参数不会饱和或裁剪实际的 **cost** 信号。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `CostOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

#### 其他数据类型

### **Likelihood data type** — 似然输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定似然输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `LikelihoodDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Likelihood data type Minimum** — 用于范围检查的似然输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的似然输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Likelihood data type Minimum** 参数不会饱和或裁剪实际的似然值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `LikelihoodOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Likelihood data type Maximum** — 用于范围检查的似然输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的似然输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Likelihood data type Maximum** 参数不会饱和或裁剪实际的似然值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `LikelihoodOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Posterior data type** — 后验概率输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定后验概率的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `PosteriorDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Posterior data type Minimum** — 用于范围检查的后验概率输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Posterior data type Minimum** 参数不会饱和或裁剪实际的后验概率。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PosteriorOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **Posterior data type Maximum** — 用于范围检查的后验概率输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Posterior data type Maximum** 参数不会饱和或裁剪实际的后验概率。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PosteriorOutMax` |
| **类型**: character vector |
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

如果使用 `fitcnb` 创建 `nbMdl` 时指定 `DistributionNames="kernel"`，则仅部分支持定点计算。在这种情况下，软件会将数值转换为浮点值以进行某些内部计算，然后再将它们转换回定点值。

## 版本历史

**在 R2023b 中引入**

## 描述

使用朴素贝叶斯模型对观测值进行分类

ClassificationNaiveBayes Predict 模块使用朴素贝叶斯分类对象（`ClassificationNaiveBayes`）对观测值进行多类分类。

通过指定包含该对象的工作区变量的名称，将训练后的分类对象导入该模块。输入端口 **x** 接收一个观测值（预测变量数据），输出端口 **label** 返回该观测值的预测类标签。可选输出端口 **score** 返回预测类得分或后验概率。可选输出端口 **cost** 返回预期分类成本。
