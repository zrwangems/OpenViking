---
type: simulink-block
title: 'Push Button'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'custompushbutton'
language: zh-CN
chinese_source: worker-translation
---

# Push Button

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要为模块打开 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后单击 **Parameters** 选项卡。

#### Connection

### **Connection** — 用于将模块参数值连接到参数值的连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧，单击 **Connect** 或 **Change**。可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接，请执行以下操作：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要将其参数值连接的模块。
4. 在表中，选择要连接到的参数。
5. 单击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

还可以将 dashboard 模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。一些属性适用于将 dashboard 模块连接到由值定义的参数，一些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

#### Main

### **Button Type** — 按钮对点击的响应 `Momentary` (default) | `Latch`

指定模块如何响应点击。

- `Momentary` — 按钮仅在按下时更改状态。当您松开点击时，按钮返回到默认状态。
- `Latch` — 按钮在点击时锁存状态更改。按钮保持按下状态，直到您再次点击它。

将 **Button Type** 配置为 `Momentary` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

将 **Button Type** 配置为 `Latch` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您松开点击时，模块转换到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您松开点击时，模块转换到 `Default` 状态。

#### 编程用法

|  |
| --- |
| **模块参数：** `ButtonType` |
| **类型：** string 或 character array |
| **值：** `'Momentary'` | `'Latch'` |

### **Button Text** — 按钮标签文本 `'Button'` (default) | string | character array

指定按钮标签的文本。该标签应用于按钮在 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选的状态。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数：** `ButtonText` |
| **类型：** character vector | string |

### **On value** — 按下或锁存按钮时赋值给已连接参数的值 `1` (default) | scalar

按下或锁存按钮时赋值给已连接模块参数的值。

**提示**

使用 **Block Type** 参数配置模块如何响应点击：

- `Momentary` — 按钮仅在您按下它时应用 **On Value**。
- `Latch` — 按钮在您点击它时锁存状态更改，并应用 **On value**，直到您再次点击它。

#### 编程用法

将模块的 `OnValue` 参数指定为格式化为字符串或字符向量的标量值。

|  |
| --- |
| **模块参数：** `OnValue` |
| **类型：** string 或 character array |
| **值：** scalar |
| **默认值：** `'1'` |

### **Label** — 显示已连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果希望标签可见，请指定标签的位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会临时解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会临时锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

#### 回调

### **ClickFcn** — 响应点击而执行的 MATLAB 代码 MATLAB code

响应按钮点击而执行的 MATLAB 代码。

每次点击按钮时，`ClickFcn` 代码都会在您松开点击的时间点执行一次。

要为 `ClickFcn` 指定代码，请从下拉菜单中选择 `ClickFcn`。在下拉菜单下方的文本框中输入代码。

#### 编程用法

将模块的 `ClickFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数：** `ClickFcn` |
| **类型：** character vector | string |
| **值：** MATLAB code |

### **PressFcn** — 响应按下而执行的 MATLAB 代码 MATLAB code

响应按钮按下而执行的 MATLAB 代码。

当按钮处于按下状态时，`PressFcn` 代码会在 **Press Delay** 时间过去后执行一次，并在每个 **Repeat Interval** 周期性地执行。

要为 `PressFcn` 指定代码，请从下拉菜单中选择 `PressFcn`。在下拉菜单下方的文本框中输入代码。

按按钮以执行 `PressFcn` 代码的方式取决于 **Button Type**。

- 如果 **Button Type** 为 `Momentary`，请按住点击您希望按下按钮的持续时间。
- 如果 **Button Type** 为 `Latch`，请点击以按下按钮，但不要按住点击。按钮保持按下状态，直到您再次点击它。

**注意**

每次点击按钮时，即使在按下按钮的过程中这样做，`ClickFcn` 代码都会在您松开点击的时间点执行一次。

#### 编程用法

将模块的 `PressFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数：** `PressFcn` |
| **类型：** character vector | string |
| **值：** MATLAB code |

### **Press Delay (ms)** — 按住按钮以触发按下的时间 `500` (default) | scalar

使 `PressFcn` 代码执行所需的持续时间。

#### 依赖关系

仅当选择 `PressFcn` 作为回调时，**Press Delay (ms)** 才可见。

#### 编程用法

将模块的 `PressDelay` 参数指定为正标量值。

|  |
| --- |
| **模块参数：** `PressDelay` |
| **类型：** scalar |

### **Repeat Interval (ms)** — 重复 `PressFcn` 代码的时间间隔 `0` (default) | scalar

如果 Callback Button 模块仍被按下，则 `PressFcn` 代码再次执行之后的时间间隔。

#### 依赖关系

仅当选择 `PressFcn` 作为回调时，**Repeat Interval (ms)** 才可见。

#### 编程用法

将模块的 `RepeatInterval` 参数指定为正标量值。

|  |
| --- |
| **模块参数：** `RepeatInterval` |
| **类型：** scalar |

### Design

要自定义 dashboard 模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。

#### Button

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

#### States

### **Select State** — 选择要配置的状态 `Default` (default) | `Pressed` | `Latched` | `Latched and Pressed`

从 **States** 组件的 **Select State** 部分的下拉菜单中选择要配置的状态。当 **Button Type** 为 `Momentary` 时，可以选择以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块被按下时的模块状态

当 **Button Type** 为 `Latch` 时，可以选择以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您松开点击时，模块转换到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您松开点击时，模块转换到 `Default` 状态。

**注意**

可以为状态配置 **Design** 选项卡的 **States** 组件中的所有参数。例如，可以选择按钮处于该状态时将显示在按钮上的图标。当您配置 **States** 组件中的任何参数时，更改将应用于 **States** 组件的 **Select State** 部分中所选的状态。

**示例：** `Pressed`

### **Text** — 按钮标签文本 `'Button'` (default) | string | character array

指定按钮标签的文本。该标签应用于按钮在 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选的状态。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数：** `ButtonText` |
| **类型：** character vector | string |

### **Color** — 标签字体颜色 `[r g b]` vector

从标准颜色调色板中为标签文本选择字体颜色，或指定自定义颜色。颜色应用于 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选状态的标签文本。

### **Horizontal Alignment** — 标签和图标对与模块的水平对齐方式 `Left` (default) | `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。该表列出了 **X Offset** 为零时标签和图标对的水平位置。非零 **X Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐方式 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

### **Vertical Alignment** — 标签和图标对与模块的垂直对齐方式 `Center` (default) | `Bottom` | `Top`

设置标签和图标对在垂直方向上的对齐方式。该表列出了 **Y Offset** 为零时标签和图标对的垂直位置。非零 **Y Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐方式 | 标签和图标对的位置 |
| --- | --- |
| `Top` | 标签和图标对的顶边缘位于模块的顶边缘。 |
| `Center` | 标签和图标对的垂直中点位于模块的垂直中点。 |
| `Bottom` | 标签和图标对的底边缘位于模块的底边缘。 |

### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0` (default) | scalar

如何测量 **X Offset** 取决于 **Horizontal Alignment** 的值。该表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对水平中点相对于模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对右边缘相对于模块右边缘的水平偏移指定为模块宽度的比例。 |

### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0` (default) | `scalar`

如何测量 **Y Offset** 取决于 **Vertical Alignment** 的值。该表列出了每个 **Vertical Alignment** 值的偏移测量方式。相对于偏移为 `0` 时文本的位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

| **Vertical Alignment** | 偏移 |
| --- | --- |
| `Top` | 将标签和图标对顶边缘相对于模块顶边缘的垂直偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对垂直中点相对于模块垂直中点的垂直偏移指定为模块宽度的比例。 |
| `Bottom` | 将标签和图标对底边缘相对于模块底边缘的垂直偏移指定为模块宽度的比例。 |

### **Icon Placement** — 图标相对于标签的位置 `Left` (default) | `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐方式。

### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (default) | `off`

启用此选项以在使用 Property Inspector 调整图像大小时保持纵横比。

### **Image X Offset** — 图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Image Y Offset** — 图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例：** `0.5`

#### Background Image

### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

还可以在 Simulink 工具条的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，并格式化为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### Foreground Image

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持纵横比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成时会忽略 Dashboard 模块。

## 版本历史

**在 R2021b 中引入**

### R2025a：在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块表示的小工具交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块的大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 dashboard 面板的模块在面板于其自己的窗口中打开或已停靠且未锁定时也处于活动状态。对于至少一个由按下按钮触发的回调具有非空值的 Callback Button 模块，始终处于活动状态。要与非活动模块表示的小工具交互，可以通过点击该模块临时激活它。当您取消选择该模块时，该模块再次变为非活动状态。

点击活动的 Callback Button 模块或连接到参数或变量值的活动 Dashboard 或 Customizable Blocks 库模块，会同时选择该模块并与该模块表示的小工具交互。例如，点击未选择的活动已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后点击该模块，在不与小工具交互的情况下选择该模块。类似地，您可以通过按 **Shift** 然后双击该模块来打开 Block Parameters 对话框。

### R2024b：使用键盘解锁 dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板与面板所连接的模型一起打包，并部署为独立桌面应用或 Web 应用。您可以使用该应用操作控件并监视面板上的显示，而独立于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会在画布中覆盖模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window。

您可以将包含面板的新窗口与模型窗口分开最小化和还原。在面板窗口中，可以运行、暂停、停止和单步执行仿真。在面板窗口中，可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中单击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久 Panels 选项卡

将 dashboard 面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名所选面板。
- 可以隐藏所选面板。

### R2022b：支持在面板中撤消和重做可自定义 dashboard 模块

从 R2022b 开始，您可以撤消和重做对面板中可自定义 dashboard 模块所做的更改。

要撤消或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的 dashboard 模块。

当您单击面板中的 dashboard 模块时，该模块的工具条选项卡会出现。例如，当您单击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您单击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b：扩展对 Raspberry Pi 板上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 板上部署 **Customizable Blocks** 库中的这些模块：

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

您可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022b：扩展对 Android 设备上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署 **Customizable Blocks** 库中的这些模块：

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

您可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022a：调整前景图像的大小和位置

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整前景图像大小并重新定位前景图像。

## 描述

使用具有可自定义外观的按钮更改参数或变量值

Push Button 模块会更改所连接变量或参数的值，并响应点击（立即松开指针）或按下（延迟松开指针）执行 MATLAB® 代码。您可以为点击指定与按下不同的代码。当您按下按钮时，代码要么在您指定的时间跨度后执行，要么在您指定的时间间隔执行。当您在 Customizable Blocks 库中使用 Push Button 模块时，可以修改模块的外观，使其看起来像真实系统中的按钮。将 Push Button 模块与其他 dashboard 模块一起使用，可创建交互式 dashboard 来控制模型。

要在仿真期间按下虚拟按钮，请点击 Push Button 模块。要在仿真未运行时按下虚拟按钮，请点击 Push Button 以选择该模块，然后再次点击 Push Button 模块以按下按钮。当您为点击按下指针时，按钮被按下。当您松开指针时，您松开按钮。

可以使用回调函数指定希望按钮执行的操作：

- `PressFcn` 函数在按钮被按下期间运行。您可以将按钮配置为在按钮被按下期间仅运行一次 `PressFcn` 函数，也可以指定重复间隔。要仅运行一次，请将重复间隔指定为 `0`。
- `ClickFcn` 函数在您松开按钮时运行。

您可以通过将 **Button Type** 设置为 `Latched`，将按钮配置为在松开指针后保持按下状态。选择锁存按钮类型时：

- 要锁存按钮，请点击按钮。
- 要取消锁存按钮，请再次点击按钮。

`PressFcn` 函数在按钮被锁存期间运行。`ClickFcn` 函数在您锁存按钮时运行一次，并在您取消锁存按钮时运行一次。

可以使用状态来指定与按钮交互时 Push Button 模块外观的变化：

- 当您按下按钮时，模块处于 `Pressed` 状态。
- 当按钮已锁存且您未按下它时，模块处于 `Latched` 状态。
- 当按钮已锁存且您正在按下它时，模块处于 `Latched and Pressed` 状态。
- 当模块未处于这三个状态中的任何一个时，它处于 `Default` 状态。

状态将指针操作与以下内容配对：

- 状态标签
- 状态图标
- 状态图像

`Pressed`、`Latched` 和 `Latched and Pressed` 状态还会将指针操作与 Push Button 模块的 **On Value** 配对。当您从默认状态进入这些状态之一时，**On Value** 会赋值给 Push Button 模块所连接的 Simulink® 组件，并保持赋值，直到按钮返回到 `Default` 状态。如果在完整时间步过去之前松开按钮，则 **On Value** 会在后续时间步的持续时间内赋值给该组件。

**注意**

- 在仿真期间双击已连接的 Push Button 模块，或在点击该模块后双击，不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Push Button 模块会同时选择该模块并按下按钮。要在不按下按钮的情况下选择该模块，请按 **Shift**，然后点击该模块。

### 自定义 Push Button 模块

将 Push Button 模块添加到模型时，该模块会预配置为默认设计。您可以使用默认设计使用该模块，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink 工具条的模块特定选项卡上，在 **Design** 下，单击 **Edit**。
- 在 Property Inspector 的 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上出现的省略号上，然后单击 Edit Custom Block 按钮。

在设计模式中，可以使用模块上方的工具栏自定义 push button。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的 Customizable Push Button 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

自定义 Push Button 模块时，需要为每个状态配置模块外观。将 **Block Type** 配置为 `Momentary` 时，模块有两个状态。将 **Block Type** 配置为 `Latch` 时，模块有四个状态。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。

**自定义所选状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 为 `Pressed`、`Latched` 和 `Latched and Pressed` 状态指定 **On Value**。 | 否 | 是 |
| 指定状态标签文本。 | 否 | 是 |
| 指定状态标签文本的颜色和不透明度。 | 是 | 是 |
| 上传状态图像。 | 是 | 是 |
| 上传状态图标。 | 是 | 是 |
| 更改状态图像和状态图标的大小。 | 否 | 是 |
| 更改状态标签、状态图像和状态图标的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，还可以在画布中以交互方式调整组件的大小和位置。要调整特定于某个状态的组件（例如状态图像）的大小，请在工具栏中选择该状态，然后调整组件的大小或位置。

**应用于所有状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传背景图像。 | 否 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并单击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

还可以将 dashboard 模块连接到 Stateflow® 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Push 模块连接到您的模型。

未连接的 Push Button 模块连接到 Constant 模块。

### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
