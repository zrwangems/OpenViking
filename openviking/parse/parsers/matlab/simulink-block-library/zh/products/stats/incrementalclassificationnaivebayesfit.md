---
type: simulink-block
title: 'IncrementalClassificationNaiveBayes Fit'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Incremental Learning'
documentation_page: 'incrementalclassificationnaivebayesfit'
documentation_source_path: 'incrementalclassificationnaivebayesfit.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationNaiveBayes Fit

## 端口

### 输入

### **x** — 预测变量数据块 数值矩阵

要拟合模型的预测变量数据块，指定为数值矩阵。假设变量和观测值的方向为 `rows`，这表示预测变量数据中的观测值沿 **x** 的行方向排列。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中观测值 *j*（行或列）的响应。以下限制适用：

- **x** 中的预测变量数量必须等于初始模型的 `NumPredictors` 属性值。如果流式数据中的预测变量数量不同于 `NumPredictors`，则模块会报错。
- IncrementalClassificationNaiveBayes Fit 模块仅支持数值输入预测变量数据。如果您的输入数据包含分类数据，则必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为由虚拟变量组成的数值矩阵。然后，将所有虚拟变量矩阵以及任何其他数值预测变量串联起来。有关更多详细信息，请参阅虚拟变量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — 类别标签块 数值向量 | 逻辑向量 | 枚举向量

要训练模型的类别标签块，指定为数值、逻辑或枚举向量。

- 观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**(`j`) 是 **x** 中观测值 *j*（行或列）的响应。
- 每个标签必须对应于数组的一行。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — 观测权重块 正数值向量

观测权重块，指定为正数值向量。IncrementalClassificationNaiveBayes Fit 模块使用 **w** 中的对应值对 **x** 中的观测值进行加权。**w** 的大小必须等于 **x** 中的观测值数量。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为观测权重添加输入端口** 复选框。

**数据类型：** `single` | `double`

### **reset** — 重置信号 `0` (`false`) | `1` (`true`) | 数值标量

*自 R2025a 起*

重置信号，指定为 `0` (`false`) 或 `1` (`true`) 或数值标量。当 **reset** 信号为正标量（大于 0）时，模块会重置增量学习模型已学习的参数（如果有）。如果在增量训练期间估计了 **mdl** 的任何超参数，则这些超参数也会被重置。`mdl.NumPredictors` 始终保留。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **mdl** — 更新后的增量学习模型参数 总线信号

拟合到流式数据的增量学习模型的更新参数，以总线信号形式返回（请参阅 `Composite Signals` (Simulink)）。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，从 **准备** 库中选择 **属性检查器**。

### 主要

### **选择初始机器学习模型** — 初始增量朴素贝叶斯分类模型 `nbMdl`（默认） | `incrementalClassificationNaiveBayes` 模型对象

指定包含已配置 `incrementalClassificationNaiveBayes` 模型对象的工作区变量名称。

初始模型必须指定以下属性：

- `NumPredictors` 属性，该属性必须是等于 **x** 中预测变量数量的正整数标量。
- `ClassNames` 属性。

以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须是数值（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `ScoreTransform` 属性不能为 `"invlogit"` 或匿名函数。
- `DistributionNames` 名称-值参数的值不能为 `"mn"` 或 `"mvmn"`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `incrementalClassificationNaiveBayes` 对象名称 |
| **默认值：** `"nbMdl"` |

### **为观测权重添加输入端口** — 为观测权重添加第二个输入端口 `off`（默认） | `on`

选中此复选框可在 IncrementalClassificationNaiveBayes Fit 模块中包含用于观测权重的输入端口 **w**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowInputWeights` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **添加用于重置已训练学习器的输入端口** — 添加用于重置已训练增量学习器的输入端口 `off`（默认） | `on`

*自 R2025a 起*

选中此复选框可在 IncrementalClassificationNaiveBayes Fit 模块中包含用于重置信号的输入端口 **reset**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowInputReset` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，IncrementalClassificationNaiveBayes Fit 模块根据模型内模块的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出时是饱和还是回绕。

| 操作 | 原因 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出会饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框后，模块输出在 127 处饱和。同样，模块输出在最小值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理越界信号。有关更多信息，请参阅排查信号范围错误 (Simulink)。 | 溢出会回绕到数据类型可以表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框后，软件会将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **内部状态数据类型** — 内部状态的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中内部状态的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `StatesDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **内部状态数据类型最小值** — 用于范围检查的内部状态最小值 `[]`（默认） | 标量

指定 Simulink 检查的内部状态范围的下限值。

Simulink 使用该最小值来执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**内部状态数据类型最小值** 参数不会饱和或裁剪实际的内部状态。要进行饱和或裁剪，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `StatesOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **内部状态数据类型最大值** — 用于范围检查的内部状态最大值 `[]`（默认） | 标量

指定 Simulink 检查的内部状态范围的上限值。

Simulink 使用该最大值来执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**内部状态数据类型最大值** 参数不会饱和或裁剪实际的内部状态。要进行饱和或裁剪，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `StatesOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **先验数据类型** — 先验项的数据类型 `double`（默认） | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部先验项的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `PriorDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"double"` |

### **先验数据类型最小值** — 用于范围检查的先验项最小值 `[]`（默认） | 标量

指定 Simulink 检查的先验项范围的下限值。

Simulink 使用该最小值来执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**先验数据类型最小值** 参数不会饱和或裁剪实际的先验项值。要进行饱和或裁剪，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `PriorOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **先验数据类型最大值** — 用于范围检查的先验项最大值 `[]`（默认） | 标量

指定 Simulink 检查的先验项范围的上限值。

Simulink 使用该最大值来执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**先验数据类型最大值** 参数不会饱和或裁剪实际的先验项值。要进行饱和或裁剪，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `PriorOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
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

拟合增量朴素贝叶斯分类模型

IncrementalClassificationNaiveBayes Fit 模块将配置的用于朴素贝叶斯分类的增量模型（`incrementalClassificationNaiveBayes`）拟合到流式数据。

通过指定包含该对象的工作区变量的名称，将初始朴素贝叶斯分类模型对象导入该模块。输入端口 **x** 接收一块预测变量数据（观测值），输入端口 **y** 接收一块模型要拟合到的响应（标签）。输出端口 **mdl** 返回更新后的 `incrementalClassificationNaiveBayes` 模型。可选输入端口 **w** 接收一块观测值权重，可选输入端口 **reset** 重置超参数。
