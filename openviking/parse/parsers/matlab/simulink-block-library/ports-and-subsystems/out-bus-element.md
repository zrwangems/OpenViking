---
type: simulink-block
title: 'Out Bus Element'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'outbuselement'
---

# Out Bus Element

Specify output of external port

## 中文

指定外部端口的输出

### 库

Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Ports & Subsystems HDL Coder / Sinks

### 描述

Out Bus Element 模块提供一个总线、信号或消息作为外部端口的输出。

要将多个总线、信号或消息分组到一个输出总线中，请使用多个与同一端口对应的 Out Bus Element 模块。Out Bus Element 模块组合了 Bus Creator 模块和 Outport 模块的功能。所有与同一端口对应的 Out Bus Element 模块共享一个对话框。

对于包含由许多总线元素组成的总线的接口，Out Bus Element 模块：

- 减少框图中信号线的复杂度和杂乱。
- 允许您更轻松地对接口进行增量更改。
- 允许在更接近使用点处访问总线元素，避免使用 Bus Creator 和 From 模块配置。

要将接口转换为使用 Out Bus Element 模块，请参阅 Simplify Subsystem and Model Interfaces with Bus Element Ports。

Out Bus Element 模块不支持将消息元素和信号元素混合作为输入。

当您将输出数据保存到工作区或文件时，由根级 Out Bus Element 模块组定义的总线数据会与根级 Outport 模块数据一起记录。

### 端口

#### 输入

#### **Port\_1** — 外部端口的完整或部分输出 scalar | vector | matrix | array | bus

连接一个总线、信号或消息，以传递到父子系统或模型的对应外部输出端口。

当多个 Out Bus Element 模块与同一外部端口关联时，此模块的输入是输出端口处总线的一个元素。模块标签中的第二个文本字段指定元素名称。

当只有一个 Out Bus Element 模块与该外部端口关联时，此模块的输入会直接传递到输出端口，或嵌套在输出端口处的总线中。要将模块的输入传递到输出端口而不将其嵌套在总线中，请删除模块标签中第二个文本字段中的文本。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** Yes

### 参数

要编辑与 Out Bus Element 模块关联的元素，请在 Simulink® Editor 中编辑模块标签。

要编辑端口、信号和执行属性，请使用 Property Inspector。在 Simulink 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

#### 模块标签

#### **Port name** — 输出端口的名称 `OutBus`（默认） | 端口名称

指定一个端口名称，该名称尚未被系统内的其他模块或端口使用。该名称会显示在父 Subsystem 或 Model 模块上。

要从 Simulink Editor 更改端口名称，请编辑模块标签的第一个文本字段。

默认 Out Bus Element 模块，其中 OutBus 在模块标签中高亮显示

多个模块可以为同一端口提供输出，只要每个模块为该端口的一个唯一元素提供输出。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `"OutBus"`（默认） | 带引号的端口名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

#### **Element** — 可选的 Bus 元素规格 `signal1`（默认） | 元素路径

要在输出端口创建 Bus，请在模块标签的第二个文本字段中指定一个元素。

默认 Out Bus Element 模块，其中 signal1 在模块标签中高亮显示

如何指定元素取决于该元素在 Bus 层级中的位置。

- 对于输出总线顶层的元素，请指定元素名称，例如 `constant`。
- 对于嵌套 Bus 中的元素，请指定嵌套 Bus 的名称、中间嵌套 Bus 和叶信号，用点分隔，例如 `sinusoidal.sine`。此元素路径不包括顶层 Bus。

每个输出元素必须唯一，并且不得与该端口的其他元素重叠。例如，对于嵌套 Bus，请使用一个对应嵌套 Bus 的 Out Bus Element 模块，或使用多个对应嵌套 Bus 元素的 Out Bus Element 模块。

要输出信号、消息或 Bus 而不创建 Bus，请删除模块标签第二个文本字段中的文本。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `"signal1"`（默认） | 带引号的元素路径 |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="constant")`

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="sinusoidal.sine")`

#### 端口选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

*R2025a 之前：要指定属性，例如输出名称，请暂停在顶层总线、信号或消息的名称上。然后，点击 Specify attributes。或者，在可用时，点击属性摘要。*

有关端口名称的信息，请参阅 **Port name**。

#### **Port number** — 端口在父模块上的位置 `1`（默认） | 实整数

指定与该模块对应的端口在父 Subsystem 或 Model 模块上出现的顺序。

- 如果添加一个会创建另一个端口的模块，则端口编号为下一个可用编号。
- 删除与某个端口关联的所有模块会删除该端口。其他端口会重新编号，使其连续且不跳过任何编号。
- 指定超过端口数量的端口编号会为该编号以及任何跳过的连续编号创建端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `"1"`（默认） | 带引号的实整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

#### **Output name** — 父子系统或模型中输出总线、信号或消息的名称 无默认值

*自 R2023a 起*

指定父子系统或模型中输出总线、信号或消息的名称。该名称会作为线条上的标签显示。

要显示模型中单条线或所有线的传播标签，请参阅 Display Propagated Signal Labels。

#### 依赖关系

- 要启用此参数：

  - 该模块必须位于模型的顶层。
  - 该元素必须是顶层总线、信号或消息。
- 当您将 **Data type** 设置为 `Simulink.Bus` 对象时，软件会将此参数设置为 `""`（空）。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutputName` |
| **值：** | `""`（默认） | 带引号的输出名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/OutBus",OutputName="model-output")`

#### **Initial output** — 父条件执行子系统的初始输出 `[]`（默认） | 标量 | 结构体

*自 R2024b 起*

对于条件执行子系统，请指定子系统执行之前以及子系统禁用时的模块输出。要从输入信号继承初始输出值，请应用以下两个默认设置：

- 将 **Initial output** 设置为 `[]`。
- 将 **Output when disabled** 设置为 `held`。

软件会尝试从输入信号继承输出值。如果输入信号不是初始输出值的有效来源，则初始输出值 `[]` 会被视为 `double(0)`。有关详细信息，请参阅 Conditional Subsystem Initial Output Values。

有关指定初始条件结构的信息，请参阅 Specify Initial Conditions for Bus Elements。

#### 提示

如果条件子系统驱动 Merge 模块，则无需为 Out Bus Element 模块指定初始条件。有关详细信息，请参阅 Underspecified initialization detection。

#### 依赖关系

要启用此参数：

- 该模块必须位于条件执行子系统或模型的顶层。
- 该元素必须是顶层总线、信号或消息。

#### 限制

- 此模块不支持 `inf` 或 `NaN` 的初始输出。
- 当输入为虚拟总线时，**Initial output** 值 `[]` 会被视为 `double(0)`。
- 当输入包含非虚拟总线时，**Initial output** 不支持非零标量值。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialOutput` |
| **值：** | `'[]'`（默认） | 带引号的标量 | 带引号的结构体 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mdl/condss/Output",InitialOutput="3")`

#### **Output when disabled** — 父条件执行子系统禁用时的输出 `held`（默认） | `reset`

*自 R2024b 起*

指定当父条件执行子系统禁用时模块输出会发生什么。

- `held` — 当子系统禁用时，输出保持。
- `reset` — 当子系统禁用时，输出重置为 **Initial output** 给定的值。

#### 提示

- 如果父子系统的输出连接到 Merge 模块，请勿将此参数设置为 `reset`。
- 对于 function-call 子系统中的 Out Bus Element 模块，仅当 Function-Call Subsystem 模块连接到 Stateflow® 图中的状态时，此参数才有意义。有关详细信息，请参阅 Bind a Function-Call Subsystem to a State (Stateflow)。

#### 依赖关系

要启用此参数：

- 该模块必须位于具有有效启用和禁用语义的条件子系统顶层。例如，enabled 子系统中的 Out Bus Element 模块支持此参数，但 triggered 子系统中的 Out Bus Element 模块不支持此参数。
- 该元素必须是顶层总线、信号或消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputWhenDisabled` |
| **值：** | `"held"`（默认） | `"reset"` |

**示例：** `set_param("mdl/condss/Output",InitialOutput="3",OutputWhenDisabled="reset")`

#### 信号选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

当您指定属性时，相应总线、信号或消息的名称旁边会出现一个括号说明。要完整显示指定的属性，请点击属性摘要。

指针暂停在总线名称旁边的属性摘要上

*R2025a 之前：要指定属性，例如数据类型，请暂停在总线、信号或消息的名称上。然后，点击 Specify attributes。或者，在可用时，点击属性摘要。*

#### **Data type** — 数据类型 `Inherit: auto`（默认） | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

总线、信号或消息的数据类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType` 对象。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Data Types Supported by Simulink。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称，并在前面加上 `Enum:`。例如，指定 `Enum: myEnumType`。
- Bus 数据类型 — 使用 `Simulink.Bus` 对象名称，并在前面加上 `Bus:`。例如，指定 `Bus: myBusObject`。
- 值类型 — 使用 `Simulink.ValueType` 对象名称，并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `"Fixed-point: unspecified scaling"` 以外的值。

当您将 `Simulink.ValueType` 对象指定为数据类型时，元素的一些参数会被忽略。例如，**Min**、**Max** 和 **Unit** 参数会被忽略。软件会使用 `Simulink.ValueType` 对象的对应属性。例如，假设您为某个元素将 **Unit** 设置为 `ft/s`。当该元素的 **Data type** 指定了一个单位为 `m/s` 的 `ValueType` 对象时，该元素会使用 `m/s` 而不是 `ft/s`。

当您将 `Simulink.Bus` 对象指定为数据类型时，元素的一些参数会重置为其默认值。例如，**Min**、**Max** 和 **Unit** 参数会被重置。软件会改为使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。

#### 提示

- 当您使用 `Simulink.Bus` 对象或具有 `Simulink.Bus` 对象数据类型的 `Simulink.ValueType` 对象指定总线时，Property Inspector 和模块对话框会显示由相应 `Simulink.BusElement` 对象定义的元素。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请点击 Open Type Editor。

#### 依赖关系

要将 `Simulink.Bus` 对象指定为总线元素端口处总线的数据类型，Out Bus Element 模块必须表示该总线或该总线的一个元素。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"`（默认） | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16)"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"string"` | `"Enum: <class name>"` | `"Bus: <object name>"` | `"ValueType: <object name>"` | 带引号的数据类型表达式 |

**示例：** `set_param("mymodel/myBus.signal1",OutDataTypeStr="int32")`

#### **Data mode** — 输出元素的数据模式 `inherit`（默认） | `signal` | `message`

指定输出元素的数据模式。

- `inherit` — 输出元素继承其数据模式。
- `signal` — 输出元素必须是信号或包含信号的总线。
- `message` — 输出元素必须是消息或包含消息的总线。

#### 依赖关系

要启用此参数，该模块必须位于模型的顶层。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `DataMode` |
| **值：** | `"inherit"`（默认） | `"signal"` | `"message"` |

**示例：** `set_param("mymodel/OutBus",DataMode="signal")`

#### **Bus virtuality** — 虚拟或非虚拟总线 `inherit`（默认） | `virtual` | `nonvirtual`

指定是继承总线虚拟性，还是将总线定义为虚拟或非虚拟。有关详细信息，请参阅 Composite Interface Guidelines。

此参数确定模块是继承还是定义总线虚拟性。如果模块定义总线虚拟性，并且输入总线的虚拟性不匹配，则编译模型会产生错误。

#### 依赖关系

要启用此参数，**Data type** 必须解析为 `Simulink.Bus` 对象。例如，将 **Data type** 设置为 `Simulink.Bus` 对象或将其数据类型指定为 `Simulink.Bus` 对象的 `Simulink.ValueType` 对象。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `BusVirtuality` |
| **值：** | `"inherit"`（默认） | `"virtual"` | `"nonvirtual"` |

**示例：** `set_param("mymodel/myBus.nestedBus",BusVirtuality="nonvirtual")`

#### **Dimensions** — 信号维度 `-1`（默认） | 整数 | `1`×`2` 的整数向量

指定信号的维度。

- `-1` — 信号可以具有任意维度。
- `N` — 信号必须是大小为 `N` 的向量。
- `[R C]` — 信号必须是具有 `R` 行和 `C` 列的矩阵。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `1`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的维度。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `PortDimensions` |
| **值：** | `"-1"`（默认） | 带引号的整数 | 带引号的 `1`×`2` 整数向量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/myBus.signal1",PortDimensions="[1
3]")`

#### **Dimensions mode** — 允许仅可变大小或固定大小信号的选项 `Inherit`（默认） | `Fixed` | `Variable`

指定允许的信号类型。

- `Inherit` — 允许可变大小和固定大小信号。
- `Variable` — 仅允许可变大小信号。
- `Fixed` — 仅允许固定大小信号。不允许可变大小信号。

当信号为可变大小时，**Dimensions** 参数指定信号的最大维度。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `Inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度模式。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的维度模式。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `VarSizeSig` |
| **值：** | `"Inherit"`（默认） | `"No"` | `"Yes"` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",VarSizeSig="No")`

#### **Unit** — 物理单位 `inherit`（默认） | Simulink 软件支持的单位

指定信号的物理单位。有关支持的单位列表，请在 MATLAB Command Window 中输入 `showunitslist`。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的单位。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的单位。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `Unit` |
| **值：** | `"inherit"`（默认） | 带引号的 Simulink 软件支持的单位 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/myBus.signal1",Unit="m/s")`

#### **Complexity** — 数值类型 `auto`（默认） | `real` | `complex`

指定信号的数值类型。要选择信号的数值类型，请选择 `auto`。否则，选择实数或复数信号类型。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `auto`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的复数性。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的复数性。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `SignalType` |
| **值：** | `"auto"`（默认） | `"real"` | `"complex"` |

**示例：** `set_param("mymodel/myBus.signal1",SignalType="real")`

#### **Minimum** — 最小值 `[]`（默认） | 标量

软件检查范围的下限值。

此数字必须是有限实数 double 标量值。

软件使用此值来执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最小值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的最小值。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `"[]"`（默认） | 带引号的标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",OutMin="0")`

#### **Maximum** — 最大值 `[]`（默认） | 标量

软件检查范围的上限值。

此数字必须是有限实数 double 标量值。

软件使用此值来执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最大值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的最大值。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `"[]"`（默认） | 带引号的标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",OutMax="2")`

#### **Description** — 总线、信号或消息的描述 无默认值

使用描述来记录有关总线、信号或消息的信息，例如其使用位置。此信息不影响处理。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件会将此参数设置为 `""`（空）。软件使用 `Simulink.Bus` 对象指定的描述。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件会忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的描述。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `Description` |
| **值：** | `""`（默认） | 带引号的描述 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",Description="This signal is
used by...")`

#### 执行选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

当您指定属性时，相应总线、信号或消息的名称旁边会出现一个括号说明。要显示指定的属性，请点击 Specify execution attributes。

指针暂停在总线名称旁边的 Specify execution attributes 按钮上

*R2025a 之前：要指定执行属性，请暂停在总线、信号或消息的名称上。然后，点击 Specify execution attributes。*

#### **Sample time** — 采样时间 `-1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time。

默认情况下，信号继承其采样时间。

#### 编程使用

要编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层级，用点分隔层级中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",SampleTime="0.01")`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

当您在生成 HDL 代码的子系统中使用此模块时，此模块可用于简化子系统总线接口，但它不包含在硬件实现中。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

此模块支持针对 `Simulink.ValueType` 对象的代码生成。有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type。

**数据类型支持**

此模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2017a 中引入**

#### R2025a: 更轻松地指定端口、信号和执行属性

现在，您可以更轻松地指定端口、信号和执行属性。

- 要切换端口、信号和执行属性的显示，请点击 Show attributes 或 Hide attributes。端口、信号和执行属性现在显示在选项卡上。Show attributes 或 Hide attributes 按钮取代了以前版本中暂停在总线、信号或消息名称上时出现的按钮。
- 当您指定执行属性时，相应总线、信号或消息的名称旁边现在会出现一个括号说明。要显示指定的属性，请点击 Specify execution attributes。
- 要编辑端口名称，请双击顶层总线、信号或消息的名称。或者，在 **Port** 选项卡上，指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements，然后选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上点击 Open Type Editor。
- **Dims mode** 现在命名为 **Dimensions mode**。

#### R2024b: 指定初始条件

在条件执行子系统和模型中，Out Bus Element 模块现在支持顶层元素上的初始条件。对于非总线信号，请将 **Initial output** 设置为与信号具有相同维度和复数性的值。对于总线，请将 **Initial output** 设置为 MATLAB 结构体，其字段具有与总线元素相同的名称和层级。要指定子系统禁用时模块输出会发生什么，请使用 **Output when disabled** 模块参数。

#### R2024a: 无需总线对象或额外模块即可指定元素

当子系统或模型具有输出总线元素端口时，您无需指定 `Simulink.Bus` 对象或添加 Out Bus Element 模块来：

- 向输出端口添加元素。
- 指定输出端口处元素的属性。

要向端口添加元素，请选择您希望包含新元素的元素。然后，点击 Add element 并选择以下选项之一：

- **Add element with block** — 向端口添加一个元素，并添加一个表示该元素的 Out Bus Element 模块。
- **Add element without block** — 向端口添加一个元素，而不添加表示该元素的 Out Bus Element 模块。

要编程方式向输出总线添加元素而不向框图添加模块，请使用 `Simulink.Bus.addElementToPort` 函数。

#### R2024a: 将模块拖到新位置时选择新选项

当您按住 **Ctrl** 并将 Out Bus Element 模块拖到新位置时，您会收到更清晰的选项：

- **New Port** — 创建一个端口。
- **New Element** — 当拖动的模块表示端口的一个元素而不是整个端口时，向该端口添加一个元素。

在以前的版本中，您会收到两个选项：

- **Create New Port** — 创建一个端口。
- **Use Existing Port** — 当拖动的模块表示端口的一个元素而不是整个端口时，向该端口添加一个元素。否则，创建一个端口。

#### R2024a: 添加或复制模块会创建端口

这些操作现在一致地创建端口：

- 双击画布。然后，开始输入 `Out Bus Element`，并从菜单中选择该模块。
- 复制并粘贴一个 Out Bus Element 模块。

在以前的版本中，这些操作会创建端口或向端口添加元素。

#### R2023a: 指定端口输出的名称

对于模型顶层的 Out Bus Element 模块，请使用 **Output name** 模块参数来指定出现在父子系统或模型中的顶层总线、信号或消息的名称。

#### R2023a: Property Inspector 支持 Out Bus Element 模块

Property Inspector 支持 In Bus Element 和 Out Bus Element 模块。

#### R2023a: 诊断消息链接到相关 Out Bus Element 模块

In Bus Element 和 Out Bus Element 模块的警告和错误消息现在会链接到框图中的对应模块，帮助您快速找到警告或错误的来源。在以前的版本中，警告和错误消息引用隐藏模块，并且不提供链接。

## Libraries

Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Ports & Subsystems HDL Coder / Sinks

## Description

The Out Bus Element block provides a bus, signal, or message as the
output of an external port.

To group multiple buses, signals, or messages into an output bus, use multiple Out
Bus Element blocks that correspond with the same port. The Out Bus
Element blocks combine the functionality of a Bus Creator block and
an Outport block. All Out Bus Element blocks that correspond
with the same port share a dialog box.

For interfaces that include buses composed of many bus elements, Out Bus
Element blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Allow you to more easily make incremental changes to the interface.
- Allow access to a bus element closer to the point of usage, avoiding the use of a
  Bus Creator and From block configuration.

To convert an interface to use Out Bus Element blocks, see Simplify Subsystem and Model Interfaces with Bus Element Ports.

The Out Bus Element block does not support mixing message and signal
elements as inputs.

When you save output data to the workspace or a file, bus data defined by groups of
root-level Out Bus Element blocks are logged along with root-level
Outport block data.

## Ports

### Input

### **Port\_1** — Full or partial output for external port scalar | vector | matrix | array | bus

Connect a bus, signal, or message to pass to the corresponding external output
port of the parent subsystem or model.

When multiple Out Bus Element blocks are associated with the same
external port, the input to this block is an element of the bus at the output port.
The second text field in the block label specifies the element name.

When one Out Bus Element block is associated with the external
port, the input to this block is passed directly to the output port or nested in a bus
at the output port. To pass the input of the block to the output port without nesting
it in a bus, delete the text from the second text field in the block label.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit the element associated with an
Out Bus Element
block, in the Simulink® Editor, edit the block label.

To edit port, signal, and execution attributes, use the Property
Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of output port `OutBus` (default) | port name

Specify a port name that is not already in use by another block or
port within the system. The name appears on the parent
Subsystem or Model block.

To change the port name from the Simulink Editor, edit the first text field of the block
label.

Default Out Bus Element block with OutBus highlighted in block label

Multiple blocks can provide output for the same port as long as each
block provides output for a unique element of the port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `"OutBus"` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

### **Element** — Optional bus element specification `signal1` (default) | element path

To create a bus at the output port, specify an element in the second
text field of the block label.

Default Out Bus Element block with signal1 highlighted in block label

How you specify the element depends on where the element is in the bus
hierarchy.

- For an element at the top level of the output bus, specify the
  element name, for example, `constant`.
- For an element in a nested bus, specify the name of the nested
  bus, intermediary nested buses, and the leaf signal separated by
  dots, for example, `sinusoidal.sine`. This
  element path does not include the top-level bus.

Each output element must be unique and must not overlap with other
elements of the port. For example, for a nested bus, use one Out
Bus Element block that corresponds with the nested bus or
multiple Out Bus Element blocks that correspond with the
nested bus elements.

To output a signal, message, or bus without creating a bus, delete the
text from the second text field of the block label.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `"signal1"` (default) | element path in quotes |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Element="constant")`

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Element="sinusoidal.sine")`

### Port Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

*Before R2025a: To specify attributes, such as output name,
pause on the name of the top-level bus, signal, or message. Then, click Specify attributes. Alternatively, when available, click an
attribute summary.*

For information about the port name, see **Port
name**.

### **Port number** — Position of port on parent block `1` (default) | real integer

Specify the order in which the port that corresponds to the block appears on the parent
Subsystem or Model block.

- If you add a block that creates another port, the port number is the next available
  number.
- Deleting all blocks associated with a port deletes the port. Other ports are
  renumbered so that they are sequential and do not skip any numbers.
- Specifying a port number that exceeds the number of ports creates a port for that
  number and for any skipped sequential numbers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `"1"` (default) | real integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **Output name** — Name of output bus, signal, or message in parent subsystem or model no default

*Since R2023a*

Specify the name of the output bus, signal, or message in the parent
subsystem or model. The name appears as a label on the line.

To display propagated labels for individual lines or all lines in a
model, see Display Propagated Signal Labels.

#### Dependencies

- To enable this parameter:

  - The block must be at the top level of a
    model.
  - The element must be the top-level bus, signal,
    or message.
- When you set **Data type** to a
  `Simulink.Bus` object, the software sets
  this parameter to `""`
  (empty).

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutputName` |
| **Values:** | `""` (default) | output name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/OutBus",OutputName="model-output")`

### **Initial output** — Initial output for parent conditionally executed subsystem `[]` (default) | scalar | structure

*Since R2024b*

For conditionally executed subsystems, specify the block output before
the subsystem executes and while the subsystem is disabled. To inherit
the initial output value from the input signal, apply both of these
default settings:

- Set **Initial output** to
  `[]`.
- Set **Output when
  disabled** to
  `held`.

The software attempts to inherit the output value from the input
signal. If the input signal is not a valid source for the initial output
value, the initial output value `[]` is treated as
`double(0)`. For more information, see Conditional Subsystem Initial Output Values.

For information about specifying an initial condition structure, see
Specify Initial Conditions for Bus Elements.

#### Tips

If the conditional subsystem is driving a Merge
block, you do not need to specify an initial condition for the
Out Bus Element block. For more information, see
Underspecified initialization detection.

#### Dependencies

To enable this parameter:

- The block must be at the top level of a conditionally
  executed subsystem or model.
- The element must be the top-level bus, signal, or
  message.

#### Limitations

- This block does not support an initial output of
  `inf` or
  `NaN`.
- When the input is a virtual bus, an **Initial
  output** value of `[]` is
  treated as `double(0)`.
- When the input contains a nonvirtual bus,
  **Initial output** does not support
  nonzero scalar values.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InitialOutput` |
| **Values:** | `'[]'` (default) | scalar in quotes | structure in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mdl/condss/Output",InitialOutput="3")`

### **Output when disabled** — Output when parent conditionally executed subsystem is disabled `held` (default) | `reset`

*Since R2024b*

Specify what happens to the block output when the parent conditionally
executed subsystem is disabled.

- `held` — The output is held when the
  subsystem is disabled.
- `reset` — The output is reset to the
  value given by **Initial output** when the
  subsystem is disabled.

#### Tips

- If the output of the parent subsystem connects to a Merge block,
  do not set this parameter to
  `reset`.
- For an Out Bus Element block in a
  function-call subsystem, this parameter is meaningful only
  if the Function-Call Subsystem block connects
  to a state in a Stateflow® chart. For more information, see Bind a Function-Call Subsystem to a State (Stateflow).

#### Dependencies

To enable this parameter:

- The block must be at the top level of a conditional
  subsystem with valid enabling and disabling semantics.
  For example, an Out Bus Element block in
  an enabled subsystem supports this parameter, but an
  Out Bus Element block in a triggered
  subsystem does not support this parameter.
- The element must be the top-level bus, signal, or
  message.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputWhenDisabled` |
| **Values:** | `"held"` (default) | `"reset"` |

**Example:** `set_param("mdl/condss/Output",InitialOutput="3",OutputWhenDisabled="reset")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify attributes, a parenthetical appears next to the name of the corresponding
bus, signal, or message. To display the specified attributes in full, click the attribute
summary.

Pointer paused on attribute summary next to bus name

*Before R2025a: To specify attributes, such as data type, pause on the
name of a bus, signal, or message. Then, click Specify attributes. Alternatively, when available, click an attribute
summary.*

### **Data type** — Data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

The data type of a bus, signal, or message can be inherited, specified directly, or
expressed as a data type object such as a `Simulink.NumericType` object.

You can specify any of these options:

- Inherited data type
- Built-in Simulink data type — For example, specify `single` or
  `uint8`. See Data Types Supported by Simulink.
- Fixed-point data type — Use the `fixdt` function. For example, specify
  `fixdt(1,16,0)`.
- Enumerated data type — Use the name of the type preceded by
  `Enum:`. For example, specify `Enum:
  myEnumType`.
- Bus data type — Use the name of the `Simulink.Bus` object preceded by `Bus:`. For example,
  specify `Bus: myBusObject`.
- Value type — Use the name of the `Simulink.ValueType` object preceded by `ValueType:`. For
  example, specify `ValueType: windVelocity`.
- Custom data type — Use a MATLAB expression that specifies the type. For example, you can
  specify a `Simulink.NumericType` object
  whose `DataTypeMode` property is set to a value other
  than `"Fixed-point: unspecified scaling"`.

When you specify a `Simulink.ValueType`
object as the data type, some parameters of the element are ignored. For example, the
**Min**, **Max**, and **Unit** parameters
are ignored. The software uses the corresponding properties of the
`Simulink.ValueType` object. For example, suppose you set
**Unit** to `ft/s` for an element. When the **Data
type** of the element specifies a `ValueType` object that has
`m/s` as its unit, the element uses `m/s` instead of
`ft/s`.

When you specify a `Simulink.Bus` object
as the data type, some parameters of the element are reset to their default values. For
example, the **Min**, **Max**, and **Unit**
parameters are reset. The software uses the corresponding properties of the
`Simulink.BusElement` objects in the `Simulink.Bus` object
instead.

#### Tips

- When you specify a bus using a `Simulink.Bus` object or a
  `Simulink.ValueType` object with a
  `Simulink.Bus` object data type, the Property Inspector
  and block dialog box display the elements defined by the corresponding
  `Simulink.BusElement` objects.
- To create a `Simulink.Bus` object using the Type
  Editor, click Open Type Editor.

#### Dependencies

To specify a `Simulink.Bus` object as the data type of a bus at a bus
element port, an
Out Bus Element
block must represent the bus or an element of the bus.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16)"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"string"` | `"Enum: <class name>"` | `"Bus: <object name>"` | `"ValueType: <object name>"` | data type expression in quotes |

**Example:** `set_param("mymodel/myBus.signal1",OutDataTypeStr="int32")`

### **Data mode** — Data mode of output element `inherit` (default) | `signal` | `message`

Specify the data mode of the output element.

- `inherit` — Output element inherits its data
  mode.
- `signal`  — Output element must be a signal or a bus
  that contains signals.
- `message` — Output element must be a message or a bus
  that contains messages.

#### Dependencies

To enable this parameter, the block must be at the top level of a model.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `DataMode` |
| **Values:** | `"inherit"` (default) | `"signal"` | `"message"` |

**Example:** `set_param("mymodel/OutBus",DataMode="signal")`

### **Bus virtuality** — Virtual or nonvirtual bus `inherit` (default) | `virtual` | `nonvirtual`

Specify whether to inherit the bus virtuality or define the bus as virtual or nonvirtual.
For more information, see Composite Interface Guidelines.

This parameter determines whether the blocks inherit or define the bus virtuality. If the
blocks define the bus virtuality and the virtuality of the input bus does not match, compiling
the model produces an error.

#### Dependencies

To enable this parameter, **Data type** must resolve to a
`Simulink.Bus` object. For example, set **Data type** to
a `Simulink.Bus` object or a `Simulink.ValueType` object that
specifies a `Simulink.Bus` object as its data type.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `BusVirtuality` |
| **Values:** | `"inherit"` (default) | `"virtual"` | `"nonvirtual"` |

**Example:** `set_param("mymodel/myBus.nestedBus",BusVirtuality="nonvirtual")`

### **Dimensions** — Signal dimensions `-1` (default) | integer | `1`-by-`2` vector of integers

Specify the dimensions of a signal.

- `-1` — The signal can have any dimensions.
- `N` — The signal must be a vector of size
  `N`.
- `[R C]` — The signal must be a matrix having `R`
  rows and `C` columns.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `1`. The software uses the
  dimensions specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the dimensions specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `PortDimensions` |
| **Values:** | `"-1"` (default) | integer in quotes | `1`-by-`2` vector of integers in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",PortDimensions="[1
3]")`

### **Dimensions mode** — Option to allow only variable-size or fixed-size signals `Inherit` (default) | `Fixed` | `Variable`

Specify the type of signals allowed.

- `Inherit` — Allow variable-size and fixed-size
  signals.
- `Variable` — Allow only variable-size signals.
- `Fixed` — Allow only fixed-size signals. Do not allow
  variable-size signals.

When the signal is variable-sized, the **Dimensions** parameter specifies
the maximum dimensions of the signal.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `Inherit`. The
  software uses the dimensions modes specified by the `Simulink.BusElement`
  objects in the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the dimensions mode specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `VarSizeSig` |
| **Values:** | `"Inherit"` (default) | `"No"` | `"Yes"` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",VarSizeSig="No")`

### **Unit** — Physical unit `inherit` (default) | unit supported by Simulink software

Specify the physical unit of the signal. For a list of supported units, in the MATLAB Command Window, enter `showunitslist`.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `inherit`. The
  software uses the units specified by the `Simulink.BusElement` objects in
  the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the unit specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `Unit` |
| **Values:** | `"inherit"` (default) | unit supported by Simulink software in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",Unit="m/s")`

### **Complexity** — Numeric type `auto` (default) | `real` | `complex`

Specify the numeric type of the signal. To choose the numeric type of the signal, select
`auto`. Otherwise, choose a real or complex signal type.

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `auto`. The
  software uses the complexity specified by the `Simulink.BusElement`
  objects in the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the complexity specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `SignalType` |
| **Values:** | `"auto"` (default) | `"real"` | `"complex"` |

**Example:** `set_param("mymodel/myBus.signal1",SignalType="real")`

### **Minimum** — Minimum value `[]` (default) | scalar

Lower value of the range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes such as SIL or
  external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `[]`. The software uses the
  minimum values specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the minimum value specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `"[]"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMin="0")`

### **Maximum** — Maximum value `[]` (default) | scalar

Upper value of the range that the software checks.

This number must be a finite real double scalar value.

The software uses this value to perform:

- Simulation range checking. For more information, see Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes such as SIL or
  external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Dependencies

- When **Data type** specifies a `Simulink.Bus`
  object, the software sets this parameter to `[]`. The software uses the
  maximum values specified by the `Simulink.BusElement` objects in the
  `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the maximum value specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `"[]"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMax="2")`

### **Description** — Description of bus, signal, or message no default

Use the description to document information about the bus, signal, or message, such as
where it is used. This information does not affect processing.

#### Dependencies

- When **Data type** specifies a
  `Simulink.Bus` object, the software sets this parameter
  to `""` (empty). The software uses the description
  specified by the `Simulink.Bus` object.
- When **Data type** specifies a
  `Simulink.ValueType` object, the software ignores the value of this
  parameter. The software uses the description specified by the
  `Simulink.ValueType` object instead.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `Description` |
| **Values:** | `""` (default) | description in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",Description="This signal is
used by...")`

### Execution Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify attributes, a parenthetical appears next to the name of the corresponding
bus, signal, or message. To display the specified attributes, click
Specify execution attributes.

Pointer paused on Specify execution attributes button next to bus name

*Before R2025a: To specify execution attributes, pause on the name
of a bus, signal, or message. Then, click Specify execution attributes.*

### **Sample time** — Sample time `-1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of
sample time, such as continuous (`0`) or inherited
(`-1`). For more options, see Types of Sample Time.

By default, the signal inherits its sample time.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",SampleTime="0.01")`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used to simplify subsystem bus interfaces when you use the block
in subsystems that generate HDL code, but it is not included in the hardware
implementation.

To learn more about using buses for HDL code generation, see Buses (HDL Coder) and Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder).

This block supports code generation for `Simulink.ValueType` object. For
more information about value types, see Specify Common Set of Signal Properties as Value Type.

**Data Type Support**

This block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2017a**

### R2025a: Specify port, signal, and execution attributes more easily

You can now specify port, signal, and execution attributes more easily.

- To toggle the display of port, signal, and execution attributes, click Show attributes or Hide attributes. Port, signal, and execution attributes
  now appear on tabs. The Show attributes or Hide attributes button replaces the buttons that appear
  when you pause on a bus, signal, or message name in a previous
  release.
- When you specify execution attributes, a parenthetical now appears next to
  the name of the corresponding bus, signal, or message. To display the
  specified attributes, click Specify execution attributes.
- To edit the port name, double-click the name of the top-level bus, signal,
  or message. Alternatively, on the **Port** tab, specify
  **Port name**.
- To change block colors, click Set color of blocks associated with selected elements and select a standard color or specify a
  custom color.
- To create a `Simulink.Bus` object using the Type
  Editor, on the **Signal** tab, click Open Type Editor.
- **Dims mode** is now named **Dimensions
  mode**.

### R2024b: Specify initial conditions

In conditionally executed subsystems and models, Out Bus Element
blocks now support initial conditions on the top-level element. For nonbus signals,
set **Initial output** to a value with the same dimensions and
complexity as the signal. For buses, set **Initial output** to a
MATLAB structure with fields that have the same names and hierarchy as the
elements of the bus. To specify what happens to the block output when the subsystem
is disabled, use the **Output when disabled** block
parameter.

### R2024a: Specify elements without bus objects or additional blocks

When a subsystem or model has an output bus element port, you do not need to
specify a `Simulink.Bus` object or add Out Bus Element
blocks to:

- Add elements to the output port.
- Specify attributes of the elements at the output port.

To add an element to the port, select the element that you want to contain the new
element. Then, click Add element and select one of these options:

- **Add element with block** — Add an element to the
  port and an Out Bus Element block that represents the
  element.
- **Add element without block** — Add an element to
  the port without adding an Out Bus Element block that
  represents the element.

To programmatically add elements to the output bus without adding blocks to the
block diagram, use the `Simulink.Bus.addElementToPort` function.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag an Out Bus Element
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — When the dragged block represents
  an element of the port and not the full port, add an element to the
  port.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — When the dragged block
  represents an element of the port and not the full port, add an element
  to the port. Otherwise, create a port.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Out Bus
  Element`, and select the block from the menu.
- Copy and paste an Out Bus Element block.

In previous releases, these actions create a port or add an element to a
port.

### R2023a: Specify name of port output

For an Out Bus Element block at the top level of a model, use the
**Output
name** block parameter to specify the name of the top-level bus,
signal, or message that appears in a parent subsystem or model.

### R2023a: Property Inspector supports Out Bus Element blocks

The Property
Inspector supports In Bus Element and Out Bus
Element blocks.

### R2023a: Diagnostic messages link to related Out Bus Element blocks

Warning and error messages for In Bus Element and Out Bus
Element blocks now link to the corresponding block in the block diagram,
helping you quickly find the source of the warning or error. In previous releases,
warning and error messages refer to a hidden block and do not provide a link.
