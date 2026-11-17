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
```yaml
ports:
- name: x
  summary: 预测变量数据 行向量 | 列向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: label
  summary: 预测类别标签 标量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: score
  summary: 预测类别分数或后验概率 行向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: cost
  summary: 预期分类代价 行向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量顺序必须与训练 **Select trained machine learning model** 所指定模型的预测变量顺序相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类别标签 标量

预测类别标签，以标量形式返回。预测类别是使预期分类代价最小的类别。有关更多详细信息，请参阅 `predict` 对象函数的“详细信息”部分。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类别分数或后验概率 行向量

预测类别分数或后验概率，以大小为 1×*k* 的行向量形式返回，其中 *k* 是朴素贝叶斯模型中的类别数。分类分数 `Score(i)` 表示 **x** 中的观测属于类别 `i` 的后验概率。

要检查类别的顺序，请使用 **Select trained machine learning model** 所指定朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **Main** 选项卡中选中 **Add output port for predicted class scores** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **cost** — 预期分类代价 行向量

预期分类代价，以大小为 1×*k* 的行向量形式返回，其中 *k* 是朴素贝叶斯模型中的类别数。分类代价 `Cost(i)` 表示将 **x** 中的观测分类到类别 `i` 的代价。

要检查类别的顺序，请使用 **Select trained machine learning model** 所指定朴素贝叶斯模型的 `ClassNames` 属性。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **Main** 选项卡中选中 **Add output port for expected classification cost** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Select trained machine learning model
  summary: 朴素贝叶斯分类模型 nbMdl（默认）| ClassificationNaiveBayes 对象
  group: 主要参数
  block_parameter: TrainedLearner
  type: 工作区变量
  values: ClassificationNaiveBayes 对象
- name: Add output port for predicted class scores
  summary: 添加预测类别分数的可选输出端口 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputScore
  type: 字符向量
  values: '"off" | "on"'
  default: '"off"'
- name: 添加预期分类代价的输出端口
  summary: 添加预期分类代价的可选输出端口 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputCost
  type: 字符向量
  values: '"off" | "on"'
  default: '"off"'
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: 字符向量
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
- name: 整数溢出时饱和
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  type: 字符向量
  values: '"off" | "on"'
  default: '"off"'
- name: 锁定输出数据类型设置以防止被定点工具更改
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: 字符向量
  values: '"off" | "on"'
  default: '"off"'
- name: Label data type
  summary: '标签输出数据类型 Inherit: Inherit via back propagation | Inherit: auto | double | single | half | int8 | uint8 | int16
    | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class name> | <data
    type expression>'
  group: 数据类型
  block_parameter: LabelDataTypeStr
  type: character vector or string
  values: '"Inherit: Inherit via back propagation" | "Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16"
    | "uint16" | "int32" | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "Enum: <class
    name>" | "<data type expression>"'
  default: '"Inherit: Inherit via back propagation" (for numeric and logical labels) | "Inherit: auto" (for nonnumeric labels)'
- name: Label data type Minimum
  summary: 用于范围检查的标签输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: LabelOutMin
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Label data type Maximum
  summary: 用于范围检查的标签输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: LabelOutMax
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Score data type
  summary: '分数输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: ScoreDataTypeStr
  type: 字符向量或字符串
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Score data type Minimum
  summary: 用于范围检查的分数输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: ScoreOutMin
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Score data type Maximum
  summary: 用于范围检查的 score 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: ScoreOutMax
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Raw score data type
  summary: '未变换的 score 数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: RawScoreDataTypeStr
  type: 字符向量
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Raw score data type Minimum
  summary: 用于范围检查的未变换分数最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: RawScoreOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Raw score data type Maximum
  summary: 用于范围检查的未变换分数最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: RawScoreOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Estimated cost data type
  summary: '代价输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: CostDataTypeStr
  type: character vector or string
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Estimated cost data type Minimum
  summary: 用于范围检查的 cost 输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: CostOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Estimated cost data type Maximum
  summary: 用于范围检查的 cost 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: CostOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Likelihood data type
  summary: '似然输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: LikelihoodDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Likelihood data type Minimum
  summary: 用于范围检查的 likelihood 输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: LikelihoodOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Likelihood data type Maximum
  summary: 用于范围检查的 likelihood 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: LikelihoodOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Posterior data type
  summary: '后验概率输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: PosteriorDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Posterior data type Minimum
  summary: 后验概率输出的最小值，用于范围检查 []（默认）| 标量
  group: 数据类型
  block_parameter: PosteriorOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Posterior data type Maximum
  summary: 后验概率输出的最大值，用于范围检查 []（默认）| 标量
  group: 数据类型
  block_parameter: PosteriorOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
```

### 主要参数

### **Select trained machine learning model** — 朴素贝叶斯分类模型 `nbMdl`（默认）| `ClassificationNaiveBayes` 对象

指定包含 `ClassificationNaiveBayes` 对象的工作区变量名称。

使用 `fitcnb` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，预测变量必须是数值类型（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- `ScoreTransform` 名称-值参数的值不能为 `"invlogit"` 或匿名函数。
- `DistributionNames` 名称-值参数的值不能为 `"mn"`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `ClassificationNaiveBayes` 对象 |
| **默认：** `"nbMdl"` |

### **Add output port for predicted class scores** — 添加预测类别分数的可选输出端口 `off`（默认）| `on`

选中此复选框可在 ClassificationNaiveBayes Predict 模块中包含输出端口 **score**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **添加预期分类代价的输出端口** — 添加预期分类代价的可选输出端口 `off`（默认）| `on`

选中此复选框可在 ClassificationNaiveBayes Predict 模块中包含输出端口 **cost**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowOutputCost` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中具有显式的饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误（Simulink）。 | 溢出回绕到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置（Fixed-Point Designer）。

#### 编程使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Label data type** — 标签输出数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

支持的数据类型取决于 **Select trained machine learning model** 所指定模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **Label data type**（参见 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **Select trained machine learning model** 指定的工作区变量名为 `myMdl`，类别标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类别标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via back propagation"` (for numeric and logical labels) | `"Inherit: auto"` (for nonnumeric labels) |

### **Label data type Minimum** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Label data type Minimum** 参数不会饱和或裁剪实际的 **label** 输出信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用数值标签时，您才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Label data type Maximum** — 用于范围检查的标签输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Label data type Maximum** 参数不会饱和或裁剪实际的 **label** 输出信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score data type** — 分数输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ScoreDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的分数输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Minimum** 参数不会饱和或裁剪实际的 **score** 输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ScoreOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score data type Maximum** — 用于范围检查的 score 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Raw score data type** — 未变换的 score 数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换 score 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用 `"none"`（默认，与 `"identity"` 相同）以外的 score 变换时，您才能指定此参数。

- 如果模型不使用 score 变换（`"none"` 或 `"identity"`），则可以使用 **Score data type** 指定 score 数据类型。
- 如果模型使用 `"none"` 或 `"identity"` 以外的 score 变换，则可以使用此参数指定未变换的原始 score 的数据类型。要指定变换后 score 的数据类型，请使用 **Score data type**。

您可以在训练期间指定 `ScoreTransform` 名称-值参数，或在训练后修改 `ScoreTransform` 属性来更改 score 变换选项。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Raw score data type Minimum** — 用于范围检查的未变换分数最小值 `[]`（默认）| 标量

指定 Simulink 检查的未变换分数范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Raw score data type Minimum** 参数不会饱和或裁剪实际的未变换分数信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Raw score data type Maximum** — 用于范围检查的未变换分数最大值 `[]`（默认）| 标量

指定 Simulink 检查的未变换分数范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Raw score data type Maximum** 参数不会饱和或裁剪实际的未变换分数信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`RawScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Estimated cost data type** — 代价输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **cost** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Estimated cost data type Minimum** — 用于范围检查的 cost 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Estimated cost data type Minimum** 参数不会饱和或裁剪实际的 **cost** 信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Estimated cost data type Maximum** — 用于范围检查的 cost 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **cost** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Estimated cost data type Maximum** 参数不会饱和或裁剪实际的 **cost** 信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`CostOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

#### Additional Data Types

### **Likelihood data type** — 似然输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定似然输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Likelihood data type Minimum** — 用于范围检查的 likelihood 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 likelihood 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Likelihood data type Minimum** 参数不会饱和或裁剪实际的 likelihood 值。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Likelihood data type Maximum** — 用于范围检查的 likelihood 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 likelihood 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Likelihood data type Maximum** 参数不会饱和或裁剪实际的 likelihood 值。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LikelihoodOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Posterior data type** — 后验概率输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定后验概率的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PosteriorDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Posterior data type Minimum** — 后验概率输出的最小值，用于范围检查 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Posterior data type Minimum** 参数不会饱和或裁剪实际的后验概率。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PosteriorOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Posterior data type Maximum** — 后验概率输出的最大值，用于范围检查 `[]`（默认）| 标量

指定 Simulink 检查的后验概率输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Posterior data type Maximum** 参数不会饱和或裁剪实际的后验概率。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PosteriorOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |
## 所属库

Statistics and Machine Learning Toolbox / Classification

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

如果在使用 `fitcnb` 创建 `nbMdl` 时指定 `DistributionNames="kernel"`，则仅部分支持定点计算。在这种情况下，软件会将数值转换为浮点数进行某些内部计算，然后再将其转换回定点。

## 版本历史

**在 R2023b 中引入**

## 描述

使用朴素贝叶斯模型对观测值进行分类

ClassificationNaiveBayes Predict 模块使用朴素贝叶斯分类对象（`ClassificationNaiveBayes`）对观测值进行多类分类。

通过指定包含已训练分类对象的工作区变量名称，将训练好的分类对象导入模块。输入端口 **x** 接收观测值（预测变量数据），输出端口 **label** 返回该观测值的预测类别标签。可选的输出端口 **score** 返回预测类别分数或后验概率。可选的输出端口 **cost** 返回预期的分类代价。
