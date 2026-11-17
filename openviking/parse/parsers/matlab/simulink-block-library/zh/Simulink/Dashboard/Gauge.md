---
type: simulink-block
title: 'Gauge'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'gauge'
documentation_source_path: 'slref/gauge.html'
language: zh-CN
chinese_source: worker-translation
---

# Gauge

## 端口

R2025b 中未记录。

## 参数

### Signal

### **Connection** — 要连接的信号及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.SignalSpecification` |
| **默认值**：`[]` |

### 主要参数

### **Minimum** — 最小刻度值 `0`（默认）| 标量

有限、实数、双精度、标量值，用于指定刻度的最小刻度值。最小值必须小于 **Maximum** 参数的值。

#### 编程使用

要以编程方式设置 `Minimum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将向量中 `Tick Interval` 的位置留空或指定 `-1`。

|  |
| --- |
| **模块参数**：`Limits` |
| **类型**：`1x3` vector |
| **默认值**：`[0 -1 100]` |

### **Maximum** — 最大刻度值 `100`（默认）| 标量

有限、实数、双精度、标量值，用于指定刻度的最大刻度值。最大值必须大于 **Minimum** 参数的值。

#### 编程使用

要以编程方式设置 `Maximum` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将向量中 `Tick Interval` 的位置留空或指定 `-1`。

|  |
| --- |
| **模块参数**：`Limits` |
| **类型**：`1x3` vector |
| **默认值**：`[0 -1 100]` |

### **Tick Interval** — 主刻度线之间的间隔 `auto`（默认）| 标量

有限、实数、正数、整数、标量值，用于指定刻度上主刻度线的间隔。当设置为 `auto` 时，模块会根据 **Maximum** 和 **Minimum** 参数的值自动调整刻度间隔。

#### 编程使用

要以编程方式设置 `Tick Interval` 参数，请使用一个 `1`×`3` 向量，按顺序包含 `Minimum`、`Tick Interval` 和 `Maximum` 参数的值。要将 `Tick Interval` 设为 `auto` 值，请将向量中 `Tick Interval` 的位置留空或指定 `-1`。

|  |
| --- |
| **模块参数**：`Limits` |
| **类型**：`1x3` vector |
| **默认值**：`[0 -1 100]` |

### **Scale Colors** — 仪表刻度上刻度范围的颜色指示

刻度上值范围的颜色规格。按 **+** 按钮添加刻度颜色。对于添加的每种颜色，指定要显示该颜色的范围的最小值和最大值。

#### 编程使用

要以编程方式指定 `Scale Colors` 参数，请使用结构体数组，其字段包括：

- `Min` — 刻度上颜色范围的最小值
- `Max` — 刻度上颜色范围的最大值
- `Color` — 由 `0` 到 `1` 之间的 `double` 值组成的 `1`×`3` 向量，以 `[r g b]` 形式指定该范围的颜色

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
| **模块参数**：`ScaleColors` |
| **类型**：structure array |
| **默认值**：`0x1` struct array |

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |

### **Scale Direction** — 仪表刻度方向 `Clockwise`（默认）| `Counterclockwise`

仪表刻度方向。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScaleDirection` |
| **类型**：character vector |
| **值**：`'Clockwise'` | `'Counterclockwise'` |
| **默认值**：`'Clockwise'` |

### Format

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

模块背景不透明度，指定为 0 到 1 之间的标量值。

**Example:** `0.5`

#### 编程使用

|  |
| --- |
| **模块参数**：`Opacity` |
| **类型**：scalar |
| **默认值**：`1` |

### **Foreground Color** — 模块前景色 `[r g b]` 向量

模块前景色，不包括文本。**Foreground Color** 应用于刻度和模块名称。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。要指定模块文本的颜色，请使用 **Font Color**。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### **Background Color** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### **Font Color** — 模块字体颜色 `[r g b]` 向量

模块字体颜色。**Font Color** 应用于刻度上的刻度标签。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `FontColor` 参数指定为一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`FontColor` |
| **类型**：`[r g b]` vector |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2015a 中引入**

## 描述

在圆形刻度上显示信号值

Gauge 模块在仿真期间在圆形刻度上显示所连接的信号。您可以将 Gauge 模块与其他 Dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式仪表板。Gauge 模块在整个仿真过程中提供所连接信号的瞬时值指示。您可以修改 Gauge 模块的范围以适合您的数据。您还可以更改表盘的外观，以提供有关信号的更多信息。例如，您可以对符合规格和超出规格的范围进行颜色编码。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号（…）上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，将鼠标悬停在 Dashboard 模块上，并点击 Done Connecting 按钮 。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Gauge 模块连接到您的模型。

一个未连接的 Gauge 模块连接到 Sine Wave 模块发送到 Display 模块的信号。
