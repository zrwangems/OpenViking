---
type: simulink-block
title: 'Toggle Switch'
family: dashboard
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'toggleswitch'
---

# Toggle Switch

Toggle parameter between two values

## 中文

将参数在两个值之间切换

### 所属库

Simulink / Dashboard

### 描述

在仿真过程中，Toggle Switch 模块将连接的模块参数的值在两个值之间切换。例如，可以将 Toggle Switch 模块连接到模型中的 Switch 模块，并在仿真期间更改其状态。将 Toggle Switch 模块与其他 Dashboard 模块结合使用，可以为模型创建交互式仪表板。

在仿真期间以及 Toggle Switch 模块处于选中状态时，双击该模块不会打开其对话框。要编辑模块的参数，可以使用**属性检查器**，或者右键点击模块并从上下文菜单中选择**模块参数**。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要连接到其参数的模块。从出现的列表中，选择要连接的参数。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数或修改定义所连接的参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Toggle Switch 模块连接到您的模型。

An unconnected Toggle Switch block connects to the Value parameter of a Constant block.

#### 参数记录

连接到 Dashboard 模块的可调参数数据会记录到仿真数据检查器，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据来访问 MATLAB® 工作区中记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅将数据导出到工作区或文件。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素来访问。

### 参数

#### **连接** — 要连接的模块参数值 参数值连接选项

Dashboard 模块不使用端口来连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的**连接**表。要从属性检查器打开“模块参数”对话框，请在**连接到**的右侧，点击**连接**或**更改**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅Connect Dashboard Blocks to Simulink Model。

使用**连接**表将控制模块连接到带标量值的参数，或将控制模块连接更改为带标量值的参数：

1. 选择模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**连接**。要更改模块的连接，请改为点击**更改**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接的参数。
5. 点击**应用**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数或修改定义所连接的参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

##### 编程用法

要以编程方式将 Dashboard 模块连接到可调参数或变量，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将 Dashboard 模块连接到由值定义的参数，有些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为一个给定的 Dashboard 模块可以连接到由值定义的参数或由变量定义的参数。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.ParamSourceInfo` |
| **默认值：**`[]` |

#### **状态** — 将值和标签配对 标量和字符向量

对组，包含要赋给所连接的变量或参数的值，以及要在模块上显示的文本。开关有两种状态 - **顶端**和**底端** - 每种状态对应一个开关位置。每种状态包含一个**值**和一个**标签**。

- **值** - 当开关处于某一位置时，要相应赋给所连接的变量或参数的值。
- **标签** - 当开关处于某一位置时，要在模块上相应显示的文本。

下表说明模块的默认配置。

| 位置 | 状态值 | 状态标签 |
| --- | --- | --- |
| **顶端** | `0` | `on` |
| **底端** | `1` | `off` |

##### 编程用法

要以编程方式为模块配置**状态**，请将 `States` 参数的值指定为包含两个元素的结构体数组，其中具有字段：

- `Value` - 表示状态的双精度标量值。
- `Label` - 用作开关位置标签的字符串或字符数组。

```
topState.Value = 0;
topState.Label = 'Off';
bottomState.Value = 1;
bottomState.Label = 'On';
switchStates = [topState bottomState];
```

|  |
| --- |
| **模块参数**：`States` |
| **类型：**结构体的二元素数组 |

#### **标签** — 模块标签位置 `Top` (默认) | `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接的元素的名称。

##### 编程用法

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型：**字符向量 |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

### 版本历史记录

**在 R2015a 中推出**

#### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。要打开它，请先选择面板并将鼠标暂停在出现的省略号上。在展开的操作菜单中，点击**在新窗口中打开**按钮 。

您可以单独最小化和还原包含面板的新窗口，而不影响模型窗口。您可以通过面板窗口运行、暂停、停止和逐步运行仿真。在面板窗口中，您可以编辑面板及其中包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，点击**在画布中打开** 。

有关在新窗口中打开面板的详细信息，请参阅Open Panels in New Window。

#### R2023a: Simulink 工具条中的持久面板选项卡

向模型添加仪表板面板时，**面板**选项卡会出现在 Simulink 工具条中，并显示用于管理和编辑面板的选项。

在之前的版本中，**面板**选项卡仅在面板选中时可见。从 R2023a 开始，即使没有选择面板时，**面板**选项卡仍保持可见。

**面板**选项卡也包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

#### R2022b: 面板中的可自定义 Dashboard 模块支持撤消和重做操作

从 R2022b 开始，您可以撤消和重做对面板中的可自定义 Dashboard 模块所做的更改。

要撤消或重做更改，请执行以下操作：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷方式基于 Windows®。在 Mac 上，按 **command** (⌘) 代替 **Ctrl**。

#### R2022b: 对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板及其中包含的 Dashboard 模块。

点击面板中的 Dashboard 模块时，将显示该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，**仪表**选项卡会出现在工具条中。

当您点击某个面板时，工具条中会出现**面板**选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 调整所有未隐藏的面板以适应当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2021a: 使用 Dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中选择要连接的参数。当选择具有非标量值的参数时，使用对话框中的文本框指定要调节的元素。

#### R2020b: Simulink 工具条对 Dashboard 模块的支持

从 R2020b 开始，当您从 Simulink 库中的 Dashboard 库中或从 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库中选择模型中的某个模块时，Simulink 工具条中的**模块**选项卡会变为特定于模块的选项卡。从工具条中，可以连接、断开连接和修改所选模块的连接。您可以跳转至连接到所选模块的模型元素，也可以将所选模块添加到面板中。

#### R2019a: 以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数从模型中的 Dashboard 库创建和配置模块。

## Libraries

Simulink / Dashboard

## Description

The Toggle Switch block toggles the value of the connected block
parameter between two values during simulation. For example, you can connect the
Toggle Switch block to a Switch block in your model
and change its state during simulation. Use the Toggle Switch block with
other Dashboard blocks to create an interactive dashboard for your model.

Double-clicking the Toggle Switch block does not open its dialog box
during simulation and when the block is selected. To edit the block's parameters, you
can use the **Property Inspector**, or you can right-click the block
and select **Block Parameters** from the context menu.

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard
block, use connect mode. To enter connect mode on an unconnected block, pause on the block
you want to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a control block to a parameter in your model or to change the connection of a
control block, enter connect mode. Select the block to whose parameter you want to connect.
From the list that appears, select the parameter to which you want to connect. Then, pause
on the dashboard block and click the Done Connecting button .

The control block cannot connect to a parameter defined by a variable until you update the
model diagram. To connect to a parameter defined by a variable or to modify the value of a
variable that defines the value of a connected parameter when the simulation is not running,
update the model diagram by pressing **Ctrl+D**.

You can connect to a parameter with a scalar value or to an element of a matrix or structure.
For more information, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

This animation shows how to connect the Toggle Switch block to your
model.

An unconnected Toggle Switch block connects to the Value parameter of a Constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB® workspace by exporting the parameter data from the Simulation Data Inspector
by using the UI or the `Simulink.sdi.exportRun` function. For more information about exporting
data using the Simulation Data Inspector UI, see Export Data to Workspace or File. The
parameter data is stored in a `Simulink.SimulationData.Parameter` object, accessible as an element in the
exported `Simulink.SimulationData.Dataset`.

## Parameters

### **Connection** — Block parameter value to connect parameter value connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink® Toolstrip, or the **Connection** table in the Block
Parameters dialog box. To open the Block Parameters dialog box from the Property
Inspector, to the right of **Connected to**, click
**Connect** or **Change**. You can connect to a
parameter with a scalar value, or to an element of a matrix. For information about
connect mode and how to connect using the toolstrip, see Connect Dashboard Blocks to Simulink Model.

To connect a control block to a parameter with a scalar value or change the connection
of a control block to a parameter with a scalar value using the
**Connection** table:

1. Select the block.
2. To connect the block, in the Property Inspector, on the
   **Parameters** tab, click **Connect**.
   To change the connection of the block, click **Change**
   instead.
3. Select the block to whose parameter value you want to connect.
4. In the table, select the parameter to which you want to connect.
5. Click **Apply**.

The control block cannot connect to a parameter defined by a variable until you update
the model diagram. To connect to a parameter defined by a variable or to modify the
value of a variable that defines the value of a connected parameter when the simulation
is not running, update the model diagram by pressing **Ctrl+D**.

You can also connect dashboard blocks to a Stateflow chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

#### Programmatic Use

To programmatically connect a dashboard block to a tunable parameter, use a
`Simulink.HMI.ParamSourceInfo` object. The
`Simulink.HMI.ParamSourceInfo` object contains four properties.
Some properties apply to connecting dashboard blocks to parameters defined by
values, and some apply to connecting dashboard blocks to parameters defined by
variables. Not all fields have a value for a connection because a given dashboard
block connects to either to a parameter defined by a value or to a parameter defined
by a variable.

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

### **States** — Pair values and labels scalar and character vector

Pairs of values to assign to the connected variable or parameter and text to
display on the block. Switches have two states — **Top** and
**Bottom** — one corresponding to each switch position. Each
state contains a **Value** and a **Label**.

- **Value** — Value to assign to the connected variable
  or parameter when the switch is in the corresponding position.
- **Label** — Text to display on the block for the
  corresponding position.

This table describes the default configuration for the block.

| Position | State Value | State Label |
| --- | --- | --- |
| **Top** | `0` | `on` |
| **Bottom** | `1` | `off` |

#### Programmatic Use

To configure the **States** for the block programmatically,
specify the value of the `States` parameter as a structure
array containing two elements with fields:

- `Value` — Scalar double value for the
  state.
- `Label` — String or character array to use as the
  label for the switch position.

```
topState.Value = 0;
topState.Label = 'Off';
bottomState.Value = 1;
bottomState.Label = 'On';
switchStates = [topState bottomState];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** two element array of structures |

### **Label** — Block label position `Top` (default) | `Bottom` | `Hide`

Position of the block label. When the block is connected to an element in the
model, the label is the name of the connected element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2015a**

### R2023b: Open panel in new window

Starting in R2023b, you can open a dashboard panel in a new window. To do so,
select the panel and pause on the ellipsis that appears. In the action menu that
expands, click the **Open In New Window** button
.

You can minimize and restore the new window containing the panel separately from
the model window. From the panel window, you can run, pause, stop, and step through
the simulation. In the panel window, you can edit the panel and the blocks it
contains.

To return the panel to the model canvas, in the panel window toolstrip, click
**Open in canvas**
.

For more information about opening a panel in a new window, see Open Panels in New Window.

### R2023a: Persistent panels tab in Simulink Toolstrip

When you add a dashboard panel to a model, the **Panels** tab
appears in the Simulink Toolstrip and shows options for managing and editing panels.

Previously, the **Panels** tab was only visible when a panel was
selected. Starting in R2023a, the **Panels** tab stays visible when
no panel is selected.

The **Panels** tab also contains these new options:

- You can add an empty panel.
- You can rename the selected panel.
- You can hide the selected panel.

### R2022b: Undo and redo support for customizable dashboard blocks in panel

Starting in R2022b, you can undo and redo the changes you make to customizable
dashboard blocks that are in a panel.

To undo or redo a change:

1. Click the panel or a block in the panel.
2. Press **Ctrl+Z** to undo the change, or press
   **Ctrl+Y** to redo the change.

**Note**

The keyboard shortcuts are based on Windows®. On a Mac, press **command** (⌘) instead of
**Ctrl**.

### R2022b: Toolstrip support for panels

Starting in R2022b, you can use the Simulink Toolstrip to manage and edit panels and the dashboard blocks that they
contain.

When you click a dashboard block in a panel, the toolstrip tab for the block
appears. For example, when you click a Circular Gauge block, the
**Gauge** tab appears in the toolstrip.

When you click a panel, the **Panel** tab appears in the
toolstrip. The tab provides these options:

- Manage the visibility of panels in the model.
- Fit all unhidden panels within the current view.
- Collapse the selected panel.
- Customize the size and the contents of the panel.
- Set a custom background image for the selected panel.
- Add a new tab to the selected panel.

### R2021a: Tune matrix and structure elements using dashboard blocks

Starting in R2021a, you can connect a block from the Dashboard library to a scalar
element of a matrix or structure that defines the value of a tunable block
parameter. When you connect a dashboard block to a tunable parameter, you first
select one or more blocks. Then, in a dialog box, you select the parameter to which
you want to connect. When you select a parameter that has a nonscalar value, specify
the element you want to tune using the text box in the dialog box.

### R2020b: Simulink Toolstrip support for dashboard blocks

Starting in R2020b, the **Block** tab in the Simulink Toolstrip turns into a block-specific tab when you select a block in
your model that is from the Dashboard library in the Simulink library or from the Flight Instruments library in the Aerospace Blockset™ Flight Control Analysis library. From the toolstrip, you can connect,
disconnect, and modify connections for the selected block. You can jump to the model
element connected to the selected block, and you can add the selected block to a
panel.

### R2019a: Programmatically add and configure dashboard blocks

Starting in R2019a, you can use functions such as `add_block`
and `set_param` to create and configure blocks from the Dashboard
library in your model.
