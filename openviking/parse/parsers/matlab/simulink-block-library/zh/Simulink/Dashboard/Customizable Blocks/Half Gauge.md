---
type: simulink-block
title: 'Half Gauge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customhalfgauge'
documentation_source_path: 'slref/customhalfgauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Half Gauge

## 端口

R2025b 中未记录。

## 参数

使用属性检查器和模块参数对话框指定模块参数的值。要设置仪表板模块的核心参数，请使用模块参数对话框或属性检查器中的 **参数** 选项卡。要自定义模块，请使用属性检查器中的 **设计** 选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在 **建模** 选项卡上的 **设计** 下，选择 **属性检查器**。

### 参数

要设置仪表板模块的核心参数，请打开属性检查器并单击 **参数** 选项卡。

#### 信号

### **Connection** — 要连接的信号及显示信号连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或模块参数对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **参数** 选项卡上，单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要连接到的信号线。
4. 在该表中，选择要连接到的信号。
5. 单击 **Apply**。

您还可以将仪表板模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认：** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0`（默认）| scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认）| scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认）| scalar

有限、实数、正、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Direction** — 递增刻度值的方向 `Clockwise`（默认）| `Counterclockwise`

设置递增刻度值的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签的位置 `Hide`（默认）| `Bottom` | `Top`

您可以显示仪表板模块所连接元素的名称，标签位于模块顶部或底部，也可以隐藏标签。如果要使标签可见，请指定标签的位置。如果不想使标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认：** `'Hide'` |

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比解锁时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### **Scale Colors** — 用于刻度范围的仪表刻度颜色的颜色指示

刻度上值范围的颜色规范。单击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要显示该颜色的范围的最小值和最大值。

#### 程序化使用

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — `1`-by-`3` 的 `double` 值 vector，值介于 `0` 和 `1` 之间，以 `[r g b]` 形式指定范围的颜色

对于要指定颜色的每个刻度范围，在数组中包含一个结构体。

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

要自定义仪表板模块，请打开属性检查器，单击 **设计** 选项卡，然后单击 **编辑**。

#### 圆形仪表

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0`（默认）| scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认）| scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认）| scalar

有限、实数、正、整数、scalar 值，指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` vector，其中包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值，按该顺序。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认：** `[0 -1 100]` |

### **Origin** — 刻度上指针移动和值条增长所依据的值 `auto`（默认）| scalar

指定刻度上指针移动和值条增长所依据的值。当设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **Direction** — 递增刻度值的方向 `Clockwise`（默认）| `Counterclockwise`

设置递增刻度值的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认：** `'Clockwise'` |

### **Arc** — 刻度的弧长 `180`（默认）| scalar

指定刻度的弧长，以 degrees 为单位，作为 scalar 值。

**示例：** `90`

### **Start Angle** — 刻度最小值的角度位置 `180`（默认）| scalar

指定最小刻度值的角度位置，以 degrees 为单位，从指向右侧的水平轴顺时针测量。

**示例：** `0`

### **Inner Radius** — 刻度线自由端的半径 scalar

指定刻度线自由端的半径，作为刻度的边界框的两个维度（宽度或高度）中较小者的比率。`Inner Radius` 可以大于 `Outer Radius`。

**示例：** `0.5`

### **Outer Radius** — 跨度线半径 scalar

指定跨度线半径，作为刻度的边界框的两个维度（宽度或高度）中较小者的比率。`Outer Radius` 可以小于 `Inner Radius`。

**示例：** `0.5`

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

指定刻度边界框左边缘相对于模块左边缘的水平偏移，作为模块宽度的比率。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

指定刻度边界框上边缘相对于模块上边缘的垂直偏移，作为模块高度的比率。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

指定刻度边界框的宽度，作为模块宽度的比率。

**示例：** `2`

### **Height** — 刻度高度 scalar

指定刻度边界框的高度，作为模块高度的比率。

**示例：** `2`

### **Lock Aspect Ratio** — 保持刻度宽高比的选项 `on`（默认）| `off`

选择此参数可在使用属性检查器调整刻度大小时保持宽高比。

### **Tick Color** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择一种颜色，或指定自定义颜色。

**提示**

您还可以通过在 Simulink 工具条的 **格式** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 程序化使用

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，该 vector 定义 `1`-by-`3` `[r g b]` vector，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Minor Tick Height** — 刻度上次刻度线的高度 `1`（默认）| scalar

指定刻度上次刻度线的高度，作为高度与外部半径和内部半径之差的比率。

**示例：** `0.5`

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择刻度标签的字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Radius** — 刻度标签与刻度中心的距离 scalar

指定刻度标签与刻度中心的距离，作为刻度半径的比率。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

指定指针图像的宽度，作为刻度的边界框的两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **Height** — 指针图像高度 scalar

指定指针图像的高度，作为刻度的边界框的两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **Lock Aspect Ratio** — 保持图像宽高比的选项 `on`（默认）| `off`

选择此参数可在使用属性检查器调整图像大小时保持宽高比。

### **Rotate Image** — 指针图像的旋转 `180`（默认）| scalar

以 90 degree 为增量围绕其中心旋转指针图像。

**示例：** `90`

### **Offset from Center** — 指针图像中心与刻度中心的偏移 `0`（默认）| scalar

指定从指针图像中心到刻度中心的距离，作为刻度直径的比率。

**示例：** `1`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认）| `on`

对于模块背景，可以提供背景图像或选择纯色。要选择纯色背景颜色，请开启 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用工具条更改背景颜色会移除背景图像并启用 **Use Background Color** 选项。

当对 Half Gauge 模块使用纯色背景时，可以设计角度跨度不同于 Half Gauge 默认 180° 的仪表。当刻度弧角度为 180° 或更小时，背景形状会与刻度一致。

带有非圆形橙色背景区域的 Half Gauge 模块

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当对 Half Gauge 模块使用纯色背景时，可以设计角度跨度不同于 Half Gauge 默认 180° 的仪表。当刻度弧角度为 180° 或更小时，背景形状会与刻度一致。

带有非圆形橙色背景区域的 Half Gauge 模块

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` 向量 |

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **Corner radius** — 模块背景颜色所覆盖区域的外边缘距刻度线的偏移量，标量

将模块背景颜色所覆盖区域的外边缘距刻度线的偏移量指定为从 `0` 到 `1` 的标量值。

**示例：** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移量，标量

将图像左边缘距模块左边缘的水平偏移量指定为模块宽度的比例。相对于偏移量为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移量，标量

将图像上边缘距模块上边缘的垂直偏移量指定为模块高度的比例。相对于偏移量为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度，标量

将前景图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度，标量

将前景图像高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认）| `off`

使用 Property Inspector 调整图像大小时，选择此参数以保持宽高比。

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

代码生成会忽略 Dashboard 模块。

## 版本历史

**在 R2024a 中引入**

### R2024b：使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键后，宽高比会锁定。

如果宽高比未锁定，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键后，宽高比会解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，现在可以将 dashboard 面板（与面板所连接的模型一起打包）部署为独立桌面应用或 Web 应用。可以使用该应用独立于 Simulink 操作控件并监视面板上的显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，可以将 dashboard 面板停靠到 Simulink Editor 窗口。可以使用停靠的面板在仿真期间监视信号并控制参数，而不会覆盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

## 描述

在仿真期间在形状为半圆且外观可自定义的仪表上显示信号值

Half Gauge 模块在具有半圆形状的仪表上显示所连接信号的值。可以将该模块设计为看起来像实际系统中的仪表。

Half Gauge 模块在整个仿真过程中显示所连接信号的瞬时值。可以修改 Half Gauge 模块上的范围和刻度值以适合数据。将 Half Gauge 模块与其他 dashboard 模块一起使用，为模型构建由控件和指示器组成的交互式 dashboard。

### 自定义 Half Gauge 模块

将 Half Gauge 模块添加到模型时，该模块预配置为默认设计。可以使用默认设计的该模块，或自定义模块外观。

要自定义模块外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在该模块特定的选项卡上的 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 将鼠标悬停在该模块上出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式下，可以使用模块上方的工具栏自定义 Half Gauge。要访问其他自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式下的 Half Gauge 模块，工具栏和 Property Inspector 中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 可在工具栏中使用 | 可在 **Design** 选项卡中使用 |
| --- | --- | --- |
| 上传指针图像。 | Yes | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景颜色。 | No | Yes |
| 上传前景图像。 | No | Yes |
| 更改刻度的弧长。 | No | Yes |
| 指定值条延伸起始点的位置。 | No | Yes |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | Yes | Yes |
| 将刻度方向指定为顺时针或逆时针。 | No | Yes |
| 更改刻度和指针的大小。 | No | Yes |
| 更改刻度和指针的位置。 | No | Yes |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中选择要更改颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计之外，还可以在画布中以交互方式调整组件大小和重新定位组件。指针的移动限于穿过模块中心和刻度上最小值的线。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，将鼠标悬停在 dashboard 模块上，点击 Done Connecting 按钮 。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Half Gauge 模块连接到模型。

未连接的 Half Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。
