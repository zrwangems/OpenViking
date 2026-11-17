---
type: simulink-block
title: 'Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboarddisplay'
documentation_source_path: 'slref/dashboarddisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Display

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 要连接的信号及显示信号连接选项
  group: 连接
  block_parameter: Binding
  type: Simulink.HMI.SignalSpecification
  default: '[]'
- name: Format
  summary: 显示信号值的格式 short（默认）| long | shortE | longE | ...
  group: 主要
  block_parameter: Format
  type: character array | string
  values: '''short'' | ''long'' | ''shortE'' | ''longE'' | ''shortG'' | ''longG'' | ''shortEng'' | ''longEng'' | ''bank''
    | ''+'' | ''hex'' | ''rat'' | ''Custom'' | ''Integer'''
  default: '''short'''
- name: Format String
  summary: 用于格式化数据的自定义字符串 '%d'（默认）| string
  group: 主要
  block_parameter: FormatString
  type: character array | string
  default: '''%d'''
- name: Alignment
  summary: 模块中的文本对齐方式 Center（默认）| Left | Right
  group: 主要
  block_parameter: Alignment
  type: character array
  values: '''Left'' | ''Center'' | ''Right'''
  default: '''Center'''
- name: Label
  summary: 模块标签位置 Hide（默认）| Bottom | Top
  group: 主要
  block_parameter: LabelPosition
  type: character vector
  values: '''Hide'' | ''Bottom'' | ''Top'''
  default: '''Hide'''
- name: Layout
  summary: 如何排列非标量数据的元素 Preserve dimensions（默认）| Fill available space
  group: 主要
  block_parameter: Layout
  type: character array | string
  values: '''Preserve dimensions'' | ''Fill available space'''
  default: '''Preserve dimensions'''
- name: Show grid for non-scalar signals
  summary: 是否显示网格 on（默认）| off
  group: 格式
  block_parameter: ShowGrid
  type: character array | string
  values: '''on'' | ''off'''
  default: '''on'''
- name: Opacity
  summary: 模块背景不透明度 1（默认）| scalar
  group: 格式
  block_parameter: Opacity
  type: scalar
  default: '1'
- name: Foreground Color
  summary: 模块前景色 [r g b] 向量
  group: 格式
  block_parameter: ForegroundColor
  type: character vector | string
  values: '[r g b] vector'
- name: Background Color
  summary: 模块背景色 [r g b] 向量
  group: 格式
  block_parameter: BackgroundColor
  type: character vector | string
  values: '[r g b] vector'
- name: Grid Color
  summary: 模块网格颜色 [r g b] 向量
  group: 格式
  block_parameter: GridColor
  type: '[r g b] vector'
  default: '[0.502 0.502 0.502]'
```

### 连接

### **Connection** — 要连接的信号及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 Dashboard 模块连接到 Stateflow 流程图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.SignalSpecification` |
| **默认值**：`[]` |

### 主要

### **Format** — 显示信号值的格式 `short`（默认）| `long` | `shortE` | `longE` | ...

指定显示信号值的格式。

| 如果选择... | 模块显示... |
| --- | --- |
| `short` | 缩放定点十进制格式，小数点后四位。 |
| `long` | 缩放定点十进制格式，对于 `double` 值小数点后十五位，对于 `single` 值小数点后七位。 |
| `shortE` | 科学计数法格式，四位数字。 |
| `longE` | 科学计数法格式，对于 `double` 值小数点后十五位，对于 `single` 值小数点后七位。 |
| `shortG` | 数据采用定点十进制或科学计数法中更紧凑的格式，总共五位数字。 |
| `longG` | 数据采用定点十进制或科学计数法中更紧凑的格式，对于 `double` 值总共十五位数字，对于 `single` 值七位数字。 |
| `shortEng` | 工程计数法，指数为三的倍数，小数点后四位。 |
| `longEng` | 工程计数法，指数为三的倍数，十五位有效数字。 |
| `+-` | 正/负格式。分别对正值、负值和零值显示 `+`、`-` 和空白字符。 |
| `bank` | 货币格式，小数点后两位。 |
| `hex` | 十六进制表示。 |
| `rat` | 比率。 |
| `Custom` | 自定义字符串格式。数据以您使用 **Format String** 参数指定的自定义字符串显示。 |
| `Integer` | 数据四舍五入到最接近的整数。 |

当您将 Display 模块连接到 String Constant 模块输出的信号时，显示信号值的格式为 `string`，无论 **Format** 参数的值如何。类似地，当您将 Display 模块连接到 Enumerated Constant 模块输出的信号时，显示信号值的格式为 `enum`，无论 **Format** 参数的值如何。

Display 模块显示以下格式的示例输出：short、long、shortE、longE、shortG、longG、Custom、shortEng、longEng、bank、plus、hex、rat、Integer、string 和 enum。

#### 编程使用

|  |
| --- |
| **模块参数**：`Format` |
| **类型**：character array | string |
| **值**：`'short'` | `'long'` | `'shortE'` | `'longE'` | `'shortG'` | `'longG'` | `'shortEng'` | `'longEng'` | `'bank'` | `'+'` | `'hex'` | `'rat'` | `'Custom'` | `'Integer'` |
| **默认值**：`'short'` |

### **Format String** — 用于格式化数据的自定义字符串 `'%d'`（默认）| string

用于格式化显示信号数据的自定义字符串，指定为字符串。格式字符串由文本和格式运算符组成，格式运算符以 `%` 符号开头，以转换字符结尾。在字符串中希望显示信号数据的位置使用格式运算符。有关支持的格式运算符的详细信息，请参阅 `compose` 函数的 `formatSpec` 输入。

**示例：** `The value of pi is %.2f` 在句子中显示所连接信号的值。

**示例：** `$%.2f` 显示所连接信号的值，带有美元符号和两位小数。

#### 依赖关系

要启用此参数，请将 **Format** 参数设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`FormatString` |
| **类型**：character array | string |
| **默认值**：`'%d'` |

### **Alignment** — 模块中的文本对齐方式 `Center`（默认）| `Left` | `Right`

Display 模块中的文本对齐方式。

#### 编程使用

|  |
| --- |
| **模块参数**：`Alignment` |
| **类型**：character array |
| **值**：`'Left'` | `'Center'` | `'Right'` |
| **默认值**：`'Center'` |

### **Label** — 模块标签位置 `Hide`（默认）| `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

### **Layout** — 如何排列非标量数据的元素 `Preserve dimensions`（默认）| `Fill available space`

如何排列非标量数据的元素，指定为以下选项之一：

- `Preserve dimensions` — 显示的元素排列与信号维度匹配。
- `Fill available space` — 在可用空间内显示尽可能多的元素。

#### 编程使用

|  |
| --- |
| **模块参数**：`Layout` |
| **类型**：character array | string |
| **值**：`'Preserve dimensions'` | `'Fill available space'` |
| **默认值**：`'Preserve dimensions'` |

### 格式

### **Show grid for non-scalar signals** — 是否显示网格 on（默认）| off

当模块显示非标量数据时，是否在模块上显示网格。使用 **Grid Color** 参数指定网格的颜色。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowGrid` |
| **类型**：character array | string |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Opacity** — 模块背景不透明度 `1`（默认）| scalar

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例：** `0.5`

#### 编程使用

|  |
| --- |
| **模块参数**：`Opacity` |
| **类型**：scalar |
| **默认值**：`1` |

### **Foreground Color** — 模块前景色 `[r g b]` 向量

模块前景色，包括文本。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义了一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### **Background Color** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义了一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### **Grid Color** — 模块网格颜色 `[r g b]` 向量

模块网格颜色。当模块显示非标量数据时显示网格。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `GridColor` 参数指定为一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`GridColor` |
| **类型**：`[r g b]` vector |
| **默认值**：`[0.502 0.502 0.502]` |
## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时被忽略。

## 版本历史

**在 R2017b 中引入**

## 描述

在仿真期间显示信号值

Display 模块连接到模型中的信号，并在仿真期间显示其值。您可以配置 Display 模块的外观和格式，使其对所显示的值具有直观意义。您可以在仿真期间编辑 Display 模块的参数。Display 模块可以显示复数、向量和二维矩阵信号。将 Display 模块与其他 Dashboard 模块一起使用，为您的模型构建交互式控件和指示器仪表板。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在该模块上并点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号（…）上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择要连接的信号。然后，将鼠标悬停在 Dashboard 模块上并点击 Done Connecting 按钮 。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 流程图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Display 模块连接到您的模型。

一个未连接的 Display 模块连接到 Ramp 模块发送到 Terminator 模块的信号。
