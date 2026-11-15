---
type: simulink-block
title: 'Dashboard Scope'
family: dashboard
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboardscope'
---

# Dashboard Scope

Trace signals on scope display during simulation

## 中文

仿真期间跟踪示波器显示画面上的信号

### 所属库

Simulink / Dashboard

### 描述

Dashboard Scope 模块在波形视图上绘制仿真过程中的连接信号。您可以将 Dashboard Scope 模块与其他 Dashboard 模块结合使用，为您的模型构建包含各种控件和指示器的交互式仪表板。连接到 Dashboard Scope 模块的信号记录到仿真数据检查器，以便在仿真期间或仿真后进行分析。Dashboard Scope 模块可以显示 Simulink® 支持的任何数据类型的信号，包括枚举数据类型，以及来自数组或总线的多达 8 个信号。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择您要连接的信号。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。要查看 Dashboard 模块显示连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Dashboard Scope 模块连接到您的模型。

An unconnected Dashboard Scope block connects three signals.

#### 分析信号数据

您可以使用 Dashboard Scope 模块的子图菜单或上下文菜单来执行以下操作：

- 显示或隐藏数据游标。
- 按固定量缩小。
- 配置鼠标交互，以进行平移和选择，或在时间轴方向、在 *y* 轴方向或同时在时间轴和 *y* 轴方向进行缩放。
- 在时间轴方向、在 *y* 轴方向或同时在时间轴和 *y* 轴方向执行适应视图操作。

**注意**

要使用键盘快捷方式来分析数据，请在 Dashboard Scope 模块中选择一个信号或轴。

要访问子图菜单，请选择 Dashboard Scope 模块，然后点击在绘图区域上暂停时出现的三个点。

A selected Dashboard Scope block with two cursors displayed and the subplot menu visible.

#### 配置信号线的线型和颜色

您可以使用“模块参数”对话框中的**连接**表或属性检查器来修改连接到 Dashboard Scope 模块的信号的颜色和线型。要修改连接信号的外观，请执行以下操作：

1. 在**连接**表的**线型**列中点击信号外观的预览。

   Line color and style selection menu for a signal connected to a Dashboard Scope block.
2. 从标准调色板中选择一种颜色，或选择**自定义**选项卡，使用 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。
3. 从**线型**列中的实线、点虚线、虚线和点线选项中选择线型。
4. 点击**设置**。

当您将连接到 Dashboard Scope 模块的信号标记为信号记录时，您也可以使用插桩属性对话框配置信号颜色和线型。在 Dashboard Scope 模块的信号颜色和线型菜单中，默认情况下**覆盖线型和颜色**选项处于选中状态，并指定您使用**连接**表为 Dashboard Scope 模块选择的信号外观选项是否覆盖在所连接信号的插桩属性中配置的信号外观选项。

当您使用“模块参数”对话框将信号连接到 Dashboard Scope 模块时，连接表会显示您连接的每个信号的默认信号颜色和线型。当您选择要连接的信号时，**连接**表会更新未选择的信号的线型和颜色，以指示您连接的下一个信号的线型和颜色。

Connection table for a Dashboard Scope block with several options of signals to connect and two signals selected.

#### 配置复信号格式

将复信号连接到 Dashboard Scope 模块时，可以通过指定信号的**复信号格式**属性来配置信号的显示方式：

1. 标记要进行信号记录的复信号。
2. 右键点击复信号的记录标记，然后选择**属性**。
3. 指定**复信号格式**。
4. 点击**确定**。

当您将**复信号格式**指定为**实部-虚部**或**幅值-相位**时，Dashboard Scope 模块将显示信号的两个分量。实部（即幅值）分量使用**连接**表中指示的颜色显示。虚部（即相位）分量是使用在**连接**表中所指示颜色的另一种深度显示。

### 参数

#### 连接表

使用**连接**表选择一个或多个要显示的信号，并配置线型和颜色。

#### **连接** — 要连接和显示的信号 信号连接选项

通过选择模型中的信号来填充**连接**表。要连接信号，请选中您要连接的信号旁边的复选框，然后点击**应用**。有关连接 Dashboard 模块的详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

##### 提示

在仿真期间，您可以将信号连接到 Dashboard Scope 模块。

##### 编程用法

要以编程方式指定一个或多个信号连接到 Dashboard Scope 模块，请使用 `Simulink.HMI.SignalSpecification` 对象的元胞数组。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.SignalSpecification` 对象的元胞数组 |
| **默认值：**`[]` |

#### **线型** — 连接的信号的线型和颜色 线型和颜色选项

您可以使用**连接**表为连接到 Dashboard Scope 模块的信号配置线型和颜色。要更改信号的线型或颜色，请在与信号行对应的**样式**列中，点击信号外观的预览。当**覆盖线型和颜色**处于清除状态时，**样式**列显示文字 `auto`，而不是线型的预览。有关详细信息，请参阅 配置信号线的线型和颜色。

##### 编程用法

要以编程方式为连接的信号配置线型和颜色，请使用 `Colors` 参数。将 `Colors` 参数的值指定为结构体数组，其中每个结构体指定一个信号的样式覆盖设置、线型和线条颜色。使用 `Colors` 参数指定的设置将应用于 `Binding` 参数值中相同索引处的信号。

将每个信号的线型和颜色指定为具有下列字段的结构体：

- `Auto` - 样式覆盖设置由以下各项指定：

  - `"on"` - 线型和颜色由软件自动设置
  - `"off"` - 由 `Color` 和 `LineStyle` 指定的线型和颜色
- `Color` - `1`×`3` `[r g b]` 向量，其值在 `0` 到 `1` 之间。
- `LineStyle` - 字符向量，用于指定下列线型选项之一：

  - 实线：`'-'`
  - 虚线：`'––'`
  - 点线：`':'`
  - 点划线：`'-.'`

```
sigColors1.Color = '';
sigColors1.LineStyle = '';
sigColors1.Auto = "on";
sigColors2.Color = [0 0 1];
sigColors2.LineStyle = '--';
sigColors2.Auto = "off";
sigColors = [sigColors1 sigColors2];

set_param(blockPath,'Colors',sigColors);
```

|  |
| --- |
| **模块参数**：`Colors` |
| **类型：**结构体数组 |

#### 常设

#### **时间跨度** — 时间轴跨度 `auto` (默认) | 标量

有限双精度实数标量值，用于设置绘图的时间范围。

当**时间跨度**设置为 `auto` 时，模块将其时间范围设置为仿真停止时间。

##### 提示

当您将**时间跨度**设置为小于仿真持续时间的值时，请使用**更新模式**参数来控制当仿真时间超过指定的时间跨度时，显示画面是换行还是滚动。

##### 编程用法

|  |
| --- |
| **模块参数**：`TimeSpan` |
| **类型：**字符串 | 字符数组 |
| **值：**`'auto'` 或数值 |
| **默认值：**`'auto'` |

#### **更新模式** — 显示更新行为 `Wrap` (默认) | `Scroll`

显示画面在仿真期间的更新方式，指定为**绕回**或**滚动**。

- `Wrap` - 在仿真时间到达时间跨度结束值后，显示画面通过换行来显示传入的数据。
- `Scroll` - 在仿真时间到达时间跨度结束值后，显示画面通过滚动来显示传入的数据。

##### 编程用法

|  |
| --- |
| **模块参数**：`UpdateMode` |
| **类型：**字符串 | 字符数组 |
| **值**：`'Wrap'` | `'Scroll'` |
| **默认值：**`'Wrap'` |

#### **最小值** — 垂直轴最小值 `-3` (默认) | 标量

有限双精度实数标量值，用于设置垂直轴的最小值。

##### 提示

要在仿真停止后保持由 **Min** 和 **Max** 设置的最小和最大垂直轴范围，请清除**停止时缩放坐标区范围**。

##### 编程用法

要以编程方式为 Dashboard Scope 模块指定 `Min` 参数，请创建一个 `1`×`2` 向量，该向量依次包含最小 *y* 轴值和最大 *y* 轴值。

|  |
| --- |
| **模块参数：**`YLimits` |
| **类型：**`1x2` 向量 |
| **默认值**：`[-3 3]` |

#### **最大值** — 垂直轴最大值 `3` (默认) | 标量

有限双精度实数标量值，用于设置垂直轴的最大值。

##### 提示

要在仿真停止后保持由 **Min** 和 **Max** 设置的最小和最大垂直轴范围，请清除**停止时缩放坐标区范围**。

##### 编程用法

要以编程方式为 Dashboard Scope 模块指定 `Max` 参数，请创建一个 `1`×`2` 向量，该向量依次包含最小 *y* 轴值和最大 *y* 轴值。

|  |
| --- |
| **模块参数：**`YLimits` |
| **类型：**`1x2` 向量 |
| **默认值**：`[-3 3]` |

#### **归一化 y 轴范围** — 归一化 *y* 轴的选项 `off` (默认) | `on`

当启用时，连接的信号数据将归一化，以在 [`0,1`] 的*y* 轴范围内显示。

##### 编程用法

|  |
| --- |
| **模块参数**：`NormalizeYAxis` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

#### **停止时缩放坐标区范围** — 仿真停止时执行适应视图的选项 `on` (默认) | `off`

当启用时，在仿真停止时会对绘图中显示的数据执行适应视图大小操作。

##### 编程用法

|  |
| --- |
| **模块参数**：`ScaleAtStop` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **显示 "双击以连接" 消息** — 连接说明可见性 `on` (默认) | `off`

当启用时，如果模块未连接，则显示说明文本。当模块未连接时，您可以将此参数指定为 `off` 以隐藏文本。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowInitialText` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### 显示

#### **刻度** — 坐标轴刻度位置 **外部** (默认) | **内部** | **无**

坐标轴刻度位置，指定为**外部**、**内部**或**无**。

- **外部** - 刻度绘制在 *x* 和 *y* 坐标轴的外侧。
- **内部** - 刻度绘制在 *x* 和 *y* 坐标轴的内侧。
- **无** - 在 *x* 或 *y* 坐标轴上不显示刻度。

##### 编程用法

|  |
| --- |
| **模块参数**：`TicksPosition` |
| **类型：**字符串 | 字符向量 |
| **值**：`'Outside'` | `'Inside'` | `'None'` |
| **默认值：**`'Outside'` |

#### **刻度标签** — 刻度标签可见性 **全部** (默认) | **T 轴** | **Y 轴** | **无**

*x* 和 *y* 轴上刻度标签的可见性。

- **全部** - *x* 和 *y* 轴上均显示刻度标签。
- **T 轴** - 仅 *x* 轴上显示刻度标签。
- **Y 轴** - 仅 *y* 轴上显示刻度标签。
- **无** - *x* 和 *y* 轴上均不显示刻度标签。

##### 编程用法

|  |
| --- |
| **模块参数**：`TickLabels` |
| **类型：**字符串 | 字符向量 |
| **值**：`'All'` | `'T-Axis'` | `'Y-Axis'` | `'None'` |
| **默认值**：`'All'` |

#### **图例** — 图例位置 **顶端** (默认) | **右侧** | **内部顶端** | **内部右侧** | **隐藏**

您可以将图例放置在图的顶部（绘图区域的内侧或外侧均可）或图的右侧（绘图区域的内侧或外侧均可）。也可以隐藏图例。图例显示为信号名称旁边的每个连接信号选择的颜色。

##### 编程用法

|  |
| --- |
| **模块参数**：`LegendPosition` |
| **类型：**字符串 | 字符向量 |
| **值：** `'Top'` | `'Right'` | `'InsideTop'` | `'InsideRight` | `'Hide'` |
| **默认值**：`'Top'` |

#### **水平** — 水平网格线可见性 **on** (默认) | **off**

水平网格线的可见性。

- **on** - Dashboard Scope 上显示水平网格线。
- **off** - Dashboard Scope 上不显示水平网格线。

##### 编程用法

|  |
| --- |
| **模块参数**：`Grid` |
| **类型：**字符串 | 字符向量 |
| **值**：`'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **默认值**：`'All'` |

#### **垂直** — 垂直网格线可见性 **on** (默认) | **off**

垂直网格线的可见性。

- **on** - Dashboard Scope 上显示垂直网格线。
- **off** - Dashboard Scope 上不显示垂直网格线。

##### 编程用法

|  |
| --- |
| **模块参数**：`Grid` |
| **类型：**字符串 | 字符向量 |
| **值**：`'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **默认值**：`'All'` |

#### **边框** — 绘图边框可见性 **on** (默认) | **off**

绘图边框可见性。

- **on** - Dashboard Scope 上显示绘图边框。
- **off** - Dashboard Scope 上不显示绘图边框。

##### 编程用法

|  |
| --- |
| **模块参数**：`Border` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **标记** — 显示信号数据标记的选项 **off** (默认) | **on**

当启用时，对在 Dashboard Scope 上绘制的信号显示数据标记。

##### 编程用法

|  |
| --- |
| **模块参数**：`Markers` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

#### 样式

#### **前景颜色** — 网格线颜色 `[r g b]` 向量

从标准颜色调色板中选择网格线的颜色，或使用 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

##### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型：**字符串 | 字符向量 |
| **值：**`[r g b]` 向量 |

#### **背景颜色** — 绘图区域颜色 `[r g b]` 向量

从标准颜色调色板中选择绘图区域的颜色，或使用 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

##### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型：**字符串 | 字符向量 |
| **值：**`[r g b]` 向量 |

#### **字体颜色** — 刻度和刻度标签颜色 `[r g b]` 向量

从标准颜色调色板中选择刻度和刻度标签的颜色，或使用 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

##### 编程用法

将模块的 `FontColor` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 到 `1` 之间。

|  |
| --- |
| **模块参数**：`FontColor` |
| **类型：**`[r g b]` 向量 |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

### 版本历史记录

**在 R2015a 中推出**

## Libraries

Simulink / Dashboard

## Description

The Dashboard Scope block plots connected signals during simulation on
a scope display. You can use the Dashboard Scope block with other
dashboard blocks to build an interactive dashboard of controls and indicators for your
model. Signals connected to the Dashboard Scope block log to the
Simulation Data Inspector for analysis during or after simulation. The Dashboard
Scope block can display signals of any data type that Simulink® supports, including enumerated data types, and up to eight signals from an
array or bus.

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard block,
use connect mode. To enter connect mode on an unconnected block, pause on the block you want
to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a display block to a signal in your model or change the connection of a display
block, enter connect mode. Select the signal line to which you want to connect. From the
list that appears, select the signal to which you want to connect. Then, pause on the
dashboard block and click the Done Connecting button . To see the dashboard block display the value of the
connected block, run the simulation.

For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

This animation shows how to connect the Dashboard Scope block to
your model.

An unconnected Dashboard Scope block connects three signals.

### Analyze Signal Data

You can use the subplot menu or the context menu for the Dashboard
Scope block to:

- Show or hide data cursors.
- Zoom out by a fixed amount.
- Configure the mouse interaction to pan and select or to zoom in time,
  in *y*, or in both time and
  *y*.
- Perform a fit-to-view in time, in *y*, or in both
  time and *y*.

**Note**

To use keyboard shortcuts to analyze data, select a signal or axis in the
Dashboard Scope block.

To access the subplot menu, select the Dashboard Scope block then
click the three dots that appear when you pause on the plot area.

A selected Dashboard Scope block with two cursors displayed and the subplot menu visible.

### Configure Signal Line Style and Color

You can modify the color and line style for signals connected to a
Dashboard Scope block using the **Connection**
table in the Block Parameters dialog box or the Property Inspector. To modify the
appearance of a connected signal:

1. Click the preview of the signal appearance in the
   **Style** column of the
   **Connection** table.

   Line color and style selection menu for a signal connected to a Dashboard Scope block.
2. Choose a color from the palette of standard colors or select the
   **Custom** tab to specify a custom color using
   `RGB` values between `0` and
   `255`.
3. Select the line style from the solid, dotted, dashed, and dot-dashed
   options in the **Style** column.
4. Click **Set**.

When you mark a signal connected to the Dashboard Scope block for
signal logging, you can also configure the signal color and line style using the
Instrumentation Properties dialog box. In the signal color and line
style menu for the Dashboard Scope block, the **Override
style and color** option is selected by default and specifies whether
signal appearance options you choose using the **Connection** table
for the Dashboard Scope block override signal appearance options
configured in the instrumentation properties for the connected signals.

When you connect signals to the Dashboard Scope block using the
Block Parameters dialog box, the connection table shows the default signal color and
line style for each signal you connect. As you select signals to connect, the
**Connection** table updates the style and color for signals
that are not selected to indicate the style and color for the next signal you connect.

Connection table for a Dashboard Scope block with several options of signals to connect and two signals selected.

### Configure Complex Signal Format

When you connect a complex signal to the Dashboard Scope block, you
can configure how the signal is displayed by specifying the **Complex
Format** property for the signal:

1. Mark the complex signal for signal logging.
2. Right-click the logging badge for the complex signal and select
   **Properties**.
3. Specify the **Complex Format**.
4. Click **OK**.

When you specify the **Complex Format** for a signal as
`Real-Imaginary` or
`Magnitude-Phase`, the Dashboard Scope
block displays both components of the signal. The real or magnitude component is
displayed using the color indicated in the **Connection** table.
The imaginary or phase component is displayed using a different shade of the color
indicated in the **Connection** table.

## Parameters

### Connection Table

Use the **Connection** table to select one or more signals to
display and to configure the line style and color.

### **Connection** — Signals to connect and display signal connection options

Populate the **Connection** table by selecting
signals in the model. To connect a signal, select the check box next to
the signal you want to connect, then click **Apply**.
For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

#### Tips

You can connect signals to a Dashboard Scope block
during simulation.

#### Programmatic Use

To programmatically specify one or more signals to connect to the
Dashboard Scope block, use a cell array of
`Simulink.HMI.SignalSpecification` objects.

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** cell array of `Simulink.HMI.SignalSpecification` objects |
| **Default:** `[]` |

### **Line Style** — Line style and color for connected signals line style and color options

You can configure the line style and color for signals connected to a
Dashboard Scope block using the
**Connection** table. To change the line style or
color for a signal, in the **Style** column that
corresponds to the signal row, click the preview of the signal
appearance. When **Override style and color** is
cleared, the **Style** column displays the word
`auto` instead of a preview of the line style. For
more information, see Configure Signal Line Style and Color.

#### Programmatic Use

To programmatically configure the line style and color for
connected signals, use the `Colors` parameter.
Specify the value for the `Colors` parameter as an
array of structures where each structure specifies the style
override setting, line style, and line color for one signal.
Settings specified using the `Colors` parameter
apply to the signal at the same index in the value for the
`Binding` parameter.

Specify the line style and color for each signal as a structure
with these fields:

- `Auto` — Style override setting
  specified by:

  - `"on"` — Line style and
    color automatically set by the software
  - `"off"` — Line style and
    color specified by `Color` and
    `LineStyle`
- `Color` —
  `1`-by-`3`
  `[r g b]` vector with values between
  `0` and
  `1`.
- `LineStyle` — Character vector that
  specifies one of these line style options:

  - Solid: `'-'`
  - Dashed: `'––'`
  - Dotted: `':'`
  - Dash-dotted: `'-.'`

```
sigColors1.Color = '';
sigColors1.LineStyle = '';
sigColors1.Auto = "on";
sigColors2.Color = [0 0 1];
sigColors2.LineStyle = '--';
sigColors2.Auto = "off";
sigColors = [sigColors1 sigColors2];

set_param(blockPath,'Colors',sigColors);
```

|  |
| --- |
| **Block Parameter:** `Colors` |
| **Type:** array of structures |

### Main

### **Time Span** — Time axis span `auto` (default) | scalar

A finite, real, double, scalar value that sets the time span of the
plot.

When **Time Span** is set to `auto`,
the block sets its time span to the simulation stop time.

#### Tips

When you set the **Time Span** to a value that is
less than the duration of the simulation, use the **Update
Mode** parameter to control whether the display wraps
or scrolls when the simulation time exceeds the specified time
span.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeSpan` |
| **Type:** string | character array |
| **Values:** `'auto'` or numeric value |
| **Default:** `'auto'` |

### **Update Mode** — Display update behavior `Wrap` (default) | `Scroll`

How the display updates during simulation, specified as
`Wrap` or
`Scroll`.

- `Wrap` — Display wraps to show incoming
  data after simulation time reaches end of time span.
- `Scroll` — Display scrolls to show
  incoming data after simulation time reaches end of time
  span.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UpdateMode` |
| **Type:** string | character array |
| **Values:** `'Wrap'` | `'Scroll'` |
| **Default:** `'Wrap'` |

### **Min** — Vertical axis minimum `-3` (default) | scalar

A finite, real, double, scalar value that sets the minimum of the
vertical axis.

#### Tips

To maintain the minimum and maximum vertical axis limits set by
**Min** and **Max** after the
simulation stops, clear **Scale axes limits at
stop**.

#### Programmatic Use

To specify the `Min` parameter for the
Dashboard Scope block programmatically, create a
`1`-by-`2` vector that
contains the minimum *y*-axis value and maximum
*y*-axis value, in that order.

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** `1x2` vector |
| **Default:** `[-3 3]` |

### **Max** — Vertical axis maximum `3` (default) | scalar

A finite, real, double, scalar value that sets the maximum of the
vertical axis.

#### Tips

To maintain the minimum and maximum vertical axis limits set by
**Min** and **Max** after the
simulation stops, clear **Scale axes limits at
stop**.

#### Programmatic Use

To specify the `Max` parameter for the
Dashboard Scope block programmatically, create a
`1`-by-`2` vector that
contains the minimum *y*-axis value and maximum
*y*-axis value, in that order.

|  |
| --- |
| **Block Parameter:** `YLimits` |
| **Type:** `1x2` vector |
| **Default:** `[-3 3]` |

### **Normalize y-axis limits** — Option to normalize *y*-axis `off` (default) | `on`

When enabled, the connected signal data is normalized to display on a
*y*-axis range of [`0,1`].

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NormalizeYAxis` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Scale axes limits at stop** — Option to perform fit-to-view upon simulation stop `on` (default) | `off`

When enabled, performs a fit-to-view operation on the data displayed
in the plot when the simulation stops.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleAtStop` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Show "Double-click to connect" message** — Connection instructions visibility `on` (default) | `off`

When enabled, shows instructional text if the block is not connected.
When the block is not connected, you can specify this parameter as
`off` to hide the text.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInitialText` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### Display

### **Ticks** — Axes tick positions `Outside` (default) | `Inside` | `None`

Axes tick positions, specified as `Outside`,
`Inside`, or
`None`.

- `Outside` — Ticks are drawn on
  the outside of the *x*- and
  *y*-axes.
- `Inside` — Ticks are drawn on the
  inside of the *x*- and
  *y*-axes.
- `None` — No ticks are shown on
  the *x*- or
  *y*-axes.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TicksPosition` |
| **Type:** string | character vector |
| **Values:** `'Outside'` | `'Inside'` | `'None'` |
| **Default:** `'Outside'` |

### **Tick Labels** — Tick label visibility `All` (default) | `T-Axis` | `Y-Axis` | `None`

Visibility of tick labels on the *x*- and
*y*-axes.

- `All` — Ticks labels are shown on
  the *x*- and
  *y*-axes.
- `T-Axis` — Tick labels are shown
  on the *x*-axis only.
- `Y-Axis` — Tick labels are shown
  on the *y*-axis only.
- `None` — No tick labels are shown
  on the *x*- or
  *y*-axis.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TickLabels` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'T-Axis'` | `'Y-Axis'` | `'None'` |
| **Default:** `'All'` |

### **Legend** — Legend position `Top` (default) | `Right` | `Inside top` | `Inside right` | `Hide`

You can position the legend at the top of the plot inside or outside
the plot area or on the right of the plot inside or outside the plot
area. You can also hide the legend. The legend shows the color chosen
for each connected signal next to the signal name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LegendPosition` |
| **Type:** string | character vector |
| **Values:** `'Top'` | `'Right'` | `'InsideTop'` | `'InsideRight` | `'Hide'` |
| **Default:** `'Top'` |

### **Horizontal** — Horizontal grid line visibility `on` (default) | `off`

Visibility of horizontal grid lines.

- `on` — Horizontal grid lines are
  visible on Dashboard Scope.
- `off` — Horizontal grid lines are
  not shown on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Grid` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **Default:** `'All'` |

### **Vertical** — Vertical grid line visibility `on` (default) | `off`

Visibility of vertical grid lines.

- `on` — Vertical grid lines are
  visible on Dashboard Scope.
- `off` — Vertical grid lines are
  not shown on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Grid` |
| **Type:** string | character vector |
| **Values:** `'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **Default:** `'All'` |

### **Border** — Plot border visibility `on` (default) | `off`

Plot border visibility.

- `on` — Plot border is shown on
  Dashboard Scope.
- `off` — Plot border is not shown
  on Dashboard Scope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Border` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Markers** — Option to show signal data markers `off` (default) | `on`

When enabled, data markers are shown for signals plotted on the
Dashboard Scope block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Markers` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### Style

### **Foreground Color** — Grid lines color `[r g b]` vector

Select the color for the grid lines from a palette of standard colors
or specify a custom color using `RGB` values between
`0` and `255`.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the
block as a string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Background Color** — Plot area color `[r g b]` vector

Select the color for the plot area from a palette of standard colors
or specify a custom color using `RGB` values between
`0` and `255`.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the
block as a string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Font Color** — Ticks and tick labels color `[r g b]` vector

Select the color for the ticks and tick labels from a palette of
standard colors or specify a custom color using `RGB`
values between `0` and `255`.

#### Programmatic Use

Specify the `FontColor` parameter for the block
as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `FontColor` |
| **Type:** `[r g b]` vector |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2015a**
