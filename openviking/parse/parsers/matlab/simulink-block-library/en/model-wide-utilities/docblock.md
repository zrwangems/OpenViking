---
type: simulink-block
title: 'DocBlock'
family: model-wide-utilities
documentation_release: R2025b
official_category: 'Model-Wide Utilities'
documentation_page: 'docblock'
language: en
---

# DocBlock

## Ports

Not documented in R2025b.

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

## Libraries

Simulink / Model-Wide Utilities HDL Coder / Model-Wide Utilities

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

## Description

Create text that documents model and save text with model

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
