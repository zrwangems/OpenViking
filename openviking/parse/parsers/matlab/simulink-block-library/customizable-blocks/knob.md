---
type: simulink-block
title: 'Knob'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customknob'
---

# Knob

Change parameter or variable value using knob with customizable appearance

## 中文

使用具有可自定义外观的旋钮更改参数或变量值

### 库

Simulink / Dashboard / Customizable Blocks

### 描述

使用 Knob 模块在仿真期间调整变量或模块参数的值。当您使用 Customizable Blocks 库中的 Knob 模块时，您可以自定义模块的外观，使其看起来像真实系统中的控件。您可以修改 Knob 模块上的范围和刻度值，以适合您要调整的值的所需范围。将 Knob 模块与其他仪表板模块一起使用，创建交互式仪表板来控制您的模型。

要在仿真运行时调整值，请使用指针将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。要在仿真未运行时调整值，请单击 Knob 模块以选择该模块，然后将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。

**注意**

- 在仿真期间或单击模块后双击已连接的 Knob 模块不会打开“模块参数”对话框。要打开“模块参数”对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间单击已连接的 Knob 模块会同时选择该模块并移动旋钮手柄。要在不移动旋钮手柄的情况下选择模块，请按 **Shift**，然后单击该模块。

#### 自定义 Knob 模块

当您将 Knob 模块添加到模型时，该模块预配置了默认设计。您可以使用默认设计的模块，或自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，在 **Design** 下，单击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上方出现的省略号上，然后单击 Edit Custom Block 按钮 。

在设计模式下，您可以使用模块上方的工具栏来自定义圆形仪表。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的可自定义 Knob 模块，显示了工具栏和 Property Inspector 中的 Design 选项卡。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传手柄图像。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 更改刻度标记、刻度标签或值条的颜色和不透明度。 | 是 | 是 |
| 更改刻度的弧长。 | 否 | 是 |
| 将刻度方向指定为顺时针或逆时针。 | 否 | 是 |
| 指定值条从中增长的原点的位置。 | 否 | 是 |
| 更改刻度和手柄的大小。 | 否 | 是 |
| 更改刻度和手柄的位置。 | 否 | 是 |

要使用工具栏更改刻度标记、刻度标签或值条的颜色和不透明度，请在工具栏左起第二部分中，选择要更改其颜色的组件。要更改颜色，请单击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中交互式地调整组件的大小和位置。手柄的移动仅限于穿过模块中心和刻度上的最小值的线。

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。

#### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中，单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。从出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，单击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示了如何将 Knob 模块连接到您的模型。

未连接的 Knob 模块连接到 Constant 模块。

#### 参数记录

连接到仪表板模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

### 参数

使用 Property Inspector 和“模块参数”对话框来指定模块参数的值。要设置仪表板模块的核心参数，请使用“模块参数”对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的“模块参数”对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，在 **Design** 下，选择 **Property Inspector**。

### 参数

要设置仪表板模块的核心参数，请打开 Property Inspector 并单击 **Parameters** 选项卡。

#### 连接

#### **Connection** — 要连接的模块参数值 连接参数值 连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或“模块参数”对话框中的 **Connection** 表。要从 Property Inspector 打开“模块参数”对话框，请在 **Connected to** 右侧，单击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择模块。
2. 要连接模块，请在 Property Inspector 的 **Parameters** 选项卡上，单击 **Connect**。要更改模块的连接，请改为单击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在表中，选择要连接到的参数。
5. 单击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将仪表板模块连接到由值定义的参数，有些适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

#### 主要

#### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Tick Interval** — 主刻度之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、标量值，指定刻度上主刻度的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Direction** — 刻度值增加的方向 `Clockwise` (default) | `Counterclockwise`

设置刻度值增加的方向。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

#### **Label** — 显示已连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

您可以显示仪表板模块连接到的元素的名称，标签位于模块的顶部或底部，或者您可以隐藏标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会临时解锁纵横比。松开 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

#### Design

要自定义仪表板模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。

#### Knob

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会解锁纵横比。松开 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

#### 刻度

#### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Tick Interval** — 主刻度之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、标量值，指定刻度上主刻度的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

#### **Origin** — 手柄移动和值条增长的刻度值 `auto` (default) | scalar

指定刻度上手柄移动和值条增长所依据的值。设置为 `auto` 时，`Origin` 是刻度的最小值。

**示例:** `0`

#### **Direction** — 刻度值增加的方向 `Clockwise` (default) | `Counterclockwise`

设置刻度值增加的方向。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

#### **Arc** — 刻度的弧长 `270` (default) | scalar

以 degrees 为单位，将刻度的弧长指定为标量值。

**示例:** `90`

#### **Start Angle** — 刻度最小值的角度位置 `135` (default) | scalar

指定最小刻度值的角度位置，以从指向右侧的水平轴开始顺时针测量的 degrees 为单位。

**示例:** `0`

#### **Inner Radius** — 刻度标记自由端的半径 scalar

将刻度标记自由端的半径指定为刻度边界框两个维度（宽度或高度）中较小者的比例。`Inner Radius` 可以大于 `Outer Radius`。

**示例:** `0.5`

#### **Outer Radius** — 跨度线半径 scalar

将跨度线半径指定为刻度边界框两个维度（宽度或高度）中较小者的比例。`Outer Radius` 可以小于 `Inner Radius`。

**示例:** `0.5`

#### **X Offset** — 刻度边界框左边缘距模块左边缘的水平偏移 scalar

将刻度边界框左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例:** `1`

#### **Y Offset** — 刻度边界框顶边缘距模块顶边缘的垂直偏移 scalar

将刻度边界框顶边缘距模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例:** `1`

#### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比例。

**示例:** `2`

#### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比例。

**示例:** `2`

#### **Lock Aspect Ratio** — 保持刻度纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整刻度大小时保持纵横比。

#### **Tick Color** — 刻度标记、跨度线和模块名称的颜色 `[r g b]` 向量

设置刻度标记、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该向量定义了一个 `1`x`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

#### **Label Color** — 刻度标签字体颜色 `[r g b]` 向量

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

#### **Label Radius** — 标签距刻度中心的距离 scalar

将标签距刻度中心的距离指定为模块两个维度（宽度或高度）中较小者的比例。

**示例:** `0.5`

#### 手柄

#### **Width** — 手柄图像宽度 scalar

将手柄图像的宽度指定为刻度边界框两个维度（宽度或长度）中较小者的比例。

**示例:** `1`

#### **Height** — 手柄图像高度 scalar

将手柄图像的高度指定为刻度边界框两个维度（宽度或长度）中较小者的比例。

**示例:** `1`

#### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

#### **Rotate Image** — 手柄图像的旋转 `180` (default) | scalar

以 90 度为增量围绕其中心旋转手柄图像。

**示例:** `90`

#### **Offset from Center** — 手柄图像中心距刻度中心的偏移 `0` (default) | scalar

将手柄图像中心到刻度中心的距离指定为刻度直径的比例。

**示例:** `1`

#### 背景图像

#### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像，或选择纯色。要选择纯色背景颜色，请打开 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用工具条更改背景颜色会移除背景图像并启用 **Use Background Color** 选项。

当您将纯色背景与 Circular Gauge 模块一起使用时，您可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Knob 模块

**示例:** `on`

#### **Background Color** — 模块背景颜色 `[r g b]` 向量

要选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当您将纯色背景与 Circular Gauge 模块一起使用时，您可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Knob 模块

#### 编程使用

将模块的 `BackgroundColor` 参数指定为一个 `1`x`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

#### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例:** `0.5`

#### **Corner radius** — 模块背景颜色区域外边缘距刻度标记的偏移 scalar

设置模块背景颜色覆盖区域的外边缘距刻度标记的偏移，指定为从 `0` 到 `1` 的标量值。

**示例:** `0.1`

#### 前景图像

#### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

#### **Y Offset** — 前景图像顶边缘距模块顶边缘的垂直偏移 scalar

将图像顶边缘距模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例:** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例:** `0.5`

#### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

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

仪表板模块在代码生成时被忽略。

#### 版本历史记录

**在 R2021a 中引入**

#### R2025a: 在仿真期间选择仪表板模块并打开“模块参数”对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块代表的控件进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与模块本身进行交互。例如，您可以移动或调整模块的大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到仪表板面板的模块在面板在其自己的窗口中打开或停靠并解锁时也处于活动状态。对于 Callback Button 模块，如果按下按钮触发的至少一个回调具有非空值，则这些模块始终处于活动状态。要与非活动模块代表的控件进行交互，您可以通过单击该模块来临时激活它。取消选择该模块后，该模块将再次变为非活动状态。

单击活动的 Callback Button 模块或来自 Dashboard 或 Customizable Blocks 库的、连接到参数或变量值的活动模块，会同时选择该模块并与该模块代表的控件进行交互。例如，单击未选择的、活动的、已连接的 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后单击该模块来选择模块而不与控件交互。同样，您可以通过按 **Shift** 然后双击该模块来打开“模块参数”对话框。

#### R2024b: 使用键盘解锁仪表板模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。松开 **Shift** 键时，纵横比会锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

#### R2024a: 将仪表板面板部署为 Web 应用或独立桌面应用

拥有 Simulink Compiler™ 许可证，您现在可以将与面板连接的模型一起打包的仪表板面板部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作控件并监视面板上的显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

#### R2024a: 停靠仪表板面板

从 R2024a 开始，您可以将仪表板面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

#### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window 。

您可以单独于模型窗口最小化和还原包含面板的新窗口。从面板窗口，您可以运行、暂停、停止和逐步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，单击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

#### R2023a: Simulink Toolstrip 中的持久面板选项卡

当您将仪表板面板添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选择了面板时可见。从 R2023a 开始，当没有选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加一个空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

#### R2022b: 对面板中的可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中的可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

#### R2022b: 对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 来管理和编辑面板及其包含的仪表板模块。

当您单击面板中的仪表板模块时，该模块的工具条选项卡会出现。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在工具条中。

当您单击面板时，**Panel** 选项卡会出现在工具条中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

#### R2022a: 更改刻度方向

从 R2022a 开始，您可以更改来自 **Customizable Blocks** 库的这些模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

#### R2022a: 为值条和指针指定原点

刻度的原点是刻度上指针移动和值条增长所依据的值。从 R2022a 开始，您可以为来自 **Customizable Blocks** 库的这些模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

#### R2022a: 调整前景图像的大小和位置

Customizable Blocks 库中的模块有一个选项，可以添加前景图像作为模块设计的一部分。从 R2022a 开始，您可以在模块设计内旋转、调整大小和重新定位前景图像。

#### R2021b: 在 Raspberry Pi 板上部署可自定义的 Gauge 和 Knob 仪表板模块

从 2021b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 硬件板上部署 Circular Gauge 模块和 Knob 模块。

您可以自定义 Simulink 模型中模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

#### R2021b: 在 Android 设备上部署可自定义的 Gauge 和 Knob 仪表板模块

从 2021b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署 Circular Gauge 模块和 Knob 模块。

您可以自定义 Simulink 模型中模块的视觉方面，并在您的 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

Use the Knob block to tune the value of a variable or block parameter to
during simulation. When you use the Knob block in the Customizable Blocks
library, you can customize the appearance of the block so that it looks like a control in a
real system. You can modify the range and tick values on the Knob block to fit
the desired range for the value you want to tune. Use the Knob block with other
dashboard blocks to create an interactive dashboard to control your model.

To tune a value when the simulation is running, use your pointer to drag the handle to the
scale value to which you want to set the connected variable or block parameter. To tune a
value when the simulation is not running, click the Knob block to select the
block, and then drag the handle to the scale value to which you want to set the connected
variable or block parameter.

**Note**

- Double-clicking a connected Knob block during simulation or after
  clicking the block does not open the Block Parameters dialog box. To open the Block
  Parameters dialog box, press **Shift**, then double-click the block.
- Clicking a connected Knob block during simulation both selects the
  block and moves the knob handle. To select the block without moving the knob handle,
  press **Shift**, then click the block.

### Customize Knob Blocks

When you add a Knob block to your model, the block is preconfigured with
a default design. You can use the block with the default design or customize the appearance
of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the circular gauge.
To access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Knob block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Upload a handle image. | Yes | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |
| Change the color and opacity of the scale tick marks, scale labels, or value bar. | Yes | Yes |
| Change the arc length of the scale. | No | Yes |
| Specify the scale direction as clockwise or counterclockwise. | No | Yes |
| Specify the location of the origin from which the value bar grows. | No | Yes |
| Change the size of the scale and handle. | No | Yes |
| Change the position the scale and handle. | No | Yes |

To change the color and opacity of the scale tick marks, scale labels, or value bar
using the toolbar, in the second section of the toolbar from the left, select the component
whose color you want to change. To change the color, click the color wheel. To change the
opacity, move the slider.

In addition to customizing the block design using the toolbar and
**Design** tab, you can also resize and reposition components
interactively in the canvas. The movement of the handle is limited to the line that passes
through the center of the block and the minimum value on the scale.

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

This animation shows how to connect the Knob block to your model.

An unconnected Knob block connects to a Constant block.

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

### **Minimum** — Minimum tick mark value `0` (default) | scalar

Finite, real, double, scalar value specifying the minimum tick mark value for the
scale. The parameter value must be less than the value of the
**Maximum** parameter.

#### Programmatic Use

To programmatically set the `Minimum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — Maximum tick mark value `100` (default) | scalar

Finite, real, double, scalar value specifying the maximum tick mark value for the
scale. The parameter value must be greater than the value of the
**Minimum** parameter.

#### Programmatic Use

To programmatically set the `Maximum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — Interval between major tick marks `auto` (default) | scalar

Finite, real, positive, whole, scalar value specifying the interval of major tick
marks on the scale. When set to `auto`, the block automatically adjusts
the tick interval based on the values of the **Maximum** and
**Minimum** parameters.

#### Programmatic Use

To programmatically set the `Tick Interval` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Direction** — Direction of increasing scale values `Clockwise` (default) | `Counterclockwise`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

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

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Knob

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

#### Scale

### **Minimum** — Minimum tick mark value `0` (default) | scalar

Finite, real, double, scalar value specifying the minimum tick mark value for the scale. The
parameter value must be less than the value of the **Maximum**
parameter.

#### Programmatic Use

To programmatically set the `Minimum` parameter, use a
`1`-by-`3`
vector containing values for the
`Minimum`, `Tick
Interval`, and `Maximum`
parameters, in that order. To use the
`auto` value for the
`Tick Interval`, leave the
`Tick Interval` position in the
vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — Maximum tick mark value `100` (default) | scalar

Finite, real, double, scalar value specifying the maximum tick mark value for the scale. The
parameter value must be greater than the value of the **Minimum**
parameter.

#### Programmatic Use

To programmatically set the `Maximum` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — Interval between major tick marks `auto` (default) | scalar

Finite, real, positive, whole, scalar value specifying the interval of major tick marks on the scale. When set to `auto`, the block automatically adjusts the tick interval based on the values of the **Maximum** and **Minimum** parameters.

#### Programmatic Use

To programmatically set the `Tick Interval` parameter, use a
`1`-by-`3` vector containing values for the
`Minimum`, `Tick Interval`, and
`Maximum` parameters, in that order. To use the
`auto` value for the `Tick Interval`, leave
the `Tick Interval` position in the vector empty, or specify
`-1`.

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Origin** — Value on scale from which handle moves and value bar grows `auto` (default) | scalar

Specify the value on the scale from which the handle moves and the value bar grows.
When set to `auto`, the `Origin` is the minimum of
the scale.

**Example:** `0`

### **Direction** — Direction of increasing scale values `Clockwise` (default) | `Counterclockwise`

Set the direction of increasing scale values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Arc** — Arc length of scale `270` (default) | scalar

Specify the arc length of the scale as a scalar value, measured in degrees.

**Example:** `90`

### **Start Angle** — Angular location of scale minimum `135` (default) | scalar

Specify the angular location of the minimum scale value, measured in
degrees clockwise from the horizontal axis pointing
right.

**Example:** `0`

### **Inner Radius** — Radius of free end of scale tick marks scalar

Specify the radius of the free end of the scale tick marks as a ratio of the
smaller of the two dimensions of the bounding box of the scale, width or
height. The `Inner Radius` can be larger than the
`Outer Radius`.

**Example:** `0.5`

### **Outer Radius** — Span line radius scalar

Specify the span line radius as a ratio of the smaller of the two dimensions
of the bounding box of the scale, width or height. The `Outer
Radius` can be smaller than the `Inner
Radius`.

**Example:** `0.5`

### **X Offset** — Horizontal offset of left edge of scale bounding box from left edge of block scalar

Specify the horizontal offset of the left edge of the bounding box of
the scale from the left edge of the block as a ratio of the
block width. Relative to the position of the scale when the
offset is `0`, an offset with a negative value
moves the scale left, and an offset with a positive value moves
the scale right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of scale bounding box from top edge of block scalar

Specify the vertical offset of the top edge of the bounding box of the scale from the
top edge of the block as a ratio of the block height. Relative to the position of the
scale when the offset is `0`, an offset with a negative value moves the
scale up, and an offset with a positive value moves the scale down.

**Example:** `1`

### **Width** — Scale width scalar

Specify the width of the bounding box of the scale as a ratio of the
block width.

**Example:** `2`

### **Height** — Scale height scalar

Specify the height of the bounding box of the scale as a ratio of the
block height.

**Example:** `2`

### **Lock Aspect Ratio** — Option to maintain scale aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the scale using the
Property Inspector.

### **Tick Color** — Color of scale tick marks, span line, and block name `[r g b]` vector

Set the color of the scale tick marks, the span line, and the block name. Choose a
color from the palette of standard colors, or specify a custom color.

**Tip**

You can also set the **Tick Color** by choosing a
**Foreground Color** on the **Format** tab of
the Simulink Toolstrip.

To specify the color of the block text, use the **Label Color**
parameter.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the block as a string
or a character vector that defines a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Label Color** — Scale label font color `[r g b]` vector

Choose a font color for the scale label from the palette of standard
colors, or specify a custom color.

**Tip**

To specify the color of the scale, use the **Tick
Color** parameter.

### **Label Radius** — Distance of labels from scale center scalar

Specify the distance of the labels from the center of the scale as a ratio of the
smaller of the two block dimensions, width or height.

**Example:** `0.5`

#### Handle

### **Width** — Handle image width scalar

Specify the width of the handle image as a ratio of the smaller of the two
dimensions of the bounding box of the scale, width or length.

**Example:** `1`

### **Height** — Handle image height scalar

Specify the height of the handle image as a ratio of the smaller of the two
dimensions of the bounding box of the scale, width or length.

**Example:** `1`

### **Lock Aspect Ratio** — Option to maintain image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

### **Rotate Image** — Rotation of handle image `180` (default) | scalar

Rotate the handle image about its center in 90 degree increments.

**Example:** `90`

### **Offset from Center** — Offset of handle image center from scale center `0` (default) | scalar

Specify the distance from the center of the handle image to the center of the
scale as a ratio of the diameter of the scale.

**Example:** `1`

#### Background Image

### **Use Background Color** — Option to specify solid block background color `off` (default) | `on`

For the block background, you can provide a background image, or to select a solid
color. To select a solid background color, turn **Use Background
Color** on. To provide a background image, turn **Use Background
Color** off.

**Note**

Changing the background color using the toolstrip removes the background image
and enables the **Use Background Color** option.

When you use a solid background with the Circular Gauge block,
you can design noncircular gauges. When the scale arc angle is 180° or smaller, the
background shape conforms to the scale.

Knob block with noncircular orange background area

**Example:** `on`

### **Background Color** — Block background color `[r g b]` vector

To select a solid background color, enable the **Use Background
Color** parameter. Then, choose a background color from the palette of
standard colors, or specify a custom color.

**Note**

When you use a solid background with the Circular Gauge block,
you can design noncircular gauges. When the scale arc angle is 180° or smaller, the
background shape conforms to the scale.

Knob block with noncircular orange background area

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

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner radius** — Offset of outer edge of area with block background color from tick marks scalar

Set the offset of the outer edge of the area covered by the block background color
from tick marks, specified as a scalar value from `0` to
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

**Introduced in R2021a**

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

### R2022a: Change scale direction

Starting in R2022a, you can change the direction of the scale of these blocks from the
**Customizable Blocks** library:

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: Specify origin for value bar and needle

The origin of a scale is the value on the scale from which the needle moves and the
value bar grows. Starting in R2022a, you can specify an origin for the scales of these
blocks from the **Customizable Blocks** library:

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: Resize and reposition foreground image

The blocks in the Customizable Blocks library have an option to add a foreground image
as part of the design for a block. Starting in R2022a, you can rotate, resize, and
reposition the foreground image within the block design.

### R2021b: Deploy customizable Gauge and Knob Dashboard blocks on Raspberry Pi boards

Starting in 2021b, the Simulink Support Package for Raspberry Pi® Hardware supports deploying the Circular Gauge block and the
Knob block on your Raspberry Pi hardware boards.

You can customize the visual aspects of the blocks in the Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on a
web browser you launch from the Raspberry Pi terminal.

### R2021b: Deploy customizable Gauge and Knob Dashboard blocks on Android device

Starting in 2021b, the Simulink Support Package for Android® Devices supports deploying the Circular Gauge block and the
Knob block on your Android device.

You can customize the visual aspects of the blocks in the Simulink model and obtain the what you see is what you get (WYSIWYG) visualization on
your Android device as well as on your web browser.
