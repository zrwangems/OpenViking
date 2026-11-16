---
type: simulink-block
title: 'Knob'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customknob'
language: zh-CN
chinese_source: worker-translation
---

# Knob



使用具有可自定义外观的旋钮更改参数或变量值

## 库

Simulink / Dashboard / Customizable Blocks

## 描述

使用 Knob 模块在仿真期间调整变量或模块参数的值。当您使用 Customizable Blocks 库中的 Knob 模块时，您可以自定义模块的外观，使其看起来像真实系统中的控件。您可以修改 Knob 模块上的范围和刻度值，以适合您要调整的值的所需范围。将 Knob 模块与其他仪表板模块一起使用，创建交互式仪表板来控制您的模型。

要在仿真运行时调整值，请使用指针将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。要在仿真未运行时调整值，请单击 Knob 模块以选择该模块，然后将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。

**注意**

- 在仿真期间或单击模块后双击已连接的 Knob 模块不会打开“模块参数”对话框。要打开“模块参数”对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间单击已连接的 Knob 模块会同时选择该模块并移动旋钮手柄。要在不移动旋钮手柄的情况下选择模块，请按 **Shift**，然后单击该模块。

### 自定义 Knob 模块

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

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中，单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。从出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，单击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示了如何将 Knob 模块连接到您的模型。

未连接的 Knob 模块连接到 Constant 模块。

### 参数记录

连接到仪表板模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

## 参数

使用 Property Inspector 和“模块参数”对话框来指定模块参数的值。要设置仪表板模块的核心参数，请使用“模块参数”对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的“模块参数”对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，在 **Design** 下，选择 **Property Inspector**。

## 参数

要设置仪表板模块的核心参数，请打开 Property Inspector 并单击 **Parameters** 选项卡。

#### 连接

### **Connection** — 要连接的模块参数值 连接参数值 连接选项

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

### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — 主刻度之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、标量值，指定刻度上主刻度的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Direction** — 刻度值增加的方向 `Clockwise` (default) | `Counterclockwise`

设置刻度值增加的方向。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Label** — 显示已连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

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

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会临时解锁纵横比。松开 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

### Design

要自定义仪表板模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。

#### Knob

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会解锁纵横比。松开 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、双精度、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — 主刻度之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、标量值，指定刻度上主刻度的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`x`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要使用 `Tick Interval` 的 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Origin** — 手柄移动和值条增长的刻度值 `auto` (default) | scalar

指定刻度上手柄移动和值条增长所依据的值。设置为 `auto` 时，`Origin` 是刻度的最小值。

**示例:** `0`

### **Direction** — 刻度值增加的方向 `Clockwise` (default) | `Counterclockwise`

设置刻度值增加的方向。

#### 编程使用

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Arc** — 刻度的弧长 `270` (default) | scalar

以 degrees 为单位，将刻度的弧长指定为标量值。

**示例:** `90`

### **Start Angle** — 刻度最小值的角度位置 `135` (default) | scalar

指定最小刻度值的角度位置，以从指向右侧的水平轴开始顺时针测量的 degrees 为单位。

**示例:** `0`

### **Inner Radius** — 刻度标记自由端的半径 scalar

将刻度标记自由端的半径指定为刻度边界框两个维度（宽度或高度）中较小者的比例。`Inner Radius` 可以大于 `Outer Radius`。

**示例:** `0.5`

### **Outer Radius** — 跨度线半径 scalar

将跨度线半径指定为刻度边界框两个维度（宽度或高度）中较小者的比例。`Outer Radius` 可以小于 `Inner Radius`。

**示例:** `0.5`

### **X Offset** — 刻度边界框左边缘距模块左边缘的水平偏移 scalar

将刻度边界框左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例:** `1`

### **Y Offset** — 刻度边界框顶边缘距模块顶边缘的垂直偏移 scalar

将刻度边界框顶边缘距模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例:** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比例。

**示例:** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比例。

**示例:** `2`

### **Lock Aspect Ratio** — 保持刻度纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整刻度大小时保持纵横比。

### **Tick Color** — 刻度标记、跨度线和模块名称的颜色 `[r g b]` 向量

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

### **Label Color** — 刻度标签字体颜色 `[r g b]` 向量

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Radius** — 标签距刻度中心的距离 scalar

将标签距刻度中心的距离指定为模块两个维度（宽度或高度）中较小者的比例。

**示例:** `0.5`

#### 手柄

### **Width** — 手柄图像宽度 scalar

将手柄图像的宽度指定为刻度边界框两个维度（宽度或长度）中较小者的比例。

**示例:** `1`

### **Height** — 手柄图像高度 scalar

将手柄图像的高度指定为刻度边界框两个维度（宽度或长度）中较小者的比例。

**示例:** `1`

### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### **Rotate Image** — 手柄图像的旋转 `180` (default) | scalar

以 90 度为增量围绕其中心旋转手柄图像。

**示例:** `90`

### **Offset from Center** — 手柄图像中心距刻度中心的偏移 `0` (default) | scalar

将手柄图像中心到刻度中心的距离指定为刻度直径的比例。

**示例:** `1`

#### 背景图像

### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像，或选择纯色。要选择纯色背景颜色，请打开 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用工具条更改背景颜色会移除背景图像并启用 **Use Background Color** 选项。

当您将纯色背景与 Circular Gauge 模块一起使用时，您可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Knob 模块

**示例:** `on`

### **Background Color** — 模块背景颜色 `[r g b]` 向量

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

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例:** `0.5`

### **Corner radius** — 模块背景颜色区域外边缘距刻度标记的偏移 scalar

设置模块背景颜色覆盖区域的外边缘距刻度标记的偏移，指定为从 `0` 到 `1` 的标量值。

**示例:** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

### **Y Offset** — 前景图像顶边缘距模块顶边缘的垂直偏移 scalar

将图像顶边缘距模块顶边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例:** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例:** `0.5`

### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

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

仪表板模块在代码生成时被忽略。

### 版本历史记录

**在 R2021a 中引入**

### R2025a: 在仿真期间选择仪表板模块并打开“模块参数”对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块代表的控件进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与模块本身进行交互。例如，您可以移动或调整模块的大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到仪表板面板的模块在面板在其自己的窗口中打开或停靠并解锁时也处于活动状态。对于 Callback Button 模块，如果按下按钮触发的至少一个回调具有非空值，则这些模块始终处于活动状态。要与非活动模块代表的控件进行交互，您可以通过单击该模块来临时激活它。取消选择该模块后，该模块将再次变为非活动状态。

单击活动的 Callback Button 模块或来自 Dashboard 或 Customizable Blocks 库的、连接到参数或变量值的活动模块，会同时选择该模块并与该模块代表的控件进行交互。例如，单击未选择的、活动的、已连接的 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后单击该模块来选择模块而不与控件交互。同样，您可以通过按 **Shift** 然后双击该模块来打开“模块参数”对话框。

### R2024b: 使用键盘解锁仪表板模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。松开 **Shift** 键时，纵横比会锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。松开 **Shift** 键时，纵横比会解锁。

### R2024a: 将仪表板面板部署为 Web 应用或独立桌面应用

拥有 Simulink Compiler™ 许可证，您现在可以将与面板连接的模型一起打包的仪表板面板部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作控件并监视面板上的显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a: 停靠仪表板面板

从 R2024a 开始，您可以将仪表板面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window 。

您可以单独于模型窗口最小化和还原包含面板的新窗口。从面板窗口，您可以运行、暂停、停止和逐步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，单击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a: Simulink Toolstrip 中的持久面板选项卡

当您将仪表板面板添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选择了面板时可见。从 R2023a 开始，当没有选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加一个空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b: 对面板中的可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中的可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b: 对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 来管理和编辑面板及其包含的仪表板模块。

当您单击面板中的仪表板模块时，该模块的工具条选项卡会出现。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在工具条中。

当您单击面板时，**Panel** 选项卡会出现在工具条中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022a: 更改刻度方向

从 R2022a 开始，您可以更改来自 **Customizable Blocks** 库的这些模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: 为值条和指针指定原点

刻度的原点是刻度上指针移动和值条增长所依据的值。从 R2022a 开始，您可以为来自 **Customizable Blocks** 库的这些模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: 调整前景图像的大小和位置

Customizable Blocks 库中的模块有一个选项，可以添加前景图像作为模块设计的一部分。从 R2022a 开始，您可以在模块设计内旋转、调整大小和重新定位前景图像。

### R2021b: 在 Raspberry Pi 板上部署可自定义的 Gauge 和 Knob 仪表板模块

从 2021b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 硬件板上部署 Circular Gauge 模块和 Knob 模块。

您可以自定义 Simulink 模型中模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

### R2021b: 在 Android 设备上部署可自定义的 Gauge 和 Knob 仪表板模块

从 2021b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署 Circular Gauge 模块和 Knob 模块。

您可以自定义 Simulink 模型中模块的视觉方面，并在您的 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。
