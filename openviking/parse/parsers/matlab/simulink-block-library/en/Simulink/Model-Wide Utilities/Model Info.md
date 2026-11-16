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
language: en
---

# Model Info

## Ports

Not documented in R2025b.

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

## Description

Display model properties and text in model

The Model Info block displays model properties and text about a model on the
mask of the block. Use the Model Info block dialog box to specify the
content and format of the text that the block displays. You can select model properties
to display on the block. In the text displayed on the block mask, the software replaces
the property name with the current value of the property in the model.
