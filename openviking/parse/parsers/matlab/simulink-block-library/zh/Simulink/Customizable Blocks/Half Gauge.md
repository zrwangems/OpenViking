---
type: simulink-block
title: 'Half Gauge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Customizable Blocks'
documentation_page: 'customhalfgauge'
documentation_source_path: 'slref/customhalfgauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Half Gauge



在仿真期间以可自定义外观的半圆形状仪表显示信号值

## 库

Simulink / Dashboard / Customizable Blocks

## 描述

Half Gauge 模块在具有半圆形状的仪表上显示所连接信号的值。您可以将该模块设计为看起来像真实系统中的仪表。

Half Gauge 模块在整个仿真过程中显示所连接信号的瞬时值。您可以修改 Half Gauge 模块上的范围和刻度值以适合您的数据。将 Half Gauge 模块与其他 dashboard 模块一起使用，可为您的模型构建由控件和指示器组成的交互式 dashboard。

### 自定义 Half Gauge 模块

当您将 Half Gauge 模块添加到模型时，该模块预配置有默认设计。您可以使用默认设计使用该模块，或自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定选项卡上的 **Design** 下，点击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
- 将鼠标悬停在模块上出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式下，您可以使用模块上方的工具栏自定义 half gauge。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的 Half Gauge 模块，其中工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传指针图像。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 更改刻度的弧长。 | 否 | 是 |
| 指定值条增长所依据的原点位置。 | 否 | 是 |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | 是 | 是 |
| 将刻度方向指定为 Clockwise 或 Counterclockwise。 | 否 | 是 |
| 更改刻度和指针的大小。 | 否 | 是 |
| 更改刻度和指针的位置。 | 否 | 是 |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二节中，选择要更改颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件的大小和位置。指针的移动被限制在经过模块中心和刻度上最小值的那条线上。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择要连接的信号。然后，将鼠标悬停在 dashboard 模块上，然后点击 Done Connecting 按钮 。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Half Gauge 模块连接到您的模型。

未连接的 Half Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。

## 参数

使用属性检查器和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或属性检查器中的 **Parameters** 选项卡。要自定义模块，请使用属性检查器中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开属性检查器，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

## 参数

要设置 dashboard 模块的核心参数，请打开属性检查器，然后点击 **Parameters** 选项卡。

#### 信号

### **Connection** — 要连接的信号以及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0` (默认) | scalar

有限、实数、double、标量值，用于指定刻度上的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (默认) | scalar

有限、实数、double、标量值，用于指定刻度上的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (默认) | scalar

有限、实数、正、整数、标量值，用于指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Direction** — 刻度值递增方向 `Clockwise` (默认) | `Counterclockwise`

设置刻度值递增的方向。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Label** — 显示所连接元素名称的标签位置 `Hide` (默认) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (默认) | `off`

在 Simulink 画布中调整模块大小时，选择此参数可保持宽高比。

锁定宽高比时，添加新的背景图像会更改模块的宽高比，使其与背景图像的宽高比匹配。解锁宽高比时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

锁定宽高比时，在调整模块大小时按下 **Shift** 键会临时解锁宽高比。释放 **Shift** 键后，宽高比会锁定。解锁宽高比时，在调整模块大小时按下 **Shift** 键会临时锁定宽高比。释放 **Shift** 键后，宽高比会解锁。

### **Scale Colors** — 仪表刻度上用于刻度范围的颜色指示

刻度上值范围的颜色规范。点击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要在其中显示该颜色的范围的最小值和最大值。

#### 编程用法

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — 由 `0` 到 `1` 之间的 `double` 值组成的 `1`-by-`3` 向量，以 `[r g b]` 形式指定该范围的颜色

对于要指定颜色的每个刻度范围，请在数组中包含一个结构体。

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
| **默认值：** `0x1` struct array |

### 设计

要自定义 dashboard 模块，请打开属性检查器，点击 **Design** 选项卡，然后点击 **Edit**。

#### 圆形仪表

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (默认) | `off`

在 Simulink 画布中调整模块大小时，选择此参数可保持宽高比。

锁定宽高比时，添加新的背景图像会更改模块的宽高比，使其与背景图像的宽高比匹配。解锁宽高比时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

锁定宽高比时，在调整模块大小时按下 **Shift** 键会解锁宽高比。释放 **Shift** 键后，宽高比会锁定。解锁宽高比时，在调整模块大小时按下 **Shift** 键会锁定宽高比。释放 **Shift** 键后，宽高比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0` (默认) | scalar

有限、实数、double、标量值，用于指定刻度上的最小刻度值。该参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (默认) | scalar

有限、实数、double、标量值，用于指定刻度上的最大刻度值。该参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (默认) | scalar

有限、实数、正、整数、标量值，用于指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将该向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Origin** — 刻度上指针移动和值条增长所依据的值 `auto` (默认) | scalar

指定刻度上指针移动和值条增长所依据的值。设置为 `auto` 时，`Origin` 为刻度最小值。

**示例：** `0`

### **Direction** — 刻度值递增方向 `Clockwise` (默认) | `Counterclockwise`

设置刻度值递增的方向。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Arc** — 刻度的弧长 `180` (默认) | scalar

以标量值指定刻度的弧长，以 degrees 为单位测量。

**示例：** `90`

### **Start Angle** — 刻度最小值的角度位置 `180` (默认) | scalar

指定刻度最小值的角度位置，以从指向右侧的水平轴开始顺时针测量的 degrees 为单位。

**示例：** `0`

### **Inner Radius** — 刻度线自由端的半径 scalar

将刻度线自由端的半径指定为刻度的边界框两个维度（宽度或高度）中较小者的比值。`Inner Radius` 可以大于 `Outer Radius`。

**示例：** `0.5`

### **Outer Radius** — 跨度线半径 scalar

将跨度线半径指定为刻度的边界框两个维度（宽度或高度）中较小者的比值。`Outer Radius` 可以小于 `Inner Radius`。

**示例：** `0.5`

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

将刻度边界框左边缘相对于模块左边缘的水平偏移指定为模块宽度的比值。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向左移动，正值偏移会将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

将刻度边界框上边缘相对于模块上边缘的垂直偏移指定为模块高度的比值。相对于偏移为 `0` 时刻度的位置，负值偏移会将刻度向上移动，正值偏移会将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比值。

**示例：** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比值。

**示例：** `2`

### **Lock Aspect Ratio** — 用于保持刻度宽高比的选项 `on` (默认) | `off`

使用属性检查器调整刻度大小时，选择此参数可保持宽高比。

### **Tick Color** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink 工具条的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` 向量。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Minor Tick Height** — 刻度上次刻度线的高度 `1` (默认) | scalar

将刻度上次刻度线的高度指定为高度与外半径和内半径之差的比值。

**示例：** `0.5`

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Radius** — 刻度标签与刻度中心的距离 scalar

将刻度标签与刻度中心的距离指定为刻度半径的比值。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

将指针图像的宽度指定为刻度的边界框两个维度（宽度或长度）中较小者的比值。

**示例：** `1`

### **Height** — 指针图像高度 scalar

将指针图像的高度指定为刻度的边界框两个维度（宽度或长度）中较小者的比值。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on` (默认) | `off`

使用属性检查器调整图像大小时，选择此参数可保持宽高比。

### **Rotate Image** — 指针图像的旋转 `180` (默认) | scalar

围绕其中心以 90 度增量旋转指针图像。

**示例：** `90`

### **Offset from Center** — 指针图像中心与刻度中心的偏移 `0` (默认) | scalar

将指针图像中心到刻度中心的距离指定为刻度直径的比值。

**示例：** `1`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off` (默认) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请打开 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用工具条更改背景颜色会移除背景图像并启用 **Use Background Color** 选项。

当您将纯色背景与 Half Gauge 模块一起使用时，可以设计覆盖角度范围不同于 half gauge 默认 180° 的仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Half Gauge 模块

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

要选择纯色背景颜色，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**注意**

当您将纯色背景与 Half Gauge 模块一起使用时，可以设计覆盖角度范围不同于 half gauge 默认 180° 的仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Half Gauge 模块

#### 编程用法

将模块的 `BackgroundColor` 参数指定为一个值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` 向量，格式为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (默认) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **Corner radius** — 具有模块背景颜色的区域外边缘与刻度线的偏移 scalar

将模块背景颜色覆盖区域的外边缘与刻度线的偏移指定为从 `0` 到 `1` 的标量值。

**示例：** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比值。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比值。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比值。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比值。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on` (默认) | `off`

使用属性检查器调整图像大小时，选择此参数可保持宽高比。

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

**在 R2024a 中引入**

### R2024b: 使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键后，宽高比会锁定。

如果宽高比已解锁，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键后，宽高比会解锁。

### R2024a: 将 dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 dashboard 面板与其所连接的模型一起打包，部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a: 停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

## 端口

R2025b 官方文档未提供。
