---
type: simulink-block
title: 'Display'
family: customizable-blocks
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customdisplay'
---

# Display

Display signal value during simulation with customizable appearance

## 中文

以可自定义的外观在仿真期间显示信号值

### 库

Simulink / Dashboard / Customizable Blocks

### 说明

Display 模块连接到模型中的信号，并在仿真期间显示信号值。Display 模块可以显示标量信号。当您在 Customizable Blocks 库中使用 Display 模块时，可以自定义该模块的外观，使其看起来像系统中的真实显示屏。将 Display 模块与其他 dashboard 模块一起使用，可为您的模型构建包含控件和指示器的交互式 dashboard。

#### 自定义 Display 模块

当您将 Display 模块添加到模型时，该模块预配置了默认设计。您可以使用默认设计使用该模块，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择该模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定选项卡上的 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上出现的省略号上，然后点击 Edit Custom Block 按钮。

在设计模式中，可以使用模块上方的工具栏自定义显示。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

设计模式下的可自定义 Display 模块，工具栏和 Property Inspector 中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改字体。可从 WYSIWYG（所见即所得）字体列表中选择，这些字体在所有平台上外观相同。 | 是 | 是 |
| 更改字体大小。 | 是 | 是 |
| 更改文本颜色。 | 是 | 是 |
| 将文本加粗、倾斜或加下划线。 | 是 | 是 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |
| 更改文本在模块中的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式重新定位文本。

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将 Display 模块连接到模型中的信号，或更改 Display 模块的连接，请进入连接模式。选择要连接到的信号线。在出现的列表中，选择要连接到的信号。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

未连接的 Display 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。

未连接的 Half Gauge 模块连接到 Sine Wave 模块发送到 Display 模块的信号。

### 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

### 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### Signal

#### **Connection** — 要连接的信号及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用 toolstrip 连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接 Display 模块或更改 Display 模块的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 中的 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接到的信号线。
4. 在表中，选择要连接到的信号。
5. 点击 **Apply**。

您还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

#### Main

#### **Format** — 用于显示信号值的格式 `short` (default) | `long` | `shortE` | `longE` | ...

指定用于显示信号值的格式。

| 如果您选择... | 模块显示... |
| --- | --- |
| `short` | 缩放定点十进制格式，小数点后四位。 |
| `long` | 缩放定点十进制格式，对于 `double` 值，小数点后十五位；对于 `single` 值，小数点后七位。 |
| `shortE` | 科学记数法格式，四位数字。 |
| `longE` | 科学记数法格式，对于 `double` 值，小数点后十五位；对于 `single` 值，小数点后七位。 |
| `shortG` | 数据采用定点十进制或科学记数法中更紧凑的格式，总共五位数字。 |
| `longG` | 数据采用定点十进制或科学记数法中更紧凑的格式，对于 `double` 值，总共十五位数字；对于 `single` 值，总共七位数字。 |
| `shortEng` | 工程记数法，其中指数为三的倍数，小数点后四位。 |
| `longEng` | 工程记数法，其中指数为三的倍数，十五位有效数字。 |
| `+-` | 正/负格式。分别对正值、负值和零值显示 `+`、`-` 和空白字符。 |
| `bank` | 货币格式，小数点后两位。 |
| `hex` | 十六进制表示。 |
| `rat` | 比率。 |
| `Custom` | 自定义字符串格式。数据以您使用 **Format String** 参数指定的自定义字符串显示。 |
| `Integer` | 数据舍入到最接近的整数。 |

当您将 Display 模块连接到 String Constant 模块输出的信号时，显示信号值的格式为 `string`，无论 **Format** 参数的值如何。同样，当您将 Display 模块连接到 Enumerated Constant 模块输出的信号时，显示信号值的格式为 `enum`，无论 **Format** 参数的值如何。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Format` |
| **类型：** character array | string |
| **值：** `'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **默认值：** `'short'` |

#### **Format String** — 用于格式化数据的自定义字符串 `'%d'` (default) | string

指定用于格式化所显示信号数据的自定义字符串。格式字符串由文本和格式运算符组成，格式运算符以 `%` 符号开头，并以转换字符结尾。在字符串中希望显示信号数据的位置使用格式运算符。有关支持的格式运算符的详细信息，请参阅 `compose` 函数的 `formatSpec` 输入。

**示例：** `The value of pi is %.2f` 在句子中显示所连接信号的值。

**示例：** `$%.2f` 显示所连接信号的值，并带有美元符号和两位小数。

#### 依赖关系

要启用此参数，请将 **Format** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FormatString` |
| **类型：** character array | string |
| **默认值：** `'%d'` |

#### **Label** — 显示所连接元素名称的标签位置 `Top` (default) | `Bottom` | `Hide`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请指定 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Top'` | `'Bottom'` | `'Hide'` |
| **默认值：** `'Top'` |

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

#### Design

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### Display

#### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

#### Text

#### **Font** — 字体 `Courier Prime` | `DSEG7-Classic` | `Noto Sans` | `Noto Serif` | `Roboto` | `Ubuntu`

从 WYSIWYG（所见即所得）字体列表中选择，这些字体在所有平台上外观相同。

#### **Size** — 字体大小 scalar

从 `6` 到 `72` 之间的字体大小列表中选择。

#### **Text Color** — 文本颜色 `[r g b]` vector

从标准颜色调色板中选择文本颜色，或指定自定义颜色。

#### **X Offset** — 文本中心相对于模块中心的水平偏移 scalar

将文本中心相对于模块中心的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的文本位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

#### **Y Offset** — 文本中心相对于模块中心的垂直偏移 scalar

将文本中心相对于模块中心的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的文本位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

#### **Width** — 文本边界框宽度 scalar

将文本边界框的宽度指定为模块宽度的比例。

#### **Height** — 文本边界框高度 scalar

将文本边界框的高度指定为模块高度的比例。

#### **Lock Aspect Ratio** — 保持文本边界框纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整文本边界框大小时保持纵横比。

#### Background Image

#### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

#### **Color** — 模块背景颜色 `[r g b]` vector

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您也可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 程序化使用

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` 的 `[r g b]` vector，其值介于 `0` 和 `1` 之间，并格式化为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` vector |

#### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

#### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色覆盖区域的圆角半径指定为模块两个维度（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### Foreground Image

#### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

#### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

#### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

#### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

#### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

### 版本历史

**在 R2023b 中引入**

#### R2024b：使用键盘解锁 dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

#### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

使用 Simulink Compiler™ 许可证，您现在可以将与面板所连接模型一起打包的 dashboard 面板部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

#### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

#### R2024a：Customizable Blocks 库中的 Display 模块可以显示字符串

从 R2024a 开始，Customizable Blocks 库中的 Display 模块可以连接并显示字符串信号。

#### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open in New Window。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中，点击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

## Libraries

Simulink / Dashboard / Customizable Blocks

## Description

The Display block connects to a signal in your model and displays the
signal value during simulation. The Display block can display scalar signals.
When you use the Display block in the Customizable Blocks library, you can customize the
appearance of the block to look like a real display in your system. Use the
Display block with other dashboard blocks to build an interactive dashboard
of controls and indicators for your model.

### Customize Display Blocks

When you add a Display block to your model, the block is preconfigured
with a default design. You can use the block with the default design or customize the
appearance of the block.

To customize the appearance of the block, use design mode.
After selecting the block, you can enter design mode in one of three ways:

- In the Simulink® Toolstrip, on the block-specific tab, under
  **Design**, click **Edit**.
- In the Property Inspector, on the **Design** tab, click
  **Edit**.
- Pause on the ellipsis that appears over the block and click the Edit Custom Block
  button .

In design mode, you can use the toolbar above the block to customize the display. To
access additional customization options or to enter exact values for design settings, use
the **Design** tab in the Property Inspector.

Customizable Display block in design mode with the toolbar and the Design tab in the Property Inspector visible.

**Design Mode Actions**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the font. Choose from a list of WYSIWYG (what you see is what you get) fonts that look the same on all platforms. | Yes | Yes |
| Change the font size. | Yes | Yes |
| Change the text color. | Yes | Yes |
| Make the text bold, italic, or underlined. | Yes | Yes |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |
| Change the position of the text within the block. | No | Yes |

In addition to customizing the block design using the toolbar and
**Design** tab, you can also reposition the text interactively in the
canvas.

When you finish editing the design, to exit design mode, click the
**X** in the upper right of the canvas.

### Connect Dashboard Blocks

Dashboard blocks do not use ports to connect to model elements. To connect a dashboard block,
use connect mode. To enter connect mode on an unconnected block, pause on the block you want
to connect and click the Connect button . To enter connect mode on a connected block, select the
block, pause on the ellipsis that appears (…), and in the action menu that expands, click
the Connect button.

To connect a display block to a signal in your model or change the connection of a display
block, enter connect mode. Select the signal line to which you want to connect. From the
list that appears, select the signal to which you want to connect. Then, pause on the
dashboard block and click the Done Connecting button . To see the dashboard block display the value of the
connected block, run the simulation.

For more information about connecting dashboard blocks, see Connect Dashboard Blocks to Simulink Model.

You can also connect dashboard blocks to a Stateflow® chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

An unconnected Display block connects to the signal that a Sine Wave block sends to
an Outport block.

An unconnected Half Gauge block connects to the signal that a Sine Wave block sends to a Display block.

## Parameters

Use the Property Inspector and the Block Parameters dialog box
to specify the values of the block parameters. To set the core parameters of the dashboard
block, use the Block Parameters dialog box or the **Parameters** tab in the
Property Inspector. To customize the block, use the **Design** tab in the
Property Inspector. To open the Block Parameters dialog box for a block, double-click the block.
To open the Property Inspector, on the **Modeling** tab, under
**Design**, select **Property Inspector**.

### Parameters

To set the core parameters of the dashboard block, open the
Property Inspector and click the **Parameters** tab.

#### Signal

### **Connection** — Signal to connect and display signal connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink Toolstrip, or the **Connection** table in the Block
Parameters dialog box. For information about connect mode and how to connect using the
toolstrip, see Connect Dashboard Blocks to Simulink Model.

To connect a display block or change the connection of a display block using the **Connection** table:

1. Select the block.
2. To connect the block, in the Property Inspector, on the **Parameters** tab, click **Connect**. To change the connection of the block, click **Change** instead.
3. Select the signal line to which you want to connect.
4. In the table, select the signal to which you want to connect.
5. Click **Apply**.

You can also connect dashboard blocks to a Stateflow chart. For more information, see Connect Dashboard Blocks to Stateflow (Stateflow).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.SignalSpecification` |
| **Default:** `[]` |

#### Main

### **Format** — Format for displaying signal values `short` (default) | `long` | `shortE` | `longE` | ...

Specify a format for displaying signal values.

| If You Select... | The Block Displays... |
| --- | --- |
| `short` | Scaled fixed-decimal format with four digits after the decimal point. |
| `long` | Scaled fixed-decimal format with fifteen digits after the decimal point for `double` values and seven digits after the decimal point for `single` values. |
| `shortE` | Scientific notation format with four digits. |
| `longE` | Scientific notation format with fifteen digits after the decimal point for `double` values and seven digits after the decimal point for `single` values. |
| `shortG` | Data takes the more compact format between fixed-decimal or scientific notation, with a total of five digits. |
| `longG` | Data takes the more compact format between fixed-decimal or scientific notation, with a total of fifteen digits for `double` values and seven digits for `single` values. |
| `shortEng` | Engineering notation where the exponent is a multiple of three, with four digits after the decimal point. |
| `longEng` | Engineering notation where the exponent is a multiple of three, with fifteen significant digits. |
| `+-` | Positive/negative format. `+`, `-`, and blank characters are displayed for positive, negative, and zero values, respectively. |
| `bank` | Currency format with two digits after the decimal point. |
| `hex` | Hexadecimal representation. |
| `rat` | Ratio. |
| `Custom` | Custom string format. Data is displayed in a custom string that you specify using the **Format String** parameter. |
| `Integer` | Data rounded to the nearest whole number. |

When you connect the Display block to the signal output
by a String Constant block, the format for displaying signal values is
`string`, regardless of the value of the
**Format** parameter. Similarly, when you connect the
Display block to the signal output by an Enumerated
Constant block, the format for displaying signal values is
`enum`, regardless of the value of the **Format** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character array | string |
| **Values:** `'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **Default:** `'short'` |

### **Format String** — Custom string to format data `'%d'` (default) | string

Specify a custom string to format displayed signal data. The format string
consists of text and format operators, which start with a `%` sign
and end with a conversion character. Use the format operators at the place in the
string where you want the signal data to display. For more information about supported
formatting operators, see the `formatSpec` input of the `compose` function.

**Example:** `The value of pi is %.2f` displays the value of the
connected signal within a sentence.

**Example:** `$%.2f` displays the value of the connected signal with a
dollar sign and two decimal places.

#### Dependencies

To enable this parameter, set **Format** to
`Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |
| **Type:** character array | string |
| **Default:** `'%d'` |

### **Label** — Position of label displaying name of connected element `Top` (default) | `Bottom` | `Hide`

You can display the name of the element to which the dashboard block connects in a
label positioned at the top or at the bottom of the block, or you can hide the label. If
you want the label to be visible, specify the position of the label. If you do not want
the label to be visible, specify `Hide`.

**Note**

When the dashboard block is not connected to an element, the label is
blank.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match the aspect ratio of the background image. When the aspect
ratio is unlocked, adding a new background image does not change the aspect ratio of the
block, but instead changes the aspect ratio of the background image to fit the size of
the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block temporarily unlocks the aspect ratio. When you release the
**Shift** key, the aspect ratio locks. When the aspect ratio is
unlocked, pressing the **Shift** key while resizing a block temporarily
locks the aspect ratio. When you release the **Shift** key, the aspect
ratio unlocks.

### Design

To customize the dashboard block, open the Property Inspector,
click the **Design** tab, and click **Edit**.

#### Display

### **Lock Aspect Ratio** — Option to maintain block aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the block in the
Simulink canvas.

When the aspect ratio is locked, adding a new background image changes the aspect
ratio of the block to match that of the background image. When the aspect ratio is
unlocked, adding a new background image does not change the proportions of the block but
instead stretches or scales the background image to fit the size of the block.

When the aspect ratio is locked, pressing the **Shift** key while
resizing a block unlocks the aspect ratio. When you release the **Shift**
key, the aspect ratio locks. When the aspect ratio is unlocked, pressing the
**Shift** key while resizing a block locks the aspect ratio. When you
release the **Shift** key, the aspect ratio unlocks.

#### Text

### **Font** — Font `Courier Prime` | `DSEG7-Classic` | `Noto Sans` | `Noto Serif` | `Roboto` | `Ubuntu`

Choose from a list of WYSIWYG (what you see is what you get) fonts that look the
same on all platforms.

### **Size** — Font size scalar

Choose from a list of font sizes between `6` and
`72`.

### **Text Color** — Text color `[r g b]` vector

Choose a text color from the palette of standard colors, or specify a custom
color.

### **X Offset** — Horizontal offset of center of text from center of block scalar

Specify the horizontal offset of the center of the text from the center of the
block as a ratio of the block width. Relative to the position of the text when the
offset is `0`, an offset with a negative value moves the text left,
and an offset with a positive value moves the text right.

### **Y Offset** — Vertical offset of center of text from center of block scalar

Specify the vertical offset of the center of the text from the center of the block
as a ratio of the block height. Relative to the position of the text when the offset
is `0`, an offset with a negative value moves the text up, and an
offset with a positive value moves the text down.

### **Width** — Width of text bounding box scalar

Specify the width of the bounding box of the text as a ratio of the block
width.

### **Height** — Height of text bounding box scalar

Specify the height of the bounding box of the text as a ratio of the block
height.

### **Lock Aspect Ratio** — Option to maintain text bounding box aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the bounding box
of the text in the Simulink canvas.

#### Background Image

### **Use Background Color** — Option to specify solid block background color `off` (default) | `on`

For the block background, you can provide a background image or select a solid color.
To select a solid background color, select this parameter. To provide a background
image, clear this parameter.

**Note**

Changing the background color using the **Format** tab of the
Simulink Toolstrip removes the background image and enables the **Use
Background Color** parameter.

**Example:** `on`

### **Color** — Block background color `[r g b]` vector

To use a solid background color, select the **Use Background Color**
parameter. Then, choose a background color from the palette of standard colors, or
specify a custom color.

**Tip**

You can also specify the **Background Color** in the
**Format** tab of the Simulink Toolstrip.

To specify the color of the block text, use the **Font Color**
parameter.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1` that is formatted as a string or a character vector.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Opacity** — Block background opacity `1` (default) | scalar

Specify the block background opacity as a scalar value from `0` to
`1`.

**Example:** `0.5`

### **Corner Radius** — Corner radius of area with block background color scalar

Specify the corner radius of the area covered by the block background color as a ratio
of half of the smaller of the two block dimensions, width or height.

**Example:** `0.25`

#### Foreground Image

### **X Offset** — Horizontal offset of left edge of foreground image from left edge of block scalar

Specify the horizontal offset of the left edge of the image from the left edge of the
block as a ratio of the block width. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image left,
and an offset with a positive value moves the image right.

**Example:** `1`

### **Y Offset** — Vertical offset of top edge of foreground image from top edge of block scalar

Specify the vertical offset of the top edge of the image from the top edge of the
block as a ratio of the block height. Relative to the position of the image when the
offset is `0`, an offset with a negative value moves the image up, and
a positive value moves the image down.

**Example:** `1`

### **Width** — Foreground image width scalar

Specify the width of the foreground image as a ratio of the block width.

**Example:** `0.5`

### **Height** — Foreground image height scalar

Specify the height of the foreground image as a ratio of the block height.

**Example:** `0.5`

### **Lock Aspect Ratio** — Option to maintain foreground image aspect ratio `on` (default) | `off`

Select this parameter to maintain the aspect ratio when resizing the image using the
Property Inspector.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard blocks are ignored for code generation.

## Version History

**Introduced in R2023b**

### R2024b: Unlock dashboard block aspect ratio with keyboard

If the aspect ratio of a block from the Dashboard library is locked, you can temporarily
unlock the aspect ratio by pressing **Shift**. When you release the
**Shift** key, the aspect ratio locks.

If the aspect ratio is unlocked, pressing **Shift** temporarily locks the
aspect ratio. When you release the **Shift** key, the aspect ratio
unlocks.

### R2024a: Deploy dashboard panel as web app or standalone desktop app

With a Simulink
Compiler™ license, you can now deploy a dashboard panel, packaged with the model to
which the panel connects, as a standalone desktop app or as a web app. You can use the app
to operate the controls and monitor the displays on the panel independent of Simulink.

To learn how to deploy panels, see Deploy Dashboard Panel as App.

### R2024a: Dock dashboard panels

Starting in R2024a, you can dock dashboard panels to the Simulink Editor window. You can use the docked panel to monitor signals and control
parameters during simulation without covering the model diagram in the canvas.

For more information, see Dock Panels.

### R2024a: Display block from Customizable Blocks library can display strings

Starting in R2024a, the Display block from the
Customizable Blocks library can connect to and display signals that are strings.

### R2023b: Open Panel in New Window

Starting in R2023b, you can open a dashboard panel in a new window. To do so, select the
panel and pause on the ellipsis that appears. In the action menu that expands, click Open in
New Window .

You can minimize and restore the new window containing the panel separately from the
model window. From the panel window, you can run, pause, stop, and step through the
simulation. In the panel window, you can edit the panel and the blocks it contains.

To return the panel to the model canvas, in the panel window toolstrip, click Open in
canvas .

For more information about opening a panel in a new window, see Open Panels in New Window.
