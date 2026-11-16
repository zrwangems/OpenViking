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

### 输入

### **mdl** — 增量学习模型总线信号

拟合流式数据的增量学习模型（`incrementalClassificationKernel`），指定为总线信号（请参阅 Composite Signals (Simulink)）。

### **x** — 预测变量数据块数值矩阵

预测变量数据块，指定为数值矩阵。

**注意**

该模块仅支持数值输入预测变量数据。如果输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为哑变量的数值矩阵。然后，将所有哑变量矩阵和任何其他数值预测变量串联起来。有关更多详细信息，请参阅 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **label** — 预测类标签块列向量

预测类标签块，以列向量形式返回。标签 `label(i)` 表示对观测值 **x**(`i`) 产生最高分数的类。有关更多详细信息，请参阅 `predict` 对象函数的 `label` 输出参数。

如果在创建 **mdl** 时指定估计期，则预测类标签是估计期内的多数类。该类占 **x** 中训练标签的最大比例。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测类分数或后验概率矩阵

预测类分数或后验概率，以矩阵形式返回。如果模型是使用逻辑学习器训练的，则分类分数是后验概率。分类分数 `score(i)` 表示 **x** 中的观测值属于类 `i` 的后验概率。有关更多详细信息，请参阅 Classification Score。

要检查类的顺序，请使用由 **选择初始机器学习模型** 指定的核分类模型的 `ClassNames` 属性。

**注意**

如果在创建 **mdl** 时指定估计期，则在估计期内预测类分数为零。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主** 选项卡上选中 **为预测类分数添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **CanPredict** — 模型状态 `0` (`false`) | `1`(`true`)

用于预测的模型状态，以数值或逻辑值 `0` (`false`) 或 `1` (`true`) 返回。

**注意**

如果在创建 **mdl** 时指定估计期，则在估计期内模型状态为 `0` (`false`)。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主** 选项卡上选中 **为训练好的机器学习模型状态添加输出端口** 复选框。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，从 **准备** 库中选择 **属性检查器**。

### 主

### **选择初始机器学习模型** — 初始增量核分类模型 `kernelMdl`（默认）| `incrementalClassificationKernel` 模型对象

指定包含已配置 `incrementalClassificationKernel` 模型对象的工作区变量的名称。

创建初始模型对象时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须为数值（`double` 或 `single`）。要将分类预测变量包含在模型中，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `ScoreTransform` 属性不能为 `"invlogit"` 或匿名函数。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** character vector or string |
| **值：** `incrementalClassificationKernel` 对象名称 |
| **默认值：** `"kernelMdl"` |

### **为预测类分数添加输出端口** — 为预测类分数添加第二个输出端口 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationKernel Predict 模块中包含输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** character vector or string |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **为训练好的机器学习模型状态添加输出端口** — 为模型状态添加第三个输出端口 `off`（默认）| `on`

选中此复选框可在 IncrementalClassificationKernel Predict 模块中包含输出端口 **CanPredict**。如果在创建 IncrementalClassificationKernel Predict 模块时，工作区中已包含名为 `kernelMdl` 且能够进行预测的增量核分类模型，则此复选框不会出现。或者，您可以通过在 Simulink 工作区中选择 IncrementalClassificationKernel Predict 模块，并在 MATLAB® 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")`，来指定包含输出端口 **CanPredict**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** character vector or string |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalClassificationKernel Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SystemSampleTime` |
| **类型：** string scalar or character vector |
| **值：** 标量 |
| **默认值：** `"–1"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成代码中提供显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中此复选框后，模块输出饱和于 127。同样，模块输出饱和于最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可以表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除此复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** character vector |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **标签数据类型** — label 输出的数据类型 `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以继承、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **选择初始机器学习模型** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点，以及数据类型对象。
- 如果模型使用非数值标签，支持的数据类型为 `Enum: <class name>` 和数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **标签数据类型**（请参阅 Data Type Propagation (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **选择初始机器学习模型** 指定的工作区变量名为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，对应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。该模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelDataTypeStr` |
| **类型**： character vector |
| **值**： `"Inherit: Inherit via back propagation"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**： `"Inherit: Inherit via back propagation"`（对于数值和逻辑标签） | `"Inherit: auto"`（对于非数值标签） |

### **标签数据类型最小值** — 用于范围检查的 label 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**标签数据类型最小值** 参数不会使实际 **label** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择初始机器学习模型** 指定的模型使用数值标签时，您才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMin` |
| **类型**： character vector |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **标签数据类型最大值** — 用于范围检查的 label 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关更多信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**标签数据类型最大值** 参数不会使实际 **label** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 依赖关系

仅当 **选择初始机器学习模型** 指定的模型使用数值标签时，您才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**： `LabelOutMax` |
| **类型**： character vector |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **分数数据类型** — score 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的更多信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `ScoreDataTypeStr` |
| **类型**： character vector or string |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **Score data type Minimum** — 用于范围检查的 score 输出最小值 `[]`（默认）| scalar

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Minimum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ScoreOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

### **Score data type Maximum** — 用于范围检查的 score 输出最大值 `[]`（默认）| scalar

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Score data type Maximum** 参数不会饱和或裁剪实际的 **score** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

#### 其他数据类型

### **Kernel data type** — Kernel 计算数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于高斯核近似计算的参数数据类型。该类型可以直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定 Kernel 数据类型。内部规则选择一种数据类型，以优化数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `KernelDataTypeStr` |
| **类型**: character vector |
| **值**: `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认**: `'Inherit: Inherit via internal rule'` |

### **Kernel data type Minimum** — 用于范围检查的 Kernel 计算最小值 `[]`（默认）| scalar

指定 Simulink 检查的 Kernel 计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Kernel data type Minimum** 参数不会饱和或裁剪实际的 Kernel 计算值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `KernelOutMin` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

### **Kernel data type Maximum** — 用于范围检查的 Kernel 计算最大值 `[]`（默认）| scalar

指定 Simulink 检查的 Kernel 计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Kernel data type Maximum** 参数不会饱和或裁剪实际的 Kernel 计算值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `KernelOutMax` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认**: `'[]'` |

### **Inner product data type** — 预测响应的内积项 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定内积数据类型。内部规则选择一种数据类型，以优化数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认**: `"Inherit: Inherit via internal rule"` |

### **Inner product data type Minimum** — 用于范围检查的内积项最小值 `[]`（默认）| scalar

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Minimum** 参数不会饱和或裁剪实际的内积项值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

### **Inner product data type Maximum** — 用于范围检查的内积项最大值 `[]`（默认）| scalar

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Inner product data type Maximum** 参数不会饱和或裁剪实际的内积项值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认**: `"[]"` |

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

使用增量核分类模型对观测进行分类

IncrementalClassificationKernel Predict 模块使用由 IncrementalClassificationKernel Fit 模块作为输出返回的训练核分类模型对观测进行分类。

通过指定包含初始核分类模型对象的工作区变量名称，将该对象导入 IncrementalClassificationKernel Predict 模块。输入端口 **mdl** 接收表示拟合到流式数据的增量学习模型的总线信号。输入端口 **x** 接收一块预测变量数据（观测），输出端口 **label** 返回该块的预测类标签。可选输出端口 **score** 返回预测类得分或后验概率，可选输出端口 **CanPredict** 返回训练模型的预测状态。
