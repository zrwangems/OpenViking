---
type: simulink-block
title: 'IncrementalClassificationLinear Predict'
family: 'incremental-learning'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning'
documentation_page: 'incrementalclassificationlinearpredict'
documentation_source_path: 'incrementalclassificationlinearpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationLinear Predict

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

增量学习模型（`incrementalClassificationLinear`），已拟合到流式数据，指定为总线信号（参见 `Composite Signals` (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。变量和观测的方向由 **预测变量数据观测维度** 指定。默认方向为 `rows`，表示预测变量数据中的观测沿 **x** 的行方向排列。

**注意**

该模块仅支持数值输入预测变量数据。如果输入数据包含分类数据，则必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，将所有虚拟变量矩阵和其他数值预测变量串联起来。有关更多详细信息，请参见 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签块 列向量

预测类标签块，返回为列向量。标签 `label(i)` 表示对观测 **x**(`i`) 产生最高分数的类。有关更多详细信息，请参见 `predict` 对象函数的 `Label` 参数。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内预测的类标签为多数类，即在 **x** 的训练标签中占比最大的类。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率矩阵

预测类分数或后验概率，返回为矩阵。如果模型使用逻辑学习器训练，则分类分数为后验概率。分类分数 `score(i)` 表示 **x** 中的观测属于类 `i` 的后验概率。有关更多详细信息，请参见 Classification Score。

要检查类的顺序，请使用由 **选择初始机器学习模型** 指定的线性分类模型的 `ClassNames` 属性。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内预测的类分数为零。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主** 选项卡上选中 **为预测的类分数添加输出端口** 对应的复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **CanPredict** — 模型状态 逻辑值

用于预测的模型状态，返回为逻辑值 `0`（`false`）或 `1`（`true`）。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内模型状态为 0（false）。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主** 选项卡上选中 **为已训练机器学习模型的状态添加输出端口** 对应的复选框。

## 参数

### 主

### **选择初始机器学习模型** — 初始增量线性分类模型 `linearMdl`（默认）| `incrementalClassificationLinear` 模型对象

指定包含已配置的 `incrementalClassificationLinear` 模型对象的工作区变量名称。

以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，预测变量必须为数值（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对它们进行预处理。
- 初始模型的 `ScoreTransform` 属性不能为 `"invlogit"` 或匿名函数。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数目。
- *在 R2024a 之前：初始模型的 `Solver` 属性必须为 `"scale-invariant"`。*

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 工作区变量 |
| **值：** `incrementalClassificationLinear` 模型对象 |
| **默认值：** `"linearMdl"` |

### **为预测的类分数添加输出端口** — 添加第二个预测类分数输出端口 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationLinear Predict 模块中包括预测类分数的输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **为已训练机器学习模型的状态添加输出端口** — 添加第二个模型状态输出端口 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationLinear Predict 模块中包括输出端口 **CanPredict**。如果在创建 IncrementalClassificationLinear Predict 模块时，工作区已包含名为 `linearMdl` 且能够进行预测的增量线性分类模型，则此复选框不会出现。或者，您可以通过在 Simulink® 工作区中选择 IncrementalClassificationLinear Predict 模块，并在 MATLAB 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")`，来指定包括输出端口 **CanPredict**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **预测变量数据观测维度** — 预测变量数据的观测维度 `rows`（默认）| `columns`

指定预测变量数据的观测维度。默认值为 `rows`，表示预测变量数据中的观测沿 **x** 的行方向排列。

#### 编程用法

|  |
| --- |
| **模块参数：** `ObservationsIn` |
| **类型：** 字符向量 |
| **值：** `"rows" | "columns"` |
| **默认值：** `"rows"` |

### **采样时间（继承时为 –1）** — 指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参见 Types of Sample Time (Simulink)。

默认情况下，IncrementalClassificationLinear Predict 模块根据模型内模块的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参见 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **对整数溢出进行饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成代码中显式提供饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和在 127。类似地，模块输出饱和在最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参见 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可以表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参见 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **标签数据类型** — label 输出的数据类型 `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以是继承的、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于由 **选择初始机器学习模型** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、fixed point 以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **标签数据类型**（参见 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设由 **选择初始机器学习模型** 指定的工作区变量名为 `myMdl`，类标签为 `class 1` 和 `class 2`。则对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参见 Control Data Types of Signals (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参见 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: Inherit via back propagation"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via back propagation"`（用于数值和逻辑标签） | `"Inherit: auto"`（用于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的标签输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**标签数据类型最小值** 参数不会对实际的 **label** 输出信号进行饱和或裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择初始机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **标签数据类型最大值** — 用于范围检查的标签输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参见 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**标签数据类型最大值** 参数不会对实际的 **label** 输出信号进行饱和或裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当由 **选择初始机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score 数据类型** — score 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreDataTypeStr` |
| **类型**: character vector or string |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **Score 数据类型最小值** — 用于范围检查的 score 输出的最小值 `[]`（默认）| scalar

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score 数据类型最小值**参数不会饱和或裁剪实际的 **score** 输出。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

### **Score 数据类型最大值** — 用于范围检查的 score 输出的最大值 `[]`（默认）| scalar

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score 数据类型最大值**参数不会饱和或裁剪实际的 **score** 输出。若要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**: `ScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

### **内积数据类型** — 内积数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定内积数据类型。该内部规则选择一种可优化数值精度、性能和生成代码大小的数据类型，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `InnerProductDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"double"` |

### **内积数据类型最小值** — 用于范围检查的内积项的最小值 `[]`（默认）| scalar

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**内积数据类型最小值**参数不会饱和或裁剪实际内积项的值。

#### 编程用法

|  |
| --- |
| **模块参数**: `InnerProductOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

### **内积数据类型最大值** — 用于范围检查的内积项的最大值 `[]`（默认）| scalar

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**内积数据类型最大值**参数不会饱和或裁剪实际内积项的值。

#### 编程用法

|  |
| --- |
| **模块参数**: `InnerProductOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / Linear

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

**R2023b 中引入**

### R2024a: 增量线性模块支持其他求解器

从 R2024a 开始，IncrementalClassificationLinear Predict 模块还额外支持初始机器学习模型，其中 `Solver` 为 `"sgd"` 或 `"asgd"`。

## 描述

使用增量线性分类模型对观测值进行分类

IncrementalClassificationLinear Predict 模块使用训练后的线性分类模型对观测值进行分类，该模型作为 IncrementalClassificationLinear Fit 模块的输出返回。

通过指定包含该对象的工作区变量名称，将初始线性分类模型对象导入到模块中。输入端口 **mdl** 接收表示拟合到流式数据的增量学习模型的总线信号。输入端口 **x** 接收一块预测变量数据（观测值），输出端口 **label** 返回该数据块的预测类标签。可选的输出端口 **score** 返回预测类得分或后验概率。可选的输出端口 **CanPredict** 返回训练模型的预测状态。
