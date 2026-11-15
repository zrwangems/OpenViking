---
type: simulink-block
title: 'Display'
family: dashboard
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboarddisplay'
---

# Display

Display signal value during simulation

## 中文

在仿真期间显示信号值

### 所属库

Simulink / Dashboard

### 描述

Display 模块连接到模型中的信号，并在仿真期间显示信号值。您可以配置 Display 模块的外观和格式，以直观显示数据值。您可以在仿真过程中编辑 Display 模块的参数。Display 模块可以显示复信号、向量信号和二维矩阵信号。将 Display 模块与其他 Dashboard 模块结合使用，为您的模型构建包含各种控件和指示器的交互式仪表板。

#### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择您要连接的信号。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。要查看 Dashboard 模块显示连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Display 模块连接到您的模型。

An unconnected Display block connects to the signal that a Ramp block sends to a Terminator block.

### 参数

#### 连接

#### **连接** — 要连接和显示的信号 信号连接选项

Dashboard 模块不使用端口来连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的**连接**表。有关连接模式以及如何使用工具条进行连接的信息，请参阅Connect Dashboard Blocks to Simulink Model。

使用**连接**表连接 Display 模块或更改 Display 模块的连接：

1. 选择模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**连接**。要更改模块的连接，请改为点击**更改**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击**应用**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

##### 编程用法

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.SignalSpecification` |
| **默认值：**`[]` |

#### 常设

#### **格式** — 用于显示信号值的格式 `short` (默认) | `long` | `shortE` | `longE` | ...

指定用于显示信号值的格式。

| 如果您选择... | 模块显示... |
| --- | --- |
| `short` | 小数点后具有 4 位数的定标固定十进制格式。 |
| `long` | 定标固定十进制格式，`double` 值的小数点后具有 15 位数，`single` 值的小数点后具有 7 位数。 |
| `shortE` | 具有 4 位数的科学记数法格式。 |
| `longE` | 科学记数法格式，`double` 值的小数点后具有 15 位数，`single` 值的小数点后具有 7 位数。 |
| `shortG` | 数据取固定十进制或科学记数法中较紧凑的格式，共有 5 位数。 |
| `longG` | 数据取固定十进制或科学记数法中较紧凑的格式，`double` 值共有 15 位数，`single` 值共有 7 位数。 |
| `shortEng` | 工程记数法，其中指数为 3 的倍数，小数点后具有 4 位数。 |
| `longEng` | 工程记数法，其中指数为 3 的倍数，有效位数为 15 位。 |
| `+-` | 正/负格式。对正值、负值和零值分别显示 `+`、`-` 和空白字符。 |
| `bank` | 货币格式，小数点后包含 2 位数。 |
| `hex` | 十六进制表示。 |
| `rat` | 比率。 |
| `Custom` | 自定义字符串格式。数据以您使用**格式化字符串**参数指定的自定义字符串形式显示。 |
| `Integer` | 数据舍入到最邻近的整数。 |

当您将 Display 模块连接到 String Constant 模块输出的信号时，无论**格式**参数的值如何，显示信号值的格式均为 `string`。同样，当您将 Display 模块连接到 Enumerated Constant 模块输出的信号时，无论**格式**参数的值如何，显示信号值的格式均为 `enum`。

Display blocks show example outputs for these formats: short, long, shortE, longE, shortG, longG, Custom, shortEng, longEng, bank, plus, hex, rat, Integer, string, and enum.

##### 编程用法

|  |
| --- |
| **模块参数**：`Format` |
| **类型：**字符数组 | 字符串 |
| **值**：`'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **默认值：**`'short'` |

#### **格式字符串** — 用于格式化数据的自定义字符串 `'%d'` (默认) | 字符串

用于格式化所显示信号数据的自定义字符串，指定为字符串。格式字符串由文本和格式化操作符组成，以 `%` 符号开头，以转换字符结尾。您可在字符串中希望显示信号数据的位置使用格式化操作符。有关支持的格式化操作符的详细信息，请参阅 `compose` 函数的 `formatSpec` 输入。

**示例:** `The value of pi is %.2f` 在一个句子中显示连接的信号的值。

**示例:** `$%.2f` 用美元符号和两位小数显示连接的信号的值。

##### 依赖关系

要启用此参数，请将**格式**参数设置为 `Custom`。

##### 编程用法

|  |
| --- |
| **模块参数**：`FormatString` |
| **类型：**字符数组 | 字符串 |
| **默认值**：`'%d'` |

#### **对齐** — 模块中的文本对齐方式 `Center` (默认) | `Left` | `Right`

Display 模块中的文本对齐。

##### 编程用法

|  |
| --- |
| **模块参数**：`Alignment` |
| **类型：**字符数组 |
| **值**：`'Left'` | `'Center'` | `'Right'` |
| **默认值**：`'Center'` |

#### **标签** — 模块标签位置 `Hide` (默认) | `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接的元素的名称。

##### 编程用法

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型：**字符向量 |
| **值：**`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

#### **布局** — 如何排列非标量数据的元素 `Preserve dimensions` (默认) | `Fill available space`

如何排列非标量数据的元素，指定为以下选项之一：

- `Preserve dimensions` - 按照与信号维度匹配的排列方式显示元素。
- `Fill available space` - 在可用空间内显示尽可能多的元素。

##### 编程用法

|  |
| --- |
| **模块参数**：`Layout` |
| **类型：**字符数组 | 字符串 |
| **值**：`'Preserve dimensions'` | `'Fill available space'` |
| **默认值**：`'Preserve dimensions'` |

#### 格式

#### **显示非标量信号的网格** — 是否显示网格 on (默认) | off

当模块显示非标量数据时，是否在模块上显示网格。使用**网格颜色**参数指定网格的颜色。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowGrid` |
| **类型：**字符数组 | 字符串 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **不透明度** — 模块背景不透明度 `1` (默认) | 标量

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例:** `0.5`

##### 编程用法

|  |
| --- |
| **模块参数：**`Opacity` |
| **类型：**标量 |
| **默认值：**`1` |

#### **前景颜色** — 模块前景颜色 `[r g b]` 向量

模块前景颜色，包括文本。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

##### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

#### **背景颜色** — 模块的背景色。 `[r g b]` 向量

模块的背景色。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

##### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

#### **网格颜色** — 模块网格颜色 `[r g b]` 向量

模块网格颜色。网格显示模块何时显示非标量数据。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

##### 编程用法

将模块的 `GridColor` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 到 `1` 之间。

|  |
| --- |
| **模块参数**：`GridColor` |
| **类型：**`[r g b]` 向量 |
| **默认值**：`[0.502 0.502 0.502]` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

### 版本历史记录

**在 R2017b 中推出**

## Libraries

Simulink / Dashboard

## Description

The Display block connects to a signal in your model and displays its
value during simulation. You can configure the appearance and format of the
Display block to make intuitive sense for the value it displays. You
can edit the parameters of the Display block during simulation. The
Display block can display complex, vector, and 2-D matrix signals.
Use the Display block with other dashboard blocks to build an interactive
dashboard of controls and indicators for your model.

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

This animation shows how to connect the Display block to your
model.

An unconnected Display block connects to the signal that a Ramp block sends to a Terminator block.

## Parameters

### Connection

### **Connection** — Signal to connect and display signal connection options

Dashboard blocks do not use ports to connect to model elements. To connect dashboard
blocks to parameter values in your model, use connect mode, the Simulink® Toolstrip, or the **Connection** table in the Block
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

### Main

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

When you connect the Display block to the
signal output by a String Constant block, the format for
displaying signal values is `string`, regardless of the
value of the **Format** parameter. Similarly, when you
connect the Display block to the signal output by an
Enumerated Constant block, the format for displaying
signal values is `enum`, regardless of the value of the
**Format** parameter.

Display blocks show example outputs for these formats: short, long, shortE, longE, shortG, longG, Custom, shortEng, longEng, bank, plus, hex, rat, Integer, string, and enum.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character array | string |
| **Values:** `'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **Default:** `'short'` |

### **Format String** — Custom string to format data `'%d'` (default) | string

Custom string to format displayed signal data, specified as a string.
The format string consists of text and format operators, which start
with a `%` sign and end with a conversion character.
Use the format operators at the place in the string where you want the
signal data to display. For more information about supported formatting
operators, see the `formatSpec` input of the `compose` function.

**Example:** `The value of pi is %.2f` displays the value
of the connected signal within a sentence.

**Example:** `$%.2f` displays the value of the connected
signal with a dollar sign and two decimal places.

#### Dependencies

To enable this parameter, set the **Format**
parameter to `Custom`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FormatString` |
| **Type:** character array | string |
| **Default:** `'%d'` |

### **Alignment** — Text alignment in block `Center` (default) | `Left` | `Right`

Text alignment in the Display block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Alignment` |
| **Type:** character array |
| **Values:** `'Left'` | `'Center'` | `'Right'` |
| **Default:** `'Center'` |

### **Label** — Block label position `Hide` (default) | `Bottom` | `Top`

Position of the block label. When the block is connected to an element in the
model, the label is the name of the connected element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

### **Layout** — How to arrange elements of non-scalar data `Preserve dimensions` (default) | `Fill available space`

How to arrange elements of non-scalar data, specified as one of these options:

- `Preserve dimensions` — Display elements
  arranged to match signal dimensions.
- `Fill available space` — Display as many
  elements as possible within available space.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Layout` |
| **Type:** character array | string |
| **Values:** `'Preserve dimensions'` | `'Fill available space'` |
| **Default:** `'Preserve dimensions'` |

### Format

### **Show grid for non-scalar signals** — Whether to show grid on (default) | off

Whether to show a grid on the block when the block displays non-scalar
data. Specify the color of the grid using the **Grid
Color** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowGrid` |
| **Type:** character array | string |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Opacity** — Block background opacity `1` (default) | scalar

Block background opacity, specified as a scalar value between 0 and 1.

**Example:** `0.5`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Opacity` |
| **Type:** scalar |
| **Default:** `1` |

### **Foreground Color** — Block foreground color `[r g b]` vector

Block foreground color, including the text. You can select a color from a palette
of standard colors or specify a custom color.

#### Programmatic Use

Specify the `ForegroundColor` parameter for the block as a
string or a character vector that defines a
`1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `ForegroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Background Color** — Block background color `[r g b]` vector

Block background color. You can select a color from a palette of standard colors or specify a custom color.

#### Programmatic Use

Specify the `BackgroundColor` parameter for the block as a string or a
character vector that defines a `1`-by-`3`
`[r g b]` vector with values between `0` and
`1`.

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** character vector | string |
| **Values:** `[r g b]` vector |

### **Grid Color** — Block grid color `[r g b]` vector

Block grid color. The grid shows when the block displays non-scalar
data. You can select a color from a palette of standard colors or
specify a custom color.

#### Programmatic Use

Specify the `GridColor` parameter for the block
as a `1`-by-`3`
`[r g b]` vector with values between
`0` and `1`.

|  |
| --- |
| **Block Parameter:** `GridColor` |
| **Type:** `[r g b]` vector |
| **Default:** `[0.502 0.502 0.502]` |

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

**Introduced in R2017b**
