---
type: simulink-block
title: 'DocBlock'
family: model-wide-utilities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'docblock'
---

# DocBlock

Create text that documents model and save text with model

## 中文

创建用以说明模型的文本并随模型保存文本

### 所属库

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

### 描述

DocBlock 允许您创建和编辑用于说明模型的文本，并随模型保存文本。双击该模块的实例将创建一个包含与此模块关联的文本的临时文件并在编辑器中打开该文件。使用编辑器修改文本并保存文件。Simulink® 软件会将所保存文件的内容存储在模型文件中。

DocBlock 支持 HTML、富文本格式 (RTF) 和 ASCII 文本文档类型。这些不同文档类型的默认编辑器是

- HTML - Microsoft® Word（如果可用）。否则，DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开 HTML 文档。
- RTF - Microsoft Word（如果可用）。否则，DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开 RTF 文档。
- 文本 - DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开文本文档。

使用 `docblock` 命令更改默认编辑器。

**提示**

要编辑 DocBlock 的模块参数，请右键点击模块图标，然后选择**封装 > 封装参数...**。

### 参数

#### **代码生成模板符号** — 生成的代码的模板符号 `''` | `Abstract` | `Description` | `History` | `Modified History` | `Notes`

在此字段中输入模板符号名称。Embedded Coder® 软件使用此符号将注释添加到从模型生成的代码中。有关详细信息，请参阅 Add Global Comments in the Generated Code (Embedded Coder)。

##### 依赖关系

要使注释显示在生成的代码中，还必须将**文档类型**设置为**文本**。

##### 编程用法

|  |
| --- |
| **模块参数**：`ECoderFlag` |
| **类型：**字符向量 |
| **值：** `'Abstract'` | `'Description'` | `'History'` | `'Modified History'` | `'Notes'` |
| **默认值：**`''` |

#### **文档类型** — 文档的类型 `Text` (默认) | `RTF` | `HTML`

选择与 DocBlock 关联的文档的类型。选项包括：

- **文本**
- **RTF**
- **HTML**

##### 依赖关系

如果您在代码生成过程中使用 DocBlock 向代码添加注释，请确保将**文档类型**设置为**文本**。如果您将**文档类型**设置为 **RTF** 或 **HTML**，则您的注释不会出现在代码中。

##### 编程用法

|  |
| --- |
| **模块参数**：`DocumentType` |
| **类型：**字符向量 |
| **值**：`'Text'` | `'RTF'` | `'HTML'` |
| **默认值：**`'Text'` |

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

使用为 Embedded Coder Flag 模块参数指定的模板符号，将注释添加到生成的代码中。需要 Embedded Coder 许可证。有关详细信息，请参阅 Use a Simulink DocBlock to Add a Comment (Embedded Coder)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅Generate HDL Code with Annotations or Comments (HDL Coder)和Integrate Custom HDL Code by Using DocBlock (HDL Coder)。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **注解**（默认值） | 在生成的代码中插入文本作为注释。 |
| **HDLText** | 将文本作为自定义 HDL 代码进行集成。 |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **TargetLanguage** | 文本的语言，Verilog® 或 VHDL®。默认值为 VHDL。  当**架构**是 **HDLText** 时，此属性可用。要了解详细信息，请参阅Integrate Custom HDL Code by Using DocBlock (HDL Coder)。 |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

**限制**

- **文档类型**必须为**文本**。

  HDL Coder 不支持 **HTML** 或 **RTF** 选项。
- 在同一个子系统中，最多可以有两个 DocBlock 模块的**架构**设置为 **HDLText**。

  如果您有两个 DocBlock 模块，则必须将其中一个模块的 **TargetLanguage** 设置为 **VHDL**，将另一个模块的 **TargetLanguage** 设置为 **Verilog**。在生成代码时，HDL Coder 仅集成来自 DocBlock 且与代码生成的目标语言匹配的自定义代码。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

## Description

The DocBlock allows you to create and edit text that documents a model,
and save that text with the model. Double-clicking an instance of the block creates a
temporary file containing the text associated with this block and opens the file in an
editor. Use the editor to modify the text and save the file. Simulink® software stores the contents of the saved file in the model file.

The DocBlock supports HTML, Rich Text Format (RTF), and ASCII text
document types. The default editors for these different document types are

- HTML — Microsoft® Word (if available). Otherwise, the DocBlock opens
  HTML documents using the editor specified on the **Editor/Debugger
  Preferences** pane of the Preferences dialog box.
- RTF — Microsoft Word (if available). Otherwise, the DocBlock opens
  RTF documents using the editor specified on the **Editor/Debugger
  Preferences** pane of the Preferences dialog box.
- Text — The DocBlock opens text documents using the
  editor specified on the **Editor/Debugger Preferences** pane of
  the Preferences dialog box.

Use the `docblock` command to change the
default editors.

**Tip**

To edit the block parameters of the DocBlock, right-click the block
icon and select **Mask > Mask Parameters...**.

## Parameters

### **Code generation template symbol** — Template symbol for generated code `''` | `Abstract` | `Description` | `History` | `Modified History` | `Notes`

Enter a template symbol name in this field. Embedded Coder® software uses this symbol to add comments to the code
generated from the model. For more information, see Add Global Comments in the Generated Code (Embedded Coder).

#### Dependencies

For comments to appear in the generated code, you must also set the
**Document type** to
`Text`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ECoderFlag` |
| **Type:** character vector |
| **Values:** `'Abstract'` | `'Description'` | `'History'` | `'Modified History'` | `'Notes'` |
| **Default:** `''` |

### **Document type** — Type of document `Text` (default) | `RTF` | `HTML`

Select the type of document associated with the DocBlock.
The options are:

- `Text`
- `RTF`
- `HTML`

#### Dependencies

If you are using a DocBlock to add comments to your
code during code generation, ensure that you set the **Document
Type** as `Text`. If you set the
**Document Type** as `RTF`
or `HTML`, your comments will not appear in the
code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DocumentType` |
| **Type:** character vector |
| **Values:** `'Text'` | `'RTF'` | `'HTML'` |
| **Default:** `'Text'` |

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

Uses the template symbol you specify for the Embedded Coder Flag block parameter
to add comments to generated code. Requires an Embedded Coder license. For more information, see Use a Simulink DocBlock to Add a Comment (Embedded Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. See also Generate HDL Code with Annotations or Comments (HDL Coder) and Integrate Custom HDL Code by Using DocBlock (HDL Coder).

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Annotation` (default) | Insert text as comment in the generated code. |
| `HDLText` | Integrate text as custom HDL code. |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **TargetLanguage** | Language of the text, either Verilog® or VHDL®. The default is VHDL.  When **Architecture** is `HDLText`, this property is available. To learn more, see Integrate Custom HDL Code by Using DocBlock (HDL Coder). |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

**Restrictions**

- **Document type** must be
  `Text`.

  HDL Coder does not support the `HTML`
  or `RTF` options.
- You can have a maximum of two DocBlock blocks with
  **Architecture** set to
  `HDLText` in the same subsystem.

  If you have two DocBlock blocks, one must have
  **TargetLanguage** set to
  `VHDL`, and the other must have
  **TargetLanguage** set to
  `Verilog`. When generating code,
  HDL Coder only integrates the custom code from the
  DocBlock that matches the target language for
  code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**
