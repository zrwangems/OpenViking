---
type: simulink-block
title: 'Detect Drift'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Drift Detection'
documentation_page: 'detectdriftblock'
documentation_source_path: 'detectdriftblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Detect Drift

## 端口

### 输入

### **x** — 输入数据 n×1 数值向量 | 逻辑向量

输入数据，指定为 *n*×1 数值向量，其中 *n* 是观测值数量，或指定为逻辑向量。在模型初始化期间：

- 如果在调用 `incrementalConceptDriftDetector` 时 `InputType` 的值为 `"continuous"`，则 **x** 必须是数值向量。
- 如果在调用 `incrementalConceptDriftDetector` 时 `InputType` 的值为 `"binary"`，则 **x** 可以是逻辑向量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **reset** — 重置信号 数值或 | `0` (`false`) | `1`(`true`)

重置信号，指定为 `0` (`false`) 或 `1`(`true` 或数值标量。当 **reset** 信号为正标量（大于 0）时，漂移检测器重置 `incrementalConceptDriftDetector` 的内部状态，包括 `PreviousDriftStatus` 和 `DriftStatus`。在数据中检测到漂移后，该模块使用用户定义的重置逻辑子系统重置检测器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **w** — 观测权重 n×1 数值向量

观测权重，指定为数值向量。Detect Drift 模块使用 **w** 中的对应值对 **x** 中的观测值进行加权。**w** 的大小必须等于 **x** 中的观测值数量。

不能为使用指数加权移动平均的 Hoeffding's Bounds Drift Detection Method (HDDMW) 提供观测权重。要使用观测权重，请在调用 `incrementalConceptDriftDetector` 时将 `DetectionMethod` 指定为 `"ddm"` 或 `"hddma"`。

#### 依赖关系

要启用此端口，请在 Block Parameters 对话框的 **Main** 选项卡上选中 **Add input port for observation weights** 复选框。

**数据类型：** `single` | `double`
### 输出

### **IsWarm** — 指示模块是否跟踪漂移状态的标志 `0` (`false`) | `1`(`true`)

指示 Detect Drift 模块是否跟踪漂移状态的标志，返回为逻辑 `0` (`false`) 或 `1` (`true`)。

| 值 | 描述 |
| --- | --- |
| `1 (true)` | `incrementalConceptDriftDetector` 对象已预热。因此，该模块在信号输出中跟踪漂移状态。 |
| `0 (false)` | `incrementalConceptDriftDetector` 对象未预热。因此，该模块仅更新内部统计量，不跟踪漂移状态。 |

**数据类型：** `Boolean`

### **status** — 当前漂移状态 `0`（稳定） | `1`（警告） | `2`（漂移）

当前漂移状态，指定为 `0`（稳定，或无漂移）、`1`（漂移警告）或 `2`（检测到漂移）。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要参数

### **Select concept drift detector** — 初始增量概念漂移检测器 `IncCDDetector`（默认） | `incrementalConceptDriftDetector` 对象

指定包含已配置的 `incrementalConceptDriftDetector` 对象的工作区变量名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`DriftDetector` |
| **类型**：character vector or string |
| **值**：`incrementalConceptDriftDetector` object name |
| **默认值**：`"IncCDDetector"` |

### **Add input port for observation weights** — 添加用于观测权重的第三个输入端口 `off`（默认） | `on`

选中该复选框以在 Detect Drift 模块中包含用于观测权重的输入端口 **w**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowInputWeights` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **采样时间（–1 表示继承）** — 用于指定采样时间的选项 `–1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`–1`）。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，Detect Drift 模块根据模型中模块的上下文继承采样时间。

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

指定定点运算的舍入模式。有关更多信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请使用 MATLAB® 舍入函数在掩码字段中输入表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **默认值：** `"Floor"` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

| 操作 | 理由 | 对溢出的影响 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框（`on`）。 | 您的模型可能存在溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出饱和到数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。 |
| 清除此复选框（`off`）。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅排查信号范围错误 (Simulink)。 | 溢出回绕到数据类型可以表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您为模块指定的数据类型。有关更多信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

#### 数据类型

### **Drift status data type** — 漂移状态输出 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>` 的数据类型

指定漂移**状态**输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: auto` 时，模块使用继承数据类型的规则。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`DriftStatusDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Drift status data type Minimum** — 用于范围检查的漂移状态输出最小值 `[]`（默认）| 标量

指定 Simulink 检查的漂移**状态**范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`DriftStatusOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Drift status data type Maximum** — 用于范围检查的漂移状态输出最大值 `[]`（默认）| 标量

指定 Simulink 检查的漂移**状态**范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`DriftStatusOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **Mean data type** — 均值 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>` 的数据类型

指定均值（输入观测值的移动平均值）的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeanDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **均值数据类型最小值** — 用于范围检查的均值最小值 `[]`（默认）| 标量

指定 Simulink 检查的均值范围的下限值。

Simulink 使用最小值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeanOutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **均值数据类型最大值** — 用于范围检查的均值最大值 `[]`（默认）| 标量

指定 Simulink 检查的均值范围的上限值。

Simulink 使用最大值执行以下操作：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeanOutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 标量 |
| **默认值**：`'[]'` |

### **方差数据类型** — 方差的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定方差（输入观测值的滑动方差）的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数**：`VarianceDataTypeStr` |
| **类型**：字符向量或字符串 |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Variance data type Minimum** — 用于范围检查的方差最小值 `[]`（默认）| 标量

指定 Simulink 检查的方差范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`VarianceOutMin` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Variance data type Maximum** — 用于范围检查的方差最大值 `[]`（默认）| 标量

指定 Simulink 检查的方差范围的上限值。

Simulink 使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`VarianceOutMax` |
| **类型**：character vector |
| **值**：`'[]'` | scalar |
| **默认值**：`'[]'` |

### **Weights sum data type** — 权重和的数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定权重和（加权输入观测值的移动和）的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

有关数据类型的详细信息，请参阅 Control Data Types of Signals (Simulink)。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`WeightsSumDataTypeStr` |
| **类型**：character vector or string |
| **值**：`"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **默认值**：`"Inherit: auto"` |

### **Weights sum data type Minimum** — 用于范围检查的权重和最小值 `[]`（默认）| 标量

指定 Simulink 检查的权重和范围的下限值。

Simulink 使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码优化。此优化可能会移除算法代码，并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `WeightsSumOutMin` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认值**: `'[]'` |

### **权重和数据类型最大值** — 用于范围检查的权重和最大值 `[]`（默认）| 标量

指定 Simulink 检查的权重和范围的上限值。

Simulink 使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式的结果，例如软件在环（SIL）模式或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 程序化使用

|  |
| --- |
| **模块参数**: `WeightsSumOutMax` |
| **类型**: 字符向量 |
| **值**: `'[]'` | 标量 |
| **默认值**: `'[]'` |

## 所属库

Statistics and Machine Learning Toolbox / Incremental Learning / Drift Detection

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

使用新数据更新漂移检测器状态和漂移状态

Detect Drift 模块在给定新数据时更新漂移检测器的内部统计量和漂移状态。

通过指定包含已初始化的增量概念漂移检测器对象（`incrementalConceptDriftDetector`）的工作区变量名称，将该对象导入模块。输入端口 **x** 接收用于评估漂移的数据流。输入端口 **reset** 接收重置漂移检测器内部状态的信号。输出端口 **IsWarm** 返回一个值，指示漂移检测器是否已预热，即是否正在跟踪漂移状态。输出端口 **status** 返回当前漂移状态。可选输入端口 **w** 接收观测权重。
