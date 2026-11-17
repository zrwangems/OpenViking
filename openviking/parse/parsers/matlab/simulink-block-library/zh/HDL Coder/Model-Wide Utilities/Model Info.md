---
type: simulink-block
title: 'Model Info'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'modelinfo'
documentation_source_path: '../simulink/slref/modelinfo.html'
language: zh-CN
chinese_source: worker-translation
---

# Model Info

## 端口

R2025b 中未记录。

## 参数

### **Enter text and tokens to display on Model Info block** — 要在 Model Info 模块上显示的文本内容和格式 `Model Info`（默认）| text

指定要在模块封装上显示的文本和属性。编辑默认文本 `Model Info`。

要在模块封装上显示模型属性：

1. 在 **Model properties** 列表中选择一个属性。
2. 点击右箭头按钮。

   模块会将形式为 `%<modelpropertyname>` 的标记添加到框中。在模块封装显示的文本中，软件会用该属性的值替换该标记。

例如，如果在 **Model properties** 列表中选择 `Description` 并点击右箭头按钮，标记 `%<Description>` 会出现在右侧的框中。您可以在模型属性之前添加说明性文本，例如 “`Model description:`”。当您点击 **Apply** 或 **OK** 时，软件会在模块封装上显示更新后的文本和模型属性的当前值。

有关模型属性的说明，请参阅 Access Model Information Programmatically。

如果您对源代码管理信息感兴趣，为了获得与源代码管理工具的灵活接口，请使用项目。请参阅 Git in MATLAB、SVN in MATLAB 和 Use Source Control with MATLAB Projects。

### **Horizontal text alignment** — 模块封装上的水平文本对齐方式 `Center`（默认）| `Left` | `Right`

指定模块封装上文本的水平对齐位置。

### **Show block frame** — 模块封装的边框 `on`（默认）| `off`

指定是否显示模块边框，即模块封装周围的边框。

## 所属库

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Model Info 模块在代码生成期间会被忽略。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**最佳实践**

在面向 HDL 代码生成的目标模型中使用 Model Info 模块时，请考虑在输入以显示在 Model Info 模块上的文本中仅使用 ASCII 字符。如果生成的 HDL 代码中包含非 ASCII 字符，RTL 仿真和综合工具可能会无法编译该代码。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

在模型中显示模型属性和文本

Model Info 模块在模块封装上显示模型属性和关于模型的文本。使用 Model Info 模块对话框指定模块所显示文本的内容和格式。您可以选择要在模块上显示的模型属性。在模块封装上显示的文本中，软件会用模型中该属性的当前值替换属性名称。
