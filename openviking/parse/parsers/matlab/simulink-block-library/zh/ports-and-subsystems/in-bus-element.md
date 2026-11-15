---
type: simulink-block
title: 'In Bus Element'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'inbuselement'
language: zh-CN
chinese_source: worker-translation
---

# In Bus Element

## 端口

### 输出

### **Port\_1** — 从外部端口选择的输入 scalar | vector | matrix | array | bus

从父子系统或模型的对应外部输入端口选择总线、信号或消息。

虽然可以选择总线元素，但不能选择总线数组的元素。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** Yes

## 参数

要编辑与 In Bus Element 模块关联的元素，请在 Simulink® Editor 中编辑模块标签。

要编辑端口、信号、执行和消息属性，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 模块标签

### **Port name** — 输入端口名称 `InBus` (default) | port name

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

### **Element** — 可选总线元素规范 `signal1` (default) | element path

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

### Port 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

有关端口名称的信息，请参阅 **Port name**。

### **Port number** — 端口在父模块上的位置 `1` (default) | real integer

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

### Signal 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

指定属性后，相应总线、信号或消息名称旁边会出现括号内容。要完整显示指定的属性，请点击属性摘要。

指针停留在总线名称旁边的属性摘要上

*在 R2025a 之前：要指定属性（例如数据类型），请将指针停在总线、信号或消息的名称上。然后点击 Specify attributes。或者，在可用时点击属性摘要。*

### **Data type** — 数据类型 `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

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

### **Bus virtuality** — 虚拟或非虚拟总线 `inherit` (default) | `virtual` | `nonvirtual`

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

### **Data mode** — 输入元素的数据模式 `inherit` (default) | `signal` | `message`

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

### **Dimensions** — 信号维度 `-1` (default) | integer | `1`-by-`2` vector of integers

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

### **Dimensions mode** — 用于仅允许可变大小或固定大小信号的选项 `Inherit` (default) | `Fixed` | `Variable`

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

### **Unit** — 物理单位 `inherit` (default) | unit supported by Simulink software

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

### **Complexity** — 数值类型 `auto` (default) | `real` | `complex`

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

### **Minimum** — 最小值 `[]` (default) | scalar

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

### **Maximum** — 最大值 `[]` (default) | scalar

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

### **Description** — 总线、信号或消息的描述 无默认值

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

### Execution 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

指定属性后，相应总线、信号或消息名称旁边会出现括号内容。要显示指定的属性，请点击 Specify execution attributes。

指针停留在总线名称旁边的 Specify execution attributes 按钮上

*在 R2025a 之前：要指定执行属性，请将指针停在总线、信号或消息的名称上。然后点击 Specify execution attributes。*

### **Sample time** — 采样时间 `-1` (default) | scalar

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

### **Events** — 用于基于流入端口的数据流触发模型分区的选项 event trigger objects 的 cell 数组

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

### 队列属性

仅当模块位于模型顶层且将 **Data mode** 参数设置为 `message` 时，队列属性才可见。

要指定队列属性，请在总线或消息名称旁边点击 Use default queue attributes。

指针停留在总线名称旁边的 Use default queue attributes 按钮上

### **Use default queue attributes** — 默认或自定义队列规范 on (default) | off

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

### **Queue capacity** — 消息存储容量 1 (default) | scalar

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

### **Queue type** — 选择 FIFO 或 LIFO 队列 `LIFO` (default) | `FIFO`

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

### **Queue overwriting** — 队列消息覆盖策略 on (default) | off

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

## 所属库

Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Ports & Subsystems HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

当在生成 HDL 代码的子系统中使用此模块时，可使用此模块简化子系统总线接口，但它不包含在硬件实现中。

要详细了解如何使用总线进行 HDL 代码生成，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

此模块支持为 `Simulink.ValueType` 对象生成代码。有关值类型的详细信息，请参阅 Specify Common Set of Signal Properties as Value Type。

**数据类型支持**

此模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2017a 中引入**

### R2025a：更轻松地指定端口、信号和执行属性

现在可以更轻松地指定端口、信号和执行属性。

- 要切换端口、信号和执行属性的显示，请点击 Show attributes 或 Hide attributes。端口、信号和执行属性现在显示在选项卡上。Show attributes 或 Hide attributes 按钮取代了以前版本中将指针停在总线、信号或消息名称上时出现的按钮。
- 指定执行属性后，相应总线、信号或消息名称旁边现在会出现括号内容。要显示指定的属性，请点击 Specify execution attributes。
- 要编辑端口名称，请双击顶层总线、信号或消息的名称。或者，在 **Port** 选项卡上指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements，然后选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上点击 Open Type Editor。
- **Dims mode** 现在命名为 **Dimensions mode**。

### R2024b：将元素名称传播为信号标签

现在可以从 In Bus Element 模块传播元素名称。例如，对于标签为 `InBus.nonconstant.chirp` 的 In Bus Element 模块，传播后的名称为 `chirp`。

有关详细信息，请参阅 Signal Label Propagation。

### R2024a：将模块拖动到新位置时选择新选项

按住 **Ctrl** 并将 In Bus Element 模块拖动到新位置时，会看到更清晰的选项：

- **New Port** — 创建端口。
- **New Element** — 向端口添加元素。
- **Duplicate** — 创建 In Bus Element 模块的副本。

在以前的版本中，会看到两个选项：

- **Create New Port** — 创建端口。
- **Use Existing Port** — 创建 In Bus Element 模块的副本。

### R2024a：添加或复制模块会创建端口

这些操作现在始终创建端口：

- 双击画布。然后开始键入 `In Bus Element`，并从菜单中选择该模块。
- 复制并粘贴 In Bus Element 模块。

在以前的版本中，这些操作会创建端口、向端口添加元素或复制模块。

### R2023b：在子系统接口处无需总线对象或额外模块即可指定元素

在子系统接口和模型接口处，可以指定输入总线的元素，而无需使用 In Bus Element 模块来表示每个元素，也无需使用 `Simulink.Bus` 对象来定义总线层次结构。以前，只有模型接口处的 In Bus Element 模块支持此功能。

要添加元素，请点击 Add element 按钮箭头。然后选择 **Add element without block**。

### R2023a：Property Inspector 支持 In Bus Element 模块

Property Inspector 支持 In Bus Element 和 Out Bus Element 模块。

### R2023a：诊断消息链接到相关的 In Bus Element 模块

In Bus Element 和 Out Bus Element 模块的警告和错误消息现在链接到框图中的对应模块，帮助您快速找到警告或错误的来源。在以前的版本中，警告和错误消息引用隐藏模块，且不提供链接。

## 描述

从外部端口选择输入

In Bus Element 模块从接收总线、信号或消息的外部端口选择输入。

当端口接收总线时，In Bus Element 模块结合了 Inport 模块和 Bus Selector 模块的功能。要从总线中选择多个元素，请使用多个 In Bus Element 模块。所有与同一端口对应的 In Bus Element 模块共享一个对话框。

对于包含由许多总线元素组成的总线的接口，In Bus Element 模块可以：

- 减少框图中信号线的复杂度和杂乱。
- 使您更容易对接口进行增量更改。
- 允许在使用点附近访问总线元素，避免使用 Bus Selector 和 Goto 模块配置。

要将接口转换为使用 In Bus Element 模块，请参阅 Simplify Subsystem and Model Interfaces with Bus Element Ports。

In Bus Element 模块不支持将消息元素和信号元素混合作为输出。
