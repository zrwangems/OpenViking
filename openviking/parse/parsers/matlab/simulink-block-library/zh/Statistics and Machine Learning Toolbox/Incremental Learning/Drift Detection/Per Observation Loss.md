---
type: simulink-block
title: 'Per Observation Loss'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Drift Detection'
documentation_page: 'perobservationloss'
documentation_source_path: 'perobservationloss.html'
language: zh-CN
chinese_source: worker-translation
---

# Per Observation Loss

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型，指定为总线信号（参见 `Composite Signals` (Simulink)）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。变量和观测值的方向由 **Predictor data observation dimension** 指定。默认方向为 `rows`，表示预测变量数据中的观测值沿 **x** 的行方向排列。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中第 *j* 个观测值（行或列）的响应。

该模块仅支持数值输入预测变量数据。如果输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为哑变量的数值矩阵。然后，将所有哑变量矩阵和任何其他数值预测变量拼接起来。有关更多详细信息，请参阅 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — 响应（标签）块 数值向量 | 逻辑向量 | 枚举向量

用于衡量模型性能的响应（标签）块，指定为数值、逻辑或枚举向量。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中第 *j* 个观测值（行或列）的响应。

对于分类问题：

- 每个标签必须对应数组的一行。
- 如果 **y** 包含不在 `mdl.ClassNames` 中的标签，模块将报错。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **IsWarm** — 指示模型是否跟踪性能指标的标志 逻辑值

指示增量模型是否跟踪性能指标的标志，返回为逻辑值 `0`（`false`）或 `1`（`true`）。

| 值 | 描述 |
| --- | --- |
| `1 (true)` | 增量模型 `mdl` 已预热。因此，模块在总线信号输出中跟踪性能指标。 |
| `0 (false)` | 模块不跟踪性能指标。 |

### **loss** — 逐观测误差 数值矩阵

使用 **x** 中的预测变量和 **y** 中的真实观测值计算的模型预测的逐观测回归或分类误差，返回为数值矩阵。该矩阵的大小为 *nchunk*×*nobs*，其中 *nchunk* 是块的总数，*nobs* 是 **x** 的一个块中的观测值数量。如果 **IsWarm** 为 `false`，则损失为 `-1`。

使用 **Loss function** 指定用于计算误差的损失函数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **选择初始机器学习模型** — 初始增量学习模型 `initMdl`（默认）

指定包含已配置模型对象的工作区变量名称。
可以使用以下对象：

- `incrementalRegressionLinear`
- `incrementalClassificationLinear`
- `incrementalClassificationECOC`
- `incrementalClassificationKernel`
- `incrementalRegressionKernel`
- `incrementalDriftAwareLearner`

如果提供了漂移感知模型对象，该模块将使用其中的增量学习模型。

以下约束适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数量。
- 初始模型的 `ScoreTransform` 属性（仅分类）不能为 `"invlogit"` 或匿名函数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** 工作区模型对象名称 |
| **默认：** `"initMdl"` |

### **损失函数** — 用于计算逐观测损失的损失函数 `classiferror`（默认） | `binodeviance` | `exponential` | `hinge` | `logit` | `quadratic` | `squarederror` | `epsiloninsensitive`

指定在增量学习期间用于计算逐观测损失的损失函数。有关损失函数的更多详细信息，请参阅 `loss`。

下表列出了内置损失函数名称：

- 对于回归模型：

  | 名称 | 描述 |
  | --- | --- |
  | `"squarederror"` | 平方误差 |
  | `"epsiloninsensitive"` | Epsilon 不敏感误差 |

  回归模型的默认值为 `"squarederror"`。
- 对于分类模型：

  | 名称 | 描述 |
  | --- | --- |
  | `"binodeviance"` | 二项偏差 |
  | `"classiferror"` | 误分类错误率 |
  | `"exponential"` | 指数 |
  | `"hinge"` | 铰链 |
  | `"logit"` | 逻辑 |
  | `"quadratic"` | 二次 |

  **注意**

  对于 `incrementalClassificationECOC` 模型，只能指定 `"classiferror"`。

逐观测损失模块忽略 **mdl** 的 `Metric` 属性指定的指标。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LossFun` |
| **类型：** 字符向量或字符串 |
| **值：** `"classiferror" | "binodeviance" | "exponential" | "hinge" | "logit" | "quadratic" | "squarederror" | "epsiloninsensitive"` |
| **默认：** 分类模型为 `"classiferror"`，回归模型为 `"squarederror"` |

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

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型（Simulink）。

默认情况下，逐观测损失模块根据模块在模型中的上下文继承采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认：** `"–1"` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中具有显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅信号范围错误疑难解答（Simulink）。 | 溢出回绕到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置（Fixed-Point Designer）。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

#### 数据类型

### **Loss data type** — 损失输出的数据类型 `double`（默认）| `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定损失输出的数据类型。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅控制信号的数据类型（Simulink）。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型（Simulink）。

#### 编程用法

|  |
| --- |
| **模块参数**： `LossDataTypeStr` |
| **类型**： 字符向量或字符串 |
| **值**： | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**： `"double"` |

### **Loss data type Minimum** — 用于范围检查的损失输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的损失输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Loss data type Minimum** 参数不会饱和或裁剪实际的损失输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LossOutMin` |
| **类型**：字符串或数值标量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Loss data type Maximum** — 用于范围检查的损失输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的损失输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Loss data type Maximum** 参数不会饱和或裁剪实际的损失输出。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LossOutMax` |
| **类型**：字符串或数值标量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Predict response data type** — 预测响应的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 Per Observation Loss 模块内部预测模块（IncrementalRegressionLinear Predict、IncrementalClassificationLinear Predict、IncrementalClassificationECOC Predict 等）的响应输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它有助于设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Predict response data type Minimum** — 用于范围检查的 predict response 最小值 `[]`（默认）| 标量

指定 Simulink 检查的内部 predict response 输出范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Predict response data type Minimum** 参数不会饱和或裁剪实际的 predict response 输出。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseOutMin` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Predict response data type Maximum** — 用于范围检查的 predict response 最大值 `[]`（默认）| 标量

指定 Simulink 检查的内部 predict response 输出范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Predict response data type Maximum** 参数不会饱和或裁剪实际的 predict response 输出。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseOutMax` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

#### Additional Data Types

### **Additional predict data type** — 附加 predict 数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 Per Observation Loss 模块内部的 predict 模块（IncrementalRegressionLinear Predict、IncrementalClassificationLinear Predict 或 IncrementalClassificationECOC Predict）附加 response 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定附加 predict 数据类型。内部规则会选择一种在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小的数据类型。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`AdditionalPredictDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via internal rule"` |

### **Additional predict data type Minimum** — 用于范围检查的附加预测最小值 `[]`（默认）| 标量

指定 Simulink 检查的附加预测输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Additional predict data type Minimum** 参数不会饱和或裁剪实际的附加预测。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`AdditionalPredictOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Additional predict data type Maximum** — 用于范围检查的附加预测最大值 `[]`（默认）| 标量

指定 Simulink 检查的附加预测输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Additional predict data type Maximum** 参数不会饱和或裁剪实际的附加预测。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`AdditionalPredictOutMax` |
| **类型**：字符串或数值标量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Linear sum data type** — 线性求和的数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部线性求和的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`LinearSumDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`Inherit: Inherit via internal rule` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`Inherit: Inherit via internal rule` |

### **Linear sum data type Minimum** — 用于范围检查的线性求和最小值 `[]`（默认）| 标量

指定 Simulink 检查的线性求和范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Linear sum data type Minimum** 参数不会饱和或裁剪实际的线性求和。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearSumOutMin` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Linear sum data type Maximum** — 用于范围检查的线性求和最大值 `[]`（默认）| 标量

指定 Simulink 检查的线性求和范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Linear sum data type Maximum** 参数不会饱和或裁剪实际的线性求和。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearSumOutMax` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Drift Detection

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

## 版本历史

**在 R2025a 中引入**

## 描述

增量模型的逐观测回归或分类误差

Per Observation Loss 模块在给定预测变量数据 **x** 和真实响应（标签）**y** 的情况下，输出已配置增量模型的逐观测回归或分类误差。

通过指定包含已训练增量学习或增量漂移感知模型对象的工作区变量名称，将该对象导入模块。输入端口 **mdl** 接收表示拟合到流数据的增量学习模型的 bus 信号。输入端口 **x** 接收一块预测变量数据（观测值），输入端口 **y** 接收一块用于测量模型损失的响应或标签。输出端口 **IsWarm** 返回一个值，指示模型是否已预热，即是否正在计算损失。输出端口 **loss** 返回计算得到的损失。
