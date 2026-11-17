---
type: simulink-block
title: 'Discrete FIR Filter'
family: 'hdlcoder'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretefirfilter'
documentation_source_path: '../simulink/slref/discretefirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete FIR Filter

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Num
  summary: 滤波器系数 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: External reset
  summary: 外部复位信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: ⎍
  summary: 使能信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 滤波后的输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

要滤波的输入信号，指定为标量、向量或矩阵。

Discrete FIR Filter 模块接受 Simulink 支持的任何数值数据类型的实数和复数信号。

#### 依赖关系

当您将 **Coefficient source** 设置为 `Dialog parameters` 时，输入信号的端口没有标签。当您将 **Coefficient source** 设置为 `Input port` 时，输入信号的端口标记为 **In**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Num** — 滤波器系数 标量 | 向量

将滤波器系数指定为标量或向量。当您指定滤波器抽头的行向量时，模块对输入应用单个滤波器。要对输入应用多个滤波器，请通过 **Coefficients** 参数以矩阵形式指定系数。

#### 依赖关系

要启用此端口，请将 **Coefficient source** 设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **External reset** — 外部复位信号 标量

外部复位信号，指定为标量。当指定的触发事件发生时，模块将状态重置为其初始条件。

**提示**

此端口的图标根据 **External reset** 参数的值而变化。

#### 依赖关系

要启用此端口，请将 **External reset** 设置为 `Rising`、`Falling`、`Either`、`Level` 或 `Level hold`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **⎍** — 使能信号 标量

使能信号，指定为标量。此端口可以控制模块的执行。当此端口的输入为非零时，模块被使能；当输入为 `0` 时，模块被禁用。输入的值在模块执行的同一时间步进行检查。

#### 依赖关系

要启用此端口，请选中 **Show enable port** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 滤波后的输出信号 标量 | 向量 | 矩阵

滤波后的输出信号，以标量、向量或矩阵形式返回。Discrete FIR Filter 模块输出 Simulink 支持的任何数值数据类型的实数和复数信号。

当模块的输入为定点时，模块输出的数据类型取决于您在 **Output** 参数中指定的值。当输入为浮点时，输出数据类型与输入数据类型匹配，因为浮点继承优先于定点设置。

当您将 **Sample time** 设置为 `-1` 时，输出信号的采样时间与输入信号 **In** 的采样时间相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Coefficient source
  summary: 系数来源 Dialog parameters（默认）| Input port
  group: 主要
  block_parameter: CoefSource
  type: 字符向量
  values: '''Dialog parameters'' | ''Input port'''
  default: '''Dialog parameters'''
- name: Filter structure
  summary: 滤波器结构 Direct form（默认）| Direct form symmetric | Direct form antisymmetric | Direct form transposed | Lattice MA
  group: 主要
  block_parameter: FilterStructure
  type: 字符向量
  values: '''Direct form'' | ''Direct form symmetric'' | ''Direct form antisymmetric'' | ''Direct form transposed'' | ''Lattice
    MA'''
  default: '''Direct form'''
- name: Coefficients
  summary: 滤波器系数 [0.5 0.5]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: Coefficients
  type: 字符向量
  values: 向量
  default: '''[0.5 0.5]'''
- name: Input processing
  summary: 基于采样或基于帧的处理 Elements as channels (sample based)（默认）| Columns as channels (frame based)
  group: 主要
  block_parameter: InputProcessing
  type: 字符向量
  values: '''Columns as channels (frame based)'' | ''Elements as channels (sample based)'''
  default: '''Elements as channels (sample based)'''
- name: Initial states
  summary: 滤波器状态的初始条件 0（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: InitialStates
  type: 字符向量
  values: 标量 | 向量 | 矩阵
  default: '''0'''
- name: Show enable port
  summary: 创建使能端口 off（默认）| on
  group: 主要
  block_parameter: ShowEnablePort
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: External reset
  summary: 外部状态复位 None（默认）| Rising | Falling | Either | Level | Level hold
  group: 主要
  block_parameter: ExternalReset
  type: 字符向量
  values: '''None'' | ''Rising'' | ''Falling'' | ''Either'' | ''Level'' | ''Level hold'''
  default: '''None'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: View Filter Response
  summary: 查看滤波器响应 按钮
  group: 主要
- name: Tap sum
  summary: '抽头求和数据类型 Inherit: Same as input（默认）| Inherit: Inherit via internal rule | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: TapSumDataTypeStr
  type: 字符向量
  values: '''Inherit: Same as input'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64''
    | ''uint64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Same as input'''
- name: Coefficients
  summary: '系数数据类型 Inherit: Same wordlength as input（默认）| int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64
    | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: CoefDataTypeStr
  type: 字符向量
  values: '''Inherit: Same word length as input''| ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''
    | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Same wordlength as input'''
- name: Coefficients minimum
  summary: 系数的最小值 []（默认）| 标量
  group: 数据类型
  block_parameter: CoeffMin
  type: 字符向量
  values: 标量
  default: '''[]'''
- name: Coefficients maximum
  summary: 系数的最大值 []（默认）| 标量
  group: 数据类型
  block_parameter: CoeffMax
  type: 字符向量
  values: 标量
  default: '''[]'''
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: ProductDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16''
    | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | int8
    | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: AccumDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as input'' | ''Inherit: Same as product output'' | ''int8''
    | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16,0)'' | ''<data type
    expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: State
  summary: '状态数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | int8 | uint8 | int16 | uint16 | int32 | uint32
    | int64 | uint64 | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: StateDataTypeStr
  type: 字符向量
  values: '''Inherit: Same as accumulator'' | ''Inherit: Same as input'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' |
    ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Same as accumulator'''
- name: Output
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | int8 | uint8 | int16 | uint16 | int32 | uint32
    | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Same as accumulator'' | ''Inherit: Same as input'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' |
    ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''<data type expression>'''
  default: '''Inherit: Same as accumulator'''
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  values: '''off'' | ''on'''
  default: '''off'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  type: character vector
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
```

### 主要

### **Coefficient source** — 系数来源 `Dialog parameters`（默认）| `Input port`

选择使用可调对话框参数或通过输入端口指定滤波器系数，后者对于时变系数非常有用。

#### 编程用法

|  |
| --- |
| **模块参数：** `CoefSource` |
| **类型：** 字符向量 |
| **值：** `'Dialog parameters' | 'Input port'` |
| **默认值：** `'Dialog parameters'` |

### **Filter structure** — 滤波器结构 `Direct form`（默认）| `Direct form symmetric` | `Direct form antisymmetric` | `Direct form transposed` | `Lattice MA`

选择您希望模块实现的滤波器结构。有关详细信息，请参阅算法。

#### 依赖关系

您必须拥有可用的 DSP System Toolbox 许可证才能运行实现了 `Direct form` 以外任何滤波器结构的 Discrete FIR Filter 模块的模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `FilterStructure` |
| **类型：** 字符向量 |
| **值：** `'Direct form' | 'Direct form symmetric' | 'Direct form antisymmetric' | 'Direct form transposed' | 'Lattice MA'` |
| **默认值：** `'Direct form'` |

### **Coefficients** — 滤波器系数 `[0.5 0.5]`（默认）| 标量 | 向量 | 矩阵

将滤波器系数指定为标量、向量或矩阵。

当您指定滤波器抽头的行向量时，模块对输入应用单个滤波器。要对同一输入应用多个滤波器，请指定系数矩阵，其中每一行代表一组不同的滤波器抽头。要实现多个滤波器，请将 **Filter structure** 设置为 `Direct form`，并且输入必须是标量。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 `Dialog parameters`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Coefficients` |
| **类型：** 字符向量 |
| **值：** 向量 |
| **默认值：** `'[0.5 0.5]'` |

### **Input processing** — 基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理。您可以选择以下选项之一：

- `Elements as channels (sample based)`
  — 将输入的每个元素视为独立通道（基于采样的处理）。
- `Columns as channels (frame based)`
  — 将输入的每一列视为独立通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox 许可证。

  有关详细信息，请参阅基于采样和基于帧的概念（DSP System Toolbox）。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputProcessing` |
| **类型：** 字符向量 |
| **值：** `'Columns as channels (frame based)' | 'Elements as channels (sample based)'` |
| **默认值：** `'Elements as channels (sample based)'` |

### **Initial states** — 滤波器状态的初始条件 `0`（默认）| 标量 | 向量 | 矩阵

指定滤波器状态的初始条件。要了解如何指定初始状态，请参阅指定初始状态。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialStates` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'0'` |

### **Show enable port** — 创建使能端口 `off`（默认）| `on`

选择使用使能端口控制此模块的执行。当此端口的输入为非零时，模块被视为已使能；当输入为 `0` 时，模块被禁用。输入的值在模块执行的同一时间步进行检查。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowEnablePort` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **External reset** — 外部状态复位 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态重置为初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当复位信号在当前时间步为非零时 - 当复位信号值从上一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当复位信号在当前时间步为非零时复位 |

#### 编程用法

|  |
| --- |
| **模块参数**： `ExternalReset` |
| **类型**： 字符向量 |
| **值**： `'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**： `'None'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮可打开滤波器可视化工具（`fvtool` (DSP System Toolbox)）并显示在模块对话框中定义的滤波器的滤波器响应。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 参数设置为 `Dialog parameters`。

仅当您拥有有效的 DSP System Toolbox 许可证时，此参数才会出现。

### 数据类型

### **Tap sum** — 抽头求和数据类型 `Inherit: Same as input`（默认）| `Inherit: Inherit via internal rule` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

指定直接型对称或直接型反对称滤波器的抽头求和数据类型，即滤波器在将输入求和后再乘以系数时使用的数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 依赖关系

仅当您将 **Filter structure** 设置为 `Direct form symmetric` 或 `Direct form antisymmetric` 时，此参数才可见。

#### 编程用法

|  |
| --- |
| **模块参数：**  `TapSumDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Same as input'` |

### **Coefficients** — 系数数据类型 `Inherit: Same wordlength as input`（默认）| `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

指定系数数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**  `CoefDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Same word length as input'| 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Same wordlength as input'` |

### **Coefficients minimum** — 系数的最小值 `[]`（默认）| 标量

指定滤波器系数应具有的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数：**  `CoeffMin` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Coefficients maximum** — 系数的最大值 `[]`（默认）| 标量

指定滤波器系数应具有的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅指定模块参数的最小值和最大值）
- 定点数据类型的自动定标

#### 编程用法

|  |
| --- |
| **模块参数：**  `CoeffMax` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `'[]'` |

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

指定乘积输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**  `ProductDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

指定累加器数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：**  `AccumDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule' | 'Inherit: Same as input' | 'Inherit: Same as product output' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Inherit via internal rule'` |

### **State** — 状态数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

指定状态数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 求值为数据类型的表达式，例如 `fixdt(1,16,0)`

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Lattice MA`。

#### 编程用法

|  |
| --- |
| **模块参数：**  `StateDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值：** `'Inherit: Same as accumulator'` |

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as
  accumulator`
- 内置数据类型，例如，
  `int8`
- 数据类型对象，例如，
  `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如，
  `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

当模块的输入为浮点类型时，输出数据类型与输入数据类型匹配，因为浮点继承优先于定点设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Same as accumulator' | 'Inherit: Same as input' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **默认值**：`'Inherit: Same as accumulator'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and
  Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges and
  Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此项可锁定此模块的数据类型设置，防止 Fixed-Point Tool 和 Fixed-Point Advisor 对其进行更改。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

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

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值
  -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为
  `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式添加饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |
## 所属库

Simulink / Discrete HDL Coder / Discrete HDL Coder / HDL Floating Point Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持自定义状态属性，以便更高效地自定义和生成代码。要访问或设置这些属性，请打开 Model Data Editor。在 **Modeling** 选项卡上，点击 **Model
Data Editor**。有关示例，请参阅 Custom State Attributes in Discrete FIR Filter block。

**使用 Intel AVX2 代码替换库生成 SIMD 代码**

**注意**

需要 Embedded Coder® 许可证

Discrete FIR Filter 模块在以下条件下支持使用 Intel AVX2 代码替换库生成 SIMD 代码：

- **Filter structure** 设置为 `Direct
  form` 或 `Direct form
  transposed`。
- **Input processing** 设置为 `Columns
  as channels (frame based)`。
- 输入信号为实值，滤波器系数为实数。
- 当 **Filter structure** 设置为
  `Direct form` 时，输入信号为复值，滤波器系数为实数或复数。
- 输入信号的数据类型为 `single` 或
  `double`。

**通过利用目标硬件指令集扩展生成 SIMD 代码** *(自 R2022b 起)*

**注意**

需要 Simulink
Coder™ 或 Embedded Coder 许可证

在以下条件下，您可以使用模型配置参数
**Leverage target hardware instruction set extensions** 在所有
Intel® 平台、ARM®
Cortex®-A 处理器和 Apple 芯片处理器上为 Discrete FIR Filter 模块生成 SIMD 代码：

- 将 **Filter structure** 设置为 `Direct
  form`
- 将 **Input processing** 设置为 `Columns
  as channels (frame based)`
- 输入信号为实值，滤波器系数为实数
- 输入信号为实值或复值。
- 输入信号的数据类型为 `single`
  （ARM
  Cortex-A 处理器）
- 输入信号的数据类型为 `single` 或
  `double`（Intel 平台）

此外，请适当配置您的模型。

在 Simulink 模型窗口的 **Modeling** 选项卡中，点击 **Model Settings**，然后在 **Code Generation** 下配置以下参数。

- 在 **Optimization** 窗格中：

  - 在
    **Leverage target hardware instruction set
    extensions** 参数中提供特定的指令集。
  - 选中 **Optimize reductions**
    参数。
  - 在 **Optimization levels** 下，将
    **Level** 设置为
    `Maximum`，将
    **Priority** 设置为 `Maximize
    execution speed`。
- 在 **Interface** 窗格中，在 **Software
  environment** 下，清除 **non-finite
  numbers**。

要使用此工作流从此模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks (DSP System Toolbox)。

对于受支持模块上的计算密集型运算，SIMD 内建函数可以显著提高生成代码在 Intel 平台上的性能。有关更多详细信息，请参阅 Optimize Code for Reduction Operations by Using SIMD (Simulink Coder)。要从此模块生成 SIMD 代码，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**注意**

对于硬件友好的有效和复位控制信号，以及在 Simulink 中建模精确的硬件延迟行为，请改用 Discrete FIR Filter (DSP HDL Toolbox) 模块。

**HDL 架构**

该模块默认架构为 `HDLDataPath`。此架构提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenFilter** | 从生成的 HDL 代码中移除 Filter 子系统的层次结构。默认值为 `auto`。请参阅 FlattenHierarchy (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行、标量数据路径的并行数据路径或向量数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **MultiplerArchitecture** | 选择乘法器架构为 `linear` 或 `shiftadd`。默认值为 `linear`。更多信息，请参阅 Product, Matrix Multiply 中的 HDL Code Generation 部分。 |
| **MultiplierInputPipeline** | 指定在滤波器乘法器输入端添加的流水线级数。另请参阅 MultiplierInputPipeline (HDL Coder)。 |
| **MultiplierOutputPipeline** | 指定在滤波器乘法器输出端添加的流水线级数。另请参阅 MultiplierOutputPipeline (HDL Coder)。 |
| **AdderChainArchitecture** | 选择加法器架构以生成线性链或树形结构的加法器来计算元素之和。默认值为 `tree`。更多信息，请参阅 Sum 中的 HDL Code Generation 部分。 |
| **AdderOutputPipeline** | 在生成代码中为加法运算插入的输出流水线级数。默认值为 `0`。更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量  向量  矩阵 | 是 | Half  Single  Double | 是 | 是 | 是 | 是 | 是 |

**优化**

该模块参与以下 HDL 优化以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 将向量数据路径转换为标量数据路径（或转换为多个较小尺寸的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，通过移动设计中的现有延迟来减少关键路径，同时保持功能行为。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化通过向设计中的模块插入流水线寄存器，创建带有寄存器的模式或模块组合，从而提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

该模块具有以下限制：

- 必须将 **Initial conditions** 设置为 `0`。不支持非零初始状态的 HDL 代码生成。
- **Filter Structure**：`Lattice MA`。
- **External reset** 参数必须设置为 `None` 或 `Level hold`。

要为特殊情况（如可编程滤波器或多通道滤波器）配置 Discrete FIR Filter 模块，请使用以下模块设置：

| 滤波器情况 | 注意事项 |
| --- | --- |
| **可编程滤波器** | HDL Coder 支持 Discrete FIR Filter 模块的可编程滤波器。  1. 在滤波器模块掩码上，将 **Coefficient source** 设置为 **Input port**。 2. 将向量信号连接到 `Num` 系数端口。 |
| **多通道滤波器** | HDL Coder 支持对 Discrete FIR Filter 模块使用向量输入，其中向量的每个元素代表一个独立通道。  1. 将向量信号连接到 Discrete FIR Filter 模块输入端口。 2. 将 **Input processing** 指定为 `Elements as channels (sample based)`。 |
| **基于帧的输入** | HDL Coder 支持对 Discrete FIR Filter 模块使用向量输入，其中向量的每个元素代表一个时间采样。可以使用最多 512 个采样的输入向量。基于帧的实现支持定点输入和输出数据类型，并使用全精度内部数据类型。可以使用实数输入信号和实数系数、复数输入信号和实数系数，或实数输入信号和复数系数。还可以将基于帧的输入与可编程系数一起使用。  1. 将向量信号连接到 Discrete FIR Filter 模块输入端口。 2. 将 **Input processing** 指定为 `Columns as channels (frame based)`。对于带可编程系数的基于帧的输入，将 **Filter structure** 设置为 `Direct form`。  当使用基于帧的输入数据时，可以使用复数输入信号和实数系数，或复数系数和实数输入信号。 |
| **带控制端口的滤波器** | 可以为带可选使能端口和可选复位端口的滤波器生成 HDL 代码。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2008a 中引入**

### R2024b：为 Apple silicon 处理器生成 SIMD 代码

在 R2024b 中，如果拥有 Embedded Coder，可以通过使用模型配置参数 **Leverage target hardware instruction set extensions** 为 Apple silicon 处理器生成 Discrete FIR Filter 模块的 SIMD 代码。更多信息，请参阅 Use Target Hardware Instruction Set Extensions to Generate SIMD Code from Simulink Blocks for Apple silicon (DSP System Toolbox)。

### R2024b：查看滤波器响应

点击 **View Filter Response** 按钮以可视化在模块对话框中指定的滤波器的频率响应。

### R2023b：为复数信号生成 SIMD 代码

在 R2023b 中，如果拥有 Embedded Coder，当输入信号为复数值时，可以通过使用模型配置参数 **Leverage target hardware instruction set extensions** 为 Discrete FIR Filter 模块生成 SIMD 代码。

### R2023b：**Sample time** 参数的条件显示

Discrete FIR Filter 模块默认不再在模块参数对话框中显示 **Sample time** 参数。仅当在命令行或现有模型中将采样时间设置为非默认值（`-1`）时，该参数才可见。更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

## 描述

对 FIR 滤波器进行建模

Discrete FIR Filter 模块使用指定的数字 FIR 滤波器独立地对输入信号的每个通道进行滤波。该模块可以实现具有固定系数的静态滤波器，以及系数随时间变化的时变滤波器。可以在仿真期间调整静态滤波器的系数。

该模块随时间独立地对输入信号的每个通道进行滤波。**Input processing** 参数允许指定模块是将输入的每个元素视为独立通道（基于采样的处理），还是将输入的每一列视为独立通道（基于帧的处理）。要执行基于帧的处理，必须拥有 DSP System Toolbox™ 许可证。

输出维度等于输入维度，除非为 **Coefficients** 参数指定滤波器抽头矩阵。在这种情况下，输出维度取决于指定的不同滤波器抽头组数。

该模块支持自定义状态属性，以更高效地自定义和生成代码。有关示例，请参阅 Custom State Attributes in Discrete FIR Filter block。在某些条件下，该模块还支持 SIMD 代码生成。有关详细信息，请参阅代码生成。

该模块的输出在数值上与 DSP System Toolbox Digital Filter Design (DSP System Toolbox) 模块的输出匹配。

该模块支持 Simulink® 状态日志记录功能。更多信息，请参阅 State。

### 滤波器结构支持

可以通过从 **Filter structure** 参数中选择以下选项之一来更改 Discrete FIR Filter 模块实现的滤波器结构：

- `Direct form`
- `Direct form symmetric`
- `Direct form antisymmetric`
- `Direct form transposed`
- `Lattice MA`

要运行使用除 `Direct form` 之外的任何这些滤波器结构的模型，必须拥有可用的 DSP System Toolbox 许可证。

有关滤波器结构的更多信息，请参阅算法。

### 指定初始状态

Discrete FIR Filter 模块默认将内部滤波器状态初始化为零，这与假设过去的输入和输出为零具有相同的效果。可以选择使用 **Initial states** 参数为滤波器延迟指定非零初始条件。

要确定必须指定的初始状态数量以及如何指定它们，请参阅有效初始状态表。**Initial states** 参数可以采用下表中描述的形式之一。

**有效初始状态**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵（用于为每个通道应用不同的延迟元素） | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件：  - 向量长度等于输入通道数与滤波器中延迟元素数 `#_of_filter_coeffs-1`（对于 `Lattice MA` 为 `#_of_reflection_coeffs`）的乘积。 - 矩阵的行数必须等于滤波器中延迟元素数 `#_of_filter_coeffs-1`（对于 `Lattice MA` 为 `#_of_reflection_coeffs`），并且必须为输入信号的每个通道有一列。 |
