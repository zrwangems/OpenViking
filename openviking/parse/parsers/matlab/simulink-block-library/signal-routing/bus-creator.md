---
type: simulink-block
title: 'Bus Creator'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'buscreator'
---

# Bus Creator

Group input signals, buses, or messages into bus

## 中文

将输入信号、总线或消息组合到总线中

### 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

Bus Creator 模块将输入信号、总线或消息合并到总线中，该总线保留信号、嵌套总线和消息的各自的身份。默认情况下，Bus Creator 模块创建一个*虚拟总线*，它类似于用束线带绑在一起的一捆电线。或者，该模块可以创建*非虚拟总线*，这类似于 C 代码中的结构体。

总线元素必须具有唯一名称。默认情况下，总线的每个元素都继承连接到 Bus Creator 模块的元素的名称。如果存在重复名称，Bus Creator 模块会将端口号追加到所有输入元素名称。对于没有名称的元素，Bus Creator 模块会生成 `signaln` 形式的名称，其中 `n` 是连接到元素的端口号。当您搜索元素源或选择元素以连接到其他模块时，您可以按名称引用元素。有关元素命名规范，请参阅信号名称和标签。

要按名称从总线中提取元素，请使用 Bus Selector 模块。

要创建包含其他总线的总线，请将其他总线连接到 Bus Creator 模块输入端口。

**提示**

对于位于子系统和模型接口上的总线，使用 Out Bus Element 模块，而不是 Bus Creator 模块和 Outport 模块。Out Bus Element 模块能够：

- 减少模块图中线的复杂度和杂乱无章。
- 允许您更轻松地逐步更改接口。

### 端口

#### 输入

#### **Port\_1** — 要包含在总线中的输入元素 标量 | 向量 | 矩阵 | 数组 | 总线

输入端口接受要包含在总线中的元素。输入端口的数量由**输入数目**参数决定。

每个 Bus Creator 模块都支持这些输入元素的组合：

- 仅信号
- 信号和信号总线
- 仅消息
- 消息和总线
- 仅限总线

您可以指定可变大小输入信号，其上界小于对应的 Bus Creator 模块输入端口可以接受的可变大小信号的上界。要配置 Bus Creator 模块输入端口可接受的可变大小信号的上界，请使用 `Simulink.BusElement` 对象。有关详细信息，请参阅 `Simulink.BusElement`。可变大小输入信号的维度必须与对应的 Bus Creator 模块输入端口配置的可接受信号维度相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输出虚拟或非虚拟总线 标量 | 总线

输出总线由输入元素组成。

**以非虚拟总线输出**参数指定输出总线是虚拟总线还是非虚拟总线。软件将虚拟总线视为其组成元素，将非虚拟总线视为标量。

有关总线类型的详细信息，请参阅合成接口规范。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

#### **输入数目** — 模块输入的数目 `2` (默认) | 整数

要创建一个总线，模块输入的数目必须为大于或等于 2 的整数。

增加输入数目会向模块添加未连接的输入端口。在对模型进行仿真之前，请确保为每个输入端口连接了一个输入。

如果每个输入端口都已连接，您可以通过将另一条线连接到 Bus Creator 模块来添加一个输入端口。

A line is dragged near a Bus Creator block with two connected ports and a third port appears.

以交互方式添加端口会更新**输入的数目**参数值并将新输入添加到**输入**列表。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

将输入的数目指定为大于或等于 2 的整数。

|  |  |
| --- | --- |
| **参数:** | `Inputs` |
| **值:** | `'2'` (默认) | integer in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb, Inputs="3")`

#### **输入** — 模块输入 元素名称列表

**输入**列表提供进入模块的元素，包括嵌套总线的元素。元素旁边的箭头表示输入是总线。要显示该总线的内容，请点击箭头。

要对输入元素重新排序，请从**输入**列表中选择一个或多个顶层元素。然后，将元素拖到新位置。

要添加或删除输入元素，请分别点击 Add 或 Remove。在仿真模型之前，确保每个输入端口都已连接。

要刷新输入元素列表，请点击 Refresh。例如，在以下情况下刷新输入元素列表：

- 在对话框打开时重命名输入元素。
- 添加、删除或重新排序未命名的输入元素。Bus Creator 模块将这些元素命名为 `signalN`，其中 *N* 是对应模块端口的编号。当对应的模块端口更改时，自动生成的名称也会随之更改。

要按名称过滤输入元素（使用或不使用正则表达式均可），请在**过滤器**框中输入搜索词。请勿将搜索词括在引号内。（可选）通过点击 Show filtered results as a flat list 将过滤后的结果显示为扁平列表。扁平列表使用圆点表示法来反映总线层次结构。默认情况下，过滤结果显示在层次结构树中。

*在 R2025a 之前的版本中: 要使用正则表达式进行过滤，请点击 Show filtering options。然后，选择**启用正则表达式**。*

要选择进入模块的元素的来源，请在列表中选择该元素。然后，点击 Select source blocks。属性检查器显示选定源模块的参数。当您选择包含多个元素的源模块时，属性检查器会显示具有焦点的源模块的参数。

无法撤消或重做对**输入**列表的更改。

##### 提示

- 当**输出数据类型**设置为 `Simulink.Bus` 对象时，要显示哪个 `Simulink.BusElement` 对象映射到顶层输入，请将鼠标悬停在顶层输入上。括号中会显示从输入到 `Simulink.BusElement` 对象的映射，例如 `Input1 → BusElementObject1`。
- 正则表达式允许您根据输入元素是否匹配某个模式进行过滤。例如，要显示其名称以小写字母 `t` 结尾的所有元素，请在**过滤器**框中输入 `t$`。有关详细信息，请参阅 正则表达式。

#### **输出数据类型** — 输出总线的数据类型 **Inherit: auto** (默认) | **Bus: <object name>**

指定输出总线的数据类型。

如果选择 **Bus: <object name>**，请用 `Simulink.Bus` 对象的名称替换 `<object name>`。编辑模型时，必须可以访问总线对象。

##### 提示

- 要使用类型编辑器创建一个 `Simulink.Bus` 对象，请点击 Open Type Editor。
- 要从输出总线创建一个 `Simulink.Bus` 对象，请使用 `Simulink.Bus.createObject` 函数。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `"Inherit: auto"` (默认) | `"Bus: <object name>"` |

**示例:** `set_param(gcb, OutDataTypeStr="Bus: control")`

#### **元素名称** — 输出总线元素名称的源 **根据输入** (默认) | **根据输出数据类型**

默认情况下，Bus Creator 模块使用模块输入的名称作为输出总线元素的名称，即使将 `Simulink.Bus` 对象指定为数据类型也是如此。

- **根据输入** - 从模块输入继承输出总线元素的名称。

  *在 R2025a 之前的版本中: 选择**使用来自输入的名称，而不是来自总线对象的名称**。*
- **根据输出数据类型** - 从指定的总线对象继承输出总线元素的名称。

  *在 R2025a 之前的版本中: 清除**使用来自输入的名称，而不是来自总线对象的名称**。*

将**元素名称**设置为**根据输出数据类型**时：

- 强制应用强数据定型。
- 避免在总线对象和模型中多次输入一个元素名称。多次输入名称可能导致意外的元素名称不匹配。
- 支持在数组元素之间必须具有一致的元素名称这一总线数组要求。

当**元素名称**设置为**根据输入**时，考虑将**元素名称不匹配**配置参数设置为**错误**。此配置参数检查输入元素名称是否与总线对象中的对应名称匹配。

##### 依赖关系

要启用此参数，请将**输出数据类型**设置为 `Simulink.Bus` 对象。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InheritFromInputs` |
| **值:** | `"on"` (默认) | `"off"` |

**示例:** `set_param(gcb, InheritFromInputs="off")`

下表将交互值映射到此参数的等效编程值。

| **元素名称**值 | `InheritFromInputs` 值 |
| --- | --- |
| **根据输入**（默认值） | `"on"`（默认值） |
| **根据输出数据类型** | `"off"` |

#### **以非虚拟总线输出** — 输出非虚拟总线的选项 **off** (默认) | **on**

选择此参数以输出非虚拟总线。

非虚拟总线类似于 C 代码中的结构体。选中此参数可以：

- 构造总线数组。
- 总线数据需要跨 MATLAB Function 模块或 Stateflow® 图边界。
- 将总线数据打包为生成的 C 代码中的结构体。
- 通过 S-Function 对接外部代码。
- 减少生成代码中传递给子组件的函数参量数目。

非虚拟总线中的所有元素都必须具有相同的采样时间，即使关联的 `Simulink.Bus` 对象的元素为某些元素指定了继承采样时间也是如此。任何导致包含不同采样率元素的非虚拟总线的操作都会生成错误。要更改采样时间不同于其他非虚拟总线输入元素的元素或总线的采样时间，请使用 Rate Transition 模块。有关详细信息，请参阅Modify Sample Times for Nonvirtual Buses。

##### 依赖关系

要启用此参数，请将**输出数据类型**设置为 `Simulink.Bus` 对象。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `NonVirtualBus` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb, NonVirtualBus="on")`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**数据类型支持**

此模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最高二维） | 是 | 半精度  单精度  双精度 | 是 | 是 | 是 | 是 |

**优化**

您可以使用以下 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源复用*是一种面积优化，其中 HDL Coder 确定多个在功能上等效的资源，并用单个资源替换它们。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，其中 HDL Coder 将向量数据路径变换为标量数据路径（或多个较小的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*或寄存器重定时是一种速度优化，它可以移动设计中的现有延迟，以在缩减关键路径的同时保留功能性行为。  对于 Sqrt 模块，HDL Coder 在模块周围（而不是在模块内）分布流水线寄存器。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟频率流水线*是 HDL Coder 中的一个优化框架，它允许其他速度优化和面积优化在时钟频率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带寄存器的模块模式或组合，通过在设计中的模块中插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| 关键路径估计 (HDL Coder) | 要快速确定设计中最可能的关键路径，请使用*关键路径估计*。关键路径估计加速寻找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅Characterized Blocks (HDL Coder)。 |

**HDL 建模规范**

有关最佳做法，请参阅：

- Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)

**限制和注意事项**

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅Buses (HDL Coder)。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: 更轻松、直观地指定参数值

Bus Creator 模块现在为模块参数值提供更直观和简化的编辑功能。

现在，您可以在属性检查器中指定 Bus Creator 模块参数值。您可以继续使用“模块参数”对话框。

下表描述参数和交互更改。

| 目的 | R2025a 之前的操作 | R2025a 及之后的操作 |
| --- | --- | --- |
| 应用更改。 | 进行您的更改。然后，点击**应用**或**确定**。 | 进行您的更改。  在属性检查器或“模块参数”对话框中指定模块参数值时，更改会立即应用。 |
| 使用正则表达式过滤。 | 点击 Show filtering options，然后选择**启用正则表达式**。然后，在**按名称过滤**框中输入搜索词。 | 在**过滤**框中输入搜索词。 |
| 将过滤结果显示为扁平列表。 | 点击**将过滤结果显示为扁平列表**。 | 点击 Show filtered results as a flat list。 |
| 查找源模块。 | 选择一个或多个输入。然后，点击**查找**。  软件会突出显示源模块。 | 选择一个或多个输入。然后，点击 Select source blocks。  软件会选择源模块，并且属性检查器会显示具有焦点的模块的参数。 |
| 添加模块输入。 | 点击**添加**。 | 点击 Add。 |
| 刷新输入列表。 | 点击**刷新**。 | 点击 Refresh。 |
| 删除模块输入。 | 点击**删除**。 | 点击 Remove。 |
| 重新排序输入。 | 选择一个或多个相邻输入。然后，点击**上移**或**下移**，直到输入处于所需位置。 | 选择一个或多个输入。然后，将输入拖到所需位置。 |
| 打开类型编辑器以定义 `Simulink.Bus` 对象。 | 点击 Show data type assistant，并将**模式**设置为**总线对象**。然后，点击**编辑**按钮。 | 点击 Open Type Editor。 |
| 指定输出总线元素名称的源。 | 选中或清除**使用来自输入的名称，而不是来自总线对象的名称**复选框。 | 将**元素名称**设置为**根据输入**或**根据输出数据类型**。 |
| 重命名输入。 | 编辑输入元素的信号标签。  或者，选择**要求输入的名称与以上的名称匹配**，选择元素，并在**重命名所选信号**框中指定新名称。 | 编辑输入元素的信号标签。 |

#### R2025a: **要求输入的名称与以上的名称匹配**和**重命名所选信号**已删除

**要求输入的名称与以上的名称匹配**和**重命名所选信号**参数已删除。要指定所需名称，请改用 `Simulink.Bus` 对象。

1. 将**输出数据类型**设置为 `Simulink.Bus` 对象。
2. 选择以下选项之一：

   - 要从指定的 `Simulink.Bus` 对象继承输出总线元素名称，请将**元素名称**设置为**根据输出数据类型**。
   - 若要求输入名称与指定的 `Simulink.Bus` 对象中的名称匹配，请将**元素名称**设置为**根据输入**，并将**元素名称不匹配**配置参数设置为**错误**。此配置参数检查输入名称是否与 `Simulink.Bus` 对象中的对应名称匹配。

不推荐将 `Inputs` 设置为以逗号分隔的元素名称列表。

有关详细信息，请参阅**元素名称**和**元素名称不匹配**。

#### R2023a: 可变大小输入信号的上界可以小于对应的 Bus Creator 模块输入端口可接受的可变大小信号的上界

从 R2023a 开始，Bus Creator  模块支持可变大小输入信号，其上界小于对应的 Bus Creator 模块输入端口可接受的可变大小信号的上界。

当输入信号的上界不等于对应的 Bus Creator 模块输入端口可以接受的可变大小信号的上界时，此增强功能允许您使用可变大小输入信号。

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Bus Creator block combines input signals, buses, or messages into a bus,
which retains the separate identities of the signals, nested buses, and messages. By
default, the Bus Creator block creates a *virtual
bus*, which is analogous to a bundle of wires held together by tie wraps.
Alternatively, the block can create a *nonvirtual bus*, which is
analogous to a structure in C code.

Elements of a bus must have unique names. By default, each element of the bus inherits
the name of the element connected to the Bus Creator block. If duplicate
names are present, the Bus Creator block appends the port number to all
input element names. For elements that do not have names, the Bus Creator
block generates names in the form `signaln`, where `n`
is the port number connected to the element. You can refer to elements by name when you
search for their sources or select elements for connection to other blocks. For element
naming guidelines, see Signal Names and Labels.

To extract elements from the bus by name, use a Bus
Selector block.

To create a bus that contains other buses, connect the other buses to the Bus
Creator block input ports.

**Tip**

For buses at subsystem and model interfaces, use Out
Bus Element blocks instead of a Bus Creator block with an
Outport block. Out Bus Element blocks:

- Reduce line complexity and clutter in a block diagram.
- Allow you to more easily change the interface incrementally.

## Ports

### Input

### **Port\_1** — Input element to include in bus scalar | vector | matrix | array | bus

The input ports accept the elements to include in the bus. The number
of input ports is driven by the **Number of inputs**
parameter.

Each Bus Creator block supports these combinations of input elements:

- Signals only
- Signals and signal buses
- Messages only
- Messages and buses
- Buses only

You can specify variable-size input signals with upper bounds smaller
than the upper bounds of the variable-size signals that the corresponding Bus
Creator block input ports can accept. To configure the upper bounds of
variable-size signals that Bus Creator block input ports accept, use a
`Simulink.BusElement` object. For more information, see `Simulink.BusElement`. Variable-size input signals must have the same
dimensionality as the variable-size signals that the corresponding Bus
Creator block input ports are configured to accept.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output virtual or nonvirtual bus scalar | bus

The output bus is composed of the input elements.

The **Output as nonvirtual bus** parameter specifies whether
the output bus is a virtual or nonvirtual bus. The software treats a
virtual bus as its constituent elements and a nonvirtual bus as a
scalar.

For more information about the types of buses, see Composite Interface Guidelines.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of inputs** — Number of block inputs `2` (default) | integer

To create a bus, the number of block inputs must be an integer greater than or equal to
2.

Increasing the number of inputs adds unconnected input ports to the block.
Before you simulate the model, make sure that an input connects to each
input port.

If each input port is already connected, you can add an input port to the Bus
Creator block by connecting another line to it.

A line is dragged near a Bus Creator block with two connected ports and a third port appears.

Interactively adding a port updates the **Number of inputs** parameter
value and adds the new input to the **Inputs** list.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Specify the number of inputs as an integer greater than or equal to 2.

|  |  |
| --- | --- |
| **Parameter:** | `Inputs` |
| **Values:** | `'2'` (default) | integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,
Inputs="3")`

### **Inputs** — Block inputs list of element names

The **Inputs** list provides the elements that enter the
block, including the elements of nested buses. An arrow next to an element
indicates that an input is a bus. To display the contents of that bus, click
the arrow.

To reorder the input elements, select one or more top-level elements from
the **Inputs** list. Then, drag the elements to a new
position.

To add or remove input elements, click Add or Remove, respectively. Before you simulate the
model, make sure that each input port is connected.

To refresh the list of input elements, click Refresh. For example, refresh the list of input
elements when:

- You rename an input element while the dialog box is
  open.
- You add, remove, or reorder unnamed input elements. The
  Bus Creator block names these elements
  `signalN`, where
  *N* is the number of the corresponding
  block port. When the corresponding block port changes, the
  autogenerated name changes.

To filter the input elements by name with or without regular expressions,
enter the search term in the **Filter** box. Do not enclose
the search term in quotation marks. Optionally, display the filtered results
as a flat list by clicking Show filtered results as a flat list. The flat list uses dot notation to
reflect the bus hierarchy. By default, the filtered results appear in a
hierarchical tree.

*Before R2025a: To filter with regular expressions,
click Show filtering options. Then, select **Enable regular
expression**.*

To select the source of an element that enters the block, select the
element in the list. Then, click Select source blocks. The Property Inspector
shows the parameters of the selected source block. When you select the
source block of multiple elements, the Property Inspector shows
the parameters of the source block that has focus.

You cannot undo or redo changes to the
**Inputs** list.

#### Tips

- When you set **Output data type** to a
  `Simulink.Bus` object, to display which
  `Simulink.BusElement` object maps to a
  top-level input, pause on the top-level input. A parenthetical
  displays the mapping from the input to the
  `Simulink.BusElement` object, for example,
  `Input1 → BusElementObject1`.
- Regular expressions let you filter based on whether the input
  elements match a pattern. For example, to display all elements
  whose names end with a lowercase `t`, enter
  `t$` in the **Filter**
  box. For more information, see Regular Expressions.

### **Output data type** — Data type of output bus `Inherit: auto` (default) | `Bus: <object name>`

Specify the data type of the output bus.

If you select `Bus: <object name>`, replace
`<object name>` with the name of a `Simulink.Bus` object. The bus object must be accessible when you edit the
model.

#### Tips

- To create a `Simulink.Bus` object using the
  Type Editor, click Open Type Editor.
- To create a `Simulink.Bus` object from the
  output bus, use the `Simulink.Bus.createObject` function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"Bus: <object name>"` |

**Example:** `set_param(gcb, OutDataTypeStr="Bus: control")`

### **Element names** — Source of output bus element names `From inputs` (default) | `From output data type`

By default, the Bus Creator block uses the names from the block inputs as
the names of the output bus elements, even when you specify a
`Simulink.Bus` object as the data type.

- `From inputs` — Inherit the names of the
  output bus elements from the block inputs.

  *Before R2025a: Select **Use names
  from inputs instead of from bus object**.*
- `From output data type` — Inherit the
  names of the output bus elements from the specified bus
  object.

  *Before R2025a: Clear **Use names
  from inputs instead of from bus object**.*

Setting **Element names** to `From output data
type`:

- Enforces strong data typing.
- Avoids having to enter an element name multiple times: in the bus
  object and in the model. Entering the name multiple times can create
  accidental element name mismatches.
- Supports the array of buses requirement to have consistent element
  names across array elements.

When you set **Element names** to `From
inputs`, consider setting the **Element name mismatch**
configuration parameter to `error`. This
configuration parameter checks that the input element names match the
corresponding names in the bus object.

#### Dependencies

To enable this parameter, set **Output data type** to a `Simulink.Bus`
object.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InheritFromInputs` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param(gcb,
InheritFromInputs="off")`

This table maps the interactive values to the equivalent programmatic
values of this parameter.

| **Element names** Value | `InheritFromInputs` Value |
| --- | --- |
| `From inputs` (default) | `"on"` (default) |
| `From output data type` | `"off"` |

### **Output as nonvirtual bus** — Option to output nonvirtual bus `off` (default) | `on`

Select this parameter to output a nonvirtual bus.

A nonvirtual bus is analogous to a structure in C code. Select this
parameter to:

- Construct an array of buses.
- Have bus data cross MATLAB Function block or
  Stateflow® chart boundaries.
- Package bus data as structures in generated C code.
- Interface with external code through an S-function.
- Reduce the number of function arguments passed to a
  subcomponent in generated code.

All elements in a nonvirtual bus must have the same sample time, even if the elements of
the associated `Simulink.Bus` object specify inherited sample times for
some elements. Any operation resulting in a nonvirtual bus containing elements with
different sample rates generates an error. To change the sample time of an element or
bus that has a different sample time than the other nonvirtual bus input elements, use a
Rate Transition block. For details, see
Modify Sample Times for Nonvirtual Buses.

#### Dependencies

To enable this parameter, set **Output data
type** to a `Simulink.Bus` object.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NonVirtualBus` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb, NonVirtualBus="on")`

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

Actual data type or capability support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

This block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | Yes | Yes | Yes | Yes |

**Optimizations**

You can use these HDL Coder optimizations to optimize the speed, area, and
I/Os.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior.  For the Sqrt block, HDL Coder distributes pipeline registers around the blocks instead of within them. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

**HDL Modeling Guidelines**

For best practices, see:

- Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)

**Limitations and Considerations**

To learn more about using buses for HDL code generation, see Buses (HDL Coder).

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced before R2006a**

### R2025a: Specify parameter values more easily and intuitively

The Bus Creator block now provides more intuitive and streamlined editing
for block parameter values.

You can now specify Bus Creator block parameter values in the Property
Inspector. You can continue to use the Block Parameters dialog
box.

This table describes the parameter and interaction changes.

| Goal | Action Before R2025a | Action Since R2025a |
| --- | --- | --- |
| Apply changes. | Make your changes. Then, click **Apply** or **OK**. | Make your changes.  When you specify block parameter values in the Property Inspector or Block Parameters dialog box, the changes apply immediately. |
| Filter with regular expressions. | Click Show filtering options, and select **Enable regular expression**. Then, enter a search term in the **Filter by name** box. | Enter a search term in the **Filter** box. |
| Show filtered results as a flat list. | Click **Show filtered results as a flat list**. | Click Show filtered results as a flat list. |
| Find source blocks. | Select one or more inputs. Then, click **Find**.  The software highlights the source blocks. | Select one or more inputs. Then, click Select source blocks.  The software selects the source blocks, and the Property Inspector displays the parameters of the block that has focus. |
| Add block input. | Click **Add**. | Click Add. |
| Refresh the list of inputs. | Click **Refresh**. | Click Refresh. |
| Remove block input. | Click **Remove**. | Click Remove. |
| Reorder inputs. | Select one or more adjacent inputs. Then, click **Up** or **Down** until the inputs are in the desired position. | Select one or more inputs. Then, drag the inputs to the desired position. |
| Open the Type Editor to define a `Simulink.Bus` object. | Click Show data type assistant, and set **Mode** to `Bus object`. Then, click the **Edit** button. | Click Open Type Editor. |
| Specify the source of the output bus element names. | Select or clear the **Use names from inputs instead of from bus object** check box. | Set **Element names** to `From inputs` or `From output data type`. |
| Rename inputs. | Edit the signal labels of the input elements.  Alternatively, select **Require names of inputs to match names above**, select an element, and specify a new name in the **Rename selected signal** box. | Edit the signal labels of the input elements. |

### R2025a: **Require names of inputs to match names above** and **Rename selected signal** have been removed

The **Require names of inputs to match names above** and
**Rename selected signal** parameters have been removed. To
specify the required names, use a `Simulink.Bus` object
instead.

1. Set **Output
   data type** to a `Simulink.Bus` object.
2. Choose one of these options:

   - To inherit the output bus element names from the specified
     `Simulink.Bus` object, set **Element
     names** to `From output data
     type`.
   - To require the input names to match the names from the
     specified `Simulink.Bus` object, set
     **Element names** to `From
     inputs` and set the **Element name
     mismatch** configuration parameter to
     `error`. This configuration
     parameter checks that the input names match the corresponding
     names in the `Simulink.Bus` object.

Setting `Inputs` to a comma-separated list of element names is not
recommended.

For more information, see **Element
names** and **Element name mismatch**.

### R2023a: Variable-size input signal upper bound can be smaller than upper bound of variable-size signal that the corresponding Bus Creator block input port can accept

Starting in R2023a, the Bus Creator  block supports variable-size
input signals with upper bounds smaller than upper bounds of variable-size signals
that the corresponding Bus Creator block input ports can
accept.

This enhancement allows you to use variable-size input signals when the upper
bounds of input signals are not equal to the upper bounds of variable-size signals
that the corresponding Bus Creator block input ports can
accept.
