---
type: simulink-block
title: 'Model Info'
family: model-wide-utilities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'modelinfo'
---

# Model Info

Display model properties and text in model

## 中文

显示模型属性和模型中的文本

### 所属库

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

### 描述

Model Info 模块在模块封装上显示模型属性和有关模型的文本。使用 Model Info 模块对话框可指定该模块显示的文本的内容和格式。您可以选择要在模块上显示的模型属性。在模块封装上显示的文本中，软件将属性名称替换为模型中该属性的当前值。

### 参数

#### **输入要在 Model Info 模块上显示的文本和标记** — 要显示的文本的内容和格式 `Model Info` (默认) | 文本

指定要在模块封装上显示的文本和属性。编辑默认文本 `Model Info`。

要在模块封装上显示模型属性，请执行以下操作：

1. 在**模型属性**列表中选择一个属性。
2. 点击向右箭头按钮。

   模块会将一个 `%<modelpropertyname>` 形式的标记添加到框中。在模块封装显示的文本中，软件会将该标记替换为属性的值。

例如，如果您在**模型属性**列表中选择 `Description` 并点击向右箭头按钮，标记 `%<Description>` 将出现在右侧的框中。您可以在模型属性前添加说明性文本，例如 `Model description:`。当您点击**应用**或**确定**时，软件会在模块封装上显示更新后的文本和模型属性的当前值。

有关模型属性的说明，请参阅以编程方式访问模型信息。

如果您对源代码管理信息感兴趣，要通过灵活的界面访问源代码管理工具，请使用工程。请参阅MATLAB 中的 Git、MATLAB 中的 SVN和对工程使用源代码管理。

#### **水平文本对齐** — 模块封装上的水平文本对齐 **居中** (默认) | **左侧** | **右侧**

指定文本在模块封装上水平对齐的位置。

#### **显示模块边框** — 模块封装的边框 `on` (默认) | `off`

指定是否显示模块边框，模块边框是模块封装周围的边框。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

代码生成期间忽略 Model Info 模块。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**最佳做法**

如果在针对 HDL 代码生成的模型中使用 Model Info 模块，则在输入要显示在 Model Info 模块上的文本时，建议您仅使用 ASCII 字符。如果生成的 HDL 代码中有非 ASCII 字符，RTL 仿真和综合工具可能无法编译代码。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

## Description

The Model Info block displays model properties and text about a model on the
mask of the block. Use the Model Info block dialog box to specify the
content and format of the text that the block displays. You can select model properties
to display on the block. In the text displayed on the block mask, the software replaces
the property name with the current value of the property in the model.

## Parameters

### **Enter text and tokens to display on Model Info block** — Content and format of the text to display `Model Info` (default) | text

Specify the text and properties to display on the block mask. Edit the
default text `Model Info`.

To display a model property on the block mask:

1. Select a property in the **Model properties**
   list.
2. Click the right arrow button.

   The block adds a token of the form
   `%<modelpropertyname>` to the box. In
   the text the block mask displays, the software replaces the
   token with the value of the property.

For example, if you select `Description` in the
**Model properties** list and click the right arrow
button, the token `%<Description>` appears in the box
to the right. You can add explanatory text before the model property, for
example, “`Model description:`”. When you
click **Apply** or **OK**, the
software displays the updated text and the current value of the model
property on the block mask.

For descriptions of the model properties, see Access Model Information Programmatically.

If you are interested in source control information, for a flexible interface to source
control tools, use a project. See Git in MATLAB,
SVN in MATLAB,
and Use Source Control with MATLAB Projects.

### **Horizontal text alignment** — Horizontal text alignment on block mask `Center` (default) | `Left` | `Right`

Specify where to align the text on the block mask horizontally.

### **Show block frame** — Frame for block mask `on` (default) | `off`

Specify whether to display the block frame, which is a border around the
block mask.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Model Info block is ignored during code generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**Best Practices**

When using Model Info blocks in models targeted for HDL code
generation, consider using only ASCII characters in the text that you enter to
display on the Model Info block. If you have non-ASCII characters
in the generated HDL code, RTL simulation and synthesis tools can fail to
compile the code.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**
