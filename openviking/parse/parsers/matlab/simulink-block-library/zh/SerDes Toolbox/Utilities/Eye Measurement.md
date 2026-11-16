---
type: simulink-block
title: 'Eye Measurement'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'eyemeasurement'
documentation_source_path: 'ref/eyemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Eye Measurement

## 端口

### 输入

### **data** — 输入数据标量

用于构造眼图的输入数据，指定为标量。

**数据类型：** `double`

### **clock** — 输入数据的采样时钟标量

输入数据的采样时钟信号，指定为标量。眼图的窗口以时钟边沿为中心。

如果您在 **clock** 端口使用时钟时间，则新的时钟时间必须位于当前仿真时间的 1 UI 之内。时钟时间应出现在对应眼图张开的中心。

#### 依赖项

要启用此端口，请在 **配置** 选项卡中选择 **Enable clock input port**。

**数据类型：** `double`

### **thresholds** — 用于分隔符号的符号阈值 向量 | 矩阵

符号阈值，用于在构建眼图时分隔符号。如果您提供此信息，它会提高 PAMn 指标的稳健性。

如果 **thresholds** 端口处的数据是向量，则在测量期间所有时间点都使用同一向量。如果 **thresholds** 端口处的数据是矩阵，则该模块对每个时间点使用一个向量。

#### 依赖项

要启用此端口，请在 **配置** 选项卡中选择 **Enable threshold input port**。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上的**准备**库中，选择**属性检查器**。

### 配置

### **Enable threshold input port** — 启用阈值输入端口 on (默认) | off

选中此选项可启用阈值输入端口。默认情况下，此端口处于启用状态。

### **Modulation** — 眼图中的符号级数 `2` (默认) | 非负整数标量

眼图中预期的符号级数，指定为非负整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Modulation` |
| **类型：** character vector |
| **值：** nonnegative integer scalar |
| **默认值：** `2` |

### **Symbol thresholds** — 符号阈值 `auto` (默认) | 实值向量

要使用的符号阈值，指定为实值向量。如果未提供阈值输入，请使用此参数指定符号阈值。

#### 依赖项

要启用此参数，请取消选择 **Enable threshold input port**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SymbolThresholds` |
| **类型：** character vector |
| **值：** real valued vector |
| **默认值：** `auto` |

### **Enable clock input port** — 启用时钟输入端口 on (默认) | off

选中此选项可启用时钟输入端口。默认情况下，此端口处于启用状态。

### **Clock type** — 确定如何对波形时钟信号进行采样 `Rising` (默认) | `Falling` | `Both` | `Times`

确定如何对波形时钟信号进行采样：

- `Rising` — 在时钟波形的上升沿对数据波形进行采样。
- `Falling` — 在时钟波形的下降沿对数据波形进行采样。
- `Both` — 在时钟波形的上升沿和下降沿对数据波形进行采样。
- `Times` — 在时钟信号指定的时间值处对数据波形进行采样。

#### 编程用法

|  |
| --- |
| **模块参数：** `ClockType` |
| **类型：** character vector |
| **值：** `Rising` | `Falling` | `Both` | `Times` |
| **默认值：** `Rising` |

### **Clock threshold** — 波形时钟的边沿检测阈值 `0` (默认) | 实数标量

波形时钟的边沿检测阈值，指定为实数标量。

#### 依赖项

要启用此参数，请将 **Enable clock input port** 选项设置为 on，并将 **Clock type** 设置为 `Rising`、`Falling` 或 `Both`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ClockThreshold` |
| **类型：** character vector |
| **值：** real scalar |
| **默认值：** `0` |

### **Clock mode** — 表示数据如何由恢复时钟捕获 `Clocked` (默认) | `Ideal` | `Convolved`

从系统角度表示数据如何由恢复时钟捕获。

- `Clocked` — 使用来自时钟恢复电路输出的时钟，在判决锁存器的输入处捕获数据。
- `Ideal` — 使用理想参考时钟源捕获数据和时钟。
- `Convolved` — 在正常模式下捕获的数据眼图和时钟 PDF 进行卷积，以呈现看起来如同在 `Clocked` 模式下运行仿真所得到的眼图和时钟。

有关详细信息，请参阅 Clock Modes (Signal Integrity Toolbox)。

**注意**

如果将 **Enable clock input port** 选项设置为 off，则 **Clock mode** 会设置为 `Ideal`，并且无法更改。

#### 编程用法

|  |
| --- |
| **模块参数：** `ClockMode` |
| **类型：** character vector |
| **值：** `Clocked` | `Ideal` | `Convolved` |
| **默认值：** `Clocked` |

### **Clock phase offset** — 用于移动时钟 PDF 的相位延迟 `0` (默认) | 非负实数标量

用于移动时钟 PDF 的相位延迟，指定为非负实数标量，以秒、样本或 UI 为单位。

当您将 **Clock mode** 设置为 `clocked` 时，**Clock phase offset** 适用于您提供的外部时钟。如果未提供外部时钟，则该模块会生成从理想时钟派生的时钟 PDF。

#### 编程用法

|  |
| --- |
| **模块参数：** `ClockPhaseOffset` |
| **类型：** character vector |
| **值：** nonnegative real scalar |
| **默认值：** `0` |

### **Window phase offset** — 理想时钟边沿与定时原点之间的延迟 `0` (默认) | 非负实数标量

理想时钟边沿与定时原点之间的延迟，指定为非负实数标量，以秒、样本或 UI 为单位。

当您将 **Clock mode** 设置为 `Ideal` 或 `Convolved` 时，**Window phase offset** 用于确定窗口相对于内部理想参考时钟的位置。

#### 依赖项

要启用此参数，请将 **Clock mode** 设置为 `Ideal` 或 `Convolved`。

#### 编程用法

|  |
| --- |
| **模块参数：** `WindowPhaseOffset` |
| **类型：** character vector |
| **值：** nonnegative real scalar |
| **默认值：** `0` |

### **Symbols per diagram** — 眼图的宽度（以符号为单位） `2` (默认) | 标量

眼图的宽度（以符号为单位），指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `SymbolsperDiagram` |
| **类型：** character vector |
| **值：** scalar |
| **默认值：** `2` |

### **Amplitude range** — 眼图中的最小和最大眼幅度 `[]` (默认) | 二元素向量

眼图中包含的最小和最大幅度，指定为二元素向量。

#### 编程用法

|  |
| --- |
| **模块参数：** `AmplitudeRange` |
| **类型：** character vector |
| **值：** two-element vector |
| **默认值：** `[]` |

### **Amplitude bins** — 眼图中的幅度箱数 `257` (默认) | 正整数标量

眼图中的幅度箱数，指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `AmplitudeBins` |
| **类型：** character vector |
| **值：** positive integer scalar |
| **默认值：** `257` |

### **Time bins** — 眼图中的时间箱数 `256` (默认) | 正整数标量

眼图中的时间箱数，指定为正整数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `TimeBins` |
| **类型：** character vector |
| **值：** positive integer scalar |
| **默认值：** `256` |

### **Hold off time** — 测量分析前的延迟 `0` (默认) | 非负实数标量

延迟测量分析以避免瞬态污染，指定为非负实数标量，以秒、样本或 UI 为单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** character vector |
| **值：** nonnegative real scalar |
| **默认值：** `0` |

### **Symbol time** — 一个符号的时间 `16e-9` (默认) | 正实数标量

一个符号的时间，指定为正实数标量。

**注意**

**Symbol time** 必须能被 **Sample time** 整除。

#### 编程用法

|  |
| --- |
| **模块参数：** `SymbolTime` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `16e-9` |

### **Sample time** — 一个样本的时间 `[1e-9, 0]` (默认) | 二元素向量 | 标量

一个样本的时间，指定为正实数标量。

如果 **Sample time** 指定为二元素向量，则它表示 Simulink 中的固定步长离散采样时间。

如果 **Sample time** 指定为标量，则它表示 SerDes Toolbox™ 中使用的采样间隔。

**注意**

**Symbol time** 必须能被 **Sample time** 整除。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** two-element vector | scalar |
| **默认值：** `[1e-9, 0]` |

### 指标设置

### **Add Metric** — 添加要计算的新指标按钮

单击以添加要计算的新眼图指标。您可以定义在哪个点计算哪个指标、符号错误率以及外推方法。

### **Remove Selected Metrics** — 移除选定的指标按钮

单击以移除选定的眼图指标，从而聚焦于感兴趣的区域。

### **Store results in base workspace** — 将指标结果存储到基础工作区 off (默认) | on

选中此选项可在仿真结束时将指标计算结果存储到基础工作区。

### **Metrics variable name** — 存储测量结果的指标变量名称 `ans` (默认) | string

在基础工作区中存储测量结果的指标变量名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `MetricsVariableName` |
| **类型：** character vector |
| **值：** string |
| **默认值：** `ans` |

### **Export to file** — 将仿真结果导出到文件按钮

单击以将仿真结果导出到文件，以便保存供以后使用。

### **Export to base workspace** — 将仿真结果导出到基础工作区按钮

单击以将仿真结果导出到基础工作区。

### 眼图模板

### **Eye mask type** — 眼图模板的形状 `Off` (默认) | `Rectangle` | `Diamond` | `Hexagon` | `Custom`

用于模板裕量测量的眼图模板形状。有关详细信息，请参阅 `eyeMask` (Mixed-Signal Blockset)。

### **W1 (UI)** — 矩形、菱形眼图模板的宽度，以及六边形眼图模板中心的宽度 `0.2` (默认) | 正实数标量

矩形或菱形眼图模板的宽度，或者六边形眼图模板中心的宽度，指定为正实数标量。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 编程用法

|  |
| --- |
| **模块参数：** `W1` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `0.2` |

### **W2 (UI)** — 六边形眼图模板顶部和底部的宽度 `0.1` (默认) | 正实数标量

六边形眼图模板顶部和底部的宽度，指定为正实数标量。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Hexagon`。

#### 编程用法

|  |
| --- |
| **模块参数：** `W2` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `0.1` |

### **H** — 矩形、菱形或六边形眼图模板的高度 `0.1` (默认) | 正实数标量

矩形、菱形或六边形眼图模板的高度，指定为正实数标量。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 编程用法

|  |
| --- |
| **模块参数：** `H` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认值：** `0.1` |

### **Position mask in eye** — 模板形状原点在眼图中的位置 `At clock` (默认) | `For best height margin` | `For best width margin`

定义模板形状原点在眼图中的位置。您可以将其定位于时钟处，或者定位于最佳眼高或眼宽处。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 编程用法

|  |
| --- |
| **模块参数：** `PositionMaskInEye` |
| **类型：** character vector |
| **值：** `At clock` | `For best height margin` | `For best width margin` |
| **默认值：** `At clock` |

### **Custom eye mask** — 从眼图模板对象定义自定义眼图模板 `[]` (默认) | object

从眼图模板对象定义自定义眼图模板。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomEyeMask` |
| **类型：** character vector |
| **值：** object |
| **默认值：** `[]` |

### **Margin SER** — 用于测量眼图模板裕量的符号错误率 `1e-5` | 范围 [0,1] 内的非负实数标量

模块测量眼图模板裕量时的符号错误率 (SER)，指定为范围 [0,1] 内的非负实数标量。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond`、`Hexagon` 或 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：** `MarginSER` |
| **类型：** character vector |
| **值：** nonnegative real scalar in the range [0,1] |
| **默认值：** `1e-5` |

### **Margin extrapolation** — 用于生成眼图轮廓的外推方法 `none` (默认) | `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima`

用于生成测量眼图裕量所用眼图轮廓的外推方法。该模块通过相邻箱之间的插值将眼图外推到指定的 SER。有关详细信息，请参阅 Extrapolation (Mixed-Signal Blockset)。

**注意**

此功能需要 Signal Integrity Toolbox™、Optimization Toolbox™ 或 Curve Fitting Toolbox™ 许可证。许可证要求按性能顺序列出，其中 Signal Integrity Toolbox 提供最快的计算。

#### 依赖项

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond`、`Hexagon` 或 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数：** `MarginExtrapolation` |
| **类型：** character vector |
| **值：** `none` | `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima` |
| **默认值：** `none` |

### **Mask variable name** — 用于导出模板的模板变量名称 `ans` (默认) | string

用于将模板导出到基础工作区的模板变量名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaskVariableName` |
| **类型：** character vector |
| **值：** string |
| **默认值：** `ans` |

### **Export mask to file** — 将模板导出到文件按钮

单击以将模板导出到文件，以便保存供以后使用。

### **Export mask to base workspace** — 将模板导出到基础工作区按钮

单击以将模板导出到基础工作区。

### 绘图设置

### **Show plots at end of simulation** — 在仿真结束时自动显示绘图 on (默认) | off

选中此选项可在仿真结束时自动将仿真结果显示为绘图。您可以定义要生成的绘图类型，包括眼图、时钟和浴盆图。

### **Plot grouping** — 定义绘图如何分组在一起 `Subplot on same figure` (默认) | `One figure per plot`

定义绘图如何分组在一起。

### **Add Plot** — 添加要显示的新绘图按钮

单击以添加要显示的新绘图。

### **Remove Selected Plots** — 移除选定的绘图按钮

单击以移除选定的绘图，从而聚焦于感兴趣的区域。

### **Show Plots** — 显示绘图按钮

单击以显示绘图。

## 所属库

Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities Signal Integrity Toolbox / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025b: 移动时钟 PDF 或眼图窗口

使用 **时钟相位偏移** 参数移动时钟 PDF。当 **时钟模式** 为 clocked 时，这有助于将眼图居中；在其他模式下，这有助于相对于眼图移动时钟 PDF。使用 **窗口相位偏移** 参数在 ideal 或 convolved 时钟模式下移动眼图窗口。

### R2025a: 更新的外推方法

选择不同的外推方法，以在更改系统参数以满足您的要求时观察眼图指标的趋势。

## 描述

根据眼图计算指标

Eye Measurement 模块根据时域波形数据生成眼图，并根据生成的眼图计算指标。
