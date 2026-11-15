---
type: simulink-block
title: 'Time Scope'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Scopes and Data Logging'
documentation_page: 'timescopeblock'
documentation_source_path: 'ref/timescopeblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Time Scope

## 端口

### 输入

### **Port\_1** — 要可视化的信号 scalar | vector | matrix | array | bus | nonvirtual bus

连接要可视化的信号。最多可以有 96 个输入端口。输入信号可以具有以下特征：

- **类型** — Continuous（sample-based）或 discrete（sample-based 和 frame-based）。
- **数据类型** — Simulink 支持的任何数据类型。请参阅 Data Types Supported by Simulink (Simulink)。

  此模块接受定点输入，但为显示将其转换为 `double`。
- **维度** — Scalar、one dimensional (vector)、two dimensional (matrix) 或 multidimensional (array)。根据维度显示一个信号内的多个通道。请参阅 Signal Dimensions (Simulink) 和 Determine Signal Dimensions (Simulink)。

#### 输入限制

- 当输入为常量信号时，示波器绘制单个点。
- 当信号值为 `NaN` 时，示波器在显示中显示间隙。
- 当在示波器中可视化多个基于帧的信号时，帧大小为 1 的信号的某些样本可能不会显示。要可视化这些信号，请将帧大小为 1 的信号移到单独的示波器。

#### 总线支持

您可以将 nonvirtual bus 和总线信号数组连接到示波器。要显示总线信号，请使用 normal 或 accelerator 仿真模式。示波器按元素在总线中出现的顺序（从上到下）显示每个总线元素信号。嵌套总线元素会被展平。

要使用示波器记录 nonvirtual bus 信号，请将 **保存格式** 参数设置为 `Dataset`。您可以使用任何 **保存格式** 来记录 virtual bus 信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** Yes

## 参数

有关如何配置 Scope 和使用工具条的信息，请参阅 Configure Time Scope Block。

### Scope 选项卡

Scope 模块和 Time Scope 模块的 Scope 选项卡。

#### 设置 > 常规

### **仿真开始时打开** — 指定示波器何时打开 off（Scope 默认） | on（Time Scope 默认）

选择此参数以在仿真开始时打开示波器。

#### 编程方式使用

请参阅 `OpenAtSimulationStart` (Simulink)。

### **显示完整路径** — 在示波器标题栏显示模块路径 off（默认） | on

选择此参数以在模块名称之外还显示模块路径。

### **输入端口数量** — 示波器上的输入端口数量 `1`（默认） | [1 96] 范围内的正整数

将示波器上的输入端口数量指定为 [1 96] 范围内的正整数。

#### 编程方式使用

请参阅 `NumInputPorts` (Simulink)。

### **显示网格** — 显示网格的维度 [1, 1]（默认） | 两元素数值向量

将显示网格的维度指定为两元素数值向量，其中每个元素大于 0 且小于或等于 16。

#### 编程方式使用

请参阅 `LayoutDimensions` (Simulink)。

### **输入处理** — 基于采样或基于帧的处理 `Elements as channels (sample based)`（Scope 默认） | `Columns as channels (frame based)`（Time Scope 默认）

指定模块执行基于采样还是基于帧的处理。

- `Elements as channels (sample based)` –– 将输入的每个元素作为独立通道处理。
- `Columns as channels (frame based)` –– 将输入的每一列作为独立通道处理。基于帧的处理仅适用于离散输入信号。

当您更改 **输入处理** 参数的设置时，示波器会清除信号数据和测量数据（如果有）。重新运行仿真以使用新设置绘制信号数据。*（自 R2025a 起）*

**注意**

基于帧的处理需要 DSP System Toolbox 许可证。有关详细信息，请参阅 Sample- and Frame-Based Concepts。

#### 编程方式使用

请参阅 `FrameBasedProcessing` (Simulink)。

### **最大化坐标轴** — 最大化绘图大小 `Off`（Scope 默认） | `Auto`（Time Scope 默认） | `On`

- `Auto` –– 如果未指定 **标题** 和 **Y 轴标签** 属性，则最大化所有绘图。
- `On` –– 最大化所有绘图。**标题** 和 **Y 轴标签** 中的值会隐藏。
- `Off` –– 不最大化绘图。

#### 编程方式使用

请参阅 `MaximizeAxes` (Simulink)。

#### 设置 > 时间

### **采样时间** — 示波器更新之间的仿真间隔 `-1`（用于继承）（默认） | 正实数

指定示波器显示更新之间的时间间隔。此属性不适用于 Floating Scope 和 Scope Viewer。有关示波器采样时间的更详细说明，请参阅 Sample Time with Scope Blocks (Simulink)。

#### 编程方式使用

请参阅 `SampleTime` (Simulink)。

### **时间范围** — 要显示的 *x* 轴长度 `Auto`（默认） | `One frame period` | `<user-defined>`

将要显示的 *x* 轴长度指定为以下之一：

- `Auto` — 仿真开始和停止时间之间的差。

  模块使用 **时间显示偏移** 和 **时间范围** 参数计算时间范围的开始和结束时间。例如，如果将 **时间显示偏移** 设置为 `10`，将 **时间范围** 设置为 `20`，则示波器将时间范围设置为 `10` 到 `30`。
- `One frame period` — 使用 Time Scope 模块输入信号的帧周期。仅当您将 **输入处理** 参数设置为 `Columns as channels (frame based)` 时，此选项才可用。
- `<user-defined>` — 输入小于总仿真时间的任意值。

#### 编程方式使用

请参阅 `TimeSpan` (Simulink)。

### **溢出操作** — 显示超出可见 *x* 轴的数据 `Wrap`（默认） | `Scroll`

指定如何显示超出可见 *x* 轴范围的数据。

仅当大型模型或小步长导致绘图缓慢时，您才能看到此选项的效果。

- `Wrap` — 从左到右绘制一整屏数据，清除屏幕，然后重新从左开始绘制数据。
- `Scroll` — 当新数据绘制在右侧时，将数据向左移动。此模式图形密集，可能影响运行时性能。

#### 编程方式使用

请参阅 `TimeSpanOverrunAction` (Simulink)。

### **时间单位** — *x* 轴单位 `None`（Scope 默认） | `Metric (based on Time Span)`（Time Scope 默认） | `Seconds`

将 *x* 轴单位指定为以下选项之一：

- `Metric (based on Time Span)` — 基于 **时间范围** 的长度显示时间单位。
- `Seconds` — 以秒为单位显示时间。
- `None` — 不显示时间单位。

#### 编程方式使用

请参阅 `TimeUnits` (Simulink)。

### **时间显示偏移** — *x* 轴偏移 `0`（默认） | 标量 | 向量

按指定的时间值偏移 *x* 轴，该值指定为实数或实数向量。

对于具有多个通道的输入信号，您可以输入标量或向量：

- Scalar — 按相同时间值偏移输入信号的所有通道。
- Vector — 独立偏移各通道。

#### 编程方式使用

请参阅 `TimeDisplayOffset` (Simulink)。

### **T 轴和刻度标签** — *x* 轴（时间）和刻度标签的显示 `Bottom displays only`（Scope 默认） | `All`（Time Scope 默认） | `None`

指定 *x* 轴（时间）和刻度标签的显示方式：

- `All` — 在所有 *y* 轴上显示 *x* 轴标签。
- `None` — 不显示标签。选择 `None` 还会清除 **显示时间轴标签** 参数。
- `Bottom displays only` — 在底部 *y* 轴上显示 *x* 轴标签。

#### 依赖关系

要启用此参数：

- 选择 **显示时间轴标签**。
- 将 **最大化坐标轴** 设置为 `Off`。

#### 编程方式使用

请参阅 `TimeAxisLabels` (Simulink)。

### **时间偏移视图** — 在状态栏上显示时间偏移 on（默认） | off

选择此参数以在状态栏上显示时间偏移。

### **显示时间轴标签** — 显示或隐藏 *x* 轴标签 off（Scope 默认） | on（Time Scope 默认）

选择此参数以显示活动显示的 *x* 轴标签。

#### 依赖关系

要启用此参数，请将 **T 轴和刻度标签** 设置为 `All` 或 `Bottom displays only`。

#### 编程方式使用

请参阅 `ShowTimeAxisLabel` (Simulink)。

#### 设置 > 坐标轴缩放

### **缩放 Y 轴范围** — *y* 轴缩放模式 `Manual`（默认） | `Auto` | `After N Updates`

将 *y* 轴缩放模式指定为以下之一：

- `Manual` — 手动缩放 *y* 轴范围。
- `Auto` — 在仿真期间和之后缩放 *y* 轴范围。选择此选项会显示 **Y 轴范围不收缩** 参数。如果您希望 y 轴范围随信号最大值增大和减小，请将 **缩放 Y 轴范围** 设置为 `Auto`，并清除 **Y 轴范围不收缩** 参数。
- `After N Updates` — 在 **更新次数** 参数中指定的时间步数（默认 `10`）之后缩放 *y* 轴。每次运行仅缩放一次。

#### 编程方式使用

请参阅 `AxesScaling` (Simulink)。

### **Y 轴范围不收缩** — 允许 *y* 轴范围限制增大 on（默认） | off

选择此参数以允许 *y* 轴范围限制在仿真期间增大。

#### 依赖关系

要使用此参数，请将 **缩放 Y 轴范围** 设置为 `Auto`。

### **更新次数** — 缩放前的更新次数 `10`（默认） | 整数

设置此属性以延迟自动缩放 *y* 轴。

#### 依赖关系

要使用此参数，请将 **缩放 Y 轴范围** 设置为 `After N Updates`。

#### 编程方式使用

请参阅 `AxesScalingNumUpdates` (Simulink)。

### **停止时缩放 Y 轴范围** — 仿真停止时缩放 *y* 轴范围 on（默认） | off

选择此参数时，示波器仅在仿真停止时缩放 *y* 轴范围。清除此参数时，示波器连续缩放 *y* 轴范围。

### **Y 轴数据范围 (%)** — 用于绘图的 *y* 轴百分比 `80`（默认） | [1,100] 之间的整数

指定用于绘制数据的 *y* 轴范围的百分比。如果将此参数设置为 `100`，绘制的数据将使用整个 *y* 轴范围。

### **Y 轴对齐** — 沿 *y* 轴对齐 `Center`（默认） | `Top` | `Bottom`

当 **Y 轴数据范围 (%)** 设置为小于 100% 时，指定沿 *y* 轴数据范围对齐绘制数据的位置。

- `Top` — 将信号与 *y* 轴范围的最大值对齐。
- `Center` — 将信号在最小值和最大值之间居中。
- `Bottom` — 将信号与 *y* 轴范围的最小值对齐。

### **缩放 X 轴范围** — 缩放 *x* 轴范围限制 off（默认） | on

缩放 *x* 轴范围以适合所有信号值。如果 **缩放 Y 轴范围** 设置为 `Auto`，则缩放当前位于坐标轴内的数据，而不是数据缓冲区中的整个信号。

### **X 轴数据范围 (%)** — 用于绘图的 *x* 轴百分比 `100`（默认） | [1,100] 范围内的整数

指定要绘制数据的 *x* 轴范围的百分比。例如，如果将此参数设置为 `100`，绘制的数据将使用整个 *x* 轴范围。

#### 依赖关系

要启用此参数，请选择 **缩放 X 轴范围**。

### **X 轴对齐** — 沿 *x* 轴对齐 `Center`（默认） | `Left` | `Right`

当 **X 轴数据范围 (%)** 设置为小于 100% 时，指定沿 *x* 轴数据范围对齐绘制数据的位置。

- `Right` — 将信号与 *x* 轴范围的最大值对齐。
- `Center` — 将信号在最小值和最大值之间居中。
- `Left` — 将信号与 *x* 轴范围的最小值对齐。

#### 依赖关系

要启用此参数，请选择 **缩放 X 轴范围**。

#### 设置 > 记录

### **将数据点限制为最后**、**将帧限制为最后** — 限制缓冲的数据点或帧 `off`（默认） | `on`

选择此属性以限制示波器内部保存的数据。当您选择此属性并将 **输入处理** 参数设置为：

- `Elements as channels (sample based)` –– 示波器将最后 *n* 个数据点保存到 **变量名称** 中指定的 MATLAB® 变量。在此设置下，此属性的名称为 **将数据点限制为最后**。
- `Columns as channels (frame based)` –– 示波器将最后 *n* 个数据帧保存到 **变量名称** 中指定的 MATLAB 变量。在此设置下，此属性的名称为 **将帧限制为最后**。

*n* 是您在 **最大点数** 参数中指定的标量值。

当您选择此参数时，示波器可以绘制短于仿真整个时间范围的信号，例如采样时间很小时。如果示波器仅绘制信号的一部分，请考虑增加要保存的数据点数量。

当您清除此属性时，示波器保存所有数据。仿真完成后，您可以在示波器中可视化整个数据。对于 **停止时间** 设置为 `inf` 的仿真，请考虑选择此属性。

**注意**

如果您不选择此属性，并且采样率高或仿真时间长，则可能会遇到内存或系统性能问题。

#### 编程方式使用

请参阅 `DataLoggingLimitDataPoints` (Simulink)。

### **最大点数** — 要保存的最大数据点数 `5000` | 正整数

将要保存的最大数据点数 *n* 指定为正整数。示波器将最后 *n* 个数据点保存到 **变量名称** 中指定的 MATLAB 变量。

#### 依赖关系

要启用此参数，请选择 **将数据点限制为最后** 或 **将帧限制为最后** 参数。

#### 编程方式使用

请参阅 `DataLoggingMaxPoints` (Simulink)。

### **抽取**、**抽取帧** — 减少要显示和保存的示波器数据量 `off`（默认） | `on`

选择此属性以每第 *N* 个数据点或帧绘制并记录（保存）示波器数据，其中 *N* 是您在 **抽取值** 参数中指定的抽取因子。

当您选择此属性并在 **抽取值** 参数中指定标量值时，示波器将限制绘制并保存到 **变量名称** 中指定的 MATLAB 变量的数据值。

当您将 **输入处理** 参数设置为：

- `Elements as channels (sample based)` –– 示波器每第 *N* 个数据点绘制并记录数据。此属性的名称为 **抽取**。
- `Columns as channels (frame based)` –– 示波器每第 *N* 帧绘制并记录数据。此属性的名称为 **抽取帧**。

当您清除此属性时，示波器保存所有示波器数据。

#### 编程方式使用

请参阅 `DataLoggingDecimateData` (Simulink) 和 `DataLoggingDecimation` (Simulink)。

### **抽取值** — 抽取值 `2`（默认） | 正整数

指定示波器每第 *N* 个数据点或帧保存或记录数据，其中 *N* 是您在此参数中指定的值。

值 `1` 会缓冲所有数据值。

#### 依赖关系

要启用此参数，请选择 **抽取** 或 **抽取帧**。

#### 编程方式使用

请参阅 `DataLoggingDecimateData` (Simulink) 和 `DataLoggingDecimation` (Simulink)。

### **将数据记录到工作区** — 将数据保存到 MATLAB 工作区 `off`（默认） | `on`

选择此参数以启用记录并将记录的数据保存到 MATLAB 工作区。当您选择此参数时，示波器还会启用 **变量名称** 和 **保存格式** 参数。此参数不适用于 Floating Scope 和 Scope Viewer。

有关使用 Scope 模块将信号保存到 MATLAB 工作区的示例，请参阅 Save Simulation Data Using Scope Block (Simulink)。

#### 编程方式使用

请参阅 `DataLogging` (Simulink)。

### **变量名称** — 保存的数据变量名称 `ScopeData`（默认） | 字符向量 | 字符串标量

指定用于在 MATLAB 工作区中保存示波器数据的变量名称。此参数不适用于 Floating Scope 和 Scope Viewer。

#### 依赖关系

要启用此参数，请选择 **将数据记录到工作区**。

#### 编程方式使用

请参阅 `DataLoggingVariableName` (Simulink)。

### **保存格式** — MATLAB 变量格式 `Dataset`（默认） | `Structure With Time` | `Structure` | `Array`

选择用于将数据保存到 MATLAB 工作区的 MATLAB 变量格式。此参数不适用于 Floating Scope 和 Scope Viewer。

- `Dataset` — 将数据保存为 `Dataset` (Simulink) 对象，默认情况下为 `timeseries` 对象。
- `Structure With Time` — 将数据保存为带有关联时间信息的结构体。
- `Structure` — 将数据保存为结构体。
- `Array` — 将数据保存为带有关联时间信息的数组。此格式不支持可变大小数据。

#### 依赖关系

要启用此参数，请选择 **将数据记录到工作区**。

#### 编程方式使用

请参阅 `DataLoggingSaveFormat` (Simulink)。

#### 设置 > 坐标轴样式

### **绘图类型** — 绘图类型 `Auto`（Scope 默认） | `Line`（Time Scope 默认） | `Stairs` | `Stem`

将绘图类型指定为以下之一：

- `Auto` –– 对于连续信号，绘图类型为线图；对于离散信号，为阶梯图；对于 Simulink 消息信号，为杆图。
- `Line` –– 线图。
- `Stairs` –– 阶梯图。阶梯图仅由水平线和垂直线组成。每条水平线表示离散采样周期的信号值，并连接到两条垂直线。每条垂直线表示在特定采样时间发生的信号值变化。
- `Stem` –– 杆图，显示为输入值处的圆点，并带有到 *x* 轴的垂直线。

### **坐标轴背景** — 单个显示的背景颜色 black（默认） | 颜色

选择示波器显示的背景颜色。

### **坐标轴和网格** — 单个显示的坐标轴、网格和标签颜色 gray（默认） | 颜色

选择单个显示的坐标轴、网格和标签颜色。

### **示波器背景** — 示波器窗口的背景颜色 black（默认） | 颜色

选择示波器窗口的背景颜色。

### **复制时保留颜色** — 复制示波器时保留颜色 off（默认） | on

选择此参数以在将示波器显示复制到剪贴板时保留颜色。未选择此参数时，示波器会将示波器颜色更改为适合打印（白色背景、可见线条）。要在复制时保留示波器上的现有颜色，请选择此参数。

#### 设置 > 显示属性

### **活动显示** — 活动显示 `1`（默认） | 正整数

选择根据 **显示属性** > **线样式**、**Y 轴** 和 **显示** 中的设置进行更新的显示。

使用对应于按列放置索引的正整数指定所需显示。对于具有多列和多行的布局，显示编号先向下映射，然后横向映射。

#### 依赖关系

要启用此参数，请将显示网格设置为具有多个显示，即在 **设置** > **常规** 下将 **显示网格** 设置为两元素数值向量，其中至少一个值大于 1。

#### 编程方式使用

请参阅 `ActiveDisplay` (Simulink)。

**注意**

所有 **线样式** 属性仅影响您通过 **活动显示** 参数选择的活动显示。

#### 设置 > 线样式

### **线** — 要更改的线 `Channel 1`（默认） | 通道名称

选择活动线以设置线样式属性。

### **样式** — 线样式 `-`（默认） | `:` | `-`. | `--` | `None`

选择使用 **线** 参数选择的活动线的线样式。

### **宽度** — 线宽 `1.5`（默认） | `0.5` | `1` | `2` | `3` | `4` | `6` | ...

指定使用 **线** 参数选择的活动线的线宽。

### **标记** — 数据点标记样式 `none`（默认） | `o` | `+` | `x` | ...

为使用 **线** 参数选择的活动线指定数据点标记。此参数类似于绘图的 `'Marker'` 属性。您可以从下拉列表中选择任何标记符号。

### **颜色** — 线颜色 yellow（默认） | 颜色选择器

指定使用 **线** 参数选择的活动线的线颜色。

**可调:** Yes

### **线可见** — 线可见性 on（默认） | off

在绘图上显示或隐藏信号。

选择此参数以在绘图上显示信号。如果清除此参数，您选择的信号将不再可见。

**注意**

所有 **Y 轴** 属性仅影响您通过 **活动显示** 参数选择的活动显示。

#### 设置 > Y 轴

### **Y 轴标签** — Y 轴标签 none（Scope 默认） | `Amplitude`（Time Scope 默认） | 字符向量 | 字符串标量

指定要在 *y* 轴上显示的文本。要显示信号单位，请将 `(%<SignalUnits>)` 添加到标签。在仿真开始时，Simulink 会将 `(%SignalUnits)` 替换为与信号关联的单位。

**示例:** 对于单位为 `m/s` 的速度信号，请输入 `Velocity (%<SignalUnits>)`。

#### 依赖关系

如果您在 **显示** 设置下选择 **按幅值-相位绘图** 参数，则此参数不适用。*y* 轴标记为 `Magnitude` 和 `Phase`。

#### 编程方式使用

请参阅 `YLabel` (Simulink)。

### **Y 轴范围** — Y 轴范围 [`-10` `10`]（默认） | 两元素数值向量

将 *y* 轴范围指定为两元素数值向量。

**可调:** Yes

#### 依赖关系

如果您选择 **按幅值-相位绘图**，此属性仅适用于幅值图。相位图的 *y* 轴范围始终为 `[-180 180]`。

#### 编程方式使用

请参阅 `YLimits` (Simulink)。

**注意**

所有 **显示** 属性仅影响您通过 **活动显示** 参数选择的活动显示。

#### 设置 > 显示

### **标题** — 显示名称 `%<SignalLabel>`（默认） | 字符向量 | 字符串标量

指定显示的标题。默认值 `%<SignalLabel>` 使用输入信号名称作为标题。

#### 编程方式使用

请参阅 `Title` (Simulink)。

### **显示图例** — 显示信号图例 off（默认） | on

选择此参数以显示信号图例。图例中列出的名称是模型中的信号名称。对于具有多个通道的信号，示波器会在信号名称后附加通道索引。连续信号在其名称前具有直线，离散信号具有阶梯形线。

在图例中，您可以控制哪些信号可见。此控制等效于在 **线样式** 属性中更改可见性。在示波器图例中，单击信号名称以在示波器中隐藏该信号。要显示该信号，请再次单击信号名称。要仅显示一个信号，请右键单击信号名称，这会隐藏所有其他信号。要显示所有信号，请按 **Esc**。

**注意**

图例仅显示前 20 个信号。任何其他信号无法从图例中控制。

#### 编程方式使用

请参阅 `ShowLegend` (Simulink)。

### **显示网格** — 显示内部网格线 on（默认） | off

选择此参数以显示内部网格线。

#### 编程方式使用

请参阅 `ShowGrid` (Simulink)。

### **按幅值-相位绘图** — 将显示拆分为幅值和相位图 off（默认） | on

选择此参数以将显示拆分为幅值和相位图。

- On — 显示幅值和相位图。如果信号为实数，示波器绘制信号绝对值作为幅值。对于正值，相位为 0 度；对于负值，相位为 180 度。此功能对于复值输入信号很有用。如果输入是实值信号，选择此参数会返回信号绝对值作为幅值。
- Off — 显示信号图。如果信号为复数，示波器在同一 *y* 轴上绘制实部和虚部。

#### 编程方式使用

请参阅 `PlotAsMagnitudePhase` (Simulink)。

#### 显示网格

### **显示网格** — 显示布局 1 乘 1 显示（默认） | `m` 乘 `n` 坐标轴的排列

指定显示的布局。打开类似于示波器布局的网格选择器。布局最多可以有 16 行和 16 列。使用网格选择器，您可以选择最大 5 乘 5 的布局。要选择大于 5 乘 5 的布局：

- 在工具条的 **Scope** 选项卡中，将 **设置** > **常规** 下的 **显示网格** 设置为两元素数值向量，其中每个元素大于 0 且小于或等于 16。例如，将 **显示网格** 设置为 [`2` `1`] 会将布局更改为 2 乘 1。
- 使用 `TimeScopeConfiguration` (Simulink) 对象的 `LayoutDimensions` 属性。

将布局从一个显示更改为两个显示的动画 GIF

如果显示数量等于端口数量，来自每个端口的信号将出现在单独的显示上。如果显示数量小于端口数量，来自额外端口的信号将出现在最后一个显示上。对于具有多列和多行的布局，端口先向下映射，然后横向映射。如果显示数量大于端口数量，示波器会创建空图块。

#### 编程方式使用

请参阅 `LayoutDimensions` (Simulink)。

#### 停靠

### **停靠** — 将示波器停靠到示波器容器 **Dock Scope**（默认） | **Dock All Scopes**

在 **Scope** 选项卡中单击 **Dock** 或 **Dock Scope**，将当前活动的示波器添加到示波器容器。单击 **Dock All Scopes**，将当前模型中所有已打开的示波器添加到示波器容器。

有关示波器容器的详细信息，请参阅 Scope Window Management。

### **取消停靠** — 从示波器容器取消停靠示波器 **Undock**（默认） | **Undock All**

在示波器容器的 **Home** 选项卡中单击 **Undock**，将当前活动的示波器从容器中移出到单独的独立窗口。单击 **Undock All**，将所有示波器从容器中移出到单独的独立窗口。

有关示波器容器的详细信息，请参阅 Scope Window Management。

#### 依赖关系

此参数仅在示波器容器的 **Home** 选项卡上可用。

### **打开时将新示波器停靠** — 打开时将新示波器添加到容器 off（默认） | on

选择此参数以将新打开的示波器（在当前 MATLAB 会话中之前未打开过）自动添加到现有示波器容器。

有关示波器容器的详细信息，请参阅 Scope Window Management。

#### 依赖关系

此参数仅在示波器容器的 **Home** 选项卡上可用。要访问此参数，请单击示波器容器 **Home** 选项卡下 **Dock All** 的下拉箭头。

### 测量选项卡

**测量** 选项卡包含示波器支持的所有信号测量的设置。测量面板出现在示波器窗口底部。要打开测量面板，必须先在 **测量** 选项卡中启用相应的测量。

Scope 模块和 Time Scope 模块的测量选项卡。

有关测量的详细信息，请参阅以下页面：

- Triggers — 设置触发器以同步重复信号并在事件发生时暂停显示。
- Cursor Measurements — 使用垂直和水平游标测量信号值。
- Signal Statistics — 显示所选信号的最大值、最小值、峰峰值差、均值、中位数和 RMS 值。
- Peak Finder — 查找最大值，显示出现这些最大值的 *x* 轴值。
- Bilevel Measurements — 测量转换、过冲、下冲和周期。

## 所属库

DSP System Toolbox / Sinks DSP System Toolbox HDL Support / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `busa` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |
|  |  |
| --- | --- |
| a Virtual bus 不受支持。Nonvirtual bus 仅在 normal 和 accelerator 模式仿真中受支持。Nonvirtual bus 的数据记录仅支持 dataset 格式。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可见性，但不包含在生成的代码中。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

此模块可用于生成代码的系统中的仿真可见性，但不包含在生成的代码中。

## 版本历史

**在 R2015b 中引入**

### R2025a: 改进的 Scope 和新的示波器容器，可将所有示波器停靠在一个窗口中

Simulink 中的 Simulink Scope (Simulink)、Time Scope 和 Floating Scope and Scope Viewer (Simulink) 模块具有新的用户界面，您可以使用该界面访问示波器的设置和测量。示波器现在响应更快，性能得到改进。使用新的示波器容器将多个示波器窗口停靠到单个窗口，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

Scope、Time Scope 和 Floating Scope and Scope Viewer 模块的关键改进包括：

- 精简的用户界面：可从新示波器工具条的 **Scope** 选项卡轻松访问所有常规示波器设置，并从 **测量** 选项卡访问所有测量设置。
- 新的示波器容器：单个窗口为模型中的所有示波器显示提供统一视图，使您能够在一个位置管理和组织多个示波器。
- 更新的设置面板：更新后的面板整合了示波器的所有常规和样式设置。要打开该面板，请单击工具条 **Scope** 选项卡中的 **Settings**。

### R2025a: 已移除通过 MATLAB Graphics API 访问 Time Scope 的功能

Time Scope 模块的底层图形已更改。您无法通过 MATLAB Graphics API 访问或修改 Time Scope 模块。

要在 MATLAB Graphics 窗口中显示示波器数据，请使用 Time Scope 模块工具条 **Scope** 选项卡中的 **Print to Figure** 功能。

### R2025a: 已移除将 Scope 停靠到 MATLAB 桌面的功能

已移除将 Simulink Scope (Simulink)、Time Scope 和 Floating Scope and Scope Viewer (Simulink) 停靠到 MATLAB 桌面的功能。请改用新的示波器容器。有关详细信息，请参阅 Scope Window Management。

如果您有在 R2024b 或更早版本中创建的模型，并且其中有四个或更多已打开的示波器，并且您在 R2025a 中打开该模型，则已打开的示波器会自动停靠在示波器容器窗口中。

## 描述

显示并分析仿真期间生成的信号，并将信号数据记录到 MATLAB

Simulink® Scope 模块和 DSP System Toolbox™ Time Scope 模块显示时域信号。

这两个模块具有相同的功能，但默认设置不同。Time Scope 针对离散时间处理进行了优化。Scope 针对一般时域仿真进行了优化。有关并排比较，请参阅 Simulink Scope Block Versus DSP System Toolbox Time Scope Block (Simulink)。

**Scope 选项卡**

此屏幕截图突出了示波器窗口的重要方面。

**示波器显示功能：**

- 仿真控制 — 使用 **Run**、**Step Forward** 和 **Step Backward** 工具栏按钮从 Scope 窗口运行和调试模型。
- 多个信号 — 使用多个输入端口在同一显示上绘制多个信号。
- 多个显示 — 在多个子图上显示信号。所有子图的 *y* 轴在 *x* 轴上具有共同的时间范围。使用工具条 **Scope** 选项卡中的 **Display Grid** 参数控制子图的布局。
- 修改参数 — 在仿真之前和期间修改示波器参数值。
- 坐标轴自动缩放 — 在仿真期间或结束时自动缩放坐标轴。在坐标轴的顶部和底部绘制边距。
- 仿真后显示数据 — 示波器数据在仿真期间保存。如果示波器在仿真开始时关闭，则在仿真后打开示波器时，示波器会显示所连接输入信号的仿真结果。

  **注意**

  如果采样率高或仿真时间长，由于示波器在内部保存数据，您可能会遇到内存或系统性能问题。要限制为示波器可视化保存的数据量，请使用 `Limit data points to last` 属性。
- 示波器窗口管理 –– 示波器容器使您能够将 Simulink 模型的多个示波器停靠到单个窗口。该容器提供了一个方便的界面，您可以从该界面可视化信号并管理示波器的设置。

**测量选项卡**

此屏幕截图突出了测量窗口的重要方面。

以下是 Time Scope 模块支持的所有测量的列表：

- Triggers — 设置触发器以同步重复信号并在事件发生时暂停显示。
- Cursor Measurements — 使用垂直和水平游标测量信号值。
- Signal Statistics — 显示所选信号的最大值、最小值、峰峰值差、均值、中位数和 RMS 值。
- Peak Finder — 查找最大值，显示出现这些最大值的 *x* 轴值。
- Bilevel Measurements — 测量转换、过冲、下冲和周期。

您必须拥有 Simscape™ 或 DSP System Toolbox 许可证才能使用 Peak Finder、Bilevel Measurements 和 Signal Statistics。

有关以编程方式控制示波器的信息，请参阅 Control Scope Blocks Programmatically (Simulink)。
