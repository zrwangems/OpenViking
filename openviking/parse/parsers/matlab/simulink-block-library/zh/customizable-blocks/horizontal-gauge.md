---
type: simulink-block
title: 'Horizontal Gauge'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'horizontalgauge'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Gauge

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要为模块打开 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### 信号

### **Connection** — 要连接的信号及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 中，在 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 dashboard 模块连接到 Stateflow chart。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认：** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Scale Direction** — 刻度值递增方向 `'Left to right'`（默认） | `'Right to left'`

设置刻度值递增的方向。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果希望标签可见，请指定标签的位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

锁定宽高比时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。解锁宽高比时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

锁定宽高比时，在调整模块大小期间按下 **Shift** 键会临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。解锁宽高比时，在调整模块大小期间按下 **Shift** 键会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### **Scale Colors** — 仪表刻度上用于刻度范围的颜色指示

刻度上值范围的颜色设定。点击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要显示该颜色的范围的最小值和最大值。

#### 编程用法

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — `1`-by-`3` 的 `double` 值向量，值介于 `0` 和 `1` 之间，以 `[r g b]` 形式指定范围的颜色

为要指定颜色的每个刻度范围在数组中包含一个结构体。

    range1.Min = 0;
    range1.Max = 10;
    range1.Color = [0 0 1];
    range2.Min = 10;
    range2.Max = 15;
    range2.Color = [0 1 0];
    scaleRanges = [range1 range2];

|  |
| --- |
| **模块参数：** `ScaleColors` |
| **类型：** structure array |
| **默认：** `0x1` struct array |

### 设计

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### 线性仪表

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

锁定宽高比时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。解锁宽高比时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

锁定宽高比时，在调整模块大小期间按下 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比会锁定。解锁宽高比时，在调整模块大小期间按下 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将该向量中 `Tick Interval` 的位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Origin** — 刻度上指针移动和值条增长所依据的值 `auto`（默认） | scalar

指定刻度上指针移动和值条增长所依据的值。设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **Scale Direction** — 刻度值递增方向 `'Left to right'`（默认） | `'Right to left'`

设置刻度值递增的方向。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

将刻度边界框的左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的刻度位置，负值偏移将刻度向左移动，正值偏移将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

将刻度边界框的上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的刻度位置，负值偏移将刻度向上移动，正值偏移将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比例。

**示例：** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比例。

**示例：** `2`

### **Lock Aspect Ratio** — 用于保持刻度宽高比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整刻度大小时保持宽高比。

### **Tick Color** — 刻度线、跨线和模块名称的颜色 `[r g b]` 向量

设置刻度线、跨线和模块名称的颜色。从标准颜色调色板中选择一种颜色，或指定自定义颜色。

**提示**

您还可以通过在 Simulink Toolstrip 的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` 向量。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` 向量 |

### **Label Color** — 刻度标签字体颜色 `[r g b]` 向量

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Offset** — 刻度标签与刻度线自由端之间的垂直距离 `0.3`（默认） | scalar

将刻度标签到刻度上其对应刻度线自由端的垂直距离指定为刻度边界框高度的比例。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

将指针图像的宽度指定为模块宽度的比例。

**示例：** `1`

### **Height** — 指针图像高度 scalar

将指针图像的高度指定为模块高度的比例。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持宽高比。

### **X Offset** — 指针图像中心相对于刻度原点的水平偏移 scalar

将指针图像中心相对于刻度原点的水平偏移指定为指针图像宽度的比例。相对于偏移为 `0` 时的指针图像位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 指针图像上边缘相对于刻度跨线的垂直偏移 scalar

将指针图像上边缘相对于刻度跨线的垂直偏移指定为指针图像高度的比例。相对于偏移为 `0` 时的指针图像位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

#### 值条

### **Offset from Scale** — 值条上边缘与跨线之间的距离 `0`（默认） | scalar

将值条上边缘到跨线的距离指定为刻度边界框高度的比例。相对于偏移为 `0` 时的值条位置，负值偏移将值条向上移动，正值偏移将值条向下移动。

**示例：** `0.25`

### **Size** — 值条粗细 scalar

将值条的粗细指定为刻度边界框高度的比例。

**示例：** `0.3`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景色的选项 `off`（默认） | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，并格式化为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` 向量 |

### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持宽高比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**R2020a 中引入**

### R2024b：使用键盘解锁 dashboard 模块宽高比

如果 Dashboard 库中模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。

如果宽高比已解锁，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

有了 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板（与面板所连接的模型一起打包）部署为独立桌面应用或 Web 应用。您可以使用该应用操作控件并监视面板上的显示，而不依赖于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号并控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

您可以从模型窗口单独最小化和还原包含面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久 Panels 选项卡

当您将 dashboard 面板添加到模型时，Simulink Toolstrip 中会显示 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时，**Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义 dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以对面板中可自定义 dashboard 模块所做的更改进行撤销和重做。

要撤销或重做更改：

1. 点击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您点击面板中的 dashboard 模块时，会显示该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，工具条中会显示 **Gauge** 选项卡。

当您点击面板时，工具条中会显示 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b：在 Raspberry Pi 板上对可自定义 Dashboard 模块的扩展支持

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

您可以自定义 Simulink 模型中模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022b：在 Android 设备上对可自定义 Dashboard 模块的扩展支持

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

您可以自定义 Simulink 模型中模块的视觉方面，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022a：更改刻度方向

从 R2022a 开始，您可以更改 **Customizable Blocks** 库中以下模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：为值条和指针指定原点

刻度的原点是刻度上指针移动和值条增长所依据的值。从 R2022a 开始，您可以为 **Customizable Blocks** 库中以下模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：调整前景图像大小并重新定位

Customizable Blocks 库中的模块有一个选项，可添加前景图像作为模块设计的一部分。从 R2022a 开始，您可以在模块设计中旋转、调整大小并重新定位前景图像。

### R2021a：可自定义 dashboard 模块仪表移至 Customizable Blocks 库

在之前的版本中，Dashboard 库包含 Circular Gauge、Horizontal Gauge 和 Vertical Gauge 模块。从 R2021a 开始，这些模块位于 Dashboard 库中的 Customizable Blocks 子库中。

### R2021a：Dashboard 仪表模块支持前景色、背景色和字体颜色

从 R2021a 开始，您可以更改以下模块的前景色、背景色和字体颜色：

- Gauge
- Half Gauge
- Linear Gauge
- Quarter Gauge
- Circular Gauge
- Horizontal Gauge
- Vertical Gauge

### R2020b：对 dashboard 模块的 Simulink 工具条支持

从 R2020b 开始，当您从 Simulink Dashboard 库或从 Aerospace Blockset™ Flight Control Analysis Library 中的 Flight Instruments 库选择模型中的模块时，Simulink Toolstrip 会打开一个模块特定的选项卡。在工具条中，您可以连接、断开连接和修改所选模块的连接。您还可以跳转到连接到所选模块的模型元素，并将所选模块添加到面板。

### R2020b：向 Horizontal Gauge、Vertical Gauge 和 Circular Gauge 模块添加前景图像

从 R2020b 开始，您可以向模型中的 Horizontal Gauge、Vertical Gauge 或 Circular Gauge 模块添加前景图像。

## 描述

在仿真期间在水平仪表上显示信号值，外观可自定义

在仿真期间，Horizontal Gauge 模块在可自定义外观以类似于真实系统中仪表的线性仪表上显示所连接信号的值。您可以修改 Horizontal Gauge 模块上的范围和刻度值，以适合您的数据。将 Horizontal Gauge 模块与其他 dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式 dashboard。

### 自定义 Horizontal Gauge 模块

当您将 Horizontal Gauge 模块添加到模型时，该模块已预配置为默认设计。您可以将该模块与默认设计一起使用，也可以自定义该模块的外观。

要自定义该模块的外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，在 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义圆形仪表。要访问更多自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的 Horizontal Gauge 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传指针图像。 | Yes | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景颜色。 | No | Yes |
| 上传前景图像。 | No | Yes |
| 指定值条从其增长的原点位置。 | No | Yes |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | Yes | Yes |
| 将刻度方向指定为从左到右或从右到左。 | No | Yes |
| 更改刻度和指针的大小。 | No | Yes |
| 更改刻度和指针的位置。 | No | Yes |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中，选择要更改其颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小并重新定位组件。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮 。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® chart。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Horizontal Gauge 模块连接到您的模型。

未连接的 Horizontal Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。
