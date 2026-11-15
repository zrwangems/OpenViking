---
type: simulink-block
title: 'Scope'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'scope'
---

# Scope

Display signals generated during simulation

## 中文

显示仿真过程中生成的信号

### 所属库

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Sinks

### 描述

Simulink® Scope 模块和 DSP System Toolbox™ Time Scope 模块显示时域信号。

这两个模块具有相同的功能，但是默认设置不同。Time Scope 针对离散时间处理进行了优化。Scope 针对一般时域仿真进行了优化。如需并排比较，请参阅 Simulink Scope 模块与 DSP System Toolbox Time Scope 模块。

**“示波器”选项卡**

此屏幕截图突出显示示波器窗口的重要方面。

**示波器画面支持：**

- 仿真控制 - 从“范围”窗口中使用**运行**、**步进**和**步退**工具栏按钮可以运行和调试模型。
- 多个信号 - 可使用多个输入端口在同一显示画面上绘制多个信号。
- 多个显示画面 - 在多个子图上显示信号。子图的所有 *y* 轴在 *x* 轴上具有共同的时间范围。使用工具条的**示波器**选项卡中的**显示网格**参数控制子图的布局。
- 修改参数 - 在仿真之前和仿真期间修改波形参数值。
- 自动缩放轴范围 - 在仿真期间或仿真结束时自动缩放轴范围。在坐标区的顶部和底部会留有边距。
- 仿真后显示数据 - 仿真期间保存波形数据。如果在仿真开始时波形视图关闭，则当您在仿真后打开波形视图时，波形视图将显示附加的输入信号的仿真结果。

  **注意**

  如果采样率高或仿真时间长，可能会遇到内存或系统性能问题，因为示波器在内部保存数据。要限制为波形可视化保存的数据量，请使用 `Limit data points to last` 属性。
- 示波器窗口管理 - 示波器容器使您能够将 Simulink 模型的多个示波器停靠到单个窗口中。该容器提供便捷的界面，您可以从中可视化信号并管理示波器的设置。

**“测量”选项卡**

此屏幕截图突出显示测量窗口的重要方面。

以下是 Scope 模块支持的所有测量列表：

- 触发器 - 设置触发器，在发生指定事件时同步重复的信号并暂停显示。
- 游标测量 - 使用垂直游标和水平游标测量信号值。
- 信号统计 - 显示所选信号的最大值、最小值、峰间差、均值、中位数和 RMS 值。
- 峰值查找器 - 查找最大值，显示出现最大值时的 *x* 轴值。
- 双电平测量 - 测量过渡过程、过冲、下冲和循环。

您必须拥有 Simscape™ 或 DSP System Toolbox 许可证，才能使用峰值查找器、双电平测量和信号统计这些功能面板。

有关以编程方式控制示波器的信息，请参阅以编程方式控制 Scope 模块。

### 端口

#### 输入

#### **Port\_1** — 要可视化的信号 标量 | 向量 | 矩阵 | 数组 | 总线 | 非虚拟总线

连接要可视化的信号。您最多可以有 96 个输入端口。输入信号可以具有以下特性：

- **类型** - 连续（基于采样）或离散（基于采样和基于帧）。
- **数据类型** - Simulink 支持的任何数据类型。请参阅 Simulink 支持的数据类型。

  此模块接受定点输入，但将其转换为 `double` 进行显示。
- **维度** - 标量、一维（向量）、二维（矩阵）或多维（数组）。根据维度在一个信号中显示多个通道。请参阅信号维度和确定信号维度。

##### 输入限制

- 当输入是常量信号时，示波器绘制单个点。
- 当信号值为 `NaN` 时，示波器会在显示画面上显示缺口。
- 当您在示波器内可视化多个基于帧的信号时，部分帧大小为 1 的信号采样可能不会显示。要可视化这些信号，请将帧大小为 1 的信号转移到单独的示波器。

##### 总线支持

可将非虚拟总线和总线信号数组连接到示波器。要显示总线信号，请使用普通或加速仿真模式。示波器按照元素在总线中出现的顺序从上到下显示每个总线元素信号。嵌套的总线元素被展平。

要使用示波器记录非虚拟总线信号，请将**保存格式**参数设置为**数据集**。您可以使用任何**保存格式**记录虚拟总线信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

### 参数

#### “示波器”选项卡

Scope tab of the Scope block and the Time Scope block.

##### 设置 > 常规

#### **仿真开始时打开** — 指定示波器何时打开 off（Scope 的默认值） | on（Time Scope 的默认值）

选择此参数可在仿真开始时打开示波器。

##### 编程用法

请参阅 `OpenAtSimulationStart`。

#### **显示完整路径** — 在示波器标题栏上显示模块路径 off (默认) | on

选择此参数将显示模块名称以及模块路径。

#### **输入端口数目** — 示波器上输入端口的数量 `1` (默认) | [1 96] 范围内的正整数

将示波器上的输入端口数指定为 [1 96] 范围内的正整数。

##### 编程用法

请参阅 `NumInputPorts`。

#### **显示网格** — 显示网格的维度 [1, 1] (默认) | 二元素数值向量

将显示网格的维度指定为二元素数值向量，其中每个元素都大于 0 且小于或等于 16。

##### 编程用法

请参阅 `LayoutDimensions`。

#### **输入处理** — 基于采样或基于帧的处理 **元素作为通道(基于采样)**（Scope 的默认值） | **列作为通道(基于帧)**（Time Scope 的默认值）

指定模块是执行基于采样还是基于帧的处理。

- **元素作为通道(基于采样)** - 将输入的每个元素作为独立通道处理。
- **列作为通道(基于帧)** - 将输入的每列作为独立通道处理。基于帧的处理方式仅对离散输入信号可用。

当您更改**输入处理**参数的设置时，示波器会清除信号数据和测量数据（如果有）。重新运行仿真以使用新设置绘制信号数据。 *(自 R2025a 起)*

**注意**

基于帧的处理需要具有 DSP System Toolbox 许可证。有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

##### 编程用法

请参阅 `FrameBasedProcessing`。

#### **最大化坐标区** — 最大化图的大小 **off**（Scope 的默认值） | **自动**（Time Scope 的默认值） | **on**

- **自动** - 如果未指定**标题**和 **Y 轴标签**属性，则最大化所有绘图。
- **On** - 最大化所有图。**标题**和 **Y 轴标签**中的值将隐藏。
- **Off** - 不最大化图。

##### 编程用法

请参阅 `MaximizeAxes`。

##### 设置 > 时间

#### **采样时间** — 示波器更新之间的仿真间隔 `-1`（表示继承） (默认) | 正实数

指定示波器显示画面更新之间的时间间隔。此属性不适用于浮动示波器和波形查看器。有关示波器中采样时间的更详细说明，请参阅Sample Time with Scope Blocks。

##### 编程用法

请参阅 `SampleTime`。

#### **时间跨度** — 要显示的 *x* 轴的长度 **自动** (默认) | **一帧周期** | **<user-defined>**

将 *x* 轴的显示长度指定为以下选项之一：

- **自动** - 仿真开始时间与停止时间之间的时间差。

  模块使用**时间显示偏移量**和**时间跨度**参数计算时间范围的开始和结束时间。例如，如果将**时间显示偏移量**设置为 `10`，将**时间跨度**设置为 `20`，波形会将时间范围设置为从 `10` 到 `30`。
- **一帧周期** - 将输入信号的帧周期用于 Scope 模块。此选项仅在**输入处理**参数设置为**列作为通道(基于帧)** 时可用。
- **<user-defined>** - 输入小于总仿真时间的任何值。

##### 编程用法

请参阅 `TimeSpan`。

#### **超限操作** — 显示超出 *x* 轴可见范围的数据 **绕回** (默认) | **滚动**

指定如何显示超出 *x* 轴可见范围的数据。

只有在由于模型较大或者步长较小而导致绘图速度缓慢时，才能看到此操作的效果。

- **绕回** - 从左到右全屏绘制数据，之后擦除屏幕，然后再从左到右重新开始绘制数据。
- **滚动** - 在右侧绘制新数据时，旧数据向左移动。此模式由于有密集的图形操作，可能会影响运行时性能。

##### 编程用法

请参阅 `TimeSpanOverrunAction`。

#### **时间单位** — *x* 轴单位 **无**（Scope 的默认值） | **度量(基于时间跨度)**（时间示波器的默认值） | **秒**

将 *x* 轴单位指定为以下选项之一：

- **度量(基于时间跨度)** - 根据**时间跨度**的长度显示时间单位。
- **秒** - 以秒为单位显示时间。
- **无** - 不显示时间单位。

##### 编程用法

请参阅 `TimeUnits`。

#### **时间显示偏移量** — *x* 轴偏移量 `0` (默认) | 标量 | 向量

将 *x* 轴偏移指定的时间值，指定为实数或由实数组成的向量。

对于具有多个通道的输入信号，可以输入标量或向量：

- 标量 - 按相同的时间值偏移输入信号的所有通道。
- 向量 - 分别偏移每个通道。

##### 编程用法

请参阅 `TimeDisplayOffset`。

#### **T 轴和刻度标签** — *x* 轴（时间）和刻度标签的显示 **仅底部显示**（Scope 的默认值） | **全部**（Time Scope 的默认值） | **无**

指定 *x* 轴（时间）和刻度标签的显示方式：

- **全部** - 在所有 *y* 轴上显示 *x* 轴标签。
- **无** - 不显示标签。选择**无**也将清除**显示时间轴标签**参数。
- **仅底部显示** - 在底部 *y* 轴上显示 *x* 轴标签。

##### 依赖关系

要启用此参数，请进行如下设置：

- 选择**显示时间轴标签**。
- 将**最大化坐标区**设置为 **Off**。

##### 编程用法

请参阅 `TimeAxisLabels`。

#### **时间偏移量视图** — 在状态栏上显示时间偏移量 on (默认) | off

选择此参数以在状态栏上显示时间偏移量。

#### **显示时间轴标签** — 显示或隐藏 *x* 轴标签 off（Scope 的默认值） | on（Time Scope 的默认值）

选择此参数以显示活动画面的 *x* 轴标签。

##### 依赖关系

要启用此参数，请将 **T 轴和刻度标签**设置为**全部**或**仅底部显示**。

##### 编程用法

请参阅 `ShowTimeAxisLabel`。

##### 设置 > 坐标区缩放

#### **缩放 Y 轴范围** — *y* 轴缩放模式 **手动** (默认) | **自动** | **N 次更新后**

将 *y* 轴缩放模式指定为以下选项之一：

- **手动** - 手动缩放 *y* 轴范围。
- **自动** - 在仿真期间和仿真后缩放 *y* 轴范围。选择此选项将显示 **Y 轴范围不会缩小**参数。如果希望 y 轴范围随信号的最大值增大和减小，请将**缩放 Y 轴范围**设置为**自动**并清除 **Y 轴范围不会缩小**参数。
- **N 次更新后** - 在**更新次数**参数中指定的时间步数（默认值为 `10`）后，缩放 *y* 轴。每次运行期间仅发生一次缩放。

##### 编程用法

请参阅 `AxesScaling`。

#### **Y 轴范围不会缩小** — 允许 *y* 轴范围界限增大 on (默认) | off

选择此参数以允许在仿真期间 *y* 轴范围界限增大。

##### 依赖关系

要使用此参数，请将**缩放 Y 轴范围**设置为**自动**。

#### **更新次数** — 缩放之前的更新次数 `10` (默认) | 整数

设置此属性可延迟 *y* 轴的自动缩放。

##### 依赖关系

要使用此参数，请将**缩放 Y 轴范围**设置为 **N 次更新后**。

##### 编程用法

请参阅 `AxesScalingNumUpdates`。

#### **停止时缩放 Y 轴范围** — 仿真停止时缩放 *y* 轴范围 on (默认) | off

选中此参数时，示波器仅在仿真停止时缩放 *y* 轴范围。清除此参数时，示波器会连续缩放 *y* 轴范围。

#### **Y 轴数据范围(%)** — 绘图空间占 *y* 轴范围的百分比 `80` (默认) | [1,100] 之间的整数

指定绘制数据图时所使用的 *y* 轴范围的百分比。如果将此参数设置为 `100`，绘制的数据将使用整个 *y* 轴范围。

#### **Y 轴对齐** — 沿 *y* 轴对齐 `Center` (默认) | `Top` | `Bottom`

指定当 **Y 轴数据范围 (%)** 设置小于 100% 时，绘图数据沿 *y* 轴数据范围对齐的位置。

- **顶端** - 将信号与 *y* 轴范围的最大值对齐。
- **居中** - 使信号在最小值和最大值之间居中。
- **底端** - 将信号与 *y* 轴范围的最小值对齐。

#### **自动缩放 X 轴范围** — 缩放 *x* 轴范围界限 off (默认) | on

缩放 *x* 轴范围以容纳所有信号值。如果**缩放 Y 轴范围**设置为 `Auto`，则只缩放当前在坐标区范围内的数据，而不是数据缓冲区中的整个信号。

#### **X 轴数据范围(%)** — 绘图空间占 *x* 轴范围的百分比 `100` (默认) | [1,100] 范围内的整数

指定绘制数据图时所使用的 *x* 轴范围的百分比。例如，如果将此参数设置为 `100`，绘制的数据将使用整个 *x* 轴范围。

##### 依赖关系

要启用此参数，请选择**缩放 X 轴范围**。

#### **X 轴对齐** — 沿 *x* 轴对齐 `Center` (默认) | `Left` | `Right`

指定当 **X 轴数据范围(%)** 设置小于 100% 时，绘图数据沿 *x* 轴数据范围对齐的位置。

- **右侧** - 将信号与 *x* 轴范围的最大值对齐。
- **居中** - 使信号在最小值和最大值之间居中。
- **左侧** - 将信号与 *x* 轴范围的最小值对齐。

##### 依赖关系

要启用此参数，请选择**缩放 X 轴范围**。

##### 设置 > 记录

#### **将数据点限制为最后**, **将帧数限制为最后** — 限制缓冲的数据点或帧 `off` (默认) | `on`

选择此属性以限制示波器内部保存的数据。如果选择此属性并将**输入处理**参数设置为：

- **元素作为通道(基于采样)** - 示波器将最后 *n* 个数据点保存到在**变量名称**中指定的 MATLAB® 变量。在此设置中，此属性的名称为**将数据点限制为最后**。
- **列作为通道(基于帧)** - 示波器将最后 *n* 个数据帧保存到在**变量名称**中指定的 MATLAB 变量。在此设置中，此属性的名称为**将帧数限制为最后**。

*n* 是您在**最大点数**参数中指定的标量值。

选择此参数时，示波器可以绘制小于整个仿真时间范围的信号，例如，在采样时间较小时，就可能出现这种情况。如果波形只绘制了信号的一部分，请考虑增加要保存的数据点数量。

当您清除此属性时，示波器将保存所有数据。仿真完成后，您可以可视化作用域内的全部数据。对于将**停止时间**设置为 `inf` 的仿真，请考虑选择此属性。

**注意**

如果不选择此属性，并且采样率较高或仿真时间较长，则可能会遇到内存或系统性能问题。

##### 编程用法

请参阅 `DataLoggingLimitDataPoints`。

#### **最大点数** — 要保存的数据点的最大数量 `5000` | 正整数

将要保存的数据点的最大数量 *n* 指定为正整数。示波器将最后 *n* 个数据点保存到在**变量名称**中指定的 MATLAB 变量。

##### 依赖关系

要启用此参数，请选择**将数据点限制为最后**或**将帧数限制为最后**参数。

##### 编程用法

请参阅 `DataLoggingMaxPoints`。

#### **抽取**, **抽取帧** — 减少要显示和保存的波形数据量 `off` (默认) | `on`

选择此属性以每隔 *N* 个数据点或帧绘制和记录（保存）示波器数据，其中 *N* 是您在**抽取值**参数中指定的抽取因子。

当您选择此属性并在**抽取值**参数中指定标量值时，作用域会将绘制和保存的数据值限制为在**变量名称**中指定的 MATLAB 变量。

如果将**输入处理**参数设置为：

- **元素作为通道(基于采样)** - 示波器每隔 *N* 个数据点绘制和记录数据。此属性的名称为**抽取**。
- **列作为通道(基于帧)** - 示波器每隔 *N* 帧绘制和记录数据。此属性的名称为**抽取帧**。

当您清除此属性时，示波器将保存所有示波器数据。

##### 编程用法

请参阅 `DataLoggingDecimateData` 和 `DataLoggingDecimation`。

#### **抽取值** — 抽取值 `2` (默认) | 正整数

指定示波器每隔 *N* 个数据点或帧保存或记录数据，其中 *N* 是您在此参数中指定的值。

值 `1` 缓冲所有数据值。

##### 依赖关系

要启用此参数，请选择**抽取**或**抽取帧**。

##### 编程用法

请参阅 `DataLoggingDecimateData` 和 `DataLoggingDecimation`。

#### **将数据记录到工作区** — 将数据保存到 MATLAB 工作区 `off` (默认) | `on`

选择此参数以启用记录并将记录的数据保存到 MATLAB 工作区。选择此参数时，示波器还会启用**变量名称**和**保存格式**参数。此参数不适用于浮动示波器和波形查看器。

有关使用 Scope 模块将信号保存到 MATLAB 工作区的示例，请参阅使用 Scope 模块保存仿真数据。

##### 编程用法

请参阅 `DataLogging`。

#### **变量名称** — 所保存数据变量的名称 **ScopeData** (默认) | 字符向量 | 字符串标量

指定一个用于在 MATLAB 工作区中保存波形数据的变量名称。此参数不适用于浮动示波器和波形查看器。

##### 依赖关系

要启用此参数，请选择**将数据记录到工作区**。

##### 编程用法

请参阅 `DataLoggingVariableName`。

#### **保存格式** — MATLAB 变量格式 **数据集** (默认) | **带时间的结构体** | **结构体** | **数组**

选择用于在 MATLAB 工作区中保存数据的 MATLAB 变量格式。此参数不适用于浮动示波器和波形查看器。

- **数据集** - 将数据保存为 `Dataset` 对象，默认为 `timeseries` 对象。
- **带时间的结构体** - 将数据保存为带有关联时间信息的结构体。
- **结构体** - 将数据保存为结构体。
- **数组** - 将数据保存为带有相关时间信息的数组。此格式不支持可变大小数据。

##### 依赖关系

要启用此参数，请选择**将数据记录到工作区**。

##### 编程用法

请参阅 `DataLoggingSaveFormat`。

##### 设置 > 坐标区样式

#### **绘图类型** — 绘图类型 **自动**（Scope 的默认值） | **线图**（Time Scope 的默认值） | **阶梯图** | **针状图**

将绘图类型指定为以下选项之一：

- **自动** - 绘图类型是对连续信号使用线图、对离散信号使用阶梯图、对 Simulink 消息信号使用针状图。
- **线图** - 线图。
- **阶梯图** - 阶梯图。阶梯图仅由水平线和垂直线组成。每条水平线表示离散采样周期的信号值，并连接到两条垂直线。每条垂直线表示在特定采样时间发生的信号值变化。
- **针状图** - 针状图，在输入值处显示为圆圈，且以垂直线连接至 *x* 轴。

#### **坐标区背景** — 单个显示画面的背景颜色 黑色 (默认) | 颜色

选择示波器显示画面的背景颜色。

#### **坐标区和网格** — 单个显示画面的坐标区、网格和标签颜色 灰色 (默认) | 颜色

选择单个显示画面的坐标区、网格和标签颜色。

#### **示波器背景** — 示波器窗口的背景色 黑色 (默认) | 颜色

选择示波器窗口的背景颜色。

#### **为副本保留颜色** — 复制示波器时保留颜色 off (默认) | on

选择此参数以在将示波器显示画面复制到剪贴板时保留颜色。未选择此参数时，示波器会将示波器的颜色更改为适合打印机的颜色（白色背景、可见线条）。要在复制时保留示波器上的现有颜色，请选择此参数。

##### 设置 > 显示属性

#### **活动画面** — 活动画面 `1` (默认) | 正整数

根据**显示属性** > **线型**、**Y 轴**和**显示**中的设置选择更新的显示。

使用与列放置索引相对应的正整数来指定所需的画面。对于具有多列和多行的布局，显示屏编号先从上到下，再从左到右进行映射。

##### 依赖关系

要启用此参数，请将显示网格设置为包含多个显示画面，即，将**设置** > **常规**下的**显示网格**设置为包含至少一个大于 1 的值的二元素数值向量。

##### 编程用法

请参阅 `ActiveDisplay`。

**注意**

所有**线型**属性仅影响通过**活动画面**参数选择的活动画面。

##### 设置 > 线型

#### **线图** — 要更改的线条 **通道 1** (默认) | 通道名称

选择设置线型属性所针对的活动线条。

#### **样式** — 线型 **-** (默认) | **:** | **-**. | **--** | **无**

为使用**线条**参数选择的活动线条选择线型。

#### **宽度** — 线宽 **1.5** (默认) | **0.5** | **1** | **2** | **3** | **4** | **6** | ...

为使用**线条**参数选择的活动线条指定线宽。

#### **标记** — 数据点标记样式 **无** (默认) | **o** | **+** | **x** | ...

为使用**线条**参数选择的活动线条指定数据点标记。此参数与绘图的 `'Marker'` 属性相似。您可以从下拉列表中选择任何标记符号。

#### **颜色** — 线条颜色 黄色 (默认) | 颜色选择器

为使用**线条**参数选择的活动线条指定线条颜色。

**可调:** Yes

#### **线条可见** — 线条可见性 on (默认) | off

在图上显示或隐藏信号。

选中此参数以在绘图上显示信号。清除此参数后，所选信号将不再可见。

**注意**

所有 **Y 轴**属性仅影响通过**活动画面**参数选择的活动画面。

##### 设置 > Y 轴

#### **Y 轴标签** — Y 轴标签 无（Scope 的默认值） | `Amplitude`（Time Scope 的默认值） | 字符向量 | 字符串标量

指定要在 *y* 轴上显示的文本。要显示信号单位，请在标签中添加 `(%<SignalUnits>)`。仿真开始时，Simulink 会将 `(%SignalUnits)` 替换为与信号关联的单位。

**示例:** 对于单位为 `m/s` 的速度信号，输入 `Velocity (%<SignalUnits>)`。

##### 依赖关系

如果在**显示**设置下选择**绘制幅值-相位图**参数，此参数不适用。两个 *y* 轴将分别显示 `Magnitude` 和 `Phase` 标签。

##### 编程用法

请参阅 `YLabel`。

#### **Y 轴范围** — Y 轴范围 [`-10` `10`] (默认) | 二元素数值向量

将 *y* 轴范围指定为二元素数值向量。

**可调:** Yes

##### 依赖关系

如果选择**绘制幅值-相位图**，此属性仅应用于幅值图。相位图的 *y* 轴范围始终为 `[-180 180]`。

##### 编程用法

请参阅 `YLimits`。

**注意**

所有**显示**属性仅影响通过**活动画面**参数选择的活动画面。

##### 设置 > 显示

#### **标题** — 画面名称 `%<SignalLabel>` (默认) | 字符向量 | 字符串标量

指定显示的标题。默认值 `%<SignalLabel>` 使用输入信号名称作为标题。

##### 编程用法

请参阅 `Title`。

#### **显示图例** — 显示信号图例。 off (默认) | on

选择此参数以显示信号图例。图例中列出的名称是来自模型的信号名称。对于具有多个通道的信号，示波器会在信号名称后附加通道索引。连续信号的名称前面带有直线条，离散信号的名称前面带有楼梯形线条。

从图例中，您可以控制哪些信号可见。此控制项等效于更改**线型**属性中的可见性。在示波器图例中，点击某信号名称可在示波器中隐藏该信号。要显示该信号，请再次点击信号名称。要只显示一个信号，请右键点击该信号名称，这将隐藏所有其他信号。要显示所有信号，请按 **Esc**。

**注意**

图例只显示前 20 个信号。任何其他信号都无法从图例中控制。

##### 编程用法

请参阅 `ShowLegend`。

#### **显示网格** — 显示内部网格线 on (默认) | off

选择此参数以显示内部网格线。

##### 编程用法

请参阅 `ShowGrid`。

#### **绘制幅值-相位图** — 将画面拆分为幅值图和相位图。 off (默认) | on

选择此参数以将显示画面拆分为幅值和相位图。

- On - 显示幅值图和相位图。如果信号是实数，则示波器绘制信号的绝对值作为幅值。正值的相位为 0 度，负值的相位为 180 度。此功能对于复数值输入信号很有用。如果输入是实数值信号，则选择此参数将返回信号的绝对值作为幅值。
- Off - 显示信号图。如果信号是复信号，则示波器基于同一 *y* 轴绘制实部和虚部。

##### 编程用法

请参阅 `PlotAsMagnitudePhase`。

##### 显示网格

#### **显示网格** — 显示布局 1×1 画面 (默认) | `m`×`n` 个坐标区

指定显示的布局。打开类似于示波器布局的网格选择器。布局最多可以有 16 行和 16 列。使用网格选择器，可以选择最大 5×5 的布局。要选择大于 5×5 的布局，请执行以下操作：

- 在工具条的**示波器**选项卡的**设置** > **常规**下，将**显示网格**设置为每个元素大于 0 且小于或等于 16 的二元素数值向量。例如，将**显示网格**设置为 [`2` `1`] 会将布局更改为 2×1。
- 使用 `TimeScopeConfiguration` 对象的 `LayoutDimensions` 属性。

Animated GIF of changing the layout from one display to two displays

如果画面数等于端口数，每个端口的信号将单独显示。如果画面数小于端口数，多出的端口信号将显示在最后一个画面上。对于具有多列和多行的布局，端口先从上到下，再从左到右进行映射。如果显示画面的数量大于端口数量，示波器会创建空图块。

##### 编程用法

请参阅 `LayoutDimensions`。

##### 停靠

#### **停靠** — 将示波器停靠到示波器容器中 **停靠示波器** (默认) | **停靠所有示波器**

在**示波器**选项卡中点击**停靠**或**停靠示波器**，可将当前活动示波器添加到示波器容器。点击**停靠所有示波器**，可将当前模型中所有打开的示波器添加到示波器容器。

有关示波器容器的详细信息，请参阅示波器窗口管理。

#### **取消停靠** — 从示波器容器取消停靠示波器 **取消停靠** (默认) | **全部取消停靠**

在示波器容器的**主页**选项卡中点击**取消停靠**，可将当前活动示波器从容器中移至单独的独立窗口中。点击**全部取消停靠**，可将所有示波器从容器中移至单独的独立窗口中。

有关示波器容器的详细信息，请参阅示波器窗口管理。

##### 依赖关系

此参数仅在示波器容器的**主页**选项卡上可用。

#### **新示波器打开时停靠** — 在新示波器打开时将其添加到容器 off (默认) | on

选择此参数可将新打开的示波器（在 MATLAB 当前会话中之前未打开过的）自动添加到现有示波器容器。

有关示波器容器的详细信息，请参阅示波器窗口管理。

##### 依赖关系

此参数仅在示波器容器的**主页**选项卡上可用。要访问此参数，请点击示波器容器的**主页**选项卡下**全部停靠**的下拉箭头。

#### “测量”选项卡

**测量**选项卡包含示波器支持的所有信号测量的设置。测量面板显示在示波器窗口底部。要打开测量面板，您必须首先在**测量**选项卡中启用对应的测量。

Measurements tab of the Scope block and the Time Scope block.

有关测量的详细信息，请参阅以下页：

- 触发器 - 设置触发器，在发生指定事件时同步重复的信号并暂停显示。
- 游标测量 - 使用垂直游标和水平游标测量信号值。
- 信号统计 - 显示所选信号的最大值、最小值、峰间差、均值、中位数和 RMS 值。
- 峰值查找器 - 查找最大值，显示出现最大值时的 *x* 轴值。
- 双电平测量 - 测量过渡过程、过冲、下冲和循环。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `busa` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 不支持虚拟总线。非虚拟总线仅在 Normal 模式和 Accelerator 模式的仿真中受支持。非虚拟总线的数据记录只支持数据集格式。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块可用于在对要生成代码的系统进行仿真时查看仿真情况，但生成的代码中不会包含此模块。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

此模块可用于在对要生成代码的系统进行仿真时查看仿真情况，但生成的代码中不会包含此模块。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块接受定点输入，但将其转换为双精度值进行显示。

### 版本历史记录

**在 R2015b 中推出**

#### R2025a: 改进的示波器和新示波器容器可将所有示波器停靠在后一个窗口中

Simulink Scope、Time Scope (DSP System Toolbox) 和 Floating Scope and Scope Viewer 模块在 Simulink 中具有新用户界面，可用于访问示波器的设置和测量。现在示波器响应更灵敏，性能有所提升。使用新示波器容器将多个示波器窗口停靠到单个窗口中，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

Scope、Time Scope 和 Floating Scope and Scope Viewer 模块的主要改进包括：

- 简化的用户界面：可从新示波器工具条的**示波器**选项卡轻松访问所有常规示波器设置，并从**测量**选项卡访问所有测量设置。
- 新示波器容器：单一窗口，为模型中的所有示波器显示画面提供统一视图，使您能够在一个位置集中管理和组织多个示波器。
- 更新后的设置面板：更新后的面板合并了示波器的所有常规和样式设置。要打开该面板，请在工具条的**示波器**选项卡中点击**设置**。

#### R2025a: 通过 MATLAB Graphics API 访问 Simulink Scope 的功能已删除

Simulink Scope 模块的基础图形已更改。您无法通过 MATLAB Graphics API 访问或修改 Simulink Scope 模块。

要在 MATLAB 图形窗口中显示示波器数据，请使用 Scope 模块工具条的**示波器**选项卡中的**打印到图窗**功能。

#### R2025a: 将示波器停靠到 MATLAB 桌面的功能已删除

将 Simulink Scope、Time Scope (DSP System Toolbox) 和 Floating Scope and Scope Viewer 停靠到 MATLAB 桌面的功能已删除。请改用新示波器容器。有关详细信息，请参阅示波器窗口管理。

如果您在 R2024b 或更早版本中创建的模型包含四个或更多打开的示波器，并且在 R2025a 中打开该模型，则打开的示波器会自动停靠在示波器容器窗口中。

## Libraries

Simulink / Commonly Used Blocks Simulink / Sinks HDL Coder / Commonly Used Blocks HDL Coder / Sinks

## Description

The Simulink®
Scope block and DSP System Toolbox™
Time Scope block display time domain signals.

The two blocks have identical
functionality, but different default settings. The Time Scope is optimized for discrete time processing.
The Scope is optimized for general time-domain simulation. For a side-by-side comparison, see Simulink Scope Block Versus DSP System Toolbox Time Scope Block.

**Scope Tab**

This screenshot highlights the important aspects of the scope window.

**Scope display features:**

- Simulation control — Run and debug models from a Scope window using
  **Run**, **Step Forward**, and
  **Step Backward** toolbar buttons.
- Multiple signals — Plot multiple signals on the same display using multiple
  input
  ports.
- Multiple displays — Display signals on multiple subplots. All the
  *y*-axes of the subplots have a common time range on the
  *x*-axis. Control the layout of the subplots using the
  **Display Grid** parameter in the
  **Scope** tab of the toolstrip.
- Modify parameters — Modify scope parameter values before and during a
  simulation.
- Axis autoscaling — Autoscale axes during or at the end of a simulation.
  Margins are drawn at the top and bottom of the axes.
- Display data after simulation — Scope data is saved during a simulation. If a
  scope is closed at the start of a simulation, when you open the scope after a
  simulation, the scope displays simulation results for attached input signals.

  **Note**

  If you have a high sample rate or long simulation time, you may run
  into issues with memory or system performance because the scope saves
  data internally. To limit the amount of data saved for scope
  visualization, use the `Limit data points to last`
  property.
- Scope window management –– The scope container enables you to dock multiple
  scopes of the Simulink model into a single window. The container provides a convenient
  interface from which you can visualize the signals and manage the settings of
  the scopes.

**Measurements Tab**

This screenshot highlights the important aspects of the measurements window.

Here is a list of all the measurements the Scope block supports:

- Triggers —
  Set triggers to sync repeating signals and pause the display when events
  occur.
- Cursor
  Measurements — Measure signal values using vertical and horizontal
  cursors.
- Signal
  Statistics — Display the maximum, minimum, peak-to-peak difference,
  mean, median, and RMS values of a selected signal.
- Peak
  Finder — Find maxima, showing the *x*-axis values at
  which they occur.
- Bilevel
  Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

You must have a Simscape™ or DSP System Toolbox license to use the Peak Finder, Bilevel Measurements, and Signal
Statistics.

For information on controlling a
scope programmatically, see Control Scope Blocks Programmatically.

## Ports

### Input

### **Port\_1** — Signal or signals to visualize scalar | vector | matrix | array | bus | nonvirtual bus

Connect the signals you want to visualize. You can have up to 96 input ports. Input signals can have
these characteristics:

- **Type** — Continuous (sample-based) or discrete (sample-based and
  frame-based).
- **Data type** — Any data type that Simulink supports. See Data Types Supported by Simulink.

  This block accepts fixed-point input, but converts it to
  `double` for display.
- **Dimension** — Scalar, one
  dimensional (vector), two dimensional (matrix), or multidimensional
  (array). Display multiple channels within one signal depending on
  the dimension. See Signal Dimensions and Determine Signal Dimensions.

#### Input Limitations

- When the input is a constant signal, the scope plots a single
  point.
- The scope shows gaps in the display when the signal value is
  `NaN`.
- When you visualize multiple frame-based signals in the scope,
  some samples of signals with a frame size of 1 might not be
  displayed. To visualize these signals, move the signals with
  frame size of 1 to a separate scope.

#### Bus Support

You can connect nonvirtual bus and arrays of bus signals to a scope.
To display the bus signals, use normal or accelerator simulation mode.
The scope displays each bus element signal in the order the elements
appear in the bus, from the top to the bottom. Nested bus elements are
flattened.

To log nonvirtual bus signals with a scope, set the **Save
format** parameter to `Dataset`.
You can use any **Save format** to log virtual bus
signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

### Scope Tab

Scope tab of the Scope block and the Time Scope block.

#### Settings > General

### **Open at simulation start** — Specify when scope opens off (default for Scope) | on (default for Time Scope)

Select this parameter to open the scope when simulation starts.

#### Programmatic Use

See `OpenAtSimulationStart`.

### **Display the full path** — Display block path on scope title bar off (default) | on

Select this parameter to display the block path in addition to the block
name.

### **Number of input ports** — Number of input ports on scope `1` (default) | positive integer in the range [1 96]

Specify the number of input ports on the scope as a positive integer in
the range [1 96].

#### Programmatic Use

See `NumInputPorts`.

### **Display grid** — Dimensions of display grid [1, 1] (default) | two-element numeric vector

Specify the dimensions of the display grid as a two-element numeric vector
with each element greater than 0 and less than or equal to 16.

#### Programmatic Use

See `LayoutDimensions`.

### **Input processing** — Sample- or frame-based processing `Elements as channels (sample based)` (default for Scope) | `Columns as channels (frame based)` (default for Time Scope)

Specify whether the block performs sample- or frame-based
processing.

- `Elements as channels (sample based)` ––
  Process each element of the input as an independent channel.
- `Columns as channels (frame based)` ––
  Process each column of the input as an independent channel.
  Frame-based processing is available only with discrete input
  signals.

When you change the setting of the
**Input processing** parameter, the scope clears the
signal data and the measurements data (if any). Rerun the simulation to plot
the signal data with the new setting. *(since R2025a)*

**Note**

Frame-based processing requires a DSP System Toolbox license. For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

#### Programmatic Use

See `FrameBasedProcessing`.

### **Maximize axes** — Maximize size of plots `Off` (default for Scope) | `Auto` (default for Time Scope) | `On`

- `Auto` –– If **Title**
  and **Y-axis label** properties are not specified,
  maximize all plots.
- `On` –– Maximize all plots. Values in
  **Title** and **Y-axis label**
  are hidden.
- `Off` –– Do not maximize plots.

#### Programmatic Use

See `MaximizeAxes`.

#### Settings > Time

### **Sample time** — Simulation interval between scope updates `-1` (for inherited) (default) | positive real number

Specify the time interval between updates of the scope display.
This property does not apply to floating scopes and scope
viewers. For a more detailed explanation of sample time with the scope, see
Sample Time with Scope Blocks.

#### Programmatic Use

See `SampleTime`.

### **Time span** — Length of *x*-axis to display `Auto` (default) | `One frame period` | `<user-defined>`

Specify the length of the *x*-axis to display as one of
these:

- `Auto` — Difference between the
  simulation start and stop times.

  The block calculates the beginning and end times of the time range
  using the **Time display offset** and
  **Time span** parameters. For example, if you
  set the **Time display offset** to
  `10` and the **Time span**
  to `20`, the scope sets the time range from
  `10` to `30`.
- `One frame period` — Use the frame period
  of the input signal to the Scope block. This option is available only when you set the
  **Input processing** parameter to
  `Columns as channels (frame
  based)`.
- `<user-defined>` — Enter any value
  less than the total simulation time.

#### Programmatic Use

See `TimeSpan`.

### **Overrun action** — Display data beyond visible *x*-axis `Wrap` (default) | `Scroll`

Specify how to display data beyond the visible *x*-axis
range.

You can see the effects of this option only when plotting is slow with
large models or small step sizes.

- `Wrap` — Draw a full screen of data from
  left to right, clear the screen, and then restart drawing the data
  from the left.
- `Scroll` — Move data to the left as new
  data is drawn on the right. This mode is graphically intensive and
  can affect run-time performance.

#### Programmatic Use

See `TimeSpanOverrunAction`.

### **Time units** — *x*-axis units `None` (default for Scope) | `Metric (based on Time Span)` (default for Time Scope) | `Seconds`

Specify the *x*-axis units as one of these
options:

- `Metric (based on Time Span)` — Display
  time units based on the length of **Time
  span**.
- `Seconds` — Display time in
  seconds.
- `None` — Do not display time
  units.

#### Programmatic Use

See `TimeUnits`.

### **Time display offset** — *x*-axis offset `0` (default) | scalar | vector

Offset the *x*-axis by a specified time value, specified
as a real number or a vector of real numbers.

For input signals with multiple channels, you can enter a scalar or
vector:

- Scalar — Offset all channels of an input signal by the same time
  value.
- Vector — Independently offset the channels.

#### Programmatic Use

See `TimeDisplayOffset`.

### **T-axis and ticks labels** — Display of *x*-axis (time) and tick labels `Bottom displays only` (default for Scope) | `All` (default for Time Scope) | `None`

Specify how the *x*-axis (time) and tick labels display:

- `All` — Display
  *x*-axis labels on all
  *y*-axes.
- `None` — Do not display labels.
  Selecting `None` also clears the
  **Show time-axis label** parameter.
- `Bottom displays only` — Display
  *x*-axis label on the bottom
  *y*-axis.

#### Dependencies

To enable this parameter:

- Select **Show time-axis label**.
- Set **Maximize axes** to
  `Off`.

#### Programmatic Use

See `TimeAxisLabels`.

### **Time offset view** — Show time offset on status bar on (default) | off

Select this parameter to show the time offset on the status bar.

### **Show time-axis label** — Display or hide *x*-axis labels off (default for Scope) | on (default for Time Scope)

Select this parameter to show the *x*-axis label for the
active display.

#### Dependencies

To enable this parameter, set **T-axis and ticks
labels** to `All` or
`Bottom displays only`.

#### Programmatic Use

See `ShowTimeAxisLabel`.

#### Settings > Axes Scaling

### **Scale Y-axis limits** — *y*-axis scaling mode `Manual` (default) | `Auto` | `After N Updates`

Specify the *y*-axis scaling mode as one of these:

- `Manual` — Manually scale the
  *y*-axis range.
- `Auto` — Scale the
  *y*-axis range during and after simulation.
  Selecting this option displays the **Y-axis limits do not
  shrink** parameter. If you want the y-axis range to
  increase and decrease with the maximum value of a signal, set
  **Scale Y-axis limits** to
  `Auto` and clear the **Y axis
  limits do not shrink** parameter.
- `After N Updates` — Scale
  *y*-axis after the number of time steps
  specified in the **Number of updates** parameter
  (`10` by default). Scaling occurs only once
  during each run.

#### Programmatic Use

See `AxesScaling`.

### **Y-axis limits do not shrink** — Allow *y*-axis range limits to increase on (default) | off

Select this parameter to allow *y*-axis range limits to
increase during simulation.

#### Dependencies

To use this parameter, set **Scale Y-axis limits** to
`Auto`.

### **Number of updates** — Number of updates before scaling `10` (default) | integer

Set this property to delay auto scaling the
*y*-axis.

#### Dependencies

To use this parameter, set **Scale Y-axis limits** to
`After N Updates`.

#### Programmatic Use

See `AxesScalingNumUpdates`.

### **Scale Y-axis limits at stop** — Scale *y*-axis limits when simulation stops on (default) | off

When you select this parameter, the scope scales the
*y*-axis limits only when the simulation stops. When you
clear this parameter, the scope scales the *y*-axis limits
continuously.

### **Y-axis data range (%)** — Percent of *y*-axis to use for plotting `80` (default) | integer between [1,100]

Specify the percentage of the *y*-axis range used for
plotting data. If you set this parameter to `100`, the
plotted data uses the entire *y*-axis range.

### **Y-axis align** — Alignment along *y*-axis `Center` (default) | `Top` | `Bottom`

Specify where to align plotted data along the *y*-axis
data range when **Y-axis data range (%)** is set to less
than 100 percent.

- `Top` — Align signals with the
  maximum values of the *y*-axis range.
- `Center` — Center signals between the
  minimum and maximum values.
- `Bottom` — Align signals with the
  minimum values of the *y*-axis range.

### **Scale X-axis limits** — Scale *x*-axis range limits off (default) | on

Scale *x*-axis range to fit all signal values. If
**Scale Y-axis limits** is set to
`Auto`, the data currently within the axes is scaled,
not the entire signal in the data buffer.

### **X-axis data range (%)** — Percent of *x*-axis to use for plotting `100` (default) | integer in the range [1,100]

Specify the percentage of the *x*-axis range to plot data
on. For example, if you set this parameter to `100`,
plotted data uses the entire *x*-axis range.

#### Dependencies

To enable this parameter, select **Scale X-axis
limits**.

### **X-axis align** — Alignment along *x*-axis `Center` (default) | `Left` | `Right`

Specify where to align plotted data along the *x*-axis
data range when **X-axis data range (%)** is set to less
than 100 percent.

- `Right` — Align signals with the maximum
  values of the *x*-axis range.
- `Center` — Center signals between the
  minimum and maximum values.
- `Left` — Align signals with the minimum
  values of the *x*-axis range.

#### Dependencies

To enable this parameter, select **Scale X-axis
limits**.

#### Settings > Logging

### **Limit data points to last**, **Limit frames to last** — Limit buffered data points or frames `off` (default) | `on`

Select this property to limit data saved by the scope internally. When you
select this property and set the **Input processing**
parameter to:

- `Elements as channels (sample based)`
  –– The scope saves the last *n* data points to
  a MATLAB® variable specified in **Variable
  name**. In this setting, the name of this property
  is **Limit data points to last**.
- `Columns as channels (frame based)`
  –– The scope saves the last *n* data frames to
  a MATLAB variable specified in **Variable
  name**. In this setting, the name of this property
  is **Limit frames to last**.

*n* is the scalar value you specify in the **Max
points** parameter.

When you select this parameter, the scope can plot signals for less than
the entire time range of a simulation, for example, if the sample time is
small. If the scope plots only a portion of the signal, consider increasing
the number of data points to save.

When you clear this property, the scope saves all the data. You can
visualize the entire data in the scope after the simulation finishes. For
simulations with **Stop Time** set to
`inf`, consider selecting this property.

**Note**

If you do not select this property and you have a high sample rate
or long simulation time, you can run into issues with memory or
system performance.

#### Programmatic Use

See `DataLoggingLimitDataPoints`.

### **Max points** — Maximum number of data points to save `5000` | positive integer

Specify the maximum number of data points *n* to save as
a positive integer. The scope saves the last *n* data
points to a MATLAB variable specified in **Variable
name**.

#### Dependencies

To enable this parameter, select the **Limit data points to
last** or the **Limit frames to last**
parameter.

#### Programmatic Use

See `DataLoggingMaxPoints`.

### **Decimation**, **Decimate frames** — Reduce amount of scope data to display and save `off` (default) | `on`

Select this property to plot and log (save) scope data every
*N*th data point or frame, where *N*
is the decimation factor you specify in the **Decimation
value** parameter.

When you select this property and specify a scalar value in the
**Decimation value** parameter, the scope limits the
data values plotted and saved to a MATLAB variable specified in **Variable
name**.

When you set the **Input processing** parameter to:

- `Elements as channels (sample based)`
  –– The scope plots and logs data every *N*th
  data point. The name of this property is
  **Decimation**.
- `Columns as channels (frame based)`
  –– The scope plots and logs data every *N*th
  frame. The name of this property is **Decimate
  frames**.

When you clear this property, the scope saves all the scope data.

#### Programmatic Use

See `DataLoggingDecimateData` and `DataLoggingDecimation`.

### **Decimation value** — Decimation value `2` (default) | positive integer

Specify the scope to save or log data every *N*th data
point or frame, where *N* is the value you specify in this
parameter.

A value of `1` buffers all the data values.

#### Dependencies

To enable this parameter, select **Decimation** or
**Decimate frames**.

#### Programmatic Use

See `DataLoggingDecimateData` and `DataLoggingDecimation`.

### **Log data to workspace** — Save data to MATLAB workspace `off` (default) | `on`

Select this parameter to enable logging and to save the logged data to the
MATLAB workspace. When you select this parameter, the scope enables
the **Variable name** and **Save format**
parameters as well. This parameter does not apply to floating scopes and
scope viewers.

For an example of saving signals to
the MATLAB Workspace using a Scope block, see Save Simulation Data Using Scope Block.

#### Programmatic Use

See `DataLogging`.

### **Variable name** — Name of saved data variable `ScopeData` (default) | character vector | string scalar

Specify a variable name for saving scope data in the MATLAB workspace. This parameter does not apply to floating scopes
and scope viewers.

#### Dependencies

To enable this parameter, select **Log data to
workspace**.

#### Programmatic Use

See `DataLoggingVariableName`.

### **Save format** — MATLAB variable format `Dataset` (default) | `Structure With Time` | `Structure` | `Array`

Select the MATLAB variable format for saving data to the MATLAB workspace. This parameter does not apply to floating scopes
and scope viewers.

- `Dataset` — Save data as a `Dataset` object,
  by default a `timeseries` object.
- `Structure With Time` — Save data as
  a structure with associated time information.
- `Structure` — Save data as a
  structure.
- `Array` — Save data as an array with
  associated time information. This format does not support
  variable-size data.

#### Dependencies

To enable this parameter, select **Log data to
workspace**.

#### Programmatic Use

See `DataLoggingSaveFormat`.

#### Settings > Axes Style

### **Plot type** — Type of plot `Auto` (default for Scope) | `Line` (default for Time Scope) | `Stairs` | `Stem`

Specify the type of the plot as one of these:

- `Auto` –– The plot type is a line
  graph for continuous signals, a stair-step graph for discrete
  signals, and a stem graph for Simulink message signals.
- `Line` –– Line graph.
- `Stairs` –– Stair-step graph. A
  stair-step graph is made up of only horizontal and vertical
  lines. Each horizontal line represents the signal value for a
  discrete sample period and is connected to two vertical lines.
  Each vertical line represents the change in the signal value
  occurring at a specific sample time.
- `Stem` –– Stem graph displayed as
  circles at the input value with vertical lines to the
  *x*-axis.

### **Axes background** — Background color for individual displays black (default) | color

Select the background color for the scope display.

### **Axes and grid** — Axes, grid, and label color for individual displays gray (default) | color

Select the axes, grid, and label color for individual displays.

### **Scope background** — Background color for scope window black (default) | color

Select the background color for the scope window.

### **Preserve colors for copy** — Preserve colors when copying scope off (default) | on

Select this parameter to preserve colors when copying the scope display to
the clipboard. When you do not select this parameter, the scope changes the
color of the scope to be printer friendly (white background, visible lines).
To preserve the existing colors on the scope while copying, select this
parameter.

#### Settings > Display Properties

### **Active Display** — Active display `1` (default) | positive integer

Select the display which updates based on the settings in the
**Display Properties** > **Line
Style**, **Y-axis**, and
**Display**.

Specify the desired display using a positive integer that corresponds to
the column-wise placement index. For layouts with multiple columns and rows,
display numbers are mapped down and then across.

#### Dependencies

To enable this parameter, set the display grid to have more than one
display, that is, set **Display grid** under
**Settings** > **General** to a
two-element numeric vector with at least one of the values greater than
1.

#### Programmatic Use

See `ActiveDisplay`.

**Note**

All the **Line Style** properties affect only the active display
that you select through the **Active Display** parameter.

#### Settings > Line Style

### **Line** — Line to change `Channel 1` (default) | channel name

Select the active line for setting line style properties.

### **Style** — Line style `-` (default) | `:` | `-`. | `--` | `None`

Select the line style for the active line that you select using the
**Line** parameter.

### **Width** — Line width `1.5` (default) | `0.5` | `1` | `2` | `3` | `4` | `6` | ...

Specify the line width for the active line that you select using the
**Line** parameter.

### **Marker** — Data point marker style `none` (default) | `o` | `+` | `x` | ...

Specify a data point marker for the active line that you select using the
**Line** parameter. This parameter is similar to the
`'Marker'` property for plots. You can choose any of the
marker symbols from the drop-down list.

### **Color** — Line color yellow (default) | color picker

Specify the line color for the active line that you select using the
**Line** parameter.

**Tunable:** Yes

### **Line visible** — Line visibility on (default) | off

Show or hide a signal on the plot.

Select this parameter to display signal on the plot. If you clear this
parameter, the signal you select is no longer visible.

**Note**

All the **Y-axis** properties affect only the active display that
you select through the **Active Display** parameter.

#### Settings > Y-axis

### **Y-axis label** — Y-axis label none (default for Scope) | `Amplitude` (default for Time Scope) | character vector | string scalar

Specify the text to display on the *y*-axis. To display
signal units, add `(%<SignalUnits>)` to the label. At
the beginning of a simulation, Simulink replaces `(%SignalUnits)` with the units
associated with the signals.

**Example:** For a velocity signal with units of `m/s`, enter
`Velocity (%<SignalUnits>)`.

#### Dependencies

If you select the **Plot as magnitude-phase**
parameter under **Display** settings, this parameter
does not apply. The *y*-axes are labeled
`Magnitude` and `Phase`.

#### Programmatic Use

See `YLabel`.

### **Y-axis limits** — Y-axis limits [`-10` `10`] (default) | two-element numeric vector

Specify the *y*-axis limits as a two-element numeric
vector.

**Tunable:** Yes

#### Dependencies

If you select **Plot as magnitude-phase**, this
property only applies to the magnitude plot. The
*y*-axis limits of the phase plot are always
`[-180 180]`.

#### Programmatic Use

See `YLimits`.

**Note**

All the **Display** properties affect only the active display
that you select through the **Active Display** parameter.

#### Settings > Display

### **Title** — Display name `%<SignalLabel>` (default) | character vector | string scalar

Specify the title for the display. The default value
`%<SignalLabel>` uses the input signal name for
the title.

#### Programmatic Use

See `Title`.

### **Show legend** — Display signal legend off (default) | on

Select this parameter to display the signal legend. The names listed in
the legend are the signal names from the model. For signals with multiple
channels, the scope appends a channel index after the signal name.
Continuous signals have straight lines before their names, and discrete
signals have step-shaped lines.

From the legend, you can control which signals are visible. This control
is equivalent to changing the visibility in the **Line
Style** properties. In the scope legend, click a signal name to
hide the signal in the scope. To show the signal, click the signal name
again. To show only one signal, right-click the signal name, which hides all
other signals. To show all signals, press **Esc**.

**Note**

The legend only shows the first 20 signals. Any additional signals
cannot be controlled from the legend.

#### Programmatic Use

See `ShowLegend`.

### **Show grid** — Show internal grid lines on (default) | off

Select this parameter to show internal grid lines.

#### Programmatic Use

See `ShowGrid`.

### **Plot as magnitude-phase** — Split display into magnitude and phase plots off (default) | on

Select this parameter to split the display into magnitude and phase
plots.

- On — Display magnitude and phase plots. If the signal is real, the
  scope plots the absolute value of the signal for the magnitude. The
  phase is 0 degrees for positive values and 180 degrees for negative
  values. This feature is useful for complex-valued input signals. If
  the input is a real-valued signal, selecting this parameter returns
  the absolute value of the signal for the magnitude.
- Off — Display signal plot. If the signal is complex, the scope
  plots the real and imaginary parts on the same
  *y*-axis.

#### Programmatic Use

See `PlotAsMagnitudePhase`.

#### Display Grid

### **Display Grid** — Display layout 1-by-1 display (default) | an arrangement of `m`-by-`n` axes

Specify the layout of the displays. Opens a grid picker similar to the
scope layout. The layout can have a maximum of 16 rows and 16 columns. Using
the grid picker, you can select a layout of size up to 5-by-5. To select a
layout of size greater than 5-by-5:

- Set **Display grid** under
  **Settings** >
  **General** in the
  **Scope** tab of the toolstrip to a
  two-element numeric vector with each element greater than 0 and
  less than or equal to 16. For example, setting **Display
  grid** to [`2`
  `1`] changes the layout to 2-by-1.
- Use the `LayoutDimensions` property of the
  `TimeScopeConfiguration` object.

Animated GIF of changing the layout from one display to two displays

If the number of displays is equal to the number of ports, signals from
each port appear on separate displays. If the number of displays is less
than the number of ports, signals from additional ports appear on the last
display. For layouts with multiple columns and rows, ports are mapped down
then across. If the number of displays is greater than the number of ports,
the scope creates empty tiles.

#### Programmatic Use

See `LayoutDimensions`.

#### Dock

### **Dock** — Dock the scope into scope container **Dock Scope** (default) | **Dock All Scopes**

Click **Dock** or **Dock Scope** in the
**Scope** tab to add the currently active scope to the
scope container. Click **Dock All Scopes** to add all the
opened scopes in the current model to the scope container.

For more information on the scope container, see Scope Window Management.

### **Undock** — Undock the scope from the scope container **Undock** (default) | **Undock All**

Click **Undock** in the **Home** tab of
the scope container to remove the currently active scope from the container
into a separate stand-alone window. Click **Undock All** to
remove all scopes from the container into separate stand-alone
windows.

For more information on the scope container, see Scope Window Management.

#### Dependencies

This parameter is available only on the **Home** tab
of the scope container.

### **Dock New Scopes on Open** — Add new scopes to the container on open off (default) | on

Select this parameter to add the newly opened scopes (which have not been
opened before in the current session of MATLAB) automatically to the existing scope container.

For more information on the scope container, see Scope Window Management.

#### Dependencies

This parameter is available only on the **Home** tab
of the scope container. To access this parameter, click the drop down
arrow of **Dock All** under the
**Home** tab of the scope container.

### Measurements Tab

The **Measurements** tab contains the settings for all the signal
measurements that the scope supports. The measurement panels appear at the bottom of the
scope window. To open a measurement panel, you must first enable the corresponding
measurement in the **Measurements** tab.

Measurements tab of the Scope block and the Time Scope block.

For more information on the measurements, see these pages:

- Triggers — Set triggers to sync repeating signals and pause the
  display when events occur.
- Cursor
  Measurements — Measure signal values using vertical and
  horizontal cursors.
- Signal
  Statistics — Display the maximum, minimum, peak-to-peak
  difference, mean, median, and RMS values of a selected signal.
- Peak
  Finder — Find maxima, showing the *x*-axis
  values at which they occur.
- Bilevel
  Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `busa` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Virtual bus not supported. Nonvirtual bus supported only in normal and accelerator mode simulation. Data logging for nonvirtual bus supported only in the dataset format. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block accepts fixed-point input, but converts it to double for
display.

## Version History

**Introduced in R2015b**

### R2025a: Improved Scope and new scope container to dock all scopes in one window

The Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer blocks in Simulink have a new user interface that you can use to access settings and measurements
of the scope. The scope is now more responsive and its performance is improved. Use the new
scope container to dock multiple scope windows into a single window and to manage and
organize the scopes. The scope container also enables you to view all the scopes in the
model in a single window.

Key improvements to the Scope, Time Scope, and
Floating Scope and Scope Viewer blocks are:

- Streamlined user interface: Easy access to all the general scope settings from
  the **Scope** tab and all the measurement settings from the
  **Measurements** tab of the new scope toolstrip.
- New scope container: A single window providing a unified view for all the
  scope displays in the model, enabling you to manage and organize multiple scopes
  in one place.
- Updated settings panel: Updated panel consolidates all general and style
  settings of the scope. To open the panel, click **Settings** in
  the **Scope** tab of the toolstrip.

### R2025a: Access to Simulink Scope through MATLAB Graphics API has been removed

The underlying graphics of the Simulink
Scope block have changed. You
cannot access or modify the Simulink
Scope block through the MATLAB Graphics API.

To display the scope data in a MATLAB Graphics window, use the **Print to Figure**
functionality in the **Scope** tab of the Scope
block toolstrip.

### R2025a: Ability to dock Scopes to MATLAB desktop has been removed

The ability to dock the Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer to the MATLAB desktop has been removed. Use the new scope container instead. For more
information, see Scope Window Management.

If you have a model created in R2024b or a previous release with four or more open scopes,
and you open that model in R2025a, the opened scopes automatically dock in the scope
container window.
