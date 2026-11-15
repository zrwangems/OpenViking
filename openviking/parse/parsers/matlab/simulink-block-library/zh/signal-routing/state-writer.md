---
type: simulink-block
title: 'State Writer'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'statewriter'
language: zh-CN
chinese_source: worker-translation
---

# State Writer



写入模块状态

## 库

Simulink / Signal Routing

## 说明

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

## 端口

### 输入

### **In** — 状态值 标量 | 向量

写入状态拥有者模块的状态值。

当使用输入标量写入状态拥有者模块时，标量值会扩展以匹配状态的维度。状态的所有元素都会设置为相同的值。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **状态拥有者模块** — 状态拥有者模块的名称 none (default)

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

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。
