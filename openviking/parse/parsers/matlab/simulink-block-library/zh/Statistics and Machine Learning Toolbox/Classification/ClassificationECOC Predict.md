---
type: simulink-block
title: 'ClassificationECOC Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationecocpredict'
documentation_source_path: 'classificationecocpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationECOC Predict

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
  summary: 预测类别得分或后验概率 行向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: pbscore
  summary: 二元学习器的正类得分 行向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量必须与训练 **Select trained machine learning model** 所指定模型的预测变量具有相同的顺序。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类别标签 标量

预测类别标签，以标量形式返回。**label** 是得分最高的类别。有关更多详细信息，请参阅 `predict` 对象函数的 `label` 参数。

该模块支持两种解码方案，用于指定模块如何聚合二元损失以计算分类得分，以及模块如何确定每个观测的预测类别。有关详细信息，请参阅 **Decoding scheme** 和 Binary Loss and Decoding Scheme。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类别得分或后验概率 行向量

预测类别得分（取负的平均二元损失）或后验概率，以大小为 1×*K* 的行向量形式返回，其中 *K* 是 ECOC 模型中的类别数。

要检查类别的顺序，请使用 **Select trained machine learning model** 所指定模型的 `ClassNames` 属性。

#### 依赖关系

- 要启用此端口，请在“模块参数”对话框的 **Main** 选项卡中选中 **Add output port for predicted class scores** 复选框。
- 该模块支持两种解码方案，用于指定模块如何聚合二元损失以计算分类得分，以及模块如何确定每个观测的预测类别。有关详细信息，请参阅 **Decoding scheme** 和 Binary Loss and Decoding Scheme。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **pbscore** — 二元学习器的正类得分 行向量

二元学习器的正类得分，以大小为 1×*B* 的行向量形式返回，其中 *B* 是 ECOC 模型中二元学习器的数量。

要检查二元学习器的类别分配代码，请使用 **Select trained machine learning model** 所指定模型的 `CodingMatrix` 属性。有关更多详细信息，请参阅 Coding Design of a `ClassificationECOC` object。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **Main** 选项卡中选中 **Add output port for positive-class scores of binary learners** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Select trained machine learning model
  summary: ECOC 分类模型 ecocMdl（默认）| ClassificationECOC 对象 | CompactClassificationECOC 对象
  group: 主要参数
  block_parameter: TrainedLearner
  type: workspace variable
  values: ClassificationECOC object | CompactClassificationECOC object
  default: '''ecocMdl'''
- name: Add output port for predicted class scores (negated average binary losses)
  summary: 添加第二个输出端口 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputScore
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Add output port for positive-class scores of binary learners
  summary: 添加第三个输出端口 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputPBScore
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Binary learner loss function
  summary: 二元学习器损失函数 hinge（默认）| binodeviance | exponential | hamming | linear | logit | quadratic
  group: 主要参数
  block_parameter: BinaryLoss
  type: character vector
  values: '''binodeviance'' | ''exponential'' | ''hamming'' | ''hinge'' | ''linear'' | ''logit'' | ''quadratic'''
  default: '''hinge'''
- name: Decoding scheme
  summary: 解码方案 lossweighted（默认）| lossbased
  group: 主要参数
  block_parameter: Decoding
  type: character vector
  values: '''lossweighted'' | ''lossbased'''
  default: '''lossweighted'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Label data type
  summary: '标签输出的数据类型 Inherit: Inherit via back propagation | Inherit: auto | double | single | half | int8 | uint8 | int16
    | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class name> | <data
    type expression>'
  group: 数据类型
  block_parameter: LabelDataTypeStr
  type: 字符向量或字符串
  values: '"Inherit: Inherit via back propagation" | "Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16"
    | "uint16" | "int32" | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "Enum: <class
    name>" | "<data type expression>"'
  default: '"Inherit: Inherit via back propagation"（用于数值和逻辑标签） | "Inherit: auto"（用于非数值标签）'
- name: Label data type Minimum
  summary: 用于范围检查的标签输出最小值 []（默认） | 标量
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
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Positive-class score data type
  summary: '正类分数数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 |
    uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: PBScoreDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Positive-class score data type Minimum
  summary: 用于范围检查的 pbscore 输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: PBScoreOutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Positive-class score data type Maximum
  summary: pbscore 输出的最大值，用于范围检查 []（默认）| 标量
  group: 数据类型
  block_parameter: PBScoreOutMax
  type: 字符向量
  values: '''[]'' | 标量'
  default: '''[]'''
- name: Kernel data type
  summary: 二分类学习器核计算数据类型 double（默认）| single | half | int8 | uint8 | int16 | uint16 | int32 | int64 | uint64 | uint32 | boolean
    | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>
  group: 数据类型
  block_parameter: KernelDataTypeStr
  type: 字符向量
  values: '''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''uint64''
    | ''int64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''double'''
- name: Kernel data type Minimum
  summary: 用于范围检查的最小核计算值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Kernel data type Maximum
  summary: 用于范围检查的最大核计算值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Inner product data type
  summary: '二分类学习器的内积数据类型 Inherit: Inherit via internal rule（默认）| double | single | half | int8 | uint8 | int16 | uint16 |
    int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: InnerProductDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16''
    | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''
    | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: 内积数据类型最小值
  summary: 用于范围检查的内积项最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMin
  type: 字符向量
  values: '''[]'' | 标量'
  default: '''[]'''
- name: 内积数据类型最大值
  summary: 用于范围检查的内积项最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMax
  type: 字符向量
  values: '''[]'' | 标量'
  default: '''[]'''
```

### 主要参数

### **Select trained machine learning model** — ECOC 分类模型 `ecocMdl`（默认）| `ClassificationECOC` 对象 | `CompactClassificationECOC` 对象

指定包含 `ClassificationECOC` 或 `CompactClassificationECOC` 模型对象的工作区变量名称。

当您使用 `fitcecoc` 训练模型时，以下限制适用：

- 您必须使用 SVM 学习器或线性学习器训练 ECOC 模型。

  - 对于 SVM 学习器，您可以将 `Learners` 名称-值参数指定为 `"svm"`、使用 `templateSVM` 创建的 SVM 模板对象，或 SVM 模板对象的元胞数组。
  - 对于线性学习器，您可以将 `Learners` 名称-值参数指定为 `"linear"`、使用 `templateLinear` 创建的线性模板对象，或线性模板对象的元胞数组。模板对象的 `Lambda` 值（正则化项强度）必须为数值标量。
- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果您在表中提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。此外，您不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。

#### 编程使用

|  |
| --- |
| **模块参数**：`TrainedLearner` |
| **类型**：workspace variable |
| **值**：`ClassificationECOC` object | `CompactClassificationECOC` object |
| **默认值**：`'ecocMdl'` |

### **Add output port for predicted class scores (negated average binary losses)** — 添加第二个输出端口 `off`（默认）| `on`

选中该复选框以在 ClassificationECOC Predict 模块中包含第二个输出端口 **score**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputScore` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Add output port for positive-class scores of binary learners** — 添加第三个输出端口 `off`（默认）| `on`

选中该复选框以在 ClassificationECOC Predict 模块中包含第三个输出端口 **pbscore**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputPBScore` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Binary learner loss function** — 二元学习器损失函数 `hinge`（默认）| `binodeviance` | `exponential` | `hamming` | `linear` | `logit` | `quadratic`

将二元学习器损失函数指定为 `binodeviance`、`exponential`、`hamming`、`hinge`、`linear`、`logit` 或 `quadratic`。

推荐的二元损失函数取决于二元学习器返回的分数范围。下表列出了一些常见情况：

| Description | Recommended Function |
| --- | --- |
| 所有二元学习器均为逻辑回归学习器的线性分类模型。 | `quadratic` |
| 所有二元学习器均为 SVM 或 SVM 学习器的线性分类模型。 | `hinge` |
| 您在训练 ECOC 模型时通过设置 `FitPosterior=true` 来指定预测类后验概率。 | `quadratic` |

有关损失函数的定义，请参阅 Binary Loss and Decoding Scheme。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryLoss` |
| **类型**：character vector |
| **值**：`'binodeviance'` | `'exponential'` | `'hamming'` | `'hinge'` | `'linear'` | `'logit'` | `'quadratic'` |
| **默认值**：`'hinge'` |

### **Decoding scheme** — 解码方案 `lossweighted`（默认）| `lossbased`

指定将二元损失聚合为 `lossweighted` 或 `lossbased` 的解码方案。

**score** 值的定义取决于 **Decoding scheme** 的值。

- 如果指定 `lossweighted`，则 **score** 中的第 *k* 个元素是二元损失之和除以第 *k* 类的二元学习器数量。
- 如果指定 `lossbased`，则 **score** 中的第 *k* 个元素是二元损失之和除以二元学习器总数。

有关更多详细信息，请参阅 Binary Loss and Decoding Scheme。

#### 编程使用

|  |
| --- |
| **模块参数**：`Decoding` |
| **类型**：character vector |
| **值**：`'lossweighted'` | `'lossbased'` |
| **默认值**：`'lossweighted'` |

### 数据类型

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值**：`"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中提供显式的饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可以表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **Label data type** — 标签输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **Select trained machine learning model** 所指定模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink® 在数据类型传播期间自动确定模块的 **Label data type**（请参阅 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **Select trained machine learning model** 指定的工作区变量名为 `myMdl`，类别标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类别标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via back propagation"`（用于数值和逻辑标签） | `"Inherit: auto"`（用于非数值标签） |

### **Label data type Minimum** — 用于范围检查的标签输出最小值 `[]`（默认） | 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Label data type Minimum** 参数不会饱和或裁剪实际的 **label** 输出信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用数值标签时，才能指定此参数。

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
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Positive-class score data type** — 正类分数数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **pbscore** 输出的数据类型。此数据类型还决定二分类学习器分类分数的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PBScoreDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Positive-class score data type Minimum** — 用于范围检查的 `pbscore` 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **pbscore** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Positive-class score data type Minimum** 参数不会饱和或裁剪实际的 **pbscore** 信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PBScoreOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Positive-class score data type Maximum** — `pbscore` 输出的最大值，用于范围检查 `[]`（默认）| 标量

指定 Simulink 检查的 **pbscore** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Positive-class score data type Maximum** 参数不会饱和或裁剪实际的 **pbscore** 信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PBScoreOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Kernel data type** — 二分类学习器核计算数据类型 `double`（默认）| `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于二分类学习器核计算的参数数据类型。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当 **Select trained machine learning model** 指定的模型使用 SVM 学习器时，才能指定此参数。如果模型使用线性学习器，则应改为指定 **Inner product data type**。

**Kernel data type** 参数根据指定 SVM 学习器的核函数类型，指定不同参数的数据类型。您可以使用 `templateSVM` 函数的 `KernelFunction` 名称-值参数指定核函数类型。必须将 `templateSVM` 的输出作为 `fitcecoc` 函数的 `Learners` 名称-值参数的值传入。

| `KernelFunction` 值 | 数据类型 |
| --- | --- |
| `'gaussian'` 或 `'rbf'` | 该参数指定高斯核 G(x,s)=exp(−D2) 的平方距离 D2=‖x−s‖2 的数据类型，其中 *x* 是某个观测的预测变量数据，*s* 是支持向量。 |
| `'linear'` | 该参数指定线性核函数 G(x,s)=xs' 的输出的数据类型，其中 *x* 是某个观测的预测变量数据，*s* 是支持向量。 |
| `'polynomial'` | 该参数指定多项式核函数 G(x,s)=(1+xs')p 的输出的数据类型，其中 *x* 是某个观测的预测变量数据，*s* 是支持向量，*p* 是多项式核函数阶数。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'double'` |

### **Kernel data type Minimum** — 用于范围检查的最小核计算值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Kernel data type Minimum** 参数不会饱和或裁剪实际的核计算值信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Kernel data type Maximum** — 用于范围检查的最大核计算值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Kernel data type Maximum** 参数不会饱和或裁剪实际的核计算值信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Inner product data type** — 二分类学习器的内积数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二分类学习器分类得分的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定输出数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当**选择训练好的机器学习模型**所指定的模型使用线性学习器时，才能指定此参数。如果模型使用 SVM 学习器，则应改为指定**核数据类型**。

对于线性分类学习器，将观测值 *x* 分类为正类的分类得分定义为

*f*(*x*) =
*x**β*+*b*。

*β* 是估计的系数列向量，*b* 是估计的标量偏置。ECOC 模型对象中的每个线性分类学习器分别在 `Beta` 和 `Bias` 属性中包含系数和偏置。

如果模型由逻辑回归学习器组成，则软件对二分类学习器的分类得分应用 `'logit'` 得分变换。将 *x* 分类为负类的分类得分为 –*f*(*x*)。软件将观测值分类为对每个二分类学习器产生正得分的类别。

使用**内积数据类型**确定 *x**β* 的数据类型，使用**正类得分数据类型**确定二分类学习器分类得分的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**：`InnerProductDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **内积数据类型最小值** — 用于范围检查的内积项最小值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最小值**参数不会饱和或裁剪实际的内积值。

#### 编程用法

|  |
| --- |
| **模块参数**：`InnerProductOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **内积数据类型最大值** — 用于范围检查的内积项最大值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最大值**参数不会饱和或裁剪实际的内积值。

#### 编程用法

|  |
| --- |
| **模块参数**：`InnerProductOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |
## 所属库

Statistics and Machine Learning Toolbox / Classification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023a 中引入**

## 描述

使用纠错输出编码 (ECOC) 分类模型对观测进行分类

ClassificationECOC Predict 模块使用纠错输出编码 (ECOC) 分类模型（`ClassificationECOC` 或 `CompactClassificationECOC`）对观测进行多类分类。

通过指定包含已训练分类对象的工作区变量名称，将训练好的分类对象导入模块。输入端口 **x** 接收一个观测（预测变量数据），输出端口 **label** 返回该观测的预测类别标签。您可以添加可选的输出端口 **score** 和 **pbscore**，其中 **score** 返回预测类别分数（取反的平均二分类损失），**pbscore** 返回二分类学习器的正类分数。
