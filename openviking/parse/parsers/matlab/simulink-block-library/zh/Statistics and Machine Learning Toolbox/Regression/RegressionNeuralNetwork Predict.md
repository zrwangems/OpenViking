---
type: simulink-block
title: 'RegressionNeuralNetwork Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression'
documentation_page: 'regressionneuralnetworkpredict'
documentation_source_path: 'regressionneuralnetworkpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# RegressionNeuralNetwork Predict

## 端口

### 输入

### **x** — 预测变量数据 行向量 | 列向量

预测变量数据，指定为一个观测的行向量或列向量。

**x** 中的变量顺序必须与训练 **Select trained machine learning model** 所指定模型的预测变量顺序相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应 标量

预测响应，以标量形式返回。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Select trained machine learning model** — 神经网络回归模型 `nnetMdl`（默认）| `RegressionNeuralNetwork` | `CompactRegressionNeuralNetwork`

指定包含 `RegressionNeuralNetwork` 对象或 `CompactRegressionNeuralNetwork` 对象的工作区变量名称。

当您使用 `fitrnet` 训练模型时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果您在表中提供训练数据，预测变量必须是数值型（`double` 或 `single`）。此外，您不能使用 `CategoricalPredictors` 名称-值参数。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 响应数据必须仅包含一个响应变量。不支持多响应回归。

#### 编程使用

|  |
| --- |
| **模块参数**：`TrainedLearner` |
| **类型**：workspace variable |
| **值**：`RegressionNeuralNetwork` object | `CompactRegressionNeuralNetwork` object |
| **默认值**：`'nnetMdl'` |

### 数据类型

#### 定点运算参数

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值**：`"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中显式添加饱和保护。 | 溢出饱和到该数据类型所能表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到该数据类型所能表示的相应值。 | `int8`（有符号 8 位整数）数据类型所能表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生非预期的结果。例如，模块结果为 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

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

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output data type Maximum** 参数不会饱和或裁剪实际的 **yfit** 信号。如需执行此操作，请改用 Saturation (Simulink) 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Output layer data type** — 最终全连接层的数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出层的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定输出数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时优化数值精度、性能和生成代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputLayerDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output layer data type Minimum** — 最终全连接层的最小值 `[]`（默认）| 标量

指定 Simulink 检查的输出层内部变量范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output layer data type Minimum** 参数不会对输出层值信号进行饱和或裁剪。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputLayerOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Output layer data type Maximum** — 最终全连接层的最大值 `[]`（默认）| 标量

指定 Simulink 检查的输出层内部变量范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Output layer data type Maximum** 参数不会对输出层值信号进行饱和或裁剪。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputLayerOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Layer 1 data type** — 第一个全连接层的数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定第一层的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成的代码大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 提示

训练好的神经网络可以有多个全连接层，不包括输出层。

- 你可以为前 10 层中的每一层指定数据类型。为每一层指定数据类型 **Layer n data type**。第一层的数据类型为 **Layer 1 data type**，第二层的数据类型为 **Layer 2 data type**，依此类推。
- 你可以使用数据类型 **Additional layer(s) data type** 为第 11 层到第 *k* 层指定数据类型，其中 *k* 是总层数。**Additional layer(s) data type** 的 **Block Parameter** 为 `Layer11DataTypeStr`。
- 数据类型 **Layer n data type** 和 **Additional layer(s) data type** 可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。这些数据类型支持与 **Layer 1 data type** 相同的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Layer1DataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Layer 1 data type Minimum** — 第一个全连接层的最小值 `[]`（默认）| 标量

指定 Simulink 检查的第一层内部变量范围的下限值。

Simulink 使用该最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可以移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Layer 1 data type Minimum** 参数不会饱和或裁剪第一层值信号。

#### 提示

训练好的神经网络可以有多个全连接层，不包括输出层。

- 你可以为前 10 层中的每一层指定 Simulink 检查的各自内部变量范围的下限值。为每一层指定下限值 **Layer n minimum**。第一层的最小值为 **Layer 1 minimum**，第二层的最小值为 **Layer 2 minimum**，依此类推。
- 你可以使用 **Additional layer(s) minimum** 为第 11 层到第 *k* 层指定下限值，其中 *k* 是总层数。**Additional layer(s) minimum** 的 **Block Parameter** 为 `Layer11OutMin`。
- **Layer n minimum** 和 **Additional layer(s) minimum** 支持与 **Layer 1 minimum** 相同的值。

#### 编程用法

|  |
| --- |
| **模块参数**：`Layer1OutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Layer 1 data type Maximum** — 第一个全连接层的最大值 `[]`（默认）| 标量

指定 Simulink 检查的第一层内部变量范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**Layer 1 data type Maximum** 参数不会饱和或裁剪第一层值信号。

#### 提示

一个训练好的神经网络可以有多个全连接层，不包括输出层。

- 您可以为前 10 层分别指定 Simulink 检查的每个单独层内部变量范围的上限值。为每一层指定上限值 **Layer n maximum**。第一层的最大值是 **Layer 1 maximum**，第二层的最大值是 **Layer 2 maximum**，依此类推。
- 您可以使用 **Additional layer(s) maximum** 为第 11 层到第 *k* 层指定上限值，其中 *k* 是总层数。**Additional layer(s) maximum** 的 **Block Parameter** 为 `Layer11OutMax`。
- **Layer n maximum** 和 **Additional layer(s) maximum** 支持与 **Layer 1 maximum** 相同的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Layer1OutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
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

**在 R2021b 中引入**

## 描述

使用神经网络回归模型预测响应

RegressionNeuralNetwork Predict 模块使用神经网络回归对象（`RegressionNeuralNetwork` 或 `CompactRegressionNeuralNetwork`）预测响应。

通过指定包含该对象的工作区变量名称，将训练好的回归对象导入模块。输入端口 **x** 接收一个观测值（预测变量数据），输出端口 **yfit** 返回该观测值的预测响应。
