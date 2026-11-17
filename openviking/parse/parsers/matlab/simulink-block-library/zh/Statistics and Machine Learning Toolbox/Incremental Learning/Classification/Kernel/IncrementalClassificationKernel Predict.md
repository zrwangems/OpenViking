---
type: simulink-block
title: 'IncrementalClassificationKernel Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Classification / Kernel'
documentation_page: 'incrementalclassificationkernelpredict'
documentation_source_path: 'incrementalclassificationkernelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationKernel Predict

## 端口
```yaml
ports:
- name: mdl
  summary: 增量学习模型总线信号
  direction: input
- name: x
  summary: 预测变量数据块 数值矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: label
  summary: 预测类标签块 列向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: score
  summary: 预测类分数或后验概率 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: CanPredict
  summary: 模型状态 0（false）| 1（true）
  direction: output
```

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型（`incrementalClassificationKernel`），指定为总线信号（参见 Composite Signals (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。

**注意**

该模块仅支持数值输入预测变量数据。如果您的输入数据包含分类数据，您必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，将所有虚拟变量矩阵和任何其他数值预测变量连接起来。有关更多详细信息，请参见 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签块 列向量

预测类标签块，以列向量形式返回。标签 `label(i)` 表示对观测值 **x**(`i`) 产生最高分数的类。有关更多详细信息，请参见 `predict` 对象函数的 `label` 输出参数。

如果在创建 **mdl** 时指定了估计期，则预测类标签为估计期内的多数类。该类占 **x** 中训练标签的最大比例。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率 矩阵

预测类分数或后验概率，以矩阵形式返回。如果模型使用逻辑学习器训练，则分类分数为后验概率。分类分数 `score(i)` 表示 **x** 中的观测值属于类 `i` 的后验概率。有关更多详细信息，请参见 Classification Score。

要检查类的顺序，请使用由 **Select initial machine learning model** 指定的核分类模型的 `ClassNames` 属性。

**注意**

如果在创建 **mdl** 时指定了估计期，则估计期内的预测类分数为零。

#### 依赖关系

要启用此端口，请在 Block Parameters 对话框的 **Main** 选项卡上选中 **Add output port for predicted class scores** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **CanPredict** — 模型状态 `0`（`false`）| `1`（`true`）

用于预测的模型状态，以数值或逻辑值 `0`（`false`）或 `1`（`true`）返回。

**注意**

如果在创建 **mdl** 时指定了估计期，则估计期内的模型状态为 `0`（`false`）。

#### 依赖关系

要启用此端口，请在 Block Parameters 对话框的 **Main** 选项卡上选中 **Add output port for status of trained machine learning model** 复选框。
## 参数
```yaml
parameters:
- name: Select initial machine learning model
  summary: 初始增量核分类模型 kernelMdl（默认）| incrementalClassificationKernel 模型对象
  group: 主要参数
  block_parameter: InitialLearner
  type: character vector or string
  values: incrementalClassificationKernel object name
  default: '"kernelMdl"'
- name: Add output port for predicted class scores
  summary: 添加第二个输出端口用于预测类别分数 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputScore
  type: character vector or string
  values: '"off" | "on"'
  default: '"off"'
- name: Add output port for status of trained machine learning model
  summary: 添加第三个输出端口用于模型状态 off（默认）| on
  group: 主要参数
  block_parameter: ShowOutputCanPredict
  type: character vector or string
  values: '"off" | "on"'
  default: '"off"'
- name: Sample time (–1 for inherited)
  summary: 用于指定采样时间的选项 –1（默认）| 标量
  group: 主要参数
  block_parameter: SystemSampleTime
  type: string scalar or character vector
  values: scalar
  default: '"–1"'
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
  summary: '标签输出的数据类型 Inherit: Inherit via back propagation | double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class name> | <data type expression>'
  group: 数据类型
  block_parameter: LabelDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via back propagation" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16"
    | "int32" | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "Enum: <class name>" |
    "<data type expression>"'
  default: '"Inherit: Inherit via back propagation" (for numeric and logical labels) | "Inherit: auto" (for nonnumeric labels)'
- name: Label data type Minimum
  summary: 用于范围检查的标签输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: LabelOutMin
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Label data type Maximum
  summary: 用于范围检查的 label 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: LabelOutMax
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Score data type
  summary: 'score 输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: ScoreDataTypeStr
  type: 字符向量或字符串
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Score data type Minimum
  summary: 用于范围检查的 score 输出最小值 []（默认）| 标量
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
- name: Kernel data type
  summary: '核计算数据类型 Inherit: Inherit via internal rule（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32
    | int64 | uint64 | uint32 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: KernelDataTypeStr
  type: 字符向量
  values: '''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''uint64''
    | ''int64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Kernel data type Minimum
  summary: 用于范围检查的核计算最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMin
  type: 字符向量
  values: '''[]'' | 标量'
  default: '''[]'''
- name: Kernel data type Maximum
  summary: 用于范围检查的核计算最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Inner product data type
  summary: '预测响应的内积项 Inherit: Inherit via internal rule（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: InnerProductDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via internal rule" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: Inherit via internal rule"'
- name: Inner product data type Minimum
  summary: 用于范围检查的内积项最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: 内积数据类型最大值
  summary: 用于范围检查的内积项最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMax
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要参数

### **Select initial machine learning model** — 初始增量核分类模型 `kernelMdl`（默认）| `incrementalClassificationKernel` 模型对象

指定包含已配置的 `incrementalClassificationKernel` 模型对象的工作区变量名称。

创建初始模型对象时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `ScoreTransform` 属性不能为 `"invlogit"` 或匿名函数。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialLearner` |
| **类型**：character vector or string |
| **值**：`incrementalClassificationKernel` object name |
| **默认值**：`"kernelMdl"` |

### **Add output port for predicted class scores** — 添加第二个输出端口用于预测类别分数 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationKernel Predict 模块中包含输出端口 **score**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputScore` |
| **类型**：character vector or string |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Add output port for status of trained machine learning model** — 添加第三个输出端口用于模型状态 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationKernel Predict 模块中包含输出端口 **CanPredict**。如果在创建 IncrementalClassificationKernel Predict 模块时，工作区中已包含名为 `kernelMdl` 且能够进行预测的增量核分类模型，则此复选框不会显示。或者，您可以通过在 Simulink 工作区中选择 IncrementalClassificationKernel Predict 模块，并在 MATLAB® 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")` 来指定包含输出端口 **CanPredict**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputCanPredict` |
| **类型**：character vector or string |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalClassificationKernel Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SystemSampleTime` |
| **类型**：string scalar or character vector |
| **值**：scalar |
| **默认值**：`"–1"` |

### 数据类型

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB 舍入函数在掩码字段中输入表达式。

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
| 选中此复选框（`on`）。 | 你的模型可能发生溢出，并且你希望在生成的代码中提供显式的饱和保护。 | 溢出饱和到该数据类型所能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 你希望优化生成代码的效率。你希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到该数据类型所能表示的相应值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖你为模块指定的数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **Label data type** — 标签输出的数据类型 `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

支持的数据类型取决于 **Select initial machine learning model** 所指定模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **Label data type**（请参阅 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **Select initial machine learning model** 指定的工作区变量名为 `myMdl`，类别标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类别标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: Inherit via back propagation"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via back propagation"` (for numeric and logical labels) | `"Inherit: auto"` (for nonnumeric labels) |

### **Label data type Minimum** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Label data type Minimum** 参数不会饱和或裁剪实际的 **label** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select initial machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Label data type Maximum** — 用于范围检查的 label 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Label data type Maximum** 参数不会饱和或裁剪实际的 **label** 输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **Select initial machine learning model** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score data type** — score 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的 score 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Minimum** 参数不会饱和或裁剪实际的 **score** 输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score data type Maximum** — 用于范围检查的 score 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

#### Additional Data Types

### **Kernel data type** — 核计算数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于高斯核近似计算的参数数据类型。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定核数据类型。该内部规则会选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小。该软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Kernel data type Minimum** — 用于范围检查的核计算最小值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Note**

**Kernel data type Minimum** 参数不会饱和或裁剪实际的核计算值。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Kernel data type Maximum** — 用于范围检查的核计算最大值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Kernel data type Maximum** 参数不会饱和或裁剪实际的核计算值。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Inner product data type** — 预测响应的内积项 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定内积数据类型。该内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成的代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InnerProductDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via internal rule"` |

### **Inner product data type Minimum** — 用于范围检查的内积项最小值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Minimum** 参数不会饱和或裁剪实际的内积项值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InnerProductOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **内积数据类型最大值** — 用于范围检查的内积项最大值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最大值**参数不会饱和或裁剪实际的内积项值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InnerProductOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |
## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / Kernel

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

**在 R2024b 中引入**

## 描述

使用增量核分类模型对观测值进行分类

IncrementalClassificationKernel Predict 模块使用由 IncrementalClassificationKernel Fit 模块输出返回的训练好的核分类模型对观测值进行分类。

通过指定包含该对象的工作区变量名称，将初始核分类模型对象导入 IncrementalClassificationKernel Predict 模块。输入端口 **mdl** 接收表示拟合到流式数据的增量学习模型的 bus 信号。输入端口 **x** 接收一块预测变量数据（观测值），输出端口 **label** 返回该块的预测类别标签。可选的输出端口 **score** 返回预测类别分数或后验概率，可选的输出端口 **CanPredict** 返回训练模型的预测状态。
