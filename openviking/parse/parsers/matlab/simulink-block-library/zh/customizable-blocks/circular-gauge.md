---
type: simulink-block
title: 'Circular Gauge'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'circulargauge'
language: zh-CN
chinese_source: worker-translation
---

# Circular Gauge



在可自定义外观的圆形仪表上显示仿真期间的信号值

## 库

Simulink / Dashboard / Customizable Blocks

## 描述

在仿真期间，Circular Gauge 模块会在圆形仪表上显示所连接信号的值，您可以将其设计为类似真实系统中的仪表。您可以修改 Circular Gauge 模块上的范围和刻度值以适合您的数据。将 Circular Gauge 模块与其他仪表板模块一起使用，为您的模型构建交互式仪表板，其中包含控件和指示器。

### 自定义 Circular Gauge 模块

将 Circular Gauge 模块添加到模型时，该模块会预配置为默认设计。您可以使用该模块的默认设计，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在特定于模块的选项卡上，在 **Design** 下，单击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上方出现的省略号上，然后单击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义圆形仪表。要访问其他自定义选项或输入设计设置的精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的 Circular Gauge 模块，工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传 needle 图像。 | Yes | Yes |
| 上传背景图像。 | Yes | Yes |
| 设置纯色背景色。 | No | Yes |
| 上传前景图像。 | No | Yes |
| 更改刻度的弧长。 | No | Yes |
| 指定值条增长所依据的原点位置。 | No | Yes |
| 更改刻度标记、刻度标签或值条的颜色和不透明度。 | Yes | Yes |
| 将刻度方向指定为顺时针或逆时针。 | No | Yes |
| 更改刻度和指针的大小。 | No | Yes |
| 更改刻度和指针的位置。 | No | Yes |

要使用工具栏更改刻度标记、刻度标签或值条的颜色和不透明度，请在工具栏从左数第二部分中，选择要更改其颜色的组件。要更改颜色，请单击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小并重新定位组件。指针的移动被限制在穿过模块中心和刻度最小值的线上。

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，暂停在仪表板模块上，并单击 Done Connecting 按钮 。要查看仪表板模块显示所连接模块的值，请运行仿真。

有关连接仪表板模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Circular Gauge 模块连接到您的模型。

未连接的 Circular Gauge 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。

## 参数

使用属性检查器和 Block Parameters 对话框指定模块参数的值。要设置仪表板模块的核心参数，请使用 Block Parameters 对话框或属性检查器中的 **Parameters** 选项卡。要自定义模块，请使用属性检查器中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开属性检查器，请在 **Modeling** 选项卡上，在 **Design** 下，选择 **Property Inspector**。

## 参数

要设置仪表板模块的核心参数，请打开属性检查器并单击 **Parameters** 选项卡。

#### 信号

### **Connection** — 要连接的信号并显示信号连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用 toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器中，在 **Parameters** 选项卡上，单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 单击 **Apply**。

您还可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

#### 主要

### **Minimum** — 最小刻度标记值 `0` (default) | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度标记值。该参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度标记值 `100` (default) | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度标记值。该参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度标记之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度标记的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Direction** — 递增刻度值的方向 `Clockwise` (default) | `Counterclockwise`

设置递增刻度值的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Label** — 显示已连接元素名称的标签位置 `Hide` (default) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示仪表板模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比，以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### **Scale Colors** — 用于刻度范围的仪表刻度颜色的颜色指示

刻度上值范围的颜色规范。单击 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要显示该颜色的范围的最小值和最大值。

#### 程序化使用

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — `1`-by-`3` 向量，包含介于 `0` 和 `1` 之间的 `double` 值，以 `[r g b]` 形式指定该范围的颜色

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
| **默认值：** `0x1` struct array |

### Design

要自定义仪表板模块，请打开属性检查器，单击 **Design** 选项卡，然后单击 **Edit**。

#### Circular Gauge

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (default) | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会更改模块的宽高比，以匹配背景图像的宽高比。当宽高比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比会锁定。当宽高比解锁时，在调整模块大小时按 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

#### 刻度

### **Minimum** — 最小刻度标记值 `0` (default) | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度标记值。该参数值必须小于 **Maximum** 参数的值。

#### 程序化使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Maximum** — 最大刻度标记值 `100` (default) | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度标记值。该参数值必须大于 **Minimum** 参数的值。

#### 程序化使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Tick Interval** — 主刻度标记之间的间隔 `auto` (default) | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度标记的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 程序化使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`-by-`3` 向量，其中按该顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设置为 `auto` 值，请将向量中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` vector |
| **默认值：** `[0 -1 100]` |

### **Origin** — 刻度上指针移动和值条增长所依据的值 `auto` (default) | scalar

指定刻度上指针移动和值条增长所依据的值。当设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例：** `0`

### **Direction** — 递增刻度值的方向 `Clockwise` (default) | `Counterclockwise`

设置递增刻度值的方向。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** character vector |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### **Arc** — 刻度的弧长 `270` (default) | scalar

以 scalar 值指定刻度的弧长，以 degrees 为单位。

**示例：** `90`

### **Start Angle** — 刻度最小值的角度位置 `135` (default) | scalar

指定最小刻度值的角度位置，以 degrees 为单位，从指向右侧的水平轴开始顺时针测量。

**示例：** `0`

### **Inner Radius** — 刻度标记自由端的半径 scalar

将刻度标记自由端的半径指定为刻度边界框两个尺寸（宽度或高度）中较小者的比例。`Inner Radius` 可以大于 `Outer Radius`。

**示例：** `0.5`

### **Outer Radius** — 跨度线半径 scalar

将跨度线半径指定为刻度边界框两个尺寸（宽度或高度）中较小者的比例。`Outer Radius` 可以小于 `Inner Radius`。

**示例：** `0.5`

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

将刻度边界框左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移将刻度向左移动，正值偏移将刻度向右移动。

**示例：** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

将刻度边界框上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移将刻度向上移动，正值偏移将刻度向下移动。

**示例：** `1`

### **Width** — 刻度宽度 scalar

将刻度边界框的宽度指定为模块宽度的比例。

**示例：** `2`

### **Height** — 刻度高度 scalar

将刻度边界框的高度指定为模块高度的比例。

**示例：** `2`

### **Lock Aspect Ratio** — 用于保持刻度宽高比的选项 `on` (default) | `off`

选择此参数以在使用属性检查器调整刻度大小时保持宽高比。

### **Tick Color** — 刻度标记、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度标记、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 程序化使用

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，用于定义值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` 向量。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Minor Tick Height** — 刻度上次要刻度标记的高度 `1` (default) | scalar

将刻度上次要刻度标记的高度指定为高度与外半径和内半径之差的比值。

**示例：** `0.5`

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中为刻度标签选择字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Radius** — 刻度标签距刻度中心的距离 scalar

将刻度标签距刻度中心的距离指定为刻度半径的比例。

**示例：** `0.5`

#### 指针

### **Width** — 指针图像宽度 scalar

将指针图像的宽度指定为刻度边界框两个尺寸（宽度或长度）中较小者的比例。

**示例：** `1`

### **Height** — 指针图像高度 scalar

将指针图像的高度指定为刻度边界框两个尺寸（宽度或长度）中较小者的比例。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on` (default) | `off`

选择此参数以在使用属性检查器调整图像大小时保持宽高比。

### **Rotate Image** — 指针图像的旋转 `180` (default) | scalar

以 90 degree 为增量绕其中心旋转指针图像。

**示例：** `90`

### **Offset from Center** — 指针图像中心相对于刻度中心的偏移 `0` (default) | scalar

将指针图像中心到刻度中心的距离指定为刻度直径的比例。

**示例：** `1`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景，请打开 **Use Background Color**。要提供背景图像，请关闭 **Use Background Color**。

**注意**

使用 toolstrip 更改背景色会移除背景图像并启用 **Use Background Color** 选项。

当您将纯色背景与 Circular Gauge 模块一起使用时，可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Circular Gauge 模块

**示例：** `on`

### **Color** — 模块背景色 `[r g b]` vector

要选择纯色背景，请启用 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**注意**

当您将纯色背景与 Circular Gauge 模块一起使用时，可以设计非圆形仪表。当刻度弧角为 180° 或更小时，背景形状会与刻度一致。

具有非圆形橙色背景区域的 Circular Gauge 模块

#### 程序化使用

将模块的 `BackgroundColor` 参数指定为值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` 向量，其格式为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

### **Corner radius** — 具有模块背景色的区域外边缘相对于刻度标记的偏移 scalar

将模块背景色覆盖区域的外边缘相对于刻度标记的偏移指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on` (default) | `off`

选择此参数以在使用属性检查器调整图像大小时保持宽高比。

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

代码生成会忽略仪表板模块。

## 版本历史

**在 R2020b 中引入**

### R2024b：使用键盘解锁仪表板模块宽高比

如果 Dashboard 库中某个模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。释放 **Shift** 键时，宽高比会锁定。

如果宽高比已解锁，按 **Shift** 会临时锁定宽高比。释放 **Shift** 键时，宽高比会解锁。

### R2024a：将仪表板面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将仪表板面板与其所连接的模型一起打包，并部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视显示器。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠仪表板面板

从 R2024a 开始，您可以将仪表板面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会在画布中遮盖模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，单击 Open In New Window 。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中单击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink Toolstrip 中的持久 Panels 选项卡

将仪表板面板添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选中任何面板时，**Panels** 选项卡会保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名选定的面板。
- 您可以隐藏选定的面板。

### R2022b：在面板中支持对可自定义仪表板模块进行撤销和重做

从 R2022b 开始，您可以撤销和重做对面板中可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 单击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的仪表板模块。

当您单击面板中的仪表板模块时，会出现该模块的 toolstrip 选项卡。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在 toolstrip 中。

当您单击面板时，**Panel** 选项卡会出现在 toolstrip 中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠选定的面板。
- 自定义面板的大小和内容。
- 为选定的面板设置自定义背景图像。
- 向选定的面板添加新选项卡。

### R2022a：更改刻度方向

从 R2022a 开始，您可以更改以下 **Customizable Blocks** 库中模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：为值条和指针指定原点

刻度的原点是刻度上指针移动和值条增长所依据的值。从 R2022a 开始，您可以为以下 **Customizable Blocks** 库中模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：调整前景图像大小并重新定位

Customizable Blocks 库中的模块具有添加前景图像作为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整大小并重新定位前景图像。

### R2021b：在 Raspberry Pi 板上部署可自定义的 Gauge 和 Knob Dashboard 模块

从 2021b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持将 Circular Gauge 模块和 Knob 模块部署到您的 Raspberry Pi 硬件板上。

您可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2021b：在 Android 设备上部署可自定义的 Gauge 和 Knob Dashboard 模块

从 2021b 开始，Simulink Support Package for Android® Devices 支持将 Circular Gauge 模块和 Knob 模块部署到您的 Android 设备。

您可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2021a：可自定义仪表板模块仪表移至 Customizable Blocks 库

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

### R2020b：对仪表板模块的 Simulink toolstrip 支持

从 R2020b 开始，当您在模型中从 Simulink Dashboard 库或 Aerospace Blockset™ Flight Control Analysis Library 中的 Flight Instruments 库选择模块时，Simulink Toolstrip 会打开特定于模块的选项卡。通过 toolstrip，您可以连接、断开连接和修改所选模块的连接。您还可以跳转到连接到所选模块的模型元素，并将所选模块添加到面板。

### R2020b：向 Horizontal Gauge、Vertical Gauge 和 Circular Gauge 模块添加前景图像

从 R2020b 开始，您可以向模型中的 Horizontal Gauge、Vertical Gauge 或 Circular Gauge 模块添加前景图像。

### R2020b：Circular Gauge 模块替换 Custom Gauge 模块

从 R2020b 开始，Circular Gauge 模块替换 Custom Gauge 模块。当您打开包含 Custom Gauge 模块的以前版本模型时，Custom Gauge 模块会自动替换为具有相同配置的 Circular Gauge 模块。
