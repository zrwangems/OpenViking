---
type: simulink-block
title: 'Display'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboarddisplay'
language: zh-CN
chinese_source: official
---

# Display

在仿真期间显示信号值

## 所属库

Simulink / Dashboard

## 描述

Display 模块连接到模型中的信号，并在仿真期间显示信号值。您可以配置 Display 模块的外观和格式，以直观显示数据值。您可以在仿真过程中编辑 Display 模块的参数。Display 模块可以显示复信号、向量信号和二维矩阵信号。将 Display 模块与其他 Dashboard 模块结合使用，为您的模型构建包含各种控件和指示器的交互式仪表板。

### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择您要连接的信号。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。要查看 Dashboard 模块显示连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Display 模块连接到您的模型。

An unconnected Display block connects to the signal that a Ramp block sends to a Terminator block.

## 参数

### 连接

### **连接** — 要连接和显示的信号 信号连接选项

Dashboard 模块不使用端口来连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的**连接**表。有关连接模式以及如何使用工具条进行连接的信息，请参阅Connect Dashboard Blocks to Simulink Model。

使用**连接**表连接 Display 模块或更改 Display 模块的连接：

1. 选择模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**连接**。要更改模块的连接，请改为点击**更改**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击**应用**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.SignalSpecification` |
| **默认值：**`[]` |

### 常设

### **格式** — 用于显示信号值的格式 `short` (默认) | `long` | `shortE` | `longE` | ...

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

#### 编程用法

|  |
| --- |
| **模块参数**：`Format` |
| **类型：**字符数组 | 字符串 |
| **值**：`'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **默认值：**`'short'` |

### **格式字符串** — 用于格式化数据的自定义字符串 `'%d'` (默认) | 字符串

用于格式化所显示信号数据的自定义字符串，指定为字符串。格式字符串由文本和格式化操作符组成，以 `%` 符号开头，以转换字符结尾。您可在字符串中希望显示信号数据的位置使用格式化操作符。有关支持的格式化操作符的详细信息，请参阅 `compose` 函数的 `formatSpec` 输入。

**示例:** `The value of pi is %.2f` 在一个句子中显示连接的信号的值。

**示例:** `$%.2f` 用美元符号和两位小数显示连接的信号的值。

#### 依赖关系

要启用此参数，请将**格式**参数设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`FormatString` |
| **类型：**字符数组 | 字符串 |
| **默认值**：`'%d'` |

### **对齐** — 模块中的文本对齐方式 `Center` (默认) | `Left` | `Right`

Display 模块中的文本对齐。

#### 编程用法

|  |
| --- |
| **模块参数**：`Alignment` |
| **类型：**字符数组 |
| **值**：`'Left'` | `'Center'` | `'Right'` |
| **默认值**：`'Center'` |

### **标签** — 模块标签位置 `Hide` (默认) | `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接的元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型：**字符向量 |
| **值：**`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

### **布局** — 如何排列非标量数据的元素 `Preserve dimensions` (默认) | `Fill available space`

如何排列非标量数据的元素，指定为以下选项之一：

- `Preserve dimensions` - 按照与信号维度匹配的排列方式显示元素。
- `Fill available space` - 在可用空间内显示尽可能多的元素。

#### 编程用法

|  |
| --- |
| **模块参数**：`Layout` |
| **类型：**字符数组 | 字符串 |
| **值**：`'Preserve dimensions'` | `'Fill available space'` |
| **默认值**：`'Preserve dimensions'` |

### 格式

### **显示非标量信号的网格** — 是否显示网格 on (默认) | off

当模块显示非标量数据时，是否在模块上显示网格。使用**网格颜色**参数指定网格的颜色。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowGrid` |
| **类型：**字符数组 | 字符串 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

### **不透明度** — 模块背景不透明度 `1` (默认) | 标量

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例:** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：**`Opacity` |
| **类型：**标量 |
| **默认值：**`1` |

### **前景颜色** — 模块前景颜色 `[r g b]` 向量

模块前景颜色，包括文本。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

### **背景颜色** — 模块的背景色。 `[r g b]` 向量

模块的背景色。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

### **网格颜色** — 模块网格颜色 `[r g b]` 向量

模块网格颜色。网格显示模块何时显示非标量数据。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `GridColor` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 到 `1` 之间。

|  |
| --- |
| **模块参数**：`GridColor` |
| **类型：**`[r g b]` 向量 |
| **默认值**：`[0.502 0.502 0.502]` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

## 版本历史记录

**在 R2017b 中推出**
