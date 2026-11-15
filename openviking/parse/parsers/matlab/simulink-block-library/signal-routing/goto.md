---
type: simulink-block
title: 'Goto'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'goto'
---

# Goto

Pass block input to From blocks

## 中文

将模块输入传递给 From 模块

### 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

Goto 模块将其输入传递给其对应的 From 模块。输入可以是任何数据类型的实数值或复数值信号或向量。From 和 Goto 模块允许您将信号从一个模块传递给另一个模块，而无需实际连接它们。

一个 Goto 模块可将其输入信号传递到多个 From 模块，尽管一个 From 模块只能接收来自一个 Goto 模块的信号。Goto 模块的输入传递到与它关联的 From 模块，就像两个模块进行了物理连接一样。

例如，此模型使用 Goto 模块和 From 模块。

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

等效模型将 Sine Wave 模块信号直接传递给 Gain 模块。

The Sine Wave block connects directly to the Gain block.

Goto 模块和 From 模块通过使用 Goto 标记进行匹配。

**标记可见性**参数确定 From 模块可以访问信号的位置。

Goto 模块支持信号标签传播。有关详细信息，请参阅信号标签传播。

您可以通过用多组相连的 Goto 和 From 模块替换冗长的信号线来简化模型图。但是，当您要跟踪信号路径时，查看信号线会很有用。您可以将信号线和虚拟总线转换为 Goto 和 From 模块集，并且可以将 Goto 和 From 模块集转换为信号线。有关详细信息，请参阅将信号线转换为 Goto 和 From 模块，反之亦然。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

要传递给对应的 From 模块的输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### **Goto 标记** — 模块标识符 **A** (默认) | ...

Goto 模块标识符。此参数标识定义了作用域的 Goto 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`GotoTag` |
| **类型：**字符向量 |
| **值：**`'A'` | `...` |
| **默认值：**`'A'` |

#### **标记可见性** — Goto 模块标记的作用域 **局部** (默认) | **限定作用域** | **全局**

Goto 模块标记的作用域，指定为**局部**、**限定作用域**或**全局**。当您将此参数设置为**限定作用域**时，您必须使用 Goto Tag Visibility 模块来定义标记可见性的作用域。

- **局部**（默认值）- 使用同一个标记的 From 和 Goto 模块必须在同一个子系统中。局部标记名称用方括号 (`[]`) 括起。
- **限定作用域** - 使用相同标记的 From 和 Goto 模块必须符合以下条件：

  - 在同一子系统中。
  - 在模型层次结构中位于 Goto Tag Visibility 模块之下的任何级别且不会超出非虚拟子系统边界。换句话说，它们必须在原子子系统、条件执行子系统或函数调用子系统或模型引用的边界内。

  范围标记名称用花括号 (`{}`) 括起。
- **全局** - 使用同一个标记的 From 和 Goto 模块可以在模型中的任意位置，但超出非虚拟子系统边界的位置除外。

From-Goto 模块连接不能穿过非虚拟子系统边界的规则存在以下例外情况。与一个条件执行子系统的状态端口连接的 Goto 模块，对另一个条件执行子系统中的 From 模块是可见的。

**注意**

封装系统中的**限定作用域** Goto 模块仅在该子系统以及它包含的非虚拟子系统中是可见的。如果您运行或更新模块图，而有一个 Goto Tag Visibility 模块在模块图中的级别高于封装子系统中对应的**限定作用域**Goto 模块，Simulink® 将生成错误。

当使用相同标记名称的 Goto 和 From 模块在同一个子系统中时，请使用 local 标记。当使用相同标记名称的 Goto 和 From 模块在不同的子系统中时，您必须使用 global 或 scoped 标记。如果您将某个标记定义为 global，则所有使用该标记的模块都访问同一个信号。定义为 scoped 的标记可在模型中的多个位置使用。

##### 编程用法

|  |
| --- |
| **模块参数**：`TagVisibility` |
| **类型：**字符向量 |
| **值：**`'local' | 'scoped' | 'global'` |
| **默认值：**`'local'` |

#### **图标显示** — 要在模块图标上显示的文本 **标记** (默认) | **信号名称** | **标记和信号名称**

指定要在模块图标上显示的文本。选项包括模块标记、模块所代表的信号的名称，或者同时包含标记和信号名称。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconDisplay` |
| **类型：**字符向量 |
| **值：**`'Signal name' | 'Tag' | 'Tag and signal name'` |
| **默认值：**`'Tag'` |

#### **全部重命名** — 在整个模型中传播名称 按钮

重命名 Goto 标记。新名称会传播给**对应的模块**框中列出的所有 From 和 Goto Tag Visibility 模块。

或者，当您更改 Goto 模块图标上的标记时，通过按 **Shift+Enter** 键将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

#### **对应的模块** — 连接到此 Goto 模块的模块 模块路径 | ...

与此 Goto 模块连接的 From 模块和 Goto Tag Visibility 模块的列表。点击列表中的某个项目，以显示并突出显示对应的 From 和 Goto Tag Visibility 模块。

或者，在 Simulink 编辑器中，选择 Goto 模块以突出显示对应的 From 和 Goto Tag Visibility 模块。

Two From blocks that correspond to the selected Goto block are highlighted.

当对应的 From 或 Goto Tag Visibility 模块不在当前图中时，包含该模块的 Subsystem 模块会突出显示。

要在打开的图或新选项卡中显示对应的模块，请选择 Goto 模块并在省略号上暂停。然后，从操作栏中选择**相关模块** Related Blocks button。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

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

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。HDL 代码生成不支持将模块的**标记可见性**设置为**全局**。另请参阅Required HDL Settings for Goto and From Blocks (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |

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

The Goto block passes its input to its corresponding From
blocks. The input can be a real- or complex-valued signal or vector of any data type.
From and Goto blocks allow you to pass a signal from
one block to another without actually connecting them.

A Goto block can pass its input signal to more than one From
block, although a From block can receive a signal from only one
Goto block. The input to that Goto block is passed to
the From blocks associated with it as though the blocks were physically
connected.

For example, this model uses a Goto block and a From
block.

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

An equivalent model passes the Sine Wave block signal directly to the
Gain block.

The Sine Wave block connects directly to the Gain block.

Goto blocks and From blocks are matched by the use of
Goto tags.

The **Tag
visibility** parameter determines where From blocks can
access the signal.

The Goto block supports signal label propagation. For more information, see
Signal Label Propagation.

You can simplify your model diagrams by replacing lengthy signal lines with sets of
connected Goto and From blocks. However, when you want to
trace a signal path, it can be useful to see the signal lines. You can convert signal
lines and virtual buses to Goto and From block sets, and
you can convert Goto and From block sets to signal lines.
For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal to be passed to the corresponding From
block, specified as a scalar, vector, matrix, or N-D array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Goto tag** — Block identifier `A` (default) | ...

The Goto block identifier. This parameter identifies the
Goto block whose scope is defined in this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

### **Tag visibility** — Scope of the Goto block tag `local` (default) | `scoped` | `global`

The scope of the Goto block tag, specified as
`local`, `scoped`, or
`global`. When you set this parameter to
`scoped`, you must use a Goto Tag Visibility block to
define the scope of tag visibility.

- `local` (default) — From
  and Goto blocks that use the same tag must be in the
  same subsystem. A local tag name is enclosed in brackets
  (`[]`).
- `scoped` — From and
  Goto blocks that use the same tag must be
  either:

  - In the same subsystem.
  - At any level in the model hierarchy below the Goto
    Tag Visibility block that does not entail
    crossing a nonvirtual subsystem boundary. In other words,
    they must be within the boundary of an atomic, conditionally
    executed, or function-call subsystem or a model
    reference.

  A scoped tag name is enclosed in braces
  (`{}`).
- `global` — From and
  Goto blocks using the same tag can be anywhere in
  the model except in locations that span nonvirtual subsystem
  boundaries.

The rule that From-Goto block connections
cannot cross nonvirtual subsystem boundaries has the following exception. A
Goto block connected to a state port in one conditionally
executed subsystem is visible to a From block inside another
conditionally executed subsystem.

**Note**

A `scoped`
Goto block in a masked system is visible only in that
subsystem and in the nonvirtual subsystems it contains. Simulink® generates an error if you run or update a diagram that has
a Goto Tag Visibility block at a higher level in the
block diagram than the corresponding `scoped`
Goto block in the masked subsystem.

Use local tags when the Goto and From blocks
using the same tag name reside in the same subsystem. You must use global or
scoped tags when the Goto and From blocks
using the same tag name reside in different subsystems. When you define a
tag as global, all uses of that tag access the same signal. A tag defined as
scoped can be used in more than one place in the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TagVisibility` |
| **Type:** character vector |
| **Values:** `'local' | 'scoped' | 'global'` |
| **Default:** `'local'` |

### **Icon display** — Text to display on block icon `Tag` (default) | `Signal name` | `Tag and signal name`

Specifies the text to display on the block icon. The options are the block
tag, the name of the signal that the block represents, or both the tag and
the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **Default:** `'Tag'` |

### **Rename All** — Propagate name throughout model button

Rename the Goto tag. The new name propagates to all
From and Goto Tag Visibility blocks that
are listed in the **Corresponding blocks** box.

Alternatively, when you change the tag on the Goto block icon, propagate
the new name to all corresponding From and Goto Tag
Visibility blocks by pressing
**Shift+Enter**.

### **Corresponding blocks** — Blocks connected to this Goto block block path | ...

List of the From blocks and Goto Tag Visibility blocks
connected to this Goto block. Click an entry in the list to
display and highlight the corresponding From and Goto
Tag Visibility blocks.

Alternatively, in the Simulink Editor, select the Goto block to highlight the
corresponding From and Goto Tag Visibility
blocks.

Two From blocks that correspond to the selected Goto block are highlighted.

When a corresponding From or Goto Tag Visibility block is
not in the current diagram, the Subsystem block that contains
the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the
Goto block and pause on the ellipsis. Then, select
**Related Blocks**
Related Blocks button from the action bar. When multiple blocks
correspond to the selected block, a list of related blocks opens. You can
filter the list of related blocks by entering a search term in the text box.
After you select a related block from the list, window focus goes to the
open diagram or new tab that shows the related block.

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
implementation and synthesized logic. HDL code generation does not support
**Tag Visibility** of the blocks set to
`global`. See also Required HDL Settings for Goto and From Blocks (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Convert signal lines to Goto and From block sets

You can convert signal lines and virtual buses to sets of connected
Goto and From blocks, and you can convert
Goto and From block sets to signal lines.

For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.
