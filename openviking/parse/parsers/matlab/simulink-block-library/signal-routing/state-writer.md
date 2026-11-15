---
type: simulink-block
title: 'State Writer'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'statewriter'
---

# State Writer

Write to a block state

## 中文

写入模块状态

### 库

Simulink / Signal Routing

### 说明

State Writer 模块设置受支持的状态拥有者模块的状态。

State Writer 模块可以将状态写入以下状态拥有者模块：

- Discrete State-Space
- Discrete-Time Integrator
- Delay
- Unit Delay
- Discrete Transfer Fcn
- Discrete Filter
- Discrete FIR Filter
- Integrator
- Second-Order Integrator
- 条件子系统模块（例如 Enabled
  Subsystem、Triggered Subsystem 和
  Function-Call Subsystem）的 Outport
- 具有多个离散状态的 S-Function

  要将 S-Function 模块配置为状态拥有者模块，每个数据类型工作向量必须使用 `ssSetDWorkUsedAsDState` 声明为离散状态向量，并使用 `ssSetDWorkName` 或 `ssSetDWorkRTWIdentifier` 在
  `mdlInitializeSizes` 中命名。

**提示**

你可以通过模块的 `IsStateOwnerBlock` 参数的值确定某个模块是否为受支持的状态拥有者模块。表达式

```
get_param(blk,'IsStateOwnerBlock')
```

其中
`blk` 是模块名称或句柄，如果该模块是受支持的状态拥有者模块，则返回
`'on'`，否则返回
`'off'`。

要将 State Reader 或 State Writer 模块添加到模型中，请点击一个状态拥有者模块以将其高亮显示。然后，在 Simulink® 工具条的当前模块选项卡中，点击 **读取器-写入器**。在菜单中，选择
`State Reader Block` 或 `State Writer Block`。

**注意**

工具条的当前模块选项卡可能以高亮模块的名称标记，例如 **Outport**，或者可能标记为
**Block**，具体取决于你高亮的模块类型。

Simulink 工具条的模块选项卡，显示带下方下拉菜单的读取器-写入器按钮。列表项为 State Reader Block 和 State Writer Block。画布上高亮显示了一个 Unit Delay 模块。

如果状态拥有者模块有多个状态，则会打开 State Reader 或 State Writer 模块对话框。从 **状态拥有者选择器树** 中选择一个状态。

**注意**

在为 Second-Order Integrator 模块添加 State Reader 或 State Writer 模块之前，必须显式命名状态。请参阅 Specifying the State Names。

创建 State Reader 或 State Writer 模块后，状态拥有者模块上方会出现一个内部带 x 的菱形徽章，并且状态拥有者模块的名称会显示在 State Reader 或 State Writer 模块旁边。

Simulink 画布，显示上方带有徽章的 Unit Delay 模块，以及旁边显示 "Unit Delay" 的 State Writer 模块

State Reader 或 State Writer 模块不能与其状态拥有者模块留在同一系统中。创建 State Reader 或 State Writer 模块后，请剪切并粘贴它以将其移动到模型层次结构中的所需位置。

或者，你可以从 Simulink Library Browser 中向模型添加 State Reader 或 State Writer 模块，然后从模块参数对话框中设置 **状态拥有者模块** 参数。

**注意**

当创建包含 State Reader 或 State Writer 模块的库模块时，你还必须在库模块中包含对应的状态拥有者模块。除了使用 Create Custom Library 中所述工作流创建的自定义库模块外，Simulink 还会将使用 Subsystem Reference 模块创建的模型组件视为单模块库。

你可以选择一个 State Reader 或 State Writer 模块，或者选择对应的状态拥有者模块，以高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请暂停在选中后出现的省略号上。然后，从操作栏中选择 **相关模块** 按钮。当多个模块与所选模块对应时，会打开相关模块列表。你可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点会转到显示该相关模块的已打开图或新选项卡。

### 端口

#### 输入

#### **In** — 状态值 标量 | 向量

写入状态拥有者模块的状态值。

当使用输入标量写入状态拥有者模块时，标量值会扩展以匹配状态的维度。状态的所有元素都会设置为相同的值。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **状态拥有者模块** — 状态拥有者模块的名称 none (default)

此模块正在写入其状态的状态拥有者模块的名称。要更改状态拥有者模块，请从 **状态拥有者选择器树** 中选择一个模块。

**注意**

如果状态拥有者模块的名称包含斜杠
(`/`)，则在 State Writer 模块参数对话框中该斜杠会显示为两个斜杠
(`//`)。此表示法用于区分模块名称本身的斜杠与分隔模型层次结构不同层级名称的斜杠。

#### 编程用法

|  |
| --- |
| **模块参数：** `StateOwnerBlock` |
| **类型：** character vector |
| **值：** `''` | `'<model path/block name>'` |
| **默认值：** `''` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## Libraries

Simulink / Signal Routing

## Description

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
