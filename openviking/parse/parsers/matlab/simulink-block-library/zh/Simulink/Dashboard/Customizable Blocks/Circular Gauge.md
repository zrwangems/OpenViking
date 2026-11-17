---
type: simulink-block
title: 'Circular Gauge'
family: 'dashboard'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'circulargauge'
documentation_source_path: 'slref/circulargauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Circular Gauge

## 端口

在 R2025b 中未记录。

## 参数

使用属性检查器和模块参数对话框指定模块参数的值。要设置仪表盘模块的核心参数，请使用模块参数对话框或属性检查器中的 **参数** 选项卡。要自定义模块，请使用属性检查器中的 **设计** 选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在 **建模** 选项卡上的 **设计** 下，选择 **属性检查器**。

### 参数

要设置仪表盘模块的核心参数，请打开属性检查器，并点击 **参数** 选项卡。

#### 信号

### **连接** — 要连接的信号及显示信号连接选项

仪表盘模块不使用端口连接到模型元素。要将仪表盘模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或模块参数对话框中的 **连接** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅将仪表盘模块连接到 Simulink 模型。

要使用 **连接** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **参数** 选项卡上点击 **连接**。要更改该模块的连接，请改为点击 **更改**。
3. 选择要连接到的信号线。
4. 在表中，选择要连接到的信号。
5. 点击 **应用**。

您还可以将仪表盘模块连接到 Stateflow 图。有关详细信息，请参阅将仪表盘模块连接到 Stateflow（Stateflow）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认：** `[]` |

#### 主要

### **最小值** — 最小刻度线值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度线值。参数值必须小于 **最大值** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **最大值** — 最大刻度线值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度线值。参数值必须大于 **最小值** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **刻度间隔** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **最大值** 和 **最小值** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **方向** — 刻度值增加的方向 `Clockwise`（默认） | `Counterclockwise`

设置刻度值增加的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **标签** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示仪表盘模块所连接元素的名称，也可以隐藏标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表盘模块未连接到元素时，标签为空。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认：** `'Hide'` |

### **锁定宽高比** — 保持模块宽高比的选项 `on`（默认） | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定后，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比解锁后，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块大小。

当宽高比锁定后，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当您释放 **Shift** 键时，宽高比会锁定。当宽高比解锁后，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当您释放 **Shift** 键时，宽高比会解锁。

### **刻度颜色** — 仪表刻度上刻度范围的颜色指示

刻度上值范围的颜色规格。点击 **+** 按钮添加一个刻度颜色。对于添加的每种颜色，请指定要显示该颜色的范围的最小值和最大值。

#### 程序化使用

要以编程方式指定 `Scale Colors` 参数，请使用具有以下字段的 structure array：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — 一个 `1`-by-`3` 的 `double` 值 vector，值介于 `0` 和 `1` 之间，以 `[r g b]` 形式指定该范围的颜色

在 array 中为您想要指定颜色的每个刻度范围包含一个 structure。

```
range1.Min = 0;
range1.Max = 10;
range1.Color = [0 0 1];
range2.Min = 10;
range2.Max = 15;
range2.Color = [0 1 0];
scaleRanges = [range1 range2];
```

|  |
| --- |
| **模块参数：** `ScaleColors` |
| **类型：** structure array |
| **默认：** `0x1` struct array |

### 设计

要自定义仪表盘模块，请打开属性检查器，点击 **设计** 选项卡，然后点击 **编辑**。

#### Circular Gauge

### **锁定宽高比** — 保持模块宽高比的选项 `on`（默认） | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定后，添加新的背景图像会更改模块的宽高比以匹配背景图像的宽高比。当宽高比解锁后，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块大小。

当宽高比锁定后，在调整模块大小时按 **Shift** 键会解锁宽高比。当您释放 **Shift** 键时，宽高比会锁定。当宽高比解锁后，在调整模块大小时按 **Shift** 键会锁定宽高比。当您释放 **Shift** 键时，宽高比会解锁。

#### 刻度

### **最小值** — 最小刻度线值 `0`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度线值。参数值必须小于 **最大值** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **最大值** — 最大刻度线值 `100`（默认） | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度线值。参数值必须大于 **最小值** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **刻度间隔** — 主刻度线之间的间隔 `auto`（默认） | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **最大值** 和 **最小值** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **原点** — 刻度上指针移动和值条增长所依据的值 `auto`（默认） | scalar

指定刻度上指针移动和值条增长所依据的值。当设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **方向** — 刻度值增加的方向 `Clockwise`（默认） | `Counterclockwise`

设置刻度值增加的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **弧** — 刻度的弧长 `270`（默认） | scalar

将刻度的弧长指定为 scalar 值，以 degrees 为单位。

**示例：** `90`

### **起始角度** — 刻度最小值的角度位置 `135`（默认） | scalar

指定刻度最小值的角度位置，以 degrees 为单位，从指向右方的水平轴开始顺时针测量。

**示例：** `0`

### **内半径** — 刻度线自由端的半径 scalar

将刻度线自由端的半径指定为刻度边界框两个维度（宽度或高度）中较小者的比率。`Inner Radius` 可以大于 `Outer Radius`。

**示例：** `0.5`

### **外半径** — 跨度线半径 scalar

将跨度线半径指定为刻度边界框两个维度（宽度或高度）中较小者的比率。`Outer Radius` 可以小于 `Inner Radius`。

**示例：** `0.5`

### **X 偏移** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

将刻度边界框左边缘相对于模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时的刻度位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例：** `1`

### **Y 偏移** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

将刻度边界框上边缘相对于模块上边缘的垂直偏移指定为模块高度的比率。相对于偏移为 `0` 时的刻度位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例：** `1`

### **宽度** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比率。

**示例：** `2`

### **高度** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比率。

**示例：** `2`

### **锁定宽高比** — 保持刻度宽高比的选项 `on`（默认） | `off`

选择此参数以在使用属性检查器调整刻度大小时保持宽高比。

### **刻度线颜色** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您也可以通过在 Simulink 工具条的 **格式** 选项卡上选择 **前景色** 来设置 **刻度线颜色**。

要指定模块文本的颜色，请使用 **标签颜色** 参数。

#### 程序化使用

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，该 string 或 character vector 定义值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` vector。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **次刻度高度** — 刻度上次刻度线的高度 `1`（默认） | scalar

将刻度上次刻度线的高度指定为高度与外半径和内半径之差的比率。

**示例：** `0.5`

### **标签颜色** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择刻度标签的字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **刻度线颜色** 参数。

### **标签半径** — 刻度标签与刻度中心的距离 scalar

将刻度标签与刻度中心的距离指定为刻度半径的比率。

**示例：** `0.5`

#### 指针

### **宽度** — 指针图像宽度 scalar

将指针图像的宽度指定为刻度边界框两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **高度** — 指针图像高度 scalar

将指针图像的高度指定为刻度边界框两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **锁定宽高比** — 保持图像宽高比的选项 `on`（默认） | `off`

选择此参数以在使用属性检查器调整图像大小时保持宽高比。

### **旋转图像** — 指针图像的旋转 `180`（默认） | scalar

将指针图像绕其中心以 90 degree 为增量旋转。

**示例：** `90`

### **距中心偏移** — 指针图像中心相对于刻度中心的偏移 `0`（默认） | scalar

将指针图像中心到刻度中心的距离指定为刻度直径的比率。

**示例：** `1`

#### 背景图像

### **使用背景色** — 用于指定纯色模块背景色的选项 `off`（默认）| `on`

对于模块背景，你可以提供背景图像或选择纯色。要选择纯色背景色，请打开 **使用背景色**。要提供背景图像，请关闭 **使用背景色**。

**注意**

使用工具条更改背景色会移除背景图像并启用 **使用背景色** 选项。

将纯色背景与 Circular Gauge 模块一起使用时，可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Circular Gauge 模块

**示例:** `on`

### **颜色** — 模块背景色 `[r g b]` 向量

要选择纯色背景色，请启用 **使用背景色** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**注意**

将纯色背景与 Circular Gauge 模块一起使用时，可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Circular Gauge 模块

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为 string 或 character vector。

|  |
| --- |
| **模块参数:** `BackgroundColor` |
| **类型:** character vector | string |
| **值:** `[r g b]` vector |

### **不透明度** — 模块背景不透明度 `1`（默认）| 标量

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例:** `0.5`

### **圆角半径** — 具有模块背景色的区域外边缘与刻度标记的偏移量 标量

将模块背景色覆盖区域的外边缘与刻度标记的偏移量指定为从 `0` 到 `1` 的标量值。

**示例:** `0.1`

#### 前景图像

### **X 偏移量** — 前景图像左边缘与模块左边缘的水平偏移量 标量

将图像左边缘与模块左边缘的水平偏移量指定为模块宽度的比例。相对于偏移量为 `0` 时图像的位置，负值偏移量将图像向左移动，正值偏移量将图像向右移动。

**示例:** `1`

### **Y 偏移量** — 前景图像上边缘与模块上边缘的垂直偏移量 标量

将图像上边缘与模块上边缘的垂直偏移量指定为模块高度的比例。相对于偏移量为 `0` 时图像的位置，负值偏移量将图像向上移动，正值偏移量将图像向下移动。

**示例:** `1`

### **宽度** — 前景图像宽度 标量

将前景图像宽度指定为模块宽度的比例。

**示例:** `0.5`

### **高度** — 前景图像高度 标量

将前景图像高度指定为模块高度的比例。

**示例:** `0.5`

### **锁定纵横比** — 用于保持前景图像纵横比的选项 `on`（默认）| `off`

使用属性检查器调整图像大小时，选择此参数以保持纵横比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成时会忽略 Dashboard 模块。

## 版本历史

**在 R2020b 中引入**

### R2024b：使用键盘解锁 dashboard 模块纵横比

如果 Dashboard 库中某个模块的纵横比已锁定，你可以按 **Shift** 临时解锁纵横比。释放 **Shift** 键后，纵横比会锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。释放 **Shift** 键后，纵横比解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，现在可以将 dashboard 面板（与该面板连接的模型一起打包）部署为独立桌面应用或 Web 应用。你可以使用该应用独立于 Simulink 操作控件并监视面板上的显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，你可以将 dashboard 面板停靠到 Simulink Editor 窗口。你可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，你可以在新窗口中打开 dashboard 面板。为此，选择该面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window。

你可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，你可以运行、暂停、停止仿真并单步执行仿真。在面板窗口中，你可以编辑该面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中单击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink Toolstrip 中的持久 Panels 选项卡

将 dashboard 面板添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选中面板时 **Panels** 选项卡也保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名选中的面板。
- 可以隐藏选中的面板。

### R2022b：支持对面板中的可自定义 dashboard 模块进行撤销和重做

从 R2022b 开始，你可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y**
   重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的 Toolstrip 支持

从 R2022b 开始，你可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

单击面板中的 dashboard 模块时，该模块的工具条选项卡会出现。例如，单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在工具条中。

单击面板时，**Panel** 选项卡会出现在工具条中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适配到当前视图内。
- 折叠选中的面板。
- 自定义面板的大小和内容。
- 为选中的面板设置自定义背景图像。
- 向选中的面板添加新选项卡。

### R2022a：更改刻度方向

从 R2022a 开始，你可以更改 **Customizable Blocks** 库中以下模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：指定值条和指针的原点

刻度的原点是指针移动和值条增长的刻度值。从 R2022a 开始，你可以为 **Customizable Blocks** 库中以下模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：调整前景图像大小并重新定位

Customizable Blocks 库中的模块提供将一个前景图像作为模块设计一部分添加的选项。从 R2022a 开始，你可以在模块设计中旋转、调整大小并重新定位前景图像。

### R2021b：在 Raspberry Pi 板上部署可自定义的 Gauge 和 Knob Dashboard 模块

从 2021b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在 Raspberry Pi 硬件板上部署 Circular Gauge 模块和 Knob 模块。

你可以在 Simulink 模型中自定义模块的视觉外观，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

### R2021b：在 Android 设备上部署可自定义的 Gauge 和 Knob Dashboard 模块

从 2021b 开始，Simulink Support Package for Android® Devices 支持在 Android 设备上部署 Circular Gauge 模块和 Knob 模块。

你可以在 Simulink 模型中自定义模块的视觉外观，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化效果。

### R2021a：可自定义 dashboard 模块仪表移至 Customizable Blocks 库

在之前的版本中，Dashboard 库包含 Circular Gauge、Horizontal Gauge 和 Vertical Gauge 模块。从 R2021a 开始，这些模块位于 Dashboard 库中的 Customizable Blocks 子库中。

### R2021a：Dashboard gauge 模块支持前景色、背景色和字体颜色

从 R2021a 开始，你可以更改以下模块的前景色、背景色和字体颜色：

- Gauge
- Half Gauge
- Linear Gauge
- Quarter Gauge
- Circular Gauge
- Horizontal Gauge
- Vertical Gauge

### R2020b：对 dashboard 模块的 Simulink toolstrip 支持

从 R2020b 开始，当你从 Simulink Dashboard 库或从 Aerospace Blockset™ Flight Control Analysis Library 中的 Flight Instruments 库中选择模型中的模块时，Simulink Toolstrip 会打开特定于该模块的选项卡。在工具条中，你可以连接、断开连接和修改所选模块的连接。你还可以跳转到连接到所选模块的模型元素，并将所选模块添加到面板。

### R2020b：向 Horizontal Gauge、Vertical Gauge 和 Circular Gauge 模块添加前景图像

从 R2020b 开始，你可以向模型中的 Horizontal Gauge、Vertical Gauge 或 Circular Gauge 模块添加前景图像。

### R2020b：Circular Gauge 模块替代 Custom Gauge 模块

从 R2020b 开始，Circular Gauge 模块替代 Custom Gauge 模块。当你打开包含 Custom Gauge 模块的旧版本模型时，Custom Gauge 模块会自动替换为具有相同配置的 Circular Gauge 模块。

## 描述

在仿真期间在具有可自定义外观的圆形仪表上显示信号值

在仿真期间，Circular Gauge 模块在圆形仪表上显示所连接信号的值，你可以将该圆形仪表设计为看起来像真实系统中的仪表。你可以修改 Circular Gauge 模块上的范围和刻度值以适合你的数据。将 Circular Gauge 模块与其他 dashboard 模块一起使用，为你的模型构建包含控件和指示器的交互式 dashboard。

### 自定义 Circular Gauge 模块

将 Circular Gauge 模块添加到模型时，该模块已预配置默认设计。你可以使用默认设计的模块，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，可通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在特定于模块的选项卡上，在 **Design** 下，单击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上出现的省略号上，然后单击 Edit Custom Block 按钮。

在设计模式中，你可以使用模块上方的工具栏自定义圆形仪表。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的 Circular Gauge 模块，其中工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传指针图像。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 更改刻度的弧长。 | 否 | 是 |
| 指定值条增长所依据的原点位置。 | 否 | 是 |
| 更改刻度标记、刻度标签或值条的颜色和不透明度。 | 是 | 是 |
| 将刻度方向指定为顺时针或逆时针。 | 否 | 是 |
| 更改刻度和指针的大小。 | 否 | 是 |
| 更改刻度和指针的位置。 | 否 | 是 |

要使用工具栏更改刻度标记、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中选择要更改颜色的组件。要更改颜色，请单击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，你还可以在画布中以交互方式调整组件大小并重新定位。指针的移动限于穿过模块中心和刻度最小值的线。

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接到的信号线。在出现的列表中，选择要连接到的信号。然后，暂停在 dashboard 模块上，并单击 Done Connecting 按钮。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

你还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Circular Gauge 模块连接到模型。

未连接的 Circular Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。
