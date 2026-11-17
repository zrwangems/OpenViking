---
type: simulink-block
title: 'Out Bus Element'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'outbuselement'
documentation_source_path: 'slref/outbuselement.html'
language: zh-CN
chinese_source: worker-translation
---

# Out Bus Element

## 端口
```yaml
ports:
- name: Port_1
  summary: 外部端口的完整或部分输出 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
```

### 输入

### **Port\_1** — 外部端口的完整或部分输出 标量 | 向量 | 矩阵 | 数组 | 总线

连接要传递到父子系统或模型对应外部输出端口的总线、信号或消息。

当多个 Out Bus Element 模块与同一个外部端口关联时，此模块的输入是输出端口处总线的一个元素。模块标签中的第二个文本字段指定元素名称。

当一个 Out Bus Element 模块与外部端口关联时，此模块的输入直接传递到输出端口，或嵌套在输出端口的总线中。要将模块的输入传递到输出端口而不将其嵌套在总线中，请删除模块标签中第二个文本字段的文本。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: 端口名称
  summary: 输出端口的名称 OutBus（默认）| 端口名称
  group: 模块标签
  block_parameter: PortName
  values: '"OutBus"（默认）| 带引号的端口名称'
- name: 元素
  summary: 可选的总线元素指定 signal1（默认）| 元素路径
  group: 模块标签
  block_parameter: Element
  values: '"signal1"（默认）| 带引号的元素路径'
- name: 端口号
  summary: 端口在父模块上的位置 1（默认）| 实数整数
  group: 端口选项卡
  block_parameter: Port
  values: '"1"（默认）| 带引号的实数整数'
- name: 输出名称
  summary: 父子系统或模型中输出总线、信号或消息的名称 无默认值
  group: 端口选项卡
  block_parameter: OutputName
  values: '""（默认）| 带引号的输出名称'
- name: 初始输出
  summary: 父条件执行子系统的初始输出 []（默认）| 标量 | 结构体
  group: 端口选项卡
  block_parameter: InitialOutput
  values: '''[]''（默认）| 带引号的标量 | 带引号的结构体'
- name: 禁用时输出
  summary: 父条件执行子系统禁用时的输出 held（默认）| reset
  group: 端口选项卡
  block_parameter: OutputWhenDisabled
  values: '"held"（默认）| "reset"'
- name: 数据类型
  summary: '数据类型 Inherit: auto（默认）| double | single | half | int8 | uint8 | int16 | uint16 | ...'
  group: 信号选项卡
  block_parameter: OutDataTypeStr
  values: '"Inherit: auto"（默认）| "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32"
    | "int64" | "uint64" | "boolean" | "fixdt(1,16)" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "string" | "Enum: <class name>"
    | "Bus: <object name>" | "ValueType: <object name>" | 带引号的数据类型表达式'
- name: 数据模式
  summary: 输出元素的数据模式 inherit（默认）| signal | message
  group: 信号选项卡
  block_parameter: DataMode
  values: '"inherit"（默认）| "signal" | "message"'
- name: 总线虚拟性
  summary: 虚拟或非虚拟总线 inherit（默认）| virtual | nonvirtual
  group: 信号选项卡
  block_parameter: BusVirtuality
  values: '"inherit"（默认）| "virtual" | "nonvirtual"'
- name: Dimensions
  summary: 信号维度 -1（默认）| 整数 | 1×2 整数向量
  group: 信号选项卡
  block_parameter: PortDimensions
  values: '"-1"（默认）| 带引号的整数 | 带引号的 1×2 整数向量'
- name: Dimensions mode
  summary: 仅允许可变大小或固定大小信号的选项 Inherit（默认）| Fixed | Variable
  group: 信号选项卡
  block_parameter: VarSizeSig
  values: '"Inherit"（默认）| "No" | "Yes"'
- name: Unit
  summary: 物理单位 inherit（默认）| Simulink 软件支持的单位
  group: 信号选项卡
  block_parameter: Unit
  values: '"inherit"（默认）| 带引号的 Simulink 软件支持的单位'
- name: Complexity
  summary: 数值类型 auto（默认）| real | complex
  group: 信号选项卡
  block_parameter: SignalType
  values: '"auto"（默认）| "real" | "complex"'
- name: Minimum
  summary: 最小值 []（默认）| 标量
  group: 信号选项卡
  block_parameter: OutMin
  values: '"[]"（默认）| 带引号的标量'
- name: Maximum
  summary: 最大值 []（默认）| 标量
  group: 信号选项卡
  block_parameter: OutMax
  values: '"[]"（默认）| 带引号的标量'
- name: Description
  summary: 总线、信号或消息的描述 无默认值
  group: 信号选项卡
  block_parameter: Description
  values: '""（默认）| 带引号的描述'
- name: Sample time
  summary: 采样时间 -1（默认）| 标量
  group: Execution Tab
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量'
```

要编辑与 Out Bus Element 模块关联的元素，请在 Simulink® 编辑器中编辑模块标签。

要编辑端口、信号和执行属性，请使用属性检查器。在 Simulink 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 模块标签

### **端口名称** — 输出端口的名称 `OutBus`（默认）| 端口名称

指定一个尚未被系统中其他模块或端口使用的端口名称。该名称显示在父子系统或模型模块上。

要从 Simulink 编辑器更改端口名称，请编辑模块标签的第一个文本字段。

默认 Out Bus Element 模块，模块标签中 OutBus 高亮显示

多个模块可以为同一个端口提供输出，只要每个模块为该端口的唯一元素提供输出即可。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `"OutBus"`（默认）| 带引号的端口名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",PortName="myBus")`

### **元素** — 可选的总线元素指定 `signal1`（默认）| 元素路径

要在输出端口创建总线，请在模块标签的第二个文本字段中指定一个元素。

默认 Out Bus Element 模块，模块标签中 signal1 高亮显示

如何指定元素取决于元素在总线层次结构中的位置。

- 对于输出总线顶层的元素，指定元素名称，例如 `constant`。
- 对于嵌套总线中的元素，指定嵌套总线名称、中间嵌套总线和叶信号，用点分隔，例如 `sinusoidal.sine`。此元素路径不包括顶层总线。

每个输出元素必须唯一，且不得与端口的其他元素重叠。例如，对于嵌套总线，使用一个与嵌套总线对应的 Out Bus Element 模块，或使用多个与嵌套总线元素对应的 Out Bus Element 模块。

要输出信号、消息或总线而不创建总线，请删除模块标签中第二个文本字段的文本。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `"signal1"`（默认）| 带引号的元素路径 |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="constant")`

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Element="sinusoidal.sine")`

### 端口选项卡

要切换选项卡是否可见，请单击显示属性或隐藏属性。

*在 R2025a 之前：要指定属性（如输出名称），请暂停在顶层总线、信号或消息的名称上。然后，单击指定属性。或者，在可用时，单击属性摘要。*

有关端口名称的信息，请参阅**端口名称**。

### **端口号** — 端口在父模块上的位置 `1`（默认）| 实数整数

指定与模块对应的端口在父子系统或模型模块上出现的顺序。

- 如果添加一个创建另一个端口的模块，端口号是下一个可用的编号。
- 删除与某个端口关联的所有模块会删除该端口。其他端口会重新编号，使其连续且不跳过任何编号。
- 指定超过端口数量的端口号会为该编号以及任何跳过的连续编号创建端口。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `"1"`（默认）| 带引号的实数整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **输出名称** — 父子系统或模型中输出总线、信号或消息的名称 无默认值

*自 R2023a 起*

指定父子系统或模型中输出总线、信号或消息的名称。该名称显示为线条上的标签。

要显示模型中个别线条或所有线条的传播标签，请参阅显示传播的信号标签。

#### 依赖关系

- 要启用此参数：

  - 模块必须位于模型的顶层。
  - 元素必须是顶层总线、信号或消息。
- 当您将**数据类型**设置为 `Simulink.Bus` 对象时，软件将此参数设置为 `""`（空）。

#### 程序化使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutputName` |
| **值：** | `""`（默认）| 带引号的输出名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/OutBus",OutputName="model-output")`

### **初始输出** — 父条件执行子系统的初始输出 `[]`（默认）| 标量 | 结构体

*自 R2024b 起*

对于条件执行子系统，指定子系统执行之前以及子系统禁用时的模块输出。要从输入信号继承初始输出值，请应用以下两个默认设置：

- 将**初始输出**设置为 `[]`。
- 将**禁用时输出**设置为 `held`。

软件尝试从输入信号继承输出值。如果输入信号不是初始输出值的有效来源，则初始输出值 `[]` 被视为 `double(0)`。有关详细信息，请参阅条件子系统初始输出值。

有关指定初始条件结构体的信息，请参阅为总线元素指定初始条件。

#### 提示

如果条件子系统驱动 Merge 模块，则不需要为 Out Bus Element 模块指定初始条件。有关详细信息，请参阅未充分指定的初始化检测。

#### 依赖关系

要启用此参数：

- 模块必须位于条件执行子系统或模型的顶层。
- 元素必须是顶层总线、信号或消息。

#### 限制

- 此模块不支持 `inf` 或 `NaN` 的初始输出。
- 当输入为虚拟总线时，**初始输出**值 `[]` 被视为 `double(0)`。
- 当输入包含非虚拟总线时，**初始输出**不支持非零标量值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialOutput` |
| **值：** | `'[]'`（默认）| 带引号的标量 | 带引号的结构体 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mdl/condss/Output",InitialOutput="3")`

### **禁用时输出** — 父条件执行子系统禁用时的输出 `held`（默认）| `reset`

*自 R2024b 起*

指定父条件执行子系统禁用时模块输出发生的情况。

- `held` — 子系统禁用时输出保持不变。
- `reset` — 子系统禁用时输出重置为**初始输出**给定的值。

#### 提示

- 如果父子系统的输出连接到 Merge 模块，请勿将此参数设置为 `reset`。
- 对于函数调用子系统中的 Out Bus Element 模块，仅当 Function-Call Subsystem 模块连接到 Stateflow® 图中的状态时，此参数才有意义。有关详细信息，请参阅将函数调用子系统绑定到状态（Stateflow）。

#### 依赖关系

要启用此参数：

- 模块必须位于具有有效启用和禁用语义的条件子系统的顶层。例如，启用子系统中的 Out Bus Element 模块支持此参数，但触发子系统中的 Out Bus Element 模块不支持此参数。
- 元素必须是顶层总线、信号或消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputWhenDisabled` |
| **值：** | `"held"`（默认）| `"reset"` |

**示例：** `set_param("mdl/condss/Output",InitialOutput="3",OutputWhenDisabled="reset")`

### 信号选项卡

要切换选项卡是否可见，请单击显示属性或隐藏属性。

当您指定属性时，相应总线、信号或消息的名称旁边会出现一个括号。要完整显示指定的属性，请单击属性摘要。

指针暂停在总线名称旁边的属性摘要上

*在 R2025a 之前：要指定属性（如数据类型），请暂停在总线、信号或消息的名称上。然后，单击指定属性。或者，在可用时，单击属性摘要。*

### **数据类型** — 数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

总线、信号或消息的数据类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType` 对象）。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Simulink 支持的数据类型。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用前面带有 `Enum:` 的类型名称。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用前面带有 `Bus:` 的 `Simulink.Bus` 对象名称。例如，指定 `Bus: myBusObject`。
- 值类型 — 使用前面带有 `ValueType:` 的 `Simulink.ValueType` 对象名称。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `"Fixed-point: unspecified scaling"` 以外的值。

当您指定 `Simulink.ValueType` 对象作为数据类型时，元素的某些参数会被忽略。例如，**最小值**、**最大值**和**单位**参数会被忽略。软件使用 `Simulink.ValueType` 对象的对应属性。例如，假设您为某个元素将**单位**设置为 `ft/s`。当该元素的**数据类型**指定了一个单位为 `m/s` 的 `ValueType` 对象时，该元素使用 `m/s` 而不是 `ft/s`。

当您指定 `Simulink.Bus` 对象作为数据类型时，元素的某些参数会重置为其默认值。例如，**最小值**、**最大值**和**单位**参数会被重置。软件改为使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象的对应属性。

#### 提示

- 当您使用 `Simulink.Bus` 对象或具有 `Simulink.Bus` 对象数据类型的 `Simulink.ValueType` 对象指定总线时，属性检查器和模块对话框会显示由对应 `Simulink.BusElement` 对象定义的元素。
- 要使用类型编辑器创建 `Simulink.Bus` 对象，请单击打开类型编辑器。

#### 依赖关系

要将 `Simulink.Bus` 对象指定为总线元素端口处总线的数据类型，Out Bus Element 模块必须表示该总线或该总线的一个元素。

#### 程序化使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"`（默认）| `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16)"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"string"` | `"Enum: <class name>"` | `"Bus: <object name>"` | `"ValueType: <object name>"` | 带引号的数据类型表达式 |

**示例：** `set_param("mymodel/myBus.signal1",OutDataTypeStr="int32")`

### **数据模式** — 输出元素的数据模式 `inherit`（默认）| `signal` | `message`

指定输出元素的数据模式。

- `inherit` — 输出元素继承其数据模式。
- `signal`  — 输出元素必须是信号或包含信号的总线。
- `message` — 输出元素必须是消息或包含消息的总线。

#### 依赖关系

要启用此参数，模块必须位于模型的顶层。

#### 程序化使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `DataMode` |
| **值：** | `"inherit"`（默认）| `"signal"` | `"message"` |

**示例：** `set_param("mymodel/OutBus",DataMode="signal")`

### **总线虚拟性** — 虚拟或非虚拟总线 `inherit`（默认）| `virtual` | `nonvirtual`

指定是继承总线虚拟性，还是将总线定义为虚拟或非虚拟。有关详细信息，请参阅复合接口指南。

此参数决定模块是继承还是定义总线虚拟性。如果模块定义总线虚拟性，且输入总线的虚拟性与定义不匹配，则编译模型会产生错误。

#### 依赖关系

要启用此参数，**数据类型**必须解析为 `Simulink.Bus` 对象。例如，将**数据类型**设置为 `Simulink.Bus` 对象或指定 `Simulink.Bus` 对象作为其数据类型的 `Simulink.ValueType` 对象。

#### 程序化使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，用点分隔层次结构中的每个名称。

|  |  |
| --- | --- |
| **参数：** | `BusVirtuality` |
| **值：** | `"inherit"`（默认）| `"virtual"` | `"nonvirtual"` |

**示例：** `set_param("mymodel/myBus.nestedBus",BusVirtuality="nonvirtual")`

### **Dimensions** — 信号维度 `-1`（默认）| 整数 | `1`×`2` 整数向量

指定信号的维度。

- `-1` — 信号可以具有任意维度。
- `N` — 信号必须是大小为 `N` 的向量。
- `[R C]` — 信号必须是具有 `R` 行和 `C` 列的矩阵。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `1`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `PortDimensions` |
| **值**：| `"-1"`（默认）| 带引号的整数 | 带引号的 `1`×`2` 整数向量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",PortDimensions="[1
3]")`

### **Dimensions mode** — 仅允许可变大小或固定大小信号的选项 `Inherit`（默认）| `Fixed` | `Variable`

指定允许的信号类型。

- `Inherit` — 允许可变大小和固定大小信号。
- `Variable` — 仅允许可变大小信号。
- `Fixed` — 仅允许固定大小信号。不允许可变大小信号。

当信号为可变大小时，**Dimensions** 参数指定信号的最大维度。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `Inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的维度模式。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度模式。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `VarSizeSig` |
| **值**：| `"Inherit"`（默认）| `"No"` | `"Yes"` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",VarSizeSig="No")`

### **Unit** — 物理单位 `inherit`（默认）| Simulink 软件支持的单位

指定信号的物理单位。有关支持的单位列表，请在 MATLAB 命令窗口中输入 `showunitslist`。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `inherit`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的单位。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的单位。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `Unit` |
| **值**：| `"inherit"`（默认）| 带引号的 Simulink 软件支持的单位 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/myBus.signal1",Unit="m/s")`

### **Complexity** — 数值类型 `auto`（默认）| `real` | `complex`

指定信号的数值类型。要选择信号的数值类型，请选择 `auto`。否则，请选择实数或复数信号类型。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `auto`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的复数性。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的复数性。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `SignalType` |
| **值**：| `"auto"`（默认）| `"real"` | `"complex"` |

**Example:** `set_param("mymodel/myBus.signal1",SignalType="real")`

### **Minimum** — 最小值 `[]`（默认）| 标量

软件检查的范围的下限值。

此数字必须是有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最小值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的最小值。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `"[]"`（默认）| 带引号的标量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMin="0")`

### **Maximum** — 最大值 `[]`（默认）| 标量

软件检查的范围的上限值。

此数字必须是有限实数双精度标量值。

软件使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `[]`。软件使用 `Simulink.Bus` 对象中 `Simulink.BusElement` 对象指定的最大值。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的最大值。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `"[]"`（默认）| 带引号的标量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",OutMax="2")`

### **Description** — 总线、信号或消息的描述 无默认值

使用描述来记录有关总线、信号或消息的信息，例如其使用位置。此信息不影响处理。

#### 依赖关系

- 当 **Data type** 指定 `Simulink.Bus` 对象时，软件将此参数设置为 `""`（空）。软件使用 `Simulink.Bus` 对象指定的描述。
- 当 **Data type** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的描述。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `Description` |
| **值**：| `""`（默认）| 带引号的描述 |
| **Data Types:** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/myBus.signal1",Description="This signal is
used by...")`

### Execution Tab

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

当您指定属性时，相应总线、信号或消息的名称旁边会出现一个括号。要显示指定的属性，请点击 Specify execution attributes。

指针暂停在总线名称旁边的 Specify execution attributes 按钮上

*在 R2025a 之前：要指定执行属性，请将鼠标暂停在总线、信号或消息的名称上。然后，点击 Specify execution attributes。*

### **Sample time** — 采样时间 `-1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time。

默认情况下，信号继承其采样时间。

#### 编程使用

要以编程方式设置元素的属性值，请使用 `set_param` 函数。将元素指定为模型名称或子系统模块路径、正斜杠以及端口名称或总线元素路径。对于总线元素端口，总线元素路径提供从顶层总线到目标元素的层次结构，层次结构中每个名称之间用点分隔。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量 |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Subsystem1/myBus.signal1",SampleTime="0.01")`
## 所属库

Simulink / Ports & Subsystems Simulink / Sinks HDL Coder / Ports & Subsystems HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

当您在生成 HDL 代码的子系统中使用此模块时，此模块可用于简化子系统总线接口，但它不包含在硬件实现中。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

此模块支持 `Simulink.ValueType` 对象的代码生成。有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type。

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2017a 中引入**

### R2025a：更轻松地指定端口、信号和执行属性

您现在可以更轻松地指定端口、信号和执行属性。

- 要切换端口、信号和执行属性的显示，请点击 Show attributes 或 Hide attributes。端口、信号和执行属性现在显示在选项卡上。Show attributes 或 Hide attributes 按钮取代了在以前版本中将鼠标暂停在总线、信号或消息名称上时出现的按钮。
- 当您指定执行属性时，相应总线、信号或消息的名称旁边会出现一个括号。要显示指定的属性，请点击 Specify execution attributes。
- 要编辑端口名称，请双击顶层总线、信号或消息的名称。或者，在 **Port** 选项卡上，指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements 并选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上点击 Open Type Editor。
- **Dims mode** 现在命名为 **Dimensions mode**。

### R2024b：指定初始条件

在条件执行的子系统和模型中，Out Bus Element 模块现在支持顶层元素的初始条件。对于非总线信号，将 **Initial output** 设置为与信号具有相同维度和复数性的值。对于总线，将 **Initial output** 设置为 MATLAB 结构体，其字段具有与总线元素相同的名称和层次结构。要指定子系统禁用时模块输出的行为，请使用 **Output when disabled** 模块参数。

### R2024a：无需总线对象或额外模块即可指定元素

当子系统或模型具有输出总线元素端口时，您无需指定 `Simulink.Bus` 对象或添加 Out Bus Element 模块来：

- 向输出端口添加元素。
- 在输出端口指定元素的属性。

要向端口添加元素，请选择要包含新元素的元素。然后，点击 Add element 并选择以下选项之一：

- **Add element with block** — 向端口添加元素以及表示该元素的 Out Bus Element 模块。
- **Add element without block** — 向端口添加元素，但不添加表示该元素的 Out Bus Element 模块。

要以编程方式向输出总线添加元素而不向框图中添加模块，请使用 `Simulink.Bus.addElementToPort` 函数。

### R2024a: 将模块拖到新位置时选择新选项

当您按下 **Ctrl** 并将 Out Bus Element 模块拖到新位置时，您会收到更清晰的选项：

- **New Port** — 创建一个端口。
- **New Element** — 当被拖动的模块表示端口的一个元素而非完整端口时，向该端口添加一个元素。

在之前的版本中，您会收到两个选项：

- **Create New Port** — 创建一个端口。
- **Use Existing Port** — 当被拖动的模块表示端口的一个元素而非完整端口时，向该端口添加一个元素。否则，创建一个端口。

### R2024a: 添加或复制模块会创建一个端口

以下操作现在会一致地创建一个端口：

- 双击画布。然后，开始键入 `Out Bus Element`，并从菜单中选择该模块。
- 复制并粘贴一个 Out Bus Element 模块。

在之前的版本中，这些操作会创建一个端口或向端口添加一个元素。

### R2023a: 指定端口输出的名称

对于位于模型顶层的 Out Bus Element 模块，使用 **Output name** 模块参数来指定出现在父子系统或模型中的顶层总线、信号或消息的名称。

### R2023a: 属性检查器支持 Out Bus Element 模块

属性检查器支持 In Bus Element 和 Out Bus Element 模块。

### R2023a: 诊断消息链接到相关的 Out Bus Element 模块

In Bus Element 和 Out Bus Element 模块的警告和错误消息现在会链接到框图中对应的模块，帮助您快速找到警告或错误的来源。在之前的版本中，警告和错误消息引用一个隐藏模块，并且不提供链接。

## 描述

指定外部端口的输出

Out Bus Element 模块将总线、信号或消息作为外部端口的输出提供。

要将多个总线、信号或消息组合成一个输出总线，请使用多个与同一端口对应的 Out Bus Element 模块。Out Bus Element 模块结合了 Bus Creator 模块和 Outport 模块的功能。所有与同一端口对应的 Out Bus Element 模块共享一个对话框。

对于包含由许多总线元素组成的总线的接口，Out Bus Element 模块：

- 减少框图中的信号线复杂度和杂乱。
- 允许您更轻松地对接口进行增量更改。
- 允许在更接近使用点的地方访问总线元素，避免使用 Bus Creator 和 From 模块配置。

要将接口转换为使用 Out Bus Element 模块，请参阅 Simplify Subsystem and Model Interfaces with Bus Element Ports。

Out Bus Element 模块不支持将消息和信号元素混合作为输入。

当您将输出数据保存到工作区或文件时，由根级 Out Bus Element 模块组定义的总线数据会与根级 Outport 模块数据一起记录。
