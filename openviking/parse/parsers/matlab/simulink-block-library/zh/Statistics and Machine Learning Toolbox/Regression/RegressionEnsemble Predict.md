---
type: simulink-block
title: 'RegressionEnsemble Predict'
family: 'stats'
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
```yaml
ports:
- name: x
  summary: 预测变量数据 行向量 | 列向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: yfit
  summary: 预测响应 标量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量必须与训练 **Select trained machine learning model** 所指定模型的预测变量具有相同的顺序。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应 标量

预测响应，以标量形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Select trained machine learning model
  summary: 回归集成模型 ensMdl（默认）| RegressionEnsemble 对象 | RegressionBaggedEnsemble 对象 | CompactRegressionEnsemble 对象
  group: 主要
  block_parameter: TrainedLearner
  type: 工作区变量
  values: RegressionEnsemble 对象 | RegressionBaggedEnsemble 对象 | CompactRegressionEnsemble 对象
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: 字符向量
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Output data type
  summary: 'yfit 输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Output data type Minimum
  summary: 用于范围检查的 yfit 输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Output data type Maximum
  summary: 用于范围检查的 yfit 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Weak learner data type
  summary: '弱学习器输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: WeakLearnerDataTypeStr
  type: character vector
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32''
    | ''uint32'' | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: auto'''
- name: Weak learner data type Minimum
  summary: 用于范围检查的弱学习器输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: WeakLearnerOutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Weak learner data type Maximum
  summary: 用于范围检查的弱学习器输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: WeakLearnerOutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
```

### 主要

### **Select trained machine learning model** — 回归集成模型 `ensMdl`（默认）| `RegressionEnsemble` 对象 | `RegressionBaggedEnsemble` 对象 | `CompactRegressionEnsemble` 对象

指定包含 `RegressionEnsemble` 对象、`RegressionBaggedEnsemble` 对象或 `CompactRegressionEnsemble` 对象的工作区变量名称。

当您使用 `fitrensemble` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量
  （`logical`、`categorical`、`char`、
  `string` 或 `cell`）。如果您在表中提供训练数据，预测变量必须是数值型（`double` 或 `single`）。
  此外，您不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- `ResponseTransform` 名称-值参数的值必须为
  `'none'`（默认）。
- 您不能对树弱学习器使用代理分裂，也就是说，当您使用 `templateTree` 函数定义树弱学习器时，`Surrogate` 名称-值
  参数的值必须为 `'off'`（默认）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TrainedLearner` |
| **类型：** 工作区变量 |
| **值：** `RegressionEnsemble` 对象 | `RegressionBaggedEnsemble` 对象 | `CompactRegressionEnsemble` 对象 |
| **默认：** `'ensMdl'` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认：** `"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中显式添加饱和保护。 | 溢出饱和到数据类型所能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型所能表示的相应值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果为 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您为模块指定的数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **Output data type** — yfit 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定 **yfit** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Output data type Minimum** — 用于范围检查的 yfit 输出最小值 `[]`（默认）| 标量

指定 Simulink® 检查的 **yfit** 输出范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output data type Minimum** 参数不会饱和或裁剪实际的 **yfit** 信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Output data type Maximum** — 用于范围检查的 yfit 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **yfit** 输出范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output data type Maximum** 参数不会饱和或裁剪实际的 **yfit** 信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Weak learner data type** — 弱学习器输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定弱学习器输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`WeakLearnerDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

### **Weak learner data type Minimum** — 用于范围检查的弱学习器输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的弱学习器输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Weak learner data type Minimum** 参数不会饱和或裁剪实际的弱学习器输出信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`WeakLearnerOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Weak learner data type Maximum** — 用于范围检查的弱学习器输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的弱学习器输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Weak learner data type Maximum** 参数不会饱和或裁剪实际的弱学习器输出信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`WeakLearnerOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |
## 所属库

Statistics and Machine Learning Toolbox / Regression

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2021a 中引入**

## 描述

使用决策树集成进行回归预测

RegressionEnsemble Predict 模块使用决策树集成（`RegressionEnsemble`、`RegressionBaggedEnsemble` 或 `CompactRegressionEnsemble`）预测响应。

通过指定包含已训练回归对象的工作区变量名称，将该对象导入模块。输入端口 **x** 接收一个观测值（预测变量数据），输出端口 **yfit** 返回该观测值的预测响应。
