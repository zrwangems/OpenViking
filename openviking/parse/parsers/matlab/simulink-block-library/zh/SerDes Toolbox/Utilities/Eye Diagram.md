---
type: simulink-block
title: 'Eye Diagram'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'legacyeyediagramscope'
documentation_source_path: 'ref/legacyeyediagramscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Eye Diagram

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 列向量
  direction: input
  data_types: double
```

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Display mode
  summary: 显示模式 Line plot（默认）| 2D color Histogram
  group: 主选项卡
- name: Enable measurements
  summary: 启用测量 off（默认）| on
  group: 主选项卡
- name: Show horizontal (jitter) histogram
  summary: 显示抖动直方图 off（默认）| on
  group: 主选项卡
- name: Show vertical (noise) histogram
  summary: 显示噪声直方图 off（默认）| on
  group: 主选项卡
- name: Do not show horizontal or vertical histogram
  summary: 不显示水平或垂直直方图 on（默认）| off
  group: 主选项卡
- name: Show horizontal bathtub curve
  summary: 显示水平浴盆曲线 off（默认）| on
  group: 主选项卡
- name: Show vertical bathtub curve
  summary: 显示垂直浴盆曲线 off（默认）| on
  group: 主选项卡
- name: Eye diagram to display
  summary: 要显示的眼图 Real only（默认）| Real and imaginary
  group: 主选项卡
- name: Color fading
  summary: 颜色渐隐 off（默认）| on
  group: 主选项卡
- name: Samples per symbol
  summary: 每符号采样数 8（默认）| 正整数
  group: 主选项卡
- name: Sample offset
  summary: 采样偏移 0（默认）| 非负整数
  group: 主选项卡
- name: Symbols per trace
  summary: 每条迹线的符号数 2（默认）| 正整数
  group: 主选项卡
- name: Traces to display
  summary: 要显示的迹线数 40（默认）| 正整数
  group: 主选项卡
- name: Title
  summary: 标题标签 *None*（默认）
  group: 坐标轴选项卡
- name: Show grid
  summary: 切换示波器网格 on（默认）| off
  group: 坐标轴选项卡
- name: Y-limits (Minimum)
  summary: '*y* 轴下限 -1.1（默认）| 标量'
  group: 坐标轴选项卡
- name: Y-limits (Maximum)
  summary: '*y* 轴上限 1.1（默认）| 标量'
  group: 坐标轴选项卡
- name: Real axis label
  summary: 实轴标签 Real Amplitude（默认）
  group: 坐标轴选项卡
- name: Imaginary axis label
  summary: 虚轴标签 Imaginary Amplitude（默认）
  group: 坐标轴选项卡
- name: Oversampling method
  summary: 过采样方法 None（默认）| Input interpolation | Histogram interpolation
  group: 2D Histogram Tab
- name: Color scale
  summary: 颜色刻度 Linear（默认）| Logarithmic
  group: 2D Histogram Tab
- name: Export measurements, histograms and bathtub curves
  summary: 导出测量值、直方图和浴盆曲线 Off（默认）| off
  group: Export Tab
- name: Variable name
  summary: 变量名 EyeData（默认）
  group: Export Tab
- name: Figure color
  summary: 图窗颜色 black（默认）
  group: Style Dialog Box
- name: Axes colors
  summary: 坐标轴颜色 black | gray（默认）
  group: Style Dialog Box
- name: Line
  summary: 线图的线型、线宽和颜色 continuous | 0.5 | yellow（默认）
  group: Style Dialog Box
- name: Marker
  summary: 数据点标记 None（默认）| ...
  group: Style Dialog Box
- name: Colormap
  summary: 直方图的颜色图 Hot（默认）| Parula | Jet | HSV | Cool | Spring Summer | Autumn | Winter | Gray | Bone | Copper | Pink | Lines
    | Custom
  group: Style Dialog Box
- name: Eye level boundaries
  summary: 计算眼高的时间范围 [40 60]（默认）| 二元素向量
  group: 测量设置窗格
- name: Decision boundary
  summary: 幅度电平阈值 0（默认）| 标量
  group: 测量设置窗格
- name: Rise/Fall thresholds
  summary: 上升和下降转换的幅度电平 [10 90]（默认）| 二元素向量
  group: 测量设置窗格
- name: Hysteresis
  summary: 水平交叉的幅度容差 0（默认）| 标量
  group: 测量设置窗格
- name: BER threshold
  summary: 用于眼图测量的 BER 1e-12（默认）| 从 0 到 0.5 的非负标量
  group: 测量设置窗格
- name: Bathtub BERs
  summary: 用于计算浴盆曲线开口的 BER 值 [0.5 0.1 0.01 0.001 0.0001 1e-05 1e-06 1e-07 1e-08 1e-09 1e-10 1e-11 1e-12]（默认）| 向量
  group: 测量设置窗格
- name: Measurement delay
  summary: 从测量中丢弃的初始数据持续时间 0（默认）| 非负标量
  group: 测量设置窗格
```

### 主选项卡

### **Display mode** — 显示模式 `Line plot`（默认）| `2D color Histogram`

眼图的显示模式，指定为 `Line
plot` 或 `2D color histogram`。
选择 `2D color histogram` 会使直方图选项卡可用。

**可调：** 是

### **Enable measurements** — 启用测量 `off`（默认）| `on`

选中此复选框可启用输入信号的眼图测量。

### **Show horizontal (jitter) histogram** — 显示抖动直方图 `off`（默认）| `on`

选择此单选按钮可显示抖动直方图。也可以通过工具栏上的直方图按钮下拉菜单访问。

#### 依赖关系

当 **Display mode** 为 `2D color histogram` 且选中 **Enable measurements** 时，此参数可用。

### **Show vertical (noise) histogram** — 显示噪声直方图 `off`（默认）| `on`

选择此单选按钮可显示噪声直方图。也可以通过工具栏上的直方图按钮下拉菜单访问。

#### 依赖关系

当 **Display mode** 为 `2D color histogram` 且选中 **Enable measurements** 时，此参数可用。

### **Do not show horizontal or vertical histogram** — 不显示水平或垂直直方图 `on`（默认）| `off`

选择此单选按钮可既不显示噪声直方图也不显示抖动直方图。

#### 依赖关系

当 **Display mode** 为 `2D color histogram` 且选中 **Enable measurements** 时，此参数可用。

### **Show horizontal bathtub curve** — 显示水平浴盆曲线 `off`（默认）| `on`

选中此复选框可显示水平浴盆曲线。也可以通过工具栏上的浴盆曲线按钮访问。

#### 依赖关系

当选中 **Enable measurements** 时，此参数可用。

### **Show vertical bathtub curve** — 显示垂直浴盆曲线 `off`（默认）| `on`

选中此复选框可显示垂直浴盆曲线。也可以通过工具栏上的浴盆曲线按钮访问。

#### 依赖关系

当选中 **Enable measurements** 时，此参数可用。

### **Eye diagram to display** — 要显示的眼图 `Real only`（默认）| `Real and imaginary`

选择 `Real only` 或 `Real and imaginary` 以显示一个或两个眼图。要进行眼图测量，此参数必须为 `Real only`。

**可调：** 是

### **Color fading** — 颜色渐隐 `off`（默认）| `on`

选中此复选框可使显示中的点随着首次绘制后时间间隔的增加而渐隐。

**可调：** 是

#### 依赖关系

此参数仅在 **Display mode** 为 `Line plot` 时可用。

### **Samples per symbol** — 每符号采样数 8（默认）| 正整数

每符号的采样数，指定为正整数。与 **Symbols per trace** 一起使用以确定每条迹线的采样数。

**可调：** 是

### **Sample offset** — 采样偏移 0（默认）| 非负整数

采样偏移，指定为小于 **Samples per symbol** 与 **Symbols per trace** 乘积的非负整数。该偏移提供了在绘制第一个点之前要省略的采样数。

**可调：** 是

### **Symbols per trace** — 每条迹线的符号数 2（默认）| 正整数

每条迹线绘制的符号数，指定为正整数。

**可调：** 是

### **Traces to display** — 要显示的迹线数 40（默认）| 正整数

绘制的迹线数，指定为正整数。

**可调：** 是

#### 依赖关系

此参数仅在 **Display mode** 为 `Line plot` 时可用。

### 坐标轴选项卡

### **Title** — 标题标签 *None*（默认）

出现在眼图绘图上方的标签。

**可调：** 是

### **Show grid** — 切换示波器网格 `on`（默认）| `off`

切换此复选框以打开和关闭网格。

**可调：** 是

### **Y-limits (Minimum)** — *y* 轴下限 `-1.1`（默认）| 标量

*y* 轴的最小值。

**可调：** 是

### **Y-limits (Maximum)** — *y* 轴上限 `1.1`（默认）| 标量

*y* 轴的最大值。

**可调：** 是

### **Real axis label** — 实轴标签 `Real Amplitude`（默认）

示波器沿实轴显示的文本。

**可调：** 是

### **Imaginary axis label** — 虚轴标签 `Imaginary Amplitude`（默认）

示波器沿虚轴显示的文本。

**可调：** 是

### 2D Histogram Tab

当您点击直方图按钮或将显示模式设置为 `2D color histogram` 时，2D 直方图选项卡可用。

### **Oversampling method** — 过采样方法 `None`（默认）| `Input interpolation` | `Histogram interpolation`

过采样方法，指定为 `None`、`Input interpolation` 或 `Histogram interpolation`。

要尽可能快地绘制眼图，请将 **Oversampling method** 设置为 `None`。不进行过采样的缺点是，当每条迹线的样本数较少时，绘图看起来会有像素化。要使用较少的每条迹线样本数创建更平滑、像素化更少的绘图，请将 **Oversampling method** 设置为 `Input interpolation` 或 `Histogram interpolation`。`Input interpolation` 是两种插值方法中较快的一种，在信噪比（SNR）较高时能产生良好的结果。在 SNR 较低时，不建议使用此过采样方法，因为它会引入直方图范围中心的偏差。`Histogram interpolation` 不如其他技术快，但即使在 SNR 较低时也能提供良好的结果。

**可调：** 是

### **Color scale** — 颜色刻度 `Linear`（默认）| `Logarithmic`

直方图绘图的颜色刻度，指定为 `Linear` 或 `Logarithmic`。如果眼图的某些区域包含不成比例的点数，请将 **Color scale** 设置为 `Logarithmic`。

**可调：** 是

工具栏包含一个直方图重置按钮 ，用于重置内部直方图缓冲区并清除显示。当显示模式设置为 `Line plot` 时，此按钮不可用。

### Export Tab

### **Export measurements, histograms and bathtub curves** — 导出测量值、直方图和浴盆曲线 `Off`（默认）| `off`

选中此复选框可将眼图测量值导出到 MATLAB® 工作区。

**可调：** 是

### **Variable name** — 变量名 `EyeData`（默认）

指定保存眼图测量值的变量名称。数据保存为具有以下字段的结构体：

- `MeasurementSettings`
- `Measurements`
- `JitterHistogram`
- `NoiseHistogram`
- `HorizontalBathtub`
- `VerticalBathtub`
- `BlockName`

**可调：** 是

### Style Dialog Box

在 **Style** 对话框中，您可以自定义活动显示的样式。您可以更改包含显示的图窗颜色、显示坐标轴的前景和背景颜色，以及显示中线条的属性。要打开此对话框，请选择 **View** > **Style**。

### **Figure color** — 图窗颜色 `black`（默认）

指定示波器图窗的背景颜色。

### **Axes colors** — 坐标轴颜色 `black` | `gray`（默认）

指定坐标轴的填充和线条颜色。

### **Line** — 线图的线型、线宽和颜色 `continuous` | `0.5` | `yellow`（默认）

指定所显示信号的线型、线宽和线条颜色。

#### 依赖关系

此参数仅在 **Display mode** 为 `Line plot` 时可用。

### **Marker** — 数据点标记 `None`（默认）| ...

所选信号的数据点标记，指定为此表数据点标记中的一个选项。此参数类似于 MATLAB Handle Graphics® 绘图对象的 `Marker` 属性。

| 标识符 | 标记类型 |
| --- | --- |
| none | 无标记（默认） |
|  | 圆形 |
|  | 方形 |
|  | 十字 |
|  | 点 |
|  | 加号 |
|  | 星号 |
|  | 菱形 |
|  | 向下三角形 |
|  | 向上三角形 |
|  | 向左三角形 |
|  | 向右三角形 |
|  | 五角星（五芒星） |
|  | 六角星（六芒星） |

#### 依赖关系

此参数仅在 **Display mode** 为 `Line plot` 时可用。

### **Colormap** — 直方图的颜色图 `Hot`（默认）| `Parula` | `Jet` | `HSV` | `Cool` | `Spring` `Summer` | `Autumn` | `Winter` | `Gray` | `Bone` | `Copper` | `Pink` | `Lines` | `Custom`

将直方图的颜色图指定为以下方案之一：`Parula`、`Jet`、`HSV`、`Hot`、`Cool`、`Spring`、`Summer`、`Autumn`、`Winter`、`Gray`、`Bone`、`Copper`、`Pink`、`Lines` 或 `Custom`。如果选择 `Custom`，将弹出一个对话框，您可以在其中输入代码来指定自己的颜色图。

#### 依赖关系

此参数仅在 **Display mode** 为 `2D color histogram` 时可用。

### 测量设置窗格

要更改测量设置，首先选择 **Enable measurements**。然后，在 **Eye Measurements** 窗格中，点击 **Settings** 旁边的箭头。您可以控制这些测量设置。

### **Eye level boundaries** — 计算眼高的时间范围 `[40 60]`（默认）| 二元素向量

用于计算眼高的时间范围，指定为二元素向量。这些值以符号持续时间的百分比表示。

**可调：** 是

### **Decision boundary** — 幅度电平阈值 `0`（默认）| 标量

幅度电平阈值，以 V 为单位，指定为标量。此参数分隔水平（抖动）直方图的不同信号区域。此参数可调，但当参数变化时抖动直方图会重置。

对于非归零（NRZ）信号，将 **Decision boundary** 设置为 0。对于归零（RZ）信号，将 **Decision boundary** 设置为最大幅度的一半。

**可调：** 是

### **Rise/Fall thresholds** — 上升和下降转换的幅度电平 `[10 90]`（默认）| 二元素向量

上升和下降转换的幅度电平，指定为二元素向量。这些值以眼幅度的百分比表示。此参数可调，但当参数变化时上升和下降阈值的交叉直方图会重置。

**可调：** 是

### **Hysteresis** — 水平交叉的幅度容差 `0`（默认）| 标量

水平交叉的幅度容差，以 V 为单位，指定为标量。增加迟滞以对噪声引起的杂散交叉提供更多容差。此参数可调，但当参数变化时抖动以及上升和下降直方图会重置。

**可调：** 是

### **BER threshold** — 用于眼图测量的 BER `1e-12`（默认）| 从 0 到 0.5 的非负标量

用于眼图测量的 BER，指定为从 0 到 0.5 的非负标量。该值用于测量随机抖动、总抖动、水平眼开度和垂直眼开度。

**可调：** 是

### **Bathtub BERs** — 用于计算浴盆曲线开口的 BER 值 `[0.5 0.1 0.01 0.001 0.0001 1e-05 1e-06 1e-07 1e-08 1e-09 1e-10 1e-11 1e-12]`（默认）| 向量

用于计算浴盆曲线开口的 BER 值，指定为元素范围从 0 到 0.5 的向量。水平眼开度和垂直眼开度针对此参数指定的每个值进行计算。

**可调：** 是

#### 依赖关系

要启用此参数，请选择 **Show horizontal bathtub curve**、**Show vertical bathtub curve** 或两者。

### **Measurement delay** — 从测量中丢弃的初始数据持续时间 `0`（默认）| 非负标量

从测量中丢弃的初始数据持续时间，以秒为单位，指定为非负标量。
## 所属库

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当对包含此模块的系统执行代码生成时，此模块会从生成的代码中排除。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可视化，但不包含在硬件实现中。

## 版本历史

**在 R2014a 中引入**

### R2025a：眼图分析已被移除

眼图分析，如测量、直方图和浴盆曲线，已从 Eye Diagram 模块中移除。要访问这些功能，您需要 Signal Integrity Toolbox™、SerDes Toolbox™ 或 Mixed-Signal Blockset™ 的许可证。

- 使用 `eyeDiagramSI`（Signal Integrity Toolbox）系统对象、Eye Measurement（Signal Integrity Toolbox）模块、`eyeContour`（Signal Integrity Toolbox）对象和 `eyeMask`（Signal Integrity Toolbox）对象来测量眼图指标，如眼高、眼宽、眼面积、线性度、垂直眼闭合（VEC）和通道工作裕量（COM）。
- 有关 Communications Toolbox™ 中的新眼图模块，请参阅 Eye Diagram。

### R2023b：眼图分析将被移除

眼图分析，如测量、直方图和浴盆曲线，将在未来版本中从 Eye Diagram 模块中移除。要访问这些功能：

- 参阅 Measurements and Testbenches（Mixed-Signal Blockset）以分析性能指标，如相位噪声、参考杂散和分数杂散、孔径抖动、时序损伤和锁定时间。
- 参阅 Get Started with SerDes Toolbox 导出 Simulink 模型并评估浴盆曲线和通道工作裕量（COM）等指标，包括抖动和串扰的影响。
- 参阅 Analyze Serial Links with Serial Link Designer（Signal Integrity Toolbox）和 Analyze Parallel Links with Parallel Link Designer（Signal Integrity Toolbox）以了解如何设置拓扑或使用预定义的“套件”来运行感兴趣的仿真。使用 Signal Integrity Viewer 应用查看波形、浴盆曲线、测量结果等。
- 有关新的眼图模块，请参阅 Eye Diagram。

## 描述

（已移除）显示时域信号的眼图

Eye Diagram 模块显示调制信号的多个轨迹以生成眼图。您可以使用该模块揭示信号的调制特性，例如脉冲整形或通道失真的影响。

Eye Diagram 模块有一个输入端口。此模块接受列向量或标量输入信号。该模块接受以下数据类型的信号：double、single、基整数和定点。在模块显示结果之前，所有数据类型都被转换为 double。

要修改眼图显示，请选择 **View** > **Configuration Properties** 或点击 **Configuration Properties** 按钮（）。然后选择 **Main**、**2D color histogram**、**Axes** 或 **Export** 选项卡并修改设置。
