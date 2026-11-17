---
type: simulink-block
title: 'Update Metrics'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning'
documentation_page: 'updatemetrics'
documentation_source_path: 'updatemetrics.html'
language: zh-CN
chinese_source: worker-translation
---

# Update Metrics

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型，指定为总线信号（参见 `Composite Signals` (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。变量和观测值的方向由 **Predictor data observation dimension** 指定。默认方向为 `rows`，表示预测变量数据中的观测值沿 **x** 的行方向排列。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中第 *j* 个观测值（行或列）的响应。

**注意**

该模块仅支持数值型输入预测变量数据。如果输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为哑变量的数值矩阵。然后，将所有哑变量矩阵和任何其他数值预测变量拼接起来。有关更多详细信息，请参阅 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — 响应（标签）块 数值向量 | 逻辑向量 | 枚举向量

用于衡量模型性能的响应（标签）块，指定为数值、逻辑或枚举向量。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中第 *j* 个观测值（行或列）的响应。

对于分类问题：

- 每个标签必须对应数组的一行。
- 如果 **y** 包含 `mdl.ClassNames` 中的标签，该模块将报错。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — 观测权重块 正数值向量

观测权重块，指定为正数值向量。Update Metrics 模块使用 **w** 中的对应值对 **x** 中的观测值进行加权。**w** 的大小必须等于 **x** 中的观测值数量。

#### 依赖关系

要启用此端口，请在 Block Parameters 对话框的 **Main** 选项卡中选中 **Add input port for observation weights** 复选框。

**数据类型：** `single` | `double`

### **reset** — 重置信号 `0` (`false`) | `1` (`true`) | 数值标量

*自 R2025a 起*

重置信号，指定为 `0` (`false`) 或 `1` (`true`) 或数值标量。当 **reset** 信号为正标量（大于 0）时，该模块重置增量学习模型的学习参数（如果有）。如果在增量训练期间估计了 **mdl** 的任何超参数，这些超参数也会被重置。`mdl.NumPredictors` 始终保留。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **IsWarm** — 指示模型是否跟踪性能指标的标志 逻辑值

指示增量模型是否跟踪性能指标的标志，返回为逻辑值 `0` (`false`) 或 `1` (`true`)。

| 值 | 描述 |
| --- | --- |
| `1 (true)` | 增量模型 `mdl` 已预热。因此，该模块在总线信号输出中跟踪性能指标。 |
| `0 (false)` | 该模块不跟踪性能指标。 |

### **metrics** — 模型性能指标矩阵

在增量学习期间更新的模型性能指标，以包含两列和 *m* 行的矩阵形式返回，其中 *m* 是 **x** 中的观测值数量。使用 **Model performance metrics to track** 指定性能指标。该模块忽略 **mdl** 的 `Metrics` 属性所指定的指标。

**metrics** 的列为：

- **`Cumulative`** — 从模型变为热启动（`IsWarm` 为 `1`）时开始的模型性能。
- **`Window`** — 在 **mdl** 的 `MetricsWindowSize` 属性所指定的窗口内对所有观测值评估的模型性能。软件在处理 `MetricsWindowSize` 个观测值后更新 `Window`。

**数据类型：** `matrix`

## 参数

### 主

### **Select initial machine learning model** — 初始增量学习模型 `Mdl`（默认）| `incrementalRegressionLinear` 模型对象 | `incrementalClassificationLinear` 模型对象 | `incrementalClassificationECOC` 模型对象

指定包含已配置的 `incrementalRegressionLinear`、`incrementalClassificationLinear` 或 `incrementalClassificationECOC` 模型对象的工作区变量名称。

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果以表格形式提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数量。
- 初始模型的 `ScoreTransform` 属性（仅分类）不能为 `"invlogit"` 或匿名函数。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 工作区变量 |
| **值：** `incrementalRegressionLinear` 模型对象、`incrementalClassificationLinear` 模型对象、`incrementalClassificationECOC` 模型对象 |
| **默认值：** `"Mdl"` |

### **Model performance metrics to track** — 性能指标函数 `classiferror`（默认）| `binodeviance` | `exponential` | `hinge` | `logit` | `quadratic` | `mse` | `epsiloninsensitive`

在增量学习期间要跟踪的累积和窗口性能指标的损失函数。有关损失函数的更多详细信息，请参阅 `loss`。

下表列出了内置损失函数名称：

- 对于回归模型：

  | 名称 | 描述 |
  | --- | --- |
  | `"mse"` | 加权均方误差 |
  | `"epsiloninsensitive"` | Epsilon 不敏感误差 |

  回归模型的默认值为 `"epsiloninsensitive"`。
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

Update Metrics 模块忽略 **mdl** 的 `Metric` 属性所指定的指标。

#### 编程使用

|  |
| --- |
| **模块参数：** `Metric` |
| **类型：** 字符向量 |
| **值：** `"classiferror" | "binodeviance" | "exponential" | "hinge" | "logit" | "quadratic" | "mse" | "epsiloninsensitive"` |
| **默认值：** `"classiferror"`（对于分类模型）| `"epsiloninsensitive"`（对于回归模型） |

### **Add input port for observation weights** — 添加用于观测权重的第二个输入端口 `off`（默认）| `on`

选中该复选框以在 Update Metrics 模块中包含用于观测权重的输入端口 **w**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowInputWeights` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Add input port for resetting trained learner** — 添加用于重置已训练学习器的输入端口 `off`（默认）| `on`

*自 R2025a 起*

选中该复选框可在 Update Metrics 模块中包含用于重置信号的输入端口 **reset**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowInputReset` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Predictor data observation dimension** — 预测器数据的观测维度 `rows`（默认）| `columns`

指定预测器数据的观测维度。默认值为 `rows`，表示预测器数据中的观测沿 **x** 的行方向排列。

#### 编程使用

|  |
| --- |
| **模块参数：** `ObservationsIn` |
| **类型：** 字符向量 |
| **值：** `"rows" | "columns"` |
| **默认值：** `"rows"` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，Update Metrics 模块根据模块在模型中的上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中具有显式的饱和保护。 | 溢出饱和到数据类型所能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型所能表示的相应值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **Metrics data type** — 指标输出的数据类型 `double`（默认）| `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定指标输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`MetricsDataTypeStr` |
| **类型**：character vector |
| **值**：`"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"double"` |

### **Metrics data type Minimum** — 用于范围检查的指标最小值 `[]`（默认）| 标量

指定 Simulink® 检查的指标输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Metrics data type Minimum** 参数不会饱和或裁剪实际的指标输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`MetricsOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Metrics data type Maximum** — 用于范围检查的指标最大值 `[]`（默认）| 标量

指定 Simulink 检查的指标输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Metrics data type Maximum** 参数不会饱和或裁剪实际的指标输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`MetricsOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Predict response data type** — 预测响应的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 Update Metrics 模块内部预测模块（IncrementalRegressionLinear Predict、IncrementalClassificationLinear Predict、IncrementalClassificationECOC Predict 等）响应输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它有助于您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Predict response data type Minimum** — 用于范围检查的预测响应最小值 `[]`（默认）| 标量

指定 Simulink 检查的内部预测响应输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Predict response data type Minimum** 参数不会饱和或裁剪实际的预测响应输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseOutMin` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Predict response data type Maximum** — 用于范围检查的预测响应最大值 `[]`（默认）| 标量

指定 Simulink 检查的内部预测响应输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Predict response data type Maximum** 参数不会饱和或裁剪实际的预测响应输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PredictResponseOutMax` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Loss data type** — 损失输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定损失值输出的数据类型，该输出由 Update Metrics 模块内部使用，用于评估累积损失以及 **mdl** 的 `MetricsWindowSize` 属性所指定窗口内的损失。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它有助于您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LossDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Loss data type Minimum** — 用于范围检查的损失最小值 `[]`（默认）| 标量

指定 Simulink 检查的内部损失输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LossOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Loss data type Maximum** — 用于范围检查的损失最大值 `[]`（默认）| 标量

指定 Simulink 检查的内部损失输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LossOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Additional predict data type** — 附加预测数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 Update Metrics 模块内部预测模块（IncrementalRegressionLinear Predict、IncrementalClassificationLinear Predict 或 IncrementalClassificationECOC Predict）的附加响应输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定附加预测数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdditionalPredictDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via internal rule"` |

### **Additional predict data type Maximum** — 用于范围检查的附加预测最大值 `[]`（默认）| 标量

指定 Simulink 检查的附加预测输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Additional predict data type Maximum** 参数不会饱和或裁剪实际的附加预测。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdditionalPredictOutMax` |
| **类型**：string or numeric scalar |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Additional loss data type** — 附加损失数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 Update Metrics 模块内部用于计算累积损失以及由 **mdl** 的 `MetricsWindowSize` 属性指定的窗口内损失的附加运算的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定附加损失数据类型。该内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码大小。该软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdditionalLossDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via internal rule"` |

### **Additional loss data type Minimum** — 用于范围检查的附加损失最小值 `[]`（默认）| 标量

指定 Simulink 检查的附加损失输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdditionalLossOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **Additional loss data type Maximum** — 用于范围检查的附加损失最大值 `[]`（默认）| 标量

指定 Simulink 检查的附加损失输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`AdditionalLossOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning

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

**在 R2023b 中引入**

### R2025a：新增 reset 输入端口

Update Metrics 新增了一个 **reset** 输入端口，允许重置增量学习模型已学习的参数（如果有的话）。如果在增量训练期间估计了模型的任何超参数，这些超参数也会被重置。在执行漂移感知学习时，使用 **reset** 信号在检测到漂移时重置模型参数。

## 描述

在增量学习模型中根据新数据更新性能指标

Update Metrics 模块根据新数据，输出已配置的增量模型的性能指标，适用于二分类（`incrementalClassificationLinear`）、多分类（`incrementalClassificationECOC`）或线性回归（`incrementalRegressionLinear`）。

通过指定包含已训练增量学习模型对象的工作区变量名称，将该对象导入模块。输入端口 **mdl** 接收表示拟合流式数据的增量学习模型的 bus 信号。输入端口 **x** 接收一块预测变量数据（观测值），输入端口 **y** 接收一块用于衡量模型性能的响应或标签。输出端口 **IsWarm** 返回一个值，指示模型是否已预热，即模型是否在跟踪性能指标。输出端口 **metrics** 返回计算得到的性能指标。可选输入端口 **w** 接收一块观测权重，可选输入端口 **reset** 重置已学习的参数。
