---
type: simulink-block
title: 'IncrementalRegressionLinear Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression / Linear Regression / Multiple Linear Regression'
documentation_page: 'incrementalregressionlinearpredict'
documentation_source_path: 'incrementalregressionlinearpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalRegressionLinear Predict

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型（`incrementalRegressionLinear`），指定为总线信号（请参阅 `Composite
Signals` (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。变量和观测值的方向由 **Predictor data observation dimension** 指定。默认方向为 `rows`，这表明预测变量数据中的观测值沿 **x** 的行方向排列。

**注意**

该模块仅支持数值输入预测变量数据。如果您的输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，将所有虚拟变量矩阵和任何其他数值预测变量串联起来。有关更多详细信息，请参阅 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **yfit** — 预测响应块 浮点向量

预测响应块，以浮点向量形式返回。有关更多详细信息，请参阅 Predicted response 和 `predict` 对象函数的 `YHat` 参数。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内预测响应为零。

**数据类型：** `single` | `double`

### **CanPredict** — 模型状态 逻辑

用于预测的模型状态，以逻辑值 `0`（`false`）或 `1`（`true`）返回。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内模型状态为 0（false）。

#### 依赖项

要启用此端口，请在“模块参数”对话框的 **主** 选项卡上选中 **Add output port for status of trained machine learning model** 复选框。

## 参数

### 主

### **Select initial machine learning model** — 初始增量线性回归模型 `linearMdl`（默认） | `incrementalRegressionLinear` 模型对象

指定包含已配置 `incrementalRegressionLinear` 模型对象的工作区变量的名称。

以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须是数值（`double` 或 `single`）。若要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对它们进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数。
- *在 R2024a 之前：初始模型的 `Solver` 属性必须为 `"scale-invariant"`。*

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 工作区变量 |
| **值：** `incrementalRegressionLinear` 模型对象 |
| **默认值：** `"linearMdl"` |

### **Add output port for status of trained machine learning model** — 为模型状态添加第二个输出端口 `off`（默认） | `on`

选中此复选框可在 IncrementalRegressionLinear Predict 模块中包含输出端口 **CanPredict**。如果在创建 IncrementalRegressionLinear Predict 模块时，工作区中已包含名为 `linearMdl` 且能够进行预测的增量线性回归模型，则不会显示此复选框。或者，您可以通过在 Simulink® 工作区中选择 IncrementalRegressionLinear Predict 模块，并在 MATLAB 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")` 来指定包含输出端口 **CanPredict**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Predictor data observation dimension** — 预测变量数据的观测维度 `rows`（默认） | `columns`

指定预测变量数据的观测维度。默认值为 `rows`，这表明预测变量数据中的观测值沿 **x** 的行方向排列。

#### 编程用法

|  |
| --- |
| **模块参数：** `ObservationsIn` |
| **类型：** 字符向量 |
| **值：** `"rows" | "columns"` |
| **默认值：** `"rows"` |

### **Sample time (–1 for inherited)** — 指定采样时间的选项 `–1`（默认） | scalar

指定采样命中之间的离散间隔，或指定另一种采样时间类型，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalRegressionLinear Predict 模块根据模块在模型中的上下文继承采样时间。

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

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认） | `on`

指定溢出时饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成的代码的效率。您希望避免过度指定模块如何处理越界信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型能表示的相应值。 | `int8`（有符号 8 位整数）数据类型能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框时，软件将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Output data type** — yfit 输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **yfit** 输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值：** `"Inherit: auto"` |

### **Output data type Minimum** — 用于范围检查的 yfit 输出最小值 `[]`（默认） | scalar

指定 Simulink 检查的 **yfit** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output data type Minimum** 参数不会饱和或裁剪实际的 **yfit** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutMin` |
| **类型：** 字符向量 |
| **值：** `"[]"` | scalar |
| **默认值：** `"[]"` |

### **Output data type Maximum** — 用于范围检查的 yfit 输出最大值 `[]`（默认） | scalar

指定 Simulink 检查的 **yfit** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output data type Maximum** 参数不会饱和或裁剪实际的 **yfit** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutMax` |
| **类型：** 字符向量 |
| **值：** `"[]"` | scalar |
| **默认值：** `"[]"` |

### **Inner product data type** — 内积数据类型 `double`（默认） | `Inherit: Inherit via internal rule` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应的内积项的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定内积数据类型。内部规则选择一种数据类型，以优化数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `InnerProductDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值：** `"double"` |

### **Inner product data type Minimum** — 用于范围检查的内积项最小值 `[]`（默认） | scalar

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Minimum** 参数不会饱和或裁剪实际的内积项值。

#### 编程用法

|  |
| --- |
| **模块参数：** `InnerProductOutMin` |
| **类型：** 字符向量 |
| **值：** `"[]"` | scalar |
| **默认值：** `"[]"` |

### **Inner product data type Maximum** — 用于范围检查的内积项最大值 `[]`（默认） | scalar

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Maximum** 参数不会饱和或裁剪实际的内积项值。

#### 编程用法

|  |
| --- |
| **模块参数：** `InnerProductOutMax` |
| **类型：** 字符向量 |
| **值：** `"[]"` | scalar |
| **默认值：** `"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Regression / Linear

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023b 中引入**

### R2024a：增量线性模块支持其他求解器

从 R2024a 开始，IncrementalRegressionLinear Predict 模块还支持 `Solver` 为 `"sgd"` 或
`"asgd"` 的初始机器学习模型。

## 描述

使用增量线性回归模型预测响应

IncrementalRegressionLinear Predict 模块使用 IncrementalRegressionLinear Fit 模块输出返回的训练线性回归模型，为流式数据预测响应。

通过指定包含该对象的工作区变量名称，将初始线性回归模型对象导入该模块。输入端口 **mdl**
接收一个总线信号，该信号表示拟合到流式数据的增量学习模型。输入端口 **x** 接收一块预测变量数据
（观测值），输出端口 **yfit** 返回该块的预测响应。可选输出端口 **CanPredict**
返回训练模型的预测状态。
