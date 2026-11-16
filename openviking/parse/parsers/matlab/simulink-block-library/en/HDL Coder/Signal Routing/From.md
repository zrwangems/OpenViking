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
language: en
---

# From

## Ports

### Output

### **Port\_1** — Signal from connected Goto block scalar | vector | matrix | N-D array

Signal from connected Goto block, output with the same
dimensions and data type as the input to the Goto
block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Goto Tag** — Tag of the Goto block that forwards its signal to this block `A` (default) | `<More Tags...>` | ...

Specify the tag of the Goto block that forwards its signal
to this From block. To change the tag, select a new tag from
the drop-down list.

The drop-down list displays the Goto tags that the From
block can currently see. An item labeled `<More
Tags...>` appears at the end of the list the first time you
display the list in a Simulink® session. Selecting this item causes the block to update the
tags list to include the tags of Goto blocks residing in
library subsystems referenced by the model containing this
From block. Simulink software displays a progress bar while building the list of
library tags. Simulink saves the updated tags list for the duration of the
Simulink session or until the next time you select the adjacent
**Update Tags** button. You need to update the tags
list again in the current session only if the libraries referenced by the
model have changed since the last time you updated the list.

**Tip**

If you use multiple From and Goto Tag Visibility blocks to
refer to the same Goto tag, you can simultaneously rename the tag in all
of the blocks. To do so, use the **Rename All** button
in the Goto block dialog box. Alternatively, when you
change the tag on the Goto block icon,
propagate the new name to all corresponding From and
Goto Tag Visibility blocks by pressing
**Shift+Enter**.

To find the relevant Goto block, use the **Goto
Source** hyperlink in the From block dialog
box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

### **Update Tags** — Update list of visible tags button

Updates the list of tags visible to this From block,
including tags residing in libraries referenced by the model containing this
From block. Update the tags list again in the current
session only if the libraries referenced by the model have changed since the
last time you updated the list.

### **Goto Source** — Path to connected Goto block block path

Path of the Goto block connected to this
From block. Clicking the path displays and highlights the
Goto block in your model.

In the Simulink Editor, selecting the From block highlights the
corresponding Goto and Goto Tag Visibility
blocks.

The Goto block that corresponds to the selected From block is highlighted.

When a corresponding Goto or Goto Tag
Visibility block is not in the current diagram, the
Subsystem block that contains the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the
From block and pause on the ellipsis. Then, select
**Related Blocks**
Related Blocks button from the action bar. When multiple blocks
correspond to the selected block, a list of related blocks opens. You can
filter the list of related blocks by entering a search term in the text box.
After you select a related block from the list, window focus goes to the
open diagram or new tab that shows the related block.

### **Icon Display** — Text to display on block icon `Tag` | `Tag and signal name` | `Signal name`

Specifies the text to display on the From block icon. The
options are the block tag, the name of the signal that the block represents,
or both the tag and the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **Default:** `'Tag'` |

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. See also Required HDL Settings for Goto and From Blocks (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Convert signal lines to Goto and From block sets

You can convert signal lines and virtual buses to sets of connected
Goto and From blocks, and you can convert
Goto and From block sets to signal lines.

For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.

## Description

Accept input from Goto block

The From block accepts a signal from a corresponding Goto
block, then passes it as output. The data type of the output is the same as that of the
input from the Goto block. From and Goto
blocks allow you to pass a signal from one block to another without actually connecting
them.

For example, this model uses a Goto block and a From
block.

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

An equivalent model passes the Sine Wave block signal directly to the
Gain block.

The Sine Wave block connects directly to the Gain block.

A From block can receive its signal from only one Goto
block, although a Goto block can pass its signal to more than one
From block.

To associate a Goto block with a From block, enter the
Goto block tag in the **Goto Tag**
parameter.

The visibility of a Goto block tag determines the From blocks
that can receive its signal. For more information, see Goto and Goto Tag Visibility. The block indicates
the visibility of the Goto block tag:

- A local tag name is enclosed in brackets (`[]`).
- A scoped tag name is enclosed in braces (`{}`).
- A global tag name appears without additional characters.

The From block supports signal label propagation. For more information, see
Signal Label Propagation.

You can simplify your model diagrams by replacing lengthy signal lines with sets of
connected Goto and From blocks. However, when you want to
trace a signal path, it can be useful to see the signal lines. You can convert signal
lines and virtual buses to Goto and From block sets, and
you can convert Goto and From block sets to signal lines.
For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.
