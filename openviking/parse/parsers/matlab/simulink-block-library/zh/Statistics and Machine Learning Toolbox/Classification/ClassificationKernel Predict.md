---
type: simulink-block
title: 'ClassificationKernel Predict'
family: 'classification'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationkernelpredict'
documentation_source_path: 'classificationkernelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# ClassificationKernel Predict

## 端口

### 输入

### **x** — 预测变量数据行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量必须与训练由 **选择训练过的机器学习模型** 指定的核分类模型所使用的预测变量具有相同顺序。

如果在训练模型时在 `fitckernel` 中将 `Standardize=true`，则 ClassificationKernel Predict 模块使用模型的 `Mu` 和 `Sigma` 属性（分别）中的均值和标准差对 **x** 的值进行标准化。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **label** — 预测的类标签 标量

预测的类标签，返回为对应于产生最高分数的类的标量。有关详细信息，请参阅 `predict` 对象函数的 `Label` 参数。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — 预测的类分数或后验概率 1×2 向量

预测的类分数或后验概率，返回为 1×2 向量。

**score** 的第一个和第二个元素分别对应于负类（`kernelMdl.ClassNames(1)`）和正类（`kernelMdl.ClassNames(2)`）的分类分数，其中 `kernelMdl` 是由 **选择训练过的机器学习模型** 指定的核模型。您可以使用 `kernelMdl` 的 `ClassNames` 属性来检查负类和正类名称。如果 `kernelMdl.Learner` 为 `'logistic'`，则分类分数为后验概率。

#### 依赖项

要启用此端口，请在模块参数对话框的 **主** 选项卡上选中 **为预测的类分数添加输出端口** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

要交互式编辑模块参数，请使用属性检查器。从 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### 主

### **选择训练过的机器学习模型** — 核分类模型 `kernelMdl`（默认）| `ClassificationKernel` 对象

指定包含 `ClassificationKernel` 对象的工作区变量名称。

当您使用 `fitckernel` 训练核分类模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果您在表中提供训练数据，则预测变量必须是数值（`double` 或 `single`）。此外，您不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- `ScoreTransform` 名称-值参数的值不能为 `'invlogit'` 或匿名函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `ClassificationKernel` 对象名称 |
| **默认值：** `"kernelMdl"` |

### **为预测的类分数添加输出端口** — 为预测的类分数添加第二个输出端口 `off`（默认）| `on`

选中此复选框以在 ClassificationKernel Predict 模块中包含输出端口 **score**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputScore` |
| **类型：** 字符向量或字符串 |
| **值：** `"off"|"on"` |
| **默认值：** `"off"` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢流是饱和还是绕回。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中具有显式饱和保护。 | 溢流饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误 (Simulink)。 | 溢流绕回到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，130（二进制 1000 0010）的模块结果表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Label 数据类型** — label 输出的数据类型 `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

指定 **label** 输出的数据类型。该类型可以是继承的、指定为枚举数据类型，或表示为数据类型对象，例如 `Simulink.NumericType`。

支持的数据类型取决于 **选择训练过的机器学习模型** 指定的模型中使用的标签。

- 如果模型使用数值或逻辑标签，则支持的数据类型为 `Inherit: Inherit via back propagation`（默认）、`double`、`single`、`half`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`boolean`、定点以及数据类型对象。
- 如果模型使用非数值标签，则支持的数据类型为 `Inherit: auto`（默认）、`Enum: <class name>` 以及数据类型对象。

当您选择继承选项时，软件的行为如下：

- `Inherit: Inherit via back propagation`（数值和逻辑标签的默认值）— Simulink 在数据类型传播期间自动确定模块的 **Label 数据类型**（请参阅数据类型传播 (Simulink)）。在这种情况下，模块使用下游模块或信号对象的数据类型。
- `Inherit: auto`（非数值标签的默认值）— 模块使用自动定义的枚举数据类型变量。例如，假设 **选择训练过的机器学习模型** 指定的工作区变量名称为 `myMdl`，类标签为 `class 1` 和 `class 2`。那么，相应的 **label** 值为 `myMdl_enumLabels.class_1` 和 `myMdl_enumLabels.class_2`。模块使用 `matlab.lang.makeValidName` 函数将类标签转换为有效的 MATLAB 标识符。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via back propagation"`（对于数值和逻辑标签）| `"Inherit: auto"`（对于非数值标签） |

### **Label 数据类型最小值** — 用于范围检查的 label 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Label 数据类型最小值** 参数不会饱和或裁剪实际的 **label** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖项

仅当 **选择训练过的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Label 数据类型最大值** — 用于范围检查的 label 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **label** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Label 数据类型最大值** 参数不会饱和或裁剪实际的 **label** 输出信号。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 依赖项

仅当 **选择训练过的机器学习模型** 指定的模型使用数值标签时，才能指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score 数据类型** — score 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **score** 输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Score 数据类型最小值** — 用于范围检查的 score 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的下限值。

Simulink 使用最小值执行：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score 数据类型最小值** 参数不会饱和或裁剪实际的 **score** 输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Score 数据类型最大值** — 用于范围检查的 score 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **score** 输出范围的上限值。

Simulink 使用最大值执行：

- 对某些模块进行参数范围检查（请参阅为模块参数指定最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**Score 数据类型最大值** 参数不会饱和或裁剪实际的 **score** 输出。要执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScoreOutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **原始分数数据类型** — 未变换的分数数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定内部未变换分数的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

仅当由 **选择训练好的机器学习模型** 指定的模型使用非 `"none"`（默认，与 `"identity"` 相同）的分数变换时，才能指定此参数。

- 如果模型不使用分数变换（`"none"` 或 `"identity"`），则可以使用 **分数数据类型** 指定分数数据类型。
- 如果模型使用除 `"none"` 或 `"identity"` 之外的分数变换，则可以使用此参数指定未变换原始分数的数据类型。要指定变换后分数的数据类型，请使用 **分数数据类型**。

您可以在训练期间通过指定 `ScoreTransform` 名称-值参数，或在训练后修改 `ScoreTransform` 属性，来更改分数变换选项。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: auto"` |

### **原始分数数据类型最小值** — 用于范围检查的未变换分数最小值 `[]`（默认） | scalar

指定 Simulink 检查的未变换分数范围的下限值。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**原始分数数据类型最小值**参数不会饱和或裁剪实际的未变换分数信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

### **原始分数数据类型最大值** — 用于范围检查的未变换分数最大值 `[]`（默认） | scalar

指定 Simulink 检查的未变换分数范围的上限值。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**原始分数数据类型最大值**参数不会饱和或裁剪实际的未变换分数信号。

#### 编程用法

|  |
| --- |
| **模块参数**: `RawScoreOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | scalar |
| **默认值**: `"[]"` |

#### 其他数据类型

### **核数据类型** — 核计算数据类型 `Inherit: Inherit via internal rule`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于高斯核近似计算的参数的数据类型。该类型可以直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定核数据类型。该内部规则会选择一种数据类型，以优化数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**: `KernelDataTypeStr` |
| **类型**: character vector |
| **值**: `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**: `'Inherit: Inherit via internal rule'` |

### **核数据类型最小值** — 用于范围检查的核计算最小值 `[]`（默认） | scalar

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用该最小值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最小值**参数不会饱和或裁剪实际的核计算值。

#### 编程用法

|  |
| --- |
| **模块参数**: `KernelOutMin` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认值**: `'[]'` |

### **核数据类型最大值** — 用于范围检查的核计算最大值 `[]`（默认） | scalar

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用该最大值执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化您从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最大值**参数不会饱和或裁剪实际的核计算值。

#### 编程用法

|  |
| --- |
| **模块参数**: `KernelOutMax` |
| **类型**: character vector |
| **值**: `'[]'` | scalar |
| **默认值**: `'[]'` |

## 所属库

Statistics and Machine Learning Toolbox / Classification

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

使用高斯核分类器进行二分类以对观测值进行分类

ClassificationKernel Predict 模块使用核分类对象（`ClassificationKernel`）对观测值进行分类，以通过随机特征扩展进行二分类。

通过指定包含该对象的工作区变量的名称，将训练好的核分类对象导入模块。输入端口 **x** 接收一个观测值（预测变量数据），输出端口 **label** 返回该观测值的预测类标签。可选输出端口 **score** 返回预测的类分数或后验概率。
