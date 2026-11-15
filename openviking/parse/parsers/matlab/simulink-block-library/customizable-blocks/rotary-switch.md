---
type: simulink-block
title: 'Rotary Switch'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customrotaryswitch'
---

# Rotary Switch

Change parameter or variable value using rotary switch with customizable appearance

## 中文

使用具有可自定义外观的旋转开关更改参数或变量值

### 所属库

Simulink / Dashboard / Customizable Blocks

### 描述

使用 Rotary Switch 模块在仿真前或仿真期间更改所连接变量或参数的值。在 Customizable Blocks 库中使用 Rotary Switch 模块时，可以自定义模块外观，使其看起来像系统中的真实旋转开关。将 Rotary Switch 模块与其他 dashboard 模块一起使用，为模型创建交互式 dashboard。

真实旋转开关具有多个设置。Rotary Switch 模块将这些设置视为不同状态。一个状态将状态值与手柄方向、点击区域以及显示在点击区域上的状态标签配对。

要在仿真期间激活某个状态，请点击该状态的点击区域，或将手柄拖动到指向该点击区域。要在仿真未运行时激活某个状态，请点击 Rotary Switch 模块以选择该模块，然后点击点击区域或将手柄拖动到指向该点击区域。激活状态时，状态值将赋给 Rotary Switch 模块所连接的 Simulink® 模块图元素。

所有状态点击区域合起来覆盖手柄从第一个状态移动到最后一个状态时所经过角度范围内的模块区域。状态标签在该范围内均匀分布，第一个标签位于范围起点，最后一个标签位于范围终点。该范围被细分为点击区域，使相邻点击区域的边界平分标签之间的角距离。

下图显示一个具有四个状态的自定义旋转开关。第一个状态和最后一个状态的标签相距 150 degrees。状态标签（顺时针读取）为 A、B、C 和 D。点击区域以四种不同颜色显示。第一个和第四个状态的点击区域跨过的角距离是其他每个状态跨过的角距离的一半。

**注意**

- 在仿真期间双击已连接的 Rotary Switch 模块，或在点击该模块后双击，不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Rotary Switch 模块会同时选择该模块并移动开关手柄。要选择该模块而不移动开关手柄，请按 **Shift**，然后点击该模块。

#### Customize Rotary Switch Blocks

将 Rotary Switch 模块添加到模型时，该模块预配置有默认设计。可以使用默认设计使用该模块，也可以自定义模块外观。

要自定义模块外观，请使用 design mode。选择模块后，可以通过以下三种方式之一进入 design mode：

- 在 Simulink Toolstrip 中，在模块特定的选项卡上，于 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在 design mode 中，可以使用模块上方的工具栏自定义旋转开关。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于 design mode 的 Customizable Rotary Switch 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

自定义 Rotary Switch 模块时，需要为每个状态配置模块外观。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。要添加状态，请在工具栏中点击 Add State 按钮 。要删除状态，请点击 Remove State 按钮 。

**自定义所选状态的 Design Mode 操作**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state value. | No | Yes |
| Specify the state label text. | No | Yes |
| Add or remove states. | Yes | Yes |
| Upload a handle image. | Yes | Yes |
| Change the size of the handle. | No | Yes |
| Change the position the handle. | No | Yes |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，还可以在画布中以交互方式调整组件大小和位置。手柄的移动限制在穿过模块中心且沿 **Start Angle** 的直线上。

要更改状态标签的颜色，请在 **Format** 选项卡上，于 **Style** 下，点击 **Foreground** 按钮上的箭头并选择颜色。可以从标准色调色板中选择，或点击 Custom Colors 按钮 指定自定义颜色。

**适用于所有状态的 Design Mode 操作**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the arc length spanned by the state labels. | No | Yes, in the **Rotary Switch** component |
| Change the start angle of the arc. | No | Yes, in the **Rotary Switch** component |
| Change the label radius. | No | Yes, in the **Rotary Switch** component |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

完成设计编辑后，要退出 design mode，请点击画布右上角的 **X**。

#### Connect Dashboard Blocks

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用 connect mode。要在未连接的模块上进入 connect mode，请暂停在要连接的模块上并点击 Connect 按钮 。要在已连接的模块上进入 connect mode，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入 connect mode。选择要连接其参数的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上并点击 Done Connecting 按钮 。

在更新模块图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模块图。

可以连接到具有标量值的参数，也可以连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Rotary Switch 模块连接到模型。

未连接的 Rotary Switch 模块连接到 Constant 模块。

#### Parameter Logging

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，可以在其中查看参数值以及记录的信号数据。可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

### 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，于 **Design** 下，选择 **Property Inspector**。

### 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector 并点击 **Parameters** 选项卡。

#### Connection

#### **Connection** — 模块参数值连接到参数值的连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用 connect mode、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关 connect mode 以及如何使用 toolstrip 连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 中，于 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模块图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模块图。

还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### Programmatic Use

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 dashboard 模块连接到由值定义的参数，某些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都具有连接的值，因为给定 dashboard 模块连接到由值定义的参数或由变量定义的参数之一。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认：** `[]` |

#### Main

#### **Label** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏标签。如果希望标签可见，请指定标签位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认：** `'Hide'` |

#### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

#### **Enumerated Data Type** — 使用 enumerated data type 指定状态值和标签 `off`（默认） | `on`

可以使用将数值与每个枚举配对的 enumerated data type 来配置模块的状态值和标签。首先，选择 **Enumerated Data Type**。然后，在文本框中指定 enumerated data type 的名称。指定 enumerated data type 的定义必须保存在 MATLAB path 上或 base workspace 中。

**注意**

可以使用 `Simulink.defineIntEnumType` 函数定义 enumerated data type。例如，要为从一到五的一组罗马数字定义 enumerated data type `myEnumType`，请使用以下命令。

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

然后，在 Property Inspector 中，于 **Parameters** 选项卡上，在 **Enumerated Data Type** 字段中，输入 `myEnumType`。

#### Programmatic Use

要使用 enumerated data type 以编程方式指定模块的状态标签和值，请将 `UseEnumeratedDataType` 参数的值设置为 `'on'`，并将 `EnumeratedDataType` 参数的值设置为 enumerated data type 的名称。

|  |
| --- |
| **模块参数：** `UseEnumeratedDataType` |
| **类型：** string or character array |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

|  |
| --- |
| **模块参数：** `EnumeratedDataType` |
| **类型：** string or character array |
| **默认：** `''` |

#### **States** — 值与标签的配对 scalar 和 character vector

每个状态将 **State Value** 与 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关具有五个状态，每个开关位置对应一个状态。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

可以使用可自定义开关模块设计具有任意数量状态且大于或等于 1 的开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，不能添加或删除状态。

**提示**

也可以在 design mode 中配置状态参数：

1. 选择开关模块。
2. 进入 design mode。在 Property Inspector 中，于 **Design** 选项卡上，点击 **Edit**。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 使用模块上方的工具栏或 Property Inspector 配置所选状态的参数值。

#### Programmatic Use

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素且具有以下字段的结构体数组：

- `Value` — 状态的 scalar double 值
- `Label` — 用作开关位置标签的 string 或 character array

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **模块参数：** `States` |
| **类型：** two element array of structures |

#### Design

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### Rotary Switch

#### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会解锁纵横比。释放 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会锁定纵横比。释放 **Shift** 键时，纵横比解锁。

#### **Arc** — 状态标签跨过的弧长 `300`（默认） | scalar

将状态标签中心点跨过的弧长指定为 scalar 值，以 degrees 测量。

**示例：** `90`

#### **Start Angle** — `State 1` 的角度位置 `120`（默认） | scalar

将第一个状态的角度位置指定为 scalar 值，以从指向右侧的水平轴顺时针方向的 degrees 测量。

**示例：** `0`

#### **Label Radius** — 标签距模块中心的距离 scalar

将标签距模块中心的距离指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `0.5`

#### States

#### **Select State** — 状态的管理和配置 scalar 和 character vector

每个状态将 **State Value** 与 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关具有五个状态，每个开关位置对应一个状态。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

可以设计具有任意数量状态且大于或等于 1 的旋转开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，不能添加或删除状态。可以在 Property Inspector 的 **Parameters** 选项卡中禁用此选项。

要配置状态，请在 **States** 组件中展开 **Select State** 部分并选择该状态。

在 Property Inspector 的 **Design** 选项卡上的 **States** 组件中配置所选状态的值和标签文本。

在 **States** 组件中对参数值所做的所有更改仅应用于所选状态。要配置其他状态，请展开 **Select State** 部分并选择该状态。然后，在 **States** 组件中配置该状态的参数值。

**提示**

还可以使用 Property Inspector 中的 **Parameters** 选项卡配置模块的状态。

#### Programmatic Use

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素且具有两个字段的结构体数组：

- `Value` — 状态的 scalar double 值
- `Label` — 用作开关位置标签的 string 或 character array

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **模块参数：** `States` |
| **类型：** two element array of structures |

#### **Value** — 状态值 scalar

每个状态将 **State Value** 与 **State Label** 配对。指定在 **Design** 选项卡中所选状态的状态值。

**注意**

当 **Enumerated Data Type** 打开时，不能更改该值。可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

#### **Text** — 状态标签文本 string | character array

每个状态将 **State Value** 与 **State Label** 配对。指定在 **Design** 选项卡中所选状态 **State Label** 的文本。

**注意**

当 **Enumerated Data Type** 打开时，不能更改文本。可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

#### Handle

#### **Width** — 手柄图像宽度 scalar

将手柄图像的宽度指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

#### **Height** — 手柄图像高度 scalar

将手柄图像的高度指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

#### **Lock Aspect Ratio** — 用于保持图像纵横比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

#### **Rotate Image** — 手柄图像的旋转 `0`（默认） | scalar

以 90 degree 增量绕其中心旋转手柄图像。

**示例：** `90`

#### **Offset from Center** — 手柄图像中心距模块中心的偏移 `0`（默认） | scalar

将手柄图像中心到模块中心的距离指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

#### Background Image

#### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认） | `on`

对于模块背景，可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

#### **Color** — 模块背景颜色 `[r g b]` vector

要选择纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准色调色板中选择背景颜色，或指定自定义颜色。

**提示**

还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Foreground Color**。

#### Programmatic Use

将模块的 `BackgroundColor` 参数指定为定义 `1`-by-`3` `[r g b]` vector 的 string 或 character vector，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

#### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

#### **Corner Radius** — 具有模块背景颜色的区域外边缘距标签半径的偏移 scalar

将模块背景颜色覆盖区域的外边缘距标签半径的偏移设置为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.1`

#### Foreground Image

#### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

#### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘距模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

#### **Lock Aspect Ratio** — 用于保持前景图像纵横比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard 模块在代码生成时会被忽略。

### 版本历史

**在 R2021b 中引入**

#### R2025a: Select dashboard block and open Block Parameters dialog box during simulation

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于 *active* 状态时，可以与模块所代表的 gadget 交互。例如，可以按下按钮或拨动开关。当模块处于 inactive 状态时，只能与模块交互。例如，可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间均处于 active 状态。提升到 dashboard panel 的模块在面板于其自身窗口中打开或停靠且解锁时也处于 active 状态。如果 Callback Button 模块中至少一个由按下按钮触发的回调具有非空值，则该模块始终处于 active 状态。要与 inactive 模块所代表的 gadget 交互，可以通过点击该模块临时激活模块。取消选择模块后，模块再次变为 inactive。

点击 active 的 Callback Button 模块或点击连接到参数或变量值的 active Dashboard 或 Customizable Blocks 库模块，会同时选择该模块并与模块所代表的 gadget 交互。例如，点击未选中的 active 已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，可以通过按 **Shift** 然后点击模块来选择模块而不与 gadget 交互。类似地，可以通过按 **Shift** 然后双击模块来打开 Block Parameters 对话框。

#### R2024b: Unlock dashboard block aspect ratio with keyboard

如果来自 Dashboard 库的模块的纵横比已锁定，可以通过按 **Shift** 临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

#### R2024a: Deploy dashboard panel as web app or standalone desktop app

拥有 Simulink Compiler™ 许可证后，现在可以将 dashboard panel（连同其连接的模型一起打包）部署为独立桌面应用或 Web 应用。可以使用该应用操作控件并监视面板上的显示，而不依赖于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

#### R2024a: Dock dashboard panels

从 R2024a 开始，可以将 dashboard panel 停靠到 Simulink Editor 窗口。可以使用停靠的面板在仿真期间监视信号并控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

#### R2023b: Open panel in new window

从 R2023b 开始，可以在新窗口中打开 dashboard panel。为此，请选择面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

可以独立于模型窗口最小化和还原包含面板的新窗口。在面板窗口中，可以运行、暂停、停止和单步执行仿真。在面板窗口中，可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

#### R2023a: Persistent panels tab in Simulink Toolstrip

将 dashboard panel 添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时 **Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名所选面板。
- 可以隐藏所选面板。

#### R2022b: Undo and redo support for customizable dashboard blocks in panel

从 R2022b 开始，可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

#### R2022b: Toolstrip support for panels

从 R2022b 开始，可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

点击面板中的 dashboard 模块时，会出现该模块的 toolstrip 选项卡。例如，点击 Circular Gauge 模块时，toolstrip 中会出现 **Gauge** 选项卡。

点击面板时，toolstrip 中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2022b: Extended support for customizable Dashboard blocks on Raspberry Pi boards

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持将 **Customizable Blocks** 库中的以下模块部署到 Raspberry Pi 板上：

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

可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

#### R2022b: Extended support for customizable Dashboard blocks on Android devices

从 R2022b 开始，Simulink Support Package for Android® Devices 支持将 **Customizable Blocks** 库中的以下模块部署到 Android 设备上：

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

可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

#### R2022a: Resize and reposition foreground image

Customizable Blocks 库中的模块具有添加前景图像作为模块设计一部分的选项。从 R2022a 开始，可以在模块设计内旋转、调整大小并重新定位前景图像。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

Use the Rotary Switch block to change the value of the connected variable
or parameter before or during simulation. When you use the Rotary Switch block
in the Customizable Blocks library, you can customize the appearance of the block to look like
a real rotary switch in your system. Use the Rotary Switch block with other
dashboard blocks to create an interactive dashboard for your model.

A real rotary switch has multiple settings. The Rotary Switch block treats
these settings as different states. A state pairs a state value with a handle orientation, a
click area, and a state label that is displayed on the click area.

To activate a state during simulation, click the click area of the state or drag the
handle to point to the click area. To activate a state when the simulation is not running,
click the Rotary Switch block to select the block, and then click the click
area or drag the handle to point to the click area. When you activate the state, the state
value is assigned to the Simulink® block diagram element to which the Rotary Switch block
connects.

Collectively, the state click areas cover the area of the block within the angular range
that the handle traverses when it moves from the first state to the last state. The state
labels are evenly spaced over the range, with the first label at the start of the range and
the last label at the end of the range. The range is subdivided into click areas such that the
borders of adjacent click areas bisect the angular distance between labels.

The image shows a custom rotary switch with four states. The labels of the first state and last states are 150 degrees apart. The state labels (read clockwise) are A, B, C, and D. The click areas are shown in four different colors. The angular distance spanned by the click areas of the first and fourth state is half of that spanned by each of the other states.

**Note**

- Double-clicking a connected Rotary Switch block during simulation or
  after clicking the block does not open the Block Parameters dialog box. To open the
  Block Parameters dialog box, press **Shift**, then double-click the
  block.
- Clicking a connected Rotary Switch block during simulation both
  selects the block and moves the switch handle. To select the block without moving the
  switch handle, press **Shift**, then click the block.

### Customize Rotary Switch Blocks

When you add a Rotary Switch block to your model, the block is
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

In design mode, you can use the toolbar above the block to customize the rotary switch.
To access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Rotary Switch block in design mode with the toolbar and the Design tab in the Property Inspector visible.

When you customize a Rotary Switch block, you configure the block
appearance for each state. To select a state to customize, use the drop-down list in the
toolbar. Alternatively, on the **Design** tab, select the
**States** component and then select from the **Select
State** list. To add a state, in the toolbar, click the Add State button
. To delete a state, click the Remove State button
.

**Design Mode Actions that Customize the Selected State**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state value. | No | Yes |
| Specify the state label text. | No | Yes |
| Add or remove states. | Yes | Yes |
| Upload a handle image. | Yes | Yes |
| Change the size of the handle. | No | Yes |
| Change the position the handle. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. The movement of the handle is limited to the line that passes
through the center of the block at the **Start Angle**.

To change the color of the state labels, on the **Format** tab, under
**Style**, click the arrow on the **Foreground**
button and select a color. You can select from a palette of standard colors or click the
Custom Colors button  to specify a custom color.

**Design Mode Actions that Apply to All States**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the arc length spanned by the state labels. | No | Yes, in the **Rotary Switch** component |
| Change the start angle of the arc. | No | Yes, in the **Rotary Switch** component |
| Change the label radius. | No | Yes, in the **Rotary Switch** component |
| Upload a background image. | Yes | Yes |
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

This animation shows how to connect the Rotary Switch block to your
model.

An unconnected Rotary Switch block connects to a Constant block.

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

### **Enumerated Data Type** — Specify state values and labels using enumerated data type `off` (default) | `on`

You can use an enumerated data type that pairs a numeric value with each
enumeration to configure the state values and labels for the block. First, select
**Enumerated Data Type**. Then, specify the name of the enumerated
data type in the text box. The definition for the specified enumerated data type must
be saved on the MATLAB path or in the base workspace.

**Note**

You can define an enumerated data type using the `Simulink.defineIntEnumType`
function. For example, to define the enumerated data type
`myEnumType` for a set of Roman numerals from one to five, use
this command.

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

Then, in the Property Inspector, on the **Parameters** tab, in
the **Enumerated Data Type** field, enter
`myEnumType`.

#### Programmatic Use

To programmatically specify the state labels and values of the block using an
enumerated data type, set the value of the `UseEnumeratedDataType`
parameter to `'on'`, and set the value of the
`EnumeratedDataType` parameter to the name of the enumerated data
type.

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

### **States** — Pairings of value with label scalar and character vector

Each state pairs a **State Value** with a **State
Label**. When the block is in a given state, it assigns the **State
Value** for that state to the connected variable or parameter. You can use
the **State Label** to display the value assigned to the connected
variable or parameter on the block or to provide a descriptive text label.

By default, the switch has five states, one corresponding to each switch
position.

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

You can use a customizable switch block to design a switch with any number of
states greater than or equal to 1. To add a new state, click the
**+** button. To delete the current state, click the
**-** button.

**Note**

When **Enumerated Data Type** is enabled, you cannot add or
delete states.

**Tip**

You can also configure the parameters for a state in design mode:

1. Select the switch block.
2. Enter design mode. In the Property Inspector, on the
   **Design** tab, click **Edit**.
3. On the **Design** tab, open the
   **States** component, expand the **Select
   State** section, and select the state that you want to configure
   from the drop-down menu.
4. Configure the parameter values for the selected state either using the
   toolbar above the block or in the Property Inspector.

#### Programmatic Use

To configure the **States** for the block programmatically,
specify the value of the `States` parameter as a structure array
containing two elements with these fields:

- `Value` — Scalar double value for the state
- `Label` — String or character array to use as the label
  for the switch position

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** two element array of structures |

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Rotary Switch

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

### **Arc** — Arc length spanned by state labels `300` (default) | scalar

Specify the arc length spanned by the center points of the state labels as a
scalar value, measured in degrees.

**Example:** `90`

### **Start Angle** — Angular location of `State 1` `120` (default) | scalar

Specify the angular location of the first state as a scalar value, measured in
degrees clockwise from the horizontal axis pointing right.

**Example:** `0`

### **Label Radius** — Distance of labels from block center scalar

Specify the distance of the labels from the center of the block as a ratio of the
smaller of the two block dimensions, width or height.

**Example:** `0.5`

#### States

### **Select State** — Management and configuration of states scalar and character vector

Each state pairs a **State Value** with a **State
Label**. When the block is in a given state, it assigns the **State
Value** for that state to the connected variable or parameter. You can use
the **State Label** to display the value assigned to the connected
variable or parameter on the block or to provide a descriptive text label.

By default, the switch has five states, one corresponding to each switch
position.

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

You can design a rotary switch with any number of states greater than or equal to
1. To add a new state, click the **+** button. To delete the
current state, click the **X** button.

**Note**

When **Enumerated Data Type** is turned on, you cannot add or
delete states. You can disable this option in the **Parameters**
tab of the Property Inspector.

To configure a state, in the **States** component, expand the
**Select State** section and select the state.

Configure the value and the label text for the selected state in the
**States** component on the **Design** tab of the
Property Inspector.

All changes that you make to parameter values in the **States**
component are applied only to the selected state. To configure a different state,
expand the **Select State** section and select the state. Then,
configure the parameter values of that state in the **States**
component.

**Tip**

You can also configure the states for the block using the
**Parameters** tab in the Property Inspector.

#### Programmatic Use

To configure the **States** for the block programmatically,
specify the value of the `States` parameter as a structure array
containing two elements with two fields:

- `Value` — Scalar double value for the state
- `Label` — String or character array to use as the label
  for the switch position

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** two element array of structures |

### **Value** — State value scalar

Each state pairs a **State Value** with a **State
Label**. Specify the **State Value** of the state selected
in the **Design** tab.

**Note**

When **Enumerated Data Type** is turned on, you cannot change
the value. You can turn off this option in the **Parameters** tab
of the Property Inspector.

### **Text** — State label text string | character array

Each state pairs a **State Value** with a **State
Label**. Specify the text for the **State Label** of the
state selected in the **Design** tab.

**Note**

When **Enumerated Data Type** is turned on, you cannot change
the text. You can turn off this option in the **Parameters** tab of
the Property Inspector.

#### Handle

### **Width** — Handle image width scalar

Specify the width of the handle image as a ratio of the smaller of the two block
dimensions, width or height.

**Example:** `1`

### **Height** — Handle image height scalar

Specify the height of the handle image as a ratio of the smaller of the two block
dimensions, width or height.

**Example:** `1`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Rotate Image** — Rotation of handle image `0` (default) | scalar

Rotate the handle image about its center in 90 degree increments.

**Example:** `90`

### **Offset from Center** — Offset of handle image center from block center `0` (default) | scalar

Specify the distance from the center of the handle image to the center of the
block as a ratio of the smaller of the two block dimensions, width or height.

**Example:** `1`

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

To select a solid background color, select the **Use Background
Color** parameter. Then, choose a background color from the palette of
standard colors, or specify a custom color.

**Tip**

You can also specify the **Background Color** in the
**Format** tab of the Simulink Toolstrip.

To specify the color of the block text, in the **Format** tab
of the Simulink Toolstrip, specify the **Foreground Color**.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a
string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner Radius** — Offset of outer edge of area with block background color from label radius scalar

Set the offset of the outer edge of the area covered by the block background color
from the label radius, specified as a scalar value from `0` to
`1`.

**Example:** `0.1`

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
