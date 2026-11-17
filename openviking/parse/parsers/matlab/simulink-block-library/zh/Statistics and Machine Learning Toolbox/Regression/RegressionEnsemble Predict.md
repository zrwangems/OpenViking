---
type: simulink-block
title: 'RegressionEnsemble Predict'
family: 'regression'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression'
documentation_page: 'regressionensemblepredict'
documentation_source_path: 'regressionensemblepredict.html'
language: zh-CN
chinese_source: worker-translation
---

# RegressionEnsemble Predict

## 端口

### 输入

### **x** — 预测变量数据行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量顺序必须与训练 **选择训练好的机器学习模型** 指定的模型的预测变量顺序相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应标量

预测响应，以标量形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **选择训练好的机器学习模型** — 回归集成模型 `ensMdl`（默认） | `RegressionEnsemble` 对象 | `RegressionBaggedEnsemble` 对象 | `CompactRegressionEnsemble` 对象

指定包含 `RegressionEnsemble` 对象、`RegressionBaggedEnsemble` 对象或 `CompactRegressionEnsemble` 对象的工作区变量的名称。

使用 `fitrensemble` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果在表中提供训练数据，则预测变量必须为数值（`double` 或 `single`）。此外，不能使用 `CategoricalPredictors` 名称-值参数。若要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- `ResponseTransform` 名称-值参数的值必须为 `'none'`（默认）。
- 不能对树弱学习器使用代理拆分，也就是说，当使用 `templateTree` 函数定义树弱学习器时，`Surrogate` 名称-值参数的值必须为 `'off'`（默认）。

#### 编程用法

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `RegressionEnsemble` 对象 | `RegressionBaggedEnsemble` 对象 | `CompactRegressionEnsemble` 对象 |
| **默认值：** `'ensMdl'` |

### 数据类型

#### 定点运算参数

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

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
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误 (Simulink)。 | 溢出回绕到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

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

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号数据类型 (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **输出数据类型最小值** — 用于范围检查的 yfit 输出的最小值 `[]`（默认） | 标量

指定 Simulink® 检查的 **yfit** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**输出数据类型最小值** 参数不会饱和或裁剪实际 **yfit** 信号。若要这样做，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **输出数据类型最大值** — 用于范围检查的 yfit 输出的最大值 `[]`（默认） | 标量

指定 Simulink 检查的 **yfit** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**输出数据类型最大值** 参数不会饱和或裁剪实际 **yfit** 信号。若要这样做，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **弱学习器数据类型** — 弱学习器输出的数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定弱学习器输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅控制信号数据类型 (Simulink)。

单击 **Show data type assistant** 按钮  以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`WeakLearnerDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

### **弱学习器数据类型最小值** — 用于范围检查的弱学习器输出的最小值 `[]`（默认） | 标量

指定 Simulink 检查的弱学习器输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式的结果，例如软件在环 (SIL) 模式或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**弱学习器数据类型最小值** 参数不会饱和或裁剪实际的弱学习器输出信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`WeakLearnerOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **弱学习器数据类型最大值** — 用于范围检查的弱学习器输出的最大值 `[]`（默认） | 标量

指定 Simulink 检查的弱学习器输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值 (Simulink)）。
- 仿真范围检查（请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)）。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

**注意**

**弱学习器数据类型最大值** 参数不会饱和或裁剪实际的弱学习器输出信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`WeakLearnerOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

## 所属库

Statistics and Machine Learning Toolbox / Regression

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

**在 R2021a 中引入**

## 描述

使用回归决策树集成预测响应

RegressionEnsemble Predict 模块使用决策树集成（`RegressionEnsemble`、`RegressionBaggedEnsemble` 或 `CompactRegressionEnsemble`）预测响应。

通过指定包含已训练回归对象的工作区变量的名称，将已训练回归对象导入模块。输入端口 **x** 接收一个观测（预测变量数据），输出端口 **yfit** 返回该观测的预测响应。
