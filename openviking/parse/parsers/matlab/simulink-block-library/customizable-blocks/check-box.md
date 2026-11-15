---
type: simulink-block
title: 'Check Box'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customcheckbox'
---

# Check Box

Change parameter or variable value during simulation using check box with customizable appearance

## 中文

在仿真期间使用具有可自定义外观的复选框更改参数或变量值

### 库

Simulink / Dashboard / Customizable Blocks

### 说明

使用 Check Box 模块在仿真前或仿真期间更改所连接的变量或参数的值。当你在 Customizable Blocks 库中使用 Check Box 模块时，可以自定义该模块的外观，例如使该模块看起来像你正在设计的数字用户界面中的复选框。将 Check Box 模块与其他 Dashboard 模块一起使用，为你的模型构建由控件和指示器组成的交互式仪表板。

你可以通过将 Check Box 模块连接到参数，然后选中或清除复选框来更改参数的值。默认情况下，选中复选框会将参数值设置为 `1`，清除复选框会将该值设置为 `0`。要自定义这些值，请打开 Property Inspector 的 **Parameters** 选项卡或 Block Parameters 对话框，然后更改 **Cleared value** 和 **Checked value**。

要在仿真期间选中或清除复选框，请点击 Check Box 模块上的复选框图标。要在仿真未运行时选中或清除复选框，请点击 Check Box 模块以选择该模块，然后点击复选框图标。

**注意**

- 在仿真期间或点击已连接的 Check Box 模块后，双击该模块不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Check Box 模块会同时选择该模块并选中或取消选中复选框。要在不选中或取消选中复选框的情况下选择模块，请按 **Shift**，然后点击该模块。

#### 自定义 Check Box 模块

当你将 Check Box 模块添加到模型中时，该模块已预配置为默认设计。你可以使用采用默认设计的模块，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，你可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，于 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式下，你可以使用模块上方的工具栏来自定义复选框。要访问其他自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式下的 Customizable Check Box 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改标签文本。 | No | Yes |
| 更改标签字体颜色。 | Yes | Yes |
| 上传表示已选中复选框的图标。 | Yes | Yes |
| 上传表示已清除复选框的图标。 | Yes | Yes |
| 更改模块内图标和标签的位置。 | No | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景颜色。 | No | Yes |
| 上传前景图像。 | No | Yes |

**注意**

你在 **Design** 选项卡中做的所有更改——包括在 **Label and Icon** 组件中做的更改——都会同时应用于已清除的复选框和已选中的复选框。例如，当你更改图标宽度时，你会同时更改表示已清除复选框的图标的宽度以及表示已选中复选框的图标的宽度。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，你还可以在画布中交互式地重新定位标签和图标。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要连接到其参数的模块。从出现的列表中，选择要连接到的参数。然后，暂停在 Dashboard 模块上，并点击 Done Connecting 按钮 。

在你更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

你可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

你也可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示如何将 Check Box 模块连接到你的模型。

未连接的 Check Box 模块会连接到 Constant 模块。

#### 参数日志记录

连接到 Dashboard 模块的可调参数会记录到 Simulation Data Inspector，你可以在其中查看参数值以及记录的信号数据。你可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® workspace 中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。

### 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 Dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

### 参数

要设置 Dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### Connection

#### **Connection** — 用于连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。你可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用 toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接，请执行以下操作：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接到其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在你更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

你也可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 以编程方式使用

要以编程方式将 Dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。一些属性适用于将 Dashboard 模块连接到由值定义的参数，另一些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的 Dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数:** `Binding` |
| **类型:** `Simulink.HMI.ParamSourceInfo` |
| **默认:** `[]` |

#### 主要

#### **Check Box Label** — 复选框标签文本 `'Label'`（默认） | string | character array

指定复选框标签的文本。

#### 以编程方式使用

|  |
| --- |
| **模块参数:** `Label` |
| **类型:** string or character vector |
| **默认:** `'Label'` |

#### **Cleared value** — 复选框已清除时所连接参数的值 0（默认） | `scalar`

指定当你清除复选框时分配给所连接参数的值。

#### **Checked value** — 复选框已选中时所连接参数的值 1（默认） | `scalar`

指定当你选中复选框时分配给所连接参数的值。

#### **Label** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

你可以在位于模块顶部或底部的标签中显示 Dashboard 模块所连接元素的名称，也可以隐藏该标签。如果你希望标签可见，请指定标签的位置。如果你不希望标签可见，请选择 `Hide`。

**注意**

当 Dashboard 模块未连接到元素时，标签为空白。

#### 以编程方式使用

|  |
| --- |
| **模块参数:** `LabelPosition` |
| **类型:** character vector |
| **值:** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认:** `'Hide'` |

#### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

在 Simulink 画布中调整模块大小时，选择此参数以保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比，以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当你释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当你释放 **Shift** 键时，宽高比会解锁。

#### Design

要自定义 Dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。你在本节中对参数值所做的更改会同时应用于已清除的复选框和已选中的复选框。

#### Check Box

#### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

在 Simulink 画布中调整模块大小时，选择此参数以保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比，以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。当你释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会锁定宽高比。当你释放 **Shift** 键时，宽高比会解锁。

#### 标签和图标

#### **Text** — 复选框标签文本 `'Label'`（默认） | string | character array

指定复选框标签的文本。

#### 以编程方式使用

|  |
| --- |
| **模块参数:** `Label` |
| **类型:** string or character vector |
| **默认:** `'Label'` |

#### **Color** — 标签字体颜色 `[0 0 0]`（默认） | `[r g b]` vector

从标准颜色调色板中为标签文本选择字体颜色，或指定自定义颜色。

#### **Horizontal Alignment** — 标签和图标对相对于模块的水平对齐 `Left`（默认） | `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。下表列出了 **X Offset** 为零时标签和图标对的水平位置。非零 **X Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

#### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0`（默认） | scalar

**X Offset** 的测量方式取决于 **Horizontal Alignment** 的值。下表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负偏移值会将文本向左移动，正偏移值会将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对的左边缘距模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的水平中点距模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对的右边缘距模块右边缘的水平偏移指定为模块宽度的比例。 |

#### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0`（默认） | `scalar`

指定标签和图标对的垂直中点距模块垂直中点的垂直偏移。相对于偏移为 `0` 时的位置，负偏移值会将文本向上移动，正偏移值会将文本向下移动。

#### **Icon Placement** — 图标相对于标签的位置 `Left`（默认） | `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐。

#### **Icon Offset** — 图标距标签的偏移 scalar

当 **Icon Placement** 设置为 `Left` 或 `Right` 时，将图标距标签的偏移指定为模块宽度的比例。

当 **Icon Placement** 设置为 `Top` 或 `Bottom` 时，将图标距标签的偏移指定为模块高度的比例。

**示例:** `0.5`

#### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例:** `0.5`

#### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例:** `0.5`

#### **Lock Aspect Ratio** — 用于保持图标宽高比的选项 `on (default)` | `off`

在 Simulink 画布中调整图标大小时，选择此参数以保持宽高比。

**示例:** `off`

#### 背景图像

#### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认） | `on`

对于模块背景，你可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例:** `on`

#### **Color** — 模块背景颜色 `[r g b]` vector

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

你也可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 以编程方式使用

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` vector，其值介于 `0` 和 `1` 之间，并格式化为 string 或 character vector。

|  |
| --- |
| **模块参数:** `BackgroundColor` |
| **类型:** string | character vector |
| **值:** `[r g b]` vector |

#### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例:** `0.5`

#### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例:** `0.25`

#### 前景图像

#### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负偏移值会将图像向左移动，正偏移值会将图像向右移动。

**示例:** `1`

#### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘距模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负偏移值会将图像向上移动，正偏移值会将图像向下移动。

**示例:** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例:** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例:** `0.5`

#### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认） | `off`

使用 Property Inspector 调整图像大小时，选择此参数以保持宽高比。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成时会忽略 Dashboard 模块。

### 版本历史

**在 R2024b 中引入**

#### R2025a：在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，你可以与该模块代表的小工具交互。例如，你可以按下按钮或拨动开关。当模块处于非活动状态时，你只能与该模块交互。例如，你可以移动或调整该模块的大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到仪表板面板的模块在面板于其自己的窗口中打开，或已停靠并解锁时，也处于活动状态。如果 Callback Button 模块中由按下按钮触发的至少一个回调具有非空值，则这些模块始终处于活动状态。要与非活动模块代表的小工具交互，你可以通过点击该模块来临时激活它。当你取消选择该模块时，该模块会再次变为非活动状态。

点击活动的 Callback Button 模块，或点击来自 Dashboard 或 Customizable Blocks 库且连接到参数或变量值的活动模块，会同时选择该模块并与该模块代表的小工具交互。例如，点击未选中的活动的已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，你可以通过按 **Shift** 然后点击该模块来选择模块，而无需与小工具交互。类似地，你可以通过按 **Shift** 然后双击该模块来打开 Block Parameters 对话框。

#### R2024b：使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，你可以通过按 **Shift** 临时解锁宽高比。当你释放 **Shift** 键时，宽高比会锁定。

如果宽高比已解锁，按 **Shift** 会临时锁定宽高比。当你释放 **Shift** 键时，宽高比会解锁。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

Use the Check Box block to change the value of the connected variable or
parameter before or during simulation. When you use the Check Box block in the
Customizable Blocks library, you can customize the appearance of the block, for example to
make the block look like a check box in a digital user interface you are designing. Use the
Check Box block with other dashboard blocks to build an interactive dashboard
of controls and indicators for your model.

You can change the value of a parameter by connecting the Check Box block
to the parameter and then checking or clearing the check box. By default, checking the check
box sets the parameter value to `1`, and clearing the check box sets the
value to `0`. To customize these values, open the
**Parameters** tab of the Property Inspector or the Block Parameters dialog
box and change the **Cleared value** and the **Checked
value**.

To check or clear the check box during simulation, click the check box icon on the
Check Box block. To check or clear the check box when the simulation is not
running, click the Check Box block to select the block, then click the check
box icon.

**Note**

- Double-clicking a connected Check Box block during simulation or
  after clicking the block does not open the Block Parameters dialog box. To open the
  Block Parameters dialog box, press **Shift**, then double-click the
  block.
- Clicking a connected Check Box block during simulation both selects
  the block and selects or deselects the check box. To select the block without selecting
  or deselecting the check box, press **Shift**, then click the block.

### Customize Check Box Blocks

When you add a Check Box block to your model, the block is preconfigured
with a default design. You can use the block with the default design or customize the
appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the check box. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Check Box block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the label text. | No | Yes |
| Change the label font color. | Yes | Yes |
| Upload an icon that represents a checked check box. | Yes | Yes |
| Upload an icon that represents a cleared check box. | Yes | Yes |
| Change the position of the icons and label within the block. | No | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

**Note**

All changes you make in the **Design** tab— including changes you
make in the **Label and Icon** component— apply to both, the cleared
check box and the checked check box. For example, when you change the icon width, you
change the width of the of the icon that represents the cleared check box and the width of
the icon that represents the checked check box.

In addition to customizing the block design using the toolbar and
**Design** tab, you can also reposition the label and icon interactively
in the canvas.

When you finish editing the design, to exit design mode, click the
**X** in the upper right of the canvas.

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

This animation shows how to connect the Check Box block to your
model.

An unconnected Check Box block connects to a Constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB® workspace by exporting the parameter data from the Simulation Data Inspector
by using the UI or the `Simulink.sdi.exportRun` function. For more information about exporting
data using the Simulation Data Inspector UI, see Export Data to Workspace or File. The
parameter data is stored in a `Simulink.SimulationData.Parameter` object, accessible as an element in the
exported `Simulink.SimulationData.Dataset`.

## Parameters

Use the Property Inspector and the Block Parameters dialog box
to specify the values of the block parameters. To set the core parameters of the dashboard
block, use the Block Parameters dialog box or the **Parameters** tab in the
Property Inspector. To customize the block, use the **Design** tab in the
Property Inspector. To open the Block Parameters dialog box for a block, double-click the block.
To open the Property Inspector, on the **Modeling** tab, under
**Design**, select **Property Inspector**.

### Parameters

To set the core parameters of the dashboard block, open the
Property Inspector and click the **Parameters** tab.

#### Connection

### **Connection** — Block parameter value to connect parameter value connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink Toolstrip, or the **Connection** table in the Block
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

#### Main

### **Check Box Label** — Check box label text `'Label'` (default) | string | character array

Specify the text of the check box label.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Label` |
| **Type:** string or character vector |
| **Default:** `'Label'` |

### **Cleared value** — Value of connected parameter when check box is cleared 0 (default) | `scalar`

Specify the value that gets assigned to the connected parameter when you clear the
check box.

### **Checked value** — Value of connected parameter when check box is checked 1 (default) | `scalar`

Specify the value that gets assigned to the connected parameter when you check the
check box.

### **Label** — Position of label displaying name of connected element `Hide` (default) | `Bottom` | `Top`

You can display the name of the element to which the dashboard block connects in a
label positioned at the top or bottom of the block, or you can hide the label. If you
want the label to be visible, specify the position of the label. If you do not want the
label to be visible, select `Hide`.

**Note**

When the dashboard block is not connected to an element, the label is
blank.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match the aspect ratio of the background image. When the aspect
ratio is unlocked, adding a new background image does not change the aspect ratio of the
block, but instead changes the aspect ratio of the background image to fit the size of
the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block temporarily unlocks the aspect ratio. When you release the
**Shift** key, the aspect ratio locks. When the aspect ratio is
unlocked, pressing the **Shift** key while resizing a block temporarily
locks the aspect ratio. When you release the **Shift** key, the aspect
ratio unlocks.

### Design

To customize the dashboard block, open the Property
Inspector, click the **Design** tab, and click **Edit**.
Changes you make to the values of the parameters in this section are applied to both the
cleared check box and the checked check box.

#### Check Box

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match that of the background image. When the aspect ratio is
unlocked, adding a new background image does not change the proportions of the block but
instead stretches or scales the background image to fit the size of the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block unlocks the aspect ratio. When you release the **Shift**
key, the aspect ratio locks. When the aspect ratio is unlocked, pressing the
**Shift** key while resizing a block locks the aspect ratio. When you
release the **Shift** key, the aspect ratio unlocks.

#### Label and Icon

### **Text** — Check box label text `'Label'` (default) | string | character array

Specify the text of the check box label.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Label` |
| **Type:** string or character vector |
| **Default:** `'Label'` |

### **Color** — Label font color `[0 0 0]` (default) | `[r g b]` vector

Choose a font color for the label text from the palette of standard colors, or
specify a custom color.

### **Horizontal Alignment** — Horizontal alignment of label and icon pair with block `Left` (default) | `Center` | `Right`

Set the alignment of the label and icon pair in the horizontal direction. The table
lists the horizontal position of the label and icon pair when the **X
Offset** is zero. A nonzero **X Offset** moves the label
and icon pair from the position listed in the table.

| Alignment | Position of the Label and Icon Pair |
| --- | --- |
| `Left` | The left edge of the label and icon pair is at the left edge of the block. |
| `Center` | The horizontal middle of the label and icon pair is at the horizontal middle of the block. |
| `Right` | The right edge of the label and icon pair is at the right edge of the block. |

### **Icon and Label X Offset** — Horizontal offset of icon and label pair from block `0` (default) | scalar

How the **X Offset** is measured depends on the value of the
**Horizontal Alignment**. The table lists how the offset is
measured for each **Horizontal Alignment** value. Relative to the
position when the offset is `0`, an offset with a negative value moves
the text left, and an offset with a positive value moves the text right.

| **Horizontal Alignment** | Offset |
| --- | --- |
| `Left` | Specify the horizontal offset of the left edge of the label and icon pair from the left edge of the block as a ratio of the block width. |
| `Center` | Specify the horizontal offset of the horizontal middle of the label and icon pair from the horizontal middle of the block as a ratio of the block width. |
| `Right` | Specify the horizontal offset of the right edge of the label and icon pair from the right edge of the block as a ratio of the block width. |

### **Icon and Label Y Offset** — Vertical offset of icon and label pair from block `0` (default) | `scalar`

Specify the vertical offset of the vertical middle of the label and icon pair from
the vertical middle of the block. Relative to the position when the offset is
`0`, an offset with a negative value moves the text up, and an
offset with a positive value moves the text down.

### **Icon Placement** — Placement of icon relative to label `Left` (default) | `Top` | `Right` | `Bottom`

Specify the placement of the icon relative to the label.

**Note**

Changing the placement of the icon moves the label, but does not change the offset
or alignment of the label.

### **Icon Offset** — Offset of icon from label scalar

When **Icon Placement** is set to `Left` or
`Right`, specify the offset of the icon from the label as a ratio
of the block width.

When **Icon Placement** is set to `Top` or
`Bottom`, specify the offset of the icon from the label as a ratio
of the block height.

**Example:** `0.5`

### **Icon Width** — Icon width scalar

Specify the icon width as a ratio of the font height of the label text.

**Example:** `0.5`

### **Icon Height** — Icon height scalar

Specify the icon height as a ratio of the font height of the label text.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain icon aspect ratio `on (default)` | `off`

Select this parameter to maintain the aspect ratio when resizing the icon in the
Simulink canvas.

**Example:** `off`

#### Background Image

### **Use Background Color** — Option to specify solid block background color `off` (default) | `on`

For the block background, you can provide a background image or select a solid color.
To select a solid background color, select this parameter. To provide a background
image, clear this parameter.

**Note**

Changing the background color using the **Format** tab of the
Simulink Toolstrip removes the background image and enables the **Use
Background Color** parameter.

**Example:** `on`

### **Color** — Block background color `[r g b]` vector

To use a solid background color, select the **Use Background Color**
parameter. Then, choose a background color from the palette of standard colors, or
specify a custom color.

**Tip**

You can also specify the **Background Color** in the
**Format** tab of the Simulink Toolstrip.

To specify the color of the block text, use the **Font Color**
parameter.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1` that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner Radius** — Corner radius of area with block background color scalar

Specify the corner radius of the area covered by the block background color as a ratio
of half of the smaller of the two block dimensions, width or height.

**Example:** `0.25`

#### Foreground Image

### **X Offset** — Horizontal offset of left edge of foreground image from left edge of block scalar

Specify the horizontal offset of the left edge of the image from the left edge of the
block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of foreground image from top edge of block scalar

Specify the vertical offset of the top edge of the image from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Width** — Foreground image width scalar

Specify the width of the foreground image as a ratio of the block width.

**Example:** `0.5`

### **Height** — Foreground image height scalar

Specify the height of the foreground image as a ratio of the block height.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain foreground image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

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

**Introduced in R2024b**

### R2025a: Select dashboard block and open Block Parameters dialog box during simulation

When a Simulink block from the Dashboard or Customizable Blocks library is
*active*, you can interact with the gadget the block represents. For
example, you can push a button or flip a switch. When a block is inactive, you can only
interact with the block. For example, you can move or resize the block. By default, all
blocks from the Dashboard and Customizable Blocks libraries are active during simulation.
Blocks promoted to a dashboard panel are also active when the panel is open in its own
window or docked and unlocked. Callback Button blocks for which at least one
of the callbacks triggered by pushing the button has a nonempty value are always active. To
interact with the gadget represented by an inactive block, you can temporarily activate a
block by clicking the block. When you deselect the block, the block becomes inactive
again.

Clicking an active Callback Button block or an active block from the
Dashboard or Customizable Blocks library that is connected to a parameter or variable value
both selects the block and interacts with the gadget the block represents. For example,
clicking an unselected active connected Push Button block both selects the
block and pushes the button. Starting in R2025a, you can select the block without
interacting with the gadget by pressing **Shift** and then clicking the block.
Similarly, you can open the Block Parameters dialog box by pressing **Shift**
and then double-clicking the block.

### R2024b: Unlock dashboard block aspect ratio with keyboard

If the aspect ratio of a block from the Dashboard library is locked, you can temporarily
unlock the aspect ratio by pressing **Shift**. When you release the
**Shift** key, the aspect ratio locks.

If the aspect ratio is unlocked, pressing **Shift** temporarily locks the
aspect ratio. When you release the **Shift** key, the aspect ratio
unlocks.
