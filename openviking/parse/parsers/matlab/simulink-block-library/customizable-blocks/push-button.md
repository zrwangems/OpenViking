---
type: simulink-block
title: 'Push Button'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'custompushbutton'
---

# Push Button

Change parameter or variable value using button with customizable appearance

## 中文

使用具有可自定义外观的按钮更改参数或变量值

### 库

Simulink / Dashboard / Customizable Blocks

### 说明

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

#### 自定义 Push Button 模块

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

#### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并单击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

还可以将 dashboard 模块连接到 Stateflow® 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Push 模块连接到您的模型。

未连接的 Push Button 模块连接到 Constant 模块。

#### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

### 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要为模块打开 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

### 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后单击 **Parameters** 选项卡。

#### Connection

#### **Connection** — 用于将模块参数值连接到参数值的连接选项

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

#### **Button Type** — 按钮对点击的响应 `Momentary` (default) | `Latch`

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

#### **Button Text** — 按钮标签文本 `'Button'` (default) | string | character array

指定按钮标签的文本。该标签应用于按钮在 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选的状态。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数：** `ButtonText` |
| **类型：** character vector | string |

#### **On value** — 按下或锁存按钮时赋值给已连接参数的值 `1` (default) | scalar

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

#### **Label** — 显示已连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

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

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会临时解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会临时锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

#### 回调

#### **ClickFcn** — 响应点击而执行的 MATLAB 代码 MATLAB code

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

#### **PressFcn** — 响应按下而执行的 MATLAB 代码 MATLAB code

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

#### **Press Delay (ms)** — 按住按钮以触发按下的时间 `500` (default) | scalar

使 `PressFcn` 代码执行所需的持续时间。

#### 依赖关系

仅当选择 `PressFcn` 作为回调时，**Press Delay (ms)** 才可见。

#### 编程用法

将模块的 `PressDelay` 参数指定为正标量值。

|  |
| --- |
| **模块参数：** `PressDelay` |
| **类型：** scalar |

#### **Repeat Interval (ms)** — 重复 `PressFcn` 代码的时间间隔 `0` (default) | scalar

如果 Callback Button 模块仍被按下，则 `PressFcn` 代码再次执行之后的时间间隔。

#### 依赖关系

仅当选择 `PressFcn` 作为回调时，**Repeat Interval (ms)** 才可见。

#### 编程用法

将模块的 `RepeatInterval` 参数指定为正标量值。

|  |
| --- |
| **模块参数：** `RepeatInterval` |
| **类型：** scalar |

#### Design

要自定义 dashboard 模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。

#### Button

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

#### States

#### **Select State** — 选择要配置的状态 `Default` (default) | `Pressed` | `Latched` | `Latched and Pressed`

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

#### **Text** — 按钮标签文本 `'Button'` (default) | string | character array

指定按钮标签的文本。该标签应用于按钮在 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选的状态。

#### 编程用法

将模块的 `ButtonText` 参数指定为字符串或字符向量。

|  |
| --- |
| **模块参数：** `ButtonText` |
| **类型：** character vector | string |

#### **Color** — 标签字体颜色 `[r g b]` vector

从标准颜色调色板中为标签文本选择字体颜色，或指定自定义颜色。颜色应用于 **Design** 选项卡上的 **States** 组件中 **Select State** 部分所选状态的标签文本。

#### **Horizontal Alignment** — 标签和图标对与模块的水平对齐方式 `Left` (default) | `Center` | `Right`

设置标签和图标对在水平方向上的对齐方式。该表列出了 **X Offset** 为零时标签和图标对的水平位置。非零 **X Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐方式 | 标签和图标对的位置 |
| --- | --- |
| `Left` | 标签和图标对的左边缘位于模块的左边缘。 |
| `Center` | 标签和图标对的水平中点位于模块的水平中点。 |
| `Right` | 标签和图标对的右边缘位于模块的右边缘。 |

#### **Vertical Alignment** — 标签和图标对与模块的垂直对齐方式 `Center` (default) | `Bottom` | `Top`

设置标签和图标对在垂直方向上的对齐方式。该表列出了 **Y Offset** 为零时标签和图标对的垂直位置。非零 **Y Offset** 会将标签和图标对从表中列出的位置移开。

| 对齐方式 | 标签和图标对的位置 |
| --- | --- |
| `Top` | 标签和图标对的顶边缘位于模块的顶边缘。 |
| `Center` | 标签和图标对的垂直中点位于模块的垂直中点。 |
| `Bottom` | 标签和图标对的底边缘位于模块的底边缘。 |

#### **Icon and Label X Offset** — 图标和标签对相对于模块的水平偏移 `0` (default) | scalar

如何测量 **X Offset** 取决于 **Horizontal Alignment** 的值。该表列出了每个 **Horizontal Alignment** 值的偏移测量方式。相对于偏移为 `0` 时的位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

| **Horizontal Alignment** | 偏移 |
| --- | --- |
| `Left` | 将标签和图标对左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对水平中点相对于模块水平中点的水平偏移指定为模块宽度的比例。 |
| `Right` | 将标签和图标对右边缘相对于模块右边缘的水平偏移指定为模块宽度的比例。 |

#### **Icon and Label Y Offset** — 图标和标签对相对于模块的垂直偏移 `0` (default) | `scalar`

如何测量 **Y Offset** 取决于 **Vertical Alignment** 的值。该表列出了每个 **Vertical Alignment** 值的偏移测量方式。相对于偏移为 `0` 时文本的位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

| **Vertical Alignment** | 偏移 |
| --- | --- |
| `Top` | 将标签和图标对顶边缘相对于模块顶边缘的垂直偏移指定为模块宽度的比例。 |
| `Center` | 将标签和图标对垂直中点相对于模块垂直中点的垂直偏移指定为模块宽度的比例。 |
| `Bottom` | 将标签和图标对底边缘相对于模块底边缘的垂直偏移指定为模块宽度的比例。 |

#### **Icon Placement** — 图标相对于标签的位置 `Left` (default) | `Top` | `Right` | `Bottom`

指定图标相对于标签的位置。

**注意**

更改图标的位置会移动标签，但不会更改标签的偏移或对齐方式。

#### **Icon Width** — 图标宽度 scalar

将图标宽度指定为标签文本字体高度的比例。

**示例：** `0.5`

#### **Icon Height** — 图标高度 scalar

将图标高度指定为标签文本字体高度的比例。

**示例：** `0.5`

#### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (default) | `off`

启用此选项以在使用 Property Inspector 调整图像大小时保持纵横比。

#### **Image X Offset** — 图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

#### **Image Y Offset** — 图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

#### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例：** `0.5`

#### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例：** `0.5`

#### Background Image

#### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

#### **Color** — 模块背景颜色 `[r g b]` vector

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

#### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.5`

#### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### Foreground Image

#### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

#### **Y Offset** — 前景图像顶边缘相对于模块顶边缘的垂直偏移 scalar

将图像顶边缘相对于模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例：** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例：** `0.5`

#### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持纵横比。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成时会忽略 Dashboard 模块。

### 版本历史

**在 R2021b 中引入**

#### R2025a：在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块表示的小工具交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块的大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 dashboard 面板的模块在面板于其自己的窗口中打开或已停靠且未锁定时也处于活动状态。对于至少一个由按下按钮触发的回调具有非空值的 Callback Button 模块，始终处于活动状态。要与非活动模块表示的小工具交互，可以通过点击该模块临时激活它。当您取消选择该模块时，该模块再次变为非活动状态。

点击活动的 Callback Button 模块或连接到参数或变量值的活动 Dashboard 或 Customizable Blocks 库模块，会同时选择该模块并与该模块表示的小工具交互。例如，点击未选择的活动已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后点击该模块，在不与小工具交互的情况下选择该模块。类似地，您可以通过按 **Shift** 然后双击该模块来打开 Block Parameters 对话框。

#### R2024b：使用键盘解锁 dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您松开 **Shift** 键时，纵横比锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。当您松开 **Shift** 键时，纵横比解锁。

#### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板与面板所连接的模型一起打包，并部署为独立桌面应用或 Web 应用。您可以使用该应用操作控件并监视面板上的显示，而独立于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

#### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会在画布中覆盖模型图。

有关详细信息，请参阅 Dock Panels。

#### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window。

您可以将包含面板的新窗口与模型窗口分开最小化和还原。在面板窗口中，可以运行、暂停、停止和单步执行仿真。在面板窗口中，可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中单击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

#### R2023a：Simulink 工具条中的持久 Panels 选项卡

将 dashboard 面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名所选面板。
- 可以隐藏所选面板。

#### R2022b：支持在面板中撤消和重做可自定义 dashboard 模块

从 R2022b 开始，您可以撤消和重做对面板中可自定义 dashboard 模块所做的更改。

要撤消或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

#### R2022b：对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的 dashboard 模块。

当您单击面板中的 dashboard 模块时，该模块的工具条选项卡会出现。例如，当您单击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您单击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2022b：扩展对 Raspberry Pi 板上可自定义 Dashboard 模块的支持

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

#### R2022b：扩展对 Android 设备上可自定义 Dashboard 模块的支持

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

#### R2022a：调整前景图像的大小和位置

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整前景图像大小并重新定位前景图像。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

The Push Button block changes the value of the connected variable or
parameter and executes MATLAB® code in response to a click (immediate release of the pointer) or a press
(delayed release of the pointer). You can specify different code for the click than the press.
When you press the button, the code either executes after a time span you specify or at time
intervals you specify. When you use the Push Button block in the Customizable
Blocks library, you can modify the appearance of the block so it looks like a button in a real
system. Use the Push Button block with other dashboard blocks to create an
interactive dashboard to control your model.

To push the virtual button during simulation, click the Push Button block.
To push the virtual button when the simulation is not running, click the Push
Button to select the block, and then click the Push Button block
again to push the button. While you press down your pointer for the click, the button is
pushed. When you release your pointer, you release the button.

You can use callback functions to specify what you want the button to do:

- `PressFcn` functions run while the button is pushed. You can
  configure the button to run the `PressFcn` function only once while the
  button is pushed, or you can specify a repeat interval. To run the function only once,
  specify a repeat interval of `0`.
- `ClickFcn` functions run when you release the button.

You can configure the button to stay pushed when you release your pointer by setting the
**Button Type** to `Latched`. When you choose the latched
button type:

- To latch the button, click the button.
- To unlatch the button, click the button again.

The `PressFcn` function runs while the button is latched. The
`ClickFcn` function runs once when you latch the button and once when you
unlatch the button.

You can use states to specify how the appearance of the Push Button block
changes when you interact with the button:

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

The `Pressed`, `Latched`, and
`Latched and Pressed` states also pair pointer actions with the
**On Value** of the Push Button block. When you enter one of
these states from the default state, the **On Value** is assigned to the
Simulink® component to which the Push Button block connects and stays
assigned until the button returns to the `Default` state. If you
release the button before a full time step elapses, the **On Value** is
assigned to the component for the duration of the subsequent time step.

**Note**

- Double-clicking a connected Push Button block during simulation or
  after clicking the block does not open the Block Parameters dialog box. To open the
  Block Parameters dialog box, press **Shift**, then double-click the
  block.
- Clicking a connected Push Button block during simulation both selects
  the block and pushes the button. To select the block without pushing the button, press
  **Shift**, then click the block.

### Customize Push Button Blocks

When you add a Push Button block to your model, the block is
preconfigured with a default design. You can use the block with the default design or
customize the appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the push button. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Push Button block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Push Button block, you configure the block
appearance for each state. When you configure the **Block Type** as
`Momentary`, the block has two states. When you configure the
**Block Type** as `Latch`, the block has four.
To select a state to customize, use the drop-down list in the toolbar. Alternatively, on the
**Design** tab, select the **States** component and then
select from the **Select State** list.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the **On Value** for the `Pressed`, `Latched`, and `Latched and Pressed` states. | No | Yes |
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

This animation shows how to connect the Push block to your model.

An unconnected Push Button block connects to a Constant block.

### Parameter Logging

Tunable parameters connected to dashboard blocks are logged to the Simulation Data
Inspector, where you can view the parameter values along with logged signal data. You can
access logged parameter data in the MATLAB workspace by exporting the parameter data from the Simulation Data Inspector
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

### **Button Text** — Button label text `'Button'` (default) | string | character array

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

### **On value** — Value assigned to connected parameter when button is pressed or latched `1` (default) | scalar

The value assigned to the connected block parameter when the button is pressed or
latched.

**Tip**

Use the **Block Type** parameter to configure how the block
responds to a click:

- `Momentary` — The button applies the
  **On Value** only while you press it.
- `Latch` — The button latches the state change
  when you click it and applies the **On value** until
  you click it again.

#### Programmatic Use

Specify the `OnValue` parameter for the block as a scalar value
that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `OnValue` |
| **Type:** string or character array |
| **Values:** scalar |
| **Default:** `'1'` |

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

### **Text** — Button label text `'Button'` (default) | string | character array

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

**Introduced in R2021b**

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

### R2024a: Deploy dashboard panel as web app or standalone desktop app

With a Simulink
Compiler™ license, you can now deploy a dashboard panel, packaged with the model to
which the panel connects, as a standalone desktop app or as a web app. You can use the app
to operate the controls and monitor the displays on the panel independent of Simulink.

To learn how to deploy panels, see Deploy Dashboard Panel as App.

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

### R2022b: Extended support for customizable Dashboard blocks on Raspberry Pi boards

Starting in R2022b, the Simulink Support Package for Raspberry Pi® Hardware supports deploying these blocks from the **Customizable
Blocks** library on your Raspberry Pi boards:

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

You can customize the visual aspects of the blocks in a Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on a
web browser you launch from a Raspberry Pi terminal.

### R2022b: Extended support for customizable Dashboard blocks on Android devices

Starting in R2022b, the Simulink Support Package for Android® Devices supports deploying these blocks from the **Customizable
Blocks** library on your Android devices:

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

You can customize the visual aspects of the blocks in a Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on
your Android device as well as on your web browser.

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.
