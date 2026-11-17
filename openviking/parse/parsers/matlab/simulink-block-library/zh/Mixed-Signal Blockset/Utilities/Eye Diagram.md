---
type: simulink-block
title: 'Eye Diagram'
family: 'utilities'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'legacyeyediagramscope'
documentation_source_path: 'ref/legacyeyediagramscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Eye Diagram

## 端口

### 输入

### **In** — 输入信号，标量 | 列向量

输入信号，指定为标量或列向量。

**数据类型：** `double`

## 参数

### 主选项卡

### **显示模式** — 显示模式 `Line plot` (默认) | `2D color Histogram`

眼图的显示模式，指定为 `Line plot` 或 `2D color histogram`。选择 `2D color histogram` 会使直方图选项卡可用。

**可调：** 是

### **启用测量** — 启用测量 `off` (默认) | `on`

选中此复选框以启用输入信号的眼图测量。

### **显示水平（抖动）直方图** — 显示抖动直方图 `off` (默认) | `on`

选择此单选按钮以显示抖动直方图。也可以通过工具栏上的直方图按钮下拉菜单访问。

#### 依赖关系

当 **显示模式** 为 `2D color histogram` 且选中 **启用测量** 时，此参数可用。

### **显示垂直（噪声）直方图** — 显示噪声直方图 `off` (默认) | `on`

选择此单选按钮以显示噪声直方图。也可以通过工具栏上的直方图按钮下拉菜单访问。

#### 依赖关系

当 **显示模式** 为 `2D color histogram` 且选中 **启用测量** 时，此参数可用。

### **不显示水平或垂直直方图** — 不显示水平或垂直直方图 `on` (默认) | `off`

选择此单选按钮以既不显示直方图噪声，也不显示直方图抖动。

#### 依赖关系

当 **显示模式** 为 `2D color histogram` 且选中 **启用测量** 时，此参数可用。

### **显示水平浴盆曲线** — 显示水平浴盆曲线 `off` (默认) | `on`

选中此复选框以显示水平浴盆曲线。也可以通过工具栏上的浴盆曲线按钮访问。

#### 依赖关系

当选中 **启用测量** 时，此参数可用。

### **显示垂直浴盆曲线** — 显示垂直浴盆曲线 `off` (默认) | `on`

选中此复选框以显示垂直浴盆曲线。也可以通过工具栏上的浴盆曲线按钮访问。

#### 依赖关系

当选中 **启用测量** 时，此参数可用。

### **要显示的眼图** — 要显示的眼图 `Real only` (默认) | `Real and imaginary`

选择 `Real only` 或 `Real and imaginary` 以显示一个或两个眼图。要进行眼图测量，此参数必须为 `Real only`。

**可调：** 是

### **颜色渐隐** — 颜色渐隐 `off` (默认) | `on`

选中此复选框可在显示中的点自首次绘制后的时间间隔增加时使其渐隐。

**可调：** 是

#### 依赖关系

仅当 **显示模式** 为 `Line plot` 时，此参数可用。

### **每符号采样数** — 每符号采样数 8 (默认) | 正整数

每符号采样数，指定为正整数。与 **每迹线符号数** 一起使用以确定每迹线的采样数。

**可调：** 是

### **采样偏移** — 采样偏移 0 (默认) | 非负整数

采样偏移，指定为小于 **每符号采样数** 与 **每迹线符号数** 乘积的非负整数。该偏移提供在绘制第一个点之前要省略的采样数。

**可调：** 是

### **每迹线符号数** — 每迹线符号数 2 (默认) | 正整数

每条迹线绘制的符号数，指定为正整数。

**可调：** 是

### **要显示的迹线数** — 要显示的迹线数 40 (默认) | 正整数

绘制的迹线数，指定为正整数。

**可调：** 是

#### 依赖关系

仅当 **显示模式** 为 `Line plot` 时，此参数可用。

### 坐标轴选项卡

### **标题** — 标题标签 *None* (默认)

出现在眼图绘图上方的标签。

**可调：** 是

### **显示网格** — 切换示波器网格 `on` (默认) | `off`

切换此复选框以打开和关闭网格。

**可调：** 是

### **Y 轴范围（最小值）** — *y* 轴的下限 `-1.1` (默认) | 标量

*y* 轴的最小值。

**可调：** 是

### **Y 轴范围（最大值）** — *y* 轴的上限 `1.1` (默认) | 标量

*y* 轴的最大值。

**可调：** 是

### **实轴标签** — 实轴标签 `Real Amplitude` (默认)

示波器沿实轴显示的文本。

**可调：** 是

### **虚轴标签** — 虚轴标签 `Imaginary Amplitude` (默认)

示波器沿虚轴显示的文本。

**可调：** 是

### 二维直方图选项卡

当您单击直方图按钮或将显示模式设置为 `2D color histogram` 时，二维直方图选项卡可用。

### **过采样方法** — 过采样方法 `None` (默认) | `Input interpolation` | `Histogram interpolation`

过采样方法，指定为 `None`、`Input interpolation` 或 `Histogram interpolation`。

要以尽可能快的速度绘制眼图，请将 **过采样方法** 设置为 `None`。不进行过采样的缺点是，当每迹线采样数较少时，绘图看起来会有像素化。要使用较少的每迹线采样数创建更平滑、像素化更少的绘图，请将 **过采样方法** 设置为 `Input interpolation` 或 `Histogram interpolation`。`Input interpolation` 是两种插值方法中较快的一种，并且在信噪比 (SNR) 较高时能产生良好结果。当 SNR 较低时，不建议使用此过采样方法，因为它会向直方图范围的中心引入偏差。`Histogram interpolation` 不如其他技术快，但即使 SNR 较低，它也能提供良好结果。

**可调：** 是

### **颜色标度** — 颜色标度 `Linear` (默认) | `Logarithmic`

直方图绘图的颜色标度，指定为 `Linear` 或 `Logarithmic`。如果眼图的某些区域包含不成比例的大量点，请将 **颜色标度** 设置为 `Logarithmic`。

**可调：** 是

工具栏包含一个直方图重置按钮 ，它会重置内部直方图缓冲区并清除显示。当显示模式设置为 `Line plot` 时，此按钮不可用。

### 导出选项卡

### **导出测量结果、直方图和浴盆曲线** — 导出测量结果、直方图和浴盆曲线 `Off` (默认) | `off`

选中此复选框以将眼图测量结果导出到 MATLAB® 工作区。

**可调：** 是

### **变量名** — 变量名 `EyeData` (默认)

指定保存眼图测量结果的变量名称。数据保存为具有以下字段的结构体：

- `MeasurementSettings`
- `Measurements`
- `JitterHistogram`
- `NoiseHistogram`
- `HorizontalBathtub`
- `VerticalBathtub`
- `BlockName`

**可调：** 是

### 样式对话框

在 **样式** 对话框中，可以自定义活动显示的样式。可以更改包含显示的图窗的颜色、显示坐标轴的背景色和前景色，以及显示中线的属性。要打开此对话框，请选择 **视图** > **样式**。

### **图窗颜色** — 图窗颜色 `black` (默认)

指定示波器图窗的背景色。

### **坐标轴颜色** — 坐标轴颜色 `black` | `gray` (默认)

指定坐标轴的填充色和线条颜色。

### **线** — 线图的线条样式、粗细和颜色 `continuous` | `0.5` | `yellow` (默认)

指定所显示信号的线条样式、线宽和线条颜色。

#### 依赖关系

仅当 **显示模式** 为 `Line plot` 时，此参数可用。

### **标记** — 数据点标记 `None` (默认) | ...

所选信号的数据点标记，指定为此表数据点标记中的选项之一。此参数类似于 MATLAB Handle Graphics® 绘图对象的 `Marker` 属性。

| 说明符 | 标记类型 |
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

仅当 **显示模式** 为 `Line plot` 时，此参数可用。

### **颜色图** — 直方图的颜色图 `Hot` (默认) | `Parula` | `Jet` | `HSV` | `Cool` | `Spring` `Summer` | `Autumn` | `Winter` | `Gray` | `Bone` | `Copper` | `Pink` | `Lines` | `Custom`

将直方图绘图的颜色图指定为以下方案之一：`Parula`、`Jet`、`HSV`、`Hot`、`Cool`、`Spring`、`Summer`、`Autumn`、`Winter`、`Gray`、`Bone`、`Copper`、`Pink`、`Lines` 或 `Custom`。如果选择 `Custom`，将弹出一个对话框，您可以在其中输入代码以指定自己的颜色图。

#### 依赖关系

仅当 **显示模式** 为 `2D color histogram` 时，此参数可用。

### 测量设置窗格

要更改测量设置，请先选中 **启用测量**。然后，在 **眼图测量** 窗格中，单击 **设置** 旁边的箭头。您可以控制这些测量设置。

### **眼图电平边界** — 用于计算眼图电平的时间范围 `[40 60]` (默认) | 二元素向量

用于计算眼图电平的时间范围，指定为二元素向量。这些值表示为符号持续时间的百分比。

**可调：** 是

### **判决边界** — 幅度电平阈值 `0` (默认) | 标量

以 V 为单位的幅度电平阈值，指定为标量。此参数分隔水平（抖动）直方图的不同信号区域。此参数可调，但当参数更改时，抖动直方图会重置。

对于非归零 (NRZ) 信号，将 **判决边界** 设置为 0。对于归零 (RZ) 信号，将 **判决边界** 设置为最大幅度的一半。

**可调：** 是

### **上升/下降阈值** — 上升和下降转换的幅度电平 `[10 90]` (默认) | 二元素向量

上升和下降转换的幅度电平，指定为二元素向量。这些值表示为眼图幅度的百分比。此参数可调，但当参数更改时，上升和下降阈值的交叉直方图会重置。

**可调：** 是

### **迟滞** — 水平交叉的幅度容差 `0` (默认) | 标量

以 V 为单位的水平交叉的幅度容差，指定为标量。增大迟滞可对由噪声引起的杂散交叉提供更大的容差。此参数可调，但当参数更改时，抖动直方图以及上升和下降直方图会重置。

**可调：** 是

### **BER 阈值** — 用于眼图测量的 BER `1e-12` (默认) | 从 0 到 0.5 的非负标量

用于眼图测量的 BER，指定为从 0 到 0.5 的非负标量。该值用于测量随机抖动、总抖动、水平眼开口和垂直眼开口。

**可调：** 是

### **浴盆曲线 BER** — 用于计算浴盆曲线开口的 BER 值 `[0.5 0.1 0.01 0.001 0.0001 1e-05 1e-06 1e-07 1e-08 1e-09 1e-10 1e-11 1e-12]` (默认) | 向量

用于计算浴盆曲线开口的 BER 值，指定为元素范围从 0 到 0.5 的向量。对于此参数指定的每个值，都会计算水平眼开口和垂直眼开口。

**可调：** 是

#### 依赖关系

要启用此参数，请选中 **显示水平浴盆曲线**、**显示垂直浴盆曲线** 或两者。

### **测量延迟** — 从测量中丢弃的初始数据持续时间 `0` (默认) | 非负标量

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

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2014a 中引入**

### R2025a：眼图分析已移除

眼图分析（例如测量、直方图和浴盆曲线）已从 Eye Diagram 模块中移除。要访问这些功能，您需要 Signal Integrity Toolbox™、SerDes Toolbox™ 或 Mixed-Signal Blockset™ 的许可证。

- 使用 `eyeDiagramSI` (Signal Integrity Toolbox) System object、Eye Measurement (Signal Integrity Toolbox) 模块、`eyeContour` (Signal Integrity Toolbox) 对象和 `eyeMask` (Signal Integrity Toolbox) 对象来测量眼图指标，例如眼高、眼宽、眼面积、线性度、垂直眼闭合 (VEC) 和通道工作裕量 (COM)。
- 对于 Communications Toolbox™ 中的新眼图模块，请参阅 Eye Diagram。

### R2023b：眼图分析将移除

眼图分析（例如测量、直方图和浴盆曲线）将在未来版本中从 Eye Diagram 模块中移除。要访问这些功能：

- 请参阅 Measurements and Testbenches 以分析性能指标，例如相位噪声、参考杂散和分数杂散、孔径抖动、时序损伤和锁定时间。
- 请参阅 Get Started with SerDes Toolbox (SerDes Toolbox) 以导出 Simulink 模型并评估指标，例如浴盆曲线和通道工作裕量 (COM)，包括抖动和串扰的影响。
- 请参阅 Analyze Serial Links with Serial Link Designer (Signal Integrity Toolbox) 和 Analyze Parallel Links with Parallel Link Designer (Signal Integrity Toolbox)，了解如何设置拓扑或使用预定义的 “kits” 之一来运行感兴趣的仿真。使用 Signal Integrity Viewer 应用查看波形、浴盆曲线、测量结果等。
- 对于新的眼图模块，请参阅 Eye Diagram。

## 描述

（已移除）显示时域信号的眼图

Eye Diagram 模块显示调制信号的多条迹线以生成眼图。您可以使用该模块揭示信号的调制特性，例如脉冲整形或信道失真的影响。 .

Eye Diagram 模块有一个输入端口。该模块接受列向量或标量输入信号。该模块接受具有以下数据类型的信号：double、single、base integer 和 fixed point。所有数据类型在模块显示结果之前都会转换为 double。

要修改眼图显示，请选择 **视图** > **配置属性** 或单击 **配置属性** 按钮 ()。然后选择 **主**、**2D color histogram**、**坐标轴** 或 **导出** 选项卡，并修改设置。
