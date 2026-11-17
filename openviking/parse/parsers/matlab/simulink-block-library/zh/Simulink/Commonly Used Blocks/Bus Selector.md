---
type: simulink-block
title: 'Bus Selector'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busselector'
documentation_source_path: 'slref/busselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Bus Selector

## 端口

### 输入

### **Port\_1** — 输入虚拟或非虚拟总线 总线

输入虚拟或非虚拟总线包含要选择的元素。

对于总线数组，使用 Selector 模块选择要与 Bus Selector 模块一起使用的总线。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是
### 输出

### **Port\_1** — 输入总线的选定元素 标量 | 向量 | 矩阵 | 数组 | 总线

默认情况下，模块从单独的输出端口输出每个选定的元素，这些端口用相应的总线元素名称标记。

当选中 **Output as virtual bus** 参数时，模块从一个端口输出选定的元素，并将它们分组到一个虚拟总线中。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

默认情况下，属性检查器使用垂直布局，输出元素位于总线元素列表下方。要并排查看总线中的元素和输出元素，请单击 Change layout。

### **Elements in the bus** — 输入总线层次结构 只读：元素名称列表

此参数为只读。

总线中的元素列表提供了进入模块的元素，包括嵌套总线及其元素。元素旁边的箭头表示输入元素是总线。要显示该总线的内容，请单击箭头。

要使用或不使用正则表达式按名称筛选总线中的元素，请在 **Filter** 框中输入搜索词。不要将搜索词括在引号中。可选地，通过单击 Show filtered results as a flat list 将筛选结果显示为平面列表。平面列表使用点表示法来反映总线层次结构。默认情况下，筛选结果以层次树形式显示。

要选择进入模块的元素的源，请在列表中选择该元素。然后，单击 Select source blocks。或者，右键单击该元素。然后，选择 **Select source blocks**。属性检查器显示所选源模块的参数。当您选择多个元素的源模块时，属性检查器显示具有焦点的源模块的参数。

要刷新进入模块的元素列表，请单击 Refresh。例如，当对话框打开时更改了元素名称，请单击此按钮。

#### 提示

- 绿色复选标记图标出现在选定的输出元素旁边。
- 当您暂停在选定的输出元素上时，括号中会显示 Bus Selector 模块选择该元素的次数。
- 正则表达式允许您根据输入元素是否匹配模式进行筛选。例如，在 **Filter** 框中输入 `t$` 以显示所有名称以小写 `t` 结尾的元素。有关更多信息，请参阅正则表达式。

#### 编程使用

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InputSignals` |
| **值：** | 只读：元素名称的元胞数组 |

**示例：** `get_param(gcb,'InputSignals')`

### **Output elements** — 选定的输出元素 元素名称列表

选定元素列表提供了退出模块的元素。该列表使用每个元素的完全限定名称。

在 Simulink 编辑器中，当 **Output as virtual bus** 清除时，通过向模块添加端口来从输入总线中选择元素。

1. 单击 Bus Selector 模块的输出边缘。或者，当模块接收总线且所有输出端口都连接到其他端口时，在靠近 Bus Selector 模块输出边缘处绘制一条新线。
2. 指定要选择的元素。

在属性检查器或模块参数对话框中，通过向 **Output elements** 列表添加元素来从输入总线中选择元素。

1. 在 **Elements in the bus** 列表中，选择一个或多个要添加到模块输出的元素。

   当您从 **Elements in the bus** 列表中选择多个元素时，选择它们的顺序决定了将它们添加到 **Output elements** 列表时的顺序。
2. 可选地，在 **Output elements** 列表中，选择要在其下方添加元素的元素。当您未选择任何元素时，软件将元素添加到列表末尾。
3. 根据对话框的布局，单击 Add to output（垂直布局）或 Add to output（水平布局）。或者，右键单击其中一个选定的元素。然后，单击 **Add to output**。

要更改输出元素的顺序，请将 **Output elements** 列表中的元素拖动到不同位置。更改元素顺序时，端口连接性保持不变。

要从模块输出中删除元素，请从 **Output elements** 列表中选择要删除的元素。然后，单击 Remove。或者，右键单击其中一个选定的元素。然后，选择 **Remove**。

如果列表中的元素不在输入总线中，则该元素名称显示为红色。从选定元素列表中删除该元素，或修改输入总线以包含具有指定名称的元素。要删除所有不在输入总线中的输出元素，请右键单击红色的元素名称。然后，选择 **Remove all invalid elements**。

#### 限制

为避免递归限制，每个 Bus Selector 模块选择的元素应少于 500 个。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputSignals` |
| **值：** | `'signal1,signal2'`（默认）| 用引号括起来的逗号分隔的元素名称列表 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'OutputSignals','constant,sine')`

### **Output as virtual bus** — 将选定元素输出为虚拟总线的选项 `off`（默认）| `on`

默认情况下，模块从单独的输出端口输出每个选定的元素，这些端口用相应的总线元素名称标记。要从一个端口输出选定的元素并将它们分组到一个虚拟总线中，请选中此参数。

要将输出转换为非虚拟总线，请在 Bus Selector 模块之后插入一个 Signal Conversion 模块。将 Signal Conversion 模块的 **Output** 参数设置为 `Nonvirtual bus`，并将 **Data type** 设置为 `Simulink.Bus` 对象。

当 **Output elements** 列表仅包含一个元素且您选中此参数时，该元素不会被包装在总线中。例如，如果该元素是总线，则输出元素就是该总线。如果该元素不是总线，则输出元素也不是总线。

#### 依赖关系

要使用此参数，模块输出不得包含消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputAsBus` |
| **值：** | `'off'`（默认）| `'on'` |

**示例：** `set_param(gcb,'OutputAsBus','on')`

## 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复数信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵（最多二维） | 是 | Half  Single  Double | 是 | 是 | 是 | 是 |

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
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带有寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可以提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |

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

### R2024b：使用属性检查器指定参数

您现在可以在属性检查器中指定 Bus Selector 模块参数。当您在属性检查器或模块参数对话框中进行更改时，更改会立即应用。**Apply** 和 **OK** 按钮已被移除。

Bus Selector 模块必须至少有一个输出元素。要完全替换输出元素，请从输入总线向模块输出添加元素。然后，移除原始输出元素。例如，对于新的 Bus Selector 模块，从输入总线向模块输出添加元素。然后，右键单击名为 `signal1` 的占位符元素，并选择 **Remove all invalid elements**。

当您找到输入元素的源模块时，源模块现在会被选中而不是高亮显示。属性检查器显示所选源模块的参数。当您选择多个元素的源模块时，属性检查器显示具有焦点的源模块的参数。为反映此更改，**Highlight source blocks** 选项（）现在称为 **Select source blocks**。

### R2024a：右键单击元素以访问选项

在 Bus Selector 模块的模块参数对话框中，右键单击元素并选择所需操作。

- **Add to output** — 将输入总线中的元素添加到模块输出。
- **Highlight source blocks** — 高亮显示输入总线中元素的源模块。
- **Remove** — 从模块输出中移除元素。
- **Remove all invalid elements** — 移除所有不在输入总线中的输出元素。无效的元素名称显示为红色。

要查看元素的可用操作，请右键单击该元素。要查看多个选定元素的可用操作，请右键单击选择中的一个元素。例如，假设您的选择仅包含无效元素。当您右键单击时，会收到两个选项：**Remove** 和 **Remove all invalid elements**。如果您的选择包含有效元素，则会收到一个选项：**Remove**。

### R2024a：重命名参数和更直观的交互

当您与 Bus Selector 模块交互时，操作结果更加清晰。

- Select elements 按钮  现在是 Add to output 按钮 。
- **Selected elements** 列表现在是 **Output elements** 列表。
- Output as virtual bus 按钮  现在是 **Output as virtual bus** 复选框。

### R2023b：精简的对话框设计

Bus Selector 模块对话框具有精简的设计和附加功能。

- 在 **Elements in the bus** 列表中，绿色复选标记图标出现在选定的输出元素旁边。
- 在 **Elements in the bus** 列表中，当您暂停在选定的输出元素上时，括号中会显示 Bus Selector 模块选择该元素的次数。
- 筛选默认支持正则表达式。
- 您可以在垂直和水平布局之间切换。

以前的功能仍然保留。

默认情况下，对话框以垂直布局打开，选定元素位于总线元素列表下方。要并排查看总线中的元素和选定的输出元素，请单击 Change layout。

水平布局更接近以前的 Bus Selector 模块对话框设计。

## 描述

从输入总线中选择元素

Bus Selector 模块按名称从输入总线层次结构中提取您选择的元素。该模块可以单独输出选定的元素，也可以在新的虚拟总线中输出。当模块单独输出选定的元素时，每个选定的元素对应一个输出端口。当模块输出新的虚拟总线时，该模块有一个虚拟总线输出端口，其中包含每个选定的元素。

虽然多个元素可以在总线层次结构的不同位置具有相同的名称，但每个元素都有一个唯一的完全限定名称，Bus Selector 模块使用该名称。例如，顶层总线和嵌套总线都可以有一个名为 `chirp` 的元素。顶层总线中元素的完全限定名称为 `chirp`。嵌套总线中元素的完全限定名称为 `nestedbus.chirp`，其中 `nestedbus` 是嵌套总线的名称。

**提示**

对于子系统和模型接口处的总线，请使用 In Bus Element 模块，而不是将 Inport 模块与 Bus Selector 模块一起使用。In Bus Element 模块：

- 减少框图中的线条复杂度和杂乱。
- 允许您更轻松地增量更改接口。
- 允许在更接近使用点的地方访问总线元素，避免使用 Bus Selector 和 Goto 模块配置。
