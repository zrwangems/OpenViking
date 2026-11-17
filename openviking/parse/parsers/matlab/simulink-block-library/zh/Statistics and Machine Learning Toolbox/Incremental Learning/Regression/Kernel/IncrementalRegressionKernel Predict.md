---
type: simulink-block
title: 'IncrementalRegressionKernel Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Regression / Kernel'
documentation_page: 'incrementalregressionkernelpredict'
documentation_source_path: 'incrementalregressionkernelpredict.html'
language: zh-CN
chinese_source: worker-translation
---

# IncrementalRegressionKernel Predict

## 端口
```yaml
ports:
- name: mdl
  summary: 增量学习模型总线信号
  direction: input
- name: x
  summary: 预测变量数据块 数值矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: yfit
  summary: 预测响应块 浮点向量
  direction: output
  data_types: single | double
- name: CanPredict
  summary: 模型状态 0（false）| 1（true）
  direction: output
```

### 输入

### **mdl** — 增量学习模型总线信号

拟合到流式数据的增量学习模型（`incrementalRegressionKernel`），指定为总线信号（参见 Composite Signals (Simulink)）。

### **x** — 预测变量数据块 数值矩阵

预测变量数据块，指定为数值矩阵。

**注意**

该模块仅支持数值输入预测变量数据。如果您的输入数据包含分类数据，您必须准备分类数据的编码版本。使用 `dummyvar` 将每个分类变量转换为哑变量的数值矩阵。然后，将所有哑变量矩阵和任何其他数值预测变量连接起来。有关更多详细信息，请参见 Dummy Variables。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **yfit** — 预测响应块 浮点向量

预测响应块，以浮点向量形式返回

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内预测响应为零。

**数据类型：** `single` | `double`

### **CanPredict** — 模型状态 `0`（`false`）| `1`（`true`）

用于预测的模型状态，以逻辑值 `0`（`false`）或 `1`（`true`）返回。

**注意**

如果在创建 **mdl** 时指定了估计期，则在估计期内模型状态为 `0`（`false`）。

#### 依赖关系

要启用此端口，请在“模块参数”对话框的**主要**选项卡中选中**为已训练机器学习模型的状态添加输出端口**复选框。
## 参数
```yaml
parameters:
- name: 选择初始机器学习模型
  summary: 初始增量核回归模型 kernelMdl（默认）| incrementalRegressionKernel 模型对象
  group: 主要
  block_parameter: InitialLearner
  type: 字符向量或字符串
  values: incrementalRegressionKernel 对象名称
- name: 为已训练机器学习模型的状态添加输出端口
  summary: 为模型状态添加第二个输出端口 off（默认）| on
  group: 主要
  block_parameter: ShowOutputCanPredict
  type: 字符向量
  values: '"off" | "on"'
- name: Sample time (–1 for inherited)
  summary: 用于指定采样时间的选项 –1（默认）| 标量
  group: 主要
  block_parameter: SystemSampleTime
  type: string scalar or character vector
  values: scalar
  default: '"–1"'
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
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
- name: 输出数据类型
  summary: 'yfit 输出的数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <数据类型表达式>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<数据类型表达式>"'
  default: '"Inherit: auto"'
- name: 输出数据类型最小值
  summary: 用于范围检查的 yfit 输出最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: 输出数据类型最大值
  summary: 用于范围检查的 yfit 输出最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  type: 字符向量
  values: '"[]" | 标量'
  default: '"[]"'
- name: Kernel data type
  summary: '高斯核近似计算的核计算数据类型 Inherit: Inherit via internal rule（默认）| double | single | half | int8 | uint8 | int16 | uint16
    | int32 | int64 | uint64 | uint32 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: KernelDataTypeStr
  type: character vector
  values: '''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''uint64''
    | ''int64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Kernel data type Minimum
  summary: 用于范围检查的核计算最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Kernel data type Maximum
  summary: 用于范围检查的核计算最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: KernelOutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: 内积数据类型
  summary: '内积数据类型 double（默认）| Inherit: Inherit via internal rule | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: 数据类型
  block_parameter: InnerProductDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via internal rule" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: Inherit via internal rule"'
- name: 内积数据类型最小值
  summary: 用于范围检查的内积项最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: 内积数据类型最大值
  summary: 用于范围检查的内积项最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: InnerProductOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **选择初始机器学习模型** — 初始增量核回归模型 `kernelMdl`（默认）| `incrementalRegressionKernel` 模型对象

指定包含已配置的 `incrementalRegressionKernel` 模型对象的工作区变量名称。

创建初始模型对象时，以下限制适用：

- 预测变量数据不能包含分类预测变量（`logical`、`categorical`、`char`、`string` 或 `cell`）。如果您以表格形式提供训练数据，预测变量必须为数值类型（`double` 或 `single`）。要在模型中包含分类预测变量，请在拟合模型之前使用 `dummyvar` 对其进行预处理。
- 初始模型的 `NumPredictors` 属性必须为正整数标量，并且必须等于 **x** 中的预测变量数量。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialLearner` |
| **类型：** 字符向量或字符串 |
| **值：** `incrementalRegressionKernel` 对象名称 |
| **默认：** `"kernelMdl"` |

### **为已训练机器学习模型的状态添加输出端口** — 为模型状态添加第二个输出端口 `off`（默认）| `on`

选中该复选框以在 IncrementalRegressionKernel Predict 模块中包含输出端口 **CanPredict**。如果在创建 IncrementalRegressionKernel Predict 模块时，工作区中已包含名为 `kernelMdl` 且能够进行预测的增量核回归模型，则该复选框不会出现。或者，您可以通过在 Simulink 工作区中选择 IncrementalRegressionKernel Predict 模块，并在 MATLAB® 命令行中输入 `set_param(gcb,ShowOutputCanPredict="on")` 来指定包含输出端口 **CanPredict**。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowOutputCanPredict` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认：** `"off"` |

### **Sample time (–1 for inherited)** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，IncrementalRegressionKernel Predict 模块根据模块在模型中的上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SystemSampleTime` |
| **类型**：string scalar or character vector |
| **值**：scalar |
| **默认值**：`"–1"` |

### 数据类型

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB 舍入函数在掩码字段中输入表达式。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值**：`"Floor"` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

| Action | Rationale | Impact on Overflows | Example |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出回绕到数据类型可以表示的相应值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`"off" | "on"` |
| **默认值**：`"off"` |

#### 数据类型

### **输出数据类型** — yfit 输出的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<数据类型表达式>`

指定 **yfit** 输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如
`Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant**
按钮以显示 **Data Type Assistant**，
它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<数据类型表达式>"` |
| **默认值**：`"Inherit: auto"` |

### **输出数据类型最小值** — 用于范围检查的 yfit 输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的 **yfit** 输出范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化
  可以移除算法代码并影响某些仿真模式的结果，
  例如软件在环（SIL）模式或外部模式。有关详细信息，
  请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**输出数据类型最小值**参数不会饱和
或裁剪实际的 **yfit** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **输出数据类型最大值** — 用于范围检查的 yfit 输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的 **yfit** 输出范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化
  可以移除算法代码并影响某些仿真模式的结果，
  例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**输出数据类型最大值**参数不会饱和
或裁剪实际的 **yfit** 输出。为此，请改用 Saturation (Simulink) 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`"[]"` | 标量 |
| **默认值**：`"[]"` |

### **Kernel data type** — 高斯核近似计算的核计算数据类型 `Inherit: Inherit via internal rule`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定高斯核近似计算的参数数据类型。
可以直接指定类型，也可以表示为数据类型对象，例如
`Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，
模块使用内部规则来确定核数据类型。该内部规则会选择
一种能够优化数值精度、性能和生成代码大小的数据类型，
同时考虑嵌入式目标硬件的属性。该软件
无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant**
按钮以显示 **Data Type Assistant**，
它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelDataTypeStr` |
| **类型**：character vector |
| **值**：`'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Kernel data type Minimum** — 用于范围检查的核计算最小值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的下限值。

Simulink 使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会
  移除算法代码并影响某些仿真模式的结果，例如
  software-in-the-loop (SIL) 模式或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Note**

**Kernel data type Minimum** 参数不会饱和
或裁剪实际的核计算值。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Kernel data type Maximum** — 用于范围检查的核计算最大值 `[]`（默认）| 标量

指定 Simulink 检查的核计算内部变量范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化您从模型生成的代码。此优化可能会
  移除算法代码并影响某些仿真模式的结果，例如 SIL
  或 external mode。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**Note**

**Kernel data type Maximum** 参数不会饱和
或裁剪实际的核计算值。

#### 编程使用

|  |
| --- |
| **模块参数**：`KernelOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **内积数据类型** — 内积数据类型 `double`（默认）| `Inherit: Inherit via internal rule` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定预测响应的内积项的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via internal rule` 时，模块使用内部规则来确定内积数据类型。内部规则选择一种数据类型，在考虑嵌入式目标硬件属性的同时，优化数值精度、性能和生成代码的大小。软件无法始终同时优化效率和数值精度。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InnerProductDataTypeStr` |
| **类型**：character vector |
| **值**：`"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: Inherit via internal rule"` |

### **内积数据类型最小值** — 用于范围检查的内积项最小值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最小值**参数不会饱和或裁剪实际的内积项值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InnerProductOutMin` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |

### **内积数据类型最大值** — 用于范围检查的内积项最大值 `[]`（默认）| 标量

指定 Simulink 检查的内积项范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

**注意**

**内积数据类型最大值**参数不会饱和或裁剪实际的内积项值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InnerProductOutMax` |
| **类型**：character vector |
| **值**：`"[]"` | scalar |
| **默认值**：`"[]"` |
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

IncrementalRegressionKernel Predict 模块使用 IncrementalRegressionKernel Fit 模块输出的已训练核回归模型，为流式数据预测响应。

通过指定包含核回归模型对象的工作区变量名称，将初始核回归模型对象导入 IncrementalRegressionKernel Predict 模块。输入端口 **mdl** 接收一个总线信号，该信号表示拟合到流式数据的增量学习模型。输入端口 **x** 接收一块预测变量数据（观测值），输出端口 **yfit** 返回该数据块的预测响应。可选输出端口 **CanPredict** 返回已训练模型的预测状态。
