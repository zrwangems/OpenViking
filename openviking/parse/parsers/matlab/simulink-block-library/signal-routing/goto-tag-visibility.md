---
type: simulink-block
title: 'Goto Tag Visibility'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'gototagvisibility'
---

# Goto Tag Visibility

Define scope of Goto block tag

## 中文

定义 Goto 模块标记的作用域

### 所属库

Simulink / Signal Routing

### 描述

Goto Tag Visibility 模块定义具有 `scoped` 可见性的 Goto 模块标记的可访问性。您为 **Goto 标记**模块参数指定的值可由模型层次结构中包含 Goto Tag Visibility 模块的同一子系统中及其下层的子系统中的 From 模块进行访问。

对于**标记可见性**参数值为 `scoped` 的 Goto 模块，Goto Tag Visibility 模块是必需的。如果标记可见性为 `local` 或 `global`，则不需要 Goto Tag Visibility 模块。模块显示的标记名称括在花括号 (`{}`) 内。

**注意**

封装系统中的**限定作用域** Goto 模块仅在该子系统以及它包含的非虚拟子系统中是可见的。如果您运行或更新模块图，而有一个 Goto Tag Visibility 模块在模块图中的级别低于封装子系统中对应的**限定作用域** Goto 模块，Simulink® 将生成错误。

在 Simulink 编辑器中，选择 Goto Tag Visibility 模块以突出显示对应的 Goto 和 From 模块。当对应的 From 或 Goto 模块不在当前图中时，包含该模块的 Subsystem 模块会突出显示。

要在打开的图或新选项卡中显示对应的模块，请选择 Goto Tag Visibility 模块并在省略号上暂停。然后，从操作栏中选择**相关模块** Related Blocks button。当多个模块对应于所选模块时，将打开一个相关模块列表。您可以通过在文本框中输入搜索词来过滤相关模块列表。从列表中选择相关模块后，窗口焦点转至显示该相关模块的打开的图或新选项卡。

### 参数

#### **Goto 标记** — 其可见性由此模块的位置定义的 Goto 模块标记 `A` (默认) | ...

其可见性由此模块的位置定义的 Goto 模块标记。使用指定的标记的 From 和 Goto 模块必须在同一个子系统中，或者位于模型层次结构中 Goto Tag Visibility 模块之下且不超出非虚拟子系统边界（换言之，原子子系统、条件执行子系统、函数调用子系统或模型引用的边界）的任何级别。范围标记名称用花括号 (`{}`) 括起。

##### 提示

如果您使用多个 From 和 Goto Tag Visibility 模块引用同一 Goto 标记，您可以同时在所有这些模块中重命名该标记。使用 Goto 模块对话框中的**全部重命名**按钮。或者，当您更改 Goto 模块图标上的标记时，通过按 **Shift+Enter** 键将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

##### 编程用法

|  |
| --- |
| **模块参数**：`GotoTag` |
| **类型：**字符向量 |
| **值：**`'A'` | `...` |
| **默认值：**`'A'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Routing

## Description

The Goto Tag Visibility block defines the accessibility of
Goto block tags that have `scoped` visibility. The
value you specify for the **Goto tag** block parameter is accessible by
From blocks in the same subsystem that contains the Goto Tag
Visibility block and in subsystems below it in the model hierarchy.

A Goto Tag Visibility block is required for Goto blocks
whose **Tag Visibility** parameter value is `scoped`.
No Goto Tag Visibility block is needed if the tag visibility is either
`local` or `global`. The block shows the tag name
enclosed in braces (`{}`).

**Note**

A `scoped`
Goto block in a masked system is visible only in that subsystem and
in the nonvirtual subsystems it contains. Simulink® generates an error if you run or update a diagram that has a
Goto Tag Visibility block at a lower level in the block diagram
than the corresponding `scoped`
Goto block in the masked subsystem.

In the Simulink Editor, select the Goto Tag Visibility block to highlight
the corresponding Goto and From blocks. When a
corresponding From or Goto block is not in the current
diagram, the Subsystem block that contains the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the Goto Tag
Visibility block and pause on the ellipsis. Then, select **Related
Blocks**
Related Blocks button from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

## Parameters

### **Goto tag** — Goto block tag whose visibility is defined by the location of this block `A` (default) | ...

The Goto block tag whose visibility is defined by the
location of this block. From and Goto blocks
using the specified tag must be in the same subsystem or at any level in the
model hierarchy below the Goto Tag Visibility block that does
not entail crossing a nonvirtual subsystem boundary, in other words, the
boundary of an atomic, conditionally executed, or function-call subsystem or
a model reference. A scoped tag name is enclosed in braces
(`{}`).

#### Tips

If you use multiple From and Goto Tag
Visibility blocks to refer to the same Goto tag, you can
simultaneously rename the tag in all of the blocks. Use the
**Rename All** button in the Goto block dialog box.
Alternatively, when you change the tag on the Goto block icon,
propagate the new name to all corresponding From and
Goto Tag Visibility blocks by pressing
**Shift+Enter**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
