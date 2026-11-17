---
type: simulink-block
title: 'Chart'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: ''
documentation_page: 'chart'
documentation_source_path: 'ref/chart.html'
language: zh-CN
chinese_source: worker-translation
---

# Chart

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入端口 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | string
- name: Port_1
  summary: 输出端口 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | string
```

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow 图中创建输入数据时，Stateflow 会在 Chart 模块上创建相应的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用 **Symbols** 窗格在 Stateflow 图中创建输出数据时，Stateflow 会在 Chart 模块上创建相应的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
## 参数
```yaml
parameters:
- name: Update method
  summary: 更新或唤醒 Stateflow 图的方法 Inherited（默认）| Discrete | Continuous
  group: ''
  block_parameter: ChartUpdate
  values: '"INHERITED"（默认）| "CONTINUOUS" | "DISCRETE"'
- name: Sample Time
  summary: Stateflow 图在仿真期间唤醒的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认） | 字符串标量 | 字符向量'
- name: Enable zero-crossing detection
  summary: 是否在图中状态转换上启用零交叉检测 on（默认） | off
  group: ''
  block_parameter: EnableZeroCrossings
  values: true 或 1（默认） | false 或 0
- name: Enable C-bit operations
  summary: 是否在图中启用 C 位运算 off（默认） | on
  group: ''
  block_parameter: EnableBitOps
  values: false 或 0（默认） | true 或 1
- name: Create output for monitoring
  summary: 是否创建活动状态数据输出 off（默认） | on
  group: ''
  block_parameter: HasOutputData
  values: false 或 0（默认） | true 或 1
- name: Output monitoring mode
  summary: 活动状态输出的监控模式 Child activity（默认） | Leaf state activity
  group: ''
  block_parameter: OutputMonitoringMode
  values: '"ChildActivity"（默认） | "LeafStateActivity"'
- name: Data name
  summary: 活动状态数据对象的名称 ChartMode | 标量
  group: ''
  block_parameter: OutputPortName
  values: '"ChartMode"（默认） | 字符串标量 | 字符向量'
- name: Enum name
  summary: 活动状态数据对象的枚举数据类型名称 ChartModeType | 标量
  group: ''
  block_parameter: EnumTypeName
  values: '"ChartModeType"（默认） | 字符串标量 | 字符向量'
- name: 手动定义枚举类型
  summary: 是否手动定义枚举数据类型 off（默认） | on
  group: ''
  block_parameter: DoNotAutogenerateEnum
  values: false 或 0（默认） | true 或 1
- name: 在初始化时执行（进入）图
  summary: 是否初始化状态配置 off（默认） | on
  group: 高级
  block_parameter: ExecuteAtInitialization
  values: false 或 0（默认） | true 或 1
- name: 整数溢出时饱和
  summary: 数据在整数溢出时是否饱和 on（默认） | off
  group: 高级
  block_parameter: SaturateOnIntegerOverflow
  values: true 或 1（默认） | false 或 0
- name: 每次图唤醒时初始化输出
  summary: 是否初始化输出数据 on（默认） | off
  group: 高级
  block_parameter: InitializeOutput
  values: true 或 1（默认） | false 或 0
- name: 支持可变大小数组
  summary: 图是否支持可变大小数据 on（默认） | off
  group: 高级
  block_parameter: SupportVariableSizing
  values: true 或 1（默认） | false 或 0
- name: Export chart level functions
  summary: 是否导出图级函数 off（默认） | on
  group: 高级
  block_parameter: ExportChartFunctions
  values: false 或 0（默认） | true 或 1
- name: Treat exported functions as globally visable
  summary: 导出的函数是否全局可见 off（默认） | on
  group: 高级
  block_parameter: AllowGlobalAccessToExportedFunctions
  values: false 或 0（默认） | true 或 1
- name: Enable super step semantics
  summary: 是否启用超步语义 off（默认） | on
  group: 高级
  block_parameter: EnableNonTerminalStates
  values: false 或 0（默认） | true 或 1
- name: Max iterations in a superstep
  summary: 最大转移次数 1000（默认） | 正整数
  group: 高级
  block_parameter: NonTerminalMaxCounts
  values: 1000（默认） | 正整数
- name: After too many iterations
  summary: 超步超过最大转移次数时的操作 Proceed（默认） | Throw Error
  group: 高级
  block_parameter: NonTerminalUnstableBehavior
  values: '"Proceed"（默认） | "Throw Error"'
- name: 将长度为 1 的维度视为固定大小
  summary: 图是否将长度为 1 的非标量数据视为固定大小 on（默认） | off
  group: 高级
  block_parameter: TreatDimensionOfLengthOneAsFixedSize
  values: true 或 1（默认） | false 或 0
- name: 变体激活时间
  summary: 在仿真和代码生成工作流的不同阶段主动选择变体模块或变体参数 update diagram analyze all choices（默认） | code compile
  group: 高级
  block_parameter: VariantActivationTime
  values: '"update diagram analyze all choices"（默认） | "code compile"'
- name: 动作语言
  summary: 动作语言 MATLAB（默认） | C
  group: 高级
  block_parameter: ActionLanguage
  values: '"MATLAB"（默认） | "C"'
- name: 状态机类型
  summary: 状态机语义 Classic（默认） | Mealy | Moore
  group: 高级
  block_parameter: StateMachineType
  values: '"Classic"（默认） | "Mealy" | "Moore"'
- name: 将这些继承的 Simulink 信号类型视为 fi 对象
  summary: 要视为 fi 对象的继承 Simulink 信号 Fixed-point（默认）| Fixed-point & Integer
  group: 定点属性
  block_parameter: TreatAsFi
  values: '"Fixed-point"（默认）| "Fixed-point & Integer"'
- name: MATLAB Chart fimath
  summary: 默认 fimath 属性 Same as MATLAB（默认）| Specify Other
  group: 定点属性
  block_parameter: EmlDefaultFimath
  values: '"Same as MATLAB Default"（默认）| "Other:UserSpecified"'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

**注意**

图还具有 Subsystem (Simulink) 模块参数，您可以通过右键单击图并单击 **Block Parameters (Subsystem)** 来访问这些参数。但是，不建议更新这些参数。

### **Update method** — 更新或唤醒 Stateflow 图的方法 `Inherited`（默认）| `Discrete` | `Continuous`

用于更新或唤醒 Stateflow 图的方法，指定为 `Inherited`、`Discrete` 或 `Continuous`。

`Inherited`
:   Simulink 模型的输入决定图在仿真期间何时唤醒。

    如果您为图定义了输入事件，则连接到触发端口的 Simulink 模块发出的信号会触发该图。Simulink 信号可以是 `Rising`、`Falling` 或 `Either`（上升沿和下降沿），也可以响应 `Function Call`。有关详细信息，请参阅 Activate a Stateflow Chart by Sending Input Events。

    如果您未定义输入事件，则 Stateflow 图会隐式继承 Simulink 模型的触发。这些隐式事件是为图提供输入的 Simulink 信号的离散或连续采样时间。如果您定义了数据输入，则图以最快数据输入的速率唤醒。如果您没有为图定义任何数据输入，则图按其父级子系统的执行行为所定义的方式唤醒。

`Discrete`
:   当 Simulink 模型以您在 **Sample Time** 图属性中指定的固定时间间隔生成隐式事件时，Stateflow 图会唤醒。Simulink 模型中的其他模块可以具有不同的采样时间。

`Continuous`
:   Stateflow 图仅在主时间步期间更新其状态，并在主时间步和次时间步期间计算输出和局部连续变量。图可以注册零交叉，这允许 Simulink 模型在状态发生变化时对 Stateflow 图进行采样。Stateflow 图为局部连续变量计算导数。有关详细信息，请参阅 Continuous-Time Modeling in Stateflow。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ChartUpdate` |
| **值：** | `"INHERITED"`（默认）| `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample Time** — Stateflow 图在仿真期间唤醒的时间间隔 `-1`（默认）| 标量 | 向量

指定图在仿真期间唤醒的时间间隔。默认值表示图从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅 Specify Sample Time (Simulink)。

不要使用 Subsystem 模块参数中的 **Sample Time** 参数。而应使用属性检查器。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Discrete`。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 字符串标量 | 字符向量 |
| **数据类型：** | `string` | `char` |

### **Enable zero-crossing detection** — 是否在图中状态转换上启用零交叉检测 `on`（默认） | `off`

是否在图中状态转换上启用零交叉检测。有关详细信息，请参阅 Stateflow 中的连续时间建模。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Continuous`。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableZeroCrossings` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **Enable C-bit operations** — 是否在图中启用 C 位运算 `off`（默认） | `on`

是否在图中状态和转换动作中使用位运算，指定为数值或逻辑 1（true）或 0（false）。

#### 依赖关系

要启用此参数，请将 **Action language** 设置为 `C`。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableBitOps` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **Create output for monitoring** — 是否创建活动状态数据输出 `off`（默认） | `on`

是否为图创建活动状态数据输出端口。有关详细信息，请参阅通过活动状态数据监控状态活动。

#### 依赖关系

要启用此参数，请创建 Stateflow 状态、状态转换表或原子子图。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `HasOutputData` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **Output monitoring mode** — 活动状态输出的监控模式 `Child activity`（默认） | `Leaf state activity`

活动状态输出数据的监控模式。有关详细信息，请参阅通过活动状态数据监控状态活动。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `OutputMonitoringMode` |
| **值：** | `"ChildActivity"`（默认） | `"LeafStateActivity"` |

### **Data name** — 活动状态数据对象的名称 `ChartMode` | 标量

状态转换表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `OutputPortName` |
| **值：** | `"ChartMode"`（默认） | 字符串标量 | 字符向量 |
| **数据类型：** | `string` | `char` |

### **Enum name** — 活动状态数据对象的枚举数据类型名称 `ChartModeType` | 标量

状态转换表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnumTypeName` |
| **值：** | `"ChartModeType"`（默认） | 字符串标量 | 字符向量 |
| **数据类型：** | `string` | `char` |

### **手动定义枚举类型** — 是否手动定义枚举数据类型 `off`（默认） | `on`

是否手动为活动状态数据输出定义枚举数据类型。有关详细信息，请参阅 Define State Activity Enumeration Type。

#### 依赖关系

要启用此参数，请启用 **Create output for monitoring**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `DoNotAutogenerateEnum` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### 高级

### **在初始化时执行（进入）图** — 是否初始化状态配置 `off`（默认） | `on`

是否在零时刻而不是在第一个输入事件时初始化图的状态配置。有关详细信息，请参阅 Execution of a Chart at Initialization。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ExecuteAtInitialization` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **整数溢出时饱和** — 数据在整数溢出时是否饱和 `on`（默认） | `off`

图中的数据在整数溢出时是否饱和。当您清除此参数时，图中的数据在整数溢出时回绕。有关详细信息，请参阅 Handle Integer and Enumeration Overflow for Chart Data。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **每次图唤醒时初始化输出** — 是否初始化输出数据 `on`（默认） | `off`

是否在每次图唤醒时初始化输出数据。

当您选择此参数时，图会在每次唤醒时重置其输出值，而不仅仅是在时刻 0。图会在函数调用、边沿触发或时钟节拍触发图时重置输出值。如果您为输出数据对象设置了初始值，则输出将重置为该值。否则，输出将重置为零。选择此参数以：

- 确保在每次图执行时定义所有输出。
- 防止输出锁存，即防止先前执行中计算的输出值。
- 为所有图输出提供有意义的初始值。

有关详细信息，请参阅 Initial value。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `InitializeOutput` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **支持可变大小数组** — 图是否支持可变大小数据 `on`（默认） | `off`

图是否支持可变大小数据。有关详细信息，请参阅 Declare Variable-Size Data in Stateflow Charts。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SupportVariableSizing` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **Export chart level functions** — 是否导出图级函数 `off`（默认） | `on`

是否将图级函数导出到 Simulink 模型中的其他模块。有关详细信息，请参阅 Export Stateflow Functions for Reuse。

#### 依赖关系

要启用此参数，请向图中添加一个函数。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ExportChartFunctions` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **Treat exported functions as globally visable** — 导出的函数是否全局可见 `off`（默认） | `on`

从图中导出的函数在 Simulink 模型中是否全局可见。启用此属性后，模型中的模块无需使用限定表示法即可调用从图中导出的函数。

#### 依赖关系

要启用此参数，请启用 **Export chart level functions**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `AllowGlobalAccessToExportedFunctions` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **Enable super step semantics** — 是否启用超步语义 `off`（默认） | `on`

是否为图启用超步语义。选择此参数可使图在每个时间步中执行多个转移，直到达到稳定状态。当您将图属性 **Update method** 设置为 `Continuous` 时，此选项不可用。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Discrete`。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableNonTerminalStates` |
| **值：** | `false` 或 `0`（默认） | `true` 或 `1` |
| **数据类型：** | `logical` |

### **Max iterations in a superstep** — 最大转移次数 `1000`（默认） | 正整数

在一个超步中可以完成的最大转移次数。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请启用 **Enable super step semantics**。

#### 程序化使用

要以编程方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalMaxCounts` |
| **值：** | `1000`（默认） | 正整数 |
| **数据类型：** | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` |

### **After too many iterations** — 超步超过最大转移次数时的操作 `Proceed`（默认） | `Throw Error`

当超步超过一个超步中的最大转移次数时，Stateflow 要执行的操作。有关详细信息，请参阅 Super Step Semantics。

#### 依赖关系

要启用此参数，请启用 **Enable super step semantics**。

#### 编程使用

要以编程方式设置图参数值，请访问图的
`Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalUnstableBehavior` |
| **值：** | `"Proceed"`（默认） | `"Throw Error"` |

### **将长度为 1 的维度视为固定大小** — 图是否将长度为 1 的非标量数据视为固定大小 `on`（默认） | `off`

*自 R2022b 起*

图是否将某个维度长度为 1 的非标量数据视为固定大小。当您选中此参数时，无论是否启用 **Variable
size** 数据属性，图都会将至少有一个维度长度为 1 的非标量数据视为固定
大小。当您清除此参数时，
图会将启用了 **Variable
size** 属性的非标量数据视为可变大小。

#### 编程使用

要以编程方式设置图参数值，请访问图的
`Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **变体激活时间** — 在仿真和代码生成工作流的不同阶段主动选择变体模块或变体参数 `update diagram analyze all choices`（默认） | `code compile`

指定 Stateflow 在仿真和代码生成期间分析哪些模块变体。根据您选择的选项，Stateflow 确定生成的代码必须仅包含
活动选择，还是同时包含活动和非活动选择。

- `update diagram analyze all choices`
  — 当您选择此选项时，Stateflow 会分析活动和非活动选择在信号属性方面的
  不兼容性，并仅针对活动选择生成代码。
- `code compile` — 当您选择此
  选项时，Stateflow 会分析变体转移的活动和非活动选择，
  并同时为活动和非活动选择生成代码。这些选择包含在 C 预处理器
  条件语句 #if 和 #endif 中，在编译生成的代码时进行条件
  编译。

#### 编程使用

要以编程方式设置图参数值，请访问图的
`Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `VariantActivationTime` |
| **值：** | `"update diagram analyze all choices"`（默认） | `"code compile"` |

### **动作语言** — 动作语言 `MATLAB`（默认） | `C`

用于对图进行编程的动作语言，指定为
`MATLAB` 或 `C`。有关更多
信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。

#### 编程使用

要以编程方式设置图参数值，请访问图的
`Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ActionLanguage` |
| **值：** | `"MATLAB"`（默认） | `"C"` |

### **状态机类型** — 状态机语义 `Classic`（默认） | `Mealy` | `Moore`

由图实现的状态机语义，指定为
`Classic`、`Mealy` 或
`Moore`。有关更多信息，请参阅 Overview of Mealy and Moore Machines。

#### 编程使用

要以编程方式设置图参数值，请访问图的
`Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `StateMachineType` |
| **值：** | `"Classic"`（默认） | `"Mealy"` | `"Moore"` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 要视为 `fi` 对象的继承 Simulink 信号 `Fixed-point`（默认）| `Fixed-point & Integer`

要视为 Fixed-Point Designer™ `fi` 对象的继承 Simulink 信号，指定为以下值之一：

- `Fixed-point` — 该图将所有定点输入视为 `fi` 对象。
- `Fixed-point & Integer` — 该图将所有定点和整数输入视为 `fi` 对象。

#### 依赖关系

要启用此参数，请将 **Action language** 设置为 `MATLAB`。

#### 编程用法

要以编程方式设置图参数值，请访问该图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatAsFi` |
| **值：** | `"Fixed-point"`（默认）| `"Fixed-point & Integer"` |

### **MATLAB Chart fimath** — 默认 `fimath` 属性 `Same as MATLAB`（默认）| `Specify Other`

该图的默认 `fimath` 属性，指定为以下值之一：

- `Same as MATLAB` — 该图使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框将变暗，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` — 通过以下两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框中构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名。如果您使用此选项并计划与他人共享您的模型，请在模型工作区中定义该变量。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)。

#### 依赖关系

要启用此参数，请将 **Action language** 设置为 `MATLAB`。

#### 编程用法

要以编程方式设置图参数值，请访问该图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EmlDefaultFimath` |
| **值：** | `"Same as MATLAB Default"`（默认）| `"Other:UserSpecified"` |
## 所属库

Stateflow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**活动状态输出**

要在 HDL 代码中生成显示活动状态的输出端口，请在图表的属性窗口中选择 **Create output for monitoring**。该输出为枚举数据类型。参见 Simplify Stateflow Charts by Incorporating Active State Output。

**寄存输出**

要插入一个将图表输出延迟一个仿真周期的输出寄存器，请使用 OutputPipeline (HDL Coder) 模块属性。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ClockDrivenOutput** | 启用时钟驱动输出，以防止组合逻辑驱动输出，并允许在时钟信号和状态变化时立即更新输出。默认值为 `off`。当您将 **ClockDrivenOutput** 设置为 `on` 时，HDL Coder 会添加一个在状态更新时更新的输出寄存器。最终输出变量随后从时钟驱动寄存器赋值。此选项仅适用于 Moore 图表。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参见 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参见 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 `inherit`。另请参见 DistributedPipelining (HDL Coder)。 |
| **GuardIndexVariables** | 指定是否将数组索引提升到条件语句之外。当您启用某些优化（如 RAM 映射、循环流式处理、共享等）时，表达式会被移出数组索引。会为可能导致仿真期间索引越界错误的表达式创建临时变量。默认值为 `off`。参见 GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成一个 VHDL® `entity` 或 Verilog® `module`。默认值为 `off`。另请参见 InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开、流式处理或不优化循环。默认值为 `none`。另请参见 LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 `off`。另请参见 MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参见 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参见 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数量。默认值为 0。另请参见 Resource Sharing (HDL Coder)。 |

**优化**

此模块参与以下 HDL 优化，以优化速度和面积。

**速度和面积优化**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中已有的延迟以减少关键路径，同时保持功能行为。 |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等价的资源，并将它们替换为单个资源。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型的关键路径上引入延迟时，*延迟平衡*会检测到在一条路径上引入的新延迟，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，它允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化通过向设计中的模块插入流水线寄存器，创建带有寄存器的模式或模块组合，从而提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中被表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

要了解使用图的限制，请参阅 Introduction to Stateflow HDL Code Generation (HDL Coder)。

当您应用优化时，该模块具有以下限制：

- **State Machine Type** 属性设置为 `Moore` 的 Stateflow Chart 不支持 HDL 优化。
- 具有 **Trigger** 端口的 Stateflow Chart 不支持 HDL 优化。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

**PLC Block properties**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 在生成的代码中抑制模块定义。默认值为 `Off`。另请参阅 UseExternalDefinition (Simulink PLC Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a: Implicit ordering of transitions and parallel states will be removed

在未来的版本中，属性 **User-specified state/transition execution order** 将被移除。此属性仅适用于使用 C 作为动作语言的图。

- 当您启用此属性时，图按照您创建它们的顺序执行转移和并行状态。您也可以手动确定执行顺序。
- 当您禁用此属性时，图根据物理位置定义的隐式顺序执行转移和并行状态。

  转移按照以下顺序执行：

  1. 每个转移的父级的层级。
  2. 转移的标签，按以下顺序：

     1. 带有事件和条件的标签。
     2. 带有事件的标签。
     3. 带有条件的标签。
     4. 无标签。
  3. 转移源的角表面位置。时钟位置最小的转移具有最高优先级。例如，2 点钟位置的转移比 4 点钟位置的转移具有更高的优先级。源位置为 12 点钟的转移具有最低优先级。

  并行状态按照以下顺序执行：

  1. 从上到下。
  2. 从左到右。

为确保您的隐式排序图保持兼容，请启用 **User-specified state/transition execution order** 属性。

### R2023b: Convert to state transition table

要将图转换为状态转移表，请使用函数 `convertToSTT`。

### R2023a: 指定如何处理维度长度为 1 的非标量数据

通过新增属性 **Treat dimensions of length 1 as fixed size**，您可以指定当至少一个维度的长度为 1 时，图表如何处理非标量数据。在 R2023a 之前，无论是否启用 **Variable size** 数据属性，图表都会将至少一个维度长度为 1 的非标量数据视为固定大小。

## 描述

使用有限状态机实现控制逻辑

Chart 模块以图形方式表示有限状态机。在 Stateflow® 图表中，状态和转移构成顺序模态逻辑系统的基本构建块。状态对应于运行模式，转移表示系统从一种运行模式到另一种运行模式的过渡。有关详细信息，请参阅 Model a Finite State Machine。

为实现控制逻辑，Stateflow 图表可以使用 MATLAB® 或 C 作为动作语言。有关详细信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。
