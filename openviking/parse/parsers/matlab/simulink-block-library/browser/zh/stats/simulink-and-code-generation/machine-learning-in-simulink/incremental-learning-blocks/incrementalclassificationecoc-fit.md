---
type: simulink-block
title: 'IncrementalClassificationECOC Fit'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Support Vector Machine Classification'
documentation_page: 'incrementalclassificationecocfit'
documentation_source_path: 'incrementalclassificationecocfit.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalClassificationECOC Fit

## 端口

### 输入

### **x** — 预测变量数据块 数值矩阵

要拟合模型的预测变量数据块，指定为数值矩阵。
变量和观测值的方向由 **预测变量数据观测维度** 指定。默认方向为 `rows`，表示预测变量数据中的观测值沿 **x** 的行方向排列。

观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；
**y**`(j)` 是 **x** 中观测值 *j*（行或列）的响应。

**注意**

**x** 中的预测变量数量必须等于初始模型的 `NumPredictors` 属性值。如果流数据中预测变量数量与 `NumPredictors` 不同，模块将报错。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — 类标签块 数值向量 | 逻辑向量 | 枚举向量

用于训练模型的类标签块，指定为数值、逻辑或枚举向量。

- 观测响应 **y** 的长度与 **x** 中的观测值数量必须相等；**y**(`j`) 是 **x** 中观测值 *j*（行或列）的响应。
- 每个标签必须对应数组的一行。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — 观测权重块 正值向量

观测权重块，指定为正值的向量。IncrementalClassificationECOC Fit 模块使用 **w** 中的对应值对 **x** 中的观测值进行加权。**w** 的大小必须等于 **x** 中的观测值数量。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡中选中 **添加观测权重输入端口** 复选框。

**数据类型：** `single` | `double`

### **reset** — 复位信号 `0` (`false`) | `1` (`true`) | 数值标量

*自 R2025a 起*

复位信号，指定为 `0` (`false`) 或 `1` (`true`) 或数值标量。当 **reset** 信号为正标量（大于 0）时，模块将复位增量学习模型的已学习参数（如果有）。如果在增量训练期间估计了 **mdl** 的任何超参数，这些超参数也会被复位。`mdl.NumPredictors` 始终保留。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **mdl** — 更新后的增量学习模型参数 总线信号

更新后的增量学习模型参数，拟合到流数据，返回为总线信号（参见 `Composite Signals` (Simulink)）。

## 参数

### 主要

### **选择初始机器学习模型** — 初始增量分类 ECOC 模型 `ecocMdl`（默认） | `incrementalClassificationECOC` 模型对象

指定包含已配置的 `incrementalClassificationECOC` 模型对象的工作区变量名称。初始模型必须指定以下属性：

- `NumPredictors` 属性，其必须是等于 **x** 中预测变量数量的正整数标量。
- `ClassNames` 属性。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 工作区变量 |
| **值：** `incrementalClassificationECOC` 模型对象 |
| **默认值：** `"ecocMdl"` |

### **添加观测权重输入端口** — 添加第二个输入端口用于观测权重 `off`（默认） | `on`

选中此复选框可在 IncrementalClassificationECOC Fit 模块中包含观测权重输入端口 **w**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowInputWeights` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **添加用于复位训练学习器的输入端口** — 添加用于复位训练增量学习器的输入端口 `off`（默认） | `on`

*自 R2025a 起*

选中此复选框可在 IncrementalClassificationECOC Fit 模块中包含复位信号输入端口 **reset**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowInputReset` |
| **类型：** 字符向量或字符串 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **预测变量数据观测维度** — 预测变量数据的观测维度 `rows`（默认） | `columns`

指定预测变量数据的观测维度。默认值为 `rows`，表示预测变量数据中的观测值沿 **x** 的行方向排列。

#### 编程使用

|  |
| --- |
| **模块参数：** `ObservationsIn` |
| **类型：** 字符向量 |
| **值：** `"rows" | "columns"` |
| **默认值：** `"rows"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalClassificationECOC Fit 模块根据模型中的模块上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** 字符串标量或字符向量 |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框时，模块输出饱和在 127。类似地，模块输出饱和在最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成的代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **二元学习器 beta 数据类型** — 线性系数估计输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定线性系数估计（beta）输出的数据类型。该类型可以继承，指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBetaDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **二元学习器 beta 数据类型最小值** — 用于范围检查的 beta 最小值 `[]`（默认） | 标量

指定 Simulink® 检查的 beta 输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二元学习器 beta 数据类型最小值** 参数不会饱和或裁剪实际的 beta 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBetaOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **二元学习器 beta 数据类型最大值** — 用于范围检查的 beta 最大值 `[]`（默认） | 标量

指定 Simulink 检查的 beta 输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二元学习器 beta 数据类型最大值** 参数不会饱和或裁剪实际的 beta 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBetaOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **二元学习器偏置数据类型** — 截距估计输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定截距估计（偏置）输出的数据类型。该类型可以继承，指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBiasDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **二元学习器偏置数据类型最小值** — 用于范围检查的偏置最小值 `[]`（默认） | 标量

指定 Simulink 检查的偏置输出范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二元学习器偏置数据类型最小值** 参数不会饱和或裁剪实际的偏置输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBiasOutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **二元学习器偏置数据类型最大值** — 用于范围检查的偏置最大值 `[]`（默认） | 标量

指定 Simulink 检查的偏置输出范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**二元学习器偏置数据类型最大值** 参数不会饱和或裁剪实际的偏置输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**： `BinaryBiasOutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **Binary learner internal states data type** — 二进制学习器内部状态输出的数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二进制学习器内部状态输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryStatesDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Binary learner internal states data type Minimum** — 用于范围检查的二进制学习器内部状态最小值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器内部状态范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryStatesOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Binary learner internal states data type Maximum** — 用于范围检查的二进制学习器内部状态最大值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器内部状态范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryStatesOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Prior data type** — 先验项的数据类型 `double` (默认) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部先验项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`PriorDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |`"<data type expression>"` |
| **默认值**：`"double"` |

### **Prior data type Minimum** — 用于范围检查的先验项最小值 `[]` (默认) | 标量

指定 Simulink 检查的先验项范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Prior data type Minimum** 参数不会饱和或裁剪实际先验项值。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PriorOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Prior data type Maximum** — 用于范围检查的先验项最大值 `[]` (默认) | 标量

指定 Simulink 检查的先验项范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Prior data type Maximum** 参数不会饱和或裁剪实际先验项值。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`PriorOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Binary learner mu data type** — 二进制学习器 mu 输出的数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二进制学习器 mu（预测变量均值）输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`Binary MuDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Binary learner mu data type Minimum** — 用于范围检查的二进制学习器 mu 最小值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器 mu 范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Binary learner mu data type Minimum** 参数不会饱和或裁剪实际 mu 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryMuOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Binary learner mu data type Maximum** — 用于范围检查的二进制学习器 mu 最大值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器 mu 范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Binary learner mu data type Maximum** 参数不会饱和或裁剪实际 mu 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinaryMuOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Binary learner sigma data type** — 二进制学习器 sigma 输出的数据类型 `Inherit: auto` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定二进制学习器 sigma（预测变量标准差）输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象（如 `Simulink.NumericType`）。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`Binary SigmaDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"`|`"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Binary learner sigma data type Minimum** — 用于范围检查的二进制学习器 sigma 最小值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器 sigma 范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Binary learner sigma data type Minimum** 参数不会饱和或裁剪实际 sigma 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinarySigmaOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Binary learner sigma data type Maximum** — 用于范围检查的二进制学习器 sigma 最大值 `[]` (默认) | 标量

指定 Simulink 检查的二进制学习器 sigma 范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。这种优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Binary learner sigma data type Maximum** 参数不会饱和或裁剪实际 sigma 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`BinarySigmaOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / ECOC

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

**在 R2024a 中引入**

### R2025a：新增 reset 输入端口

IncrementalClassificationECOC Fit 有一个新的 **reset** 输入端口，可用于重置增量学习模型的已学习参数（如果有）。如果在增量训练期间估计了模型的任何超参数，这些超参数也会被重置。在执行漂移感知学习时，使用 **reset** 信号在检测到漂移时重置模型参数。

## 描述

拟合增量 ECOC 分类模型

IncrementalClassificationECOC Fit 模块将配置的增量纠错输出码 (ECOC) 分类模型 (`incrementalClassificationECOC`) 拟合到流式数据，用于多类分类。

通过指定包含该对象的工作区变量名称，将初始 ECOC 分类对象导入到模块中。输入端口 **x** 接收一部分预测变量数据（观测值），输入端口 **y** 接收模型所拟合的一部分响应（标签）。输出端口返回更新后的 `incrementalClassificationECOC` 模型 **mdl**。可选输入端口 **w** 接收一部分观测权重，可选输入端口 **reset** 重置已学习参数。
