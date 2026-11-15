---
type: simulink-block
title: 'Horizontal Slider'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'horizontalslider'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Slider

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **参数** 选项卡。要自定义模块，请使用 Property Inspector 中的 **设计** 选项卡。要为模块打开 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **建模** 选项卡上，在 **设计** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector 并点击 **参数** 选项卡。

#### 连接

### **Connection** — 要连接到的模块参数值 参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关连接模式以及如何使用工具条连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **参数** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 dashboard 模块连接到由值定义的参数，某些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、double、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、double、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (default) | scalar

有限、实数、正、整数、标量值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Scale Direction** — 刻度值增加的方向 `'Left to right'` (default) | `'Right to left'`

设置刻度值增加的方向。

#### 编程用法

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空。

#### 编程用法

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

锁定纵横比时，添加新背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。解锁纵横比时，添加新背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

锁定纵横比时，在调整模块大小期间按 **Shift** 键会临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。解锁纵横比时，在调整模块大小期间按 **Shift** 键会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

### 设计

要自定义 dashboard 模块，请打开 Property Inspector，点击 **设计** 选项卡，然后点击 **编辑**。

#### 滑块

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持纵横比。

锁定纵横比时，添加新背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。解锁纵横比时，添加新背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

锁定纵横比时，在调整模块大小期间按 **Shift** 键会解锁纵横比。释放 **Shift** 键时，纵横比锁定。解锁纵横比时，在调整模块大小期间按 **Shift** 键会锁定纵横比。释放 **Shift** 键时，纵横比解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0` (default) | scalar

有限、实数、double、标量值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (default) | scalar

有限、实数、double、标量值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (default) | scalar

有限、实数、正、整数、标量值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **Block Parameter:** `Limits` |
| **Type:** `1x3` vector |
| **Default:** `[0 -1 100]` |

### **Origin** — 手柄移动和值条增长所依据的刻度上的值 `auto` (default) | scalar

指定刻度上手柄移动和值条增长所依据的值。设置为 `auto` 时，`Origin` 是刻度的最小值。

**示例:** `0`

### **Scale Direction** — 刻度值增加的方向 `'Left to right'` (default) | `'Right to left'`

设置刻度值增加的方向。

#### 编程用法

|  |
| --- |
| **Block Parameter:** `ScaleDirection` |
| **Type:** character vector |
| **Values:** `'Clockwise'` | `'Counterclockwise'` |
| **Default:** `'Clockwise'` |

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移量 scalar

指定刻度边界框左边缘相对于模块左边缘的水平偏移量，作为模块宽度的比率。相对于偏移量为 `0` 时刻度的位置，负值偏移量将刻度向左移动，正值偏移量将刻度向右移动。

**示例:** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移量 scalar

指定刻度边界框上边缘相对于模块上边缘的垂直偏移量，作为模块高度的比率。相对于偏移量为 `0` 时刻度的位置，负值偏移量将刻度向上移动，正值偏移量将刻度向下移动。

**示例:** `1`

### **Width** — 刻度宽度 scalar

指定刻度边界框的宽度，作为模块宽度的比率。

**示例:** `2`

### **Height** — 刻度高度 scalar

指定刻度边界框的高度，作为模块高度的比率。

**示例:** `2`

### **Lock Aspect Ratio** — 保持刻度纵横比的选项 `on` (default) | `off`

选择此参数以在使用 Property Inspector 调整刻度大小时保持纵横比。

### **Tick Color** — 刻度线、跨越线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨越线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以通过在 Simulink Toolstrip 的 **格式** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Offset** — 刻度标签与刻度线自由端之间的垂直距离 `0.3` (default) | scalar

指定从刻度标签到刻度上对应刻度线自由端的垂直距离，作为刻度边界框高度的比率。

**示例:** `0.5`

#### 手柄

### **Width** — 手柄图像宽度 scalar

指定手柄图像的宽度，作为模块宽度的比率。

**示例:** `1`

### **Height** — 手柄图像高度 scalar

指定手柄图像的高度，作为模块高度的比率。

**示例:** `1`

### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (default) | `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持纵横比。

### **X Offset** — 手柄图像中心相对于刻度原点的水平偏移量 scalar

指定手柄图像中心相对于刻度原点的水平偏移量，作为手柄图像宽度的比率。相对于偏移量为 `0` 时手柄图像的位置，负值偏移量将图像向左移动，正值偏移量将图像向右移动。

**示例:** `1`

### **Y Offset** — 手柄图像上边缘相对于刻度跨越线的垂直偏移量 scalar

指定手柄图像上边缘相对于刻度跨越线的垂直偏移量，作为手柄图像高度的比率。相对于偏移量为 `0` 时手柄图像的位置，负值偏移量将图像向上移动，正值偏移量将图像向下移动。

**示例:** `1`

#### 值条

### **Offset from Scale** — 值条上边缘与跨越线之间的距离 `0` (default) | scalar

指定从值条上边缘到跨越线的距离，作为刻度边界框高度的比率。相对于偏移量为 `0` 时值条的位置，负值偏移量将值条向上移动，正值偏移量将值条向下移动。

**示例:** `0.25`

### **Size** — 值条厚度 scalar

指定值条的厚度，作为刻度边界框高度的比率。

**示例:** `0.3`

#### 背景图像

### **Use Background Color** — 指定纯色模块背景色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **格式** 选项卡更改背景色会移除背景图像并启用 **Use Background Color** 参数。

**示例:** `on`

### **Color** — 模块背景色 `[r g b]` vector

要使用纯色背景色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **格式** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为一个 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，并格式化为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例:** `0.5`

### **Corner Radius** — 具有模块背景色区域的圆角半径 scalar

指定模块背景色所覆盖区域的圆角半径，作为模块两个尺寸（宽度或高度）中较小者的一半的比率。

**示例:** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移量 scalar

指定图像左边缘相对于模块左边缘的水平偏移量，作为模块宽度的比率。相对于偏移量为 `0` 时图像的位置，负值偏移量将图像向左移动，正值偏移量将图像向右移动。

**示例:** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移量 scalar

指定图像上边缘相对于模块上边缘的垂直偏移量，作为模块高度的比率。相对于偏移量为 `0` 时图像的位置，负值偏移量将图像向上移动，正值偏移量将图像向下移动。

**示例:** `1`

### **Width** — 前景图像宽度 scalar

指定前景图像的宽度，作为模块宽度的比率。

**示例:** `0.5`

### **Height** — 前景图像高度 scalar

指定前景图像的高度，作为模块高度的比率。

**示例:** `0.5`

### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持纵横比。

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

**R2021a 中引入**

### R2025a: 在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的 gadget 交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 dashboard 面板的模块在面板于其自己的窗口中打开或停靠且解锁时也处于活动状态。对于至少一个通过按下按钮触发的回调具有非空值的 Callback Button 模块，这些模块始终处于活动状态。要与非活动模块所代表的 gadget 交互，您可以通过点击该模块来临时激活它。取消选择该模块后，该模块会再次变为非活动状态。

点击活动的 Callback Button 模块或连接到参数或变量值的、来自 Dashboard 或 Customizable Blocks 库的活动模块，会同时选择该模块并与该模块所代表的 gadget 交互。例如，点击未选中的活动已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后点击该模块来选择模块而不与 gadget 交互。类似地，您可以通过按 **Shift** 然后双击该模块来打开 Block Parameters 对话框。

### R2024b: 使用键盘解锁 dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

### R2024a: 将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板（与其连接的模型一起打包）部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a: 停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板，并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。从面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，点击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a: Simulink Toolstrip 中的持久 **Panels** 选项卡

将 dashboard 面板添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b: 对面板中的可自定义 dashboard 模块提供撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中的可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b: 对面板提供 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您点击面板中的 dashboard 模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，**Gauge** 选项卡会出现在工具条中。

当您点击面板时，**Panel** 选项卡会出现在工具条中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b: 扩展对 Raspberry Pi 板卡上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 板卡上部署来自 **Customizable Blocks** 库的以下模块：

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

### R2022b: 扩展对 Android 设备上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署来自 **Customizable Blocks** 库的以下模块：

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在您的 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022a: 更改刻度方向

从 R2022a 开始，您可以更改来自 **Customizable Blocks** 库的以下模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: 为值条和手柄指定原点

刻度的原点是刻度上手柄移动和值条增长所依据的值。从 R2022a 开始，您可以为来自 **Customizable Blocks** 库的以下模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a: 调整前景图像大小和位置

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整大小和重新定位前景图像。

## 描述

使用具有可自定义外观的 Horizontal Slider 更改参数或变量值

使用 Horizontal Slider 模块在仿真期间调整变量或模块参数的值。您可以自定义 Horizontal Slider 模块的外观，使其看起来像真实系统中的控件。您可以调整刻度范围和刻度值，以适合要调整的值的所需范围。将 Horizontal Slider 模块与其他 dashboard 模块一起使用，以创建交互式 dashboard 来控制模型。

要在仿真运行时调整值，使用指针将手柄拖到要连接变量或模块参数设置为的刻度值。要在仿真未运行时调整值，点击 Horizontal Slider 模块以选择该模块，然后将手柄拖到要连接变量或模块参数设置为的刻度值。

**注意**

- 在仿真期间或点击已连接的 Horizontal Slider 模块后，双击该模块不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Horizontal Slider 模块会同时选择该模块并移动滑块手柄。要在不移动滑块手柄的情况下选择该模块，请按 **Shift**，然后点击该模块。

### 自定义 Horizontal Slider 模块

将 Horizontal Slider 模块添加到模型时，该模块预配置为默认设计。您可以使用默认设计使用该模块，也可以自定义该模块的外观。

要自定义模块外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在该模块特定的选项卡上，在 **设计** 下，点击 **编辑**。
- 在 Property Inspector 中，在 **设计** 选项卡上，点击 **编辑**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮。

在设计模式中，可以使用模块上方的工具栏自定义圆形仪表。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **设计** 选项卡。

处于设计模式的 Horizontal Slider 模块，工具栏和 Property Inspector 中的 **设计** 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **设计** 选项卡中可用 |
| --- | --- | --- |
| 上传手柄图像。 | Yes | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景色。 | No | Yes |
| 上传前景图像。 | No | Yes |
| 指定值条增长所依据的原点位置。 | No | Yes |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | Yes | Yes |
| 将刻度方向指定为从左到右或从右到左。 | No | Yes |
| 更改刻度和手柄的大小。 | No | Yes |
| 更改刻度和手柄的位置。 | No | Yes |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中，选择要更改颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **设计** 选项卡自定义模块设计外，还可以在画布中交互式调整组件大小和位置。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画演示如何将 Horizontal Gauge 模块连接到模型。

未连接的 Horizontal Slider 模块连接到 Constant 模块。

### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
