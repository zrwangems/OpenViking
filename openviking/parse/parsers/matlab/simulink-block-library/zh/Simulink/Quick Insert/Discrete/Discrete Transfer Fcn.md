---
type: simulink-block
title: 'Discrete Transfer Fcn'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'discretetransferfcn'
documentation_source_path: 'slref/discretetransferfcn.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Transfer Fcn

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Num
  summary: 分子系数 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Den
  summary: 分母系数 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: External reset
  summary: 外部复位信号 标量
  direction: input
  data_types: single | double | Boolean | int8 | int16 | int32 | fixed point
- name: x0
  summary: 初始状态 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **u** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，该模块支持可变大小输入信号，即您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。*（自 R2024a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Num** — 分子系数 标量 | 向量 | 矩阵

以 *z* 的降幂指定的分子多项式系数，指定为向量或矩阵。使用行向量指定单个分子多项式的系数。使用矩阵指定要应用于同一输入的多个滤波器的系数。矩阵的每一行代表一组滤波器抽头。分母的阶数必须大于或等于分子的阶数。

#### 依赖关系

要启用此端口，请将 **Numerator Source** 设置为 `Input port`。

分子和分母系数必须具有相同的复数性。它们可以具有不同的字长和小数长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **Den** — 分母系数 标量 | 向量 | 矩阵

以 *z* 的降幂指定的分母多项式系数，指定为向量。使用行向量指定单个分母多项式的系数。使用矩阵指定要应用于同一输入的多个滤波器的系数。矩阵的每一行代表一组滤波器抽头。分母的阶数必须大于或等于分子的阶数。分母的首项系数不能为 `0`。

#### 依赖关系

要启用此端口，请将 **Denominator Source** 设置为 `Input port`。

分子和分母系数必须具有相同的复数性。它们可以具有不同的字长和小数长度。

要将 **Denominator Source** 设置为 `Input port`，请选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。该模块忽略分母首项系数值 a0 并将其替换为 1。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **External reset** — 外部复位信号 标量

外部复位信号，指定为标量。当指定的触发事件发生时，该模块将状态重置为其初始条件。

**提示**

此端口的图标根据 **External reset** 参数的值而变化。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为 `Rising`、`Falling`、`Either`、`Level` 或 `Level hold`。

#### 限制

复位信号必须是 single、double、Boolean 或整数类型的标量。不支持定点数据类型，`ufix1` 除外。

**数据类型：** `single` | `double` | `Boolean` | `int8` | `int16` | `int32` | `fixed point`

### **x0** — 初始状态 标量 | 向量 | 矩阵

初始状态，指定为标量、向量或矩阵。有关指定状态的详细信息，请参阅 Specifying Initial States。当输入或系数为复数时，状态为复数。

#### 依赖关系

要启用此端口，请将 **Initial states Source** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，指定为标量、向量或矩阵。

当您将 **Sample time** 设置为 `-1` 时，输出信号的采样时间与输入信号 **u** 的采样时间相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
## 参数
```yaml
parameters:
- name: Numerator Source
  summary: 分子系数来源 Dialog（默认）| Input port
  group: 主要
  block_parameter: NumeratorSource
  type: 字符向量
  values: '''Dialog'' | ''Input port'''
- name: Numerator Value
  summary: 分子系数 [1]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: Numerator
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: Denominator Source
  summary: 分母系数来源 Dialog（默认）| Input port
  group: 主要
  block_parameter: DenominatorSource
  type: 字符向量
  values: '''Dialog'' | ''Input port'''
- name: Denominator Value
  summary: 分母系数 [1 0.5]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: Denominator
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: Initial states Source
  summary: 初始状态来源 Dialog（默认）| Input port
  group: 主要
  block_parameter: InitialStatesSource
  type: 字符向量
  values: '''Dialog'' | ''Input port'''
- name: Initial states Value
  summary: 初始滤波器状态 0（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: InitialStates
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: External reset
  summary: 外部状态复位 None（默认）| Rising | Falling | Either | Level | Level hold
  group: 主要
  block_parameter: ExternalReset
  type: 字符向量
  values: '''None'' | ''Rising'' | ''Falling'' | ''Either'' | ''Level'' | ''Level hold'''
- name: Input processing
  summary: 基于采样或基于帧的处理 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: 主要
  block_parameter: InputProcessing
  type: 字符向量
  values: '''Elements as channels (sample based)'' | ''Columns as channels (frame based)'''
- name: Optimize by skipping divide by leading denominator coefficient (a0)
  summary: 跳过除以 a0 off（默认）| on
  group: 主要
  block_parameter: a0EqualsOne
  type: 字符向量
  values: '''off'' | ''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: View Filter Response
  summary: 查看滤波器响应 按钮
  group: 主要
- name: State
  summary: '状态数据类型 Inherit: Same as input（默认）| int8 | int16 | int32 | int64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: StateDataTypeStr
  type: 字符向量
  values: '''Inherit: Same as input'' | ''int8'' | ''int16'' | ''int32'' | ''int64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
- name: Numerator coefficients
  summary: '分子系数数据类型 Inherit: Inherit via internal rule（默认）| int8 | int16 | int32 | int64 | fixdt(1,16) | fixdt(1,16,0) |
    <data type expression>'
  group: 数据类型
  block_parameter: NumCoefDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''int8'' | ''int16'' | ''int32'' | ''int64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)''
    | ''<data type expression>'''
- name: Numerator coefficient minimum
  summary: 分子系数的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: NumCoefMin
  type: 字符向量
  values: 标量
- name: Numerator coefficient maximum
  summary: 分子系数的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: NumCoefMax
  type: 字符向量
  values: 标量
- name: Numerator product output
  summary: '分子乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | int8 | int16 | int32 | int64 | fixdt(1,16,0)
    | <data type expression>'
  group: 数据类型
  block_parameter: NumProductDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''int8'' | ''int16'' | ''int32'' | ''int64''
    | ''fixdt(1,16,0)'' | ''<data type expression>'''
- name: Numerator accumulator
  summary: 'Numerator accumulator 数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product
    output | int8 | int16 | int32 | int64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: NumAccumDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''Inherit: Same as product output'' | ''int8''
    | ''int16'' | ''int32'' | ''int64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Denominator coefficients
  summary: '分母系数数据类型 Inherit: Inherit via internal rule（默认）| int8 | int16 | int32 | int64 | fixdt(1,16) | fixdt(1,16,0) |
    <data type expression>'
  group: 数据类型
  block_parameter: DenCoefDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''int8'' | ''int16'' | ''int32'' | ''int64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)''
    | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Denominator coefficient minimum
  summary: 分母系数的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: DenCoefMin
  type: character vector
  values: scalar
  default: '''[]'''
- name: Denominator coefficient maximum
  summary: 分母系数的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: DenCoefMax
  type: character vector
  values: scalar
  default: '''[]'''
- name: Denominator product output
  summary: '分母乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | int8 | int16 | int32 | int64 | fixdt(1,16,0)
    | <data type expression>'
  group: 数据类型
  block_parameter: DenProductDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''int8'' | ''int16'' | ''int32'' | ''int64''
    | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Denominator accumulator
  summary: '分母累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | int8
    | int16 | int32 | int64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: DenAccumDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''Inherit: Same as product output'' | ''int8''
    | ''int16'' | ''int32'' | ''int64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Output
  summary: '输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | int8 | int16 | int32 | int64 | fixdt(1,16)
    | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''int8'' | ''int16'' | ''int32'' | ''int64''
    | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Output minimum
  summary: 输出的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  type: character vector
  values: scalar
  default: '''[]'''
- name: Output maximum
  summary: 输出的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  type: character vector
  values: scalar
  default: '''[]'''
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: State name
  summary: 模块状态的唯一名称 ''（默认）| 字母数字字符串
  group: State Attributes
  block_parameter: StateName
  type: character vector
  values: unique name
  default: ''''''
- name: State name must resolve to Simulink signal object
  summary: 要求状态名称解析为信号对象 off（默认）| on
  group: State Attributes
  block_parameter: StateMustResolveToSignalObject
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### 主要

### **Numerator Source** — 分子系数来源 `Dialog`（默认）| `Input port`

将分子系数的来源指定为 `Dialog` 或 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumeratorSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **Numerator Value** — 分子系数 `[1]`（默认）| 标量 | 向量 | 矩阵

离散传递函数的分子系数。要指定系数，请将 **Source** 设置为 `Dialog`。然后，在 **Value** 中以 *z* 的降幂输入系数。使用行向量指定单个分子多项式的系数。使用矩阵指定要应用于同一输入的多个滤波器的系数。矩阵的每一行代表一组滤波器抽头。

#### 依赖关系

要启用此参数，请将 **Numerator Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Numerator` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[1]'` |

### **Denominator Source** — 分母系数来源 `Dialog`（默认）| `Input port`

将分母系数的来源指定为 `Dialog` 或 `Input port`。

要将 **Denominator Source** 设置为 `Input port`，请选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `DenominatorSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **Denominator Value** — 分母系数 `[1 0.5]`（默认）| 标量 | 向量 | 矩阵

离散传递函数的分母系数。要指定系数，请将 **Source** 设置为 `Dialog`。然后，在 **Value** 中以 *z* 的降幂输入系数。使用行向量指定单个分母多项式的系数。使用矩阵指定要应用于同一输入的多个滤波器的系数。矩阵的每一行代表一组滤波器抽头。

当您选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数时，如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

#### 依赖关系

要启用此参数，请将 **Denominator Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Denominator` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[1 0.5]'` |

### **Initial states Source** — 初始状态来源 `Dialog`（默认）| `Input port`

将初始状态的来源指定为 `Dialog` 或 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialStatesSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog' | 'Input port'` |
| **默认：** `'Dialog'` |

### **Initial states Value** — 初始滤波器状态 `0`（默认）| 标量 | 向量 | 矩阵

将初始滤波器状态指定为标量、向量或矩阵。要了解如何指定初始状态，请参阅 Specifying Initial States。

#### 依赖关系

要启用此参数，请将 **Initial states Source** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'0'` |

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

#### 编程使用

|  |
| --- |
| **模块参数**： `ExternalReset` |
| **类型**： 字符向量 |
| **值**： `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认**： `'None'` |

### **Input processing** — 基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定该模块执行基于采样还是基于帧的处理。

- `Elements as channels (sample based)` — 将输入的每个元素作为独立通道处理。
- `Columns as channels (frame based)` — 将输入的每一列作为独立通道处理。

  **注意**

  基于帧的处理需要 DSP System Toolbox 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputProcessing` |
| **类型：** 字符向量 |
| **值：** `'Elements as channels (sample based)' | 'Columns as channels (frame based)'` |
| **默认：** `'Elements as channels (sample based)'` |

### **Optimize by skipping divide by leading denominator coefficient (a0)** — 跳过除以 a0 `off`（默认）| `on`

当您选中此复选框时，该模块在仿真或生成的代码中都不会除以 *a0*。此参数可优化您的代码。如果在模块对话框中指定分母系数且 *a0* ≠ 1，则会发生错误。

如果从输入端口 **Den** 指定分母系数，则必须选择 **Optimize by skipping divide by leading denominator coefficient (a0)** 参数。当您选中此复选框时，该模块忽略分母首项系数 *a0* 并将其替换为 1。

当您清除此复选框时，该模块在仿真期间完全可调。它在仿真和代码生成中都会除以 *a0*。

#### 编程使用

|  |
| --- |
| **模块参数：** `a0EqualsOne` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮可打开 Filter Visualization Tool（`fvtool` (DSP System Toolbox)）并显示模块对话框中定义的滤波器的滤波器响应。

#### 依赖关系

要启用此参数，请将 **Numerator Source** 和 **Denominator Source** 参数设置为 `Dialog`。

仅当您拥有有效的 DSP System Toolbox 许可证时，此参数才会出现。

### 数据类型

### **State** — 状态数据类型 `Inherit: Same as input`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定状态数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数：** `StateDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Same as input'` |

### **Numerator coefficients** — 分子系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数：**  `NumCoefDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **Numerator coefficient minimum** — 分子系数的最小值 `[]`（默认）| 标量

指定分子系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数：** `NumCoefMin` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'[]'` |

### **Numerator coefficient maximum** — 分子系数的最大值 `[]`（默认）| 标量

指定分子系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数：** `NumCoefMax` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'[]'` |

### **Numerator product output** — 分子乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的乘积输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumProductDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认：** `'Inherit: Inherit via internal rule'` |

### **Numerator accumulator** — Numerator accumulator 数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分子系数的累加器数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumAccumDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator coefficients** — 分母系数数据类型 `Inherit: Inherit via internal rule`（默认）| `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置整数类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenCoefDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator coefficient minimum** — 分母系数的最小值 `[]`（默认）| 标量

指定分母系数可以具有的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`DenCoefMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Denominator coefficient maximum** — 分母系数的最大值 `[]`（默认）| 标量

指定分母系数可以具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

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

指定分母系数的乘积输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenProductDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Denominator accumulator** — 分母累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16,0)` | `<data type expression>`

指定分母系数的累加器数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`DenAccumDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `int16` | `int32` | `int64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'int16' | 'int32' | 'int64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Output minimum** — 输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Output maximum** — 输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges）
- 定点数据类型的自动定标

#### 编程使用

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'[]'` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成的代码中具有显式饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### State Attributes

### **State name** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **Apply** 时，此参数会启用 **State name must resolve to Simulink signal object**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateName` |
| **类型**：character vector |
| **值**：unique name |
| **默认值**：`''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框可要求状态名称解析为 Simulink 信号对象。

#### 依赖关系

要启用此参数，请为 **State name** 指定一个值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，此参数才会出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

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

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstMultiplierOptimization** | 规范有符号数字（CSD）或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于尾数中没有前导零时可表示的最小浮点数的数。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**Restrictions**

- 此模块不支持双精度数据类型。请改用单精度数据类型。
- 不支持帧、矩阵和向量输入数据类型。
- 前导分母系数（a0）必须为 1 或 -1。
- 不支持将数据类型设置为 `Inherit: Inherit via internal rule`。

Discrete Transfer Fcn 模块被排除在以下优化之外：

- 资源共享
- 分布式流水线

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

## 版本历史

**在 R2006a 之前引入**

### R2024b: View filter response

点击 **View Filter Response** 按钮可可视化您在模块对话框中指定的滤波器的频率响应。

### R2024a: Discrete Transfer Fcn 模块支持可变大小输入信号

当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，Discrete Transfer Fcn 模块支持可变大小输入信号。

当输入为可变大小信号时，您可以在仿真期间更改信号的帧大小（行数），但通道数（列数）必须保持不变。

### R2023b: **Sample time** 参数的条件显示

Discrete Transfer Fcn 模块默认不再在模块参数对话框中显示 **Sample time** 参数。仅当您在命令行或现有模型中将采样时间设置为非默认值（`-1`）时，该参数才可见。有关详细信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

## 描述

实现离散传递函数

Discrete Transfer Fcn 模块按如下方式实现 *z* 变换传递函数：

H(z)=num(z)den(z)=num0zm+num1zm−1+...+nummden0zn+den1zn−1+...+denn

其中 m+1 和 n+1 分别是分子和分母系数的数量。*num* 和 *den* 包含按 *z* 的降幂排列的分子和分母系数。*num* 可以是向量或矩阵，而 *den* 必须是向量。分母的阶数必须大于或等于分子的阶数。

指定按 *z* 的降幂排列的分子和分母多项式系数。此模块允许您使用 *z* 的多项式来表示离散系统，这是控制工程师通常使用的方法。相反，Discrete Filter 模块允许您使用 *z-1*（延迟算子）的多项式来表示离散系统，这是信号处理工程师通常使用的方法。当分子和分母多项式长度相同时，这两种方法是相同的。

Discrete Transfer Fcn 模块将 *z* 变换传递函数应用于输入的每个独立通道。**Input processing** 参数允许您指定模块是将输入的每一列视为一个独立通道（基于帧的处理），还是将输入的每个元素视为一个独立通道（基于采样的处理）。要执行基于帧的处理，您必须拥有 DSP System Toolbox™ 许可证。

### 指定初始状态

使用 **Initial states** 参数指定初始滤波器状态。您指定的初始状态是实现离散传递函数的滤波器图中使用的单位延迟模块的初始条件。

要确定必须指定的初始状态数量以及如何指定它们，请使用以下表格。

**基于帧的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 列向量（*K*×1） - 无方向向量（*K*） | 1 | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） | - 标量 - 列向量（*M*×1） |
| - 行向量（1×*N*） - 矩阵（*K*×*N*） | *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×*N*） | - 标量 - 矩阵（*M*×*N*） |

**基于采样的处理**

| 输入 | 通道数 | 有效初始状态（对话框） | 有效初始状态（输入端口） |
| --- | --- | --- | --- |
| - 标量 | 1 | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） |
| - 行向量（1×*N*） - 列向量（*N*×1） - 无方向向量（*N*） | *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×*N*） | - 标量 |
| - 矩阵（*K*×*N*） | *K* × *N* | - 标量 - 列向量（*M*×1） - 行向量（1×*M*） - 矩阵（*M*×(*K*×*N*)） | - 标量 |

当 **Initial states** 为标量时，模块将所有滤波器状态初始化为相同的标量值。要将所有状态初始化为零，请输入 `0`。当 **Initial states** 为向量或矩阵时，每个向量或矩阵元素为对应通道中的对应延迟元件指定唯一的初始状态：

- 向量长度必须等于滤波器中的延迟元件数量，`M = max(number of zeros, number of poles)`。
- 矩阵的行数必须与滤波器中的延迟元件数量相同，`M = max(number of zeros, number of poles)`。矩阵还必须为输入信号的每个通道包含一列。

以下示例显示了初始滤波器输出与初始输入和状态之间的关系。给定初始输入 *u1*，第一个输出 *y1* 与初始状态 [*x1*, *x2*] 和初始输入的关系如下：

y1=4x1x2=1/2(u1−3x1)
