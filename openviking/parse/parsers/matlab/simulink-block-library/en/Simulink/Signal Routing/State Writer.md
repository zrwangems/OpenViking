---
type: simulink-block
title: 'State Writer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'statewriter'
documentation_source_path: 'slref/statewriter.html'
language: en
---

# State Writer

## Ports

### Input

### **In** — State value scalar | vector

State value written to a state owner block.

When writing to a state owner block with an input scalar, the scalar
value is expanded to match the dimension of the state. All elements of
the state are set to the same value.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **State owner block** — Name of state owner block none (default)

Name of state owner block whose state this block is writing. To change the
state owner block, select a block from the **State Owner Selector
Tree**.

**Note**

If the name of a state owner block contains a slash
(`/`), the slash appears as two slashes
(`//`) in the State Writer block
parameters dialog. This notation distinguishes the slash in the block
name itself from slashes that separate names at different levels of the
model hierarchy.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StateOwnerBlock` |
| **Type:** character vector |
| **Value:** `''` | `'<model path/block name>'` |
| **Default:** `''` |

## Libraries

Simulink / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

Not documented in R2025b.

## Description

Write to a block state

The State Writer block sets the state of a supported state owner
block.

State Writer blocks can write state to these state owner blocks:

- Discrete State-Space
- Discrete-Time Integrator
- Delay
- Unit Delay
- Discrete Transfer Fcn
- Discrete Filter
- Discrete FIR Filter
- Integrator
- Second-Order Integrator
- Outport of conditional subsystem blocks such as Enabled
  Subsystem, Triggered Subsystem, and
  Function-Call Subsystem
- S-Function with multiple discrete states

  To configure an S-Function block as a state owner block, each data type work
  vector must be declared as a discrete state vector using `ssSetDWorkUsedAsDState` and
  named using `ssSetDWorkName` or `ssSetDWorkRTWIdentifier` in
  `mdlInitializeSizes`.

**Tip**

You can determine whether a block is a supported state owner block by the value of
the block's `IsStateOwnerBlock` parameter. The
expression

```
get_param(blk,'IsStateOwnerBlock')
```

where
`blk` is a block name or handle, returns
`'on'` if the block is a supported state owner block and
`'off'` otherwise.

To add a State Reader or State Writer block to your
model, click a state owner block to highlight it. Then, from the current block tab of
the Simulink® toolstrip, click **Reader-Writer**. From the menu, select
`State Reader Block` or `State Writer
Block`.

**Note**

The current block tab of the toolstrip might be labeled with the name of the
highlighted block, for example, **Outport**, or it might be labeled
**Block**, depending on the type of block you highlight.

Block tab of Simulink toolstrip, showing Reader-Writer button with drop-down menu beneath it. List items are State Reader Block and State Writer Block. A Unit Delay block is highlighted on the canvas.

If the state owner block has multiple states, then the State Reader or
State Writer block dialog opens. Select a state from the
**State Owner Selector Tree**.

**Note**

Before adding a State Reader or State Writer
block for a Second-Order Integrator block, you must explicitly
name the states. See Specifying the State Names.

After you create a State Reader or State Writer block,
a diamond shape with an x inside it badge appears above the state owner block, and the
name of the state owner block appears next to the State Reader or
State Writer block.

Simulink canvas showing Unit Delay block with a badge above it, and a State Writer block with "Unit Delay" appearing next to it

A State Reader or State Writer block cannot remain in
the same system as its state owner block. After you create a State Reader
or State Writer block, cut and paste it to move it to the desired
location within the model hierarchy.

Alternatively, you can add a State Reader or State
Writer block to your model from the Simulink Library Browser, then set the **State owner block**
parameter from the block parameters dialog.

**Note**

When you create a library block with a State Reader or State
Writer block, you must also include the corresponding state owner block
in the library block. In addition to custom library blocks created using the
workflow mentioned in Create Custom Library, Simulink treats model components created using Subsystem Reference block as a one-block library.

You can select a State Reader or State Writer block or a
corresponding state owner block to highlight blocks related to it. To show a related
block in an open diagram or new tab, pause on the ellipsis that appears after selection.
Then, select **Related Blocks**
Related Blocks button from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.
