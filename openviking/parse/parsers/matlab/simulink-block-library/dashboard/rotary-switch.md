---
type: simulink-block
title: 'Rotary Switch'
family: dashboard
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'rotaryswitch'
---

# Rotary Switch

Switch parameter to set values on dial

## 中文

切换旋钮开关所设置的参数值

### 库

Simulink / Dashboard

### 描述

Rotary Switch 在仿真期间将所连接模块参数的值更改为多个指定值。例如，您可以将 Rotary Switch 模块连接到模型中输入信号的 amplitude 或 frequency，并在仿真期间更改其特性。将 Rotary Switch 模块与其他 Dashboard 模块一起使用，以创建交互式 dashboard 来控制您的模型。

在仿真期间且选中该模块时，双击 Rotary Switch 模块不会打开其对话框。要编辑模块的参数，可以使用 **Property Inspector**，或者右键单击该模块，然后从上下文菜单中选择 **Block Parameters**。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用 connect mode。要在未连接的模块上进入 connect mode，请将鼠标悬停在要连接的模块上，然后单击 Connect 按钮 。要在已连接的模块上进入 connect mode，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入 connect mode。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，将鼠标悬停在 dashboard 模块上，并单击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。若要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Rotary Switch 模块连接到您的模型。

未连接的 Rotary Switch 模块连接到 Gain 模块的 Gain 参数。

#### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。

### 参数

#### **Connection** — 要连接的模块参数值 parameter value connection options

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用 connect mode、Simulink® Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧单击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关 connect mode 以及如何使用 toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块到具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在该表中，选择要连接到的参数。
5. 单击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。若要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 dashboard 模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### Programmatic Use

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将 dashboard 模块连接到由值定义的参数，有些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

#### **States** — 位置标签和值 scalar and character vector

要分配给所连接变量或参数的数值对，并带有用于该模块的标签。一个 State 由一个 **State Value** 和一个 **State Label** 组成。

- **State Value** — 当 Rotary Switch 模块位于对应 **State Label** 时，分配给所连接变量或参数的值。
- **State Label** — 开关位置的标签。您可以使用 **State Label** 显示当 Rotary Switch 模块指向 **State Label** 时所连接变量或参数采用的值，也可以使用描述性文本标签。

单击 **+** 按钮以添加 **States**。

该模块的默认配置包含以下 **States**：

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |

#### Programmatic Use

要以编程方式配置该模块的 **States**，请将 `States` 参数的值指定为具有以下字段的结构体数组：

- `Value` — 该状态的标量 double 值。
- `Label` — 要用作开关位置标签的字符串或字符数组。

为要对该模块指定的每个状态在数组中包含一个结构体元素。

```
state1.Value = 1;
state1.Label = 'State 1';
state2.Value = 2;
state2.Label = 'State 2';
states = [state1 state2];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** structure array |

#### **Enumerated Data Type** — 使用枚举数据类型指定状态值和标签 `off` (default) | `on`

您可以使用枚举数据类型，该类型将数值与每个枚举配对，以配置该模块的状态值和标签。要使用枚举数据类型为该模块指定状态，请先选择 **Enumerated Data Type** 选项。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB path 或 base workspace 中。

**Example:** `myEnumType`

#### Programmatic Use

要使用枚举数据类型以编程方式为该模块指定状态标签和值，请为 `UseEnumeratedDataType` 参数指定 `'on'`，并为 `EnumeratedDataType` 参数指定枚举数据类型的名称。

|  |
| --- |
| **Block Parameter:** `UseEnumeratedDataType` |
| **Type:** string or character array |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `EnumeratedDataType` |
| **Type:** string or character array |
| **Default:** `''` |

#### **Label** — 模块标签位置 `Top` (default) | `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接元素的名称。

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

### 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

#### 版本历史记录

**Introduced in R2015a**

#### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，单击 **Open In New Window** 按钮 。

您可以独立于模型窗口，最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和逐步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中，单击 **Open in canvas** 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

#### R2023a: Simulink Toolstrip 中的持久 Panels 选项卡

当您将 dashboard 面板添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时，**Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

#### R2022b: 面板中可自定义 dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 单击该面板或该面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷方式基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

#### R2022b: 面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您单击面板中的 dashboard 模块时，该模块的 toolstrip 选项卡会出现。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在 toolstrip 中。

当您单击面板时，**Panel** 选项卡会出现在 toolstrip 中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2021a: 使用 dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将 dashboard 模块连接到可调参数时，您首先选择一个或多个模块。然后，在对话框中，选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调节的元素。

#### R2020b: dashboard 模块的 Simulink Toolstrip 支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink Toolstrip 中的 **Block** 选项卡会变为特定于模块的选项卡。在 toolstrip 中，您可以连接、断开连接和修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并可以将所选模块添加到面板。

#### R2019b: Rotary Switch 模块和 Combo Box 模块的增强枚举数据类型支持

从 R2019b 开始，您可以使用枚举类来配置 Rotary Switch 模块和 Combo Box 模块的状态值和标签。

要使用枚举数据类型配置 Rotary Switch 或 Combo Box 模块的 **States**，请选择 **Enumerated Data Type**。在文本框中，输入要使用的枚举类的名称。

当您使用枚举类配置模块的状态时，无法从 **States** 表中手动编辑、添加或移除状态。

#### R2019a: 以编程方式添加和配置 dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## Libraries

Simulink / Dashboard

## Description

The Rotary Switch changes the value of the connected block parameter to
several specified values during simulation. For example, you can connect the
Rotary Switch block to the amplitude or frequency of an input signal
in your model and change its characteristics during simulation. Use the Rotary
Switch block with other Dashboard blocks to create an interactive dashboard
to control your model.

Double-clicking the Rotary Switch block does not open its dialog box
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

This animation shows how to connect the Rotary Switch block to your
model.

An unconnected Rotary Switch block connects to the Gain parameter of a Gain block.

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

### **States** — Position labels and values scalar and character vector

Pairs of numeric values to assign to the connected variable or parameter
with labels for the block. A State consists of a **State
Value** and a **State Label**.

- **State Value** — Value assigned to the
  connected variable or parameter when the Rotary
  Switch block is positioned at the corresponding
  **State Label**.
- **State Label** — Label for the switch
  position. You can use the **State Label** to
  display the value the connected variable or parameter takes when
  the Rotary Switch block points to the
  **State Label**, or you can use a
  descriptive text label.

Click the **+** button to add
**States**.

The default configuration for the block includes these
**States**:

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |

#### Programmatic Use

To configure the **States** for the block
programmatically, specify the value of the `States`
parameter as a structure array with fields:

- `Value` — Scalar double value for the
  state.
- `Label` — String or character array to
  use as the label for the switch position.

Include a structure element in the array for each state you want to
specify for the block.

```
state1.Value = 1;
state1.Label = 'State 1';
state2.Value = 2;
state2.Label = 'State 2';
states = [state1 state2];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** structure array |

### **Enumerated Data Type** — Specify state values and labels using an enumerated data type `off` (default) | `on`

You can use an enumerated data type that pairs a numeric value with each enumeration to configure the state values and labels for the block. To specify the states for the block using an enumerated data type, first select the **Enumerated Data Type** option. Then, specify the name of the enumerated data type in the text box. The definition for the specified enumerated data type must be saved on the MATLAB path or in the base workspace.

**Example:** `myEnumType`

#### Programmatic Use

To programmatically specify the state labels and values for the block using an enumerated data type, specify `'on'` for the `UseEnumeratedDataType` parameter and the name of the enumerated data type for the `EnumeratedDataType` parameter.

|  |
| --- |
| **Block Parameter:** `UseEnumeratedDataType` |
| **Type:** string or character array |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `EnumeratedDataType` |
| **Type:** string or character array |
| **Default:** `''` |

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

### R2019b: Enhanced enumerated data type support for the Rotary Switch block and Combo Box block

Starting in R2019b, you can use an enumeration class to configure the values and
labels for the states of a Rotary Switch block and a Combo
Box block.

To configure the **States** for a Rotary
Switch or Combo Box block with an enumerated data type,
select **Enumerated Data Type**. In the text box, enter
the name of the enumeration class you want to use.

When you use an enumeration class to configure the states of the block, you cannot
manually edit, add, or remove states from the **States**
table.

### R2019a: Programmatically add and configure dashboard blocks

Starting in R2019a, you can use functions such as `add_block`
and `set_param` to create and configure blocks from the Dashboard
library in your model.
