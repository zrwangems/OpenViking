---
type: simulink-block
title: 'Eye Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
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

### **data** — 输入数据 标量

用于构建眼图的输入数据，指定为标量。

**数据类型：** `double`

### **clock** — 输入数据的采样时钟 标量

输入数据的采样时钟信号，指定为标量。眼图的窗口以时钟边沿为中心。

如果在 **clock** 端口使用时钟时间，新的时钟时间必须在当前仿真时间的 1 UI 范围内。时钟时间应出现在对应眼图的中心。

#### 依赖关系

要启用此端口，请在 **Configuration** 选项卡中选中 **Enable clock input port**。

**数据类型：** `double`

### **thresholds** — 用于分离符号的符号阈值 向量 | 矩阵

符号阈值，用于在构建眼图时分离符号。如果提供此信息，它会提高 PAMn 指标的鲁棒性。

如果 **thresholds** 端口的数据是向量，则在测量期间所有时间点使用相同的向量。如果 **thresholds** 端口的数据是矩阵，则模块对每个时间点使用一个向量。

#### 依赖关系

要启用此端口，请在 **Configuration** 选项卡中选中 **Enable threshold input port**。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 配置

### **Enable threshold input port** — 启用阈值输入端口 on（默认）| off

选中以启用阈值输入端口。默认情况下，此端口已启用。

### **Modulation** — 眼图中的符号电平数 `2`（默认）| 非负整数标量

眼图中预期的符号电平数，指定为非负整数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Modulation` |
| **类型**：character vector |
| **值**：nonnegative integer scalar |
| **默认值**：`2` |

### **Symbol thresholds** — 符号阈值 `auto`（默认）| 实值向量

要使用的符号阈值，指定为实值向量。如果未提供阈值输入，请使用此参数指定符号阈值。

#### 依赖关系

要启用此参数，请取消选中 **Enable threshold input port**。

#### 编程使用

|  |
| --- |
| **模块参数：** `SymbolThresholds` |
| **类型**：character vector |
| **值**：real valued vector |
| **默认值**：`auto` |

### **Enable clock input port** — 启用时钟输入端口 on（默认）| off

选中以启用时钟输入端口。默认情况下，此端口已启用。

### **Clock type** — 确定如何对波形时钟信号进行采样 `Rising`（默认）| `Falling` | `Both` | `Times`

确定如何对波形时钟信号进行采样：

- `Rising` — 在时钟波形的上升沿对数据波形进行采样。
- `Falling` — 在时钟波形的下降沿对数据波形进行采样。
- `Both` — 在时钟波形的上升沿和下降沿对数据波形进行采样。
- `Times` — 在时钟信号指定的时间值处对数据波形进行采样。

#### 编程使用

|  |
| --- |
| **模块参数：** `ClockType` |
| **类型**：character vector |
| **值**：`Rising` | `Falling` | `Both` | `Times` |
| **默认值**：`Rising` |

### **Clock threshold** — 波形时钟的边沿检测阈值 `0`（默认）| 实标量

波形时钟的边沿检测阈值，指定为实标量。

#### 依赖关系

要启用此参数，请将 **Enable clock input port** 选项设置为 on，并将 **Clock type** 设置为 `Rising`、`Falling` 或 `Both`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ClockThreshold` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`0` |

### **Clock mode** — 表示数据如何由恢复时钟捕获 `Clocked`（默认）| `Ideal` | `Convolved`

从系统角度表示数据如何由恢复时钟捕获。

- `Clocked` — 数据在判决锁存器输入端使用时钟恢复电路输出的时钟进行捕获。
- `Ideal` — 数据和时钟使用理想参考时钟源进行捕获。
- `Convolved` — 在正常模式下捕获的数据眼图和时钟 PDF 进行卷积，以呈现如同在时钟模式下运行仿真时的眼图和时钟。

有关详细信息，请参阅 Clock Modes (Signal Integrity Toolbox)。

**注意**

如果将 **Enable clock input port** 选项设置为 off，
**Clock mode** 将设置为 `Ideal`，且无法更改。

#### 编程使用

|  |
| --- |
| **模块参数：** `ClockMode` |
| **类型**：character vector |
| **值**：`Clocked` | `Ideal` | `Convolved` |
| **默认值**：`Clocked` |

### **Clock phase offset** — 移动时钟 PDF 的相位延迟 `0`（默认）| 非负实数标量

用于移动时钟 PDF 的相位延迟，指定为非负实数标量，单位为秒、采样点或 UI。

当将 **Clock mode** 设置为 `clocked` 时，**Clock phase offset** 适用于您提供的外部时钟。如果您不提供外部时钟，该模块将生成由理想时钟导出的时钟 PDF。

#### 编程使用

|  |
| --- |
| **模块参数：** `ClockPhaseOffset` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`0` |

### **Window phase offset** — 理想时钟边沿与定时原点之间的延迟 `0`（默认）| 非负实数标量

理想时钟边沿与定时原点之间的延迟，指定为非负实数标量，单位为秒、采样点或 UI。

当将 **Clock mode** 设置为 `Ideal` 或 `Convolved` 时，**Window phase offset** 用于确定窗口相对于内部理想参考时钟的位置。

#### 依赖关系

要启用此参数，请将 **Clock mode** 设置为 `Ideal` 或 `Convolved`。

#### 编程使用

|  |
| --- |
| **模块参数：** `WindowPhaseOffset` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`0` |

### **Symbols per diagram** — 眼图的宽度（以符号为单位） `2`（默认）| 标量

眼图的宽度（以符号为单位），指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `SymbolsperDiagram` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`2` |

### **Amplitude range** — 眼图中的最小和最大眼幅度 `[]`（默认）| 二元素向量

眼图中包含的最小和最大幅度，指定为二元素向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `AmplitudeRange` |
| **类型**：character vector |
| **值**：two-element vector |
| **默认值**：`[]` |

### **Amplitude bins** — 眼图中的幅度 bin 数量 `257`（默认）| 正整数标量

眼图中的幅度 bin 数量，指定为正整数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `AmplitudeBins` |
| **类型**：character vector |
| **值**：positive integer scalar |
| **默认值**：`257` |

### **Time bins** — 眼图中的时间 bin 数量 `256`（默认）| 正整数标量

眼图中的时间 bin 数量，指定为正整数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `TimeBins` |
| **类型**：character vector |
| **值**：positive integer scalar |
| **默认值**：`256` |

### **Hold off time** — 测量分析前的延迟 `0`（默认）| 非负实数标量

延迟测量分析以避免瞬态干扰，指定为非负实数标量，单位为秒、采样点或 UI。

#### 程序化使用

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `0` |

### **Symbol time** — 一个符号的时间 `16e-9`（默认）| 正实数标量

一个符号的时间，指定为正实数标量。

**注意**

**Symbol time** 必须能被 **Sample time** 整除。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SymbolTime` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `16e-9` |

### **Sample time** — 一个采样点的时间 `[1e-9, 0]`（默认）| 二元素向量 | 标量

一个采样点的时间，指定为正实数标量。

如果 **Sample time** 指定为二元素向量，则表示 Simulink 中的固定步长离散采样时间。

如果 **Sample time** 指定为标量，则表示 SerDes Toolbox™ 中使用的采样间隔。

**注意**

**Symbol time** 必须能被 **Sample time** 整除。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 二元素向量 | 标量 |
| **默认值：** `[1e-9, 0]` |

### 指标设置

### **Add Metric** — 添加新指标以进行计算 按钮

点击以添加新的眼图指标进行计算。您可以定义在哪个点计算哪个指标、符号错误率以及外推方法。

### **Remove Selected Metrics** — 移除所选指标 按钮

点击以移除所选眼图指标，以聚焦于感兴趣的区域。

### **Store results in base workspace** — 将指标结果存储到基础工作区 关（默认）| 开

选择以在仿真结束时将指标计算结果存储到基础工作区。

### **Metrics variable name** — 存储测量结果的指标变量名称 `ans`（默认）| 字符串

在基础工作区中存储测量结果的指标变量名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MetricsVariableName` |
| **类型：** 字符向量 |
| **值：** 字符串 |
| **默认值：** `ans` |

### **Export to file** — 将仿真结果导出到文件 按钮

点击以将仿真结果导出到文件，以便日后使用。

### **Export to base workspace** — 将仿真结果导出到基础工作区 按钮

点击以将仿真结果导出到基础工作区。

### 眼图模板

### **Eye mask type** — 眼图模板的形状 `Off`（默认）| `Rectangle` | `Diamond` | `Hexagon` | `Custom`

用于模板裕量测量的眼图模板形状。有关详细信息，请参阅 `eyeMask`。

### **W1 (UI)** — 矩形、菱形和六边形眼图模板中心处的宽度 `0.2`（默认）| 正实数标量

矩形或菱形眼图模板的宽度，或六边形眼图模板中心处的宽度，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `W1` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `0.2` |

### **W2 (UI)** — 六边形眼图模板顶部和底部的宽度 `0.1`（默认）| 正实数标量

六边形眼图模板顶部和底部的宽度，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Hexagon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `W2` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `0.1` |

### **H** — 矩形、菱形或六边形眼图模板的高度 `0.1`（默认）| 正实数标量

矩形、菱形或六边形眼图模板的高度，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `H` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `0.1` |

### **Position mask in eye** — 眼图中掩码形状原点的位置 `At clock`（默认）| `For best height margin` | `For best width margin`

定义眼图中掩码形状原点的位置。您可以将其定位在时钟处，或为获得最佳眼高或眼宽而定位。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond` 或 `Hexagon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PositionMaskInEye` |
| **类型：** 字符向量 |
| **值：** `At clock` | `For best height margin` | `For best width margin` |
| **默认值：** `At clock` |

### **Custom eye mask** — 从眼掩码对象定义自定义眼掩码 `[]`（默认）| 对象

从眼掩码对象定义自定义眼掩码。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CustomEyeMask` |
| **类型：** 字符向量 |
| **值：** 对象 |
| **默认值：** `[]` |

### **Margin SER** — 用于测量眼掩码裕度的符号错误率 `1e-5` | 范围 [0,1] 内的非负实数标量

模块测量眼掩码裕度时的符号错误率（SER），指定为范围 [0,1] 内的非负实数标量。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond`、`Hexagon` 或 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MarginSER` |
| **类型：** 字符向量 |
| **值：** 范围 [0,1] 内的非负实数标量 |
| **默认值：** `1e-5` |

### **Margin extrapolation** — 用于生成眼轮廓的外推方法 `none`（默认）| `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima`

用于生成眼轮廓以测量眼裕度的外推方法。模块通过相邻 bin 之间的插值将眼图外推到指定的 SER。有关详细信息，请参阅 Extrapolation。

**注意**

此功能需要 Signal Integrity Toolbox™、Optimization Toolbox™ 或 Curve Fitting Toolbox™ 的许可证。许可证要求按性能顺序列出，其中 Signal Integrity Toolbox 提供最快的计算速度。

#### 依赖关系

要启用此参数，请将 **Eye mask type** 设置为 `Rectangle`、`Diamond`、`Hexagon` 或 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MarginExtrapolation` |
| **类型：** 字符向量 |
| **值：** `none` | `dualdirac` | `gaussian` | `linear` | `spline` | `pchip` | `makima` |
| **默认值：** `none` |

### **Mask variable name** — 要导出掩码的掩码变量名称 `ans`（默认）| 字符串

要将掩码导出到基础工作区的掩码变量名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaskVariableName` |
| **类型：** 字符向量 |
| **值：** 字符串 |
| **默认值：** `ans` |

### **Export mask to file** — 将掩码导出到文件按钮

点击将掩码导出到文件以供以后使用。

### **Export mask to base workspace** — 将掩码导出到基础工作区按钮

点击将掩码导出到基础工作区。

### 绘图设置

### **Show plots at end of simulation** — 在仿真结束时自动显示绘图 on（默认）| off

选择此项可在仿真结束时自动将仿真结果显示为绘图。您可以定义要生成的绘图类型，包括眼图、时钟图和浴盆图。

### **Plot grouping** — 定义绘图的分组方式 `Subplot on same figure`（默认）| `One figure per plot`

定义绘图的分组方式。

### **Add Plot** — 添加新绘图以显示按钮

点击添加要显示的新绘图。

### **Remove Selected Plots** — 移除所选绘图按钮

点击移除所选绘图以聚焦于感兴趣的区域。

### **Show Plots** — 显示绘图按钮

点击以显示绘图。

## 所属库

Mixed-Signal Blockset / Utilities SerDes Toolbox / Utilities Signal Integrity Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025b：移动时钟 PDF 或眼图窗口

使用 **Clock phase offset** 参数移动时钟 PDF。当 **Clock mode** 为 clocked 以将眼图居中时，这很有用；在其他模式下，也可用于相对于眼图移动时钟 PDF。使用 **Window phase offset** 参数在 ideal 或 convolved 时钟模式下移动眼图窗口。

### R2025a：更新的外推方法

从不同的外推方法中选择，以在更改系统参数以满足您的需求时观察眼图指标的趋势。

## 描述

从眼图计算指标

Eye Measurement 模块从时域波形数据生成眼图，并从生成的图案中计算指标。
