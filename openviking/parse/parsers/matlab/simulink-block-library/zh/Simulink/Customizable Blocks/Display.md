---
type: simulink-block
title: 'Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Customizable Blocks'
documentation_page: 'customdisplay'
documentation_source_path: 'slref/customdisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Display



以可自定义的外观在仿真期间显示信号值

## 库

Simulink / Dashboard / Customizable Blocks

## 说明

Display 模块连接到模型中的信号，并在仿真期间显示信号值。Display 模块可以显示标量信号。当您在 Customizable Blocks 库中使用 Display 模块时，可以自定义该模块的外观，使其看起来像系统中的真实显示屏。将 Display 模块与其他 dashboard 模块一起使用，可为您的模型构建包含控件和指示器的交互式 dashboard。

### 自定义 Display 模块

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

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将 Display 模块连接到模型中的信号，或更改 Display 模块的连接，请进入连接模式。选择要连接到的信号线。在出现的列表中，选择要连接到的信号。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

未连接的 Display 模块连接到 Sine Wave 模块发送到 Outport 模块的信号。

未连接的 Half Gauge 模块连接到 Sine Wave 模块发送到 Display 模块的信号。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

## 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### Signal

### **Connection** — 要连接的信号及显示信号连接选项

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

### **Format** — 用于显示信号值的格式 `short` (default) | `long` | `shortE` | `longE` | ...

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

### **Format String** — 用于格式化数据的自定义字符串 `'%d'` (default) | string

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

### **Label** — 显示所连接元素名称的标签位置 `Top` (default) | `Bottom` | `Hide`

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

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

### Design

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### Display

### **Lock Aspect Ratio** — 保持模块纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，在调整模块大小时按 **Shift** 键会解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。当纵横比未锁定时，在调整模块大小时按 **Shift** 键会锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

#### Text

### **Font** — 字体 `Courier Prime` | `DSEG7-Classic` | `Noto Sans` | `Noto Serif` | `Roboto` | `Ubuntu`

从 WYSIWYG（所见即所得）字体列表中选择，这些字体在所有平台上外观相同。

### **Size** — 字体大小 scalar

从 `6` 到 `72` 之间的字体大小列表中选择。

### **Text Color** — 文本颜色 `[r g b]` vector

从标准颜色调色板中选择文本颜色，或指定自定义颜色。

### **X Offset** — 文本中心相对于模块中心的水平偏移 scalar

将文本中心相对于模块中心的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的文本位置，负值偏移会将文本向左移动，正值偏移会将文本向右移动。

### **Y Offset** — 文本中心相对于模块中心的垂直偏移 scalar

将文本中心相对于模块中心的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的文本位置，负值偏移会将文本向上移动，正值偏移会将文本向下移动。

### **Width** — 文本边界框宽度 scalar

将文本边界框的宽度指定为模块宽度的比例。

### **Height** — 文本边界框高度 scalar

将文本边界框的高度指定为模块高度的比例。

### **Lock Aspect Ratio** — 保持文本边界框纵横比的选项 `on` (default) | `off`

选择此参数可在 Simulink 画布中调整文本边界框大小时保持纵横比。

#### Background Image

### **Use Background Color** — 指定纯色模块背景颜色的选项 `off` (default) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

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

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色覆盖区域的圆角半径指定为模块两个维度（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### Foreground Image

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持前景图像纵横比的选项 `on` (default) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2023b 中引入**

### R2024b：使用键盘解锁 dashboard 模块纵横比

如果来自 Dashboard 库的模块的纵横比已锁定，您可以通过按 **Shift** 临时解锁纵横比。当您释放 **Shift** 键时，纵横比锁定。

如果纵横比未锁定，按 **Shift** 会临时锁定纵横比。当您释放 **Shift** 键时，纵横比解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

使用 Simulink Compiler™ 许可证，您现在可以将与面板所连接模型一起打包的 dashboard 面板部署为独立桌面应用或 Web 应用。您可以使用该应用独立于 Simulink 操作面板上的控件并监视显示。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2024a：Customizable Blocks 库中的 Display 模块可以显示字符串

从 R2024a 开始，Customizable Blocks 库中的 Display 模块可以连接并显示字符串信号。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open in New Window。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中，点击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

## 端口

R2025b 官方文档未提供。
