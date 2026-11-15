---
type: simulink-block
title: 'Quarter Gauge'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customquartergauge'
language: zh-CN
chinese_source: worker-translation
---

# Quarter Gauge



在仿真期间在形状为四分之一圆、外观可自定义的仪表上显示信号值

## 库

Simulink / Dashboard / Customizable Blocks

## 描述

Quarter Gauge 模块在四分之一圆形状的仪表上显示所连接信号的值。您可以将该模块设计为看起来像真实系统中的仪表。

Quarter Gauge 模块在整个仿真过程中显示所连接信号的瞬时值。您可以修改 Quarter Gauge 模块上的范围和刻度值以适合您的数据。将 Quarter Gauge 模块与其他 Dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式 Dashboard。

### 自定义 Quarter Gauge 模块

当您将 Quarter Gauge 模块添加到模型时，该模块预配置有默认设计。您可以将该模块与默认设计一起使用，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在该模块特定的选项卡上，在 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义 Quarter Gauge。要访问其他自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的 Quarter Gauge 模块，其中可见工具栏和 Property Inspector 中的 Design 选项卡。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传指针图像。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 更改刻度的弧长。 | 否 | 是 |
| 指定值条增长所依据的原点的位置。 | 否 | 是 |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | 是 | 是 |
| 将刻度方向指定为 Clockwise 或 Counterclockwise。 | 否 | 是 |
| 更改刻度和指针的大小。 | 否 | 是 |
| 更改刻度和指针的位置。 | 否 | 是 |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中，选择要更改颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和重新定位组件。指针的移动限制在穿过模块中心和刻度最小值的线上。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，暂停在 Dashboard 模块上，并点击 Done Connecting 按钮 。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

您还可以将 Dashboard 模块连接到 Stateflow® chart。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

此动画展示如何将 Quarter Gauge 模块连接到您的模型。

未连接的 Quarter Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 Dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

## 参数

要设置 Dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### 信号

### **Connection** — 要连接的信号以及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用 Toolstrip 连接的信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 中的 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 Dashboard 模块连接到 Stateflow chart。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

#### 程序化用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0`（默认）| scalar

用于指定刻度最小刻度值的有限、实数、double、scalar 值。参数值必须小于 **Maximum** 参数的值。

#### 程序化用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认）| scalar

用于指定刻度最大刻度值的有限、实数、double、scalar 值。参数值必须大于 **Minimum** 参数的值。

#### 程序化用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认）| scalar

用于指定刻度上主刻度线间隔的有限、实数、正数、整数、scalar 值。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Direction** — 增大刻度值的方向 `Clockwise`（默认）| `Counterclockwise`

设置增大刻度值的方向。

#### 程序化用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签的位置 `Hide`（默认）| `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 Dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 Dashboard 模块未连接到元素时，标签为空白。

#### 程序化用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按下 **Shift** 键会暂时解锁纵横比。松开 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按下 **Shift** 键会暂时锁定纵横比。松开 **Shift** 键时，纵横比解锁。

### **Scale Colors** — 仪表刻度上针对刻度范围的颜色指示

刻度上值范围的颜色规格。点击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定您希望显示该颜色的范围的最小值和最大值。

#### 程序化用法

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的 structure array：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — `1`-by-`3` vector of `double` values between `0` and `1`，用于以 `[r g b]` 形式指定该范围的颜色

对于要指定颜色的每个刻度范围，在 array 中包含一个 structure。

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
| **默认值：** `0x1` struct array |

### 设计

要自定义 Dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### 圆形仪表

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按下 **Shift** 键会解锁纵横比。松开 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按下 **Shift** 键会锁定纵横比。松开 **Shift** 键时，纵横比解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0`（默认）| scalar

用于指定刻度最小刻度值的有限、实数、double、scalar 值。参数值必须小于 **Maximum** 参数的值。

#### 程序化用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认）| scalar

用于指定刻度最大刻度值的有限、实数、double、scalar 值。参数值必须大于 **Minimum** 参数的值。

#### 程序化用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认）| scalar

用于指定刻度上主刻度线间隔的有限、实数、正数、整数、scalar 值。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` vector，其中按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Origin** — 刻度上指针开始移动且值条开始增长所依据的值 `auto`（默认）| scalar

指定刻度上指针开始移动且值条开始增长所依据的值。当设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **Direction** — 增大刻度值的方向 `Clockwise`（默认）| `Counterclockwise`

设置增大刻度值的方向。

#### 程序化用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Arc** — 刻度的弧长 `90`（默认）| scalar

以 degrees 为单位，将刻度的弧长指定为 scalar 值。

**示例：** `90`

### **Start Angle** — 刻度最小值的角度位置 `180`（默认）| scalar

指定刻度最小值的角度位置，以 degrees 为单位，从指向右侧的水平轴起沿顺时针方向测量。

**示例：** `0`

### **Inner Radius** — 刻度线自由端的半径 scalar

将刻度线自由端的半径指定为刻度边界框两个维度（宽度或高度）中较小者的比率。`Inner Radius` 可以大于 `Outer Radius`。

**示例：** `0.5`

### **Outer Radius** — 跨度线半径 scalar

将跨度线半径指定为刻度边界框两个维度（宽度或高度）中较小者的比率。`Outer Radius` 可以小于 `Inner Radius`。

**示例：** `0.5`

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

将刻度边界框左边缘相对于模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

将刻度边界框上边缘相对于模块上边缘的垂直偏移指定为模块高度的比率。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比率。

**示例：** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比率。

**示例：** `2`

### **Lock Aspect Ratio** — 用于保持刻度纵横比的选项 `on`（默认）| `off`

选择此参数可在使用 Property Inspector 调整刻度大小时保持纵横比。

### **Tick Color** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 程序化用法

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，该 string 或 character vector 定义值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` vector。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Minor Tick Height** — 刻度上次刻度线的高度 `1`（默认）| scalar

将刻度上次刻度线的高度指定为高度与内外半径之差的比率。

**示例：** `0.5`

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Radius** — 刻度标签与刻度中心的距离 scalar

将刻度标签与刻度中心的距离指定为刻度半径的比率。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

将指针图像的宽度指定为刻度边界框两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **Height** — 指针图像高度 scalar

将指针图像的高度指定为刻度边界框两个维度（宽度或长度）中较小者的比率。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像纵横比的选项 `on`（默认）| `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### **Rotate Image** — 指针图像的旋转 `180`（默认）| scalar

以 90 degree 为增量绕其中心旋转指针图像。

**示例：** `90`

### **Offset from Center** — 指针图像中心相对于刻度中心的偏移 `0`（默认）| scalar

将指针图像中心到刻度中心的距离指定为刻度直径的比率。

**示例：** `1`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认）| `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请打开 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用 Toolstrip 更改背景颜色会移除背景图像并启用 **Use Background Color** 选项。

当您将纯色背景与 Quarter Gauge 模块一起使用时，可以设计角度跨度不同于四分之一仪表默认 90° 的仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Quarter Gauge 模块

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

要选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当您将纯色背景与 Quarter Gauge 模块一起使用时，可以设计角度跨度不同于四分之一仪表默认 90° 的仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Quarter Gauge 模块

#### 程序化用法

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` vector，其值介于 `0` 和 `1` 之间，并且格式为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1`（默认）| scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

### **Corner radius** — 具有模块背景颜色的区域外边缘相对于刻度线的偏移 scalar

将模块背景颜色所覆盖区域的外边缘相对于刻度线的偏移指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比率。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比率。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比率。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像纵横比的选项 `on`（默认）| `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

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

代码生成时会忽略 Dashboard 模块。

## 版本历史

**在 R2024a 中引入**

### R2024b：使用键盘解锁 dashboard 模块纵横比

如果 Dashboard 库中某个模块的纵横比已锁定，您可以通过按 **Shift** 暂时解锁纵横比。松开 **Shift** 键时，纵横比锁定。

如果纵横比未锁定，按 **Shift** 会暂时锁定纵横比。松开 **Shift** 键时，纵横比解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板与其所连接的模型一起打包，并部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视面板上的显示。

要了解如何部署面板，请参阅将 Dashboard 面板部署为 App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会在画布中覆盖模型图。

有关详细信息，请参阅停靠面板。
