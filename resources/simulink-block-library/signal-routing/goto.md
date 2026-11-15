---
type: simulink-block
title: 'Goto'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'goto'
---

# Goto

Pass block input to From blocks

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Goto block passes its input to its corresponding From
blocks. The input can be a real- or complex-valued signal or vector of any data type.
From and Goto blocks allow you to pass a signal from
one block to another without actually connecting them.

A Goto block can pass its input signal to more than one From
block, although a From block can receive a signal from only one
Goto block. The input to that Goto block is passed to
the From blocks associated with it as though the blocks were physically
connected.

For example, this model uses a Goto block and a From
block.

A Sine Wave block connects to a Goto block. The corresponding From block connects to a Gain block.

An equivalent model passes the Sine Wave block signal directly to the
Gain block.

The Sine Wave block connects directly to the Gain block.

Goto blocks and From blocks are matched by the use of
Goto tags.

The **Tag
visibility** parameter determines where From blocks can
access the signal.

The Goto block supports signal label propagation. For more information, see
Signal Label Propagation.

You can simplify your model diagrams by replacing lengthy signal lines with sets of
connected Goto and From blocks. However, when you want to
trace a signal path, it can be useful to see the signal lines. You can convert signal
lines and virtual buses to Goto and From block sets, and
you can convert Goto and From block sets to signal lines.
For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal to be passed to the corresponding From
block, specified as a scalar, vector, matrix, or N-D array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Goto tag** — Block identifier `A` (default) | ...

The Goto block identifier. This parameter identifies the
Goto block whose scope is defined in this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `GotoTag` |
| **Type:** character vector |
| **Values:** `'A'` | `...` |
| **Default:** `'A'` |

### **Tag visibility** — Scope of the Goto block tag `local` (default) | `scoped` | `global`

The scope of the Goto block tag, specified as
`local`, `scoped`, or
`global`. When you set this parameter to
`scoped`, you must use a Goto Tag Visibility block to
define the scope of tag visibility.

- `local` (default) — From
  and Goto blocks that use the same tag must be in the
  same subsystem. A local tag name is enclosed in brackets
  (`[]`).
- `scoped` — From and
  Goto blocks that use the same tag must be
  either:

  - In the same subsystem.
  - At any level in the model hierarchy below the Goto
    Tag Visibility block that does not entail
    crossing a nonvirtual subsystem boundary. In other words,
    they must be within the boundary of an atomic, conditionally
    executed, or function-call subsystem or a model
    reference.

  A scoped tag name is enclosed in braces
  (`{}`).
- `global` — From and
  Goto blocks using the same tag can be anywhere in
  the model except in locations that span nonvirtual subsystem
  boundaries.

The rule that From-Goto block connections
cannot cross nonvirtual subsystem boundaries has the following exception. A
Goto block connected to a state port in one conditionally
executed subsystem is visible to a From block inside another
conditionally executed subsystem.

**Note**

A `scoped`
Goto block in a masked system is visible only in that
subsystem and in the nonvirtual subsystems it contains. Simulink® generates an error if you run or update a diagram that has
a Goto Tag Visibility block at a higher level in the
block diagram than the corresponding `scoped`
Goto block in the masked subsystem.

Use local tags when the Goto and From blocks
using the same tag name reside in the same subsystem. You must use global or
scoped tags when the Goto and From blocks
using the same tag name reside in different subsystems. When you define a
tag as global, all uses of that tag access the same signal. A tag defined as
scoped can be used in more than one place in the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TagVisibility` |
| **Type:** character vector |
| **Values:** `'local' | 'scoped' | 'global'` |
| **Default:** `'local'` |

### **Icon display** — Text to display on block icon `Tag` (default) | `Signal name` | `Tag and signal name`

Specifies the text to display on the block icon. The options are the block
tag, the name of the signal that the block represents, or both the tag and
the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IconDisplay` |
| **Type:** character vector |
| **Values:** `'Signal name' | 'Tag' | 'Tag and signal name'` |
| **Default:** `'Tag'` |

### **Rename All** — Propagate name throughout model button

Rename the Goto tag. The new name propagates to all
From and Goto Tag Visibility blocks that
are listed in the **Corresponding blocks** box.

Alternatively, when you change the tag on the Goto block icon, propagate
the new name to all corresponding From and Goto Tag
Visibility blocks by pressing
**Shift+Enter**.

### **Corresponding blocks** — Blocks connected to this Goto block block path | ...

List of the From blocks and Goto Tag Visibility blocks
connected to this Goto block. Click an entry in the list to
display and highlight the corresponding From and Goto
Tag Visibility blocks.

Alternatively, in the Simulink Editor, select the Goto block to highlight the
corresponding From and Goto Tag Visibility
blocks.

Two From blocks that correspond to the selected Goto block are highlighted.

When a corresponding From or Goto Tag Visibility block is
not in the current diagram, the Subsystem block that contains
the block is highlighted.

To show a corresponding block in an open diagram or new tab, select the
Goto block and pause on the ellipsis. Then, select
**Related Blocks**
Related Blocks button from the action bar. When multiple blocks
correspond to the selected block, a list of related blocks opens. You can
filter the list of related blocks by entering a search term in the text box.
After you select a related block from the list, window focus goes to the
open diagram or new tab that shows the related block.

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
implementation and synthesized logic. HDL code generation does not support
**Tag Visibility** of the blocks set to
`global`. See also Required HDL Settings for Goto and From Blocks (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Convert signal lines to Goto and From block sets

You can convert signal lines and virtual buses to sets of connected
Goto and From blocks, and you can convert
Goto and From block sets to signal lines.

For more information, see Convert Signal Lines to Goto and From Blocks and Vice Versa.
