---
type: simulink-block
title: 'Spectrum Analyzer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Circuit Envelope Fundamentals'
documentation_page: 'spectrumanalyzer'
documentation_source_path: 'ref/spectrumanalyzer.html'
language: zh-CN
chinese_source: worker-translation
---

# Spectrum Analyzer

## 端口

### 输入

### **u** — 要可视化的信号 标量 | 向量 | 矩阵 | 数组

连接您要可视化的信号。您最多可以有 96 个输入端口。输入信号必须具有以下特征：

- **信号域** — 频域或时域信号。
- **类型** — 离散信号。
- **数据类型** — Simulink® 支持的任何数据类型。请参阅 Data Types Supported by Simulink。
- **维度** — 一维（向量）、二维（矩阵）或多维（数组）信号。输入信号必须具有固定数量的通道。请参阅 Signal Dimensions 和 Determine Signal Dimensions。

Spectrum Analyzer 模块支持可变大小输入信号，即信号帧大小可在仿真期间变化。当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。

Spectrum Analyzer 模块接受定点输入，但会将其转换为 `double` 以进行显示。

在启用 **RBW** 端口之前，此端口是未命名的。*（自 R2024a 起）*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **RBW** — RBW 值 正标量

通过此端口指定以 Hz 为单位的分辨率带宽。RBW 定义了示波器可分辨的最小正频率。您还可以在 **Estimation** 选项卡上使用 **RBW (Hz)** 参数指定 RBW 值。

#### 依赖关系

要启用此端口，请在 **Estimation** 选项卡上将 **RBW (Hz)** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

本节列出 Simscape™ 和 RF Blockset 中 Spectrum Analyzer 模块的模块参数。有关参数的完整列表，请参阅 Spectrum Analyzer (DSP System Toolbox)。

### Scope 选项卡

#### 视图

### **Spectrum** — 要显示的频谱类型 `Power`（默认）| `Power Density` | `RMS`

将频谱类型设置为以下值之一：

- `Power` — Spectrum Analyzer 显示功率谱。
- `Power Density` — Spectrum Analyzer 显示功率谱密度。功率谱密度是归一化到 1 Hz 带宽的频谱幅值平方。
- `RMS` — Spectrum Analyzer 显示均方根频谱。使用此选项查看电压或电流信号的频率。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `SpectrumType` |
| **类型:** 字符向量或字符串标量 |

**数据类型：** `char` | `string`

#### 带宽

### **Sample Rate (Hz)** — 示波器使用的采样率，以 Hz 为单位 `Inherited`（默认）| 正标量

将示波器使用的采样率指定为以下值之一，以 Hz 为单位：

- `Inherited` — 使用此选项指定与输入信号相同的采样率。
- 正标量 — 您指定的采样率必须至少为输入信号采样率的两倍。否则，由于混叠，在示波器中可视化信号时可能会看到意外行为。

当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。

要在状态栏上显示采样率，请单击状态栏中的 ⋮ 图标，然后选择 `Sample Rate`。

#### 编程用法

|  |
| --- |
| **模块参数:** `SampleRate`, `SampleRateSource` |
| **类型:** `double` |

**可调：** Yes

### **Offset (Hz)** — 应用于频率轴的偏移 `0`（默认）| 标量 | 向量

将应用于频率轴（*x* 轴）的偏移指定为以下值之一，以 Hz 为单位：

- 标量 — 对所有通道应用相同的频率偏移。
- 向量 — 为每个通道应用特定的频率偏移。向量长度必须等于输入通道数。

  总跨度必须落在 Nyquist Frequency Interval 内。您可以根据 **Span (Hz)** 参数的设置方式，以不同方式控制总跨度。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `FrequencyOffset` |
| **类型:** `double` |

#### 配置 > Spectrum Analyzer 设置

### **Num Inputs** — 输入端口数 1（默认）| 1 到 96 之间的整数

模块的输入端口数，指定为 1 到 96 之间的整数。要更改输入端口数，请将新的输入信号线拖到模块，模块会自动创建新端口。

#### 编程用法

|  |
| --- |
| **模块参数:** `NumInputPorts` |
| **类型:** 字符向量或字符串标量 |
| **值:** 1 到 96 之间的标量 |

### **Open at Simulation Start** — 仿真开始时自动打开示波器 on（默认）| off

选择此参数以在运行仿真时自动打开 Spectrum Analyzer 窗口。

#### 编程用法

|  |
| --- |
| **模块参数:** `OpenAtSimulationStart` |
| **类型:** logical |

### **Display Precision** — 示波器显示中数据的精度 `4`（默认）| ≤ 15 的正整数

*自 R2024b 起*

将示波器显示中数值的精度指定为范围 [1, 15] 内的正整数。

**可调：** Yes

### **Y-Label** — *y* 轴标签 字符向量 | 字符串标量

将 Spectrum 显示中的 *y* 轴标签指定为字符向量或字符串标量。要显示信号单位，请将 `(%<SignalUnits>)` 添加到标签中。仿真开始时，Simulink 会将 `(%SignalUnits)` 替换为与信号关联的单位。例如，对于单位为 m/s 的速度信号，请输入：

```
Velocity (%<SignalUnits>)
```

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `YLabel` |
| **类型:** 字符向量或字符串标量 |

### **Y-Limits** — *y* 轴范围 [`−80` `20`] | [`ymin ymax`]

将 Spectrum Analyzer 显示中的 *y* 轴范围指定为形式为 [`ymin ymax`] 的二元素数值向量。*y* 轴范围的单位取决于 **Spectrum** 选项卡中的 **Spectrum Unit**。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `YLimits` |
| **类型:** `double` |

### **Title** — 显示标题 字符向量 | 字符串

指定显示标题。输入 `%<SignalLabel>` 以将 Simulink 模型中的信号标签用作坐标轴标题。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `Title` |
| **类型:** 字符向量或字符串 |

### **Show Grid** — 显示内部网格线 `on`（默认）| `off`

选中此复选框以在 Spectrum Analyzer 显示中显示网格。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `ShowGrid` |
| **类型:** `logical` |

### **Plot Type** — 绘图类型 `Line`（默认）| `Stem`

指定在 Spectrum 显示中显示 `Line` 还是 `Stem` 图。

您可以单独控制每条线的绘图类型。选择该线并相应地设置 **Plot Type**。*（自 R2025a 起）*

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `PlotType` |
| **类型:** 字符向量或字符串标量 |

### **Font Size** — 标签字体大小 `8.5`（默认）| 正标量

将示波器的刻度、标签、标题和测量的字体大小指定为正标量。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `-` |
| **类型:** double |

### **Background** — 窗口背景 black（默认）| 颜色选择器

指定示波器图形中的背景颜色。

**可调：** Yes

### **Axes** — 坐标轴背景颜色 black（默认）| 颜色选择器

指定坐标轴的背景颜色。

**可调：** Yes

### **Labels** — 标签颜色 gray（默认）| 颜色选择器

指定标签、网格和图例中通道名称的颜色。

**可调：** Yes

### **Line** — 用于线属性设置的通道 通道名称

指定要修改其可见性、线颜色、样式、宽度和标记属性的通道。

**可调：** Yes

### **Visible** — 通道可见性 `on`（默认）| `off`

选中此复选框以显示您已选择的通道。如果清除此复选框，所选通道将不再可见。您还可以单击图例中的信号名称来控制其可见性。有关更多详细信息，请参阅 Legend。

**可调：** Yes

### **Style** — 线型 `-`（默认）| `:` | `-`. | `--` | `None`

指定所选通道的线型。

**可调：** Yes

### **Width** — 线宽 `1.5`（默认）| `0.5` | `1` | `2` | ...

指定所选通道的线宽。

**可调：** Yes

### **Marker** — 数据点标记 `None`（默认）| `+` | `x` | ...

为所选通道指定数据点标记。此参数类似于绘图的 Marker 属性。您可以从下拉列表中选择任何标记符号。

**可调：** Yes

### **Color** — 线颜色 yellow（默认）| 颜色选择器

指定所选通道的线颜色。

**可调：** Yes

#### 配置

### **Legend** — 显示或隐藏信号图例 按钮

单击 **Legend** 按钮以启用 Spectrum Analyzer 显示。图例显示模型中的信号名称。对于具有多个通道的信号，示波器会在信号名称后附加通道索引。连续信号名称前有直线，离散信号有阶梯状线。

您可以使用图例控制哪些信号可见。要在示波器图例中隐藏信号，请单击信号名称。要显示信号，请再次单击信号名称。或者，您可以使用 **Spectrum Analyzer 设置**（齿轮按钮）中的 **Visible** 参数控制哪个信号可见。

要仅显示一个信号并隐藏所有其他信号，请右键单击您希望示波器显示的信号名称。要显示所有信号，请按 **Esc**。

**注意**

图例仅显示前 20 个信号。您无法从图例查看或控制任何其他信号。

#### 编程用法

|  |
| --- |
| **模块参数:** `ShowLegend` |
| **类型:** `logical` |

**可调：** Yes

#### 共享

### **Copy to Clipboard** — 将显示内容发送到剪贴板 按钮

单击此按钮以将示波器显示复制到剪贴板。您可以通过在 **Copy to Clipboard** 下拉列表中选择 **Preserve Colors** 来保留显示中的颜色。

### **Preserve Colors** — 复制到剪贴板时保留颜色 `off`（默认）| `on`

当您使用 **Scope** 选项卡 > **Share** 部分中的 **Copy to Clipboard** 和 **Print** 选项将显示内容复制到剪贴板时，选择此参数以使示波器保留颜色。

要访问 **Preserve Colors**，请单击 **Copy to Clipboard** 的下拉箭头。

**可调：** Yes

### **Print** — 打印显示内容 按钮

单击此按钮以将示波器显示保存为图像或 PDF，或打印显示内容。

### Estimation 选项卡

#### 频率分辨率

### **RBW (Hz)** — 以 Hz 为单位的分辨率带宽 `Auto`（默认）| `Input port` | 正标量

指定以 Hz 为单位的分辨率带宽。此参数定义示波器可分辨的最小正频率。默认情况下，此参数设置为 `Auto`。在这种情况下，频谱分析仪会确定适当的值，以确保在指定频率跨度上有 1024 个 RBW 区间。

如果将此参数设置为 `Input port`，则可以通过模块上的输入端口指定 RBW 值。

如果将此参数设置为数值，则该值必须允许在指定频率跨度上至少有 2 个 RBW 区间。换言之，总频率跨度与 RBW 之比必须大于 2：

spanRBW>2

要在状态栏上显示此属性，请单击状态栏中的 ⋮ 图标，然后选择 `RBW`。

#### 编程用法

|  |
| --- |
| **模块参数:** `RBWSource`, `RBW` |
| **类型:** 字符向量、字符串标量、`double` |

**可调：** Yes

#### 平均

### **Averaging Method** — 平滑方法 `Exponential`（默认）| `VBW` | `Running`

将平滑方法指定为以下之一：

- `Exponential` — 模块计算按指数衰减遗忘因子加权的样本平均值。使用 **Forgetting Factor** 参数指定加权遗忘因子。
- `VBW` — 模块使用低通滤波器平滑轨迹并降低噪声。使用 **VBW (Hz)** 参数指定视频带宽 (VBW) 值。
- `Running` — 最后 *Q* 个样本的滑动平均。使用 **Spectral Averages** 参数指定 *Q*。*（自 R2025a 起）*

有关平均方法的更多信息，请参阅 Averaging Method。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `AveragingMethod` |
| **类型:** 字符向量或字符串标量 |

### **VBW (Hz)** — 视频带宽 `Auto`（默认）| `Input port` | 正标量

将视频带宽指定为以下之一：

- `Auto` –– Spectrum Analyzer 调整 VBW，使等效遗忘因子为 0.9。
- `Input port` –– 示波器上会出现一个输入端口，您可以通过此端口指定 VBW 值。
- 正标量 –– 您指定一个正标量。Spectrum Analyzer 使用此值调整 VBW。您指定的值必须小于或等于 **Sample Rate (Hz)**/2。

有关视频带宽方法的更多详细信息，请参阅 Averaging Method。

Spectrum Analyzer 在显示底部的状态栏中显示 VBW 值。要显示 VBW 值，请单击状态栏中最右角的状态栏图标中的 kebab 图标，然后选择 `VBW`。

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `VBW`。

#### 编程用法

|  |
| --- |
| **模块参数:** `VBWSource`, `VBW` |
| **类型:** `double` |

**可调：** Yes

### **Forgetting Factor** — 加权平均方法的遗忘因子 `0.9`（默认）| [0,1] 范围内的标量

将指数加权平均方法的遗忘因子指定为 [0,1] 范围内的标量。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `Exponential`。

#### 编程用法

|  |
| --- |
| **模块参数:** `ForgettingFactor` |
| **类型:** `double` |

### **Spectral Averages** — 频谱平均次数 `1`（默认）| 正整数

*自 R2025a 起*

将频谱平均次数 *Q* 指定为正整数。

Spectrum Analyzer 通过计算最后 *Q* 个功率谱估计的滑动平均来计算当前功率谱估计。

#### 依赖关系

要启用此参数，请将 **Averaging Method** 设置为 `Running`。

#### 编程用法

|  |
| --- |
| **模块参数:** `SpectralAverages` |
| **类型:** `double` |

**数据类型：** `double`

#### 窗选项

### **Window** — 加窗方法 `Hann`（默认）| `Rectangular`

指定要应用于频谱的加窗方法。加窗用于控制频谱估计中旁瓣的影响。您指定的窗会影响达到分辨率带宽所需的窗长度以及每次更新所需的样本数。有关加窗的更多信息，请参阅 Windows (Signal Processing Toolbox)。

如果安装 DSP System Toolbox，则可以访问其他加窗算法。

**可调：** Yes

#### 编程用法

|  |
| --- |
| **模块参数:** `Window` |
| **类型:** 字符向量或字符串标量 |

### **Overlap (%)** — 重叠百分比 `0` (默认) | 范围 [0 100) 内的标量

将前一个和当前缓冲数据段之间的重叠百分比指定为范围 [0 100) 内的标量。重叠会创建一个窗口段，示波器使用该窗口段计算频谱估计。该值必须大于或等于零且小于 100。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `OverlapPercent` |
| **类型：** `double` |

### 测量选项卡

#### 通道

### **Channel** — 用于获取测量的通道 `1` (默认) | 正整数

需要获取测量的通道，指定为范围 [1 *N*] 内的正整数，其中 *N* 是输入通道数。

**可调：** 是

#### 依赖关系

要启用此参数，请通过示波器传递一些数据。

#### 编程用法

参见 `MeasurementChannel`。

#### 光标

### **Data Cursors** — 启用光标测量按钮

点击 **Data Cursors** 按钮以启用数据光标测量。每个光标沿信号跟踪一条垂直线。示波器在光标之间的框中显示两个光标处信号的 *x* 值和 *y* 值之差。

**可调：** 是

#### 编程用法

参见 `Enabled`。

### **Snap to data** — 将光标对齐到数据 `off` (默认) | `on`

选择此参数以将光标定位在信号数据点上。

**可调：** 是

#### 编程用法

参见 `SnapToData`。

### **Lock cursor spacing** — 锁定光标间距 `off` (默认) | `on`

选择此参数以锁定两个光标之间的频率差。

**可调：** 是

#### 编程用法

参见 `LockSpacing`。

#### 峰值

### **Peak Finder** — 启用峰值查找器测量按钮

点击 **Peak Finder** 按钮以启用峰值查找器测量。每个最大值处的绘图上会出现一个箭头，并且示波器窗口底部会出现一个 Peaks 面板。

**可调：** 是

#### 编程用法

参见 `Enabled`。

### **Num Peaks** — 要显示的最大峰值数 `3` (默认) | 小于 100 的正整数

将要显示的最大峰值数指定为小于 100 的正整数。

**可调：** 是

#### 编程用法

参见 `NumPeaks`。

### **Min Height** — 示波器检测峰值的电平阈值 `-Inf` (默认) | 实标量值

指定示波器检测峰值的电平阈值，指定为实标量。

**可调：** 是

#### 编程用法

参见 `MinHeight`。

### **Min Distance** — 相邻峰值之间的最小样本数 `1` (默认) | 正整数

将相邻峰值之间的最小样本数指定为正整数。

**可调：** 是

#### 编程用法

参见 `MinDistance`。

### **Threshold** — 峰值高度与其相邻样本之间的最小差 `0` (默认) | 非负标量

将峰值高度与其相邻样本之间的最小差指定为非负标量。

**可调：** 是

#### 编程用法

参见 `Threshold`。

### **Label Peaks** — 标记峰值按钮

点击 **Label Peaks** 按钮以标记峰值。示波器在绘图中的箭头上方显示标签（**P1**、**P2**、…）。

**可调：** 是

#### 编程用法

参见 `LabelPeaks`。

#### 失真

### **Distortion** — 启用失真测量按钮

点击 **Distortion** 按钮以启用失真测量。点击此按钮后，示波器窗口底部会出现 Distortion 面板。

**可调：** 是

#### 编程用法

参见 `Enabled`。

### **Distortion Type** — 要显示的测量类型 `Harmonic` (默认) | `Intermodulation`

将要显示的测量数据类型指定为 `Harmonic` 或 `Intermodulation`。有关更多详细信息，请参阅 Distortion Measurements。

**可调：** 是

#### 编程用法

参见 `Type`。

### **Num Harmonics** — 要测量的谐波数 `6` (默认) | 正整数

将要测量的谐波数指定为小于或等于 99 的正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distortion Type** 设置为 `Harmonic`。

#### 编程用法

参见 `NumHarmonics`。

### **Label Harmonics** — 标记谐波 `off` (默认) | `on`

选择此参数时，Spectrum Analyzer 会向频谱显示中的谐波添加数值标签。

**可调：** 是

#### 编程用法

参见 `LabelValues`。

### **Label Frequencies** — 标记频率 `off` (默认) | `on`

选择此参数时，Spectrum Analyzer 会向 Spectrum Analyzer 显示中的一阶互调产物和三阶频率添加数值标签。

**可调：** 是

#### 编程用法

参见 `LabelValues`。

### 频谱选项卡

#### 轨迹选项

### **Two-Sided Spectrum** — 启用双边频谱视图 `on` (默认) | `off`

选中此复选框以启用双边频谱视图。在此视图中，Spectrum Analyzer 同时显示负频率和正频率。当输入信号为复数值时，必须选择此参数。如果清除此复选框，Spectrum Analyzer 将显示仅包含正频率的单边频谱。在这种情况下，输入信号数据必须为实数值。

清除此复选框时，Spectrum Analyzer 使用功率折叠。除 `0` 和 Nyquist 频率外，*y* 轴的值是选择此参数时的两倍。单边功率谱密度 (PSD) 包含从 DC 到半 Nyquist 速率的频率区间内信号的总功率。有关更多信息，请参阅 `pwelch` (Signal Processing Toolbox)。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `PlotAsTwoSidedSpectrum` |
| **类型：** `logical` |

#### 刻度

### **Frequency Scale** — 频率轴刻度 `Linear` (默认) | `Log`

指定用于显示频率的刻度为 `Linear` 或 `Log`。当频率跨度包含负频率值时，不能选择对数选项。

**可调：** 是

#### 依赖关系

要将 **Frequency Scale** 设置为 `Log`，请清除 **Spectrum** 选项卡中 **Trace Options** 部分中的 **Two-Sided Spectrum** 复选框。如果选中 **Two-Sided Spectrum** 复选框，则 **Frequency Scale** 参数设置为 `Linear`。

#### 编程用法

|  |
| --- |
| **模块参数：** `FrequencyScale` |
| **类型：** character vector or string scalar |

### **Reference load (Ω)** — 以 Ω 为单位的参考负载 `1` (默认) | 正实标量

指定 Spectrum Analyzer 用作计算功率值的参考的参考负载，单位为欧姆。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Spectrum** 类型为 `Power` 或 `Power Density`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ReferenceLoad` |
| **类型：** `double` |

### **Spectrum Unit** — 频谱单位 `dBm` (默认) | `dBm/Hz` | `dBV` | `dBuV` *（自 R2023b 起）* | `Vrms`

将 Spectrum Analyzer 显示功率值所用的单位指定为以下之一：

- `dBm`
- `dBV`
- `dBuV` *（自 R2023b 起）*
- `Vrms`
- `dBm/Hz`

**可调：** 是

#### 依赖关系

可用单位取决于你在 **Scope** 选项卡中为 **Spectrum** 参数选择的值。

| Scope 选项卡 > Spectrum 选项 | 可用单位 |
| --- | --- |
| `Power` | `dBm` |
| `Power Density` | `dBm/Hz` |
| `RMS` | `dBV`, `dBuV` *（自 R2023b 起）*, `Vrms` |

#### 编程用法

|  |
| --- |
| **模块参数：** `SpectrumUnits` |
| **类型：** character vector or string scalar |

### 仅属性检查器

### **Channel Names** — 输入通道名称 `[]` (默认) | character vector | string | array of strings or character vectors.

输入通道名称，指定为字符向量、字符串或数组。这些名称会出现在图例、**Settings** 和 **Measurements** 面板中。如果未指定名称，示波器会将通道标记为 `Channel 1`、`Channel 2` 等。

**示例：** ["A","B"]

#### 依赖关系

要查看通道名称，请在 **Scope** 选项卡中选择 **Legend**。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChannelNames` |
| **类型：** cell array of character vectors or string array |

### **Maximize Axes** — 最大化绘图大小 `Auto` (默认) | `Off` | `On`

- `Auto` — 如果未指定 **Title** 和 **Y-Label**，示波器会最大化所有绘图。
- `On` — 示波器最大化所有绘图，并隐藏 **Title** 和 **Y-label** 中的所有值。
- `Off` — 示波器不最大化绘图。

将鼠标悬停在 Spectrum Analyzer 上可查看最大化坐标轴按钮。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `MaximizeAxes` |
| **类型：** character vector or string scalar |

### **Axes Scaling** — Y 轴缩放模式 `OnceAtStop` (默认) | `Manual` | `Auto` | `Updates`

- `OnceAtStop` — 在仿真完成后缩放 *y* 轴。
- `Manual` — 使用 **Scale Y-axis Limits** 工具栏按钮手动缩放 *y* 轴范围。
- `Auto` — 在仿真期间和仿真后缩放 *y* 轴范围。
- `Updates` — 在 Number of Updates 文本框中指定的时间步数后缩放 *y* 轴（默认 `100`）。每次运行中仅缩放一次。

**可调：** 是

#### 编程用法

|  |
| --- |
| **模块参数：** `AxesScaling` |
| **类型：** character vector or string scalar |

### **Number of Updates** — 缩放前的更新次数 `100` (默认) | integer

设置此属性以延迟 y 轴的自动缩放。

**可调：** 是

#### 依赖关系

要启用此属性，请将 Axes Scaling 设置为 `Updates`。

#### 编程用法

|  |
| --- |
| **模块参数：** `AxesScalingNumUpdates` |
| **类型：** character vector or string scalar |
| **值：** 标量 |

## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可视化。但是，该模块不包含在生成的代码中。

## 版本历史

**在 R2017b 中引入**

### R2025a：单独控制每条线的绘图类型

现在可以单独控制每条线的绘图类型。要控制某条线的绘图类型，请选择该线并相应地设置 **Plot Type** 参数。

### R2025a：支持运行平均方法

Spectrum Analyzer 模块现在支持运行平均方法来计算功率谱估计。要启用此模式，请将 **Estimation** 选项卡中的 **Averaging Method** 参数设置为 `Running`，并将 **Spectral Averages** 参数设置为正整数。

有关更多信息，请参阅 Algorithms 部分。

### R2024b：显示任意数量输入样本的频谱数据并相应调整 RBW

以前，Spectrum Analyzer 模块需要最少样本数才能更新给定 RBW 值的显示。从 R2024b 开始，此限制已移除。示波器现在会针对任意数量的输入样本更新其显示，并相应调整 RBW 值。

### R2024b：自动调整 RBW 以维持 1024 个样本

Spectrum Analyzer 模块现在可以自动调整分辨率带宽 (RBW)，以便无论选择何种窗，都将每次频谱更新的样本数维持在 1024（*Nsamples* = 1024）。

要在 Spectrum Analyzer 模块中启用此模式，请设置：

- **RBW (Hz)** 为 `Auto`。

### R2024b：示波器 UI 中更高的显示精度

现在，可以使用 **Display and Labels** 下的示波器设置中的 **Display Precision** 属性将显示精度提高到 15 位。此精度会影响示波器在其状态栏上显示的所有测量和数据。

### R2024b：**Preserve Colors** 现在在示波器工具条中可用

**Preserve colors for copy to clipboard** 属性已重命名为 **Preserve Colors**，并且现在可在 **Copy Display** 下的示波器工具条中使用。

### R2024a：**Analyzer** 选项卡已重命名为 **Scope** 选项卡

Spectrum Analyzer 中的 **Analyzer** 选项卡已重命名为 **Scope** 选项卡。

### R2023b：Spectrum Analyzer 支持 `dBuV` 单位

当将 **Spectrum** 设置为 `RMS` 时，可以将 **Spectrum Unit** 设置为 `dBuV`。

### R2023a：Simulink 中具有改进响应能力和工具条界面的 Spectrum Analyzer

在 R2023a 中，Spectrum Analyzer 模块响应更快，其工具条界面经过改进，可让您轻松访问频谱分析、估计和测量。可以使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置和显示 Spectrum Analyzer 设置。

## 描述

显示时域信号的频谱

**注意**

RF Blockset™ 中的 Spectrum Analyzer 模块提供 DSP System Toolbox™ 中同名模块所提供的功能的子集。本页描述在 RF Blockset 许可证下可用的模块配置和功能。

如果还拥有 DSP System Toolbox 许可证，则 RF Blockset > Utilities 库中的 Spectrum Analyzer 模块与 DSP System Toolbox > Sinks 库中的模块相同。有关更多信息，请参阅 Spectrum Analyzer (DSP System Toolbox)。

Spectrum Analyzer 模块显示具有离散采样时间的输入信号的频谱。

在 RF Blockset 模型中，要使用 Spectrum Analyzer 模块而不是常规示波器：

1. 将 Spectrum Analyzer 模块添加到您的模块图中。
2. 如果您的模型使用可变步长求解器，还应添加一个 Rate Transition 模块并将其连接到 Spectrum Analyzer 模块的输入端口。将 **Output port sample time** 参数设置为您希望 Spectrum Analyzer 使用的采样时间。

   如果您的模型使用局部求解器，则它会输出具有离散采样时间的物理信号，您无需添加 Rate Transition 模块。但是，如果需要从求解器固定步长进行下采样，则可以使用 Rate Transition 模块。有关使用局部求解器的更多信息，请参阅 Making Optimal Solver Choices for Physical Simulation。
3. 使用 PS-Simulink Converter 模块将感兴趣的物理输出信号连接到 Spectrum Analyzer 模块的输入端口（如果使用 Rate Transition 模块，则连接到其输入端口）。有关更多信息，请参阅 Connecting Simscape Diagrams to Simulink Sources and Scopes。您还可以在 PS-Simulink Converter 和 Spectrum Analyzer 模块之间使用其他信号处理模块来提高信号质量。
4. 运行仿真。仿真完成后，Spectrum Analyzer（此处称为示波器）会打开并显示信号的频谱。

示波器窗口中的信号频谱

### 编程控制

可以使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置和显示 Spectrum Analyzer 设置。
