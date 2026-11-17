---
type: simulink-block
title: 'Bus Creator'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'buscreator'
documentation_source_path: '../simulink/slref/buscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Bus Creator

## 端口
```yaml
ports:
- name: Port_1
  summary: 要包含在总线中的输入元素 标量 | 向量 | 矩阵 | 数组 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
- name: Port_1
  summary: 输出虚拟或非虚拟总线 标量 | 总线
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
```

### 输入

### **Port\_1** — 要包含在总线中的输入元素 标量 | 向量 | 矩阵 | 数组 | 总线

输入端口接受要包含在总线中的元素。输入端口数量由 **Number of inputs** 参数决定。

每个 Bus Creator 模块支持以下输入元素组合：

- 仅信号
- 信号和信号总线
- 仅消息
- 消息和总线
- 仅总线

您可以指定可变大小输入信号，其上界小于对应 Bus Creator 模块输入端口可接受的可变大小信号的上界。要配置 Bus Creator 模块输入端口可接受的可变大小信号的上界，请使用 `Simulink.BusElement` 对象。有关详细信息，请参阅 `Simulink.BusElement`。可变大小输入信号必须与对应 Bus Creator 模块输入端口配置为接受的可变大小信号具有相同的维度。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是
### 输出

### **Port\_1** — 输出虚拟或非虚拟总线 标量 | 总线

输出总线由输入元素组成。

**Output as nonvirtual bus** 参数指定输出总线是虚拟总线还是非虚拟总线。软件将虚拟总线视为其组成元素，将非虚拟总线视为标量。

有关总线类型的详细信息，请参阅 Composite Interface Guidelines。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 模块输入数量 2（默认）| 整数
  group: ''
  block_parameter: Inputs
  values: '''2''（默认）| 带引号的整数'
- name: Inputs
  summary: 模块输入 元素名称列表
  group: ''
- name: Output data type
  summary: '输出总线的数据类型 Inherit: auto（默认）| Bus: <object name>'
  group: ''
  block_parameter: OutDataTypeStr
  values: '"Inherit: auto"（默认）| "Bus: <object name>"'
- name: Element names
  summary: 输出总线元素名称的来源 From inputs（默认）| From output data type
  group: ''
  block_parameter: InheritFromInputs
  values: '"on"（默认）| "off"'
- name: Output as nonvirtual bus
  summary: 输出非虚拟总线的选项 off（默认）| on
  group: ''
  block_parameter: NonVirtualBus
  values: '"off"（默认）| "on"'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Number of inputs** — 模块输入数量 `2`（默认）| 整数

要创建总线，模块输入数量必须是大于或等于 2 的整数。

增加输入数量会向模块添加未连接的输入端口。在仿真模型之前，请确保每个输入端口都连接了输入。

如果每个输入端口都已连接，您可以通过将另一条线连接到 Bus Creator 模块来添加输入端口。

将一条线拖到具有两个已连接端口的 Bus Creator 模块附近时，会出现第三个端口。

以交互方式添加端口会更新 **Number of inputs** 参数值，并将新输入添加到 **Inputs** 列表中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

将输入数量指定为大于或等于 2 的整数。

|  |  |
| --- | --- |
| **参数：** | `Inputs` |
| **值：** | `'2'`（默认）| 带引号的整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,
Inputs="3")`

### **Inputs** — 模块输入 元素名称列表

**Inputs** 列表提供进入模块的元素，包括嵌套总线的元素。元素旁边的箭头表示输入是总线。要显示该总线的内容，请单击箭头。

要重新排列输入元素，请从 **Inputs** 列表中选择一个或多个顶层元素。然后，将元素拖动到新位置。

要添加或删除输入元素，请分别单击 Add 或 Remove。在仿真模型之前，请确保每个输入端口都已连接。

要刷新输入元素列表，请单击 Refresh。例如，在以下情况下刷新输入元素列表：

- 在对话框打开时重命名输入元素。
- 添加、删除或重新排列未命名输入元素。Bus Creator 模块将这些元素命名为 `signalN`，其中 *N* 是对应模块端口的编号。当对应模块端口发生变化时，自动生成的名称也会改变。

要使用或不使用正则表达式按名称筛选输入元素，请在 **Filter** 框中输入搜索词。不要将搜索词括在引号中。可选地，通过单击 Show filtered results as a flat list 将筛选结果显示为平面列表。平面列表使用点表示法来反映总线层次结构。默认情况下，筛选结果以层次树形式显示。

*在 R2025a 之前：要使用正则表达式进行筛选，请单击 Show filtering options。然后，选择 **Enable regular expression**。*

要选择进入模块的元素的源，请在列表中选择该元素。然后，单击 Select source blocks。属性检查器显示所选源模块的参数。当您选择多个元素的源模块时，属性检查器显示具有焦点的源模块的参数。

您无法撤销或重做对 **Inputs** 列表的更改。

#### 提示

- 当您将 **Output data type** 设置为 `Simulink.Bus` 对象时，要显示哪个 `Simulink.BusElement` 对象映射到顶层输入，请将鼠标悬停在顶层输入上。括号中会显示从输入到 `Simulink.BusElement` 对象的映射，例如 `Input1 → BusElementObject1`。
- 正则表达式允许您根据输入元素是否匹配某个模式来进行筛选。例如，要显示所有名称以小写字母 `t` 结尾的元素，请在 **Filter** 框中输入 `t$`。有关详细信息，请参阅 Regular Expressions。

### **Output data type** — 输出总线的数据类型 `Inherit: auto`（默认）| `Bus: <object name>`

指定输出总线的数据类型。

如果选择 `Bus: <object name>`，请将 `<object name>` 替换为 `Simulink.Bus` 对象的名称。在编辑模型时，该总线对象必须可访问。

#### 提示

- 要使用类型编辑器创建 `Simulink.Bus` 对象，请单击 Open Type Editor。
- 要从输出总线创建 `Simulink.Bus` 对象，请使用 `Simulink.Bus.createObject` 函数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"`（默认）| `"Bus: <object name>"` |

**示例：** `set_param(gcb, OutDataTypeStr="Bus: control")`

### **Element names** — 输出总线元素名称的来源 `From inputs`（默认）| `From output data type`

默认情况下，Bus Creator 模块使用模块输入的名称作为输出总线元素的名称，即使您将 `Simulink.Bus` 对象指定为数据类型也是如此。

- `From inputs` — 从模块输入继承输出总线元素的名称。

  *在 R2025a 之前：选择 **Use names from inputs instead of from bus object**。*
- `From output data type` — 从指定的总线对象继承输出总线元素的名称。

  *在 R2025a 之前：清除 **Use names from inputs instead of from bus object**。*

将 **Element names** 设置为 `From output data type`：

- 强制实施强数据类型。
- 避免多次输入元素名称：在总线对象中和在模型中。多次输入名称可能会导致意外的元素名称不匹配。
- 支持总线数组要求在数组元素之间具有一致的元素名称。

当您将 **Element names** 设置为 `From inputs` 时，请考虑将 **Element name mismatch** 配置参数设置为 `error`。此配置参数检查输入元素名称是否与总线对象中的对应名称匹配。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Simulink.Bus` 对象。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InheritFromInputs` |
| **值：** | `"on"`（默认）| `"off"` |

**示例：** `set_param(gcb,
InheritFromInputs="off")`

此表将此参数的交互值映射到等效的编程值。

| **Element names** 值 | `InheritFromInputs` 值 |
| --- | --- |
| `From inputs`（默认） | `"on"`（默认） |
| `From output data type` | `"off"` |

### **Output as nonvirtual bus** — 输出非虚拟总线的选项 `off`（默认）| `on`

选择此参数以输出非虚拟总线。

非虚拟总线类似于 C 代码中的结构体。选择此参数以：

- 构造总线数组。
- 使总线数据跨越 MATLAB Function 模块或 Stateflow® 图边界。
- 在生成的 C 代码中将总线数据打包为结构体。
- 通过 S-function 与外部代码接口。
- 减少生成代码中传递给子组件的函数参数数量。

非虚拟总线中的所有元素必须具有相同的采样时间，即使关联的 `Simulink.Bus` 对象为某些元素指定了继承采样时间。任何导致非虚拟总线包含具有不同采样率的元素的操作都会生成错误。要更改与其他非虚拟总线输入元素具有不同采样时间的元素或总线的采样时间，请使用 Rate Transition 模块。有关详细信息，请参阅 Modify Sample Times for Nonvirtual Buses。

#### 依赖关系

要启用此参数，请将 **Output data type** 设置为 `Simulink.Bus` 对象。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NonVirtualBus` |
| **值：** | `"off"`（默认）| `"on"` |

**示例：** `set_param(gcb, NonVirtualBus="on")`
## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

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

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

此模块支持以下用于 HDL 代码生成的数据类型：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最多二维） | 是 | Half  Single  Double | 是 | 是 | 是 | 是 |

**优化**

您可以使用这些 HDL Coder 优化来优化速度、面积和 I/O。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效的资源并将其替换为单个资源。 |
| Streaming (HDL Coder) | *流式处理*是一种面积优化，HDL Coder 在其中将向量数据路径转换为标量数据路径（或转换为若干较小尺寸的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它在设计中移动现有延迟以减少关键路径，同时保持功能行为。对于 Sqrt 模块，HDL Coder 将流水线寄存器分布在模块周围而不是模块内部。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带有寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中可能的关键路径，请使用*关键路径估计*。关键路径估计加速了查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**HDL 建模指南**

有关最佳实践，请参阅：

- 使用总线提高模型可读性并生成 HDL 代码（HDL Coder）

**限制和注意事项**

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 之前引入**

### R2025a: 更轻松、更直观地指定参数值

Bus Creator 模块现在为模块参数值提供更直观、更简化的编辑方式。

现在可以在 Property Inspector 中指定 Bus Creator 模块参数值。你可以继续使用 Block Parameters 对话框。

下表描述了参数和交互方式的变化。

| 目标 | R2025a 之前的操作 | R2025a 之后的动作 |
| --- | --- | --- |
| 应用更改。 | 进行更改。然后，点击 **Apply** 或 **OK**。 | 进行更改。当你在 Property Inspector 或 Block Parameters 对话框中指定模块参数值时，更改会立即应用。 |
| 使用正则表达式过滤。 | 点击 Show filtering options，然后选择 **Enable regular expression**。然后，在 **Filter by name** 框中输入搜索词。 | 在 **Filter** 框中输入搜索词。 |
| 将过滤结果以平面列表显示。 | 点击 **Show filtered results as a flat list**。 | 点击 Show filtered results as a flat list。 |
| 查找源模块。 | 选择一个或多个输入。然后，点击 **Find**。软件会高亮显示源模块。 | 选择一个或多个输入。然后，点击 Select source blocks。软件会选择源模块，并且 Property Inspector 会显示具有焦点的模块的参数。 |
| 添加模块输入。 | 点击 **Add**。 | 点击 Add。 |
| 刷新输入列表。 | 点击 **Refresh**。 | 点击 Refresh。 |
| 删除模块输入。 | 点击 **Remove**。 | 点击 Remove。 |
| 重新排序输入。 | 选择一个或多个相邻输入。然后，点击 **Up** 或 **Down**，直到输入位于所需位置。 | 选择一个或多个输入。然后，将输入拖动到所需位置。 |
| 打开 Type Editor 以定义 `Simulink.Bus` 对象。 | 点击 Show data type assistant，并将 **Mode** 设置为 `Bus object`。然后，点击 **Edit** 按钮。 | 点击 Open Type Editor。 |
| 指定输出总线元素名称的来源。 | 选中或清除 **Use names from inputs instead of from bus object** 复选框。 | 将 **Element names** 设置为 `From inputs` 或 `From output data type`。 |
| 重命名输入。 | 编辑输入元素的信号标签。或者，选择 **Require names of inputs to match names above**，选择一个元素，然后在 **Rename selected signal** 框中指定新名称。 | 编辑输入元素的信号标签。 |

### R2025a: **Require names of inputs to match names above** 和 **Rename selected signal** 已被移除

**Require names of inputs to match names above** 和 **Rename selected signal** 参数已被移除。要指定所需名称，请改用 `Simulink.Bus` 对象。

1. 将 **Output data type** 设置为 `Simulink.Bus` 对象。
2. 选择以下选项之一：

   - 要从指定的 `Simulink.Bus` 对象继承输出总线元素名称，请将 **Element names** 设置为 `From output data type`。
   - 要要求输入名称与指定的 `Simulink.Bus` 对象中的名称匹配，请将 **Element names** 设置为 `From inputs`，并将 **Element name mismatch** 配置参数设置为 `error`。此配置参数会检查输入名称是否与 `Simulink.Bus` 对象中的对应名称匹配。

不建议将 `Inputs` 设置为以逗号分隔的元素名称列表。

有关详细信息，请参阅 **Element names** 和 **Element name mismatch**。

### R2023a: 可变大小输入信号上界可以小于对应 Bus Creator 模块输入端口可接受的可变大小信号上界

从 R2023a 开始，Bus Creator 模块支持可变大小输入信号，其上界小于对应 Bus Creator 模块输入端口可接受的可变大小信号上界。

此增强允许你在输入信号的上界不等于对应 Bus Creator 模块输入端口可接受的可变大小信号上界时使用可变大小输入信号。

## 描述

将输入信号、总线或消息组合为总线

Bus Creator 模块将输入信号、总线或消息组合为一条总线，同时保留信号、嵌套总线和消息的各自标识。默认情况下，Bus Creator 模块会创建*虚拟总线*，它类似于用扎带捆在一起的一束导线。或者，该模块可以创建*非虚拟总线*，它类似于 C 代码中的结构体。

总线元素必须具有唯一名称。默认情况下，总线的每个元素都会继承连接到 Bus Creator 模块的元素的名称。如果存在重复名称，Bus Creator 模块会将端口号追加到所有输入元素名称。对于没有名称的元素，Bus Creator 模块会生成 `signaln` 形式的名称，其中 `n` 是连接到该元素的端口号。当你搜索元素的源或选择元素以连接到其他模块时，可以按名称引用元素。有关元素命名指南，请参阅 Signal Names and Labels。

要按名称从总线中提取元素，请使用 Bus Selector 模块。

要创建包含其他总线的总线，请将其他总线连接到 Bus Creator 模块输入端口。

**提示**

对于子系统或模型接口处的总线，请使用 Out Bus Element 模块，而不是将 Bus Creator 模块与 Outport 模块一起使用。Out Bus Element 模块：

- 减少框图中的线条复杂度和杂乱。
- 允许你更轻松地以增量方式更改接口。
