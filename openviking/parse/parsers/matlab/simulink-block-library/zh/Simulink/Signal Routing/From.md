---
type: simulink-block
title: 'From'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'from'
documentation_source_path: 'slref/from.html'
language: zh-CN
chinese_source: official
---

# From

## 端口

### 输出

### **Port\_1** — 来自连接的 Goto 模块的信号 标量 | 向量 | 矩阵 | N 维数组

来自连接的 Goto 模块的信号，输出信号的维度和数据类型与 Goto 模块的输入信号的维度和数据类型相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### **Goto 标记** — 将信号转发给此模块的 Goto 模块的标记。 `A` (默认) | `<More Tags...>` | ...

指定将信号转发给此 From 模块的 Goto 模块的标记。要更改该标记，请从下拉列表中选择新标记。

下拉列表显示 From 模块当前可以看到的 Goto 标记。当您第一次在 Simulink® 会话中显示此列表时，列表的末尾会出现一个标签为 `<More Tags...>` 的列表项。如果您选择此列表项，模块将更新标记列表，以包括库子系统（由包含此 From 模块的模型引用）中的 Goto 模块的标记。Simulink 软件会在生成库标记列表时显示一个进度条。Simulink 会一直保存更新的标记列表直到该 Simulink 会话结束，或者直到您再次选择旁边的**更新标记**按钮为止。仅在您上次更新标记列表后模型所引用的库又发生变化的情况下，才需要再次更新当前会话中的标记列表。

**提示**

如果您使用多个 From 和 Goto Tag Visibility 模块引用同一 Goto 标记，您可以同时在所有这些模块中重命名该标记。为此，请使用 Goto 模块对话框中的**全部重命名**按钮。或者，当您更改 Goto 模块图标上的标记时，通过按 **Shift+Enter** 键将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

要找到相关 Goto 模块，请使用 From 模块对话框中的 **Goto 源**超链接。

#### 编程用法

|  |
| --- |
| **模块参数**：`GotoTag` |
| **类型：**字符向量 |
| **值：**`'A'` | `...` |
| **默认值：**`'A'` |

### **更新标记** — 更新可见标记的列表 按钮

更新对此 From 模块可见的标记列表，包括包含此 From 模块的模型所引用的库中存在的标记。仅在您上次更新标记列表后模型所引用的库又发生变化的情况下，再次更新当前会话中的标记列表。

### **Goto 源** — 所连接的 Goto 模块的路径 模块路径

连接到此 From 模块的 Goto 模块的路径。点击该路径将在模型中显示并突出显示 Goto 模块。

在 Simulink 编辑器中，选择 From 模块会突出显示对应的 Goto 和 Goto Tag Visibility 模块。

The Goto block that corresponds to the selected From block is highlighted.

当对应的 Goto 或 Goto Tag Visibility 模块不在当前图中时，包含该模块的 Subsystem 模块会突出显示。

要在打开的图或新选项卡中显示对应的模块，请选择 From 模块并在省略号上暂停。然后，从操作栏中选择**相关模块** Related Blocks button。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

### **图标显示** — 要在模块图标上显示的文本 **标记** | **标记和信号名称** | **信号名称**

指定要在 From 模块图标上显示的文本。选项包括模块标记、模块所代表的信号的名称，或者同时包含标记和信号名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型：**字符向量 |
| **值：**`'Signal name' | 'Tag' | 'Tag and signal name'` |
| **默认值：**`'Tag'` |

## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅Required HDL Settings for Goto and From Blocks (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2024a: 将信号线转换为 Goto 和 From 模块集

您可以将信号线和虚拟总线转换为连接的 Goto 和 From 模块集，并且可以将 Goto 和 From 模块集转换为信号线。

有关详细信息，请参阅将信号线转换为 Goto 和 From 模块，反之亦然。

## 描述

接受来自 Goto 模块的输入

From 模块从对应的 Goto 模块接受信号，然后将其作为输出传递出去。输出的数据类型与来自 Goto 模块的输入的数据类型相同。From 和 Goto 模块允许您将信号从一个模块传递到另一个模块，而无需实际连接它们。

例如，此模型使用 Goto 模块和 From 模块。

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

等效模型将 Sine Wave 模块信号直接传递给 Gain 模块。

The Sine Wave block connects directly to the Gain block.

一个 From 模块只能接收来自一个 Goto 模块的信号，尽管 Goto 模块可以将其信号传递给多个 From 模块。

要将 Goto 模块与 From 模块关联，请在 **Goto 标记**参数中输入 Goto 模块标记。

Goto 模块标记的可见性决定了哪些 From 模块能够接收其信号。有关详细信息，请参阅 Goto 和 Goto Tag Visibility。模块通过以下方式指明 Goto 模块标记的可见性：

- 局部标记名称用方括号 (`[]`) 括起。
- 范围标记名称用花括号 (`{}`) 括起。
- global 标记名称不带其他任何字符。

From 模块支持信号标签传播。有关详细信息，请参阅信号标签传播。

您可以通过用多组相连的 Goto 和 From 模块替换冗长的信号线来简化模型图。但是，当您要跟踪信号路径时，查看信号线会很有用。您可以将信号线和虚拟总线转换为 Goto 和 From 模块集，并且可以将 Goto 和 From 模块集转换为信号线。有关详细信息，请参阅将信号线转换为 Goto 和 From 模块，反之亦然。
