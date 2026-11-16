---
type: simulink-block
title: 'Rocker Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Customizable Blocks'
documentation_page: 'customrockerswitch'
documentation_source_path: 'slref/customrockerswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Rocker Switch



使用具有可自定义外观的开关更改参数或变量值

## 库

Simulink / Dashboard / Customizable Blocks

## 描述

使用 Rocker Switch 模块在仿真之前或仿真期间更改所连接变量或参数的值。当您在 Customizable Blocks 库中使用 Rocker Switch 模块时，您可以自定义模块外观，使其看起来像您系统中的真实开关。您可以将开关配置为具有任意数量的状态以自定义行为。例如，您可以设计三向拨动开关或变速箱。将 Rocker Switch 模块与其他 dashboard 模块一起使用，为模型创建交互式仪表板。

真实的翘板开关具有多个设置。Rocker Switch 模块将这些设置视为不同状态。一个状态将状态值与图像、点击区域以及显示在点击区域上的状态标签配对。

要在仿真期间激活某个状态，请点击该状态的点击区域。要在仿真未运行时激活某个状态，请点击 Rocker Switch 模块以选择该模块，然后点击该状态的点击区域。当您激活该状态时，状态值会赋给 Rocker Switch 模块所连接的 Simulink® 模块图元素。

**注意**

- 在仿真期间或点击相连的 Rocker Switch 模块后，双击该模块不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击相连的 Rocker Switch 模块会同时选择该模块并移动开关。要选择模块而不移动开关，请按 **Shift**，然后点击该模块。

### 自定义 Rocker Switch 模块

当您将 Rocker Switch 模块添加到模型时，该模块预配置了默认设计。您可以使用默认设计使用该模块，也可以自定义模块外观。

要自定义模块外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink Toolstrip 中，在模块专属选项卡上的 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义翘板开关。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的可自定义 Rocker Switch 模块，显示工具栏和 Property Inspector 中的 Design 选项卡。

当您自定义 Rocker Switch 模块时，您为每个状态配置模块外观。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。要添加状态，请在工具栏中点击 Add State 按钮 。要删除状态，请点击 Remove State 按钮 。

**自定义所选状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 指定状态值。 | No | Yes |
| 指定状态标签文本和颜色。 | No | Yes |
| 添加或删除状态。 | Yes | Yes |
| 上传用于定义模块在该状态下外观的状态图像。 | Yes | Yes |
| 更改状态图像和点击区域的大小。 | No | Yes |
| 更改状态标签、状态图像和点击区域的位置。 | No | Yes |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和位置。要调整某个状态特有的组件（例如状态图像）的大小，请在工具栏中选择该状态，然后调整组件大小或位置。

**适用于所有状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传背景图像。 | No | Yes |
| 设置纯色背景色。 | No | Yes |
| 上传前景图像。 | No | Yes |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Rocker Switch 模块连接到模型。

未连接的 Rocker Switch 模块连接到 Constant 模块。

### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，以在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

## 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### 连接

### **Connection** — 用于连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关连接模式以及如何使用 toolstrip 连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 程序化使用

要以程序化方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 dashboard 模块连接到由值定义的参数，某些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

#### 主要

### **Label** — 显示所连接元素名称的标签位置 `Hide` (默认) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果希望标签可见，请指定标签位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适应模块大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

### **States** — 值与标签的配对 scalar and character vector

每个状态将一个 **State Value** 与一个 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。您可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关有两个状态，分别对应每个开关位置：

- 在 `Off` 状态下，模块将所连接的变量或参数赋值为 `0`。
- 在 `On` 状态下，模块将所连接的变量或参数赋值为 `1`。

您可以使用可自定义开关模块设计具有大于或等于 1 的任意数量状态的开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **-** 按钮。

**提示**

除了值和标签之外，您还可以在设计模式中为状态配置各种其他参数。例如，您可以选择开关处于该状态时显示的图像。要在设计模式中配置参数：

1. 选择开关模块。
2. 进入设计模式。在 Property Inspector 的 **Design** 选项卡上，点击 **Edit** 按钮。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 使用模块上方的工具栏，或在 Property Inspector 的 **Design** 选项卡上的 **States** 组件中，配置所选状态的参数值。

#### 程序化使用

要以程序化方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素的结构体数组，其字段为：

- `Value` — 该状态的 scalar double 值。
- `Label` — 用作开关位置标签的 string 或 character array。

    leftState.Value = 0;
    leftState.Label = 'Off';
    rightState.Value = 1;
    rightState.Label = 'On';
    switchStates = [leftState rightState];

|  |
| --- |
| **模块参数：** `States` |
| **类型：** two element array of structures |

### 设计

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### 开关

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适应模块大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

#### 状态

### **Select State** — 状态的管理和配置 scalar and character vector

每个状态将一个 **State Value** 与一个 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。您可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关有两个状态，分别对应每个开关位置：

- 在 `Off` 状态下，模块将所连接的变量或参数赋值为 `0`。
- 在 `On` 状态下，模块将所连接的变量或参数赋值为 `1`。

您可以使用可自定义开关模块设计具有大于或等于 1 的任意数量状态的开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **X** 按钮。

要配置状态，请在 **States** 组件中展开 **Select State** 部分，然后选择该状态。

您可以在 Property Inspector 的 **Design** 选项卡上的 **States** 组件中，为所选状态配置值、标签文本以及各种其他参数。例如，您可以选择开关处于该状态时显示的图像。

您在 **States** 组件中对参数值所做的所有更改仅应用于所选状态。要配置其他状态，请在 **Select State** 部分的下拉菜单中选择该状态。然后，在 **States** 组件中配置该状态的参数值。

**提示**

或者，您可以：

- 使用设计模式中出现在开关模块上方的工具栏配置所选状态的参数
- 使用 Property Inspector 中的 **Parameters** 选项卡配置模块状态的值和标签文本

#### 程序化使用

要以程序化方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素的结构体数组，其字段为：

- `Value` — 该状态的 scalar double 值。
- `Label` — 用作开关位置标签的 string 或 character array。

    leftState.Value = 0;
    leftState.Label = 'Off';
    rightState.Value = 1;
    rightState.Label = 'On';
    switchStates = [leftState rightState];

|  |
| --- |
| **模块参数：** `States` |
| **类型：** two element array of structures |

### **Value** — 状态值 scalar

每个状态将一个 **State Value** 与一个 **State Label** 配对。指定在 **Design** 选项卡中所选状态的 **State Value**。

### **Text** — 状态标签文本 string | character array

每个状态将一个 **State Value** 与一个 **State Label** 配对。指定在 **Design** 选项卡中所选状态的 **State Label** 文本。

### **Color** — 标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择标签文本的字体颜色，或指定自定义颜色。该颜色会应用于 **Design** 选项卡上 **States** 组件的 **Select State** 部分中所选状态的标签文本。

### **Label X Offset** — 文本中心距模块左边缘的水平偏移 `scalar`

将 **State Label** 中心的水平偏移指定为模块宽度的比例，从模块左边缘算起。相对于偏移为 `0` 时的文本位置，负偏移值会将文本向左移动，正偏移值会将文本向右移动。

### **Label Y Offset** — 文本中心距模块上边缘的垂直偏移 `scalar`

将 **State Label** 中心的垂直偏移指定为模块高度的比例，从模块上边缘算起。相对于偏移为 `0` 时的文本位置，负偏移值会将文本向上移动，正偏移值会将文本向下移动。

### **Image X Offset** — 图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘的水平偏移指定为模块宽度的比例，从模块左边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向左移动，正偏移值会将图像向右移动。

**示例：** `1`

### **Image Y Offset** — 图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘的垂直偏移指定为模块高度的比例，从模块上边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向上移动，正偏移值会将图像向下移动。

**示例：** `1`

### **Image Width** — 图像宽度 scalar

将图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Image Height** — 图像高度 scalar

将图像高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持图像纵横比的选项 `on` (默认) | `off`

启用此选项可在使用 Property Inspector 调整图像大小时保持纵横比。

### **Click Area X Offset** — 点击区域左边缘距模块左边缘的水平偏移 scalar

将点击区域左边缘的水平偏移指定为模块宽度的比例，从模块左边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向左移动，正偏移值会将图像向右移动。

**示例：** `1`

### **Click Area Y Offset** — 点击区域上边缘距模块上边缘的垂直偏移 scalar

将点击区域上边缘的垂直偏移指定为模块高度的比例，从模块上边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向上移动，正偏移值会将图像向下移动。

**示例：** `1`

### **Click Area Width** — 点击区域宽度 scalar

将点击区域宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Click Area Height** — 点击区域高度 scalar

将点击区域高度指定为模块高度的比例。

**示例：** `0.5`

#### 背景图像

### **Use Background Color** — 用于指定模块纯色背景色的选项 `off` (默认) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景色会移除背景图像，并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景色 `[r g b]` vector

要使用纯色背景色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 程序化使用

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，并格式化为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (默认) | scalar

将模块背景不透明度指定为 `0` 到 `1` 之间的 scalar 值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景色的区域的圆角半径 scalar

将模块背景色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘的水平偏移指定为模块宽度的比例，从模块左边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向左移动，正偏移值会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘的垂直偏移指定为模块高度的比例，从模块上边缘算起。相对于偏移为 `0` 时的图像位置，负偏移值会将图像向上移动，正偏移值会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像纵横比的选项 `on` (默认) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成会忽略 Dashboard 模块。

## 版本历史

**R2021b 中引入**

### R2025a：在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当 Dashboard 或 Customizable Blocks 库中的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的小工具交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块大小。默认情况下，Dashboard 和 Customizable Blocks 库中的所有模块在仿真期间都处于活动状态。提升到 dashboard panel 的模块在面板于其自己的窗口中打开或停靠且解锁时也处于活动状态。对于 Callback Button 模块，如果按下按钮触发的至少一个回调具有非空值，则该模块始终处于活动状态。要与非活动模块所代表的小工具交互，您可以通过点击该模块临时激活它。当您取消选择该模块时，该模块会再次变为非活动状态。

点击活动的 Callback Button 模块，或点击连接到参数或变量值的 Dashboard 或 Customizable Blocks 库中的活动模块，会同时选择该模块并与其代表的小工具交互。例如，点击未选择的活动的已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后点击该模块来选择模块而不与小工具交互。类似地，您可以通过按 **Shift** 然后双击该模块来打开 Block Parameters 对话框。

### R2024b：使用键盘解锁 dashboard 模块纵横比

如果 Dashboard 库中模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

### R2024a：将 dashboard panel 部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard panel（与其所连接的模型一起打包）部署为独立桌面应用或 Web 应用。您可以使用该应用操作控件并监视面板上的显示，而无需依赖 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard panel

从 R2024a 开始，您可以将 dashboard panel 停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard panel。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink Toolstrip 中的持久 Panels 选项卡

当您将 dashboard panel 添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选择任何面板时，**Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：支持对面板中的可自定义 dashboard 模块执行撤消和重做

从 R2022b 开始，您可以撤消和重做对面板中可自定义 dashboard 模块所做的更改。

要撤消或重做更改：

1. 点击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您点击面板中的 dashboard 模块时，该模块的 toolstrip 选项卡会出现。例如，当您点击 Circular Gauge 模块时，toolstrip 中会出现 **Gauge** 选项卡。

当您点击面板时，toolstrip 中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b：扩展对 Raspberry Pi 板上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持将 **Customizable Blocks** 库中的以下模块部署到您的 Raspberry Pi 板上：

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

### R2022b：扩展对 Android 设备上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持将 **Customizable Blocks** 库中的以下模块部署到您的 Android 设备上：

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在您的 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

### R2022a：调整前景图像大小并重新定位

Customizable Blocks 库中的模块具有添加前景图像作为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整前景图像大小并重新定位。

## 端口

R2025b 官方文档未提供。
