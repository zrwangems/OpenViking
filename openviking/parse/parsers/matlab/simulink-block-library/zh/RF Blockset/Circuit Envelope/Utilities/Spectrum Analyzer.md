---
type: simulink-block
title: 'Spectrum Analyzer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'spectrumanalyzer'
documentation_source_path: 'ref/spectrumanalyzer.html'
language: zh-CN
chinese_source: worker-translation
---

# Spectrum Analyzer

## 端口

### 输入

### **u** — 要可视化的信号 标量 | 向量 | 矩阵 | 数组

连接要可视化的信号。最多可以有 96 个输入端口。输入信号必须具有以下特征：

- **信号域** — 频率或时间信号。
- **类型** — 离散信号。
- **数据类型** — Simulink® 支持的任何数据类型。请参阅 Simulink 支持的数据类型。
- **维度** — 一维（向量）、二维（矩阵）或多维（数组）信号。输入信号必须具有固定数量的通道。请参阅信号维度和确定信号维度。

Spectrum Analyzer 模块支持可变大小输入信号，即信号的帧大小可以在仿真过程中变化。当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。

Spectrum Analyzer 模块接受定点输入，但会将其转换为 `double` 进行显示。

在启用 **RBW** 端口之前，此端口没有名称。*（自 R2024a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **RBW** — RBW 值 正标量

通过此端口以 Hz 为单位指定分辨率带宽。RBW 定义了示波器能够分辨的最小正频率。您也可以使用 **Estimation** 选项卡上的 **RBW (Hz)** 参数指定 RBW 值。

#### 依赖关系

要启用此端口，请将 **Estimation** 选项卡上的 **RBW (Hz)** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

本节列出了 Simscape™ 和 RF Blockset 中 Spectrum Analyzer 模块的模块参数。有关完整的参数列表，请参阅 Spectrum Analyzer (DSP System Toolbox)。

### Scope 选项卡

#### 视图

### **Spectrum** — 要显示的频谱类型 `Power`（默认）| `Power Density` | `RMS`

将要显示的频谱类型设置为以下值之一：

- `Power` — Spectrum Analyzer 显示功率谱。
- `Power Density` — Spectrum Analyzer 显示功率谱密度。功率谱密度是归一化到 1 Hz 带宽的频谱幅度的平方。
- `RMS` — Spectrum Analyzer 显示均方根频谱。使用此选项可查看电压或电流信号的频率。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `SpectrumType` |
| **类型：** 字符向量或字符串标量 |

**数据类型：** `char` | `string`

#### 带宽

### **Sample Rate (Hz)** — 示波器使用的采样率（以 Hz 为单位） `Inherited`（默认）| 正标量

将示波器使用的采样率（以 Hz 为单位）指定为以下之一：

- `Inherited` — 使用此选项可指定与输入信号相同的采样率。
- 正标量 — 您指定的采样率必须至少是输入信号采样率的两倍。否则，由于混叠，在示波器中可视化信号时可能会看到意外行为。

当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。

要在状态栏上显示采样率，请单击状态栏中的 ⋮ 图标并选择 `Sample Rate`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleRate`、`SampleRateSource` |
| **类型：** `double` |

**可调：** 是

### **Offset (Hz)** — 应用于频率轴的偏移量 `0`（默认）| 标量 | 向量

指定应用于频率轴（*x* 轴）的偏移量，单位为 Hz，可为以下之一：

- 标量 — 对所有通道应用相同的频率偏移量。
- 向量 — 为每个通道应用特定的频率偏移量。向量长度必须等于输入通道数。

  总跨度必须落在奈奎斯特频率区间内。您可以根据 **Span (Hz)** 参数的设置方式以不同方式控制总跨度。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `FrequencyOffset` |
| **类型：** `double` |

#### 配置 > 频谱分析仪设置

### **Num Inputs** — 输入端口数 1（默认）| 1 到 96 之间的整数

模块的输入端口数，指定为 1 到 96 之间的整数。要更改输入端口数，请将新的输入信号线拖到模块上，模块会自动创建新端口。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumInputPorts` |
| **类型：** 字符向量或字符串标量 |
| **值：** 1 到 96 之间的标量 |

### **Open at Simulation Start** — 仿真开始时自动打开示波器 on（默认）| off

选择此参数可在运行仿真时自动打开频谱分析仪窗口。

#### 编程使用

|  |
| --- |
| **模块参数：** `OpenAtSimulationStart` |
| **类型：** `logical` |

### **Display Precision** — 示波器显示中数据的精度 `4`（默认）| 小于等于 15 的正整数

*自 R2024b 起*

将示波器显示中数值的精度指定为范围 [1, 15] 内的正整数。

**可调：** 是

### **Y-Label** — *y* 轴标签 字符向量 | 字符串标量

将频谱显示中的 *y* 轴标签指定为字符向量或字符串标量。要显示信号单位，请在标签中添加 `(%<SignalUnits>)`。仿真开始时，Simulink 会将 `(%SignalUnits)` 替换为与信号关联的单位。例如，对于单位为 m/s 的速度信号，请输入：

```
Velocity (%<SignalUnits>)
```

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `YLabel` |
| **类型：** 字符向量或字符串标量 |

### **Y-Limits** — *y* 轴范围 [`−80` `20`] | [`ymin ymax`]

将频谱分析仪显示中的 *y* 轴范围指定为形式为 [`ymin ymax`] 的二元素数值向量。*y* 轴范围的单位取决于 **Spectrum** 选项卡中的 **Spectrum Unit**。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `YLimits` |
| **类型：** `double` |

### **Title** — 显示标题 字符向量 | 字符串

指定显示标题。输入 `%<SignalLabel>` 以使用 Simulink 模型中的信号标签作为坐标轴标题。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `Title` |
| **类型：** 字符向量或字符串 |

### **Show Grid** — 显示内部网格线 `on`（默认）| `off`

选中此复选框可在频谱分析仪显示中显示网格。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowGrid` |
| **类型：** `logical` |

### **Plot Type** — 绘图类型 `Line`（默认）| `Stem`

指定在频谱显示中显示 `Line` 还是 `Stem` 绘图。

您可以单独控制每条线的绘图类型。选择该线并相应地设置 **Plot Type**。*（自 R2025a 起）*

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `PlotType` |
| **类型：** 字符向量或字符串标量 |

### **Font Size** — 标签的字体大小 `8.5`（默认）| 正标量

将示波器的刻度、标签、标题和测量的字体大小指定为正标量。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `-` |
| **类型：** double |

### **Background** — 窗口背景 黑色（默认）| 颜色选择器

指定示波器图窗中的背景颜色。

**可调：** 是

### **Axes** — 坐标区背景颜色 黑色（默认）| 颜色选择器

指定坐标区的背景颜色。

**可调：** 是

### **Labels** — 标签颜色 灰色（默认）| 颜色选择器

指定标签、网格以及图例中通道名称的颜色。

**可调：** 是

### **Line** — 用于线条属性设置的通道 通道名称

指定要修改其可见性、线条颜色、样式、宽度和标记属性的通道。

**可调：** 是

### **Visible** — 通道可见性 `on`（默认）| `off`

选中此复选框可显示您所选的通道。如果清除此复选框，所选通道将不再可见。您也可以点击图例中的信号名称来控制其可见性。有关更多详细信息，请参阅图例。

**可调：** 是

### **Style** — 线型 `-`（默认）| `:` | `-.` | `--` | `None`

指定所选通道的线型。

**可调：** 是

### **Width** — 线宽 `1.5`（默认）| `0.5` | `1` | `2` | ...

指定所选通道的线宽。

**可调：** 是

### **Marker** — 数据点标记 `None`（默认）| `+` | `x` | ...

为所选通道指定数据点标记。此参数类似于绘图中的 Marker 属性。您可以从下拉列表中选择任意标记符号。

**可调：** 是

### **Color** — 线条颜色 黄色（默认）| 颜色选择器

指定所选通道的线条颜色。

**可调：** 是

#### 配置

### **Legend** — 显示或隐藏信号图例 按钮

点击 **Legend** 按钮以启用频谱分析仪显示。图例显示模型中的信号名称。对于具有多个通道的信号，示波器会在信号名称后附加通道索引。连续信号在其名称前有直线，离散信号有阶梯状线条。

您可以使用图例控制哪些信号可见。要隐藏示波器图例中的信号，请点击信号名称。要显示该信号，请再次点击信号名称。或者，您可以使用 **Spectrum Analyzer Settings**（齿轮按钮）中的 **Visible** 参数来控制哪个信号可见。

要仅显示一个信号并隐藏所有其他信号，请右键点击您希望示波器显示的信号名称。要显示所有信号，请按 **Esc**。

**注意**

图例仅显示前 20 个信号。您无法从图例中查看或控制任何其他信号。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowLegend` |
| **类型：** `logical` |

**可调：** 是

#### Share

### **Copy to Clipboard** — 将显示内容发送到剪贴板 按钮

点击此按钮可将示波器显示内容复制到剪贴板。您可以通过在 **Copy to Clipboard** 下拉列表中选择 **Preserve Colors** 来保留显示内容中的颜色。

### **Preserve Colors** — 复制到剪贴板时保留颜色 `off`（默认）| `on`

当您使用 **Scope** 选项卡 > **Share** 部分中的 **Copy to Clipboard** 和 **Print** 选项将显示内容复制到剪贴板时，选择此参数可使示波器保留颜色。

要访问 **Preserve Colors**，请点击 **Copy to Clipboard** 的下拉箭头。

**可调：** 是

### **Print** — 打印显示内容 按钮

点击此按钮可将示波器显示内容保存为图像或 PDF，或打印显示内容。

### Estimation Tab

#### Frequency Resolution

### **RBW (Hz)** — 分辨率带宽，单位为 Hz `Auto`（默认）| `Input port` | 正标量

指定以 Hz 为单位的分辨率带宽。此参数定义示波器能够分辨的最小正频率。默认情况下，此参数设置为 `Auto`。在这种情况下，频谱分析仪会确定适当的值，以确保在指定的频率跨度内有 1024 个 RBW 区间。

如果将此参数设置为 `Input port`，则可以通过模块上的输入端口指定 RBW 值。

如果将此参数设置为数值，则该值必须允许在指定的频率跨度内至少有 2 个 RBW 区间。换句话说，总频率跨度与 RBW 的比值必须大于 2：

spanRBW>2

要在状态栏上显示此属性，请单击状态栏中的 ⋮ 图标，然后选择 `RBW`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RBWSource`, `RBW` |
| **类型：** 字符向量、字符串标量、`double` |

**可调：** 是

#### 平均

### **Averaging Method** — 平滑方法 `Exponential`（默认）| `VBW` | `Running`

将平滑方法指定为以下之一：

- `Exponential` — 该模块计算按指数衰减遗忘因子加权的样本平均值。使用 **Forgetting Factor** 参数指定加权遗忘因子。
- `VBW` — 该模块使用低通滤波器平滑迹线并降低噪声。使用 **VBW (Hz)** 参数指定视频带宽（VBW）值。
- `Running` — 最后 *Q* 个样本的滑动平均值。使用 **Spectral Averages** 参数指定 *Q*。*（自 R2025a 起）*

有关平均方法的更多信息，请参阅 Averaging Method。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `AveragingMethod` |
| **类型：** 字符向量或字符串标量 |

### **VBW (Hz)** — 视频带宽 `Auto`（默认）| `Input port` | 正标量

将视频带宽指定为以下之一：

- `Auto` –– 频谱分析仪调整 VBW，使等效遗忘因子为 0.9。
- `Input port` –– 示波器上会出现一个输入端口，您可以通过此端口指定 VBW 值。
- 正标量 –– 您指定一个正标量。频谱分析仪使用此值调整 VBW。您指定的值必须小于或等于 **Sample Rate (Hz)**/2。

有关视频带宽方法的更多详细信息，请参阅 Averaging Method。

频谱分析仪在显示屏底部的状态栏中显示 VBW 值。要显示 VBW 值，请单击状态栏最右侧角落的 kebab 图标，然后选择 `VBW`。

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `VBW`。

#### 编程用法

|  |
| --- |
| **模块参数：** `VBWSource`, `VBW` |
| **类型：** `double` |

**可调：** 是

### **Forgetting Factor** — 加权平均法的遗忘因子 `0.9`（默认）| [0,1] 范围内的标量

将指数加权平均法的遗忘因子指定为 [0,1] 范围内的标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `Exponential`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ForgettingFactor` |
| **类型：** `double` |

### **Spectral Averages** — 频谱平均数 `1`（默认）| 正整数

*自 R2025a 起*

将频谱平均数 *Q* 指定为正整数。

频谱分析仪通过计算最后 *Q* 个功率谱估计的滑动平均值来计算当前功率谱估计。

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `Running`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SpectralAverages` |
| **类型：** `double` |

**数据类型：** `double`

#### 窗口选项

### **Window** — 加窗方法 `Hann`（默认）| `Rectangular`

指定应用于频谱的加窗方法。加窗用于控制频谱估计中旁瓣的影响。您指定的窗会影响达到分辨率带宽所需的窗长度以及每次更新所需的样本数。有关加窗的详细信息，请参阅 Windows (Signal Processing Toolbox)。

如果安装了 DSP System Toolbox，则可以访问其他加窗算法。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `Window` |
| **类型：** 字符向量或字符串标量 |

### **Overlap (%)** — 重叠百分比 `0`（默认）| 范围 [0 100) 内的标量

指定前一个缓冲数据段与当前缓冲数据段之间的重叠百分比，指定为范围 [0 100) 内的标量。重叠会创建一个窗段，示波器使用该窗段计算频谱估计。该值必须大于或等于零且小于 100。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `OverlapPercent` |
| **类型：** `double` |

### Measurements Tab

#### Channel

### **Channel** — 要获取测量的通道 `1`（默认）| 正整数

需要获取测量的通道，指定为范围 [1 *N*] 内的正整数，其中 *N* 是输入通道数。

**可调：** 是

#### 依赖关系

要启用此参数，请将一些数据传递通过示波器。

#### 程序化使用

请参阅 `MeasurementChannel`。

#### Cursors

### **Data Cursors** — 启用光标测量按钮

点击 **Data Cursors** 按钮以启用数据光标测量。每个光标沿信号跟踪一条垂直线。示波器在两个光标之间的框中显示两个光标处信号 *x* 值和 *y* 值之间的差。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Snap to data** — 将光标对齐到数据 `off`（默认）| `on`

选择此参数可将光标定位在信号数据点上。

**可调：** 是

#### 程序化使用

请参阅 `SnapToData`。

### **Lock cursor spacing** — 锁定光标间距 `off`（默认）| `on`

选择此参数可锁定两个光标之间的频率差。

**可调：** 是

#### 程序化使用

请参阅 `LockSpacing`。

#### Peaks

### **Peak Finder** — 启用峰值查找器测量按钮

点击 **Peak Finder** 按钮以启用峰值查找器测量。每个最大值处会在图上显示一个箭头，并且示波器窗口底部会出现一个 Peaks 面板。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Num Peaks** — 要显示的最大峰值数 `3`（默认）| 小于 100 的正整数

指定要显示的最大峰值数，指定为小于 100 的正整数。

**可调：** 是

#### 程序化使用

请参阅 `NumPeaks`。

### **Min Height** — 示波器检测峰值的电平阈值 `-Inf`（默认）| 实数标量值

指定示波器检测峰值的电平阈值，指定为实数标量。

**可调：** 是

#### 程序化使用

请参阅 `MinHeight`。

### **Min Distance** — 相邻峰值之间的最小样本数 `1`（默认）| 正整数

指定相邻峰值之间的最小样本数，指定为正整数。

**可调：** 是

#### 程序化使用

请参阅 `MinDistance`。

### **Threshold** — 峰值高度与其相邻样本之间的最小差值 `0`（默认）| 非负标量

指定峰值高度与其相邻样本之间的最小差值，指定为非负标量。

**可调：** 是

#### 程序化使用

请参阅 `Threshold`。

### **Label Peaks** — 标记峰值按钮

点击 **Label Peaks** 按钮以标记峰值。示波器会在图中的箭头上方显示标签（**P1**、**P2**、……）。

**可调：** 是

#### 程序化使用

请参阅 `LabelPeaks`。

#### Distortion

### **Distortion** — 启用失真测量按钮

点击 **Distortion** 按钮以启用失真测量。点击此按钮后，示波器窗口底部会出现一个 Distortion 面板。

**可调：** 是

#### 程序化使用

参见 `Enabled`。

### **Distortion Type** — 要显示的测量类型 `Harmonic`（默认）| `Intermodulation`

指定要显示的测量数据类型为 `Harmonic` 或 `Intermodulation`。有关更多详细信息，请参阅 Distortion Measurements。

**可调：** 是

#### 程序化使用

参见 `Type`。

### **Num Harmonics** — 要测量的谐波数量 `6`（默认）| 正整数

指定要测量的谐波数量为小于或等于 99 的正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distortion Type** 设置为 `Harmonic`。

#### 程序化使用

参见 `NumHarmonics`。

### **Label Harmonics** — 标记谐波 `off`（默认）| `on`

当您选择此参数时，频谱分析仪会在频谱显示中为谐波添加数字标签。

**可调：** 是

#### 程序化使用

参见 `LabelValues`。

### **Label Frequencies** — 标记频率 `off`（默认）| `on`

当您选择此参数时，频谱分析仪会在频谱分析仪显示中为一阶互调产物和三阶频率添加数字标签。

**可调：** 是

#### 程序化使用

参见 `LabelValues`。

### Spectrum 选项卡

#### 轨迹选项

### **Two-Sided Spectrum** — 启用双边频谱视图 `on`（默认）| `off`

选中此复选框以启用双边频谱视图。在此视图中，频谱分析仪同时显示负频率和正频率。当输入信号为复值时，您必须选择此参数。如果清除此复选框，频谱分析仪将显示仅含正频率的单边频谱。在这种情况下，输入信号数据必须为实值。

当您清除此复选框时，频谱分析仪使用功率折叠。*y* 轴值为选择此参数时的两倍振幅，但在 `0` 和奈奎斯特频率处除外。单边功率谱密度（PSD）包含从直流到半奈奎斯特频率区间内信号的总功率。有关更多信息，请参阅 `pwelch`（Signal Processing Toolbox）。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotAsTwoSidedSpectrum` |
| **类型：** `logical` |

#### 刻度

### **Frequency Scale** — 频率轴的刻度 `Linear`（默认）| `Log`

指定频率显示刻度为 `Linear` 或 `Log`。当频率范围包含负频率值时，您无法选择对数选项。

**可调：** 是

#### 依赖关系

要将 **Frequency Scale** 设置为 `Log`，请清除 **Spectrum** 选项卡中 **Trace Options** 部分的 **Two-Sided Spectrum** 复选框。如果您选中 **Two-Sided Spectrum** 复选框，则 **Frequency Scale** 参数将设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyScale` |
| **类型：** 字符向量或字符串标量 |

### **Reference load (Ω)** — 参考负载，单位为 Ω `1`（默认）| 正实数标量

指定 Spectrum Analyzer 用作计算功率值的参考负载，单位为欧姆。

**可调：** 是

#### 依赖关系

要启用此参数，请将：

- **Spectrum** 类型设置为 `Power` 或 `Power Density`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ReferenceLoad` |
| **类型：** `double` |

### **Spectrum Unit** — 频谱的单位 `dBm`（默认）| `dBm/Hz` | `dBV` | `dBuV` *（自 R2023b 起）* | `Vrms`

指定 Spectrum Analyzer 显示功率值的单位，为以下之一：

- `dBm`
- `dBV`
- `dBuV` *（自 R2023b 起）*
- `Vrms`
- `dBm/Hz`

**可调：** 是

#### 依赖关系

可用的单位取决于您在 **Scope** 选项卡中为 **Spectrum** 参数选择的值。

| Scope 选项卡 > Spectrum 选项 | 可用单位 |
| --- | --- |
| `Power` | `dBm` |
| `Power Density` | `dBm/Hz` |
| `RMS` | `dBV`、`dBuV` *（自 R2023b 起）*、`Vrms` |

#### 编程用法

|  |
| --- |
| **模块参数：** `SpectrumUnits` |
| **类型：** 字符向量或字符串标量 |

### 仅属性检查器

### **Channel Names** — 输入通道名称 `[]`（默认）| 字符向量 | 字符串 | 字符串或字符向量数组

输入通道名称，指定为字符向量、字符串或数组。这些名称显示在图例、**Settings** 和 **Measurements** 面板中。如果未指定名称，示波器将通道标记为 `Channel 1`、`Channel 2` 等。

**示例：** ["A","B"]

#### 依赖关系

要查看通道名称，请在 **Scope** 选项卡中选择 **Legend**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChannelNames` |
| **类型：** 字符向量元胞数组或字符串数组 |

### **Maximize Axes** — 最大化绘图尺寸 `Auto`（默认）| `Off` | `On`

- `Auto` — 如果未指定 **Title** 和 **Y-Label**，示波器将最大化所有绘图。
- `On` — 示波器最大化所有绘图并隐藏 **Title** 和 **Y-label** 中的所有值。
- `Off` — 示波器不最大化绘图。

将鼠标悬停在 Spectrum Analyzer 上可看到最大化坐标轴按钮 。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `MaximizeAxes` |
| **类型：** 字符向量或字符串标量 |

### **Axes Scaling** — Y 轴缩放模式 `OnceAtStop`（默认）| `Manual` | `Auto` | `Updates`

- `OnceAtStop` — 仿真完成后缩放 *y* 轴。
- `Manual` — 使用 **Scale Y-axis Limits** 工具栏按钮手动缩放 *y* 轴范围。
- `Auto` — 在仿真期间和仿真后缩放 *y* 轴范围。
- `Updates` — 在 Number of Updates 文本框中指定的时间步数（默认为 `100`）之后缩放 *y* 轴。每次运行仅缩放一次。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `AxesScaling` |
| **类型：** 字符向量或字符串标量 |

### **Number of Updates** — 缩放前的更新次数 `100`（默认）| 整数

设置此属性以延迟 *y* 轴的自动缩放。

**可调：** 是

#### 依赖关系

要启用此属性，请将 Axes Scaling 设置为 `Updates`。

#### 编程用法

|  |
| --- |
| **模块参数：** `AxesScalingNumUpdates` |
| **类型：** 字符向量或字符串标量 |
| **值：** 标量 |

## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可视化。但是，生成的代码中不包含此模块。

## 版本历史

**在 R2017b 中引入**

### R2025a：单独控制每条线的绘图类型

您现在可以单独控制每条线的绘图类型。要控制某条线的绘图类型，请选择该线并相应地设置 **Plot Type** 参数。

### R2025a：支持运行平均方法

Spectrum Analyzer 模块现在支持运行平均方法来计算功率谱估计。要启用此模式，请将 **Estimation** 选项卡中的 **Averaging Method** 参数设置为 `Running`，并将 **Spectral Averages** 参数设置为正整数。

有关详细信息，请参阅算法部分。

### R2024b：显示任意数量输入样本的频谱数据并相应调整 RBW

以前，Spectrum Analyzer 模块需要最少数量的样本才能更新给定 RBW 值的显示。从 R2024b 开始，此限制已移除。示波器现在可以针对任意数量的输入样本更新其显示，并相应地调整 RBW 值。

### R2024b：自动调整 RBW 以保持 1024 个采样点

Spectrum Analyzer 模块现在可以自动调整分辨率带宽（RBW），以便无论您选择何种窗函数，都能将每次频谱更新的采样点数保持在 1024（*Nsamples* = 1024）。

要在 Spectrum Analyzer 模块中启用此模式，请设置：

- **RBW (Hz)** 为 `Auto`。

### R2024b：示波器 UI 中更高的显示精度

您现在可以使用示波器设置中 **Display and Labels** 下的 **Display Precision** 属性将显示精度提高到 15 位数字。此精度会影响示波器在其状态栏上显示的所有测量值和数据。

### R2024b：**Preserve Colors** 现已在示波器工具条中提供

**Preserve colors for copy to clipboard** 属性已重命名为 **Preserve Colors**，现可在 **Copy Display** 下的示波器工具条中使用。

### R2024a：**Analyzer** 选项卡已重命名为 **Scope** 选项卡

频谱分析器中的 **Analyzer** 选项卡已重命名为 **Scope** 选项卡。

### R2023b：Spectrum Analyzer 支持 `dBuV` 单位

当您将 **Spectrum** 设置为 `RMS` 时，可以将 **Spectrum Unit** 设置为 `dBuV`。

### R2023a：Simulink 中 Spectrum Analyzer 具有改进的响应性和工具条界面

在 R2023a 中，Spectrum Analyzer 模块的响应性更好，其工具条界面经过改进，可让您轻松访问频谱分析、估计和测量功能。您可以使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置和显示 Spectrum Analyzer 设置。

## 描述

显示时域信号的频谱

**注意**

RF Blockset™ 中的 Spectrum Analyzer 模块提供的功能是 DSP System Toolbox™ 中同名模块所提供功能的子集。本页介绍 RF Blockset 许可证下可用的模块配置和功能。

如果您同时拥有 DSP System Toolbox 许可证，则 RF Blockset > Utilities 库中的 Spectrum Analyzer 模块与 DSP System Toolbox > Sinks 库中的模块完全相同。有关更多信息，请参阅 Spectrum Analyzer (DSP System Toolbox)。

Spectrum Analyzer 模块显示具有离散采样时间的输入信号的频谱。

在 RF Blockset 模型中，要使用 Spectrum Analyzer 模块代替常规示波器：

1. 将 Spectrum Analyzer 模块添加到您的框图中。
2. 如果您的模型使用变步长求解器，还需添加一个 Rate Transition 模块并将其连接到 Spectrum Analyzer 模块的输入端口。将 **Output port sample time** 参数设置为您希望 Spectrum Analyzer 使用的采样时间。

   如果您的模型使用局部求解器，则它输出具有离散采样时间的物理信号，您无需添加 Rate Transition 模块。但是，如果您需要从求解器固定步长进行降采样，可以使用 Rate Transition 模块。有关使用局部求解器的更多信息，请参阅 Making Optimal Solver Choices for Physical Simulation。
3. 使用 PS-Simulink Converter 模块将感兴趣的物理输出信号连接到 Spectrum Analyzer 模块的输入端口（或者连接到 Rate Transition 模块的输入端口，如果您使用了该模块）。有关更多信息，请参阅 Connecting Simscape Diagrams to Simulink Sources and Scopes。您还可以在 PS-Simulink Converter 和 Spectrum Analyzer 模块之间使用额外的信号处理模块来提高信号质量。
4. 运行仿真。仿真完成后，Spectrum Analyzer（此处称为示波器）将打开并显示信号的频谱。

示波器窗口中信号的频谱

### 编程控制

您可以使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置和显示 Spectrum Analyzer 设置。
