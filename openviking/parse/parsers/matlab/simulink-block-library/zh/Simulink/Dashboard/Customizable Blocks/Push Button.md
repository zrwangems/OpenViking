---
type: simulink-block
title: 'Push Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'custompushbutton'
documentation_source_path: 'slref/custompushbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Push Button

## 端口

R2025b 中未记录。

## 参数

使用属性检查器和模块参数对话框指定模块参数的值。要设置仪表板模块的核心参数，请使用模块参数对话框或属性检查器中的**参数**选项卡。要自定义模块，请使用属性检查器中的**设计**选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在**建模**选项卡上的**设计**下，选择**属性检查器**。

### 参数

要设置仪表板模块的核心参数，请打开属性检查器并点击**参数**选项卡。

#### 连接

### **Connection** — 要连接的模块参数值 参数值连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或模块参数对话框中的**Connection**表。要从属性检查器打开模块参数对话框，请在**Connected to**右侧点击**Connect**或**Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用**Connection**表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**Connect**。要更改该模块的连接，请改为点击**Change**。
3. 选择要将其参数值连接到的模块。
4. 在表中，选择要连接到的参数。
5. 点击**Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按**Ctrl+D**更新模型图。

您还可以将仪表板模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表板模块连接到由值定义的参数，某些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.ParamSourceInfo` |
| **默认值**：`[]` |

#### 主要

### **Button Type** — 按钮对点击的响应 `Momentary`（默认）| `Latch`

指定模块如何响应点击。

- `Momentary` — 按钮仅在按下时改变状态。当您释放点击时，按钮返回其默认状态。
- `Latch` — 按钮在点击时锁存状态变化。按钮保持按下状态，直到您再次点击它。

当您将 **Button Type** 配置为 `Momentary` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块按下时的模块状态

当您将 **Button Type** 配置为 `Latch` 时，模块具有以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您释放点击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您释放点击时，模块过渡到 `Default` 状态。

#### 编程使用

|  |
| --- |
| **模块参数**：`ButtonType` |
| **类型**：string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

### **Button Text** — 按钮标签文本 `'Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于**设计**选项卡上 **States** 组件的 **Select State** 部分中所选状态的按钮。

#### 编程使用

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数**：`ButtonText` |
| **类型**：character vector | string |

### **On value** — 按钮按下或锁存时分配给已连接参数的值 `1`（默认）| scalar

按钮按下或锁存时分配给已连接模块参数的值。

**提示**

使用 **Block Type** 参数配置模块如何响应点击：

- `Momentary` — 按钮仅在您按下时应用 **On Value**。
- `Latch` — 按钮在您点击时锁存状态变化，并应用 **On value** 直到您再次点击它。

#### 编程使用

将模块的 `OnValue` 参数指定为格式化为字符串或字符向量的标量值。

|  |
| --- |
| **模块参数**：`OnValue` |
| **类型**：string or character array |
| **值**：scalar |
| **默认值**：`'1'` |

### **Label** — 显示已连接元素名称的标签位置 `Hide`（默认）| `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示仪表板模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适应模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

#### 回调

### **ClickFcn** — 响应点击而执行的 MATLAB 代码 MATLAB 代码

响应按钮点击而执行的 MATLAB 代码。

每次您点击按钮时，`ClickFcn` 代码执行一次，执行时间为您释放点击的时间点。

要为 `ClickFcn` 指定代码，请从下拉菜单中选择 `ClickFcn`。在菜单下方的文本框中输入代码。

#### 编程使用

将模块的 `ClickFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数**：`ClickFcn` |
| **类型**：character vector | string |
| **值**：MATLAB code |

### **PressFcn** — 响应按下而执行的 MATLAB 代码 MATLAB 代码

响应按钮按下而执行的 MATLAB 代码。

当按钮处于按下状态时，`PressFcn` 代码在 **Press Delay** 时间过去后执行一次，并在每个 **Repeat Interval** 周期性地执行。

要为 `PressFcn` 指定代码，请从下拉菜单中选择 `PressFcn`。在菜单下方的文本框中输入代码。

您如何按下按钮以执行 `PressFcn` 代码取决于 **Button Type**。

- 如果 **Button Type** 为 `Momentary`，请按住点击，持续您想要按下按钮的时间。
- 如果 **Button Type** 为 `Latch`，请点击以按下按钮，但不要按住点击。按钮保持按下状态，直到您再次点击它。

**注意**

每次您点击按钮时，即使是在按下按钮的过程中，`ClickFcn` 代码也会执行一次，执行时间为您释放点击的时间点。

#### 编程使用

将模块的 `PressFcn` 参数指定为格式化为字符串或字符向量的 MATLAB 代码。

|  |
| --- |
| **模块参数**：`PressFcn` |
| **类型**：character vector | string |
| **值**：MATLAB code |

### **Press Delay (ms)** — 按下按钮所需保持的时间 `500`（默认）| scalar

导致 `PressFcn` 代码执行所需的时间量。

#### 依赖关系

**Press Delay (ms)** 仅在 `PressFcn` 被选为回调时可见。

#### 编程使用

将模块的 `PressDelay` 参数指定为正标量值。

|  |
| --- |
| **模块参数**：`PressDelay` |
| **类型**：scalar |

### **Repeat Interval (ms)** — 重复 `PressFcn` 代码的时间间隔 `0`（默认）| scalar

如果 Callback Button 模块仍被按下，`PressFcn` 代码再次执行的时间间隔。

#### 依赖关系

**Repeat Interval (ms)** 仅在 `PressFcn` 被选为回调时可见。

#### 编程使用

将模块的 `RepeatInterval` 参数指定为正标量值。

|  |
| --- |
| **模块参数**：`RepeatInterval` |
| **类型**：scalar |

### 设计

要自定义仪表板模块，请打开属性检查器，点击**设计**选项卡，然后点击**Edit**。

#### 按钮

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适应模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

#### 状态

### **Select State** — 选择要配置的状态 `Default`（默认）| `Pressed` | `Latched` | `Latched and Pressed`

从 **States** 组件的 **Select State** 部分的下拉菜单中选择要配置的状态。当 **Button Type** 为 `Momentary` 时，您可以选择以下状态：

- `Default` — 模块未按下时的默认状态
- `Pressed` — 模块按下时的模块状态

当 **Button Type** 为 `Latch` 时，您可以选择以下状态：

- `Default` — 模块未按下时的默认状态。
- `Pressed` — 当按钮处于 `Default` 状态时按下按钮的过渡状态。当您释放点击时，模块过渡到 `Latched` 状态。
- `Latched` — 模块未按下时的锁存状态。
- `Latched and Pressed` — 当按钮处于 `Latched` 状态时按下按钮的过渡状态。当您释放点击时，模块过渡到 `Default` 状态。

**注意**

您可以为某个状态配置**设计**选项卡的 **States** 组件中的所有参数。例如，您可以选择按钮处于该状态时显示在按钮上的图标。当您配置 **States** 组件中的任何参数时，更改将应用于 **States** 组件的 **Select State** 部分中所选的状态。

**示例：** `Pressed`

### **Text** — 按钮标签文本 `'Button'`（默认）| string | character array

指定按钮标签的文本。该标签应用于**设计**选项卡上 **States** 组件的 **Select State** 部分中所选状态的按钮。

#### 编程使用

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数**：`ButtonText` |
| **类型**：character vector | string |

### **Color** — 标签字体颜色 `[r g b]` 向量

从标准颜色调色板中为标签文本选择字体颜色，或指定自定义颜色。该颜色应用于**设计**选项卡上 **States** 组件的 **Select State** 部分中所选状态的标签文本。

### **Horizontal Alignment** — 标签和图标对与模块的水平对齐 `Left`（默认）| `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。下表列出了当 **X Offset** 为零时标签和图标对的水平位置。非零的 **X Offset** 会将标签和图标对从表中列出的位置移动。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

### **Vertical Alignment** — 标签和图标对与模块的垂直对齐 `Center`（默认）| `Bottom` | `Top`

设置标签和图标对在垂直方向上的对齐方式。下表列出了当 **Y Offset** 为零时标签和图标对的垂直位置。非零的 **Y Offset** 会将标签和图标对从表中列出的位置移动。

| 对齐 | 标签和图标对的位置 |
| --- | --- |
| `Top` | 标签和图标对的顶边缘位于模块的顶边缘。 |
| `Center` | 标签和图标对的垂直中点位于模块的垂直中点。 |
| `Bottom` | 标签和图标对的底边缘位于模块的底边缘。 |

### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0`（默认）| scalar

**X Offset** 的测量方式取决于 **Horizontal Alignment** 的值。下表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负值偏移将文本向左移动，正值偏移将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对的左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的水平中点相对于模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对的右边缘相对于模块右边缘的水平偏移指定为模块宽度的比例。 |

### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0`（默认）| `scalar`

**Y Offset** 的测量方式取决于 **Vertical Alignment** 的值。下表列出了每个 **Vertical Alignment** 值对应的偏移测量方式。相对于偏移为 `0` 时文本的位置，负值偏移将文本上移，正值偏移将文本下移。

| **Vertical Alignment** | 偏移 |
| --- | --- |
| `Top` | 将标签和图标对的顶边相对于模块顶边的垂直偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对的垂直中心相对于模块垂直中心的垂直偏移指定为模块宽度的比例。 |
| `Bottom` | 将标签和图标对的底边相对于模块底边的垂直偏移指定为模块宽度的比例。 |

### **Icon Placement** — 图标相对于标签的位置 `Left`（默认）| `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐方式。

### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持图像宽高比的选项 `on`（默认）| `off`

启用此选项可在使用属性检查器调整图像大小时保持宽高比。

### **Image X Offset** — 图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像左移，正值偏移将图像右移。

**示例：** `1`

### **Image Y Offset** — 图像顶边相对于模块顶边的垂直偏移 scalar

将图像顶边相对于模块顶边的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像上移，正值偏移将图像下移。

**示例：** `1`

### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例：** `0.5`

#### Background Image

### **Use Background Color** — 指定纯色模块背景色的选项 `off`（默认）| `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要使用纯色背景，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您也可以在 Simulink 工具条的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型**：string | character vector |
| **值**：`[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1`（默认）| scalar

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.5`

### **Corner Radius** — 模块背景色区域的圆角半径 scalar

将模块背景色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### Foreground Image

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像左移，正值偏移将图像右移。

**示例：** `1`

### **Y Offset** — 前景图像顶边相对于模块顶边的垂直偏移 scalar

将图像顶边相对于模块顶边的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像上移，正值偏移将图像下移。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持前景图像宽高比的选项 `on`（默认）| `off`

选择此参数可在使用属性检查器调整图像大小时保持宽高比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2021b 中引入**

### R2025a：在仿真期间选择仪表板模块并打开 Block Parameters 对话框

当 Dashboard 或 Customizable Blocks 库中的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的控件进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与模块本身进行交互。例如，您可以移动或调整模块大小。默认情况下，Dashboard 和 Customizable Blocks 库中的所有模块在仿真期间均处于活动状态。提升到仪表板面板的模块在面板于其自身窗口中打开或停靠且未锁定时也处于活动状态。对于 Callback Button 模块，如果按下按钮触发的至少一个回调具有非空值，则该模块始终处于活动状态。要与非活动模块所代表的控件进行交互，您可以通过点击该模块临时激活它。当您取消选择该模块时，模块将再次变为非活动状态。

点击活动的 Callback Button 模块或连接到参数或变量值的 Dashboard 或 Customizable Blocks 库中的活动模块，既会选择该模块，也会与该模块所代表的控件进行交互。例如，点击未选中的活动已连接 Push Button 模块既会选择该模块，也会按下按钮。从 R2025a 开始，您可以通过按住 **Shift** 然后点击模块来选择模块而不与控件交互。同样，您可以通过按住 **Shift** 然后双击模块来打开 Block Parameters 对话框。

### R2024b：使用键盘解锁仪表板模块宽高比

如果 Dashboard 库中模块的宽高比已锁定，您可以通过按住 **Shift** 临时解锁宽高比。当您释放 **Shift** 键时，宽高比将锁定。

如果宽高比已解锁，按住 **Shift** 将临时锁定宽高比。当您释放 **Shift** 键时，宽高比将解锁。

### R2024a：将仪表板面板部署为 Web 应用或独立桌面应用

拥有 Simulink Compiler™ 许可证后，您现在可以将仪表板面板（与其所连接的模型一起打包）部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监控显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠仪表板面板

从 R2024a 开始，您可以将仪表板面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监控信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

您可以独立于模型窗口最小化和恢复包含面板的新窗口。从面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久 Panels 选项卡

当您将仪表板面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，**Panels** 选项卡在未选中面板时保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名选中的面板。
- 您可以隐藏选中的面板。

### R2022b：面板中可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command**（⌘）而不是 **Ctrl**。

### R2022b：工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的仪表板模块。

当您点击面板中的仪表板模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适配到当前视图中。
- 折叠选中的面板。
- 自定义面板的大小和内容。
- 为选中的面板设置自定义背景图像。
- 为选中的面板添加新选项卡。

### R2022b：扩展对 Raspberry Pi 板上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 板上部署 **Customizable Blocks** 库中的以下模块：

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

您可以在 Simulink 模型中自定义模块的视觉外观，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得（WYSIWYG）的可视化效果。

### R2022b：扩展对 Android 设备上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署 **Customizable Blocks** 库中的以下模块：

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

您可以在 Simulink 模型中自定义模块的视觉外观，并在您的 Android 设备以及 Web 浏览器上获得所见即所得（WYSIWYG）的可视化效果。

### R2022a：调整前景图像大小和重新定位

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整大小和重新定位前景图像。

## 描述

使用具有可自定义外观的按钮更改参数或变量值

Push Button 模块会更改所连接变量或参数的值，并响应点击（立即释放指针）或按下（延迟释放指针）执行 MATLAB® 代码。您可以为点击指定与按下不同的代码。当您按下按钮时，代码要么在您指定的时间跨度后执行，要么在您指定的时间间隔执行。当您在 Customizable Blocks 库中使用 Push Button 模块时，可以修改模块的外观，使其看起来像真实系统中的按钮。将 Push Button 模块与其他仪表板模块一起使用，可创建交互式仪表板来控制您的模型。

要在仿真期间按下虚拟按钮，请点击 Push Button 模块。要在仿真未运行时按下虚拟按钮，请点击 Push Button 以选中该模块，然后再次点击 Push Button 模块以按下按钮。当您为点击而按下指针时，按钮被按下。当您释放指针时，您释放了按钮。

您可以使用回调函数来指定希望按钮执行的操作：

- `PressFcn` 函数在按钮被按下时运行。您可以将按钮配置为在按钮被按下时仅运行一次 `PressFcn` 函数，也可以指定重复间隔。要仅运行一次该函数，请将重复间隔指定为 `0`。
- `ClickFcn` 函数在您释放按钮时运行。

您可以通过将 **Button Type** 设置为 `Latched`，将按钮配置为在您释放指针时保持按下状态。当您选择锁存按钮类型时：

- 要锁存按钮，请点击该按钮。
- 要取消锁存按钮，请再次点击该按钮。

`PressFcn` 函数在按钮被锁存时运行。`ClickFcn` 函数在您锁存按钮时运行一次，并在您取消锁存按钮时运行一次。

您可以使用状态来指定当您与按钮交互时 Push Button 模块的外观如何变化：

- 当您按下按钮时，模块处于 `Pressed` 状态。
- 当按钮被锁存且您未按下它时，模块处于 `Latched` 状态。
- 当按钮被锁存且您正在按下它时，模块处于 `Latched and Pressed` 状态。
- 当模块不处于这三种状态中的任何一种时，它处于 `Default` 状态。

一个状态将指针操作与以下内容配对：

- 状态标签
- 状态图标
- 状态图像

`Pressed`、`Latched` 和 `Latched and Pressed` 状态还会将指针操作与 Push Button 模块的 **On Value** 配对。当您从默认状态进入这些状态之一时，**On Value** 会被赋给 Push Button 模块所连接的 Simulink® 组件，并保持赋值状态，直到按钮返回到 `Default` 状态。如果您在完整时间步过去之前释放按钮，**On Value** 会在后续时间步的持续时间内赋给该组件。

**注意**

- 在仿真期间或点击已连接的 Push Button 模块后，双击该模块不会打开“模块参数”对话框。要打开“模块参数”对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Push Button 模块会同时选中该模块并按下按钮。要在不按下按钮的情况下选中该模块，请按 **Shift**，然后点击该模块。

### 自定义 Push Button 模块

当您将 Push Button 模块添加到模型时，该模块已预配置为默认设计。您可以将该模块与默认设计一起使用，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选中模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink 工具条中，在模块特定选项卡上的 **Design** 下，点击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式下，您可以使用模块上方的工具栏来自定义按钮。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的可自定义 Push Button 模块，工具栏和属性检查器中的 Design 选项卡可见。

当您自定义 Push Button 模块时，您会为每个状态配置模块外观。当您将 **Block Type** 配置为 `Momentary` 时，模块有两个状态。当您将 **Block Type** 配置为 `Latch` 时，模块有四个状态。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。

**自定义所选状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 为 `Pressed`、`Latched` 和 `Latched and Pressed` 状态指定 **On Value**。 | 否 | 是 |
| 指定状态标签文本。 | 否 | 是 |
| 指定状态标签文本的颜色和不透明度。 | 是 | 是 |
| 上传状态图像。 | 是 | 是 |
| 上传状态图标。 | 是 | 是 |
| 更改状态图像和状态图标的大小。 | 否 | 是 |
| 更改状态标签、状态图像和状态图标的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和重新定位组件。要调整特定于某个状态的组件（例如状态图像）的大小，请在工具栏中选择该状态，然后调整组件大小或重新定位组件。

**适用于所有状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传背景图像。 | 否 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选中该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，并点击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Push 模块连接到您的模型。

未连接的 Push Button 模块连接到 Constant 模块。

### 参数记录

连接到仪表板模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
