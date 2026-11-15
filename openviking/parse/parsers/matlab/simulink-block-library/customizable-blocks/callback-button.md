---
type: simulink-block
title: 'Callback Button'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customcallbackbutton'
---

# Callback Button

Execute MATLAB code using button with customizable appearance

## 中文

使用具有可自定义外观的按钮执行 MATLAB 代码

### 库

Simulink / Dashboard / Customizable Blocks

### 说明

Callback Button 模块响应点击（立即释放指针）或按下（延迟释放指针）运行 MATLAB® 代码。你可以为点击指定与按下不同的代码。
当你按下按钮时，代码要么在指定的时间跨度后执行，要么按你指定的时间间隔执行。你可以自定义 Callback Button 模块的外观，使其看起来像真实系统中的按钮。将 Callback Button 模块与其他 dashboard 模块一起使用，创建交互式 dashboard 来控制模型。

当 Callback Button 模块处于 *活动* 状态时，你可以与该模块表示的小工具交互。点击活动的 Callback Button 模块会按下虚拟按钮。当你按住指针时，按钮被按下。当你释放指针时，按钮被释放。Callback Button 模块在以下情况下处于活动状态：仿真正在运行，模块位于在其自己的窗口中打开或已停靠且未锁定的面板中，或者由点击或按下触发的至少一个回调具有非空值。要选择活动的 Callback Button 模块而不按下按钮，请按 **Shift**，然后单击该模块。要打开活动的 Callback Button 模块的 Block Parameters 对话框，请按 **Shift**，然后双击该模块。

当模块处于非活动状态时，你只能与该模块交互，例如执行调整大小或拖动模块等操作。要临时激活非活动的 Callback Button 模块，请点击该模块。当取消选择 Callback Button 模块时，该模块会再次变为非活动状态。

使用回调函数指定按下按钮时要执行的操作：

- `PressFcn` 函数在按钮被按下时运行。你可以将按钮配置为在按钮被按下时仅运行一次 `PressFcn` 函数，也可以指定重复间隔。要仅运行一次函数，请将重复间隔指定为 `0`。
- `ClickFcn` 函数在释放按钮时运行。

你可以通过将 **Button Type** 设置为 `Latched` 来配置按钮在释放指针后保持按下状态。当你选择锁存按钮类型时：

- 要锁存按钮，请点击按钮。
- 要取消锁存按钮，请再次点击按钮。

`PressFcn` 函数在按钮被锁存时运行。`ClickFcn` 函数在锁存按钮时运行一次，并在取消锁存按钮时运行一次。

你可以使用状态来指定 Callback Button 模块的外观在你与按钮交互时如何变化：

- 当你按下按钮时，模块处于 `Pressed` 状态。
- 当按钮被锁存且你未按下它时，模块处于 `Latched` 状态。
- 当按钮被锁存且你正在按下它时，模块处于 `Latched and Pressed` 状态。
- 当模块不处于这三种状态中的任何一种时，它处于 `Default` 状态。

一个状态将指针操作与以下内容配对：

- 状态标签
- 状态图标
- 状态图像

#### 自定义 Callback Button 模块

当你将 Callback Button 模块添加到模型时，该模块预配置了默认设计。你可以使用默认设计使用该模块，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，你可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，在 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮。

在设计模式下，你可以使用模块上方的工具栏来自定义 callback button。要访问其他自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的可自定义 Callback Button 模块，工具栏和 Property Inspector 中的 Design 选项卡可见。

当你自定义 Callback Button 模块时，你为每个状态配置模块外观。当你将 **Block Type** 配置为 `Momentary` 时，模块有两个状态。当你将 **Block Type** 配置为 `Latch` 时，模块有四个状态。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。

**自定义所选状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 指定状态标签文本。 | 否 | 是 |
| 指定状态标签文本的颜色和不透明度。 | 是 | 是 |
| 上传状态图像。 | 是 | 是 |
| 上传状态图标。 | 是 | 是 |
| 更改状态图像和状态图标的大小。 | 否 | 是 |
| 更改状态标签、状态图像和状态图标的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，你还可以在画布中交互式调整组件大小和重新定位。要调整特定于某个状态的组件（例如状态图像）的大小，请在工具栏中选择该状态，然后调整组件的大小或重新定位。

**适用于所有状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传背景图像。 | 否 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，在 **Design** 下，选择 **Property Inspector**。

### 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector 并点击 **Parameters** 选项卡。

#### 主要

#### **Button Type** — 按钮对点击的响应 `Momentary`（默认）| `Latch`

指定模块如何响应点击。

- `Momentary` — 按钮仅在按下时改变状态。当你释放点击时，按钮返回其默认状态。
- `Latch` — 按钮在点击时锁存状态变化。按钮保持按下状态，直到你再次点击它。

当你将 **Button Type** 配置为 `Momentary` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

当你将 **Button Type** 配置为 `Latch` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当你释放点击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当你释放点击时，模块过渡到 `Default` 状态。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `ButtonType` |
| **Type:** string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

#### **Button Text** — 按钮标签文本 `'Callback Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于在 **Design** 选项卡上的 **States** 组件的 **Select State** 部分中选择的状态对应的按钮。

#### 程序化使用

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

#### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比被锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比被锁定时，在调整模块大小时按下 **Shift** 键会临时解锁宽高比。当你释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按下 **Shift** 键会临时锁定宽高比。当你释放 **Shift** 键时，宽高比解锁。

#### 回调

#### **ClickFcn** — 响应点击执行的 MATLAB 代码 MATLAB code

响应按钮点击执行的 MATLAB 代码。

每次点击按钮时，`ClickFcn` 代码执行一次，执行时间为释放点击的时间点。

要为 `ClickFcn` 指定代码，请从下拉菜单中选择 `ClickFcn`。在菜单下方的文本框中输入代码。

#### 程序化使用

将模块的 `ClickFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **Block Parameter:** `ClickFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

#### **PressFcn** — 响应按下执行的 MATLAB 代码 MATLAB code

响应按钮按下执行的 MATLAB 代码。

当按钮处于按下状态时，`PressFcn` 代码在 **Press Delay** 时间过去后执行一次，然后每隔 **Repeat Interval** 周期性执行。

要为 `PressFcn` 指定代码，请从下拉菜单中选择 `PressFcn`。在菜单下方的文本框中输入代码。

你按下按钮以执行 `PressFcn` 代码的方式取决于 **Button Type**。

- 如果 **Button Type** 为 `Momentary`，请按住点击达到你想要按下按钮的持续时间。
- 如果 **Button Type** 为 `Latch`，请点击以按下按钮，但不要按住点击。按钮保持按下状态，直到你再次点击它。

**注意**

每次点击按钮时，即使你这样做是按下按钮过程的一部分，`ClickFcn` 代码也会执行一次，执行时间为释放点击的时间点。

#### 程序化使用

将模块的 `PressFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **Block Parameter:** `PressFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

#### **Press Delay (ms)** — 按住按钮以触发按下的时间 `500`（默认）| scalar

使 `PressFcn` 代码执行所需的时间量。

#### 依赖项

**Press Delay (ms)** 仅在 `PressFcn` 被选择为回调时可见。

#### 程序化使用

将模块的 `PressDelay` 参数指定为正标量值。

|  |
| --- |
| **Block Parameter:** `PressDelay` |
| **Type:** scalar |

#### **Repeat Interval (ms)** — 重复 `PressFcn` 代码的时间间隔 `0`（默认）| scalar

如果 Callback Button 模块仍被按下，`PressFcn` 代码再次执行之后的时间间隔。

#### 依赖项

**Repeat Interval (ms)** 仅在 `PressFcn` 被选择为回调时可见。

#### 程序化使用

将模块的 `RepeatInterval` 参数指定为正标量值。

|  |
| --- |
| **Block Parameter:** `RepeatInterval` |
| **Type:** scalar |

#### 设计

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### 按钮

#### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比被锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比被锁定时，在调整模块大小时按下 **Shift** 键会解锁宽高比。当你释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按下 **Shift** 键会锁定宽高比。当你释放 **Shift** 键时，宽高比解锁。

#### 状态

#### **Select State** — 选择要配置的状态 `Default`（默认）| `Pressed` | `Latched` | `Latched and Pressed`

从 **States** 组件的 **Select State** 部分的下拉菜单中选择要配置的状态。当 **Button Type** 为 `Momentary` 时，你可以选择以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

当 **Button Type** 为 `Latch` 时，你可以选择以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当你释放点击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当你释放点击时，模块过渡到 `Default` 状态。

**注意**

你可以为某个状态配置 **Design** 选项卡的 **States** 组件中的所有参数。例如，你可以选择当按钮处于该状态时显示在按钮上的图标。当你配置 **States** 组件中的任何参数时，更改将应用于 **States** 组件的 **Select State** 部分中选择的状态。

**示例:** `Pressed`

#### **Text** — 按钮标签文本 `'Callback Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于在 **Design** 选项卡上的 **States** 组件的 **Select State** 部分中选择的状态对应的按钮。

#### 程序化使用

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

#### **Color** — 标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择标签文本的字体颜色，或指定自定义颜色。该颜色应用于在 **Design** 选项卡上的 **States** 组件的 **Select State** 部分中选择的状态的标签文本。

#### **Horizontal Alignment** — 标签和图标对与模块的水平对齐 `Left`（默认）| `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。下表列出了当 **X Offset** 为零时标签和图标对的水平位置。非零 **X Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

#### **Vertical Alignment** — 标签和图标对与模块的垂直对齐 `Center`（默认）| `Bottom` | `Top`

设置标签和图标对在垂直方向上的对齐方式。下表列出了当 **Y Offset** 为零时标签和图标对的垂直位置。非零 **Y Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Top` | 标签和图标对的顶边缘位于模块的顶边缘。 |
| `Center` | 标签和图标对的垂直中点位于模块的垂直中点。 |
| `Bottom` | 标签和图标对的底边缘位于模块的底边缘。 |

#### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0`（默认）| scalar

**X Offset** 的测量方式取决于 **Horizontal Alignment** 的值。下表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对的左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的水平中点相对于模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对的右边缘相对于模块右边缘的水平偏移指定为模块宽度的比例。 |

#### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0`（默认）| `scalar`

**Y Offset** 的测量方式取决于 **Vertical Alignment** 的值。下表列出了每个 **Vertical Alignment** 值的偏移测量方式。相对于偏移为 `0` 时文本的位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

| **Vertical Alignment** | 偏移 |
| --- | --- |
| `Top` | 将标签和图标对的顶边缘相对于模块顶边缘的垂直偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的垂直中点相对于模块垂直中点的垂直偏移指定为模块宽度的比例。 |
| `Bottom` | 将标签和图标对的底边缘相对于模块底边缘的垂直偏移指定为模块宽度的比例。 |

#### **Icon Placement** — 图标相对于标签的位置 `Left`（默认）| `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐方式。

#### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例:** `0.5`

#### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例:** `0.5`

#### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on`（默认）| `off`

启用此选项以在使用 Property Inspector 调整图像大小时保持宽高比。

#### **Image X Offset** — 图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

#### **Image Y Offset** — 图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

#### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例:** `0.5`

#### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例:** `0.5`

#### 背景图像

#### **Use Background Color** — 为按钮指定纯色背景颜色的选项 `off`（默认）| `on`

你可以为模块提供背景图像，或为按钮选择纯色背景颜色。要为按钮选择纯色背景颜色，请选择此参数。要为模块提供背景图像，请清除此参数。

**注意**

- 当你为按钮设置纯色背景颜色时，状态图像不可见。要使状态图像可见，请关闭 **Use Background Color**。
- 使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并打开 **Use Background Color** 参数。

**示例:** `on`

#### **Color** — 按钮背景颜色 `[r g b]` vector

要为按钮选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当你设置纯色背景颜色时，状态图像不可见。要使状态图像可见，请在 Property Inspector 中，在 **Design** 选项卡上，在 **Background Image** 组件中，关闭 **Use Background Color**。

**提示**

你也可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 程序化使用

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，并格式化为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

#### **Opacity** — 模块背景不透明度 `1`（默认）| scalar

将纯色背景颜色的不透明度指定为从 0 到 1 的标量值。

**示例:** `0.5`

#### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

指定纯色背景颜色覆盖区域的圆角半径。

**示例:** `0.25`

#### 前景图像

#### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

#### **Y Offset** — 前景图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例:** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例:** `0.5`

#### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认）| `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持宽高比。

### 模块特性

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

### 版本历史

**在 R2021b 中引入**

#### R2025a：仿真未运行时单击一次即可按下回调按钮，而不是单击两次

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于 *活动* 状态时，你可以与该模块表示的小工具交互。例如，你可以按下按钮或拨动开关。当模块处于非活动状态时，你只能与该模块交互。例如，你可以移动或调整模块大小。要在模块处于非活动状态时与小工具交互，你可以通过点击模块临时激活该模块。当你取消选择模块时，模块会再次变为非活动状态。

默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 dashboard 面板的模块在面板于其自己的窗口中打开或已停靠且未锁定时也处于活动状态。在以前的版本中，模块在所有其他情况下都处于非活动状态。具体而言，当仿真未运行时，模型画布中的或位于既未在其自己的窗口中打开也未停靠且未锁定的面板中的 Callback Button 模块处于非活动状态。要按下按钮，必须点击模块两次：一次用于临时激活模块，一次用于按下按钮。

从 R2025a 开始，对于按钮按下触发的至少一个回调具有非空值的 Callback Button 模块始终处于活动状态，无论仿真是否正在运行。此更改意味着当仿真未运行时，你可以单击一次按下回调按钮。当仿真未运行时，你可以移动和调整活动的 Callback Button 模块的大小。

还有一个用于与活动模块交互的新键盘快捷方式。点击活动的 Callback Button 模块或连接到参数或变量值的来自 Dashboard 或 Customizable Blocks 库的活动模块，会同时选择该模块并与其表示的小工具交互。例如，点击未选择的活动的已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，你可以通过按 **Shift**，然后点击模块来选择模块而不与小工具交互。同样，你可以通过按 **Shift**，然后双击模块来打开 Block Parameters 对话框。

#### R2024b：使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，你可以通过按 **Shift** 临时解锁宽高比。当你释放 **Shift** 键时，宽高比锁定。

如果宽高比未锁定，按 **Shift** 会临时锁定宽高比。当你释放 **Shift** 键时，宽高比解锁。

#### R2024a：停靠 dashboard 面板

从 R2024a 开始，你可以将 dashboard 面板停靠到 Simulink Editor 窗口。你可以使用停靠的面板在仿真期间监视信号和控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

#### R2023b：在新窗口中打开面板

从 R2023b 开始，你可以在新窗口中打开 dashboard 面板。为此，选择面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

你可以独立于模型窗口最小化和还原包含该面板的新窗口。从面板窗口中，你可以运行、暂停、停止和逐步执行仿真。在面板窗口中，你可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

#### R2023a：Simulink Toolstrip 中的持久 Panels 选项卡

当你将 dashboard 面板添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选择了面板时可见。从 R2023a 开始，当未选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 你可以添加空面板。
- 你可以重命名所选面板。
- 你可以隐藏所选面板。

#### R2022b：支持撤销和重做面板中的可自定义 dashboard 模块

从 R2022b 开始，你可以撤销和重做对面板中的可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷方式基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

#### R2022b：对面板的 Toolstrip 支持

从 R2022b 开始，你可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当你点击面板中的 dashboard 模块时，该模块的 toolstrip 选项卡会出现。例如，当你点击 Circular Gauge 模块时，**Gauge** 选项卡会出现在 toolstrip 中。

当你点击面板时，**Panel** 选项卡会出现在 toolstrip 中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2022a：调整前景图像大小和重新定位

Customizable Blocks 库中的模块具有添加前景图像作为模块设计一部分的选项。从 R2022a 开始，你可以在模块设计中旋转、调整大小和重新定位前景图像。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

The Callback Button block runs MATLAB® code in response to a click (immediate release of the pointer) or a press
(delayed release of the pointer). You can specify different code for the click than the press.
When you press the button, the code either executes after a time span or at time intervals
that you specify. You can customize the appearance of the Callback Button block
to look like a button in a real system. Use the Callback Button block with
other dashboard blocks to create an interactive dashboard to control your model.

When a Callback Button block is *active*, you can
interact with the gadget the block represents. Clicking an active Callback
Button block pushes a virtual button. While you press your pointer, the button is
pushed. When you release your pointer, you release the button. Callback Button
blocks are active when the simulation is running, the block is in a panel that is open in its
own window or docked and unlocked, or at least one of the callbacks triggered by a click or
press has a nonempty value. To select an active Callback Button block without
pushing the button, press **Shift**, and then click the block. To open the Block
Parameters dialog box of an active Callback Button block, press
**Shift**, and then double-click the block.

When a block is inactive, you can only interact with the block, for example, taking
actions such as resizing or dragging the block. To temporarily activate an inactive
Callback Button block, click the block. When you deselect the Callback
Button block, the block becomes inactive again.

Specify what you want pushing the button to do using callback functions:

- `PressFcn` functions run while the button is pushed. You can
  configure the button to run the `PressFcn` function only once while the
  button is pushed, or you can specify a repeat interval. To run the function only once,
  specify a repeat interval of `0`.
- `ClickFcn` functions run when you release the button.

You can configure the button to remain pushed when you release the pointer by setting the
**Button Type** to `Latched`. When you choose the
latched button type:

- To latch the button, click the button.
- To unlatch the button, click the button again.

The `PressFcn` function runs while the button is latched. The
`ClickFcn` function runs once when you latch the button and once when you
unlatch the button.

You can use states to specify how the appearance of the Callback Button
block changes when you interact with the button:

- While you push the button, the block is in the `Pressed`
  state.
- When the button is latched and you are not pushing it, the block is in the
  `Latched` state.
- When the button is latched and you are pushing it, the block is in the
  `Latched and Pressed` state.
- When the block is not in any of these three states, it is in the
  `Default` state.

A state pairs pointer actions with:

- A state label
- A state icon
- A state image

### Customize Callback Button Blocks

When you add a Callback Button block to your model, the block is
preconfigured with a default design. You can use the block with the default design or
customize the appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the callback
button. To access additional customization options or to enter exact values for design
settings, use the **Design** tab in the Property Inspector.

Customizable Callback Button block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Callback Button block, you configure the block
appearance for each state. When you configure the **Block Type** as
`Momentary`, the block has two states. When you configure the
**Block Type** as `Latch`, the block has four.
To select a state to customize, use the drop-down list in the toolbar. Alternatively, on
the **Design** tab, select the **States** component and
then select from the **Select State** list.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state label text. | No | Yes |
| Specify the color and opacity of the state label text. | Yes | Yes |
| Upload a state image. | Yes | Yes |
| Upload a state icon. | Yes | Yes |
| Change the size of the state image and state icon. | No | Yes |
| Change the position of the state label, state image, and state icon. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. To resize a component specific to a state, such as the state
image, select the state in the toolbar, and then resize or reposition the component.

**Design Mode Actions that Apply to All States**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a background image. | No | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

When you finish editing the design, to exit design mode, click the
**X** in the upper right of the canvas.

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

#### Main

### **Button Type** — Button response to click `Momentary` (default) | `Latch`

Specify how the block responds to a click.

- `Momentary` — The button changes state only while
  pressed. When you release the click, the button returns to its default
  state.
- `Latch` — The button latches the state change
  when clicked. The button remains in the pressed state until you click it
  again.

When you configure **Button Type** as
`Momentary`, the block has these states:

- `Default` — Default state for the block when it
  is not pressed
- `Pressed` — Block state when the block is
  pressed

When you configure **Button Type** as
`Latch`, the block has these states:

- `Default` — Default state for the block when it
  is not pressed.
- `Pressed` — Transitional state when you press the
  button while it is in the `Default` state. The
  block transitions to the `Latched` state when you
  release the click.
- `Latched` — Latched state for the block when it
  is not pressed.
- `Latched and Pressed` — Transitional state when
  you press the button while it is in the `Latched`
  state. The block transitions to the `Default` state
  when you release the click.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ButtonType` |
| **Type:** string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

### **Button Text** — Button label text `'Callback Button'` (default) | string | character array

Specify the text for the button label. The label is applied to the button for the
state that is selected in the **Select State** section of the
**States** component on the **Design** tab.

#### Programmatic Use

Specify the `ButtonText` parameter for the block as a string or
a character vector.

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

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

#### Callbacks

### **ClickFcn** — MATLAB code that executes in response to click MATLAB code

MATLAB code that executes in response to a click of the button.

Every time you click the button, the `ClickFcn` code executes
once, at the point in time when you release the click.

To specify code for the `ClickFcn`, select
`ClickFcn` from the drop-down menu. Enter the code in the
text box below the menu.

#### Programmatic Use

Specify the `ClickFcn` parameter for the block as MATLAB code that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `ClickFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

### **PressFcn** — MATLAB code that executes in response to press MATLAB code

MATLAB code that executes in response to a press of the button.

While the button is in the pressed state, the `PressFcn` code
executes once when the **Press Delay** time has elapsed and
periodically at every **Repeat Interval**.

To specify code for the `PressFcn`, select
`PressFcn` from the drop-down menu. Enter the code in the
text box below the menu.

How you press the button to execute the `PressFcn` code
depends on the **Button Type**.

- If the **Button Type** is
  `Momentary`, hold down your click for the duration
  that you want to press the button.
- If the **Button Type** is `Latch`,
  click to press the button, but do not hold down your click. The button remains
  pressed until you click it again.

**Note**

Every time that you click on the button, even when you do so as part of the
process for pressing the button, the `ClickFcn` code
executes once, at the point in time when you release the click.

#### Programmatic Use

Specify the `PressFcn` parameter for the block as MATLAB code that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `PressFcn` |
| **Type:** character vector | string |
| **Values:** MATLAB code |

### **Press Delay (ms)** — Time to hold button for press `500` (default) | scalar

Amount of time required to cause the `PressFcn` code to
execute.

#### Dependencies

**Press Delay (ms)** is visible only when
`PressFcn` is selected as the callback.

#### Programmatic Use

Specify the `PressDelay` parameter for the block as a positive
scalar value.

|  |
| --- |
| **Block Parameter:** `PressDelay` |
| **Type:** scalar |

### **Repeat Interval (ms)** — Time interval to repeat `PressFcn` code `0` (default) | scalar

Time interval after which the `PressFcn` code executes again
if the Callback Button block is still pressed.

#### Dependencies

**Repeat Interval (ms)** is visible only when
`PressFcn` is selected as the callback.

#### Programmatic Use

Specify the `RepeatInterval` parameter for the block as a
positive scalar value.

|  |
| --- |
| **Block Parameter:** `RepeatInterval` |
| **Type:** scalar |

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Button

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

#### States

### **Select State** — Selection of state to configure `Default` (default) | `Pressed` | `Latched` | `Latched and Pressed`

Select a state that you want to configure from the drop-down menu in the
**Select State** section of the **States**
component. When the **Button Type** is
`Momentary`, you can select these states:

- `Default` — Default state for the block when it
  is not pressed
- `Pressed` — Block state when the block is
  pressed

When the **Button Type** is `Latch`, you can
select these states:

- `Default` — Default state for the block when it
  is not pressed.
- `Pressed` — Transitional state when you press the
  button while it is in the `Default` state. The
  block transitions to the `Latched` state when you
  release the click.
- `Latched` — Latched state for the block when it
  is not pressed.
- `Latched and Pressed` — Transitional state when
  you press the button while it is in the `Latched`
  state. The block transitions to the `Default` state
  when you release the click.

**Note**

You can configure all of the parameters in the **States**
component of the **Design** tab for a state. For example, you can
select an icon that will appear on the button when it is in the state. When you
configure any of the parameters in the **States** component, the
changes are applied to the state that is selected in the **Select
State** section of the **States** component.

**Example:** `Pressed`

### **Text** — Button label text `'Callback Button'` (default) | string | character array

Specify the text for the button label. The label is applied to the button for the
state that is selected in the **Select State** section of the
**States** component on the **Design** tab.

#### Programmatic Use

Specify the `ButtonText` parameter for the block as a string or
a character vector.

|  |
| --- |
| **Block Parameter:** `ButtonText` |
| **Type:** character vector | string |

### **Color** — Label font color `[r g b]` vector

Choose a font color for the label text from the palette of standard colors, or specify
a custom color. The color is applied to the label text for the state that is selected in
the **Select State** section of the **States**
component on the **Design** tab.

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

### **Vertical Alignment** — Vertical alignment of label and icon pair with block `Center` (default) | `Bottom` | `Top`

Set the alignment of the label and icon pair in the vertical direction. The table
lists the vertical position of the label and icon pair when the **Y
Offset** is zero. A nonzero **Y Offset** moves the label
and icon pair from the position listed in the table.

| Alignment | Position of the Label and Icon Pair |
| --- | --- |
| `Top` | The top edge of the label and icon pair is at the top edge of the block. |
| `Center` | The vertical middle of the label and icon pair is at the vertical middle of the block. |
| `Bottom` | The bottom edge of the label and icon pair is at the bottom edge of the block. |

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

How the **Y Offset** is measured depends on the value of the
**Vertical Alignment**. The table lists how the offset is measured
for each **Vertical Alignment** value. Relative to the position of the
text when the offset is `0`, an offset with a negative value moves the
text up, and an offset with a positive value moves the text down.

| **Vertical Alignment** | Offset |
| --- | --- |
| `Top` | Specify the vertical offset of the top edge of the label and icon pair from the top edge of the block as a ratio of the block width. |
| `Center` | Specify the vertical offset of the vertical middle of the label and icon pair from the vertical middle of the block as a ratio of the block width. |
| `Bottom` | Specify the vertical offset of the bottom edge of the label and icon pair from the bottom edge of the block as a ratio of the block width. |

### **Icon Placement** — Placement of icon relative to label `Left` (default) | `Top` | `Right` | `Bottom`

Specify the placement of the icon relative to the label.

**Note**

Changing the placement of the icon moves the label, but does not change the offset
or alignment of the label.

### **Icon Width** — Icon width scalar

Specify the icon width as a ratio of the font height of the label text.

**Example:** `0.5`

### **Icon Height** — Icon height scalar

Specify the icon height as a ratio of the font height of the label text.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Enable this option to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Image X Offset** — Horizontal offset of left edge of image from left edge of block scalar

Specify the horizontal offset of the left edge of the image from the left edge of the
block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Image Y Offset** — Vertical offset of top edge of image from top edge of block scalar

Specify the vertical offset of the top edge of the image from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Image Width** — Image width scalar

Specify the image width as a ratio of the block width.

**Example:** `0.5`

### **Image Height** — Image height scalar

Specify the image height as a ratio of the block height.

**Example:** `0.5`

#### Background Image

### **Use Background Color** — Option to specify solid background color for button `off` (default) | `on`

You can provide a background image for the block or select a solid background
color for the button. To select a solid background color for the button, select this
parameter. To provide a background image for the block, clear this parameter.

**Note**

- The state images are not visible when you set a solid background color for
  the button. To make the state images visible, turn off **Use Background
  Color**.
- Changing the background color using the **Format** tab of
  the Simulink Toolstrip removes the background image and turns on the
  **Use Background Color** parameter.

**Example:** `on`

### **Color** — Button background color `[r g b]` vector

To select a solid background color for the button, enable the **Use
Background Color** parameter. Then, choose a background color from the
palette of standard colors, or specify a custom color.

**Note**

The state images are not visible when you set a solid background color. To make
the state images visible, in the Property Inspector, on the
**Design** tab, in the **Background Image**
component, turn off **Use Background Color**.

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
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the opacity of the solid background color as a scalar value from 0 to
1.

**Example:** `0.5`

### **Corner Radius** — Corner radius of area with block background color scalar

Specify the corner radius of the area covered by the solid background
color.

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
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2021b**

### R2025a: Push callback button with one click instead of two when simulation is not running

When a Simulink block from the Dashboard or Customizable Blocks library is
*active*, you can interact with the gadget the block represents. For
example, you can push a button or flip a switch. When a block is inactive, you can only
interact with the block. For example, you can move or resize the block. To interact with the
gadget when a block is inactive, you can temporarily activate the block by clicking the
block. When you deselect the block, the block becomes inactive again.

By default, all blocks from the Dashboard and Customizable Blocks libraries are active
during simulation. Blocks promoted to a dashboard panel are also active when the panel is
open in its own window or docked and unlocked. In previous releases, the blocks are inactive
in all other cases. Specifically, when the simulation is not running, a Callback
Button block in the model canvas or in a panel that is neither open in its own
window nor docked and unlocked is inactive. To push the button, you must click the block
twice: once to temporarily activate the block, and once to push the button.

Starting in R2025a, Callback Button blocks for which at least one of the
callbacks triggered by pushing the button has a nonempty value are always active, regardless
of whether the simulation is running. This change means when the simulation is not running,
you can push callback buttons with a single click. When the simulation is not running, you
can move and resize active Callback Button blocks.

There is also a new keyboard shortcut for interacting with active blocks. Clicking an
active Callback Button block or an active block from the Dashboard or
Customizable Blocks library that is connected to a parameter or variable value both selects
the block and interacts with the gadget the block represents. For example, clicking an
unselected active connected Push Button block both selects the block and
pushes the button. Starting in R2025a, you can select the block without interacting with the
gadget by pressing **Shift** and then clicking the block. Similarly, you can
open the Block Parameters dialog box by pressing **Shift** and then
double-clicking the block.

### R2024b: Unlock dashboard block aspect ratio with keyboard

If the aspect ratio of a block from the Dashboard library is locked, you can temporarily
unlock the aspect ratio by pressing **Shift**. When you release the
**Shift** key, the aspect ratio locks.

If the aspect ratio is unlocked, pressing **Shift** temporarily locks the
aspect ratio. When you release the **Shift** key, the aspect ratio
unlocks.

### R2024a: Dock dashboard panels

Starting in R2024a, you can dock dashboard panels to the Simulink Editor window. You can use the docked panel to monitor signals and control
parameters during simulation without covering the model diagram in the canvas.

For more information, see Dock Panels.

### R2023b: Open panel in new window

Starting in R2023b, you can open a dashboard panel in a new window. To do so, select the
panel and pause on the ellipsis that appears. In the action menu that expands, click Open In
New Window .

You can minimize and restore the new window containing the panel separately from the
model window. From the panel window, you can run, pause, stop, and step through the
simulation. In the panel window, you can edit the panel and the blocks it contains.

To return the panel to the model canvas, in the panel window toolstrip, click Open in
canvas .

For more information about opening a panel in a new window, see Open Panels in New Window.

### R2023a: Persistent panels tab in Simulink Toolstrip

When you add a dashboard panel to a model, the **Panels** tab appears
in the Simulink Toolstrip and shows options for managing and editing panels.

Previously, the **Panels** tab was only visible when a panel was
selected. Starting in R2023a, the **Panels** tab stays visible when no
panel is selected.

The **Panels** tab also contains these new options:

- You can add an empty panel.
- You can rename the selected panel.
- You can hide the selected panel.

### R2022b: Undo and redo support for customizable dashboard blocks in panel

Starting in R2022b, you can undo and redo the changes you make to customizable dashboard
blocks that are in a panel.

To undo or redo a change:

1. Click the panel or a block in the panel.
2. Press **Ctrl+Z** to undo the change, or press **Ctrl+Y**
   to redo the change.

**Note**

The keyboard shortcuts are based on Windows®. On a Mac, press **command** (⌘) instead of
**Ctrl**.

### R2022b: Toolstrip support for panels

Starting in R2022b, you can use the Simulink Toolstrip to manage and edit panels and the dashboard blocks that they
contain.

When you click a dashboard block in a panel, the toolstrip tab for the block appears.
For example, when you click a Circular Gauge block, the
**Gauge** tab appears in the toolstrip.

When you click a panel, the **Panel** tab appears in the toolstrip. The
tab provides these options:

- Manage the visibility of panels in the model.
- Fit all unhidden panels within the current view.
- Collapse the selected panel.
- Customize the size and the contents of the panel.
- Set a custom background image for the selected panel.
- Add a new tab to the selected panel.

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.
