---
type: simulink-block
title: 'Trigger'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'trigger'
documentation_source_path: '../simulink/slref/trigger.html'
language: zh-CN
chinese_source: worker-translation
---

# Trigger

## 端口
```yaml
ports:
- name: Port_1
  summary: 描述控制信号或消息负载的值 标量 | 向量 | 矩阵
  direction: output
  data_types: double | int8
```

### 输出

### **Port\_1** — 描述控制信号或消息负载的值 标量 | 向量 | 矩阵

如果 **Trigger type** 为
`rising`、
`falling`、
`either` 或
`function-call`，则该端口输出一个用于标识控制信号的值，以标量或向量形式返回。对于输入信号的每个元素，给定时间步的值如下：

- `1` 表示引起上升触发的信号
- `-1` 表示引起下降触发的信号
- `2` 表示函数调用事件
- `0` 表示所有其他情况

如果 **Trigger type** 为
`message`，则该端口输出从控制端口接收的消息中提取的数据。

#### 依赖关系

要启用此端口，请选择 **Show output port**
或将 **Trigger type** 设置为
`message`。

**数据类型：** `double` | `int8`
## 参数
```yaml
parameters:
- name: Trigger type
  summary: 选择控制信号类型 rising（默认）| falling | either | function-call | message
  group: 主要
  block_parameter: TriggerType
  type: character vector
  values: '''rising'' | ''falling'' | ''either'' | ''function-call'' | ''message'''
  default: '''rising'''
- name: Treat as Simulink function
  summary: 创建 Simulink Function 模块 off（默认）| on
  group: 主要
  block_parameter: IsSimulinkFunction
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Execute function call asynchronously
  summary: 调用方请求调用函数是否可以等待服务执行 off（默认）| on
  group: 主要
  block_parameter: AsynchronousFunction
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Function name
  summary: 为 Simulink Function 模块指定函数名称 f（默认）| 函数名称
  group: 主要
  block_parameter: FunctionName
  type: character vector
  values: '''f'' | 带引号的函数名称'
  default: '''f'''
- name: Function visibility
  summary: 选择函数的范围可见性 scoped（默认）| global | port
  group: 主要
  block_parameter: FunctionVisibility
  type: character vector
  values: '''scoped'' | ''global'' | ''port'''
  default: '''scoped'''
- name: Scope to port
  summary: 指定导出函数端口的名称 ''（默认）| 字符向量
  group: 主要
  block_parameter: ScopeName
  type: character vector
  values: 带引号的端口名称
  default: ''''''
- name: Enable variant condition
  summary: 控制激活变体控制（条件）off（默认）| on
  group: 主要
  block_parameter: Variant
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Variant control
  summary: 指定变体控制（条件）表达式 (inherit)（默认）| 逻辑表达式
  group: 主要
  block_parameter: VariantControl
  type: character vector
  values: '''(inherit)'' | 逻辑表达式 | Simulink.VariantExpression 对象'
  default: '''(inherit)'''
- name: Generate preprocessor conditionals
  summary: 控制将变体选择包含在 C 预处理器条件语句中 off（默认）| on
  group: 主要
  block_parameter: GeneratePreprocessorConditionals
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: States when enabling
  summary: 选择如何设置模块状态值 held（默认）| reset | inherit
  group: 主要
  block_parameter: StatesWhenEnabling
  type: character vector
  values: '''held'' | ''reset''| ''inherit'''
  default: '''held'''
- name: Propagate sizes of variable-size signals
  summary: 选择何时传播可变大小信号 During execution（默认）| Only when enabling
  group: 主要
  block_parameter: PropagateVarSize
  type: character vector
  values: '''During execution'' | ''Only when enabling'''
  default: '''During execution'''
- name: Show output port
  summary: 控制输出端口的显示 off（默认）| on
  group: 主要
  block_parameter: ShowOutputPort
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output data type
  summary: 选择输出端口数据类型 auto（默认）| double | int8
  group: 主要
  block_parameter: OutputDataType
  type: character vector
  values: '''auto'' | ''double'' | ''int8'''
  default: '''auto'''
- name: Sample time type
  summary: 选择调用速率 triggered（默认）| periodic
  group: 主要
  block_parameter: SampleTimeType
  type: character vector
  values: '''triggered'' | ''periodic'''
  default: '''triggered'''
- name: Sample time
  summary: 指定时间间隔 1（默认）| Ts | [Ts, To] | -1
  group: 主要
  block_parameter: SampleTime
  type: character vector
  values: '''1'' | ''Ts''| ''[Ts, To]'' | ''-1'''
  default: '''1'''
- name: Enable zero-crossing detection
  summary: 控制零交叉检测 on（默认）| off
  group: 主要
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Initial trigger signal state
  summary: 选择触发信号 compatibility (no trigger on first evaluation)（默认）| zero | positive | negative 的初始状态
  group: 主要
  block_parameter: InitialTriggerSignalState
  type: 字符向量
  values: '''compatibility (no trigger on first evaluation)'' | ''zero'' | ''positive'' | ''negative'''
  default: '''compatibility (no trigger on first evaluation)'''
- name: Trigger time
  summary: 指定消息输入何时触发子系统执行 on message available（默认）| on sample time hit
  group: 主要
  block_parameter: TriggerTime
  type: 字符向量
  values: '''on message available'' | ''on sample time hit'''
  default: '''on message available'''
- name: Schedule as aperiodic partition
  summary: 指定执行的立即模式或调度模式 on（默认）| off
  group: 主要
  block_parameter: ScheduleAsAperiodic
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Port dimensions
  summary: 指定触发信号的维度 1（默认）| [n] | [m n] | -1
  group: 信号属性
  block_parameter: PortDimensions
  type: 字符向量
  values: '''1'' | ''[n]'' | ''[m n]'' | -1'
  default: '''1'''
- name: Trigger signal sample time
  summary: 指定时间间隔 -1（默认）| Ts | [Ts, To]
  group: 信号属性
  block_parameter: TriggerSignalSampleTime
  type: 字符向量
  values: '''-1'' | ''Ts''| ''[Ts, To]'''
  default: '''-1'''
- name: Minimum
  summary: 指定触发信号的最小输出值 []（默认）| 实数标量
  group: 信号属性
  block_parameter: OutMin
  type: 字符向量
  values: '''[]'' | 带引号的实数标量'
  default: '''[]'''
- name: Maximum
  summary: 指定触发信号的最大输出值 []（默认）| 实数标量
  group: 信号属性
  block_parameter: OutMax
  type: 字符向量
  values: '''[]'' | 带引号的实数标量'
  default: '''[]'''
- name: Data type
  summary: '选择触发信号的输出数据类型 Inherit: auto（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64
    | boolean | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^,0) | <data type expression>'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''
    | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: auto'''
- name: Mode
  summary: 选择数据类型类别 Built in（默认）| Fixed point | Expression
  group: 信号属性
- name: Interpolate data
  summary: 控制如何估计缺失的工作区数据 on（默认）| off
  group: 信号属性
  block_parameter: Interpolate
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
```

### 主要

### **Trigger type** — 选择控制信号类型 `rising`（默认）| `falling` | `either` | `function-call` | `message`

选择执行子系统或模型的控制信号类型。

- `rising` — 当控制信号从负值或零值上升到正值时，触发子系统或模型的执行。如果初始值为负值，信号上升到零也会触发执行。
- `falling` — 当控制信号从正值或零值下降到负值时，触发子系统或模型的执行。如果初始值为正值，信号下降到零也会触发执行。
- `either` — 当控制信号上升或下降时，触发子系统或模型的执行。
- `function-call` — 当控制端口从 Stateflow 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块接收到函数调用事件时，执行子系统或模型。
- `message` — 当控制端口有消息可用时，触发子系统的执行。该模块必须位于子系统内部。

#### 编程使用

|  |
| --- |
| **模块参数**：`TriggerType` |
| **类型**：character vector |
| **值**：`'rising'` | `'falling'` | `'either'` | `'function-call'` | `'message'` |
| **默认值**：`'rising'` |

### **Treat as Simulink function** — 创建 Simulink Function 模块 `off`（默认）| `on`

选择此参数可通过配置一个可由函数调用方带参数调用的 Subsystem 模块来创建 Simulink Function 模块。Trigger 模块必须位于该子系统内。您可以编辑显示在模块图标上的函数原型，以指定模块的输入和输出参数。

清除此参数可移除该配置。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为
`function-call`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IsSimulinkFunction` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Execute function call asynchronously** — 调用方请求调用函数是否可以等待服务执行 `off`（默认）| `on`

指定是否对包含此 Trigger 端口模块的子系统异步执行 Simulink Function 模块。

- 选择此参数可对*异步执行*进行建模，其中调用方（客户端）发出调用函数（服务端）的请求。函数根据 Schedule Editor 中定义的顺序执行，然后将输出参数返回给调用方。
- 清除此参数可对*同步执行*进行建模，其中调用方调用函数，函数立即运行，然后将输出参数返回给调用方。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，选择 **Treat as a Simulink Function**，并将 **Function visibility** 设置为
`port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`AsynchronousFunction` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Function name** — 为 Simulink Function 模块指定函数名称 `f`（默认）| 函数名称

为 Simulink Function 模块指定函数名称。或者，您可以通过编辑模块图标上的函数原型来指定名称。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，并选择 **Treat as a Simulink Function**。

#### 编程使用

|  |
| --- |
| **模块参数**：`FunctionName` |
| **类型**：character vector |
| **值**：`'f'` | 带引号的函数名称 |
| **默认值**：`'f'` |

### **Function visibility** — 选择函数的范围可见性 `scoped`（默认）| `global` | `port`

选择 Simulink Function 模块在子系统或模型中的范围。

- `scoped` — 将函数的可访问性限制为：

  - 包含 Simulink Function 模块的层级及其以下层级。
  - 带限定条件的一个上级层级。
- `global` — 函数可从模型层级中的任何部分访问。
- `port` — 函数仅可通过由 Function Element 模块创建的导出函数端口访问。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，并选择 **Treat as a Simulink Function**。

#### 编程使用

|  |
| --- |
| **模块参数**：`FunctionVisibility` |
| **类型**：character vector |
| **值**：`'scoped'` | `'global'` | `'port'` |
| **默认值**：`'scoped'` |

### **Scope to port** — 指定导出函数端口的名称 `''`（默认）| 字符向量

对于具有端口可见性的 Simulink Function 模块，指定由 Function Element 模块创建的导出函数端口的名称，通过该端口可以调用函数。

**示例：** `'ServerPort'`

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，选择 **Treat as a Simulink Function**，并将 **Function visibility** 设置为
`port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScopeName` |
| **类型**：character vector |
| **值**：带引号的端口名称 |
| **默认值**：`''` |

### **Enable variant condition** — 控制激活变体控制（条件）`off`（默认）| `on`

控制激活由 **Variant Control** 参数定义的变体控制（条件）。

选择此参数可激活子系统的变体控制。选择此参数：

- 启用 **Variant control** 参数。
- 在模块图标上显示变体徽章，表示变体条件已启用。

清除此参数可停用子系统的变体控制。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，并选择 **Treat as Simulink function**。

#### 编程使用

|  |
| --- |
| **模块参数**：`Variant` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Variant control** — 指定变体控制（条件）表达式 `(inherit)`（默认）| 逻辑表达式

指定变体控制（条件）表达式，当表达式求值为 `true` 时执行变体 Simulink Function 模块。

- `(inherit)` — 变体控制的默认值。从模型中相应的 Function Caller 模块继承变体条件。当 **Variant Control** 设置为 `(inherit)` 时，**Generate preprocessor conditionals** 的值会自动从模型中的 Function Caller 模块继承。
- 逻辑表达式 — 逻辑（布尔）表达式或表示逻辑表达式的 `Simulink.VariantExpression` 对象。当表达式求值为 `true` 时，函数被激活。

  如果要为模型生成代码，请将表达式中的变量定义为 `Simulink.Parameter` 对象。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `function-call`，选择 **Treat as a Simulink Function**，并选择 **Enable variant condition**。

#### 编程使用

|  |
| --- |
| **模块参数**：`VariantControl` |
| **类型**：character vector |
| **值**：`'(inherit)'` | 逻辑表达式 | `Simulink.VariantExpression` 对象 |
| **默认值**：`'(inherit)'` |

### **Generate preprocessor conditionals** — 控制将变体选择包含在 C 预处理器条件语句中 `off`（默认）| `on`

控制将变体选择包含在 C 预处理器条件语句中。

选择此参数可在为 ERT 目标生成代码时将变体选择包含在 C 预处理器条件语句（#if）中。

#### 依赖关系

要显示并启用此参数，请选择 **Enable variant condition**。

#### 编程使用

|  |
| --- |
| **模块参数**：`GeneratePreprocessorConditionals` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **States when enabling** — 选择如何设置模块状态值 `held`（默认）| `reset` | `inherit`

选择当子系统或模型被禁用时如何设置模块状态值。

- `held` — 将模块状态保持在其当前值。
- `reset` — 重置模块状态值。
- `inherit` — 使用发起函数调用的父子系统中的 `held` 或 `reset` 设置。如果发起方的父级是模型根，则继承的设置为 `held`。如果触发器有多个发起方，请将所有发起方的父级设置为 `held` 或 `reset`。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `function-call`。

此参数设置仅在模型显式启用和禁用函数调用子系统时适用。例如：

- 函数调用子系统位于一个使能子系统内。在这种情况下，模型随父子系统一起启用和禁用函数调用子系统。
- 控制函数调用子系统的函数调用发起方位于一个使能子系统内。在这种情况下，模型随包含函数调用发起方的使能子系统一起启用和禁用函数调用子系统。
- 函数调用发起方是绑定到特定状态的 Stateflow 事件。请参阅 Control Function-Call Subsystems by Using bind Actions (Stateflow)。
- 函数调用发起方是显式启用和禁用函数调用子系统的 S-function。请参阅 `ssEnableSystemWithTid` 获取示例。

#### 编程使用

|  |
| --- |
| **模块参数**：`StatesWhenEnabling` |
| **类型**：character vector |
| **值**：`'held'` | `'reset'`| `'inherit'` |
| **默认值**：`'held'` |

### **Propagate sizes of variable-size signals** — 选择何时传播可变大小信号 `During execution`（默认）| `Only when enabling`

选择何时传播可变大小信号。

- `During execution` — 在每个时间步传播可变大小信号。
- `Only when enabling` — 在执行包含 Enable 端口、**Trigger type** 设置为 `function-call` 的 Trigger 端口或 Action Port 模块的 Subsystem 模块或 Model 模块时传播可变大小信号。选择此选项时，采样时间必须为周期性。

#### 依赖关系

要为 Trigger 端口模块显示并启用此参数，请将 **Trigger type** 设置为 `Function-call`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PropagateVarSize` |
| **类型**：character vector |
| **值**：`'During execution'` | `'Only when enabling'` |
| **默认值**：`'During execution'` |

### **Show output port** — 控制输出端口的显示 `off`（默认）| `on`

控制用于标识触发信号或函数调用事件信号的输出端口的显示。

选择此参数可显示输出端口，并确定哪个信号引起了触发信号或函数调用事件。输出端口信号的宽度为控制信号的宽度。信号值为：

- `1` 表示引起上升触发的信号
- `-1` 表示引起下降触发的信号
- `2` 表示函数调用事件
- `0` 表示所有其他情况

清除此参数可移除输出端口。

#### 依赖关系

要显示并启用此参数，请将 **Trigger type** 设置为 `message` 以外的选项。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowOutputPort` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output data type** — 选择输出端口数据类型 `auto`（默认）| `double` | `int8`

选择用于标识触发信号或函数调用事件信号的输出端口数据类型。

- `auto` — 来自连接到输出的端口的数据类型
- `double` — 双精度值
- `int8` — 整数值

#### 依赖关系

要启用此参数，请选择 **Show output port**。

Trigger 模块忽略 Fixed-Point Tool 的 **Data type override** 设置。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputDataType` |
| **类型**：character vector |
| **值**：`'auto'` | `'double'` | `'int8'` |
| **默认值**：`'auto'` |

### **Sample time type** — 选择调用速率 `triggered`（默认）| `periodic`

选择子系统或模型的调用速率。

- `triggered`
  — 适用于没有周期性函数调用频率的应用。函数调用发起方可以在每个时间步执行一次或多次触发（非周期性）函数调用子系统，并可以提供一系列非周期性函数调用事件。
- `periodic` — 函数调用发起方在每个时间步只能执行一次周期性函数调用系统，并且必须提供一系列周期性函数调用事件。Stateflow 图是函数调用发起方的一个示例。

#### 依赖关系

要启用此参数，请将 **Trigger type** 设置为 `Function-call`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTimeType` |
| **类型**：character vector |
| **值**：`'triggered'` | `'periodic'` |
| **默认值**：`'triggered'` |

### **Sample time** — 指定时间间隔 `1`（默认）| `Ts` | `[Ts, To]` | `-1`

指定对包含此 Trigger 端口模块的子系统或模型的函数调用之间的时间间隔。如果子系统或模型的实际调用速率与此参数指定的时间间隔不同，软件将显示错误。

- `Ts` — 标量，其中 `Ts` 是时间间隔
- `[Ts, To]` — 向量，其中 `Ts` 是时间间隔，`To` 是初始时间偏移
- `-1` — 从控制信号继承的时间间隔

#### 依赖关系

要启用此参数，请将 **Trigger type** 设置为 `function-call`，并将 **Sample time type** 设置为 `periodic`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：`'1'` | `'Ts'`| `'[Ts, To]'` | `'-1'` |
| **默认值**：`'1'` |

### **Enable zero-crossing detection** — 控制零交叉检测 `on`（默认）| `off`

选择此参数可检测零交叉。

#### 依赖关系

要启用此参数，请将 **Trigger type** 设置为 `rising`、`falling` 或 `either`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Initial trigger signal state** — 选择触发信号 `compatibility (no trigger on first evaluation)`（默认）| `zero` | `positive` | `negative` 的初始状态

选择触发控制信号的初始状态。

- `compatibility (no trigger on first
  evaluation)` — 在触发信号的首次求值时不触发。如果选择此选项，并且 Trigger 模块位于状态被重置的子系统内，则该模块不会重置。
- `zero` — 零。有助于在第一个时间步对上升沿或下降沿触发信号进行求值。
- `positive` — 正值。有助于在第一个时间步对下降沿触发信号进行求值。
- `negative` — 负值。有助于在第一个时间步对上升沿触发信号进行求值。

#### 依赖关系

要显示并激活此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialTriggerSignalState` |
| **类型**：字符向量 |
| **值**：`'compatibility (no trigger on first evaluation)'` | `'zero'` | `'positive'` | `'negative'` |
| **默认值**：`'compatibility (no trigger on first evaluation)'` |

### **Trigger time** — 指定消息输入何时触发子系统执行 `on message available`（默认）| `on sample time hit`

对于由消息输入触发的子系统，指定执行时机。

- `on message available` — 当控制端口有一个或多个消息可用时，触发子系统执行并拉取消息。
- `on sample time hit` — 在每个时间步，检查控制端口是否有消息可用。如果有，则拉取一条消息并触发子系统执行。如果没有消息可用，则不在该时间步执行子系统。

#### 依赖关系

要显示并激活此参数，请将 **Trigger
type** 设置为 `message`。

#### 编程用法

|  |
| --- |
| **模块参数**：`TriggerTime` |
| **类型**：字符向量 |
| **值**：`'on message available'` | `'on sample time hit'` |
| **默认值**：`'on message available'` |

### **Schedule as aperiodic partition** — 指定执行的立即模式或调度模式 `on`（默认）| `off`

对于由消息可用性触发的子系统，指定执行模式。

清除此参数以使用*立即模式*，在该模式下，子系统在控制端口有消息可用时立即执行，控制端口将消息推送到子系统，而不使用队列缓冲消息。

选中此参数以使用*调度模式*，该模式允许子系统执行在特定 Simulink® 任务之后延迟，同时保持在同一时间步。

#### 依赖关系

要显示并激活此参数，请将 **Trigger
type** 设置为 `message`，并将
**Trigger time** 设置为 `on message
available`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScheduleAsAperiodic` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### 信号属性

### **Port dimensions** — 指定触发信号的维度 `1`（默认）| `[n]` | `[m n]` | `-1`

指定外部连接到 Model 模块并传入被引用模型的触发信号的维度。

- `1` — 标量信号
- `[n]` — 宽度为
  `n` 的向量信号
- `[m n]` — 具有
  `m` 行和 `n`
  列的矩阵信号
- `-1` — 继承维度

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`PortDimensions` |
| **类型**：字符向量 |
| **值**：`'1'` | `'[n]'` | `'[m n]'` | `-1` |
| **默认值**：`'1'` |

### **Trigger signal sample time** — 指定时间间隔 `-1`（默认）| `Ts` | `[Ts, To]`

指定驱动触发信号的模块的模块方法执行之间的时间间隔。

- `-1` — 继承时间间隔
- `Ts` — 标量，其中 `Ts` 是时间间隔
- `[Ts, To]` — 向量，其中
  `Ts` 是时间间隔，
  `To` 是初始时间偏移

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`TriggerSignalSampleTime` |
| **类型**：字符向量 |
| **值**：`'-1'` | `'Ts'`| `'[Ts, To]'` |
| **默认值**：`'-1'` |

### **Minimum** — 指定触发信号的最小输出值 `[]`（默认）| 实数标量

指定外部连接到 Model 模块并传递到模块内部的触发信号的最小值。

软件使用此值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 生成代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 带引号的实数标量 |
| **默认值**：`'[]'` |

### **Maximum** — 指定触发信号的最大输出值 `[]`（默认）| 实数标量

指定外部连接到 Model 模块并传递到模块内部的触发信号的最大值。

软件使用此值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 生成代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 带引号的实数标量 |
| **默认值**：`'[]'` |

### **Data type** — 选择触发信号的输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `<data type expression>`

选择外部连接到 Model 模块并传递到模块内部的触发信号的数据类型。

- `Inherit: auto` — 继承数据类型
- `double` — 双精度浮点
- `single` — 单精度浮点
- `int8` — 有符号 8 位整数
- `uint8` — 无符号 8 位整数
- `int16` — 有符号 16 位整数
- `uint16` — 无符号 16 位整数
- `int32` — 有符号 32 位整数
- `uint32` — 无符号 32 位整数
- `int64` — 有符号 64 位整数
- `uint64` — 无符号 64 位整数
- `boolean` — 值为
  `true` 或 `false` 的布尔值
- `fixdt(1,16)` — 二进制点未定义的有符号 16 位定点数
- `fixdt(1,16,0)` — 二进制点设置为零的有符号 16 位定点数
- `fixdt(1,16,2^,0)` — 斜率设置为 `2^0`、偏置设置为 `0` 的有符号 16 位定点数
- `<data type expression>` — 数据类型对象，例如 `Simulink.NumericType`
  对象

不能将 `Simulink.Bus` 对象的名称作为数据类型表达式输入。

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

### **Mode** — 选择数据类型类别 `Built in`（默认）| `Fixed point` | `Expression`

选择数据类型类别并显示下拉列表以帮助您定义数据类型。

- `Built in` — 显示数据类型和 **Data type override** 的菜单。
- `Fixed point` — 显示
  **Signedness**、
  **Scaling** 和 **Data type
  override** 的菜单。
- `Expression` — 显示用于输入表达式的文本框。

#### 依赖关系

要启用此参数，请选择 Show data type assistant
按钮 。

### **Interpolate data** — 控制如何估计缺失的工作区数据 `on`（默认）| `off`

控制从 MATLAB® 工作区加载数据时如何估计缺失的工作区数据。

选中此参数可对没有对应工作区数据的时间步处的输出进行线性插值。

清除此参数可将此类时间步处的输出设置为等于存在数据的最近时间步处的输出。

#### 依赖关系

要为模型根级别的 Trigger
port 模块显示并启用此参数，请将 **Trigger
type** 设置为 `rising`、
`falling` 或
`either`。

#### 编程用法

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |
## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

有关详细信息，请参阅 HDL Code Generation in Triggered Subsystem。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**限制**

无法为 **Trigger
type** 设置为 `function-call` 或
`message` 的 Trigger Block 生成 HDL 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

向子系统或模型添加触发端口或函数端口

Trigger 模块添加外部信号或消息端口，以控制子系统或模型的执行。要启用此功能，请将此模块添加到
Subsystem 模块中，或添加到在
Model 模块中引用的模型的根级别。

然后，配置 Trigger 模块以执行子系统或模型：

- 在每个时间步执行一次，当控制信号的值以您指定的方式变化时。
- 在一个时间步内执行多次，当控制信号是来自 Stateflow® 图、Function-Call Generator 模块或
  S-Function 模块的函数调用事件时。
- 基于在控制端口接收到的消息执行。
