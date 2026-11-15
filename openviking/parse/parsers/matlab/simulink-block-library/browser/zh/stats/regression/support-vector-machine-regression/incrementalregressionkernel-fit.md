---
type: simulink-block
title: 'IncrementalRegressionKernel Fit'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression / Support Vector Machine Regression'
documentation_page: 'incrementalregressionkernelfit'
documentation_source_path: 'incrementalregressionkernelfit.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalRegressionKernel Fit

## 端口

### 输入

### **x** — 预测变量数据块 数值矩阵

要拟合模型的预测变量数据块，指定为数值矩阵。假设变量和观测值的方向为 `rows`，这表示预测变量数据中的观测值沿 **x** 的行方向排列。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**`(j)` 是 **x** 中观测值 *j*（行或列）的响应。以下限制适用：

- **x** 中的预测变量数量必须等于初始模型的 `NumPredictors` 属性值。如果流式数据中的预测变量数量与 `NumPredictors` 不同，模块会发出错误。
- IncrementalRegressionKernel Fit 模块仅支持数值输入预测变量数据。如果输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，连接所有虚拟变量矩阵和任何其他数值预测变量。有关更多详细信息，请参阅虚拟变量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — 响应数据块 数值向量

要拟合模型的响应数据块，指定为数值向量。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；`y(j)` 是 **x** 中观测值 *j*（行或列）的响应。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **w** — 观测值权重数据块 正值向量

观测值权重数据块，指定为正值的向量。IncrementalRegressionKernel Fit 模块使用 **w** 中的对应值对 **x** 中的观测值进行加权。**w** 的大小必须等于 **x** 中的观测值数量。

#### 依赖项

要启用此端口，请在模块参数对话框的 **Main** 选项卡上选中 **Add input port for observation weights** 复选框。

**数据类型：** `single` | `double`

### **reset** — 重置信号 `0` (`false`) | `1` (`true`) | 数值标量

*自 R2025a 起*

重置信号，指定为 `0` (`false`) 或 `1` (`true`) 或数值标量。当 **reset** 信号为正标量（大于 0）时，模块会重置增量学习模型的已学习参数（如果有）。如果在增量训练期间估计了 **mdl** 的任何超参数，这些超参数也会被重置。`mdl.NumPredictors` 始终保留。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **mdl** — 更新后的增量学习模型参数 总线信号

拟合到流式数据的增量学习模型的更新参数（包括 `Beta` 和 `Bias`），以总线信号形式返回（请参阅复合信号 (Simulink)）。

## 参数

要交互式编辑模块参数，请使用属性检查器。从 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### Main

### **Select initial machine learning model** — 初始增量核回归模型 `kernelMdl`（默认） | `incrementalRegressionKernel` 模型对象

指定包含已配置 `incrementalRegressionKernel` 模型对象的工作区变量名称。

创建初始模型对象时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数量。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `incrementalRegressionKernel` 对象名称 |
| **默认值：** `"kernelMdl"` |

### **Add input port for observation weights** — 添加用于观测值权重的第二个输入端口 `off`（默认） | `on`

选中此复选框可在 IncrementalRegressionKernel Fit 模块中包含用于观测值权重的输入端口 **w**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowInputWeights` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Add input port for resetting trained learner** — 添加用于重置已训练增量学习器的输入端口 `off`（默认） | `on`

*自 R2025a 起*

选中此复选框可在 IncrementalRegressionKernel Fit 模块中包含用于重置信号的输入端口 **reset**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowInputReset` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，IncrementalRegressionKernel Fit 模块根据模型内模块的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作方法 `off`（默认） | `on`

指定溢出是饱和还是绕回。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框时，模块输出在 127 处饱和。类似地，模块输出在最小值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块处理超出范围信号的方式。有关更多信息，请参阅排查信号范围错误 (Simulink)。 | 溢出绕回到数据类型可表示的相应值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Beta data type** — 线性系数估计的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中线性系数估计（beta）的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`BetaDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Beta data type Minimum** — 用于范围检查的 beta 最小值 `[]`（默认） | 标量

指定 Simulink 检查的 beta 范围的下限。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码并影响某些仿真模式（例如 software-in-the-loop (SIL) 模式或外部模式）的结果。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Beta data type Minimum** 参数不会饱和或裁剪实际 beta 估计。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`BetaOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Beta data type Maximum** — 用于范围检查的 beta 最大值 `[]`（默认） | 标量

指定 Simulink 检查的 beta 范围的上限。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Beta data type Maximum** 参数不会饱和或裁剪实际 beta 估计。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`BetaOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Bias data type** — 截距估计的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中截距估计（bias）的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`BiasDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Bias data type Minimum** — 用于范围检查的 bias 最小值 `[]`（默认） | 标量

指定 Simulink 检查的 bias 范围的下限。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码并影响某些仿真模式（例如 software-in-the-loop (SIL) 模式或外部模式）的结果。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Bias data type Minimum** 参数不会饱和或裁剪实际 bias 估计。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`BiasOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Bias data type Maximum** — 用于范围检查的 bias 最大值 `[]`（默认） | 标量

指定 Simulink 检查的 bias 范围的上限。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关更多信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Bias data type Maximum** 参数不会饱和或裁剪实际 bias 估计。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`BiasOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **核数据类型** — 核计算数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于高斯核近似计算的参数的数据类型。
该类型可以直接指定，也可以表示为数据类型对象，例如
`Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定核数据类型。该内部规则会选择一种可优化数值精度、性能和生成代码大小的数据类型，同时考虑嵌入式目标硬件的属性。该软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`KernelDataTypeStr` |
| **类型**：character vector |
| **值**：`'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **核数据类型最小值** — 用于范围检查的核计算最小值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最小值**参数不会饱和或裁剪实际的核计算值。

#### 编程用法

|  |
| --- |
| **模块参数**：`KernelOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **核数据类型最大值** — 用于范围检查的核计算最大值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最大值**参数不会饱和或裁剪实际的核计算值。

#### 编程用法

|  |
| --- |
| **模块参数**：`KernelOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

#### 其他数据类型

### **内部状态数据类型** — 内部状态的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中内部状态的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`StatesDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **内部状态数据类型最小值** — 用于范围检查的内部状态最小值 `[]`（默认）| 标量

指定 Simulink 检查的内部状态范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**内部状态数据类型最小值**参数不会饱和或裁剪实际的内部状态。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`StatesOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **内部状态数据类型最大值** — 用于范围检查的内部状态最大值 `[]`（默认）| 标量

指定 Simulink 检查的内部状态范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**内部状态数据类型最大值**参数不会饱和或裁剪实际的内部状态。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`StatesOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Mu 数据类型** — 预测变量均值的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中预测变量均值 (mu) 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

如果在创建初始模型时未指定 `Standardize`=`"true"`，则 IncrementalRegressionKernel Fit 模块将 mu 设置为 `0`。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`MuDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Mu 数据类型最小值** — 用于范围检查的 mu 最小值 `[]`（默认）| 标量

指定 Simulink 检查的 mu 范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Mu 数据类型最小值**参数不会饱和或裁剪实际的 mu 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`MuOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Mu 数据类型最大值** — 用于范围检查的 mu 最大值 `[]`（默认）| 标量

指定 Simulink 检查的 mu 范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Mu 数据类型最大值**参数不会饱和或裁剪实际的 mu 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`MuOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Sigma 数据类型** — 预测变量标准差的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **mdl** 输出总线信号中预测变量标准差 (sigma) 的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

如果在创建初始模型时未指定 `Standardize`=`true`，则 IncrementalRegressionKernel Fit 模块将 sigma 设置为 `0`。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`SigmaDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Sigma 数据类型最小值** — 用于范围检查的 sigma 最小值 `[]`（默认）| 标量

指定 Simulink 检查的 sigma 范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如软件在环 (SIL) 模式或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Sigma 数据类型最小值**参数不会饱和或裁剪实际的 sigma 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`SigmaOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Sigma 数据类型最大值** — 用于范围检查的 sigma 最大值 `[]`（默认）| 标量

指定 Simulink 检查的 sigma 范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可以删除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**Sigma 数据类型最大值**参数不会饱和或裁剪实际的 sigma 值。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`SigmaOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Regression / Kernel

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

### R2025a：新增 reset 输入端口

IncrementalRegressionKernel Fit 具有新的 **reset** 输入端口，可用于重置增量学习模型已学习的参数（如有）。如果在增量训练期间估计了模型的任何超参数，这些超参数也会被重置。在执行漂移感知学习时，使用 **reset** 信号在检测到漂移时重置模型参数。

## 描述

拟合增量核回归模型

IncrementalRegressionKernel Fit 模块将配置的核回归增量模型 (`incrementalRegressionKernel`) 拟合到流式数据。

通过指定包含初始核回归模型对象的工作区变量名称，将该对象导入模块。输入端口 **x** 接收一块预测变量数据（观测值），输入端口 **y** 接收一块模型所拟合的响应。输出端口 **mdl** 返回更新后的 `incrementalRegressionKernel` 模型。可选输入端口 **w** 接收一块观测权重，可选输入端口 **reset** 重置已学习的参数。
