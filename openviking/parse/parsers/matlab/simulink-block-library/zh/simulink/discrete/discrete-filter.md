---
type: simulink-block
title: 'Discrete Filter'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discrete'
documentation_page: 'discretefilter'
documentation_source_path: 'slref/discretefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Filter

## 端口

### 输入

### **u** — 输入信号 标量 | 向量 | 矩阵

要滤波的输入信号，指定为标量、向量或矩阵。

当您将 **输入处理** 参数设置为 `Columns as channels (frame based)` 时，该模块支持可变大小输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。*（自 R2024a 起）*

#### 依赖关系

此端口的名称取决于您为分子系数、分母系数和初始状态指定的来源。当您将 **分子**、**分母** 和 **初始状态** 设置为 `Dialog` 时，只有一个输入端口，且该端口未标记。当您将 **分子**、**分母** 或 **初始状态** 设置为 `Input port` 时，此端口标记为 **u**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — 分子系数 标量 | 向量

离散滤波器的分子系数，按 *z* 的降幂指定。使用行向量指定单个分子多项式的系数。

#### 依赖关系

要启用此端口，请将 **分子源** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — 分母系数 标量 | 向量

离散滤波器的分母系数，按 *z* 的降幂指定。使用行向量指定单个分母多项式的系数。

#### 依赖关系

要启用此端口，请将 **分母源** 设置为 `Input port`。

要将 **分母源** 设置为 `Input port`，请选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。该模块忽略前导分母系数值 a0，并将其替换为 1。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **External reset** — 外部复位信号 标量

外部复位信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据 **外部复位** 参数的值而变化。

#### 依赖关系

要启用此端口，请将 **外部复位** 设置为 `Rising`、`Falling`、`Either`、`Level` 或 `Level hold`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **x0** — 初始状态 标量 | 向量 | 矩阵

初始状态，指定为标量、向量或矩阵。有关指定状态的更多信息，请参阅指定初始状态。

#### 依赖关系

要启用此端口，请将 **滤波器结构** 设置为 `Direct form II` 或 `Direct form II transposed`，并将 **初始状态** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **Port_1** — 滤波后的输出信号 标量 | 向量 | 矩阵

滤波后的输出信号。输出维度等于输入维度，除非您为 **分子系数** 参数指定滤波器抽头矩阵。在这种情况下，输出维度取决于您指定的不同滤波器抽头集的数量。

当您将 **采样时间** 设置为 `-1` 时，输出信号的采样时间与输入信号 **u** 的采样时间相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### 主要

### **滤波器结构** — 滤波器结构 `Direct form II`（默认）| `Direct form I transposed` | `Direct form I` | `Direct form II transposed`

指定离散 IIR 滤波器结构。

#### 依赖关系

要使用除 `Direct form II` 以外的任何滤波器结构，您必须拥有可用的 DSP System Toolbox 许可证。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterStructure` |
| **类型：** character vector |
| **值：** `'Direct form II' | 'Direct form I transposed' | 'Direct form I' | 'Direct form II transposed'` |
| **默认：** `'Direct form II'` |

### **分子源** — 分子系数源 `Dialog`（默认）| `Input port`

将分子系数的源指定为 `Dialog` 或 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumeratorSource` |
| **类型：** character vector |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **分子值** — 分子系数 `[1]`（默认）| 标量 | 向量 | 矩阵

将离散滤波器的分子系数指定为 *z* 的降幂。使用行向量指定单个分子多项式的系数。要指定多个滤波器的系数，请指定系数矩阵，其中每一行代表一组不同的滤波器抽头。要实现多个滤波器，**滤波器结构** 必须为 `Direct form II`，**输入处理** 必须为 `Elements as channels (sample based)`，并且输入必须为标量。

#### 依赖关系

要启用此参数，请将 **分子源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Numerator` |
| **类型：** character vector |
| **值：** scalar | vector | matrix |
| **默认：** `'[1]'` |

### **分母源** — 分母系数源 `Dialog`（默认）| `Input port`

将分母系数的源指定为 `Dialog` 或 `Input port`。

要将 **分母源** 设置为 `Input port`，请选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenominatorSource` |
| **类型：** character vector |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **分母值** — 分母系数 `[1 0.5]`（默认）| 向量

将离散滤波器的分母系数指定为 *z* 的降幂。使用行向量指定单个分母多项式的系数。

当您选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数时，如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

#### 依赖关系

要启用此参数，请将 **分母源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Denominator` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认：** `'[1 0.5]'` |

### **初始状态源** — 初始状态源 `Dialog`（默认）| `Input port`

将初始状态的源指定为 `Dialog` 或 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialStatesSource` |
| **类型：** character vector |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **初始状态值** — 初始滤波器状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

#### 依赖关系

要启用此参数，请将 **滤波器结构** 设置为 `Direct form II` 或 `Direct form II transposed`，并将 **初始状态源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** character vector |
| **值：** scalar | vector | matrix |
| **默认：** `'0'` |

或者，使用 `IC`。

### **分子侧的初始状态** — 初始分子状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始分子滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

#### 依赖关系

要启用此端口，请将 **滤波器结构** 设置为 `Direct form I` 或 `Direct form I transposed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** character vector |
| **值：** scalar | vector | matrix |
| **默认：** `'0'` |

### **分母侧的初始状态** — 初始分母状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始分母滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅指定初始状态。

#### 依赖关系

要启用此端口，请将 **滤波器结构** 设置为 `Direct form I` 或 `Direct form I transposed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialDenominatorStates` |
| **类型：** character vector |
| **值：** scalar | vector | matrix |
| **默认：** `'0'` |

### **外部复位** — 外部状态复位 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态重置为初始条件的触发事件。

| Reset Mode | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当前时间步复位信号非零时 - 复位信号值从上一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当前时间步复位信号非零时复位 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认**：`'None'` |

### **输入处理** — 基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样处理还是基于帧处理。

- `Elements as channels (sample based)` — 将输入的每个元素作为独立通道处理。
- `Columns as channels (frame based)` — 将输入的每一列作为独立通道处理。

#### 依赖关系

基于帧的处理需要 DSP System Toolbox 许可证。

有关更多信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputProcessing` |
| **类型：** character vector |
| **值：** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **默认：** `'Elements as channels (sample based)'` |

### **Optimize by skipping divide by leading denominator coefficient (a0)** — 跳过除以 a0 `off`（默认）| `on`

当您选中此复选框时，模块在仿真或生成的代码中都不会除以 *a0*。此参数优化您的代码。如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

如果您从输入端口 **Den** 指定分母系数，则必须选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。当您选中此复选框时，模块忽略前导分母系数 *a0*，并将其替换为 1。

当您清除此复选框时，模块在仿真期间完全可调。它在仿真和代码生成中都会除以 *a0*。

#### 程序化使用

|  |
| --- |
| **模块参数：** `a0EqualsOne` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **采样时间（-1 表示继承）** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **查看滤波器响应** — 查看滤波器响应按钮

单击此按钮可打开滤波器可视化工具 (`fvtool` (DSP System Toolbox))，并显示模块对话框中定义的滤波器的滤波器响应。

#### 依赖关系

要启用此参数，请将 **分子源** 和 **分母源** 参数设置为 `Dialog`。

仅当您拥有有效的 DSP System Toolbox 许可证时，此参数才会出现。

### 数据类型

### **状态** — 状态数据类型 `Inherit: Same as input`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定状态数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Same as input'` |

### **分子系数** — 分子系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置有符号整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumCoefDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **分子系数最小值** — 分子系数的最小值 `[]`（默认）| 标量

指定分子系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumCoefMin` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **分子系数最大值** — 分子系数的最大值 `[]`（默认）| 标量

指定分子系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumCoefMax` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **分子乘积输出** — 分子乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的乘积输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumProductDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **分子累加器** — 分子累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的累加器数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumAccumDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **分母系数** — 分母系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenCoefDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **分母系数最小值** — 分母系数的最小值 `[]`（默认）| 标量

指定分母系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenCoefMin` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **分母系数最大值** — 分母系数的最大值 `[]`（默认）| 标量

指定分母系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenCoefMax` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **分母乘积输出** — 分母乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数的乘积输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenProductDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **分母累加器** — 分母累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数的累加器数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DenAccumDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **输出** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **输出最小值** — 输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutMin` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **输出最大值** — 输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutMax` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `'[]'` |

### **被乘数数据类型** — 被乘数数据类型 `Inherit: Same as input`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定被乘数数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **滤波器结构** 设置为 `Direct form I transposed`

#### 程序化使用

|  |
| --- |
| **模块参数：** `MultiplicandDataTypeStr` |
| **类型：** character vector |
| **值：** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Same as input'` |

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的数据类型设置，防止 Fixed-Point Tool 和 Fixed-Point Advisor 进行更改。有关更多信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LockScale` |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时饱和还是环绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出环绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小值 -128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 为 -126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关更多信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选择此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### 状态属性

### **状态名称** — 为每个状态分配唯一名称 `' '`（默认）| `'position'` | `{'a', 'b', 'c'}` | `a` | ...

为每个状态分配唯一名称。如果此字段为空（`' '`），则不会进行名称分配。

- 要为单个状态分配名称，请在引号内输入名称，例如 `'position'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、元胞数组或结构体。

#### 限制

- 状态名称仅适用于所选模块。
- 状态数必须能够被状态名称数整除。
- 您可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，您可以在具有四个状态的系统中指定两个名称。第一个名称适用于前两个状态，第二个名称适用于后两个状态。

#### 依赖关系

要启用此参数，请将 **滤波器结构** 设置为 `Direct form II`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** character vector |
| **值：** `' '` | user-defined |
| **默认：** `' '` |

### **状态名称必须解析为 Simulink 信号对象** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框可要求状态名称解析为 Simulink 信号对象。

#### 依赖关系

要启用此参数，请将 **滤波器结构** 设置为 `Direct form II`，并为 **状态名称** 指定值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，此参数才会出现。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateMustResolveToSignalObject` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

## 所属库

Simulink / Discrete DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `integera` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持有符号定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

Discrete Filter 模块接受并输出 Simulink 支持的任何有符号数值数据类型的实数和复数信号。该模块对分子和分母系数支持相同的类型。

分子和分母系数必须具有相同的复数性。它们可以具有不同的字长和小数长度。

以下图表展示了离散滤波器模块中用于定点信号的滤波器结构及数据类型。

当您选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数时，该模块省略虚线除法。

## 版本历史

**在 R2006a 之前引入**

### R2024b：查看滤波器响应

单击 **View Filter Response** 按钮可可视化您在模块对话框中指定的滤波器的频率响应。

### R2024a：Discrete Filter 模块支持可变大小输入信号

当您将 **输入处理** 参数设置为 `Columns as channels (frame based)` 时，Discrete Filter 模块支持可变大小输入信号。

当输入为可变大小信号时，您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。

### R2023b：**采样时间** 参数的条件显示

Discrete Filter 模块默认不再在模块参数对话框中显示 **采样时间** 参数。仅当您在命令行或现有模型中将采样时间设置为默认值（`-1`）以外的值时，该参数才可见。有关更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

## 描述

模型无限脉冲响应 (IIR) 滤波器

Discrete Filter 模块使用指定的数字 IIR 滤波器独立地对输入信号的每个通道进行滤波。您可以将滤波器结构指定为 `Direct form I`、`Direct form I transposed`、`Direct form II` 或 `Direct form II transposed`。该模块实现具有固定系数的静态滤波器。您可以调优这些静态滤波器的系数。

此模块随时间独立地对输入信号的每个通道进行滤波。**输入处理** 参数允许您指定模块如何处理输入的每个元素。您可以指定将输入元素视为独立通道（基于采样处理），或将输入的每一列视为独立通道（基于帧处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

输出维度等于输入维度，除非您为 **分子系数** 参数指定滤波器抽头矩阵。在这种情况下，输出维度取决于您指定的不同滤波器抽头集的数量。

使用 **分子系数** 参数指定离散滤波器分子多项式的系数。使用 **分母系数** 参数指定函数分母多项式的系数。**分母系数** 参数必须是系数向量。

按 *z-1* 的升幂指定分子和分母多项式的系数。Discrete Filter 模块允许您使用 *z-1*（延迟算子）的多项式来表示离散系统。信号处理工程师通常使用此方法。相反，Discrete Transfer Fcn 模块允许您使用 *z* 的多项式来表示离散系统。控制工程师通常使用此方法。当分子和分母多项式长度相同时，这两种方法完全相同。

### 指定初始状态

在 **Dialog parameters** 和 **Input port(s)** 模式下，模块默认将内部滤波器状态初始化为零，这等价于假设过去的输入和输出为零。您可以选择使用 **初始状态** 参数为滤波器延迟指定非零初始状态。

要确定必须指定的初始状态值数量以及如何指定它们，请参阅下表中关于有效初始状态和延迟元素数量（滤波器状态）。**初始状态** 参数可以采用下表中描述的四种形式之一。

**有效初始状态**

| 初始状态 | 示例 | 描述 |
| --- | --- | --- |
| 标量 | `5` 每个通道的每个延迟元素设置为 `5`。 | 模块将滤波器中所有延迟元素初始化为该标量值。 |
| 向量（用于将相同延迟元素应用于每个通道） | 对于具有两个延迟元素的滤波器：[*d1**d2*] 所有通道的延迟元素为 d1 和 d2。 | 每个向量元素为对应延迟元素指定唯一的初始条件。模块将相同的初始条件向量应用于输入信号的每个通道。向量长度必须等于滤波器中延迟元素的数量（在表 延迟元素数量（滤波器状态）中指定）。 |
| 向量或矩阵（用于将不同延迟元素应用于每个通道） | 对于三通道输入信号和具有两个延迟元素的滤波器： [*d*1*d2**D1**D2**d1**d2*] 或 [d1D1d1d2D2d2] - 通道 1 的延迟元素为 *d1* 和 *d2*。 - 通道 2 的延迟元素为 *D1* 和 *D2*。 - 通道 3 的延迟元素为 *d1* 和 *d2*。 | 每个向量或矩阵元素为对应通道中的对应延迟元素指定唯一的初始条件： - 向量长度必须等于输入通道数与滤波器中延迟元素数量的乘积（在表 延迟元素数量（滤波器状态）中指定）。 - 矩阵必须具有与滤波器中延迟元素数量相同的行数（在表 延迟元素数量（滤波器状态）中指定），并且必须为输入信号的每个通道具有一列。 |
| 空矩阵 | `[ ]` 每个通道的每个延迟元素设置为 `0`。 | 空矩阵 `[]` 等价于将 **Initial conditions** 参数设置为标量值 `0`。 |

每个输入通道的延迟元素（滤波器状态）数量取决于滤波器结构，如下表所示。

**延迟元素数量（滤波器状态）**

| 滤波器结构 | 每个通道的延迟元素数量 |
| --- | --- |
| `Direct form I   Direct form I transposed` | - `number of zeros - 1` - `number of poles - 1` |
| `Direct form II   Direct form II transposed` | `max(number of zeros, number of poles)-1` |

下表根据您将 **输入处理** 参数设置为基于帧还是基于采样，描述了不同输入大小和不同通道数的有效初始状态。

**基于帧的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 列向量（*K*-by-1） - 无方向向量（*K*） | 1 | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） | - 标量 - 列向量（*M*-by-1） |
| - 行向量（1-by-*N*） - 矩阵（*K*-by-*N*） | *N* | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） - 矩阵（*M*-by-*N*） | - 标量 - 矩阵（*M*-by-*N*） |

**基于采样的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 无方向标量 | 1 | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） |
| - 行向量（1-by-*N*） - 列向量（*N*-by–1） - 无方向向量（*N*） | *N* | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） - 矩阵（*M*-by-*N*） | - 标量 |
| - 矩阵（*K*-by-*N*） | *K* × *N* | - 标量 - 列向量（*M*-by-1） - 行向量（1-by-*M*） - 矩阵（*M*-by-(*K*×*N*)) | - 标量 |

当 **初始状态** 为标量时，模块将所有滤波器状态初始化为相同的标量值。输入 `0` 将所有状态初始化为零。当 **初始状态** 为向量或矩阵时，每个向量或矩阵元素指定唯一的初始状态。此唯一状态对应于对应通道中的延迟元素：

- 向量长度必须等于滤波器中延迟元素的数量，`M = max(number of zeros, number of poles)`。
- 矩阵必须具有与滤波器中延迟元素数量相同的行数，`M = max(number of zeros, number of poles)`。矩阵还必须为输入信号的每个通道具有一列。

初始滤波器输出 *y1*、初始输入 *u1* 和初始状态 [*x1*, *x2*] 之间的关系由以下方程给出。

y1=b1[(u1−a2x1−a3x2)a1]+b2x1+b3x2

其中，

- *b1*、*b2* 和 *b3* 是离散滤波器的分子系数。
- *a1*、*a2* 和 *a3* 是离散滤波器的分母系数。
