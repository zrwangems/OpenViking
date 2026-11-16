---
type: simulink-block
title: 'IncrementalRegressionKernel Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression / Support Vector Machine Regression'
documentation_page: 'incrementalregressionkernelpredict'
documentation_source_path: 'incrementalregressionkernelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalRegressionKernel Predict

## 端口

### 输入

### **mdl** — 增量学习模型总线信号

增量学习模型（`incrementalRegressionKernel`），已拟合流式数据，指定为总线信号（参见复合信号 (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。

**注意**

该模块仅支持数值输入预测变量数据。如果您的输入数据包含分类数据，必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为虚拟变量的数值矩阵。然后，串联所有虚拟变量矩阵以及任何其他数值预测变量。有关详细信息，请参见虚拟变量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **yfit** — 预测响应数据块 浮点向量

预测响应数据块，以浮点向量形式返回。

**注意**

如果在创建 **mdl** 时指定估计期，则在估计期内预测响应为零。

**数据类型：** `single` | `double`

### **CanPredict** — 模型状态 `0` (`false`) | `1` (`true`)

用于预测的模型状态，以逻辑值 `0` (`false`) 或 `1` (`true`) 返回。

**注意**

如果在创建 **mdl** 时指定估计期，则在估计期内模型状态为 `0` (`false`)。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的 **主要** 选项卡上选中 **为训练好的机器学习模型的状态添加输出端口** 复选框。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

### 主要

### **选择初始机器学习模型** — 初始增量核回归模型 `kernelMdl`（默认） | `incrementalRegressionKernel` 模型对象

指定包含已配置 `incrementalRegressionKernel` 模型对象的工作区变量名称。

创建初始模型对象时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果以表形式提供训练数据，预测变量必须是数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对它们进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数目。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `incrementalRegressionKernel` 对象名称 |
| **默认值：** `"kernelMdl"` |

### **为训练好的机器学习模型的状态添加输出端口** — 添加第二个输出端口用于模型状态 `off`（默认） | `on`

选中该复选框以在 IncrementalRegressionKernel Predict 模块中包含输出端口 **CanPredict**。如果在创建 IncrementalRegressionKernel Predict 模块时，工作区中已包含名为 `kernelMdl` 且能够进行预测的增量核回归模型，则此复选框不会出现。或者，您可以通过在 Simulink 工作区中选择 IncrementalRegressionKernel Predict 模块，并在 MATLAB® 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")` 来指定包含输出端口 **CanPredict**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **采样时间（继承时为 –1）** — 用于指定采样时间的选项 `–1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参见采样时间类型 (Simulink)。

默认情况下，IncrementalRegressionKernel Predict 模块根据模型中模块的上下文继承采样时间。

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

指定定点运算的舍入模式。有关详细信息，请参见舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB 舍入函数在掩码字段中输入表达式。

#### 编程用法

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
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出会饱和到该数据类型能够表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型能够表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出在 127 处饱和。类似地，模块输出在最小值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参见排查信号范围错误 (Simulink)。 | 溢出会回绕到该数据类型能够表示的相应值。 | `int8`（有符号 8 位整数）数据类型能够表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件会将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数以防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参见使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **输出数据类型** — yfit 输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **yfit** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参见控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参见使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**： `"Inherit: auto"` |

### **输出数据类型最小值** — 用于范围检查的 yfit 输出最小值 `[]`（默认） | 标量

指定 Simulink 检查的 **yfit** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（参见指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参见指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参见使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**输出数据类型最小值**参数不会使实际 **yfit** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutMin` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **输出数据类型最大值** — 用于范围检查的 yfit 输出最大值 `[]`（默认） | 标量

指定 Simulink 检查的 **yfit** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（参见指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参见指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参见使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**输出数据类型最大值**参数不会使实际 **yfit** 输出饱和或对其进行裁剪。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutMax` |
| **类型**： 字符向量 |
| **值**： `"[]"` | 标量 |
| **默认值**： `"[]"` |

### **核数据类型** — 核计算数据类型 `Inherit: Inherit via internal rule`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定用于高斯核近似计算的参数数据类型。该类型可以直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定核数据类型。该内部规则会选择一种在数值精度、性能和生成代码大小方面进行优化的数据类型，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参见使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**： `KernelDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**： `'Inherit: Inherit via internal rule'` |

### **核数据类型最小值** — 用于范围检查的核计算最小值 `[]`（默认） | 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（参见指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参见指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参见使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最小值**参数不会使实际核计算值饱和或对其进行裁剪。

#### 编程用法

|  |
| --- |
| **模块参数**： `KernelOutMin` |
| **类型**： 字符向量 |
| **值**： `'[]'` | 标量 |
| **默认值**： `'[]'` |

### **核数据类型最大值** — 用于范围检查的核计算最大值 `[]`（默认） | 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（参见指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（参见指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参见使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**核数据类型最大值**参数不会使实际核计算值饱和或对其进行裁剪。

#### 编程用法

|  |
| --- |
| **模块参数**： `KernelOutMax` |
| **类型**： 字符向量 |
| **值**： `'[]'` | 标量 |
| **默认值**： `'[]'` |

### **内积数据类型** — 内积数据类型 `double`（默认） | `Inherit: Inherit via internal rule` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则确定内积数据类型。该内部规则会选择一种在数值精度、性能和生成代码大小方面进行优化的数据类型，同时考虑嵌入式目标硬件的属性。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参见控制信号的数据类型 (Simulink)。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参见使用数据类型助手指定数据类型 (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductDataTypeStr` |
| **类型**: character vector |
| **值**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**: `"Inherit: Inherit via internal rule"` |

### **内积数据类型最小值** — 用于范围检查的内积项最小值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最小值**参数不会饱和或裁剪实际的内积项值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductOutMin` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

### **内积数据类型最大值** — 用于范围检查的内积项最大值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值来执行：

- 对某些模块进行参数范围检查（参见 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（参见 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最大值**参数不会饱和或裁剪实际的内积项值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InnerProductOutMax` |
| **类型**: character vector |
| **值**: `"[]"` | 标量 |
| **默认值**: `"[]"` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Regression / Kernel

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

**在 R2024b 中引入**

## 描述

使用增量核回归模型预测响应

IncrementalRegressionKernel Predict 模块使用训练好的核回归模型预测流式数据的响应，该模型作为 IncrementalRegressionKernel Fit 模块的输出返回。

通过指定包含该对象的工作区变量的名称，将初始核回归模型对象导入 IncrementalRegressionKernel Predict 模块。输入端口 **mdl** 接收一个总线信号，该信号表示拟合到流式数据的增量学习模型。输入端口 **x** 接收一块预测变量数据（观测值），输出端口 **yfit** 返回该数据块的预测响应。可选输出端口 **CanPredict** 返回训练后模型的预测状态。
