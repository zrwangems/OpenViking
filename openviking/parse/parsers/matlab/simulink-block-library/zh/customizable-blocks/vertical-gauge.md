---
type: simulink-block
title: 'Vertical Gauge'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'verticalgauge'
language: zh-CN
chinese_source: worker-translation
---

# Vertical Gauge

## 端口

R2025b 官方文档未提供。

## 参数

使用属性检查器和模块参数对话框指定模块参数的值。要设置 Dashboard 模块的核心参数，请使用模块参数对话框或属性检查器中的 **参数** 选项卡。要自定义模块，请使用属性检查器中的 **设计** 选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在 **建模** 选项卡上的 **设计** 下，选择 **属性检查器**。

要设置 Dashboard 模块的核心参数，请打开属性检查器并单击 **参数** 选项卡。

#### 信号

### **Connection** — 要连接的信号和显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或模块参数对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择模块。
2. 要连接模块，请在属性检查器中的 **参数** 选项卡上，单击 **连接**。要更改模块的连接，请改为单击 **更改**。
3. 选择要连接到的信号线。
4. 在表中，选择要连接到的信号。
5. 单击 **应用**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow（Stateflow）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认：** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以程序化方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以程序化方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以程序化方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Scale Direction** — 刻度值增加的方向 `'Bottom to top'`（默认） | `'Top to bottom'`

设置刻度值增加的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` \| `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签位置 `Top`（默认） | `Bottom` | `Hide`

您可以在位于模块顶部或底部的标签中显示 Dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请指定 `Hide`。

**注意**

当 Dashboard 模块未连接到元素时，标签为空白。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Top'` \| `'Bottom'` \| `'Hide'` |
| **默认：** `'Top'` |

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

锁定宽高比时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。未锁定宽高比时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

锁定宽高比时，在调整模块大小时按下 **Shift** 键会暂时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。未锁定宽高比时，在调整模块大小时按下 **Shift** 键会暂时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### **Scale Colors** — 仪表刻度上用于刻度范围的颜色指示

刻度上值范围的颜色规格。单击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要显示该颜色的范围的最小值和最大值。

#### 程序化使用

要以程序化方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — `1`-by-`3` 的 `double` 值 vector，值介于 `0` 和 `1` 之间，以 `[r g b]` 形式指定该范围的颜色

对于要指定颜色的每个刻度范围，在数组中包含一个结构体。

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

要自定义 Dashboard 模块，请打开属性检查器，单击 **设计** 选项卡，然后单击 **编辑**。

#### 线性仪表

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

锁定宽高比时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。未锁定宽高比时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

锁定宽高比时，在调整模块大小时按下 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比会锁定。未锁定宽高比时，在调整模块大小时按下 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以程序化方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以程序化方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以程序化方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Origin** — 指针移动和值条增长所依据的刻度值 `auto`（默认） | scalar

指定指针移动和值条增长所依据的刻度值。当设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **Scale Direction** — 刻度值增加的方向 `'Bottom to top'`（默认） | `'Top to bottom'`

设置刻度值增加的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` \| `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **X Offset** — 刻度边界框左边缘距模块左边缘的水平偏移 scalar

将刻度边界框左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的刻度位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘距模块上边缘的垂直偏移 scalar

将刻度边界框上边缘距模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的刻度位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比例。

**示例：** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比例。

**示例：** `2`

### **Lock Aspect Ratio** — 保持刻度宽高比的选项 `on`（默认） | `off`

选择此参数可在使用属性检查器调整刻度大小时保持宽高比。

### **Tick Color** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以通过在 Simulink 工具条的 **格式** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 程序化使用

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，该值定义 `1`-by-`3` 的 `[r g b]` vector，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector \| string |
| **值：** `[r g b]` vector |

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择刻度标签的字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Offset** — 刻度标签距刻度线自由端的水平距离 `0.3`（默认） | scalar

将刻度标签到其对应刻度线自由端的水平距离指定为刻度边界框宽度的比例。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

将指针图像的宽度指定为模块宽度的比例。

**示例：** `1`

### **Height** — 指针图像高度 scalar

将指针图像的高度指定为模块高度的比例。

**示例：** `1`

### **Lock Aspect Ratio** — 保持图像宽高比的选项 `on`（默认） | `off`

选择此参数可在使用属性检查器调整图像大小时保持宽高比。

### **X Offset** — 指针图像左边缘距刻度跨度线的水平偏移 scalar

将指针图像左边缘距刻度跨度线的水平偏移指定为指针图像宽度的比例。相对于偏移为 `0` 时的指针图像位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 指针图像中心距刻度原点的垂直偏移 scalar

将指针图像中心距刻度原点的垂直偏移指定为指针图像高度的比例。相对于偏移为 `0` 时的指针图像位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

#### 值条

### **Offset from Scale** — 值条左边缘距跨度线的距离 `0`（默认） | scalar

将值条左边缘到跨度线的距离指定为刻度边界框宽度的比例。相对于偏移为 `0` 时的值条位置，负值偏移会将值条向左移动，正值偏移会将值条向右移动。

**示例：** `0.25`

### **Size** — 值条粗细 scalar

将值条的粗细指定为刻度边界框宽度的比例。

**示例：** `0.3`

#### 背景图像

### **Use Background Color** — 指定纯色模块背景色的选项 `off`（默认） | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的 **格式** 选项卡更改背景色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景色 `[r g b]` vector

要使用纯色背景色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**提示**

您还可以在 Simulink 工具条的 **格式** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 程序化使用

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` 的 `[r g b]` vector，值介于 `0` 和 `1` 之间，格式为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string \| character vector |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景色的区域的圆角半径 scalar

将模块背景色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者一半的比例。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘距模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持前景图像宽高比的选项 `on`（默认） | `off`

选择此参数可在使用属性检查器调整图像大小时保持宽高比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成中被忽略。

## 版本历史

**在 R2020a 中引入**

### R2024b：使用键盘解锁 Dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。

如果宽高比未锁定，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### R2024a：将 Dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将与面板所连接模型一起打包的 Dashboard 面板部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作控件并监视面板上的显示。

要了解如何部署面板，请参阅将 Dashboard 面板部署为应用。

### R2024a：停靠 Dashboard 面板

从 R2024a 开始，您可以将 Dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而无需覆盖画布中的模型图。

有关详细信息，请参阅停靠面板。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 Dashboard 面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，单击“在新窗口中打开” 。

您可以从模型窗口之外单独最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，单击“在画布中打开” 。

有关在新窗口中打开面板的详细信息，请参阅在新窗口中打开面板。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将 Dashboard 面板添加到模型时，**面板** 选项卡会出现在 Simulink 工具条中，并显示用于管理和编辑面板的选项。

以前，**面板** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时，**面板** 选项卡仍保持可见。

**面板** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：支持撤销和重做面板中的可自定义 Dashboard 模块

从 R2022b 开始，您可以撤销和重做对面板中可自定义 Dashboard 模块所做的更改。

要撤销或重做更改：

1. 单击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的 Dashboard 模块。

当您单击面板中的 Dashboard 模块时，该模块的工具条选项卡会出现。例如，当您单击 Circular Gauge 模块时，工具条中会出现 **仪表** 选项卡。

当您单击面板时，工具条中会出现 **面板** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
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

您可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器中获得所见即所得 (WYSIWYG) 可视化。

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器中获得所见即所得 (WYSIWYG) 可视化。

### R2022a：更改刻度方向

从 R2022a 开始，您可以更改以下来自 **Customizable Blocks** 库的模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：为值条和指针指定原点

刻度的原点是刻度上指针移动和值条增长所依据的值。从 R2022a 开始，您可以为以下来自 **Customizable Blocks** 库的模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：调整前景图像大小和位置

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整前景图像大小和重新定位前景图像。

### R2021a：可自定义 Dashboard 模块仪表移至 Customizable Blocks 库

在以前的版本中，Dashboard 库包含 Circular Gauge、Horizontal Gauge 和 Vertical Gauge 模块。从 R2021a 开始，这些模块位于 Dashboard 库中的 Customizable Blocks 子库中。

### R2021a：Dashboard 仪表模块支持前景色、背景色和字体颜色

从 R2021a 开始，您可以更改以下模块的前景色、背景色和字体颜色：

- Gauge
- Half Gauge
- Linear Gauge
- Quarter Gauge
- Circular Gauge
- Horizontal Gauge
- Vertical Gauge

### R2020b：Simulink 工具条对 Dashboard 模块的支持

从 R2020b 开始，当您在模型中选择来自 Simulink Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis Library 中的 Flight Instruments 库的模块时，Simulink 工具条会打开特定于模块的选项卡。您可以从工具条连接、断开连接和修改所选模块的连接。您还可以跳转到连接到所选模块的模型元素，并将所选模块添加到面板。

### R2020b：向 Horizontal Gauge、Vertical Gauge 和 Circular Gauge 模块添加前景图像

从 R2020b 开始，您可以向模型中的 Horizontal Gauge、Vertical Gauge 或 Circular Gauge 模块添加前景图像。

## 描述

在仿真期间在具有可自定义外观的 vertical gauge 上显示信号值

在仿真期间，Vertical Gauge 模块在 linear gauge 上显示所连接信号的值，您可以自定义该 gauge，使其看起来像真实系统中的仪表。您可以修改 Vertical Gauge 模块上的范围和刻度值以适合您的数据。将 Vertical Gauge 模块与其他 Dashboard 模块一起使用，为您的模型构建包含控件和指示器的交互式 Dashboard。

### 自定义 Vertical Gauge 模块

当您将 Vertical Gauge 模块添加到模型时，该模块已预配置为默认设计。您可以将该模块与默认设计一起使用，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® 工具条上，在特定于模块的选项卡上的 **设计** 下，单击 **编辑**。
- 在属性检查器中，在 **设计** 选项卡上，单击 **编辑**。
- 将鼠标悬停在模块上出现的省略号上，然后单击“编辑自定义模块”按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义 circular gauge。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **设计** 选项卡。

处于设计模式的 Vertical Gauge 模块，其中工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **设计** 选项卡中可用 |
| --- | --- | --- |
| 上传指针图像。 | Yes | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景色。 | No | Yes |
| 上传前景图像。 | No | Yes |
| 指定值条增长所依据的原点位置。 | No | Yes |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | Yes | Yes |
| 将刻度方向指定为从左到右或从右到左。 | No | Yes |
| 更改刻度和指针的大小。 | No | Yes |
| 更改刻度和指针的位置。 | No | Yes |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中，选择要更改其颜色的组件。要更改颜色，请单击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **设计** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和位置。

完成编辑设计后，要退出设计模式，请单击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后单击“连接”按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中单击“连接”按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接到的信号线。在出现的列表中，选择要连接到的信号。然后，将鼠标悬停在 Dashboard 模块上，并单击“完成连接”按钮 。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow（Stateflow）。

此动画显示如何将 Vertical Gauge 模块连接到您的模型。

未连接的 Vertical Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。
