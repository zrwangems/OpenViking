---
type: simulink-block
title: 'State Reader'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'statereader'
---

# State Reader

Read a block state

## 中文

读取模块状态

### 库

Simulink / Signal Routing

### 描述

State Reader block 读取受支持的状态拥有者模块的当前状态。

State Reader block 可以从以下状态拥有者模块读取状态：

- Discrete State-Space
- Discrete-Time Integrator
- Delay
- Unit Delay
- Discrete Transfer Fcn
- Discrete Filter
- Discrete FIR Filter
- Integrator
- Second-Order Integrator
- Enabled Subsystem、Triggered Subsystem 和 Function-Call Subsystem 等条件子系统模块的 Outport
- 具有多个离散状态的 S-Function

  要将 S-Function block 配置为状态拥有者模块，必须使用 `ssSetDWorkUsedAsDState` 将每个数据类型工作向量声明为离散状态向量，并在 `mdlInitializeSizes` 中使用 `ssSetDWorkName` 或 `ssSetDWorkRTWIdentifier` 为其命名。

**提示**

您可以通过模块的 `IsStateOwnerBlock` 参数值确定该模块是否为受支持的状态拥有者模块。表达式

`get_param(blk,'IsStateOwnerBlock')`

其中 `blk` 是模块名称或句柄；如果该模块是受支持的状态拥有者模块，则返回 `'on'`，否则返回 `'off'`。

要将 State Reader 或 State Writer block 添加到模型，请点击一个状态拥有者模块以将其高亮显示。然后，在 Simulink® 工具条的当前模块选项卡中，点击 **读取器-写入器**。从菜单中选择 `State Reader Block` 或 `State Writer Block`。

**注意**

工具条的当前模块选项卡可能以高亮模块的名称标记，例如 **Outport**，也可能标记为 **模块**，具体取决于您高亮的模块类型。

Simulink 工具条的模块选项卡，显示读取器-写入器按钮及其下方的下拉菜单。列表项为 State Reader Block 和 State Writer Block。画布上有一个 Unit Delay block 处于高亮状态。

如果状态拥有者模块具有多个状态，则会打开 State Reader 或 State Writer block 对话框。从 **状态拥有者选择器树** 中选择一个状态。

**注意**

在为 Second-Order Integrator block 添加 State Reader 或 State Writer block 之前，必须显式命名状态。请参阅“指定状态名称”。

创建 State Reader 或 State Writer block 后，状态拥有者模块上方会出现一个内部带有 x 的菱形标记，且状态拥有者模块的名称会出现在 State Reader 或 State Writer block 旁边。

Simulink 画布显示一个 Unit Delay block，其上方有一个标记，以及一个 State Writer block，旁边显示 "Unit Delay"

State Reader 或 State Writer block 不能与其状态拥有者模块位于同一系统中。创建 State Reader 或 State Writer block 后，请剪切并粘贴它，以将其移动到模型层次结构中的所需位置。

或者，您可以从 Simulink 库浏览器向模型添加 State Reader 或 State Writer block，然后在模块参数对话框中设置 **状态拥有者模块** 参数。

**注意**

创建包含 State Reader 或 State Writer block 的库模块时，还必须在库模块中包含对应的状态拥有者模块。除了使用“创建自定义库”中所述工作流创建的自定义库模块外，Simulink 还会将使用 Subsystem Reference block 创建的模型组件视为单模块库。

您可以选择 State Reader 或 State Writer block，或对应的状态拥有者模块，以高亮与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在选择后出现的省略号上。然后，从操作栏中选择 **相关模块** 按钮。当多个模块与所选模块对应时，会打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开图或新选项卡。

### 端口

#### 输出

#### **Out** — 状态值 标量 | 向量

从状态拥有者模块读取的状态值。

输出的维度是完整状态向量的维度。有关特定模块，请参阅 **初始条件** 参数。例如，对于 **延迟长度** 为 `N` 的 Delay block，State Reader block 返回长度为 `[1xN]` 的状态向量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **状态拥有者模块** — 状态拥有者模块的名称 none（默认）

此模块正在读取其状态的状态拥有者模块的名称。要更改状态拥有者模块，请从 **状态拥有者选择器树** 中选择一个模块。

**注意**

如果状态拥有者模块的名称包含斜杠（`/`），则在 State Reader block 参数对话框中该斜杠会显示为两个斜杠（`//`）。此表示法将模块名称本身的斜杠与用于分隔模型层次结构不同级别名称的斜杠区分开来。

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

The State Reader block reads the current state of a supported state
owner block.

State Reader blocks can read state from these state owner
blocks:

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

Block tab of Simulink toolstrip, showing Reader-Writer button with drop-down menu beneath it. List items are State Reader Block and State Writer Block. An Unit Delay block is highlighted on the canvas.

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

When you create a library block with a State Reader or
State Writer block, you must also include the corresponding state
owner block in the library block. In addition to custom library blocks created using
the workflow mentioned in Create Custom Library, Simulink treats model components created using Subsystem Reference block as a one-block library.

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

### Output

### **Out** — State value scalar | vector

State value read from a state owner block.

The dimension of the output is the dimension of the full state vector.
Refer to the **Initial conditions** parameter for
specific blocks. For example, for a Delay block with a
**Delay length** of `N`, the
State Reader block returns a state vector of length
`[1xN]`.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **State owner block** — Name of state owner block none (default)

Name of state owner block whose state this block is reading. To change the
state owner block, select a block from the **State Owner Selector
Tree**.

**Note**

If the name of a state owner block contains a slash
(`/`), the slash appears as two slashes
(`//`) in the State Reader block
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
