---
type: simulink-block
title: 'DocBlock'
family: model-wide-utilities
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'docblock'
language: zh-CN
chinese_source: official
---

# DocBlock

创建用以说明模型的文本并随模型保存文本

## 所属库

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

## 描述

DocBlock 允许您创建和编辑用于说明模型的文本，并随模型保存文本。双击该模块的实例将创建一个包含与此模块关联的文本的临时文件并在编辑器中打开该文件。使用编辑器修改文本并保存文件。Simulink® 软件会将所保存文件的内容存储在模型文件中。

DocBlock 支持 HTML、富文本格式 (RTF) 和 ASCII 文本文档类型。这些不同文档类型的默认编辑器是

- HTML - Microsoft® Word（如果可用）。否则，DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开 HTML 文档。
- RTF - Microsoft Word（如果可用）。否则，DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开 RTF 文档。
- 文本 - DocBlock 将使用“预设项”对话框的**编辑器/调试器预设项**窗格中指定的编辑器打开文本文档。

使用 `docblock` 命令更改默认编辑器。

**提示**

要编辑 DocBlock 的模块参数，请右键点击模块图标，然后选择**封装 > 封装参数...**。

## 参数

### **代码生成模板符号** — 生成的代码的模板符号 `''` | `Abstract` | `Description` | `History` | `Modified History` | `Notes`

在此字段中输入模板符号名称。Embedded Coder® 软件使用此符号将注释添加到从模型生成的代码中。有关详细信息，请参阅 Add Global Comments in the Generated Code (Embedded Coder)。

#### 依赖关系

要使注释显示在生成的代码中，还必须将**文档类型**设置为**文本**。

#### 编程用法

|  |
| --- |
| **模块参数**：`ECoderFlag` |
| **类型：**字符向量 |
| **值：** `'Abstract'` | `'Description'` | `'History'` | `'Modified History'` | `'Notes'` |
| **默认值：**`''` |

### **文档类型** — 文档的类型 `Text` (默认) | `RTF` | `HTML`

选择与 DocBlock 关联的文档的类型。选项包括：

- **文本**
- **RTF**
- **HTML**

#### 依赖关系

如果您在代码生成过程中使用 DocBlock 向代码添加注释，请确保将**文档类型**设置为**文本**。如果您将**文档类型**设置为 **RTF** 或 **HTML**，则您的注释不会出现在代码中。

#### 编程用法

|  |
| --- |
| **模块参数**：`DocumentType` |
| **类型：**字符向量 |
| **值**：`'Text'` | `'RTF'` | `'HTML'` |
| **默认值：**`'Text'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

使用为 Embedded Coder Flag 模块参数指定的模板符号，将注释添加到生成的代码中。需要 Embedded Coder 许可证。有关详细信息，请参阅 Use a Simulink DocBlock to Add a Comment (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史记录

**在 R2006a 之前推出**
