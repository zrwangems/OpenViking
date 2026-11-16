---
type: simulink-block
title: 'Horizontal Slider'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'horizontalslider'
documentation_source_path: 'slref/horizontalslider.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Slider

## 端口

R2025b 中未记录。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要为仪表板模块设置核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

### 参数

要为仪表板模块设置核心参数，请打开 Property Inspector 并点击 **Parameters** 选项卡。

#### 连接

### **Connection** — 要连接的模块参数值 连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧，点击 **Connect** 或 **Change**。您可以连接到具有 scalar 值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参见 Connect Dashboard Blocks to Simulink Model。

要将控制模块连接到具有 scalar 值的参数，或使用 **Connection** 表更改控制模块到具有 scalar 值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的
   **Parameters** 选项卡上，点击 **Connect**。
   要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您也可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参见 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将仪表板模块连接到由值定义的参数，有些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定仪表板模块连接到由值定义的参数或由变量定义的参数之一。

|  |
| --- |
| **模块参数:** `Binding` |
| **类型:** `Simulink.HMI.ParamSourceInfo` |
| **默认:** `[]` |

#### 主要

### **Minimum** — 最小刻度值 `0` (默认) | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (默认) | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (默认) | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Scale Direction** — 刻度值增加的方向 `'Left to right'` (默认) | `'Right to left'`

设置刻度值增加的方向。

#### 编程用法

|  |
| --- |
| **模块参数:** `ScaleDirection` |
| **类型:** character vector |
| **值:** `'Clockwise'` | `'Counterclockwise'` |
| **默认:** `'Clockwise'` |

### **Label** — 显示已连接元素名称的标签位置 `Hide` (默认) | `Bottom` | `Top`

您可以将仪表板模块连接到的元素名称显示在位于模块顶部或底部的标签中，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数:** `LabelPosition` |
| **类型:** character vector |
| **值:** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认:** `'Hide'` |

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按下 **Shift** 键会暂时解锁纵横比。释放 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按下 **Shift** 键会暂时锁定纵横比。释放 **Shift** 键时，纵横比会解锁。

### 设计

要自定义仪表板模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### 滑块

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按下 **Shift** 键会解锁纵横比。释放 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，在调整模块大小时按下 **Shift** 键会锁定纵横比。释放 **Shift** 键时，纵横比会解锁。

#### 刻度

### **Minimum** — 最小刻度值 `0` (默认) | scalar

有限、实数、double、scalar 值，指定刻度的最小刻度值。参数值必须小于 **Maximum** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Maximum** — 最大刻度值 `100` (默认) | scalar

有限、实数、double、scalar 值，指定刻度的最大刻度值。参数值必须大于 **Minimum** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto` (默认) | scalar

有限、实数、正数、整数、scalar 值，指定刻度上主刻度线的间隔。设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用 `1`-by-`3` vector，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要对 `Tick Interval` 使用 `auto` 值，请将 vector 中的 `Tick Interval` 位置留空，或指定 `-1`。

|  |
| --- |
| **模块参数:** `Limits` |
| **类型:** `1x3` vector |
| **默认:** `[0 -1 100]` |

### **Origin** — 刻度上的值，手柄从该值移动且值条从该值增长 `auto` (默认) | scalar

指定刻度上的值，手柄从该值移动且值条从该值增长。设置为 `auto` 时，`Origin` 为刻度的最小值。

**示例:** `0`

### **Scale Direction** — 刻度值增加的方向 `'Left to right'` (默认) | `'Right to left'`

设置刻度值增加的方向。

#### 编程用法

|  |
| --- |
| **模块参数:** `ScaleDirection` |
| **类型:** character vector |
| **值:** `'Clockwise'` | `'Counterclockwise'` |
| **默认:** `'Clockwise'` |

### **X Offset** — 刻度边界框左边缘相对于模块左边缘的水平偏移 scalar

指定刻度边界框左边缘相对于模块左边缘的水平偏移，作为模块宽度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移将刻度向左移动，正值偏移将刻度向右移动。

**示例:** `1`

### **Y Offset** — 刻度边界框上边缘相对于模块上边缘的垂直偏移 scalar

指定刻度边界框上边缘相对于模块上边缘的垂直偏移，作为模块高度的比例。相对于偏移为 `0` 时刻度的位置，负值偏移将刻度向上移动，正值偏移将刻度向下移动。

**示例:** `1`

### **Width** — 刻度宽度 scalar

指定刻度边界框的宽度，作为模块宽度的比例。

**示例:** `2`

### **Height** — 刻度高度 scalar

指定刻度边界框的高度，作为模块高度的比例。

**示例:** `2`

### **Lock Aspect Ratio** — 保持刻度纵横比的选项 `on` (默认) | `off`

选择此参数可在使用 Property Inspector 调整刻度大小时保持纵横比。

### **Tick Color** — 刻度线、跨度线和模块名称的颜色 `[r g b]` vector

设置刻度线、跨度线和模块名称的颜色。从标准颜色调色板中选择颜色，或指定自定义颜色。

**提示**

您还可以通过在 Simulink Toolstrip 的 **Format** 选项卡上选择 **Foreground Color** 来设置 **Tick Color**。

要指定模块文本的颜色，请使用 **Label Color** 参数。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，该 string 或 character vector 定义值介于 `0` 和 `1` 之间的 `1`-by-`3` `[r g b]` vector。

|  |
| --- |
| **模块参数:** `ForegroundColor` |
| **类型:** character vector | string |
| **值:** `[r g b]` vector |

### **Label Color** — 刻度标签字体颜色 `[r g b]` vector

从标准颜色调色板中选择刻度标签的字体颜色，或指定自定义颜色。

**提示**

要指定刻度的颜色，请使用 **Tick Color** 参数。

### **Label Offset** — 刻度标签与刻度线自由端之间的垂直距离 `0.3` (默认) | scalar

指定从刻度标签到刻度上其对应刻度线自由端的垂直距离，作为刻度边界框高度的比例。

**示例:** `0.5`

#### 手柄

### **Width** — 手柄图像宽度 scalar

指定手柄图像的宽度，作为模块宽度的比例。

**示例:** `1`

### **Height** — 手柄图像高度 scalar

指定手柄图像的高度，作为模块高度的比例。

**示例:** `1`

### **Lock Aspect Ratio** — 保持图像纵横比的选项 `on` (默认) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### **X Offset** — 手柄图像中心相对于刻度原点的水平偏移 scalar

指定手柄图像中心相对于刻度原点的水平偏移，作为手柄图像宽度的比例。相对于偏移为 `0` 时手柄图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例:** `1`

### **Y Offset** — 手柄图像上边缘相对于刻度跨度线的垂直偏移 scalar

指定手柄图像上边缘相对于刻度跨度线的垂直偏移，作为手柄图像高度的比例。相对于偏移为 `0` 时手柄图像的位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例:** `1`

#### 值条

### **Offset from Scale** — 值条上边缘与跨度线之间的距离 `0` (默认) | scalar

指定从值条上边缘到跨度线的距离，作为刻度边界框高度的比例。相对于偏移为 `0` 时值条的位置，负值偏移将值条向上移动，正值偏移将值条向下移动。

**示例:** `0.25`

### **Size** — 值条厚度 scalar

指定值条的厚度，作为刻度边界框高度的比例。

**示例:** `0.3`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景色的选项 `off` (默认) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景色会移除背景图像，并启用 **Use Background Color** 参数。

**示例:** `on`

### **颜色** — 模块背景色 `[r g b]` 向量

要使用纯色背景，请选择 **使用背景色** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**提示**

您也可以在 Simulink 工具条的 **格式** 选项卡中指定 **背景色**。

要指定模块文本的颜色，请使用 **字体颜色** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` 向量 |

### **不透明度** — 模块背景不透明度 `1`（默认）| 标量

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **圆角半径** — 具有模块背景色的区域圆角半径 标量

将模块背景色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### 前景图像

### **X 偏移** — 前景图像左边缘相对于模块左边缘的水平偏移 标量

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y 偏移** — 前景图像上边缘相对于模块上边缘的垂直偏移 标量

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

### **宽度** — 前景图像宽度 标量

将前景图像宽度指定为模块宽度的比例。

**示例：** `0.5`

### **高度** — 前景图像高度 标量

将前景图像高度指定为模块高度的比例。

**示例：** `0.5`

### **锁定纵横比** — 用于保持前景图像纵横比的选项 `on`（默认）| `off`

选择此参数以在使用属性检查器调整图像大小时保持纵横比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2021a 中引入**

### R2025a：在仿真期间选择 Dashboard 模块并打开模块参数对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块所表示的控件交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间均处于活动状态。提升到 Dashboard 面板的模块在面板于其自己的窗口中打开，或已停靠且未锁定时也处于活动状态。对于按下按钮触发的回调中至少有一个具有非空值的 Callback Button 模块，始终处于活动状态。要与非活动模块所表示的控件交互，您可以通过点击模块临时激活模块。当您取消选择该模块时，模块会再次变为非活动状态。

点击活动的 Callback Button 模块，或点击来自 Dashboard 或 Customizable Blocks 库且连接到参数或变量值的活动模块，既会选择该模块，也会与该模块所表示的控件交互。例如，点击未选中的活动且已连接的 Push Button 模块，既会选择该模块，也会按下按钮。从 R2025a 开始，您可以通过按 **Shift** 再点击该模块来选择模块，而无需与控件交互。同样，您可以通过按 **Shift** 再双击该模块来打开模块参数对话框。

### R2024b：使用键盘解锁 Dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您释放 **Shift** 键时，纵横比会锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。当您释放 **Shift** 键时，纵横比会解锁。

### R2024a：将 Dashboard 面板部署为 Web 应用或独立桌面应用

借助 Simulink Compiler™ 许可证，您现在可以将 Dashboard 面板（与面板所连接的模型一起打包）部署为独立桌面应用或 Web 应用。您可以使用该应用操作面板上的控件并监视显示内容，而无需依赖 Simulink。

要了解如何部署面板，请参阅将 Dashboard 面板部署为应用。

### R2024a：停靠 Dashboard 面板

从 R2024a 开始，您可以将 Dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅停靠面板。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 Dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击在新窗口中打开。

您可以独立于模型窗口最小化和还原包含面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击在画布中打开。

有关在新窗口中打开面板的详细信息，请参阅在新窗口中打开面板。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将 Dashboard 面板添加到模型时，Simulink 工具条中会出现 **面板** 选项卡，并显示用于管理和编辑面板的选项。

以前，**面板** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选择面板时，**面板** 选项卡仍保持可见。

**面板** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名选定的面板。
- 您可以隐藏选定的面板。

### R2022b：对面板中的可自定义 Dashboard 模块提供撤消和重做支持

从 R2022b 开始，您可以撤消和重做对面板中的可自定义 Dashboard 模块所做的更改。

要撤消或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：工具条支持面板

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的 Dashboard 模块。

当您点击面板中的 Dashboard 模块时，会出现该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **仪表** 选项卡。

当您点击面板时，工具条中会出现 **面板** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠选定的面板。
- 自定义面板的大小和内容。
- 为选定的面板设置自定义背景图像。
- 向选定的面板添加新选项卡。

### R2022b：在 Raspberry Pi 板上扩展对可自定义 Dashboard 模块的支持

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

您可以自定义 Simulink 模型中模块的视觉外观，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022b：在 Android 设备上扩展对可自定义 Dashboard 模块的支持

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

您可以自定义 Simulink 模型中模块的视觉外观，并在您的 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022a：更改刻度方向

从 R2022a 开始，您可以更改 **Customizable Blocks** 库中以下模块的刻度方向：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：为值条和手柄指定原点

刻度的原点是刻度上的这样一个值：手柄从该值开始移动，值条从该值开始增长。从 R2022a 开始，您可以为 **Customizable Blocks** 库中以下模块的刻度指定原点：

- Circular Gauge
- Horizontal Gauge
- Horizontal Slider
- Knob
- Vertical Gauge
- Vertical Slider

### R2022a：调整前景图像大小并重新定位

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整大小和重新定位前景图像。

## 描述

使用具有可自定义外观的 Horizontal Slider 更改参数或变量值

在仿真期间，使用 Horizontal Slider 模块调整变量或模块参数的值。您可以自定义 Horizontal Slider 模块的外观，使其看起来像真实系统中的控件。您可以调整刻度范围和刻度值，以适合您要调整的值所需的范围。将 Horizontal Slider 模块与其他 Dashboard 模块一起使用，创建用于控制模型的交互式仪表板。

要在仿真运行时调整值，请使用指针将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。要在仿真未运行时调整值，请点击 Horizontal Slider 模块以选择该模块，然后将手柄拖动到您要将连接的变量或模块参数设置为的刻度值。

**注意**

- 在仿真期间或点击模块后，双击已连接的 Horizontal Slider 模块不会打开模块参数对话框。要打开模块参数对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Horizontal Slider 模块既会选择该模块，也会移动滑块手柄。要在不移动滑块手柄的情况下选择该模块，请按 **Shift**，然后点击该模块。

### 自定义 Horizontal Slider 模块

将 Horizontal Slider 模块添加到模型时，该模块已预配置默认设计。您可以使用具有默认设计的模块，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® 工具条中，在模块特定的选项卡上，在 **设计** 下，点击 **编辑**。
- 在属性检查器中，在 **设计** 选项卡上，点击 **编辑**。
- 暂停在模块上方出现的省略号上，然后点击编辑自定义模块按钮。

在设计模式下，您可以使用模块上方的工具栏自定义圆形仪表。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **设计** 选项卡。

处于设计模式的 Horizontal Slider 模块，其中工具栏和属性检查器中的设计选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **设计** 选项卡中可用 |
| --- | --- | --- |
| 上传手柄图像。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 指定值条从何处开始增长的原点位置。 | 否 | 是 |
| 更改刻度线、刻度标签或值条的颜色和不透明度。 | 是 | 是 |
| 将刻度方向指定为从左到右或从右到左。 | 否 | 是 |
| 更改刻度和手柄的大小。 | 否 | 是 |
| 更改刻度和手柄的位置。 | 否 | 是 |

要使用工具栏更改刻度线、刻度标签或值条的颜色和不透明度，请在工具栏从左侧数第二部分中，选择要更改颜色的组件。要更改颜色，请点击色轮。要更改不透明度，请移动滑块。

除了使用工具栏和 **设计** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和重新定位组件。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击连接按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击连接按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数作为连接目标的模块。从出现的列表中，选择要连接到的参数。然后，暂停在 Dashboard 模块上，并点击完成连接按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

此动画显示了如何将 Horizontal Gauge 模块连接到您的模型。

未连接的 Horizontal Slider 模块连接到 Constant 模块。

### 参数记录

连接到 Dashboard 模块的可调参数会记录到仿真数据检查器，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅将数据导出到工作区或文件。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。
