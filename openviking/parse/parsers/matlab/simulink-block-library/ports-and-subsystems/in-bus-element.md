---
type: simulink-block
title: 'In Bus Element'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'inbuselement'
---

# In Bus Element

Select input from external port

## 中文

从外部端口选择输入

### 库

Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Ports & Subsystems HDL Coder / Sources

### 描述

In Bus Element 模块从接收总线、信号或消息的外部端口选择输入。

当端口接收总线时，In Bus Element 模块结合了 Inport 模块和 Bus Selector 模块的功能。要从总线中选择多个元素，请使用多个 In Bus Element 模块。所有与同一端口对应的 In Bus Element 模块共享一个对话框。

对于包含由许多总线元素组成的总线的接口，In Bus Element 模块可以：

- 减少框图中信号线的复杂度和杂乱。
- 使您更容易对接口进行增量更改。
- 允许在使用点附近访问总线元素，避免使用 Bus Selector 和 Goto 模块配置。

要将接口转换为使用 In Bus Element 模块，请参阅 Simplify Subsystem and Model Interfaces with Bus Element Ports。

In Bus Element 模块不支持将消息元素和信号元素混合作为输出。

### 端口

#### 输出

#### **Port\_1** — 从外部端口选择的输入 scalar | vector | matrix | array | bus

从父子系统或模型的对应外部输入端口选择总线、信号或消息。

虽然可以选择总线元素，但不能选择总线数组的元素。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** Yes

### 参数

要编辑与 In Bus Element 模块关联的元素，请在 Simulink® Editor 中编辑模块标签。

要编辑端口、信号、执行和消息属性，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

#### 模块标签

#### **Port name** — 输入端口名称 `InBus` (default) | port name

指定一个尚未被系统中另一个模块或端口使用的端口名称。该名称显示在父 Subsystem 或 Model 模块上。

要从 Simulink Editor 更改端口名称，请编辑模块标签的第一个文本字段。

默认 In Bus Element 模块，其中 InBus 在模块标签中高亮显示

多个模块可以访问同一个端口。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `"InBus"` (default) | port name in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

#### **Element** — 可选总线元素规范 `signal1` (default) | element path

当端口从父系统接收总线时，可选地指定要从总线中选择的元素。

要指定模块选择的元素，请在 Simulink Editor 中编辑模块标签的第二个文本字段。

In Bus Element 模块，其中 signal1 在模块标签中高亮显示

如何指定元素取决于该元素在总线层次结构中的位置。

- 对于输入总线顶层的元素，指定元素名称，例如 `constant`。
- 对于嵌套总线中的元素，指定嵌套总线名称、中间嵌套总线以及叶信号名称，以点分隔，例如 `sinusoidal.sine`。此元素路径不包括顶层总线。

多个模块可以访问同一个元素。

要选择顶层信号、消息或总线，请删除模块标签第二个文本字段中的文本。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `"signal1"` (default) | element path in quotes |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="constant")`

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="sinusoidal.sine")`

#### Port 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

有关端口名称的信息，请参阅 **Port name**。

#### **Port number** — 端口在父模块上的位置 `1` (default) | real integer

指定与该模块对应的端口在父 Subsystem 或 Model 模块上出现的顺序。

- 如果添加创建一个新端口的模块，则端口编号为下一个可用编号。
- 删除与某端口关联的所有模块会删除该端口。其他端口会重新编号，使其连续且不跳过任何编号。
- 指定超过端口数的端口编号会为该编号以及任何跳过的连续编号创建端口。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `"1"` (default) | real integer in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

#### Signal 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

指定属性后，相应总线、信号或消息名称旁边会出现括号内容。要完整显示指定的属性，请点击属性摘要。

指针停留在总线名称旁边的属性摘要上

*在 R2025a 之前：要指定属性（例如数据类型），请将指针停在总线、信号或消息的名称上。然后点击 Specify attributes。或者，在可用时点击属性摘要。*

#### **Data type** — 数据类型 `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

总线、信号或消息的数据类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType` 对象。

可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Data Types Supported by Simulink。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称，并在前面加上 `Enum:`。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用 `Simulink.Bus` 对象的名称，并在前面加上 `Bus:`。例如，指定 `Bus: myBusObject`。
- 值类型 — 使用 `Simulink.ValueType` 对象的名称，并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB 表达式。例如，可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `"Fixed-point: unspecified scaling"` 以外的值。

当指定 `Simulink.ValueType` 对象作为数据类型时，元素的某些参数会被忽略。例如，**Min**、**Max** 和 **Unit** 参数会被忽略。软件使用 `Simulink.ValueType` 对象的对应属性。例如，假设为某元素将 **Unit** 设置为 `ft/s`。当该元素的 **Data type** 指定一个以 `m/s` 作为其单位的 `ValueType` 对象时，该元素使用 `m/s` 而不是 `ft/s`。

当指定 `Simulink.Bus` 对象作为数据类型时，元素的某些参数会重置为其默认值。例如，**Min**、**Max** 和 **Unit** 参数会重置。软件改为使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。

#### 提示

- 当使用 `Simulink.Bus` 对象或具有 `Simulink.Bus` 对象数据类型的 `Simulink.ValueType` 对象指定总线时，Property Inspector 和模块对话框会显示相应 `Simulink.BusElement` 对象定义的元素。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请点击 Open Type Editor。

#### 依赖关系

要将 `Simulink.Bus` 对象指定为总线元素端口处总线的数据类型，In Bus Element 模块必须表示该总线或该总线的一个元素。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"` (default) | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16)"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"string"` | `"Enum: <class name>"` | `"Bus: <object name>"` | `"ValueType: <object name>"` | data type expression in quotes |

**示例：** `set_param("mymodel/myBus.signal1",OutDataTypeStr="int32")`

#### **Bus virtuality** — 虚拟或非虚拟总线 `inherit` (default) | `virtual` | `nonvirtual`

指定是继承总线虚拟性，还是将总线定义为虚拟或非虚拟。有关详细信息，请参阅 Composite Interface Guidelines。

此参数确定模块是继承还是定义总线虚拟性。如果模块定义总线虚拟性，并且输入总线的虚拟性不匹配，则编译模型会产生错误。

#### 依赖关系

要启用此参数，**Data type** 必须解析为 `Simulink.Bus` 对象。例如，将 **Data type** 设置为 `Simulink.Bus` 对象或将其数据类型指定为 `Simulink.Bus` 对象的 `Simulink.ValueType` 对象。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `BusVirtuality` |
| **值：** | `"inherit"` (default) | `"virtual"` | `"nonvirtual"` |

**示例：** `set_param("mymodel/myBus.nestedBus",BusVirtuality="nonvirtual")`

#### **Data mode** — 输入元素的数据模式 `inherit` (default) | `signal` | `message`

指定输入元素的数据模式。

- `inherit` — 输入元素继承其数据模式。
- `signal` — 输入元素必须是信号或包含信号的总线。
- `message` — 输入元素必须是消息或包含消息的总线。

当选择 `message` 作为消息或总线的数据模式时，消息或总线旁边会出现信封按钮。使用该信封按钮指定自定义队列属性。

#### 提示

要为总线中的每条消息指定不同的自定义队列属性，请为每条消息而不是总线设置 **Data mode** 参数。

#### 依赖关系

要启用此参数，模块必须位于模型的顶层。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `DataMode` |
| **值：** | `"inherit"` (default) | `"signal"` | `"message"` |

**示例：** `set_param("mymodel/InBus",DataMode="signal")`

#### **Dimensions** — 信号维度 `-1` (default) | integer | `1`-by-`2` vector of integers

指定信号的维度。

- `-1` — 信号可以具有任意维度。
- `N` — 信号必须是大小为 `N` 的向量。
- `[R C]` — 信号必须是具有 `R` 行和 `C` 列的矩阵。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `1`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的维度。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `PortDimensions` |
| **值：** | `"-1"` (default) | integer in quotes | `1`-by-`2` vector of integers in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/myBus.signal1",PortDimensions="[1 3]")`

#### **Dimensions mode** — 用于仅允许可变大小或固定大小信号的选项 `Inherit` (default) | `Fixed` | `Variable`

指定允许的信号类型。

- `Inherit` — 允许可变大小和固定大小信号。
- `Variable` — 仅允许可变大小信号。
- `Fixed` — 仅允许固定大小信号。不允许可变大小信号。

当信号为可变大小时，**Dimensions** 参数指定信号的最大维度。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `Inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度模式。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的维度模式。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `VarSizeSig` |
| **值：** | `"Inherit"` (default) | `"No"` | `"Yes"` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",VarSizeSig="No")`

#### **Unit** — 物理单位 `inherit` (default) | unit supported by Simulink software

指定信号的物理单位。有关支持的单位列表，请在 MATLAB Command Window 中输入 `showunitslist`。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的单位。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的单位。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `Unit` |
| **值：** | `"inherit"` (default) | unit supported by Simulink software in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/myBus.signal1",Unit="m/s")`

#### **Complexity** — 数值类型 `auto` (default) | `real` | `complex`

指定信号的数值类型。要选择信号的数值类型，请选择 `auto`。否则，选择实数或复数信号类型。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `auto`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的复数性。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的复数性。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `SignalType` |
| **值：** | `"auto"` (default) | `"real"` | `"complex"` |

**示例：** `set_param("mymodel/myBus.signal1",SignalType="real")`

#### **Minimum** — 最小值 `[]` (default) | scalar

软件检查范围的下限值。

此数字必须是有限实数 double 标量值。

软件使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最小值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的最小值。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `"[]"` (default) | scalar in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",OutMin="0")`

#### **Maximum** — 最大值 `[]` (default) | scalar

软件检查范围的上限值。

此数字必须是有限实数 double 标量值。

软件使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或 external mode）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最大值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的最大值。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `"[]"` (default) | scalar in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",OutMax="2")`

#### **Description** — 总线、信号或消息的描述 无默认值

使用描述记录有关总线、信号或消息的信息，例如其使用位置。此信息不影响处理。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `""`（空）。软件使用 `Simulink.Bus` 对象指定的描述。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改为使用 `Simulink.ValueType` 对象指定的描述。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `Description` |
| **值：** | `""` (default) | description in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",Description="This signal is used by...")`

#### Execution 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

指定属性后，相应总线、信号或消息名称旁边会出现括号内容。要显示指定的属性，请点击 Specify execution attributes。

指针停留在总线名称旁边的 Specify execution attributes 按钮上

*在 R2025a 之前：要指定执行属性，请将指针停在总线、信号或消息的名称上。然后点击 Specify execution attributes。*

#### **Sample time** — 采样时间 `-1` (default) | scalar

指定采样时间命中之间的离散间隔，或指定另一种类型的采样时间，例如 continuous (`0`) 或 inherited (`-1`)。有关更多选项，请参阅 Types of Sample Time。

默认情况下，信号继承其采样时间。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"` (default) | scalar in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",SampleTime="0.01")`

#### **Events** — 用于基于流入端口的数据流触发模型分区的选项 event trigger objects 的 cell 数组

*自 R2022b 起*

**Events** 参数存储与端口关联的事件触发器。*事件触发器*基于模型中特定位置处的运行时活动创建调度事件。模型的调度指定响应调度事件而执行的分区，以及执行优先级。要配置模型的调度，请使用 Schedule Editor。

下表总结了可在根级输入端口上配置的事件触发器。每个事件触发器将与该端口的数据流相关的 *input event* 映射到要触发的调度事件名称。可以为每个 input event 配置一个事件触发器。

| Input Event | Input Event Description | Event Trigger Object |
| --- | --- | --- |
| Input write | 每次输入端口值更新时发生 *input write* 事件。 | `simulink.event.InputWrite` |
| Input write timeout | 当输入端口值在指定时间内未更新时发生 *input write timeout* 事件。 | `simulink.event.InputWriteTimeout` |
| Input write lost | 当新的输入端口值覆盖未处理的数据时发生 *input write lost* 事件。 | `simulink.event.InputWriteLost` |

#### 总线端口上的事件触发器

在总线端口上配置事件触发器时，根据总线的虚拟性确定在何处指定事件触发器。

- 虚拟总线 — 在总线的叶元素上指定事件触发器。虚拟总线本身不支持事件触发器。
- 非虚拟总线 — 在总线上指定事件触发器。非虚拟总线的元素不支持事件触发器。

In Bus Element 模块必须选择具有一个或多个事件触发器的每个元素。

#### 依赖关系

要启用此参数：

- 端口必须是基于速率的模型中的根级输入端口。
- 如果端口加载非虚拟总线，请在层次树中选择该总线。非虚拟总线的元素不支持事件触发器。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `EventTriggers` |
| **值：** | `[]` (default) | `1`-by-`1` cell array | `2`-by-`1` cell array | `3`-by-`1` cell array |

**示例：** `set_param("mymodel/InBusNonvirtual",EventTriggers={inputWrite,writeTimeout,writeLost})` 为名为 `InBusNonvirtual` 的非虚拟总线指定事件触发器。

**示例：** `set_param("mymodel/InBus.signal1",EventTriggers={inputWrite,writeTimeout,writeLost})` 为名为 `InBus` 的虚拟总线的名为 `signal1` 的叶元素指定事件触发器。

#### 队列属性

仅当模块位于模型顶层且将 **Data mode** 参数设置为 `message` 时，队列属性才可见。

要指定队列属性，请在总线或消息名称旁边点击 Use default queue attributes。

指针停留在总线名称旁边的 Use default queue attributes 按钮上

#### **Use default queue attributes** — 默认或自定义队列规范 on (default) | off

使用此参数在默认或自定义队列规范之间进行选择。

要使用默认队列属性，请保持此参数处于选中状态。在这种情况下，对于每个消息总线元素，会自动插入容量为 1 的 LIFO 覆盖队列。

要使用自定义规范，请清除此参数并配置队列属性。如果组件外部未放置 storage block，则队列属性适用。

有关详细信息，请参阅 Specify Queue Properties for Message Interface。

#### 依赖关系

要为元素启用此参数，请将该元素的 **Data mode** 设置为 `message`。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `MessageQueueUseDefaultAttributes` |
| **值：** | `"on"` (default) | `"off"` |

**示例：** `set_param("mymodel/InBus.message1",MessageQueueUseDefaultAttributes="off")`

#### **Queue capacity** — 消息存储容量 1 (default) | scalar

指定队列可以存储的消息元素数量。

#### 依赖关系

要为元素启用此参数，请将该元素的 **Data mode** 设置为 `message`。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `MessageQueueCapacity` |
| **值：** | `"1"` (default) | scalar in quotes |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/InBus.message1",MessageQueueCapacity="10")`

#### **Queue type** — 选择 FIFO 或 LIFO 队列 `LIFO` (default) | `FIFO`

选择以下队列类型之一：

- `FIFO` — 先进先出
- `LIFO` — 后进先出

#### 依赖关系

要为元素启用此参数，请将该元素的 **Data mode** 设置为 `message`。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `MessageQueueType` |
| **值：** | `"LIFO"` (default) | `"FIFO"` |

**示例：** `set_param("mymodel/InBus.message1",MessageQueueType="FIFO")`

#### **Queue overwriting** — 队列消息覆盖策略 on (default) | off

选择此参数以在两种队列覆盖策略之间进行选择。

- 如果选中此参数，则当队列已满时，传入的消息元素会覆盖最早的消息。
- 如果清除此参数，则当队列已满时，模块不接受新消息。

#### 依赖关系

要为元素启用此参数，请将该元素的 **Data mode** 设置为 `message`。

#### 以编程方式使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠，以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，并用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `MessageQueueOverwriting` |
| **值：** | `"on"` (default) | `"off"` |

**示例：** `set_param("mymodel/InBus.message1",MessageQueueOverwriting="off")`

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

当在生成 HDL 代码的子系统中使用此模块时，可使用此模块简化子系统总线接口，但它不包含在硬件实现中。

要详细了解如何使用总线进行 HDL 代码生成，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

此模块支持为 `Simulink.ValueType` 对象生成代码。有关值类型的详细信息，请参阅 Specify Common Set of Signal Properties as Value Type。

**数据类型支持**

此模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2017a 中引入**

#### R2025a：更轻松地指定端口、信号和执行属性

现在可以更轻松地指定端口、信号和执行属性。

- 要切换端口、信号和执行属性的显示，请点击 Show attributes 或 Hide attributes。端口、信号和执行属性现在显示在选项卡上。Show attributes 或 Hide attributes 按钮取代了以前版本中将指针停在总线、信号或消息名称上时出现的按钮。
- 指定执行属性后，相应总线、信号或消息名称旁边现在会出现括号内容。要显示指定的属性，请点击 Specify execution attributes。
- 要编辑端口名称，请双击顶层总线、信号或消息的名称。或者，在 **Port** 选项卡上指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements，然后选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上点击 Open Type Editor。
- **Dims mode** 现在命名为 **Dimensions mode**。

#### R2024b：将元素名称传播为信号标签

现在可以从 In Bus Element 模块传播元素名称。例如，对于标签为 `InBus.nonconstant.chirp` 的 In Bus Element 模块，传播后的名称为 `chirp`。

有关详细信息，请参阅 Signal Label Propagation。

#### R2024a：将模块拖动到新位置时选择新选项

按住 **Ctrl** 并将 In Bus Element 模块拖动到新位置时，会看到更清晰的选项：

- **New Port** — 创建端口。
- **New Element** — 向端口添加元素。
- **Duplicate** — 创建 In Bus Element 模块的副本。

在以前的版本中，会看到两个选项：

- **Create New Port** — 创建端口。
- **Use Existing Port** — 创建 In Bus Element 模块的副本。

#### R2024a：添加或复制模块会创建端口

这些操作现在始终创建端口：

- 双击画布。然后开始键入 `In Bus Element`，并从菜单中选择该模块。
- 复制并粘贴 In Bus Element 模块。

在以前的版本中，这些操作会创建端口、向端口添加元素或复制模块。

#### R2023b：在子系统接口处无需总线对象或额外模块即可指定元素

在子系统接口和模型接口处，可以指定输入总线的元素，而无需使用 In Bus Element 模块来表示每个元素，也无需使用 `Simulink.Bus` 对象来定义总线层次结构。以前，只有模型接口处的 In Bus Element 模块支持此功能。

要添加元素，请点击 Add element 按钮箭头。然后选择 **Add element without block**。

#### R2023a：Property Inspector 支持 In Bus Element 模块

Property Inspector 支持 In Bus Element 和 Out Bus Element 模块。

#### R2023a：诊断消息链接到相关的 In Bus Element 模块

In Bus Element 和 Out Bus Element 模块的警告和错误消息现在链接到框图中的对应模块，帮助您快速找到警告或错误的来源。在以前的版本中，警告和错误消息引用隐藏模块，且不提供链接。

## Libraries

Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Ports & Subsystems HDL Coder / Sources

## Description

The In Bus Element block selects input from an external port that
receives a bus, signal, or message.

When the port receives a bus, the In Bus Element block combines the
functionality of an Inport block and a Bus Selector block. To
select multiple elements from the bus, use multiple In Bus Element blocks. All
In Bus Element blocks that correspond with the same port share a dialog
box.

For interfaces that include buses composed of many bus elements, In Bus
Element blocks:

- Reduce signal line complexity and clutter in a block diagram.
- Allow you to more easily make incremental changes to the interface.
- Allow access to a bus element closer to the point of usage, avoiding the use of a
  Bus Selector and Goto block configuration.

To convert an interface to use In Bus Element blocks, see Simplify Subsystem and Model Interfaces with Bus Element Ports.

The In Bus Element block does not support mixing message and signal
elements as outputs.

## Ports

### Output

### **Port\_1** — Selected input from external port scalar | vector | matrix | array | bus

Select a bus, signal, or message from the corresponding external input
port of the parent subsystem or model.

While you can select bus elements, you cannot select elements of
arrays of buses.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit the element associated with an
In Bus Element
block, in the Simulink® Editor, edit the block label.

To edit port, signal, execution, and message
attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of input port `InBus` (default) | port name

Specify a port name that is not already in use by another block or
port within the system. The name appears on the parent
Subsystem or Model block.

To change the port name from the Simulink Editor, edit the first text field of the block
label.

Default In Bus Element block with InBus highlighted in block label

Multiple blocks can access the same port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `"InBus"` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

### **Element** — Optional bus element specification `signal1` (default) | element path

When the port receives a bus from the parent system, optionally
specify an element to select from the bus.

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

In Bus Element block with signal1 highlighted in block label

How you specify the element depends on where the element is in the bus
hierarchy.

- For an element at the top level of the input bus, specify the
  element name, for example, `constant`.
- For an element in a nested bus, specify the name of the nested
  bus, intermediary nested buses, and the leaf signal separated by
  dots, for example, `sinusoidal.sine`. This
  element path does not include the top-level bus.

Multiple blocks can access the same element.

To select the top-level signal, message, or bus, delete the text from
the second text field of the block label.

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
In Bus Element
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

### **Data mode** — Data mode of input element `inherit` (default) | `signal` | `message`

Specify the data mode of the input element.

- `inherit` — Input element inherits its data
  mode.
- `signal`  — Input element must be a signal or a bus
  that contains signals.
- `message` — Input element must be a message or a bus
  that contains messages.

When you choose `message` as the data mode of a message
or bus, an envelope button appears next to the message or bus. Use the envelope button
to specify custom queue properties.

#### Tips

To specify different custom queue properties for each message in a bus, set the
**Data mode** parameter for each message instead of the
bus.

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

**Example:** `set_param("mymodel/InBus",DataMode="signal")`

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

### **Events** — Option to trigger model partition based on flow of data into port cell array of event trigger objects

*Since R2022b*

The **Events** parameter stores the event triggers
associated with the port. *Event triggers* create
schedule events based on the runtime activity at a particular location
in the model. The schedule for the model specifies the partitions that
execute in response to the schedule event, as well as the priority of
execution. To configure the schedule for your model, use the Schedule Editor.

The table summarizes the event triggers you can configure on
root-level input ports. Each event trigger maps an *input
event* related to the flow of data into the port to the
name of the schedule event to trigger. You can configure an input port
with one event trigger for each input event.

| Input Event | Input Event Description | Event Trigger Object |
| --- | --- | --- |
| Input write | An *input write* event occurs each time the input port value updates. | `simulink.event.InputWrite` |
| Input write timeout | An *input write timeout* event occurs each time the input port value does not update within a specified amount of time. | `simulink.event.InputWriteTimeout` |
| Input write lost | An *input write lost* event occurs each time a new input port value overwrites unprocessed data. | `simulink.event.InputWriteLost` |

#### Event Triggers on Bus Ports

When you configure event triggers on a bus port, determine where
to specify the event triggers based on the virtuality of the
bus.

- Virtual bus — Specify event triggers on leaf elements of
  the bus. Event triggers are not supported on the virtual bus
  itself.
- Nonvirtual bus — Specify event triggers on the bus. Event
  triggers are not supported on elements of nonvirtual
  buses.

In Bus Element blocks must select each element that
has one or more event triggers.

#### Dependencies

To enable this parameter:

- The port must be a root-level input port in a rate-based
  model.
- If the port loads a nonvirtual bus, in the hierarchical
  tree, select the bus. Event triggers are not supported on
  elements of a nonvirtual bus.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param`
function. Specify the element as the model
name,
a forward slash, and the port name or bus element path. For a bus
element port, the bus element path provides the hierarchy from the
top-level bus to the target element, separating each name in the
hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `EventTriggers` |
| **Values:** | `[]` (default) | `1`-by-`1` cell array | `2`-by-`1` cell array | `3`-by-`1` cell array |

**Example:** `set_param("mymodel/InBusNonvirtual",EventTriggers={inputWrite,writeTimeout,writeLost})`
specifies event triggers for the nonvirtual bus named
`InBusNonvirtual`.

**Example:** `set_param("mymodel/InBus.signal1",EventTriggers={inputWrite,writeTimeout,writeLost})`
specifies event triggers for a leaf element named
`signal1` of the virtual bus named
`InBus`.

### Queue Attributes

Queue attributes are visible only when the block is at the top level of a model and you
set the **Data
mode** parameter to `message`.

To specify queue attributes, next to the name of a bus or message, click Use default queue attributes.

Pointer paused on Use default queue attributes button next to bus name

### **Use default queue attributes** — Default or custom queue specifications on (default) | off

Use this parameter to select between default or custom queue
specifications.

To use the default queue properties, leave the parameter selected. In this case,
for each message bus element, a LIFO overwriting queue of capacity 1 is automatically
inserted.

To use custom specifications, clear the parameter and configure the queue
properties. Queue attributes are applicable if there is no storage block placed
outside a component.

For more information, see Specify Queue Properties for Message Interface.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueUseDefaultAttributes` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueUseDefaultAttributes="off")`

### **Queue capacity** — Message storage capacity 1 (default) | scalar

Specify the number of messages elements the queue can store.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueCapacity` |
| **Values:** | `"1"` (default) | scalar in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueCapacity="10")`

### **Queue type** — Choose FIFO or LIFO queue `LIFO` (default) | `FIFO`

Choose one of these queue types:

- `FIFO` — First-in-first-out
- `LIFO` — Last-in-first-out

#### Dependencies

To enable this parameter for an element, set the **Data mode** of
the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueType` |
| **Values:** | `"LIFO"` (default) | `"FIFO"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueType="FIFO")`

### **Queue overwriting** — Queue message overwriting policy on (default) | off

Select this parameter to choose between two queue overwriting policies.

- If you select the parameter, an incoming message element overwrites the oldest
  message if the queue is full.
- If you clear the parameter, the block does not accept new messages if the
  queue is full.

#### Dependencies

To enable this parameter for an element, set the **Data
mode** of the element to `message`.

#### Programmatic Use

To programmatically set the attribute value for an element, use the `set_param` function. Specify the element as the model name or subsystem block
path, a forward slash, and the port name or bus element path. For a bus element port, the
bus element path provides the hierarchy from the top-level bus to the target element,
separating each name in the hierarchy with a dot.

|  |  |
| --- | --- |
| **Parameter:** | `MessageQueueOverwriting` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param("mymodel/InBus.message1",MessageQueueOverwriting="off")`

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

This block can be used to simplify subsystem bus interfaces when you use the block in
subsystems that generate HDL code, but it is not included in the hardware
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

### R2024b: Propagate element names as signal labels

You can now propagate element names from In Bus Element blocks. For
example, for an In Bus Element block labeled
`InBus.nonconstant.chirp`, the propagated name is
`chirp`.

For more information, see Signal Label Propagation.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag an In Bus Element
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — Add an element to the
  port.
- **Duplicate** — Create a duplicate In Bus
  Element block.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — Create a duplicate
  In Bus Element block.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `In Bus
  Element`, and select the block from the menu.
- Copy and paste an In Bus Element block.

In previous releases, these actions create a port, add an element to a port, or
duplicate a block.

### R2023b: Specify elements without bus objects or additional blocks at subsystem interfaces

At both subsystem and model interfaces, you can specify the elements of an input
bus without In Bus Element blocks to represent each element or a
`Simulink.Bus` object to define the bus hierarchy. Previously,
only In Bus Element blocks at model interfaces supported this
functionality.

To add the elements, click the Add element button arrow. Then, select **Add element
without block**.

### R2023a: Property Inspector supports In Bus Element blocks

The Property
Inspector supports In Bus Element and Out Bus
Element blocks.

### R2023a: Diagnostic messages link to related In Bus Element blocks

Warning and error messages for In Bus Element and Out Bus
Element blocks now link to the corresponding block in the block diagram,
helping you quickly find the source of the warning or error. In previous releases,
warning and error messages refer to a hidden block and do not provide a link.
