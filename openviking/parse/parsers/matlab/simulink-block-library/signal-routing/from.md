---
type: simulink-block
title: 'From'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'from'
---

# From

Accept input from Goto block

## 中文

接受来自 Goto 模块的输入

### 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

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

### 端口

#### 输出

#### **Port\_1** — 来自连接的 Goto 模块的信号 标量 | 向量 | 矩阵 | N 维数组

来自连接的 Goto 模块的信号，输出信号的维度和数据类型与 Goto 模块的输入信号的维度和数据类型相同。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### **Goto 标记** — 将信号转发给此模块的 Goto 模块的标记。 `A` (默认) | `<More Tags...>` | ...

指定将信号转发给此 From 模块的 Goto 模块的标记。要更改该标记，请从下拉列表中选择新标记。

下拉列表显示 From 模块当前可以看到的 Goto 标记。当您第一次在 Simulink® 会话中显示此列表时，列表的末尾会出现一个标签为 `<More Tags...>` 的列表项。如果您选择此列表项，模块将更新标记列表，以包括库子系统（由包含此 From 模块的模型引用）中的 Goto 模块的标记。Simulink 软件会在生成库标记列表时显示一个进度条。Simulink 会一直保存更新的标记列表直到该 Simulink 会话结束，或者直到您再次选择旁边的**更新标记**按钮为止。仅在您上次更新标记列表后模型所引用的库又发生变化的情况下，才需要再次更新当前会话中的标记列表。

**提示**

如果您使用多个 From 和 Goto Tag Visibility 模块引用同一 Goto 标记，您可以同时在所有这些模块中重命名该标记。为此，请使用 Goto 模块对话框中的**全部重命名**按钮。或者，当您更改 Goto 模块图标上的标记时，通过按 **Shift+Enter** 键将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

要找到相关 Goto 模块，请使用 From 模块对话框中的 **Goto 源**超链接。

##### 编程用法

|  |
| --- |
| **模块参数**：`GotoTag` |
| **类型：**字符向量 |
| **值：**`'A'` | `...` |
| **默认值：**`'A'` |

#### **更新标记** — 更新可见标记的列表 按钮

更新对此 From 模块可见的标记列表，包括包含此 From 模块的模型所引用的库中存在的标记。仅在您上次更新标记列表后模型所引用的库又发生变化的情况下，再次更新当前会话中的标记列表。

#### **Goto 源** — 所连接的 Goto 模块的路径 模块路径

连接到此 From 模块的 Goto 模块的路径。点击该路径将在模型中显示并突出显示 Goto 模块。

在 Simulink 编辑器中，选择 From 模块会突出显示对应的 Goto 和 Goto Tag Visibility 模块。

The Goto block that corresponds to the selected From block is highlighted.

当对应的 Goto 或 Goto Tag Visibility 模块不在当前图中时，包含该模块的 Subsystem 模块会突出显示。

要在打开的图或新选项卡中显示对应的模块，请选择 From 模块并在省略号上暂停。然后，从操作栏中选择**相关模块** Related Blocks button。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

#### **图标显示** — 要在模块图标上显示的文本 **标记** | **标记和信号名称** | **信号名称**

指定要在 From 模块图标上显示的文本。选项包括模块标记、模块所代表的信号的名称，或者同时包含标记和信号名称。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型：**字符向量 |
| **值：**`'Signal name' | 'Tag' | 'Tag and signal name'` |
| **默认值：**`'Tag'` |

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

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅Required HDL Settings for Goto and From Blocks (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: 将信号线转换为 Goto 和 From 模块集

您可以将信号线和虚拟总线转换为连接的 Goto 和 From 模块集，并且可以将 Goto 和 From 模块集转换为信号线。

有关详细信息，请参阅将信号线转换为 Goto 和 From 模块，反之亦然。

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The From block accepts a signal from a corresponding Goto
block, then passes it as output. The data type of the output is the same as that of the
input from the Goto block. From and Goto
blocks allow you to pass a signal from one block to another without actually connecting
them.

For example, this model uses a Goto block and a From
block.

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

An equivalent model passes the Sine Wave block signal directly to the
Gain block.

The Sine Wave block connects directly to the Gain block.

A From block can receive its signal from only one Goto
block, although a Goto block can pass its signal to more than one
From block.

To associate a Goto block with a From block, enter the
Goto block tag in the **Goto Tag**
parameter.

The visibility of a Goto block tag determines the From blocks
that can receive its signal. For more information, see Goto and Goto Tag Visibility. The block indicates
the visibility of the Goto block tag:

- A local tag name is enclosed in brackets (`[]`).
- A scoped tag name is enclosed in braces (`{}`).
- A global tag name appears without additional characters.

The From block supports signal label propagation. For more information, see
Signal Label Propagation.

You can simplify your model diagrams by replacing lengthy signal lines with sets of
connected Goto and From blocks. However, when you want to
trace a signal path, it can be useful to see the signal lines. You can convert signal
lines and virtual buses to Goto and From block sets, and
you can convert Goto and From block sets to signal lines.
For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.

## Ports

### Output

### **Port\_1** — Signal from connected Goto block scalar | vector | matrix | N-D array

Signal from connected Goto block, output with the same
dimensions and data type as the input to the Goto
block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Goto Tag** — Tag of the Goto block that forwards its signal to this block `A` (default) | `<More Tags...>` | ...

Specify the tag of the Goto block that forwards its signal
to this From block. To change the tag, select a new tag from
the drop-down list.

The drop-down list displays the Goto tags that the From
block can currently see. An item labeled `<More
Tags...>` appears at the end of the list the first time you
display the list in a Simulink® session. Selecting this item causes the block to update the
tags list to include the tags of Goto blocks residing in
library subsystems referenced by the model containing this
From block. Simulink software displays a progress bar while building the list of
library tags. Simulink saves the updated tags list for the duration of the
Simulink session or until the next time you select the adjacent
**Update Tags** button. You need to update the tags
list again in the current session only if the libraries referenced by the
model have changed since the last time you updated the list.

**Tip**

If you use multiple From and Goto Tag Visibility blocks to
refer to the same Goto tag, you can simultaneously rename the tag in all
of the blocks. To do so, use the **Rename All** button
in the Goto block dialog box. Alternatively, when you
change the tag on the Goto block icon,
propagate the new name to all corresponding From and
Goto Tag Visibility blocks by pressing
**Shift+Enter**.

To find the relevant Goto block, use the **Goto
Source** hyperlink in the From block dialog
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

### **Update Tags** — Update list of visible tags button

Updates the list of tags visible to this From block,
including tags residing in libraries referenced by the model containing this
From block. Update the tags list again in the current
session only if the libraries referenced by the model have changed since the
last time you updated the list.

### **Goto Source** — Path to connected Goto block block path

Path of the Goto block connected to this
From block. Clicking the path displays and highlights the
Goto block in your model.

In the Simulink Editor, selecting the From block highlights the
corresponding Goto and Goto Tag Visibility
blocks.

The Goto block that corresponds to the selected From block is highlighted.

When a corresponding Goto or Goto Tag
Visibility block is not in the current diagram, the
Subsystem block that contains the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the
From block and pause on the ellipsis. Then, select
**Related Blocks**
Related Blocks button from the action bar. When multiple blocks
correspond to the selected block, a list of related blocks opens. You can
filter the list of related blocks by entering a search term in the text box.
After you select a related block from the list, window focus goes to the
open diagram or new tab that shows the related block.

### **Icon Display** — Text to display on block icon `Tag` | `Tag and signal name` | `Signal name`

Specifies the text to display on the From block icon. The
options are the block tag, the name of the signal that the block represents,
or both the tag and the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **Default:** `'Tag'` |

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

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. See also Required HDL Settings for Goto and From Blocks (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Convert signal lines to Goto and From block sets

You can convert signal lines and virtual buses to sets of connected
Goto and From blocks, and you can convert
Goto and From block sets to signal lines.

For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.
