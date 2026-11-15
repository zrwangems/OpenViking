---
type: simulink-block
title: 'State Writer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'statewriter'
documentation_source_path: 'slref/statewriter.html'
language: zh-CN
chinese_source: worker-translation
---

# State Writer

## 端口

### 输入

### **In** — 状态值 标量 | 向量

状态值写入到状态所有者模块。

当使用输入标量写入状态所有者模块时，标量值会扩展以匹配状态的维度。状态的所有元素都设置为相同的值。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **State owner block** — 状态所有者模块名称 none（默认）

此模块正在写入其状态的状态所有者模块的名称。要更改状态所有者模块，请从 **State Owner Selector Tree** 中选择一个模块。

**注意**

如果状态所有者模块的名称包含斜杠（`/`），则斜杠在 State Writer 模块参数对话框中显示为两个斜杠（`//`）。此表示法将模块名称本身的斜杠与分隔模型层次结构中不同级别名称的斜杠区分开。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateOwnerBlock` |
| **类型：** character vector |
| **值：** `''` | `'<model path/block name>'` |
| **默认值：** `''` |

## 所属库

Simulink / Signal Routing

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

## 版本历史

R2025b 中未记录。

## 描述

写入模块状态

State Writer 模块设置受支持的状态所有者模块的状态。

State Writer 模块可以将状态写入这些状态所有者模块：

- Discrete State-Space
- Discrete-Time Integrator
- Delay
- Unit Delay
- Discrete Transfer Fcn
- Discrete Filter
- Discrete FIR Filter
- Integrator
- Second-Order Integrator
- 条件子系统模块（例如 Enabled Subsystem、Triggered Subsystem 和 Function-Call Subsystem）的 Outport
- 具有多个离散状态的 S-Function

  要将 S-Function 模块配置为状态所有者模块，必须使用 `ssSetDWorkUsedAsDState` 将每个数据类型工作向量声明为离散状态向量，并在 `mdlInitializeSizes` 中使用 `ssSetDWorkName` 或 `ssSetDWorkRTWIdentifier` 命名。

**提示**

您可以通过模块的 `IsStateOwnerBlock` 参数的值确定模块是否为受支持的状态所有者模块。表达式

```
get_param(blk,'IsStateOwnerBlock')
```

其中 `blk` 是模块名称或句柄，如果模块是受支持的状态所有者模块，则返回 `'on'`，否则返回 `'off'`。

要将 State Reader 或 State Writer 模块添加到模型，请点击状态所有者模块以突出显示它。然后，在 Simulink® 工具条的当前模块选项卡中，点击 **Reader-Writer**。从菜单中，选择 `State Reader Block` 或 `State Writer Block`。

**注意**

工具条的当前模块选项卡可能以突出显示的模块名称标记，例如 **Outport**，或者可能标记为 **Block**，具体取决于您突出显示的模块类型。

Simulink 工具条的模块选项卡，显示 Reader-Writer 按钮及其下方的下拉菜单。列表项为 State Reader Block 和 State Writer Block。画布上突出显示了一个 Unit Delay 模块。

如果状态所有者模块有多个状态，则打开 State Reader 或 State Writer 模块对话框。从 **State Owner Selector Tree** 中选择一个状态。

**注意**

在为 Second-Order Integrator 模块添加 State Reader 或 State Writer 模块之前，必须显式命名状态。请参阅 Specifying the State Names。

创建 State Reader 或 State Writer 模块后，状态所有者模块上方会出现一个内部带 x 的菱形标记，并且状态所有者模块的名称会出现在 State Reader 或 State Writer 模块旁边。

Simulink 画布显示一个 Unit Delay 模块，其上方有一个标记，以及一个 State Writer 模块，旁边显示 "Unit Delay"。

State Reader 或 State Writer 模块不能与其状态所有者模块保留在同一系统中。创建 State Reader 或 State Writer 模块后，请剪切并粘贴它以将其移动到模型层次结构中的所需位置。

或者，您可以从 Simulink Library Browser 将 State Reader 或 State Writer 模块添加到模型，然后从模块参数对话框设置 **State owner block** 参数。

**注意**

当创建包含 State Reader 或 State Writer 模块的库模块时，还必须将对应的状态所有者模块包含在库模块中。除了使用 Create Custom Library 中所述工作流创建的自定义库模块外，Simulink 还将使用 Subsystem Reference 模块创建的模型组件视为单模块库。

您可以选择 State Reader 或 State Writer 模块或对应的状态所有者模块，以突出显示与其相关的模块。要在打开的图或新选项卡中显示相关模块，请暂停在选中后出现的省略号上。然后，从操作栏中选择 **Related Blocks** Related Blocks 按钮。当多个模块与所选模块对应时，会打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示相关模块的打开图或新选项卡。
