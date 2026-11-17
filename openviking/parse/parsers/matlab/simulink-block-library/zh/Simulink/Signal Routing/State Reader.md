---
type: simulink-block
title: 'State Reader'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'statereader'
documentation_source_path: 'slref/statereader.html'
language: zh-CN
chinese_source: worker-translation
---

# State Reader

## 端口

### 输出

### **Out** — 状态值 标量 | 向量

从状态所有者模块读取的状态值。

输出的维度为完整状态向量的维度。
有关具体模块，请参阅 **Initial conditions** 参数。例如，对于 **Delay length** 为 `N` 的 Delay 模块，State Reader 模块返回长度为 `[1xN]` 的状态向量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **State owner block** — 状态所有者模块的名称 none（默认）

此模块正在读取其状态的状态所有者模块的名称。要更改状态所有者模块，请从 **State Owner Selector Tree** 中选择一个模块。

**注意**

如果状态所有者模块的名称包含斜杠（`/`），则该斜杠在 State Reader 模块参数对话框中显示为两个斜杠（`//`）。此表示法用于区分模块名称本身中的斜杠与分隔模型层次结构中不同层级名称的斜杠。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateOwnerBlock` |
| **类型**：character vector |
| **Value:** `''` | `'<model path/block name>'` |
| **默认值**：`''` |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

R2025b 中未记录。

## 描述

读取模块状态

State Reader 模块读取受支持的状态所有者模块的当前状态。

State Reader 模块可以从以下状态所有者模块读取状态：

- Discrete State-Space
- Discrete-Time Integrator
- Delay
- Unit Delay
- Discrete Transfer Fcn
- Discrete Filter
- Discrete FIR Filter
- Integrator
- Second-Order Integrator
- 条件子系统模块的输出端口，例如 Enabled Subsystem、Triggered Subsystem 和 Function-Call Subsystem
- 具有多个离散状态的 S-Function

  要将 S-Function 模块配置为状态所有者模块，必须在 `mdlInitializeSizes` 中使用 `ssSetDWorkUsedAsDState` 将每个数据类型工作向量声明为离散状态向量，并使用 `ssSetDWorkName` 或 `ssSetDWorkRTWIdentifier` 为其命名。

**提示**

您可以通过模块的 `IsStateOwnerBlock` 参数值来确定模块是否为受支持的状态所有者模块。表达式

```
get_param(blk,'IsStateOwnerBlock')
```

其中 `blk` 是模块名称或句柄，如果该模块是受支持的状态所有者模块，则返回 `'on'`，否则返回 `'off'`。

要将 State Reader 或 State Writer 模块添加到模型中，请点击状态所有者模块以将其高亮显示。然后，在 Simulink® 工具条的当前模块选项卡中，点击 **Reader-Writer**。从菜单中选择 `State Reader Block` 或 `State Writer Block`。

**注意**

工具条的当前模块选项卡可能以高亮显示的模块名称标记，例如 **Outport**，也可能标记为 **Block**，具体取决于您高亮显示的模块类型。

Simulink 工具条的模块选项卡，显示 Reader-Writer 按钮及其下方的下拉菜单。列表项为 State Reader Block 和 State Writer Block。画布上高亮显示了一个 Unit Delay 模块。

如果状态所有者模块具有多个状态，则会打开 State Reader 或 State Writer 模块对话框。从 **State Owner Selector Tree** 中选择一个状态。

**注意**

在为 Second-Order Integrator 模块添加 State Reader 或 State Writer 模块之前，必须显式命名状态。请参阅 Specifying the State Names。

创建 State Reader 或 State Writer 模块后，状态所有者模块上方会出现一个内部带有 x 的菱形标记，并且状态所有者模块的名称会显示在 State Reader 或 State Writer 模块旁边。

Simulink 画布显示一个带有上方标记的 Unit Delay 模块，以及一个旁边显示“Unit Delay”的 State Writer 模块

State Reader 或 State Writer 模块不能与其状态所有者模块位于同一系统中。创建 State Reader 或 State Writer 模块后，请剪切并粘贴它以将其移动到模型层次结构中的所需位置。

或者，您可以从 Simulink Library Browser 向模型中添加 State Reader 或 State Writer 模块，然后在模块参数对话框中设置 **State owner block** 参数。

**注意**

当您创建包含 State Reader 或 State Writer 模块的库模块时，还必须在该库模块中包含相应的状态所有者模块。除了使用 Create Custom Library 中所述工作流创建的自定义库模块外，Simulink 还将使用 Subsystem Reference 模块创建的模型组件视为单模块库。

您可以选择 State Reader 或 State Writer 模块或相应的状态所有者模块，以高亮显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请将鼠标悬停在选择后出现的省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，会打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开图或新选项卡。
