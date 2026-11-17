---
type: simulink-block
title: 'Discrete Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'discretefilter'
documentation_source_path: '../simulink/slref/discretefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Filter

## 端口

### 输入

### **u** — 输入信号 标量 | 向量 | 矩阵

滤波器的输入信号，指定为标量、向量或矩阵。

当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，该模块支持可变大小输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。*（自 R2024a 起）*

#### 依赖关系

此端口的名称取决于您为分子系数、分母系数和初始状态指定的来源。当您将 **Numerator**、**Denominator** 和 **Initial states** 设置为 `Dialog` 时，只有一个输入端口，且该端口无标签。当您将 **Numerator**、**Denominator** 或 **Initial states** 设置为 `Input port` 时，此端口标记为 **u**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — 分子系数 标量 | 向量

离散滤波器的分子系数，以 *z* 的降幂指定。使用行向量指定单个分子多项式的系数。

#### 依赖关系

要启用此端口，请将 **Numerator Source** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — 分母系数 标量 | 向量

离散滤波器的分母系数，以 *z* 的降幂指定。使用行向量指定单个分母多项式的系数。

#### 依赖关系

要启用此端口，请将 **Denominator Source** 设置为 `Input port`。

要将 **Denominator Source** 设置为 `Input port`，请选中 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。该模块忽略前导分母系数值 a0 并将其替换为 1。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **External reset** — 外部复位信号 标量

外部复位信号，指定为标量。当指定的触发事件发生时，该模块将状态重置为其初始条件。

**提示**

此端口的图标根据 **External reset** 参数的值而变化。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为 `Rising`、`Falling`、`Either`、`Level` 或 `Level hold`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **x0** — 初始状态 标量 | 向量 | 矩阵

初始状态，指定为标量、向量或矩阵。有关指定状态的详细信息，请参阅 Specifying Initial States。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed`，并将 **Initial states** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Port\_1** — 滤波后的输出信号 标量 | 向量 | 矩阵

滤波后的输出信号。输出维度等于输入维度，除非您为 **Numerator coefficients** 参数指定滤波器抽头的矩阵。在这种情况下，输出维度取决于您指定的不同滤波器抽头组的数量。

当您将 **Sample time** 设置为 `-1` 时，输出信号的采样时间与输入信号 **u** 的采样时间相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### 主要

### **Filter structure** — 滤波器结构 `Direct form II`（默认）| `Direct form I transposed` | `Direct form I` | `Direct form II transposed`

指定离散 IIR 滤波器结构。

#### 依赖关系

要使用除 `Direct form II` 以外的任何滤波器结构，您必须拥有可用的 DSP System Toolbox 许可证。

#### 编程用法

|  |
| --- |
| **模块参数：** `FilterStructure` |
| **类型：** 字符向量 |
| **值：** `'Direct form II' | 'Direct form I transposed' | 'Direct form I' | 'Direct form II transposed'` |
| **默认值：** `'Direct form II'` |

### **Numerator Source** — 分子系数来源 `Dialog`（默认）| `Input port`

将分子系数的来源指定为 `Dialog` 或 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumeratorSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认值：** `'Dialog'` |

### **Numerator Value** — 分子系数 `[1]`（默认）| 标量 | 向量 | 矩阵

将离散滤波器的分子系数指定为 *z* 的降幂。使用行向量指定单个分子多项式的系数。要指定多个滤波器的系数，请指定系数矩阵，其中每一行代表一组不同的滤波器抽头。要实现多个滤波器，**Filter structure** 必须为 `Direct form II`，**Input processing** 必须为 `Elements as channels (sample based)`，且输入必须为标量。

#### 依赖关系

要启用此参数，请将 **Numerator Source** 设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Numerator` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'[1]'` |

### **Denominator Source** — 分母系数来源 `Dialog`（默认）| `Input port`

将分母系数的来源指定为 `Dialog` 或 `Input port`。

要将 **Denominator Source** 设置为 `Input port`，请选中 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DenominatorSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认值：** `'Dialog'` |

### **Denominator Value** — 分母系数 `[1 0.5]`（默认）| 向量

将离散滤波器的分母系数指定为 *z* 的降幂。使用行向量指定单个分母多项式的系数。

当您选中 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数时，如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

#### 依赖关系

要启用此参数，请将 **Denominator Source** 设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Denominator` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'[1 0.5]'` |

### **Initial states Source** — 初始状态来源 `Dialog`（默认）| `Input port`

将初始状态的来源指定为 `Dialog` 或 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialStatesSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认值：** `'Dialog'` |

### **Initial states Value** — 初始滤波器状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅 Specifying Initial States。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Direct form II` 或 `Direct form II transposed`，并将 **Initial states Source** 设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

或者，使用 `IC`。

### **Initial states on numerator side** — 初始分子状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始分子滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅 Specifying Initial States。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

### **Initial states on denominator side** — 初始分母状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始分母滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅 Specifying Initial States。

#### 依赖关系

要启用此端口，请将 **Filter structure** 设置为 `Direct form I` 或 `Direct form I transposed`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialDenominatorStates` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

### **External reset** — 外部状态复位 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态重置为初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当复位信号在当前时间步为非零时 - 当复位信号值从前一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当复位信号在当前时间步为非零时复位 |

#### 编程用法

|  |
| --- |
| **模块参数**： `ExternalReset` |
| **类型**： 字符向量 |
| **值**： `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**： `'None'` |

### **Input processing** — 基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理。

- `Elements as channels (sample based)` — 将输入的每个元素作为独立通道处理。
- `Columns as channels (frame based)` — 将输入的每一列作为独立通道处理。

#### 依赖关系

基于帧的处理需要 DSP System Toolbox 许可证。

有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputProcessing` |
| **类型：** 字符向量 |
| **值：** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **默认值：** `'Elements as channels (sample based)'` |

### **Optimize by skipping divide by leading denominator coefficient (a0)** — 跳过除以 a0 `off`（默认）| `on`

当您选中此复选框时，该模块在仿真或生成的代码中都不会除以 *a0*。此参数可优化您的代码。如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

如果从输入端口 **Den** 指定分母系数，则必须选中 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。当您选中此复选框时，该模块忽略前导分母系数 *a0* 并将其替换为 1。

当您清除此复选框时，该模块在仿真期间完全可调。它在仿真和代码生成中都会除以 *a0*。

#### 编程用法

|  |
| --- |
| **模块参数：** `a0EqualsOne` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **View Filter Response** — 查看滤波器响应 按钮

单击此按钮可打开 Filter Visualization Tool（`fvtool` (DSP System Toolbox)）并显示模块对话框中定义的滤波器的滤波器响应。

#### 依赖关系

要启用此参数，请将 **Numerator Source** 和 **Denominator Source** 参数设置为 `Dialog`。

仅当您拥有有效的 DSP System Toolbox 许可证时，此参数才会出现。

### 数据类型

### **State** — 状态数据类型 `Inherit: Same as input`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定状态数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程用法

|  |
| --- |
| **模块参数：** `StateDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Same as input'` |

### **Numerator coefficients** — 分子系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置有符号整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumCoefDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **Numerator coefficient minimum** — 分子系数的最小值 `[]`（默认）| 标量

指定分子系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数：** `NumCoefMin` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Numerator coefficient maximum** — 分子系数的最大值 `[]`（默认）| 标量

指定分子系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数：** `NumCoefMax` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Numerator product output** — 分子乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的乘积输出数据类型。
您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumProductDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Numerator accumulator** — 分子累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的累加器数据类型。您
可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumAccumDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator coefficients** — 分母系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数数据类型。您可以将此
参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置整数，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenCoefDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator coefficient minimum** — 分母系数最小值 `[]`（默认）| 标量

指定分母系数可以具有的最小值。默认
值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`DenCoefMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Denominator coefficient maximum** — 分母系数最大值 `[]`（默认）| 标量

指定分母系数可以具有的最大值。默认
值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`DenCoefMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Denominator product output** — 分母乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数的乘积输出数据类型。
您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenProductDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator accumulator** — 分母累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数的累加器数据类型。
您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenAccumDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal
  rule`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output minimum** — 输出最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。默认值
为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Output maximum** — 输出最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。默认值
为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Multiplicand data type** — 被乘数数据类型 `Inherit: Same as input`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定被乘数数据类型。您可以将此参数
设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as input`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据
属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Direct form I
transposed`

#### 编程使用

|  |
| --- |
| **模块参数**：`MultiplicandDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Same as input'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的数据类型设置，防止其被
Fixed-Point Tool 和 Fixed-Point Advisor 更改。有关详细信息，
请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。
有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：character vector |
| **值**：`'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值**：`'Floor'` |

### **Saturate on integer overflow** — 溢出操作方式 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型所能表示的
  最小值或最大值。
- `off` — 溢出回绕到数据类型所能表示的
  相应值。

例如，有符号 8 位整数 `int8`
能表示的最大值是 127。任何大于此最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值
  -128。
- 清除此参数时，软件将导致溢出的值解释为
  `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时是 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中
  获得显式饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于
  避免过度指定模块如何处理超出范围的信号。有关更多
  信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，
  代码生成器不会生成饱和
  代码。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### State Attributes

### **State name** — 为每个状态分配唯一名称 `' '`（默认）| `'position'` | `{'a', 'b', 'c'}` | `a` | ...

为每个状态分配唯一名称。如果此字段为空（`'
'`），则不进行名称分配。

- 要为单个状态分配名称，请在
  引号之间输入名称，例如，`'position'`。
- 要为多个状态分配名称，请输入以逗号分隔的
  列表并用花括号括起，例如，`{'a', 'b',
  'c'}`。每个名称必须唯一。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。该
  变量可以是字符向量、元胞数组或
  结构体。

#### 限制

- 状态名称仅适用于所选模块。
- 状态数必须能被状态名称数
  整除。
- 您可以指定的名称数少于状态数，但不能
  指定的名称数多于状态数。

  例如，您可以在具有
  四个状态的系统中指定两个名称。第一个名称适用于前两个状态，
  第二个名称适用于后两个状态。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Direct form
II`。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateName` |
| **类型**：character vector |
| **值**：`' '` | user-defined |
| **默认值**：`' '` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框可要求状态名称解析为
Simulink 信号对象。

#### 依赖关系

要启用此参数，请将 **Filter
structure** 设置为 `Direct form
II` 并为 **State
name** 指定值。仅当您将
模型配置参数 **Signal resolution**
设置为 `None` 以外的值时，此参数才会出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Discrete DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持有符号定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

Discrete Filter 模块接受并输出 Simulink 支持的任何有符号数值数据类型的实数和复数信号。该模块对分子和分母系数支持相同的类型。

分子和分母系数必须具有相同的复/实性。它们可以具有不同的字长和小数长度。

以下图示展示了定点信号在 Discrete Filter 模块内使用的滤波器结构和数据类型。

当您选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数时，该模块会省略虚线除法。

## 版本历史

**在 R2006a 之前推出**

### R2024b: 查看滤波器响应

点击 **View Filter Response** 按钮，以可视化您在模块对话框中指定的滤波器的频率响应。

### R2024a: Discrete Filter 模块支持可变大小输入信号

当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，Discrete Filter 模块支持可变大小输入信号。

当输入为可变大小信号时，您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。

### R2023b: **Sample time** 参数的条件显示

Discrete Filter 模块默认不再在模块参数对话框中显示 **Sample time** 参数。仅当您在命令行或现有模型中将采样时间设置为非默认值（`-1`）时，该参数才可见。有关详细信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

## 描述

对无限脉冲响应 (IIR) 滤波器进行建模

Discrete Filter 模块使用指定的数字 IIR 滤波器独立地对输入信号的每个通道进行滤波。您可以将滤波器结构指定为 `Direct form I`、`Direct form I transposed`、`Direct form II` 或 `Direct form II transposed`。该模块实现具有固定系数的静态滤波器。您可以调整这些静态滤波器的系数。

此模块随时间独立地对输入信号的每个通道进行滤波。**Input processing** 参数允许您指定模块如何处理输入的每个元素。您可以指定将输入元素视为独立通道（基于样本的处理），或将输入的每一列视为独立通道（基于帧的处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

输出维度等于输入维度，除非您为 **Numerator coefficients** 参数指定滤波器抽头矩阵。当您这样做时，输出维度取决于您指定的不同滤波器抽头组数。

使用 **Numerator coefficients** 参数指定离散滤波器分子多项式的系数。使用 **Denominator coefficients** 参数指定函数分母多项式的系数。**Denominator coefficients** 参数必须是系数向量。

按 *z-1* 的升幂指定分子和分母多项式的系数。Discrete Filter 模块允许您使用 *z-1*（延迟算子）中的多项式来表示离散系统。信号处理工程师通常使用此方法。相反，Discrete Transfer Fcn 模块允许您使用 *z* 中的多项式来表示离散系统。控制工程师通常使用此方法。当分子和分母多项式长度相同时，这两种方法是相同的。

### 指定初始状态

在 **Dialog parameters** 和 **Input port(s)** 模式下，模块默认将内部滤波器状态初始化为零，这相当于假设过去的输入和输出为零。您可以选择使用 **Initial states** 参数为滤波器延迟指定非零初始状态。

要确定必须指定的初始状态值的数量以及如何指定它们，请参阅下面关于有效初始状态和延迟元素数量（滤波器状态）的表格。**Initial states** 参数可以采用下表中描述的四种形式之一。

**有效初始状态**

| 初始状态 | 示例 | 描述 |
| --- | --- | --- |
| 标量 | `5` 每个通道的每个延迟元素都设置为 `5`。 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量   （用于将相同的延迟元素应用于每个通道） | 对于具有两个延迟元素的滤波器：[*d1**d2*] 所有通道的延迟元素为 d1 和 d2。 | 每个向量元素为相应的延迟元素指定唯一的初始条件。模块将相同的初始条件向量应用于输入信号的每个通道。向量长度必须等于滤波器中的延迟元素数量（在表 延迟元素数量（滤波器状态）中指定）。 |
| 向量或矩阵   （用于将不同的延迟元素应用于每个通道） | 对于三通道输入信号和具有两个延迟元素的滤波器：  [*d*1*d2**D1**D2**d1**d2*] 或    [d1D1d1d2D2d2]    - 通道 1 的延迟元素是   *d1* 和   *d2*。 - 通道 2 的延迟元素是   *D1* 和   *D2*。 - 通道 3 的延迟元素是   *d1* 和   *d2*。 | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件：  - 向量长度必须等于输入通道数与滤波器中的延迟元素数量（在表 延迟元素数量（滤波器状态）中指定）的乘积。 - 矩阵的行数必须与滤波器中的延迟元素数量（在表 延迟元素数量（滤波器状态）中指定）相同，并且必须为输入信号的每个通道包含一列。 |
| 空矩阵 | `[ ]` 每个通道的每个延迟元素都设置为 `0`。 | 空矩阵 `[]` 等效于将 **Initial conditions** 参数设置为标量值 `0`。 |

每个输入通道的延迟元素（滤波器状态）数量取决于滤波器结构，如下表所示。

**延迟元素数量（滤波器状态）**

| 滤波器结构 | 每个通道的延迟元素数量 |
| --- | --- |
| `Direct form I   Direct form I transposed` | - `number of zeros - 1` - `number of poles - 1` |
| `Direct form II   Direct form II transposed` | `max(number of zeros, number of poles)-1` |

以下表格描述了不同输入大小和不同通道数下的有效初始状态，具体取决于您将 **Input processing** 参数设置为基于帧还是基于样本。

**基于帧的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 列向量（*K*×1） - 无方向向量（*K*） | 1 | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） | - 标量 - 列向量（*M*×1） |
| - 行向量（1×*N*） - 矩阵（*K*×*N*） | *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×*N*） | - 标量 - 矩阵（*M*×*N*） |

**基于样本的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 无方向标量 | 1 | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） |
| - 行向量（1×*N*） - 列向量（*N*×1） - 无方向向量（*N*） | *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×*N*） | - 标量 |
| - 矩阵（*K*×*N*） | *K* × *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×(*K*×*N*)） | - 标量 |

当 **Initial states** 为标量时，模块将所有滤波器状态初始化为相同的标量值。输入 `0` 将所有状态初始化为零。当 **Initial states** 为向量或矩阵时，每个向量或矩阵元素指定唯一的初始状态。此唯一状态对应于相应通道中的延迟元素：

- 向量长度必须等于滤波器中的延迟元素数量，`M = max(number of zeros, number of poles)`。
- 矩阵的行数必须与滤波器中的延迟元素数量相同，`M = max(number of zeros, number of poles)`。矩阵还必须为输入信号的每个通道包含一列。

初始滤波器输出 *y1*、初始输入 *u1* 和初始状态 [*x1*, *x2*] 之间的关系由以下方程给出。

y1=b1[(u1−a2x1−a3x2)a1]+b2x1+b3x2

其中，

- *b1*、*b2* 和 *b3* 是离散滤波器的分子系数。
- *a1*、*a2* 和 *a3* 是离散滤波器的分母系数。
