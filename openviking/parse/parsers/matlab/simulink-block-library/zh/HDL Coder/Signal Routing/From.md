---
type: simulink-block
title: 'From'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'from'
documentation_source_path: '../simulink/slref/from.html'
language: zh-CN
chinese_source: worker-translation
---

# From

## 端口
```yaml
ports:
- name: Port_1
  summary: 来自连接的 Goto 模块的信号 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
```

### 输出

### **Port\_1** — 来自连接的 Goto 模块的信号 标量 | 向量 | 矩阵 | N 维数组

来自连接的 Goto 模块的信号，输出的维度和数据类型与 Goto 模块的输入相同。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Goto Tag
  summary: 将信号转发到此模块的 Goto 模块的标签 A（默认）| <More Tags...> | ...
  group: ''
  block_parameter: GotoTag
  type: 字符向量
  values: '''A'' | ...'
  default: '''A'''
- name: Update Tags
  summary: 更新可见标签列表 按钮
  group: ''
- name: Goto Source
  summary: 指向连接的 Goto 模块的路径 模块路径
  group: ''
- name: Icon Display
  summary: 在模块图标上显示的文本 Tag | Tag and signal name | Signal name
  group: ''
  block_parameter: IconDisplay
  type: 字符向量
  values: '''Signal name'' | ''Tag'' | ''Tag and signal name'''
  default: '''Tag'''
```

### **Goto Tag** — 将信号转发到此模块的 Goto 模块的标签 `A`（默认）| `<More Tags...>` | ...

指定将信号转发到此 From 模块的 Goto 模块的标签。要更改标签，请从下拉列表中选择一个新标签。

下拉列表显示 From 模块当前可见的 Goto 标签。在 Simulink® 会话中首次显示该列表时，列表末尾会出现一个标记为 `<More Tags...>` 的项。选择此项会使模块更新标签列表，以包含驻留在包含此 From 模块的模型所引用的库子系统中的 Goto 模块的标签。Simulink 软件在构建库标签列表时显示进度条。Simulink 在 Simulink 会话期间或直到您下次选择相邻的 **Update Tags** 按钮之前保存更新后的标签列表。仅当模型引用的库自上次更新列表以来发生更改时，您才需要在当前会话中再次更新标签列表。

**提示**

如果您使用多个 From 和 Goto Tag Visibility 模块来引用同一个 Goto 标签，您可以同时重命名所有模块中的该标签。为此，请使用 Goto 模块对话框中的 **Rename All** 按钮。或者，当您更改 Goto 模块图标上的标签时，按 **Shift+Enter** 将新名称传播到所有对应的 From 和 Goto Tag Visibility 模块。

要查找相关的 Goto 模块，请使用 From 模块对话框中的 **Goto Source** 超链接。

#### 编程用法

|  |
| --- |
| **模块参数：** `GotoTag` |
| **类型：** 字符向量 |
| **值：** `'A'` | `...` |
| **默认值：** `'A'` |

### **Update Tags** — 更新可见标签列表 按钮

更新此 From 模块可见的标签列表，包括驻留在包含此 From 模块的模型所引用的库中的标签。仅当模型引用的库自上次更新列表以来发生更改时，您才需要在当前会话中再次更新标签列表。

### **Goto Source** — 指向连接的 Goto 模块的路径 模块路径

连接到此 From 模块的 Goto 模块的路径。点击该路径会显示并高亮模型中的 Goto 模块。

在 Simulink 编辑器中，选择 From 模块会高亮对应的 Goto 和 Goto Tag Visibility 模块。

与所选 From 模块对应的 Goto 模块会被高亮显示。

当对应的 Goto 或 Goto Tag Visibility 模块不在当前图中时，包含该模块的 Subsystem 模块会被高亮显示。

要在打开的图或新选项卡中显示对应的模块，请选择 From 模块并将鼠标悬停在省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，会打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点会转到显示该相关模块的打开的图或新选项卡。

### **Icon Display** — 在模块图标上显示的文本 `Tag` | `Tag and signal name` | `Signal name`

指定在 From 模块图标上显示的文本。选项包括模块标签、模块所表示的信号名称，或标签和信号名称两者。

#### 编程用法

|  |
| --- |
| **模块参数：** `IconDisplay` |
| **类型：** 字符向量 |
| **值：** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **默认值：** `'Tag'` |
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

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅 Required HDL Settings for Goto and From Blocks (HDL Coder)。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

### R2024a: 将信号线转换为 Goto 和 From 模块集

您可以将信号线和虚拟总线转换为连接的 Goto 和 From 模块集，也可以将 Goto 和 From 模块集转换为信号线。

有关更多信息，请参阅 Convert Signal Lines to Goto and From Blocks and Vice Versa。

## 描述

接受来自 Goto 模块的输入

From 模块接受来自对应 Goto 模块的信号，然后将其作为输出传递。输出的数据类型与来自 Goto 模块的输入的数据类型相同。From 和 Goto 模块允许您将一个信号从一个模块传递到另一个模块，而无需实际连接它们。

例如，此模型使用了一个 Goto 模块和一个 From 模块。

一个 Sine Wave 模块连接到一个 Goto 模块。对应的 From 模块连接到一个 Gain 模块。

一个等效模型将 Sine Wave 模块信号直接传递给 Gain 模块。

Sine Wave 模块直接连接到 Gain 模块。

一个 From 模块只能从一个 Goto 模块接收其信号，尽管一个 Goto 模块可以将其信号传递给多个 From 模块。

要将 Goto 模块与 From 模块关联，请在 **Goto Tag** 参数中输入 Goto 模块标签。

Goto 模块标签的可见性决定了哪些 From 模块可以接收其信号。有关更多信息，请参阅 Goto and Goto Tag Visibility。模块会指示 Goto 模块标签的可见性：

- 局部标签名用方括号（`[]`）括起来。
- 作用域标签名用花括号（`{}`）括起来。
- 全局标签名不显示附加字符。

From 模块支持信号标签传播。有关更多信息，请参阅 Signal Label Propagation。

您可以通过将冗长的信号线替换为连接的 Goto 和 From 模块集来简化模型图。但是，当您想要追踪信号路径时，查看信号线可能会很有用。您可以将信号线和虚拟总线转换为 Goto 和 From 模块集，也可以将 Goto 和 From 模块集转换为信号线。有关更多信息，请参阅 Convert Signal Lines to Goto and From Blocks and Vice Versa。
