---
type: simulink-block
title: 'Goto'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'goto'
documentation_source_path: 'slref/goto.html'
language: zh-CN
chinese_source: worker-translation
---

# Goto

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

要传递给对应 From 模块的输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Goto tag
  summary: 模块标识符 A（默认）| ...
  group: ''
  block_parameter: GotoTag
  type: 字符向量
  values: '''A'' | ...'
  default: '''A'''
- name: Tag visibility
  summary: Goto 模块标签的作用域 local（默认）| scoped | global
  group: ''
  block_parameter: TagVisibility
  type: 字符向量
  values: '''local'' | ''scoped'' | ''global'''
  default: '''local'''
- name: Icon display
  summary: 在模块图标上显示的文本 Tag（默认）| Signal name | Tag and signal name
  group: ''
  block_parameter: IconDisplay
  type: 字符向量
  values: '''Signal name'' | ''Tag'' | ''Tag and signal name'''
  default: '''Tag'''
- name: Rename All
  summary: 在整个模型中传播名称 按钮
  group: ''
- name: Corresponding blocks
  summary: 连接到此 Goto 模块的模块 模块路径 | ...
  group: ''
```

### **Goto tag** — 模块标识符 `A`（默认）| ...

Goto 模块标识符。此参数标识 Goto 模块，其作用域在此模块中定义。

#### 程序化使用

|  |
| --- |
| **模块参数：** `GotoTag` |
| **类型：** 字符向量 |
| **值：** `'A'` | `...` |
| **默认值：** `'A'` |

### **Tag visibility** — Goto 模块标签的作用域 `local`（默认）| `scoped` | `global`

Goto 模块标签的作用域，指定为 `local`、`scoped` 或 `global`。当您将此参数设置为 `scoped` 时，必须使用 Goto Tag Visibility 模块来定义标签可见性的作用域。

- `local`（默认）— 使用相同标签的 From 和 Goto 模块必须位于同一子系统中。局部标签名称用方括号（`[]`）括起来。
- `scoped` — 使用相同标签的 From 和 Goto 模块必须满足以下条件之一：

  - 位于同一子系统中。
  - 位于模型中 Goto Tag Visibility 模块下方的任意层级，且不跨越非虚拟子系统边界。换句话说，它们必须位于原子子系统、条件执行子系统或函数调用子系统或模型引用的边界内。

  作用域标签名称用花括号（`{}`）括起来。
- `global` — 使用相同标签的 From 和 Goto 模块可以位于模型中的任何位置，但跨越非虚拟子系统边界的位置除外。

From-Goto 模块连接不能跨越非虚拟子系统边界的规则有以下例外。在一个条件执行子系统中连接到状态端口的 Goto 模块对另一个条件执行子系统内的 From 模块可见。

**注意**

掩码系统中的 `scoped` Goto 模块仅在该子系统及其包含的非虚拟子系统中可见。如果运行或更新框图时，Goto Tag Visibility 模块在框图中所在的层级高于掩码子系统中对应的 `scoped` Goto 模块，Simulink® 将生成错误。

当使用相同标签名称的 Goto 和 From 模块位于同一子系统中时，请使用局部标签。当使用相同标签名称的 Goto 和 From 模块位于不同子系统中时，必须使用全局或作用域标签。当您将标签定义为全局时，该标签的所有使用都访问同一信号。定义为作用域的标签可以在模型中的多个位置使用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TagVisibility` |
| **类型：** 字符向量 |
| **值：** `'local' | 'scoped' | 'global'` |
| **默认值：** `'local'` |

### **Icon display** — 在模块图标上显示的文本 `Tag`（默认）| `Signal name` | `Tag and signal name`

指定在模块图标上显示的文本。选项包括模块标签、模块所表示的信号名称，或标签和信号名称两者。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IconDisplay` |
| **类型：** 字符向量 |
| **值：** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **默认值：** `'Tag'` |

### **Rename All** — 在整个模型中传播名称 按钮

重命名 Goto 标签。新名称将传播到 **Corresponding blocks** 框中列出的所有 From 和 Goto Tag Visibility 模块。

或者，当您更改 Goto 模块图标上的标签时，按 **Shift+Enter** 将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

### **Corresponding blocks** — 连接到此 Goto 模块的模块 模块路径 | ...

连接到此 Goto 模块的 From 模块和 Goto Tag Visibility 模块的列表。单击列表中的条目以显示并高亮对应的 From 和 Goto Tag Visibility 模块。

或者，在 Simulink Editor 中，选择 Goto 模块以高亮对应的 From 和 Goto Tag Visibility 模块。

与所选 Goto 模块对应的两个 From 模块将被高亮显示。

当对应的 From 或 Goto Tag Visibility 模块不在当前框中时，包含该模块的 Subsystem 模块将被高亮显示。

要在打开的框图或新选项卡中显示对应的模块，请选择 Goto 模块并暂停在省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块对应于所选模块时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的已打开框图或新选项卡。
## 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

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

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。HDL 代码生成不支持将模块的 **Tag Visibility** 设置为 `global`。另请参阅 Required HDL Settings for Goto and From Blocks (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2024a：将信号线转换为 Goto 和 From 模块集

您可以将信号线和虚拟总线转换为连接的 Goto 和 From 模块集，也可以将 Goto 和 From 模块集转换为信号线。

有关更多信息，请参阅 Convert Signal Lines to Goto and From Blocks and Vice Versa。

## 描述

将模块输入传递给 From 模块

Goto 模块将其输入传递给对应的 From 模块。输入可以是任意数据类型的实值或复值信号或向量。From 和 Goto 模块允许您将信号从一个模块传递到另一个模块，而无需实际连接它们。

一个 Goto 模块可以将其输入信号传递给多个 From 模块，但一个 From 模块只能接收来自一个 Goto 模块的信号。该 Goto 模块的输入被传递给与其关联的 From 模块，就像这些模块在物理上连接一样。

例如，此模型使用了一个 Goto 模块和一个 From 模块。

一个 Sine Wave 模块连接到一个 Goto 模块。对应的 From 模块连接到一个 Gain 模块。

一个等效模型将 Sine Wave 模块信号直接传递给 Gain 模块。

Sine Wave 模块直接连接到 Gain 模块。

Goto 模块和 From 模块通过使用 Goto 标签进行匹配。

**Tag visibility** 参数决定 From 模块可以在何处访问该信号。

Goto 模块支持信号标签传播。有关更多信息，请参阅 Signal Label Propagation。

您可以通过用连接的 Goto 和 From 模块集替换冗长的信号线来简化模型框图。但是，当您想要追踪信号路径时，查看信号线可能会很有用。您可以将信号线和虚拟总线转换为 Goto 和 From 模块集，也可以将 Goto 和 From 模块集转换为信号线。有关更多信息，请参阅 Convert Signal Lines to Goto and From Blocks and Vice Versa。
