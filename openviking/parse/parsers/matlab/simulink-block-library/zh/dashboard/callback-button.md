---
type: simulink-block
title: 'Callback Button'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'callbackbutton'
language: zh-CN
chinese_source: worker-translation
---

# Callback Button

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，在 **Design** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector 并单击 **Parameters** 选项卡。

#### 主要

### **Button Type** — 按钮对单击的响应 `Momentary`（默认）| `Latch`

指定模块如何响应单击。

- `Momentary` — 按钮仅在按下时改变状态。当您释放单击时，按钮返回其默认状态。
- `Latch` — 按钮在单击时锁存状态变化。按钮保持按下状态，直到您再次单击它。

当您将 **Button Type** 配置为 `Momentary` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

当您将 **Button Type** 配置为 `Latch` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您释放单击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您释放单击时，模块过渡到 `Default` 状态。

#### 编程用法

|  |
| --- |
| **模块参数:** `ButtonType` |
| **类型:** string or character array |
| **值:** `'Momentary'` | `'Latch'` |

### **Text** — 按钮标签文本 `'Callback Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于在 **Design** 选项卡上的 **States** 组件中的 **Select State** 部分中选择的状态的按钮。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数:** `ButtonText` |
| **类型:** character vector | string |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比未锁定时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比锁定时，调整模块大小时按 **Shift** 键会临时解锁宽高比。释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，调整模块大小时按 **Shift** 键会临时锁定宽高比。释放 **Shift** 键时，宽高比解锁。

#### 回调

### **ClickFcn** — 响应单击而执行的 MATLAB 代码 MATLAB code

响应单击按钮而执行的 MATLAB 代码。

每次单击按钮时，`ClickFcn` 代码都会在您释放单击的时间点执行一次。

要为 `ClickFcn` 指定代码，请从下拉菜单中选择 `ClickFcn`。在菜单下方的文本框中输入代码。

#### 编程用法

将模块的 `ClickFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数:** `ClickFcn` |
| **类型:** character vector | string |
| **值:** MATLAB code |

### **PressFcn** — 响应按下而执行的 MATLAB 代码 MATLAB code

响应按下按钮而执行的 MATLAB 代码。

当按钮处于按下状态时，`PressFcn` 代码在 **Press Delay** 时间过去后执行一次，并以每个 **Repeat Interval** 周期性地执行。

要为 `PressFcn` 指定代码，请从下拉菜单中选择 `PressFcn`。在菜单下方的文本框中输入代码。

您按下按钮以执行 `PressFcn` 代码的方式取决于 **Button Type**。

- 如果 **Button Type** 为 `Momentary`，请按住单击，持续您希望按下按钮的时长。
- 如果 **Button Type** 为 `Latch`，请单击以按下按钮，但不要按住单击。按钮保持按下，直到您再次单击它。

**注意**

每次您单击按钮时，即使这是按下按钮过程的一部分，`ClickFcn` 代码也会在您释放单击的时间点执行一次。

#### 编程用法

将模块的 `PressFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数:** `PressFcn` |
| **类型:** character vector | string |
| **值:** MATLAB code |

### **Press Delay (ms)** — 按下按钮以触发按下所需保持的时间 `500`（默认）| scalar

使 `PressFcn` 代码执行所需的时间量。

#### 依赖项

**Press Delay (ms)** 仅在 `PressFcn` 被选为回调时可见。

#### 编程用法

将模块的 `PressDelay` 参数指定为 positive scalar 值。

|  |
| --- |
| **模块参数:** `PressDelay` |
| **类型:** scalar |

### **Repeat Interval (ms)** — 重复 `PressFcn` 代码的时间间隔 `0`（默认）| scalar

如果 Callback Button 模块仍被按下，`PressFcn` 代码再次执行的时间间隔。

#### 依赖项

**Repeat Interval (ms)** 仅在 `PressFcn` 被选为回调时可见。

#### 编程用法

将模块的 `RepeatInterval` 参数指定为 positive scalar 值。

|  |
| --- |
| **模块参数:** `RepeatInterval` |
| **类型:** scalar |

### 设计

要自定义 dashboard 模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。

#### 按钮

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比锁定时，调整模块大小时按 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，调整模块大小时按 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比解锁。

#### 状态

### **Select State** — 选择要配置的状态 `Default`（默认）| `Pressed` | `Latched` | `Latched and Pressed`

从 **States** 组件中 **Select State** 部分的下拉菜单中选择要配置的状态。当 **Button Type** 为 `Momentary` 时，您可以选择以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

当 **Button Type** 为 `Latch` 时，您可以选择以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您释放单击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您释放单击时，模块过渡到 `Default` 状态。

**注意**

您可以为某个状态配置 **Design** 选项卡的 **States** 组件中的所有参数。例如，您可以选择按钮处于该状态时将在按钮上显示的图标。当您配置 **States** 组件中的任何参数时，更改将应用于 **States** 组件中 **Select State** 部分所选的状态。

**示例:** `Pressed`

### **Text** — 按钮标签文本 `'Callback Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于在 **Design** 选项卡上的 **States** 组件中的 **Select State** 部分中选择的状态的按钮。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数:** `ButtonText` |
| **类型:** character vector | string |

### **Color** — 标签字体颜色 `[r g b]` vector

从标准颜色调色板中为标签文本选择字体颜色，或指定自定义颜色。该颜色应用于在 **Design** 选项卡上的 **States** 组件中的 **Select State** 部分中选择的状态的标签文本。

### **Horizontal Alignment** — 标签和图标对与模块的水平对齐 `Left`（默认）| `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。下表列出了当 **X Offset** 为零时标签和图标对的水平位置。非零 **X Offset** 会将标签和图标对从表中列出的位置移动。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

### **Vertical Alignment** — 标签和图标对与模块的垂直对齐 `Center`（默认）| `Bottom` | `Top`

设置标签和图标对在垂直方向上的对齐方式。下表列出了当 **Y Offset** 为零时标签和图标对的垂直位置。非零 **Y Offset** 会将标签和图标对从表中列出的位置移动。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Top` | 标签和图标对的顶边缘位于模块的顶边缘。 |
| `Center` | 标签和图标对的垂直中点位于模块的垂直中点。 |
| `Bottom` | 标签和图标对的底边缘位于模块的底边缘。 |

### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0`（默认）| scalar

如何测量 **X Offset** 取决于 **Horizontal Alignment** 的值。下表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对的左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的水平中点相对于模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对的右边缘相对于模块右边缘的水平偏移指定为模块宽度的比例。 |

### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0`（默认）| `scalar`

如何测量 **Y Offset** 取决于 **Vertical Alignment** 的值。下表列出了每个 **Vertical Alignment** 值的偏移测量方式。相对于偏移为 `0` 时文本的位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

| **Vertical Alignment** | 偏移 |
| --- | --- |
| `Top` | 将标签和图标对的顶边缘相对于模块顶边缘的垂直偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的垂直中点相对于模块垂直中点的垂直偏移指定为模块宽度的比例。 |
| `Bottom` | 将标签和图标对的底边缘相对于模块底边缘的垂直偏移指定为模块宽度的比例。 |

### **Icon Placement** — 图标相对于标签的位置 `Left`（默认）| `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐方式。

### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例:** `0.5`

### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例:** `0.5`

### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on`（默认）| `off`

启用此选项以在使用 Property Inspector 调整图像大小时保持宽高比。

### **Image X Offset** — 图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

### **Image Y Offset** — 图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例:** `0.5`

### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例:** `0.5`

#### 背景图像

### **Use Background Color** — 为按钮指定纯色背景颜色的选项 `on`（默认）| `off`

您可以为模块提供背景图像，或为按钮选择纯色背景颜色。要为按钮选择纯色背景颜色，请选择此参数。要为模块提供背景图像，请清除此参数。

**注意**

- 当您为按钮设置纯色背景颜色时，状态图像不可见。要使状态图像可见，请关闭 **Use Background Color**。
- 使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像，并打开 **Use Background Color** 参数。

**示例:** `on`

### **Color** — 按钮背景颜色 `[r g b]` vector

要为按钮选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当您设置纯色背景颜色时，状态图像不可见。要使状态图像可见，请在 Property Inspector 中，在 **Design** 选项卡上，在 **Background Image** 组件中，关闭 **Use Background Color**。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **模块参数:** `BackgroundColor` |
| **类型:** character vector | string |
| **值:** `[r g b]` vector |

### **Opacity** — 按钮背景不透明度 `1`（默认）| scalar

将纯色背景颜色的不透明度指定为从 0 到 1 的 scalar 值。

**示例:** `0.5`

### **Corner Radius** — 具有按钮背景颜色的区域的圆角半径 scalar

指定由纯色背景颜色覆盖的区域的圆角半径。

**示例:** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

### **Y Offset** — 前景图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例:** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例:** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认）| `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持宽高比。

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展能力

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

dashboard 模块在代码生成时被忽略。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2017b 中引入**

### R2025a: 当仿真未运行时，通过一次单击而不是两次按下 Callback Button

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块表示的 gadget 交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块大小。要在模块处于非活动状态时与 gadget 交互，您可以通过单击模块临时激活该模块。当您取消选择该模块时，该模块再次变为非活动状态。

默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 dashboard panel 的模块在 panel 在其自己的窗口中打开或已停靠且未锁定时也处于活动状态。在以前的版本中，模块在所有其他情况下都处于非活动状态。具体而言，当仿真未运行时，位于模型画布中或位于既未在其自己的窗口中打开也未停靠且未锁定的 panel 中的 Callback Button 模块处于非活动状态。要按下按钮，您必须单击模块两次：一次用于临时激活模块，一次用于按下按钮。

从 R2025a 开始，对于由按下按钮触发的至少一个回调具有非空值的 Callback Button 模块，无论仿真是否正在运行，它们始终处于活动状态。此更改意味着当仿真未运行时，您可以通过单击一次按下 Callback Button。当仿真未运行时，您可以移动和调整活动的 Callback Button 模块的大小。

还有一个新的键盘快捷键用于与活动模块交互。单击活动的 Callback Button 模块，或单击来自 Dashboard 或 Customizable Blocks 库且连接到参数或变量值的活动模块，会同时选择该模块并与该模块表示的 gadget 交互。例如，单击未选中的活动的已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift**，然后单击该模块来选择该模块而不与 gadget 交互。类似地，您可以通过按 **Shift**，然后双击该模块来打开 Block Parameters 对话框。

### R2024b: 使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键时，宽高比锁定。

如果宽高比未锁定，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键时，宽高比解锁。

### R2024a: 停靠 dashboard panel

从 R2024a 开始，您可以将 dashboard panel 停靠到 Simulink Editor 窗口。您可以使用停靠的 panel 在仿真期间监视信号和控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b: 在新窗口中打开 panel

从 R2023b 开始，您可以在新窗口中打开 dashboard panel。为此，请选择该 panel 并暂停在出现的省略号上。在展开的操作菜单中，单击 **Open In New Window** 按钮 。

您可以分别从模型窗口最小化和还原包含该 panel 的新窗口。从 panel 窗口，您可以运行、暂停、停止和单步执行仿真。在 panel 窗口中，您可以编辑 panel 及其包含的模块。

要将 panel 返回到模型画布，请在 panel 窗口 toolstrip 中，单击 **Open in canvas** 。

有关在新窗口中打开 panel 的详细信息，请参阅 Open Panels in New Window。

### R2023a: Simulink Toolstrip 中的持久 Panels 选项卡

当您将 dashboard panel 添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑 panel 的选项。

以前，**Panels** 选项卡仅在选中 panel 时可见。从 R2023a 开始，未选择任何 panel 时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空 panel。
- 您可以重命名所选 panel。
- 您可以隐藏所选 panel。

### R2023a: Dashboard 库和 Customizable Blocks 库中的 Callback Button 模块具有相同的自定义选项

从 R2023a 开始，来自 Dashboard 库的 Callback Button 模块具有与来自 Customizable Blocks 库的 Callback Button 模块相同的自定义选项。

### R2022b: 支持对 panel 中可自定义 dashboard 模块进行撤销和重做

从 R2022b 开始，您可以撤销和重做对 panel 中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 单击 panel 或 panel 中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b: Toolstrip 对 panel 的支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑 panel 及其包含的 dashboard 模块。

当您单击 panel 中的 dashboard 模块时，该模块的 toolstrip 选项卡会出现。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在 toolstrip 中。

当您单击 panel 时，**Panel** 选项卡会出现在 toolstrip 中。该选项卡提供以下选项：

- 管理模型中 panel 的可见性。
- 将当前视图中所有未隐藏的 panel 调整到合适大小。
- 折叠所选 panel。
- 自定义 panel 的大小和内容。
- 为所选 panel 设置自定义背景图像。
- 为所选 panel 添加新选项卡。

### R2020b: Simulink Toolstrip 对 dashboard 模块的支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink Toolstrip 中的 **Block** 选项卡会变为模块特定的选项卡。从 toolstrip 中，您可以为所选模块连接、断开连接和修改连接。您可以跳转到连接到所选模块的模型元素，并且可以将所选模块添加到 panel。

### R2019a: 以编程方式添加和配置 dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置来自 Dashboard 库的模块。

## 描述

使用按钮执行 MATLAB 代码

Callback Button 模块响应单击（立即释放指针）或按下（延迟释放指针）运行 MATLAB® 代码。您可以为单击指定与按下不同的代码。当您按下按钮时，代码要么在您指定的时间段后执行，要么按您指定的时间间隔执行。您可以自定义 Callback Button 模块的外观，使其看起来像实际系统中的按钮。将 Callback Button 模块与其他 dashboard 模块一起使用，创建交互式 dashboard 以控制您的模型。

当 Callback Button 模块处于*活动*状态时，您可以与该模块表示的 gadget 交互。单击活动的 Callback Button 模块会按下虚拟按钮。当您按住指针时，按钮被按下。当您释放指针时，按钮被释放。当仿真正在运行、模块位于在其自己的窗口中打开或已停靠且未锁定的 panel 中，或者由单击或按下触发的至少一个回调具有非空值时，Callback Button 模块处于活动状态。要选择活动的 Callback Button 模块而不按下按钮，请按 **Shift**，然后单击该模块。要打开活动的 Callback Button 模块的 Block Parameters 对话框，请按 **Shift**，然后双击该模块。

当模块处于非活动状态时，您只能与该模块交互，例如执行调整大小或拖动模块等操作。要临时激活非活动的 Callback Button 模块，请单击该模块。当您取消选择 Callback Button 模块时，该模块再次变为非活动状态。

使用回调函数指定按下按钮时要执行的操作：

- `PressFcn` 函数在按钮被按下时运行。您可以将按钮配置为在按钮被按下时仅运行 `PressFcn` 函数一次，也可以指定重复间隔。要仅运行一次，请将重复间隔指定为 `0`。
- `ClickFcn` 函数在您释放按钮时运行。

您可以通过将 **Button Type** 设置为 `Latched`，将按钮配置为在释放指针后仍保持按下。当您选择 latched 按钮类型时：

- 要锁存按钮，请单击该按钮。
- 要取消锁存按钮，请再次单击该按钮。

`PressFcn` 函数在按钮被锁存时运行。`ClickFcn` 函数在您锁存按钮时运行一次，并在您取消锁存按钮时运行一次。

您可以使用状态指定 Callback Button 模块的外观在您与按钮交互时如何变化：

- 当您按下按钮时，模块处于 `Pressed` 状态。
- 当按钮被锁存且您未按下它时，模块处于 `Latched` 状态。
- 当按钮被锁存且您正在按下它时，模块处于 `Latched and Pressed` 状态。
- 当模块不处于这三种状态中的任何一种时，它处于 `Default` 状态。

状态将指针操作与以下内容配对：

- 状态标签
- 状态图标
- 状态图像

### 自定义 Callback Button 模块

当您将 Callback Button 模块添加到模型时，该模块预配置为默认设计。您可以按默认设计使用该模块，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，在 **Design** 下，单击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上方出现的省略号上，然后单击 Edit Custom Block 按钮 。

Callback Button 模块处于设计模式，工具栏和 Property Inspector 中的 Design 选项卡可见。

设计 Callback Button 模块时，您为每个可能的状态配置模块外观。当您将 **Block Type** 配置为 `Momentary` 时，模块有两个状态。当您将 **Block Type** 配置为 `Latch` 时，模块有四个。

您可以使用模块上方的工具栏切换状态。对于每个状态，您可以：

- 上传状态图像。
- 上传状态图标并指定图标相对于状态标签的位置。
- 指定 State Label 文本、颜色、不透明度和位置。

您还可以上传前景或背景图像，或设置纯色背景颜色。前景和背景应用于所有状态。

使用模块上方的工具栏配置图像、图标以及 State Label 的颜色和不透明度。

您可以使用 Property Inspector 中的 **Design** 选项卡精细控制模块设计，并为设计设置输入精确值。

使用 **Design** 选项卡可以：

- 指定 State Label 文本和位置。
- 指定图标位置。
- 上传前景图像。
- 上传背景图像。
- 设置纯色背景颜色。

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。
