---
type: simulink-block
title: 'Trigger'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'trigger'
---

# Trigger

Add trigger or function port to subsystem or model

## 中文

向子系统或模型添加触发器或函数端口

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

Trigger 模块可以添加外部信号或消息端口来控制子系统或模型的执行。要启用此功能，可在 Subsystem 模块中添加此模块，或在 Model 模块所引用模型的根级别添加此模块。

然后，对 Trigger 模块进行配置，以按下列方式之一执行子系统或模型：

- 当控制信号的值以您指定的方式更改时，在每个时间步执行一次。
- 当控制信号是来自 Stateflow® 图、Function-Call Generator 模块或 S-Function 模块的函数调用事件时，在一个时间步执行多次。
- 基于在控制端口接收的消息。

### 端口

#### 输出

#### **Port\_1** — 描述控制信号或消息有效负载的值 标量 | 向量 | 矩阵

如果**触发器类型**是**上升沿**、**下降沿**、**任一沿**或**函数调用**，则端口输出一个标识控制信号的值，以标量或向量形式返回。对于输入信号的每个元素，在给定时间步的值为：

- 对于启动上升触发器的信号，为 `1`
- 对于启动下降触发器的信号，为 `-1`
- 对于函数调用事件，为 `2`
- 对于所有其他情况，为 `0`

如果**触发器类型**是**消息**，则端口输出从控制端口接收的消息中提取的数据。

##### 依赖关系

要启用此端口，请选择**显示输出端口**或将**触发器类型**设置为**消息**。

**数据类型:** `double` | `int8`

### 参数

#### 常设

#### **触发器类型** — 选择控制信号的类型 **上升沿** (默认) | **下降沿** | **任一沿** | **函数调用** | **消息**

选择执行子系统或模型的控制信号的类型。

- **上升沿** - 当控制信号从负值或零值上升到正值时，触发子系统或模型的执行。如果初始值为负值，信号上升到零则触发执行。
- **下降沿** - 当控制信号从正值或零值下降到负值时，触发子系统或模型的执行。如果初始值为正值，则信号下降到零会触发执行。
- **任一沿** - 当控制信号上升或下降时，触发子系统或模型的执行。
- **函数调用** - 当控制端口接收到来自 Stateflow 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块的函数调用事件时，执行子系统或模型。
- **消息** - 当消息在控制端口上可用时，触发子系统的执行。模块必须在子系统内部。

##### 编程用法

|  |
| --- |
| **模块参数**：`TriggerType` |
| **类型：**字符向量 |
| **值：** `'rising'` | `'falling'` | `'either'` | `'function-call'` | `'message'` |
| **默认值：**`'rising'` |

#### **视为 Simulink 函数** — 创建 Simulink Function 模块 `off` (默认) | `on`

选择此参数可通过配置 Subsystem 模块，使其成为可使用参量从函数调用方调用的模块，以此来创建 Simulink Function 模块。Trigger 模块必须位于子系统内。您可以编辑显示在模块上的函数原型，以指定模块的输入和输出参量。

清除此参数以删除配置。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**。

##### 编程用法

|  |
| --- |
| **模块参数**：`IsSimulinkFunction` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **异步执行函数调用** — 调用函数的调用方请求是否可以等待服务执行 `off` (默认) | `on`

指定是否为包含此 Trigger 端口模块的子系统异步执行 Simulink Function 模块。

- 选中此参数可模拟*异步执行*，其中调用方（客户端）请求调用函数（服务器）。该函数根据在调度编辑器中定义的顺序执行，然后将输出参量返回到调用方。
- 清除此参数可模拟*同步执行*，其中调用方调用函数，函数立即运行，然后将输出参量返回到调用方。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，选择**视为 Simulink 函数**，并将**函数可见性**设置为**端口**。

##### 编程用法

|  |
| --- |
| **模块参数**：`AsynchronousFunction` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### **函数名称** — 指定 Simulink Function 模块的函数名称 `f` (默认) | 函数名称

指定 Simulink Function 模块的函数名称。您也可以通过在模块上编辑函数原型来指定名称。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，并选择**视为 Simulink 函数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`FunctionName` |
| **类型：**字符向量 |
| **值：**`'f'` | 用引号引起来的函数名称 |
| **默认值：**`'f'` |

#### **函数可见性** — 选择函数的作用域可见性 **限定作用域** (默认) | **全局** | **端口**

选择 Simulink Function 模块在子系统或模型内的作用域。

- **限定作用域** - 将函数的可访问性限制为以下作用域：

  - 包含 Simulink Function 模块的层次级别以及更低的级别。
  - 当前层级的上一级，但有一定限制。
- **全局** - 可从模型层次结构的任何部分访问函数。
- **端口** - 只能通过由 Function Element 模块创建的导出函数端口访问的函数。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，并选择**视为 Simulink 函数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`FunctionVisibility` |
| **类型：**字符向量 |
| **值**：`'scoped'` | `'global'` | `'port'` |
| **默认值：**`'scoped'` |

#### **示波器到端口** — 指定导出函数端口的名称 `''` (默认) | 字符向量

对于具有端口可见性的 Simulink Function 模块，指定由 Function Element 模块创建的导出函数端口的名称，通过该端口可以调用函数。

**示例:** `'ServerPort'`

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，选择**视为 Simulink 函数**，并将**函数可见性**设置为**端口**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ScopeName` |
| **类型：**字符向量 |
| **值：**用引号引起来的端口名称 |
| **默认值：**`''` |

#### **启用变体条件** — 控制是否激活变体控制项（条件） `off` (默认) | `on`

控制是否激活通过**变体控制项**参数定义的变体控制项（条件）。

选择此参数可激活子系统的变体控制项。选择此参数将：

- 启用**变体控制项**参数。
- 在模块上显示一个变体标志 ，指示变体条件已启用。

清除此参数可反激活子系统的变体控制项。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，并选择**视为 Simulink 函数**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Variant` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'on'` |

#### **变体控制项** — 指定变体控制项（条件）表达式 `(inherit)` (默认) | 逻辑表达式

指定变量控制项（条件）表达式，当该表达式的计算结果为 `true` 时执行变体 Simulink Function 模块。

- `(inherit)` - 变体控制项的默认值。从模型中相应的 Function Caller 模块继承变体条件。当**变体控制项**设置为 `(inherit)` 时，**生成预处理器条件句**的值将自动从该模型中的 Function Caller 模块继承。
- 逻辑表达式 - 逻辑（布尔）表达式或表示逻辑表达式的 `Simulink.VariantExpression` 对象。当表达式的计算结果为 `true` 时将激活函数。

  如果要为模型生成代码，请将表达式中的变量定义为 `Simulink.Parameter` 对象。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**函数调用**，选择**视为 Simulink 函数**，然后选择**启用变体条件**。

##### 编程用法

|  |
| --- |
| **模块参数**：`VariantControl` |
| **类型：**字符向量 |
| **值：**`'(inherit)'` | 逻辑表达式 | `Simulink.VariantExpression` 对象 |
| **默认值：**`'(inherit)'` |

#### **生成预处理器条件句** — 控制条件语句中包含的变体选择项 `off` (默认) | `on`

控制 C 预处理器条件语句中包含的变体选择项。

选择此参数可在为 ERT 目标生成代码时，在 C 预处理器条件语句 (#if) 中包含变体选择项。

##### 依赖关系

要显示和启用此参数，请选择**启用变体条件**。

##### 编程用法

|  |
| --- |
| **模块参数**：`GeneratePreprocessorConditionals` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **启用时的状态** — 选择如何设置模块状态值 **保持** (默认) | **重置** | **inherit**

选择当子系统或模型禁用时如何设置模块状态值。

- **保持** - 将模块状态保留为其当前值。
- **重置** - 重置模块状态值。
- **继承** - 使用发出函数调用的父级子系统的**保持**或**重置**设置。如果发起方的父级为模型根，则继承的设置为**保持**。如果触发器有多个发起方，则将所有发起方的父级设置为**保持**或**重置**。

##### 依赖关系

要启用此参数，请将**触发器类型**设置为**函数调用**。

只有模型明确启用和禁用函数调用子系统时，此参数设置才适用。例如：

- 函数调用子系统位于使能子系统中。在这种情况下，模型会随父级子系统一起启用和禁用函数调用子系统。
- 控制函数调用子系统的函数调用发起方位于使能子系统中。在这种情况下，模型会随包含函数调用发起方的使能子系统一起启用和禁用函数调用子系统以。
- 函数调用发起方是与特定状态绑定的 Stateflow 事件。请参阅Control Function-Call Subsystems by Using bind Actions (Stateflow)。
- 函数调用发起方是明确启用和禁用函数调用子系统的 S-Function。有关示例，请参阅 `ssEnableSystemWithTid`。

##### 编程用法

|  |
| --- |
| **模块参数**：`StatesWhenEnabling` |
| **类型：**字符向量 |
| **值：**`'held'` | `'reset'`| `'inherit'` |
| **默认值：**`'held'` |

#### **传播可变大小信号的大小** — 选择何时传播可变大小的信号 **执行期间** (默认) | **仅在启用时**

选择何时传播可变大小的信号。

- **执行期间** - 在每个时间步传播可变大小的信号。
- **仅在启用时** - 仅在执行 Action Port 模块时，或在执行包含 Enable 端口、Trigger 端口且**触发器类型**设置为**函数调用**的 Subsystem 模块或 Model 模块时，传播可变大小的信号。如果您选择此选项，采样时间必须为周期性采样时间。

##### 依赖关系

要为 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**函数调用**。

##### 编程用法

|  |
| --- |
| **模块参数**：`PropagateVarSize` |
| **类型：**字符向量 |
| **值**：`'During execution'` | `'Only when enabling'` |
| **默认值：**`'During execution'` |

#### **显示输出端口** — 控制输出端口的显示 `off` (默认) | `on`

控制是否为标识触发信号或函数调用事件信号的信号显示输出端口。

选择此参数可显示输出端口并确定哪个信号启动了触发器信号或函数调用事件。输出端口信号的宽度即为控制信号的宽度。信号值：

- 对于启动上升触发器的信号，为 `1`
- 对于启动下降触发器的信号，为 `-1`
- 对于函数调用事件，为 `2`
- 对于所有其他情况，为 `0`

清除此参数可删除输出端口。

##### 依赖关系

要显示和启用此参数，请将**触发器类型**设置为**消息**以外的选项。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowOutputPort` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **输出数据类型** — 选择输出端口的数据类型 `auto` (默认) | `double` | `int8`

为标识触发信号或函数调用事件信号的信号选择输出端口的数据类型。

- `auto` - 来自连接到输出的端口的数据类型
- `double` - 双精度值
- `int8` - 整数值

##### 依赖关系

要启用此参数，请选择**显示输出端口**。

Trigger 模块将忽略定点工具的**数据类型覆盖**设置。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputDataType` |
| **类型**：字符向量 |
| **值**：`'auto'` | `'double'` | `'int8'` |
| **默认值**：`'auto'` |

#### **采样时间类型** — 选择调用速率 **已触发** (默认) | **周期性**

选择子系统或模型的调用速率。

- **触发** - 适用于包含非周期函数调用的应用程序。函数调用发起方可以在每个时间步执行一次或多次触发的（非周期）函数调用子系统，并且可以提供一系列非周期函数调用事件。
- **周期性** - 函数调用发起方在每个时间步只能执行一次周期函数调用系统，并且必须提供一系列周期函数调用事件。Stateflow 图就是一个函数调用发起方示例。

##### 依赖关系

要启用此参数，请将**触发器类型**设置为**函数调用**。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTimeType` |
| **类型**：字符向量 |
| **值**：`'triggered'` | `'periodic'` |
| **默认值**：`'triggered'` |

#### **采样时间** — 指定时间间隔 `1` (默认) | `Ts` | `[Ts, To]` | `-1`

指定对包含此 Trigger 端口模块的子系统或模型的函数调用之间的时间间隔。如果子系统或模型的实际调用速率与此参数指定的时间间隔不同，软件将显示错误。

- `Ts` - 标量，其中 `Ts` 是时间间隔
- `[Ts, To]` - 向量，其中 `Ts` 是时间间隔，`To` 是初始时间偏移量
- `-1` - 从控制信号中继承时间间隔

##### 依赖关系

要启用此参数，请将**触发器类型**设置为**函数调用**，并将**采样时间类型**设置为**周期性**。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：`'1'` | `'Ts'` | `'[Ts, To]'` | `'-1'` |
| **默认值**：`'1'` |

#### **启用过零检测** — 控制过零检测 `on` (默认) | `off`

选择此参数可检测过零。

##### 依赖关系

要启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **初始触发信号状态** — 选择触发信号的初始状态 **兼容性(首次计算时不触发)** (默认) | **零** | **正值** | **负值**

选择触发器控制信号的初始状态。

- **兼容性(首次计算时不触发)** - 首次计算触发信号时不触发。如果选择此选项并且 Trigger  模块位于状态已重置的子系统中，则该模块不会重置。
- **零** - 零值。适合计算在第一个时间步上升或下降的触发信号。
- **正值** - 正值。适合计算在第一个时间步下降的触发信号。
- **负值** - 负值。适合计算在第一个时间步上升的触发信号。

##### 依赖关系

要显示和激活此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialTriggerSignalState` |
| **类型**：字符向量 |
| **值**：`'compatibility (no trigger on first evaluation)'` | `'zero'` | `'positive'` | `'negative'` |
| **默认值**：`'compatibility (no trigger on first evaluation)'` |

#### **触发时间** — 指定消息输入触发子系统执行的时间 **在消息可用时** (默认) | **在采样时间命中点上**

对于由消息输入触发的子系统，请指定执行时间。

- **在消息可用时** - 每当控制端口上有一个或多个消息可用时便触发子系统的执行并拉取消息。
- **在采样时间命中点上** - 在每个时间步，检查控制端口上是否有可用的消息。如果有，则拉取一条消息并触发子系统的执行。如果没有可用消息，则不在该时间步执行子系统。

##### 依赖关系

要显示和激活此参数，请将**触发器类型**设置为**消息**。

##### 编程用法

|  |
| --- |
| **模块参数**：`TriggerTime` |
| **类型**：字符向量 |
| **值**：`'on message available'` | `'on sample time hit'` |
| **默认值**：`'on message available'` |

#### **作为非周期性分区调度** — 指定执行模式为即时模式还是调度模式 `on` (默认) | `off`

对于由消息可用性触发的子系统，请指定执行模式。

对于*即时模式*，请清除此参数。在即时模式下，一旦控制端口上有消息可用，子系统就会执行，这会将消息推送到子系统而没有队列缓冲消息。

对于*调度模式*，请选中此参数。调度模式允许子系统在同一时间步上的特定 Simulink® 任务后执行。

##### 依赖关系

要显示和激活此参数，请将**触发器类型**设置为**消息**，将**触发时间**设置为**在消息可用时**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ScheduleAsAperiodic` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

#### 信号属性

#### **端口维度** — 指定触发信号的维度 `1` (默认) | `[n]` | `[m n]` | `-1`

指定外部连接到 Model 模块并传入引用模型中的触发信号的维度。

- `1` - 标量信号
- `[n]` - 宽度为 `n` 的向量信号
- `[m n]` - 具有 `m` 行和 `n` 列的矩阵信号
- `-1` - 继承的维度

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`PortDimensions` |
| **类型**：字符向量 |
| **值**：`'1'` | `'[n]'` | `'[m n]'` | `-1` |
| **默认值**：`'1'` |

#### **触发信号采样时间** — 指定时间间隔 `-1` (默认) | `Ts` | `[Ts, To]`

指定驱动触发信号的模块的各次模块方法执行之间的时间间隔。

- `-1` - 继承的时间间隔
- `Ts` - 标量，其中 `Ts` 是时间间隔
- `[Ts, To]` - 向量，其中 `Ts` 是时间间隔，`To` 是初始时间偏移量

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`TriggerSignalSampleTime` |
| **类型**：字符向量 |
| **值**：`'-1'` | `'Ts'`| `'[Ts, To]'` |
| **默认值**：`'-1'` |

#### **最小** — 指定触发信号的最小输出值 `[]` (默认) | 实数标量

指定从外部连接到 Model 模块并传递到模块内部的触发信号的最小值。

软件使用此值执行：

- 仿真范围检查。请参阅指定信号范围。
- 定点数据类型的自动定标。
- 所生成代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMin` |
| **类型**：字符向量 |
| **值**：`'[]'` | 用引号引起来的实数标量 |
| **默认值**：`'[]'` |

#### **最大** — 指定触发信号的最大输出值 `[]` (默认) | 实数标量

指定从外部连接到 Model 模块并传递到模块内部的触发信号的最大值。

软件使用此值执行：

- 仿真范围检查。请参阅指定信号范围。
- 定点数据类型的自动定标。
- 所生成代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutMax` |
| **类型**：字符向量 |
| **值**：`'[]'` | 用引号引起来的实数标量 |
| **默认值**：`'[]'` |

#### **数据类型** — 选择触发信号的输出数据类型 **Inherit: auto** (默认) | **double** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^,0)** | **<数据类型表达式>**

选择从外部连接到 Model 模块并传递到模块内部的触发信号的数据类型。

- **继承: 自动** - 继承的数据类型
- **double** - 双精度浮点
- **single** - 单精度浮点
- **int8** - 有符号 8 位整数
- **uint8** - 无符号 8 位整数
- **int16** - 有符号 16 位整数
- **uint16** - 无符号 16 位整数
- **int32** - 有符号 32 位整数
- **uint32** - 无符号 32 位整数
- **int64** - 有符号 64 位整数
- **uint64** - 无符号 64 位整数
- **布尔** - 值为 `true` 或 `false` 的布尔值
- **fixdt(1,16)** - 未定义二进制小数点位置的有符号 16 位定点数
- **fixdt(1,16,0)** - 二进制小数点位置设置为零的有符号 16 位定点数
- **fixdt(1,16,2^,0)** - 斜率设置为 `2^0` 且偏置设置为 `0` 的有符号 16 位定点数
- **<数据类型表达式>** - 数据类型对象，例如 `Simulink.NumericType` 对象

您不能以数据类型表达式的形式输入 `Simulink.Bus` 对象的名称。

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: auto'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: auto'` |

#### **模式** — 选择数据类型类别 **内置** (默认) | **定点** | **表达式**

选择数据类型类别并显示下拉列表以帮助您定义数据类型。

- **内置** - 显示数据类型和**数据类型覆盖**的菜单。
- **定点** - 显示**符号性**、**定标**和**数据类型覆盖**的菜单。
- **表达式** - 显示用于输入表达式的文本框。

##### 依赖关系

要启用此参数，请选择“显示数据类型助手”按钮 。

#### **数据插值** — 控制如何估算缺失的工作区数据 `on` (默认) | `off`

控制从 MATLAB® 工作区加载数据时如何估算缺失的工作区数据。

选择此参数可在不存在对应工作区数据的时间步上对输出进行线性插值。

清除此参数可将在此类时间步上的输出设置为等于存在数据的最近时间步上的输出。

##### 依赖关系

要为模型根级别的 Trigger 端口模块显示和启用此参数，请将**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

##### 编程用法

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

有关详细信息，请参阅Triggered Subsystem中的 HDL 代码生成。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**限制**

对于**触发器类型**设置为**函数调用**或**消息**的 Trigger 模块，无法生成 HDL 代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The Trigger block adds an external signal or message port to control
the execution of a subsystem or a model. To enable this functionality, add this block to
a Subsystem block or at the root level of a model that is referenced in a
Model block.

Then, configure the Trigger block to execute a subsystem or
model:

- Once at each time step, when the value of the control signal changes in a way
  that you specify.
- Multiple times during a time step, when the control signal is a function-call
  event from a Stateflow® chart, Function-Call Generator block, or
  S-Function block.
- Based on messages received at the control port.

## Ports

### Output

### **Port\_1** — Value that describes control signal or message payload scalar | vector | matrix

If the **Trigger type** is
`rising`,
`falling`,
`either`, or
`function-call`, the port outputs a value
that identifies a control signal, returned as a scalar or vector. For
each element of the input signal, the value at a given time step
is:

- `1` for a signal that causes a rising
  trigger
- `-1` for a signal that causes a falling
  trigger
- `2` for a function-call event
- `0` in all other cases

If the **Trigger type** is
`message`, the port outputs data extracted
from message received at the control port.

#### Dependencies

To enable this port, select **Show output port**
or set **Trigger type** to
`message`.

**Data Types:** `double` | `int8`

## Parameters

### Main

### **Trigger type** — Select the type of control signal `rising` (default) | `falling` | `either` | `function-call` | `message`

Select the type of control signal that executes a subsystem or
model.

- `rising` — Trigger execution of
  subsystem or model when the control signal rises from a negative
  or zero value to a positive value. If the initial value is
  negative, a rising signal to zero triggers execution.
- `falling` — Trigger execution of
  subsystem or model when the control signal falls from a positive
  or a zero value to a negative value. If the initial value is
  positive, a falling signal to zero triggers execution.
- `either` — Trigger execution of
  subsystem or model when the control signal is either rising or
  falling.
- `function-call` — Execute subsystem
  or model when the control port receives a function-call event
  from a Stateflow chart, Function-Call Generator
  block, S-Function block, or Hit
  Crossing block.
- `message` — Trigger execution of
  subsystem when a message is available at the control port. The
  block must be inside a subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TriggerType` |
| **Type:** character vector |
| **Values:** `'rising'` | `'falling'` | `'either'` | `'function-call'` | `'message'` |
| **Default:** `'rising'` |

### **Treat as Simulink function** — Create Simulink Function block `off` (default) | `on`

Select this parameter to create a Simulink Function
block by configuring a Subsystem block that is callable
with arguments from a function caller. The Trigger block
must reside within the subsystem. You can edit the function prototype
that displays on the block face to specify input and output arguments
for the block.

Clear this parameter to remove the configuration.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to
`function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsSimulinkFunction` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Execute function call asynchronously** — Whether caller request to call function can wait for service execution `off` (default) | `on`

Specify whether to execute the Simulink Function block
asynchronously for a subsystem containing this Trigger
port block.

- Select this parameter to model *asynchronous
  execution* where the caller (client) makes a
  request to call the function (server). The function is executed
  based on the ordering defined in the Schedule Editor and then returns the output
  arguments to the caller.
- Clear this parameter to model *synchronous
  execution* where the caller calls the function
  and the function runs immediately then returns the output
  arguments to the caller.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and set
**Function visibility** to
`port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AsynchronousFunction` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

### **Function name** — Specify function name for Simulink Function block `f` (default) | function name

Specify the function name for a Simulink Function
block. Alternatively, you can specify the name by editing the function
prototype on the face of the block.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as a Simulink Function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionName` |
| **Type:** character vector |
| **Values:** `'f'` | function name in quotes |
| **Default:** `'f'` |

### **Function visibility** — Select scope visibility of function `scoped` (default) | `global` | `port`

Select scope of Simulink Function block within
subsystem or model.

- `scoped` — Limit accessibility of
  function to:

  - Hierarchic level containing the Simulink
    Function block and levels below.
  - One hierarchical level above with
    qualification.
- `global` — Function accessible from
  any part of the model hierarchy.
- `port` — Function accessible only
  through an exporting function port created by a Function
  Element block.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as a Simulink Function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionVisibility` |
| **Type:** character vector |
| **Values:** `'scoped'` | `'global'` | `'port'` |
| **Default:** `'scoped'` |

### **Scope to port** — Specify name of exporting function port `''` (default) | character vector

For a Simulink Function block with port visibility,
specify the name of the exporting function port created by a Function
Element block through which the function can be
called.

**Example:** `'ServerPort'`

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and set
**Function visibility** to
`port`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScopeName` |
| **Type:** character vector |
| **Values:** port name in quotes |
| **Default:** `''` |

### **Enable variant condition** — Controls activating the variant control (condition) `off` (default) | `on`

Control activating the variant control (condition) defined with the
**Variant Control** parameter.

Select this parameter to activate variant control of the subsystem.
Selecting this parameter:

- Enables the **Variant control**
  parameter.
- Displays a variant badge  on the face of the block
  indicating that variant conditions are enabled.

Clear this parameter to deactivate variant control of the
subsystem.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call` and
select **Treat as Simulink function**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Variant` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Variant control** — Specify variant control (condition) expression `(inherit)` (default) | logical expression

Specify variant control (condition) expression that executes a variant
Simulink Function block when the expression evaluates
to `true`.

- `(inherit)` — Default value for variant
  control. Inherits the variant condition from the corresponding
  Function Caller blocks in the model. When
  **Variant Control** is set as
  `(inherit)` the value for
  **Generate preprocessor conditionals** is
  inherited automatically from the Function Caller
  block in the model.
- logical expression — A logical (Boolean) expression or a
  `Simulink.VariantExpression` object
  representing a logical expression. The function is activated
  when the expression evaluates to `true`.

  If you want to generate code for your model, define the
  variables in the expression as
  `Simulink.Parameter` objects.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to `function-call`,
select **Treat as a Simulink Function**, and
select **Enable variant condition**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantControl` |
| **Type:** character vector |
| **Values:** `'(inherit)'` | logical expression | `Simulink.VariantExpression` object |
| **Default:** `'(inherit)'` |

### **Generate preprocessor conditionals** — Control enclosing variant choices `off` (default) | `on`

Control enclosing variant choices within C preprocessor conditional
statements.

Select this parameter to enclose variant choices within C preprocessor
conditional statements (#if) when generating code for an ERT
target.

#### Dependencies

To display and enable this parameter, select **Enable
variant condition** .

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GeneratePreprocessorConditionals` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **States when enabling** — Select how to set block state values `held` (default) | `reset` | `inherit`

Select how to set block state values when the subsystem or model is
disabled.

- `held` — Leave the block states at
  their current values.
- `reset` — Reset the block state
  values.
- `inherit` — Use the
  `held` or
  `reset` setting from the parent
  subsystem initiating the function-call. If the parent of the
  initiator is the model root, the inherited setting is
  `held`. If the trigger has multiple
  initiators, set the parents of all initiators to either
  `held` or
  `reset`.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`function-call`.

This parameter setting applies only if the model explicitly
enables and disables the function-call subsystem. For
example:

- The function-call subsystem resides in an enabled
  subsystem. In this case, the model enables and disables
  the function-call subsystem along with the parent
  subsystem.
- The function-call initiator that controls the
  function-call subsystem resides in an enabled subsystem.
  In this case, the model enables and disables the
  function-call subsystem along with the enabled subsystem
  containing the function-call initiator.
- The function-call initiator is a Stateflow event bound to a particular state. See
  Control Function-Call Subsystems by Using bind Actions (Stateflow).
- The function-call initiator is an S-function that
  explicitly enables and disables the function-call
  subsystem. See `ssEnableSystemWithTid` for an
  example.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StatesWhenEnabling` |
| **Type:** character vector |
| **Values:** `'held'` | `'reset'`| `'inherit'` |
| **Default:** `'held'` |

### **Propagate sizes of variable-size signals** — Select when to propagate variable-size signals `During execution` (default) | `Only when enabling`

Select when to propagate variable-size signals.

- `During execution` — Propagate
  variable-size signals at each time step.
- `Only when enabling` — Propagate
  variable-size signals when executing a Subsystem
  block or Model block containing an
  Enable port, Trigger port with
  **Trigger type** set to
  `function-call`, or Action
  Port block. When you select this option, sample time
  must be periodic.

#### Dependencies

To display and enable this parameter for a Trigger
port block, set **Trigger type** to
`Function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PropagateVarSize` |
| **Type:** character vector |
| **Values:** `'During execution'` | `'Only when enabling'` |
| **Default:** `'During execution'` |

### **Show output port** — Control display of output port `off` (default) | `on`

Control display of an output port for a signal that identifies the
trigger signal or function-call event signal.

Select this parameter to display the output port and determine which
signal caused the trigger signal or function-call event. The width of
the output port signal is the width of the control signal. The signal
value is:

- `1` for a signal that causes a rising
  trigger
- `-1` for a signal that causes a falling
  trigger
- `2` for a function-call event
- `0` in all other cases

Clear this parameter to remove the output port.

#### Dependencies

To display and enable this parameter, set **Trigger
type** to an option other than
`message`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPort` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output data type** — Select output port data type `auto` (default) | `double` | `int8`

Select the output port data type for the signal that identifies the
trigger signal or function-call event signal.

- `auto` — Data type from the port connected to
  the output
- `double` — Double value
- `int8` — Integer value

#### Dependencies

To enable this parameter, select **Show output
port**.

The Trigger block ignores the **Data type override** setting for the Fixed-Point
Tool.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputDataType` |
| **Type**: character vector |
| **Values**: `'auto'` | `'double'` | `'int8'` |
| **Default**: `'auto'` |

### **Sample time type** — Select calling rate `triggered` (default) | `periodic`

Select the calling rate for a subsystem or model.

- `triggered`
  — Apply to applications that do not have a periodic
  function-call frequency. A function-call initiator can execute a
  triggered (aperiodic) function-call subsystem one or more times
  per time step and can provide a series of aperiodic
  function-call events.
- `periodic` — A function-call
  initiator can execute a periodic function-call system only once
  per time step and must provide a series of periodic
  function-call events.. A Stateflow chart is an example of a function-call
  initiator.

#### Dependencies

To enable this parameter, set **Trigger type**
to `Function-call`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTimeType` |
| **Type**: character vector |
| **Values**: `'triggered'` | `'periodic'` |
| **Default**: `'triggered'` |

### **Sample time** — Specify time interval `1` (default) | `Ts` | `[Ts, To]` | `-1`

Specify the time interval between function calls to a subsystem or
model containing this Trigger port block. If the actual
calling rate for the subsystem or model differs from the time interval
this parameter specifies, the software displays an error.

- `Ts` — Scalar where `Ts` is
  the time interval
- `[Ts, To]` — Vector where
  `Ts` is the time interval and
  `To` is the initial time offset
- `-1` — Inherited time interval from the
  control signal

#### Dependencies

To enable this parameter, set **Trigger type**
to `function-call` and **Sample
time type** to
`periodic`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `'1'` | `'Ts'`| `'[Ts, To]'` | `'-1'` |
| **Default**: `'1'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Select this parameter to detect zero crossings.

#### Dependencies

To enable this parameter, set **Trigger type** to
`rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Initial trigger signal state** — Select the initial state of the trigger signal `compatibility (no trigger on first evaluation)` (default) | `zero` | `positive` | `negative`

Select the initial state of the trigger control signal.

- `compatibility (no trigger on first
  evaluation)` — No trigger at the first
  evaluation of trigger signal. If you choose this option and the
  Trigger block is in a subsystem where the
  states are reset, the block does not reset.
- `zero` — Zero. Helps to evaluate a
  rising or falling trigger signal at the first time step.
- `positive` — Positive value. Helps to
  evaluate a falling trigger signal at the first time step.
- `negative` — Negative value. Helps to
  evaluate a rising trigger signal at the first time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialTriggerSignalState` |
| **Type**: character vector |
| **Values**: `'compatibility (no trigger on first evaluation)'` | `'zero'` | `'positive'` | `'negative'` |
| **Default**: `'compatibility (no trigger on first evaluation)'` |

### **Trigger time** — Specify when message input triggers execution of subsystem `on message available` (default) | `on sample time hit`

For a subsystem triggered by message input, specify timing of execution.

- `on message available` — Trigger
  execution of subsystem and pull messages whenever one or
  more messages are available at the control port.
- `on sample time hit` — At each
  time step, check whether a message is available at the
  control port. If so, pull one message and trigger execution
  of subsystem. If no message is available, do not execute
  subsystem at that time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `message`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TriggerTime` |
| **Type**: character vector |
| **Values**: `'on message available'` | `'on sample time hit'` |
| **Default**: `'on message available'` |

### **Schedule as aperiodic partition** — Specify immediate mode or scheduled mode for execution `on` (default) | `off`

For a subsystem triggered by message availability, specify execution
mode.

Clear this parameter for *immediate mode*, in
which the subsystem executes as soon as a message is available at the
control port, which pushes the message to the subsystem without a queue
buffering the message.

Select this parameter for *scheduled mode*, which
allows subsystem execution to be deferred after a specific Simulink® task while staying at the same time step.

#### Dependencies

To display and activate this parameter, set **Trigger
type** to `message` and
**Trigger time** to `on message
available`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScheduleAsAperiodic` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### Signal Attributes

### **Port dimensions** — Specify dimensions for the trigger signal `1` (default) | `[n]` | `[m n]` | `-1`

Specify dimensions for the trigger signal attached externally a
Model block and passed into the referenced
model.

- `1` — Scalar signal
- `[n]` — Vector signal of width
  `n`
- `[m n]` — Matrix signal having
  `m` rows and `n`
  columns
- `-1` — Inherited dimensions

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PortDimensions` |
| **Type**: character vector |
| **Values**: `'1'` | `'[n]'` | `'[m n]'` | `-1` |
| **Default**: `'1'` |

### **Trigger signal sample time** — Specify time interval `-1` (default) | `Ts` | `[Ts, To]`

Specify time interval between block method executions for the block
driving the trigger signal.

- `-1` — Inherited time interval
- `Ts` — Scalar where `Ts` is
  the time interval
- `[Ts, To]` — Vector where
  `Ts` is the time interval and
  `To` is the initial time offset

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TriggerSignalSampleTime` |
| **Type**: character vector |
| **Values**: `'-1'` | `'Ts'`| `'[Ts, To]'` |
| **Default**: `'-1'` |

### **Minimum** — Specify minimum output value for the trigger signal `[]` (default) | real scalar

Specify minimum value for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

The software uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | real scalar in quotes |
| **Default**: `'[]'` |

### **Maximum** — Specify maximum output value for the trigger signal `[]` (default) | real scalar

Specify maximum value for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

The software uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | real scalar in quotes |
| **Default**: `'[]'` |

### **Data type** — Select output data type for the trigger signal `Inherit: auto` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `<data type expression>`

Select data type for the trigger signal attached externally to a
Model block and passed to the inside of the
block.

- `Inherit: auto` — Inherited data
  type
- `double` — Double-precision floating
  point
- `single` — Single-precision floating
  point
- `int8` — Signed 8-bit integer
- `uint8` — Unsigned 8-bit
  integer
- `int16` — Signed 16-bit
  integer
- `uint16` — Unsigned 16-bit
  integer
- `int32` — Signed 32-bit
  integer
- `uint32` — Unsigned 32-bit
  integer
- `int64` — Signed 64-bit
  integer
- `uint64` — Unsigned 64-bit
  integer
- `boolean` — Boolean with a value of
  `true` or `false`
- `fixdt(1,16)` — Signed 16-bit fixed
  point number with binary point undefined
- `fixdt(1,16,0)` — Signed 16-bit fixed
  point number with binary point set to zero
- `fixdt(1,16,2^,0)` — Signed 16-bit
  fixed point number with slope set to `2^0` and
  bias set to `0`
- `<data type expression>` — Data
  type object, for example a `Simulink.NumericType`
  object

You cannot enter the name of a `Simulink.Bus` object as
a data type expression.

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: auto'` |

### **Mode** — Select data type category `Built in` (default) | `Fixed point` | `Expression`

Select data type category and display drop-down lists to help you
define the data type.

- `Built in` — Display menus for data
  type and **Data type override**.
- `Fixed point` — Display menus for
  **Signedness**,
  **Scaling**, and **Data type
  override**.
- `Expression` — Display text box for
  entering an expression.

#### Dependencies

To enable this parameter, select the Show data type assistant
button .

### **Interpolate data** — Control how missing workspace data is estimated `on` (default) | `off`

Control how missing workspace data is estimated when loading data from
the MATLAB® workspace.

Select this parameter to linearly interpolate output at time steps for
which no corresponding workspace data exists.

Clear this parameter to set the output at such time steps equal to the
output at the most recent time step for which data exists.

#### Dependencies

To display and enable this parameter for a Trigger
port block at the root-level of a model, set **Trigger
type** to `rising`,
`falling`, or
`either`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Interpolate` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

For more information, see HDL Code Generation in Triggered Subsystem.

**HDL Architecture**

This block has one default HDL architecture.

**Restriction**

You cannot generate HDL code for a Trigger Block that has **Trigger
type** set to `function-call` or
`message`.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
