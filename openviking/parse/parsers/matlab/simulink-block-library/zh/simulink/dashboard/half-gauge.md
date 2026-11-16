---
type: simulink-block
title: 'Half Gauge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'halfgauge'
documentation_source_path: 'slref/halfgauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Half Gauge

## 端口

R2025b 中未记录。

## 参数

### 信号

### **连接** — 要连接的信号，并显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或模块参数对话框中的 **连接** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

要使用 **连接** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器中，在 **参数** 选项卡上，点击 **连接**。要更改该模块的连接，请改为点击 **更改**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **应用**。

您也可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

### 主要

### **最小值** — 最小刻度值 `0`（默认值）| 标量

有限、实数、double、标量值，用于指定刻度的最小刻度值。最小值必须小于 **最大值** 参数的值。

#### 编程用法

要以编程方式设置 `Minimum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要为 `Tick Interval` 使用 `auto` 值，请将向量中的 `Tick Interval` 位置留空或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` 向量 |
| **默认值：** `[0 -1 100]` |

### **最大值** — 最大刻度值 `100`（默认值）| 标量

有限、实数、double、标量值，用于指定刻度的最大刻度值。最大值必须大于 **最小值** 参数的值。

#### 编程用法

要以编程方式设置 `Maximum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要为 `Tick Interval` 使用 `auto` 值，请将向量中的 `Tick Interval` 位置留空或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` 向量 |
| **默认值：** `[0 -1 100]` |

### **刻度间隔** — 主刻度标记之间的间隔 `auto`（默认值）| 标量

有限、实数、正数、整数、标量值，用于指定刻度上主刻度标记的间隔。当设置为 `auto` 时，模块会根据 **最大值** 和 **最小值** 参数的值自动调整刻度间隔。

#### 编程用法

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要为 `Tick Interval` 使用 `auto` 值，请将向量中的 `Tick Interval` 位置留空或指定 `-1`。

|  |
| --- |
| **模块参数：** `Limits` |
| **类型：** `1x3` 向量 |
| **默认值：** `[0 -1 100]` |

### **刻度颜色** — 仪表刻度上用于刻度范围的颜色指示

刻度上值范围的颜色规范。点击 **+** 按钮添加刻度颜色。对于添加的每种颜色，请指定要在其中显示该颜色的范围的最小值和最大值。

#### 编程用法

要以编程方式指定 `Scale Colors` 参数，请使用包含以下字段的结构体数组：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — 由 `1`×`3` 的 `double` 值组成的向量，值介于 `0` 和 `1` 之间，用于以 `[r g b]` 形式指定范围的颜色

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
| **类型：** 结构体数组 |
| **默认值：** `0x1` 结构体数组 |

### **标签** — 模块标签位置 `Top`（默认值）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** 字符向量 |
| **值：** `'Top'` | `'Bottom'` | `'Hide'` |
| **默认值：** `'Top'` |

### **刻度方向** — 仪表刻度方向 `Clockwise`（默认值）| `Counterclockwise`

仪表刻度方向。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleDirection` |
| **类型：** 字符向量 |
| **值：** `'Clockwise'` | `'Counterclockwise'` |
| **默认值：** `'Clockwise'` |

### 格式

### **不透明度** — 模块背景不透明度 `1`（默认值）| 标量

模块背景不透明度，指定为 0 和 1 之间的标量值。

**示例：** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** 标量 |
| **默认值：** `1` |

### **前景色** — 模块前景色 `[r g b]` 向量

模块前景色，不包括文本。**前景色** 应用于刻度和模块名称。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。要指定模块文本的颜色，请使用 **字体颜色**。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** 字符向量 | 字符串 |
| **值：** `[r g b]` 向量 |

### **背景色** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** 字符向量 | 字符串 |
| **值：** `[r g b]` 向量 |

### **字体颜色** — 模块字体颜色 `[r g b]` 向量

模块字体颜色。**字体颜色** 应用于刻度上的刻度标签。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `FontColor` 参数指定为一个 `1`×`3` `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `FontColor` |
| **类型：** `[r g b]` 向量 |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时将被忽略。

## 版本历史

**在 R2015a 中引入**

## 描述

在半圆形刻度上显示输入值

Half Gauge 模块在仿真期间在半圆形刻度上显示连接的信号。您可以将 Half Gauge 模块与其他 Dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式仪表盘。Half Gauge 模块在整个仿真过程中提供连接信号的瞬时值指示。您可以修改 Half Gauge 模块的范围以适合您的数据。您还可以自定义 Half Gauge 模块的外观，以提供有关信号的更多信息。例如，您可以对符合规格和不符合规格的范围进行颜色编码。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击连接按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击连接按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择要连接的信号。然后，暂停在 Dashboard 模块上，并点击完成连接按钮。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

您也可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

此动画显示如何将 Half Gauge 模块连接到您的模型。

未连接的 Half Gauge 模块连接到 Sine Wave 模块发送到 Display 模块的信号。
