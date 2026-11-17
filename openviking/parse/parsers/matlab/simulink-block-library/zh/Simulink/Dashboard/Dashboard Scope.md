---
type: simulink-block
title: 'Dashboard Scope'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'dashboardscope'
documentation_source_path: 'slref/dashboardscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Dashboard Scope

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
  group: Connection Table
  block_parameter: Binding
  type: cell array of Simulink.HMI.SignalSpecification objects
  default: '[]'
- name: Line Style
  summary: 已连接信号的线型和颜色 线型和颜色选项
  group: Connection Table
  block_parameter: Colors
  type: array of structures
- name: Time Span
  summary: 时间轴跨度 auto (default) | scalar
  group: 主要参数
  block_parameter: TimeSpan
  type: string | character array
  values: '''auto'' or numeric value'
  default: '''auto'''
- name: Update Mode
  summary: 显示更新行为 Wrap (default) | Scroll
  group: 主要参数
  block_parameter: UpdateMode
  type: string | character array
  values: '''Wrap'' | ''Scroll'''
  default: '''Wrap'''
- name: Min
  summary: 垂直轴最小值 -3 (default) | scalar
  group: 主要参数
  block_parameter: YLimits
  type: 1x2 vector
  default: '[-3 3]'
- name: Max
  summary: 垂直轴最大值 3 (default) | scalar
  group: 主要参数
  block_parameter: YLimits
  type: 1x2 vector
  default: '[-3 3]'
- name: Normalize y-axis limits
  summary: 归一化 *y* 轴的选项 off (default) | on
  group: 主要参数
  block_parameter: NormalizeYAxis
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Scale axes limits at stop
  summary: 仿真停止时执行适配视图的选项 on (default) | off
  group: 主要参数
  block_parameter: ScaleAtStop
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Show "Double-click to connect" message
  summary: 连接说明的可见性 on (default) | off
  group: 主要参数
  block_parameter: ShowInitialText
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Ticks
  summary: 轴刻度位置 Outside (default) | Inside | None
  group: Display
  block_parameter: TicksPosition
  type: string | character vector
  values: '''Outside'' | ''Inside'' | ''None'''
  default: '''Outside'''
- name: Tick Labels
  summary: 刻度标签可见性 All (default) | T-Axis | Y-Axis | None
  group: Display
  block_parameter: TickLabels
  type: string | character vector
  values: '''All'' | ''T-Axis'' | ''Y-Axis'' | ''None'''
  default: '''All'''
- name: Legend
  summary: 图例位置 Top (default) | Right | Inside top | Inside right | Hide
  group: Display
  block_parameter: LegendPosition
  type: string | character vector
  values: '''Top'' | ''Right'' | ''InsideTop'' | ''InsideRight | ''Hide'''
  default: '''Top'''
- name: Horizontal
  summary: 水平网格线可见性 on (default) | off
  group: Display
  block_parameter: Grid
  type: string | character vector
  values: '''All'' | ''Horizontal'' | ''Vertical'' | ''None'''
  default: '''All'''
- name: Vertical
  summary: 垂直网格线可见性 on (default) | off
  group: Display
  block_parameter: Grid
  type: string | character vector
  values: '''All'' | ''Horizontal'' | ''Vertical'' | ''None'''
  default: '''All'''
- name: Border
  summary: 绘图边框可见性 on (default) | off
  group: Display
  block_parameter: Border
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Markers
  summary: 显示信号数据标记的选项 off (default) | on
  group: Display
  block_parameter: Markers
  type: string | character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Foreground Color
  summary: 网格线颜色 [r g b] vector
  group: Style
  block_parameter: ForegroundColor
  type: string | character vector
  values: '[r g b] vector'
- name: Background Color
  summary: 绘图区域颜色 [r g b] vector
  group: Style
  block_parameter: BackgroundColor
  type: string | character vector
  values: '[r g b] vector'
- name: Font Color
  summary: 刻度和刻度标签颜色 [r g b] vector
  group: Style
  block_parameter: FontColor
  type: '[r g b] vector'
```

### Connection Table

使用 **Connection** 表选择一个或多个要显示的信号，并配置线型和颜色。

### **Connection** — 要连接的信号及显示信号连接选项

通过在模型中选择信号来填充 **Connection** 表。要连接信号，请选中要连接的信号旁边的复选框，然后单击 **Apply**。有关连接仪表板模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

#### 提示

您可以在仿真期间将信号连接到 Dashboard Scope 模块。

#### 编程使用

要以编程方式指定一个或多个要连接到 Dashboard Scope 模块的信号，请使用 `Simulink.HMI.SignalSpecification` 对象的元胞数组。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：cell array of `Simulink.HMI.SignalSpecification` objects |
| **默认值**：`[]` |

### **Line Style** — 已连接信号的线型和颜色 线型和颜色选项

您可以使用 **Connection** 表为连接到 Dashboard Scope 模块的信号配置线型和颜色。要更改信号的线型或颜色，请在信号行对应的 **Style** 列中，单击信号外观的预览。当 **Override style and color** 清除时，**Style** 列显示 `auto` 一词，而不是线型的预览。有关详细信息，请参阅 Configure Signal Line Style and Color。

#### 编程使用

要以编程方式为已连接信号配置线型和颜色，请使用 `Colors` 参数。将 `Colors` 参数的值指定为一个结构体数组，其中每个结构体为一个信号指定样式覆盖设置、线型和线条颜色。使用 `Colors` 参数指定的设置应用于 `Binding` 参数值中相同索引处的信号。

将每个信号的线型和颜色指定为具有以下字段的结构体：

- `Auto` — 样式覆盖设置，由以下值指定：

  - `"on"` — 线型和颜色由软件自动设置
  - `"off"` — 线型和颜色由 `Color` 和 `LineStyle` 指定
- `Color` — `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。
- `LineStyle` — 字符向量，指定以下线型选项之一：

  - Solid: `'-'`
  - Dashed: `'––'`
  - Dotted: `':'`
  - Dash-dotted: `'-.'`

```
sigColors1.Color = '';
sigColors1.LineStyle = '';
sigColors1.Auto = "on";
sigColors2.Color = [0 0 1];
sigColors2.LineStyle = '--';
sigColors2.Auto = "off";
sigColors = [sigColors1 sigColors2];

set_param(blockPath,'Colors',sigColors);
```

|  |
| --- |
| **模块参数**：`Colors` |
| **类型**：array of structures |

### 主要参数

### **Time Span** — 时间轴跨度 `auto` (default) | scalar

一个有限、实数、双精度、标量值，用于设置绘图的时间跨度。

当 **Time Span** 设置为 `auto` 时，模块将其时间跨度设置为仿真停止时间。

#### 提示

当您将 **Time Span** 设置为小于仿真持续时间的值时，请使用 **Update Mode** 参数来控制当仿真时间超过指定时间跨度时显示是环绕还是滚动。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeSpan` |
| **类型**：string | character array |
| **值**：`'auto'` or numeric value |
| **默认值**：`'auto'` |

### **Update Mode** — 显示更新行为 `Wrap` (default) | `Scroll`

仿真期间显示的更新方式，指定为 `Wrap` 或 `Scroll`。

- `Wrap` — 当仿真时间达到时间跨度末尾后，显示环绕以显示传入数据。
- `Scroll` — 当仿真时间达到时间跨度末尾后，显示滚动以显示传入数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpdateMode` |
| **类型**：string | character array |
| **值**：`'Wrap'` | `'Scroll'` |
| **默认值**：`'Wrap'` |

### **Min** — 垂直轴最小值 `-3` (default) | scalar

一个有限、实数、双精度、标量值，用于设置垂直轴的最小值。

#### 提示

要在仿真停止后保持由 **Min** 和 **Max** 设置的垂直轴最小值和最大值限制，请清除 **Scale axes limits at stop**。

#### 编程使用

要以编程方式为 Dashboard Scope 模块指定 `Min` 参数，请创建一个 `1`×`2` 向量，按顺序包含 *y* 轴最小值和 *y* 轴最大值。

|  |
| --- |
| **模块参数**：`YLimits` |
| **类型**：`1x2` vector |
| **默认值**：`[-3 3]` |

### **Max** — 垂直轴最大值 `3` (default) | scalar

一个有限、实数、双精度、标量值，用于设置垂直轴的最大值。

#### 提示

要在仿真停止后保持由 **Min** 和 **Max** 设置的垂直轴最小值和最大值限制，请清除 **Scale axes limits at stop**。

#### 编程使用

要以编程方式为 Dashboard Scope 模块指定 `Max` 参数，请创建一个 `1`×`2` 向量，按顺序包含 *y* 轴最小值和 *y* 轴最大值。

|  |
| --- |
| **模块参数**：`YLimits` |
| **类型**：`1x2` vector |
| **默认值**：`[-3 3]` |

### **Normalize y-axis limits** — 归一化 *y* 轴的选项 `off` (default) | `on`

启用后，已连接的信号数据将被归一化，以在 [`0,1`] 的 *y* 轴范围内显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`NormalizeYAxis` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Scale axes limits at stop** — 仿真停止时执行适配视图的选项 `on` (default) | `off`

启用后，当仿真停止时，对绘图中显示的数据执行适配视图操作。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScaleAtStop` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Show "Double-click to connect" message** — 连接说明的可见性 `on` (default) | `off`

启用后，如果模块未连接，则显示说明文本。当模块未连接时，您可以将此参数指定为 `off` 以隐藏文本。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowInitialText` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### Display

### **Ticks** — 轴刻度位置 `Outside` (default) | `Inside` | `None`

轴刻度位置，指定为 `Outside`、`Inside` 或 `None`。

- `Outside` — 刻度绘制在 *x* 轴和 *y* 轴的外侧。
- `Inside` — 刻度绘制在 *x* 轴和 *y* 轴的内侧。
- `None` — *x* 轴或 *y* 轴上不显示刻度。

#### 编程使用

|  |
| --- |
| **模块参数**：`TicksPosition` |
| **类型**：string | character vector |
| **值**：`'Outside'` | `'Inside'` | `'None'` |
| **默认值**：`'Outside'` |

### **Tick Labels** — 刻度标签可见性 `All` (default) | `T-Axis` | `Y-Axis` | `None`

*x* 轴和 *y* 轴上刻度标签的可见性。

- `All` — 刻度标签显示在 *x* 轴和 *y* 轴上。
- `T-Axis` — 刻度标签仅显示在 *x* 轴上。
- `Y-Axis` — 刻度标签仅显示在 *y* 轴上。
- `None` — *x* 轴或 *y* 轴上不显示刻度标签。

#### 编程使用

|  |
| --- |
| **模块参数**：`TickLabels` |
| **类型**：string | character vector |
| **值**：`'All'` | `'T-Axis'` | `'Y-Axis'` | `'None'` |
| **默认值**：`'All'` |

### **Legend** — 图例位置 `Top` (default) | `Right` | `Inside top` | `Inside right` | `Hide`

您可以将图例放置在绘图区域的顶部（在绘图区域内部或外部），或放置在绘图的右侧（在绘图区域内部或外部）。您也可以隐藏图例。图例在信号名称旁边显示为每个已连接信号选择的颜色。

#### 编程使用

|  |
| --- |
| **模块参数**：`LegendPosition` |
| **类型**：string | character vector |
| **值**：`'Top'` | `'Right'` | `'InsideTop'` | `'InsideRight` | `'Hide'` |
| **默认值**：`'Top'` |

### **Horizontal** — 水平网格线可见性 `on` (default) | `off`

水平网格线的可见性。

- `on` — 水平网格线在 Dashboard Scope 上可见。
- `off` — 水平网格线不在 Dashboard Scope 上显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`Grid` |
| **类型**：string | character vector |
| **值**：`'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **默认值**：`'All'` |

### **Vertical** — 垂直网格线可见性 `on` (default) | `off`

垂直网格线的可见性。

- `on` — 垂直网格线在 Dashboard Scope 上可见。
- `off` — 垂直网格线不在 Dashboard Scope 上显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`Grid` |
| **类型**：string | character vector |
| **值**：`'All'` | `'Horizontal'` | `'Vertical'` | `'None'` |
| **默认值**：`'All'` |

### **Border** — 绘图边框可见性 `on` (default) | `off`

绘图边框可见性。

- `on` — 绘图边框在 Dashboard Scope 上显示。
- `off` — 绘图边框不在 Dashboard Scope 上显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`Border` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Markers** — 显示信号数据标记的选项 `off` (default) | `on`

启用后，将为绘制在 Dashboard Scope 模块上的信号显示数据标记。

#### 编程使用

|  |
| --- |
| **模块参数**：`Markers` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### Style

### **Foreground Color** — 网格线颜色 `[r g b]` vector

从标准颜色调色板中选择网格线的颜色，或使用介于 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型**：string | character vector |
| **值**：`[r g b]` vector |

### **Background Color** — 绘图区域颜色 `[r g b]` vector

从标准颜色调色板中选择绘图区域的颜色，或使用介于 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型**：string | character vector |
| **值**：`[r g b]` vector |

### **Font Color** — 刻度和刻度标签颜色 `[r g b]` vector

从标准颜色调色板中选择刻度和刻度标签的颜色，或使用介于 `0` 和 `255` 之间的 `RGB` 值指定自定义颜色。

#### 编程使用

将模块的 `FontColor` 参数指定为一个 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`FontColor` |
| **类型**：`[r g b]` vector |
## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仪表板模块在代码生成时被忽略。

## 版本历史

**在 R2015a 中引入**

## 描述

在仿真期间在示波器显示上追踪信号

Dashboard Scope 模块在仿真期间在示波器显示上绘制已连接的信号。您可以将 Dashboard Scope 模块与其他仪表板模块一起使用，为您的模型构建由控件和指示器组成的交互式仪表板。连接到 Dashboard Scope 模块的信号会记录到 Simulation Data Inspector，以便在仿真期间或之后进行分析。Dashboard Scope 模块可以显示 Simulink® 支持的任何数据类型的信号，包括枚举数据类型，以及来自数组或总线的最多八个信号。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在该模块上并单击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，将鼠标悬停在仪表板模块上并单击 Done Connecting 按钮 。要查看仪表板模块显示所连接模块的值，请运行仿真。

有关连接仪表板模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Dashboard Scope 模块连接到您的模型。

一个未连接的 Dashboard Scope 模块连接三个信号。

### 分析信号数据

您可以使用 Dashboard Scope 模块的子图菜单或上下文菜单来：

- 显示或隐藏数据游标。
- 按固定量缩小。
- 将鼠标交互配置为平移和选择，或在时间上、在 *y* 上、或在时间和 *y* 两者上放大。
- 在时间上、在 *y* 上、或在时间和 *y* 两者上执行适配视图。

**注意**

要使用键盘快捷键分析数据，请在 Dashboard Scope 模块中选择一个信号或轴。

要访问子图菜单，请选择 Dashboard Scope 模块，然后单击将鼠标悬停在绘图区域上时出现的三个点。

一个选中的 Dashboard Scope 模块，显示两个游标且子图菜单可见。

### 配置信号线型和颜色

您可以使用“模块参数”对话框或属性检查器中的 **Connection** 表修改连接到 Dashboard Scope 模块的信号的线条颜色和线型。要修改已连接信号的外观：

1. 在 **Connection** 表的 **Style** 列中点击信号外观预览。

   连接到 Dashboard Scope 模块的信号的线条颜色和线型选择菜单。
2. 从标准颜色调色板中选择一种颜色，或选择 **Custom** 选项卡，使用 `0` 到 `255` 之间的 `RGB` 值指定自定义颜色。
3. 在 **Style** 列中从实线、点线、虚线和点划线选项中选择线型。
4. 点击 **Set**。

当您将连接到 Dashboard Scope 模块的信号标记为信号记录时，还可以使用 Instrumentation Properties 对话框配置信号颜色和线型。在 Dashboard Scope 模块的信号颜色和线型菜单中，**Override style and color** 选项默认处于选中状态，用于指定您使用 Dashboard Scope 模块的 **Connection** 表选择的信号外观选项是否覆盖已连接信号的 instrumentation properties 中配置的信号外观选项。

当您使用“模块参数”对话框将信号连接到 Dashboard Scope 模块时，连接表会显示您连接的每个信号的默认信号颜色和线型。当您选择要连接的信号时，**Connection** 表会更新未选中信号的样式和颜色，以指示您接下来连接的信号的样式和颜色。

Dashboard Scope 模块的连接表，其中包含多个可连接信号选项以及两个已选中的信号。

### 配置复信号格式

当您将复信号连接到 Dashboard Scope 模块时，可以通过为信号指定 **Complex Format** 属性来配置信号的显示方式：

1. 将复信号标记为信号记录。
2. 右键点击复信号的记录标记，然后选择 **Properties**。
3. 指定 **Complex Format**。
4. 点击 **OK**。

当您将信号的 **Complex Format** 指定为 `Real-Imaginary` 或 `Magnitude-Phase` 时，Dashboard Scope 模块会显示信号的两个分量。实部或幅值分量使用 **Connection** 表中指示的颜色显示。虚部或相位分量使用 **Connection** 表中指示颜色的不同色调显示。
