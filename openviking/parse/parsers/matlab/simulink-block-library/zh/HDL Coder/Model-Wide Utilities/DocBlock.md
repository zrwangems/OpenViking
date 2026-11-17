---
type: simulink-block
title: 'DocBlock'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'docblock'
documentation_source_path: '../simulink/slref/docblock.html'
language: zh-CN
chinese_source: worker-translation
---

# DocBlock

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Code generation template symbol
  summary: 生成代码的模板符号 '' | Abstract | Description | History | Modified History | Notes
  group: ''
  block_parameter: ECoderFlag
  type: 字符向量
  values: '''Abstract'' | ''Description'' | ''History'' | ''Modified History'' | ''Notes'''
  default: ''''''
- name: Document type
  summary: 文档类型 Text（默认）| RTF | HTML
  group: ''
  block_parameter: DocumentType
  type: 字符向量
  values: '''Text'' | ''RTF'' | ''HTML'''
  default: '''Text'''
```

### **Code generation template symbol** — 生成代码的模板符号 `''` | `Abstract` | `Description` | `History` | `Modified History` | `Notes`

在此字段中输入模板符号名称。Embedded Coder® 软件使用此符号向从模型生成的代码添加注释。有关详细信息，请参阅 Add Global Comments in the Generated Code (Embedded Coder)。

#### 依赖关系

要使注释出现在生成的代码中，还必须将 **Document type** 设置为 `Text`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ECoderFlag` |
| **类型：** 字符向量 |
| **值：** `'Abstract'` | `'Description'` | `'History'` | `'Modified History'` | `'Notes'` |
| **默认值：** `''` |

### **Document type** — 文档类型 `Text`（默认）| `RTF` | `HTML`

选择与 DocBlock 关联的文档类型。选项包括：

- `Text`
- `RTF`
- `HTML`

#### 依赖关系

如果在代码生成期间使用 DocBlock 向代码添加注释，请确保将 **Document Type** 设置为 `Text`。如果将 **Document Type** 设置为 `RTF` 或 `HTML`，注释将不会出现在代码中。

#### 编程用法

|  |
| --- |
| **模块参数：** `DocumentType` |
| **类型：** 字符向量 |
| **值：** `'Text'` | `'RTF'` | `'HTML'` |
| **默认值：** `'Text'` |
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

使用为 Embedded Coder Flag 模块参数指定的模板符号向生成的代码添加注释。需要 Embedded Coder 许可证。有关详细信息，请参阅 Use a Simulink DocBlock to Add a Comment (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅 Generate HDL Code with Annotations or Comments (HDL Coder) 和 Integrate Custom HDL Code by Using DocBlock (HDL Coder)。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Annotation`（默认） | 将文本作为注释插入生成的代码中。 |
| `HDLText` | 将文本作为自定义 HDL 代码集成。 |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **TargetLanguage** | 文本的语言，可以是 Verilog® 或 VHDL®。默认值为 VHDL。当 **Architecture** 为 `HDLText` 时，此属性可用。要了解更多信息，请参阅 Integrate Custom HDL Code by Using DocBlock (HDL Coder)。 |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，表示未连接逻辑不会保留在 HDL 代码中。有关详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

**限制**

- **Document type** 必须为 `Text`。

  HDL Coder 不支持 `HTML` 或 `RTF` 选项。
- 在同一子系统中，最多可以有两个 **Architecture** 设置为 `HDLText` 的 DocBlock 模块。

  如果有两个 DocBlock 模块，一个必须将 **TargetLanguage** 设置为 `VHDL`，另一个必须将 **TargetLanguage** 设置为 `Verilog`。生成代码时，HDL Coder 仅集成与代码生成目标语言匹配的 DocBlock 中的自定义代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

创建用于记录模型的文本并将文本与模型一起保存

DocBlock 允许您创建和编辑用于记录模型的文本，并将该文本与模型一起保存。双击该模块的实例会创建一个包含与该模块关联的文本的临时文件，并在编辑器中打开该文件。使用编辑器修改文本并保存文件。Simulink® 软件将保存文件的内容存储在模型文件中。

DocBlock 支持 HTML、富文本格式 (RTF) 和 ASCII 文本文档类型。这些不同文档类型的默认编辑器为

- HTML — Microsoft® Word（如果可用）。否则，DocBlock 使用在首选项对话框的 **Editor/Debugger Preferences** 窗格中指定的编辑器打开 HTML 文档。
- RTF — Microsoft Word（如果可用）。否则，DocBlock 使用在首选项对话框的 **Editor/Debugger Preferences** 窗格中指定的编辑器打开 RTF 文档。
- Text — DocBlock 使用在首选项对话框的 **Editor/Debugger Preferences** 窗格中指定的编辑器打开文本文档。

使用 `docblock` 命令更改默认编辑器。

**提示**

要编辑 DocBlock 的模块参数，请右键单击模块图标并选择 **Mask > Mask Parameters...**。
