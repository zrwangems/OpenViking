---
type: simulink-block
title: 'Goto Tag Visibility'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'gototagvisibility'
---

# Goto Tag Visibility

Define scope of Goto block tag

## Libraries

Simulink / Signal Routing

## Description

The Goto Tag Visibility block defines the accessibility of
Goto block tags that have `scoped` visibility. The
value you specify for the **Goto tag** block parameter is accessible by
From blocks in the same subsystem that contains the Goto Tag
Visibility block and in subsystems below it in the model hierarchy.

A Goto Tag Visibility block is required for Goto blocks
whose **Tag Visibility** parameter value is `scoped`.
No Goto Tag Visibility block is needed if the tag visibility is either
`local` or `global`. The block shows the tag name
enclosed in braces (`{}`).

**Note**

A `scoped`
Goto block in a masked system is visible only in that subsystem and
in the nonvirtual subsystems it contains. Simulink® generates an error if you run or update a diagram that has a
Goto Tag Visibility block at a lower level in the block diagram
than the corresponding `scoped`
Goto block in the masked subsystem.

In the Simulink Editor, select the Goto Tag Visibility block to highlight
the corresponding Goto and From blocks. When a
corresponding From or Goto block is not in the current
diagram, the Subsystem block that contains the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the Goto Tag
Visibility block and pause on the ellipsis. Then, select **Related
Blocks**
Related Blocks button from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

## Parameters

### **Goto tag** — Goto block tag whose visibility is defined by the location of this block `A` (default) | ...

The Goto block tag whose visibility is defined by the
location of this block. From and Goto blocks
using the specified tag must be in the same subsystem or at any level in the
model hierarchy below the Goto Tag Visibility block that does
not entail crossing a nonvirtual subsystem boundary, in other words, the
boundary of an atomic, conditionally executed, or function-call subsystem or
a model reference. A scoped tag name is enclosed in braces
(`{}`).

#### Tips

If you use multiple From and Goto Tag
Visibility blocks to refer to the same Goto tag, you can
simultaneously rename the tag in all of the blocks. Use the
**Rename All** button in the Goto block dialog box.
Alternatively, when you change the tag on the Goto block icon,
propagate the new name to all corresponding From and
Goto Tag Visibility blocks by pressing
**Shift+Enter**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
