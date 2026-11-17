---
type: simulink-block
title: 'Spectrum Analyzer'
family: 'sinks'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'spectrumanalyzerblock'
documentation_source_path: '../audio/../dsp/ref/spectrumanalyzerblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Spectrum Analyzer

## 端口

### 输入

### **u** — 要可视化的信号 标量 | 向量 | 矩阵 | 数组

连接要可视化的信号。最多可以有 96 个输入端口。输入信号必须具有以下特征：

- **Signal Domain** — 频域或时域信号。
- **Type** — 离散信号。
- **Data type** — Simulink 支持的任何数据类型。请参阅 Data Types Supported by Simulink (Simulink)。
- **Dimension** — 一维（向量）、二维（矩阵）或多维（数组）信号。输入信号必须具有固定数量的通道。请参阅 Signal Dimensions (Simulink) 和 Determine Signal Dimensions (Simulink)。

Spectrum Analyzer 模块支持可变大小输入信号，即信号帧大小可以在仿真期间变化。当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。有关展示此行为的示例，请参阅 Display Variable-Size Input Signals on Spectrum Analyzer。

Spectrum Analyzer 模块接受 fixed-point 输入，但会将其转换为 `double` 以进行显示。

此端口在启用以下任一输入端口之前没有名称：

- **F**
- **RBW**
- **VBW**

*(自 R2024a 起)*

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **F** — 以 Hz 为单位的频率 列向量

指定以 Hz 为单位的频率。频率向量必须是有限、单调递增、包含两个或更多元素的列向量。频率向量点的数量必须等于输入帧大小。也可以使用 **Estimation** 选项卡上的 **Frequency (Hz)** 参数指定频率。

#### 依赖关系

要启用此端口，请设置：

- **Estimation** 选项卡上的 **Input Domain** 参数为 `Frequency`。
- **Estimation** 选项卡上的 **Frequency (Hz)** 参数为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **RBW** — RBW 值 正标量

通过此端口指定分辨率带宽，以 Hz 为单位。RBW 定义示波器可以分辨的最小正频率。也可以使用 **Estimation** 选项卡上的 **RBW (Hz)** 参数指定 RBW 值。

#### 依赖关系

要启用此端口，请将 **Estimation** 选项卡上的 **RBW (Hz)** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **VBW** — VBW 值 正标量

通过此端口指定视频带宽，以 Hz 为单位。视频带宽是示波器用于在显示信号之前对信号中的噪声进行平均或平滑的低通滤波器的带宽。也可以使用 **Estimation** 选项卡上的 **VBW (Hz)** 参数指定 VBW 值。

#### 依赖关系

要启用此端口，请设置：

- **Estimation** 选项卡上的 **Input Domain** 参数为 `Time`。
- **Estimation** 选项卡上的 **Averaging Method** 参数为 `VBW`。
- **Estimation** 选项卡上的 **VBW (Hz)** 参数为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### Scope 选项卡

#### 视图

### **Spectrum** — 要显示的频谱类型 `Power` (默认) | `Power Density` | `RMS`

将频谱类型设置为以下值之一：

- `Power` — Spectrum Analyzer 显示功率谱。
- `Power Density` — Spectrum Analyzer 显示功率谱密度。功率谱密度是归一化到 1 Hz 带宽的频谱幅度的平方。
- `RMS` — Spectrum Analyzer 显示均方根频谱。使用此选项可查看电压或电流信号的频率。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Estimation** 选项卡上的 **Input Domain** 参数设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpectrumType` |
| **类型：** character vector or string scalar |

### **Spectrogram** — 要显示的频谱图类型 `Power` (默认) | `Power Density` | `RMS`

将频谱图类型设置为以下值之一：

- `Power` — Spectrum Analyzer 显示功率频谱图。
- `Power Density` — Spectrum Analyzer 显示频谱图的功率密度。功率频谱图密度是归一化到 1 Hz 带宽的频谱图幅度的平方。
- `RMS` — Spectrum Analyzer 显示频谱图的均方根。均方根显示均方值的平方根。使用此选项可查看电压或电流信号的频率。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Estimation** 选项卡上的 **Input Domain** 参数设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpectrumType` |
| **类型：** character vector or string scalar |

#### 带宽

### **Sample Rate (Hz)** — 示波器使用的采样率，以 Hz 为单位 `Inherited` (默认) | 正标量

将示波器使用的采样率指定为以下选项之一，以 Hz 为单位：

- `Inherited` — 使用此选项可指定与输入信号相同的采样率。
- 正标量 — 指定的采样率必须至少是输入信号采样率的两倍。否则，由于混叠，在示波器中可视化信号时可能会看到意外行为。

当信号帧大小变化时，示波器使用的采样率会相应变化，进而更新频谱显示的频率跨度。有关展示此行为的示例，请参阅 Display Variable-Size Input Signals on Spectrum Analyzer。

要在状态栏上显示采样率，请点击状态栏中的 ⋮ 图标，然后选择 `Sample Rate`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleRate`, `SampleRateSource` |
| **类型：** `double` |

**可调：** 是

### **Offset (Hz)** — 应用于频率轴的偏移 `0` (默认) | 标量 | 向量

将应用于频率轴（*x* 轴）的偏移指定为以下选项之一，以 Hz 为单位：

- 标量 — 对所有通道应用相同的频率偏移。
- 向量 — 为每个通道应用特定的频率偏移。向量长度必须等于输入通道数。

  总跨度必须落在 Nyquist Frequency Interval 内。您可以根据 **Span (Hz)** 参数的设置方式，以不同方式控制总跨度。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyOffset` |
| **类型：** `double` |

#### 配置 > Spectrum Analyzer 设置（齿轮按钮）

### **Num Inputs** — 输入端口数量 1 (默认) | 1 到 96 之间的整数

模块的输入端口数量，指定为 1 到 96 之间的整数。要更改输入端口数量，请将新的输入信号线拖到模块上，模块会自动创建新端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumInputPorts` |
| **类型：** character vector or string scalar |
| **值：** 1 到 96 之间的标量 |

### **Open at Simulation Start** — 仿真开始时自动打开示波器 on (默认) | off

选择此参数可在运行仿真时自动打开 Spectrum Analyzer 窗口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OpenAtSimulationStart` |
| **类型：** logical |

### **Display Precision** — 示波器显示中数据的精度 `4` (默认) | 小于等于 15 的正整数

*自 R2024b 起*

将示波器显示中数值的精度指定为 [1, 15] 范围内的正整数。

**可调：** 是

### **Y-Label** — *y* 轴标签 字符向量 | 字符串标量

将 Spectrum 显示中的 *y* 轴标签指定为字符向量或字符串标量。要显示信号单位，请将 `(%<SignalUnits>)` 添加到标签中。仿真开始时，Simulink 会将 `(%SignalUnits)` 替换为与信号关联的单位。

例如，对于单位为 m/s 的速度信号，输入

```
Velocity (%<SignalUnits>)
```

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YLabel` |
| **类型：** character vector or string scalar |

### **Y-Limits** — *y* 轴范围 [`−80` `20`] | [`ymin ymax`]

将 Spectrum Analyzer 显示中的 *y* 轴范围指定为 [`ymin ymax`] 形式的二元素数值向量。*y* 轴范围的单位取决于 **Spectrum** 选项卡中的 **Spectrum Unit**。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YLimits` |
| **类型：** `double` |

### **Title** — 显示标题 字符向量 | 字符串

指定显示标题。输入 `%<SignalLabel>` 以将 Simulink 模型中的信号标签用作坐标轴标题。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `Title` |
| **类型：** character vector or string |

### **Show Grid** — 显示内部网格线 `on` (默认) | `off`

选中此复选框可在 Spectrum Analyzer 显示中显示网格。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowGrid` |
| **类型：** `logical` |

### **Color Map** — 频谱图颜色图 `jet` (默认) | `hot` | `bone` | `cool` | `copper` | `gray` | `parula` | 三列矩阵

为频谱图选择有效的颜色图名称，或输入一个三列矩阵，其值在 [0,1] 范围内，用于定义 RGB 三元组。有关颜色图的详细信息，请参阅 `colormap`。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrogram**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Colormap` |
| **类型：** character vector or string scalar |

### **Color Limits** — 频谱图的颜色范围 [`-80 20`] (默认) | [`colorMin colorMax`]

将频谱图的颜色范围指定为 [`colorMin colorMax`] 形式的二元素数值向量。颜色范围的单位直接取决于 **Spectrogram** 选项卡中的 **Spectrum Unit**。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrogram**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ColorLimits` |
| **类型：** `double` |

### **Plot Type** — 绘图类型 `Line` (默认) | `Stem`

指定在 Spectrum 显示中显示 `Line` 还是 `Stem` 绘图。

您可以单独控制每个通道的绘图类型。要控制每个通道的绘图类型，请选择该通道并相应设置 **Plot Type** 参数。*(自 R2025a 起)*

**可调：** 是

#### 依赖关系

要启用此参数：

- 在 **Scope** 选项卡中选择 **Spectrum**。
- 在 **Spectrum** 选项卡中选中 **Normal Trace** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotType` |
| **类型：** character vector or string scalar |

### **Font Size** — 标签的字体大小 `8.5` (默认) | 正标量

将示波器的刻度、标签、标题和测量值的字体大小指定为正标量。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `-` |
| **类型：** double |

### **Background** — 窗口背景 black (默认) | 颜色选择器

指定示波器图窗中的背景色。

**可调：** 是

### **Axes** — 坐标轴背景色 black (默认) | 颜色选择器

指定坐标轴的背景色。

**可调：** 是

### **Labels** — 标签颜色 gray (默认) | 颜色选择器

指定标签、网格和图例中通道名称的颜色。

**可调：** 是

### **Line** — 用于线属性设置的通道 通道名称

指定要修改其可见性、线颜色、样式、宽度和标记属性的通道。

**可调：** 是

### **Visible** — 通道可见性 `on` (默认) | `off`

选中此复选框可显示已选择的通道。如果清除此复选框，所选通道将不再可见。您也可以点击图例中的信号名称来控制其可见性。有关详细信息，请参阅 Legend。

**可调：** 是

### **Style** — 线型 `-` (默认) | `:` | `-`. | `--` | `None`

指定所选通道的线型。

**可调：** 是

### **Width** — 线宽 `1.5` (默认) | `0.5` | `1` | `2` | ...

指定所选通道的线宽。

**可调：** 是

### **Marker** — 数据点标记 `None` (默认) | `+` | `x` | ...

指定所选通道的数据点标记。此参数类似于绘图中的 Marker 属性。可以从下拉列表中选择任何标记符号。

**可调：** 是

### **Color** — 线颜色 yellow (默认) | 颜色选择器

指定所选通道的线颜色。

**可调：** 是

#### 配置

### **Legend** — 显示或隐藏信号图例 按钮

点击 **Legend** 按钮使频谱分析仪显示信号图例。图例显示模型中的信号名称。对于具有多个通道的信号，示波器会在信号名称后附加通道索引。连续信号名称前有直线，离散信号名称前有阶梯线。

您可以使用图例控制哪些信号可见。要隐藏信号，请在示波器图例中点击信号名称。要显示信号，请再次点击信号名称。或者，您可以使用 **Spectrum Analyzer Settings**（齿轮按钮）中的 **Visible** 参数控制哪个信号可见。

要仅显示一个信号并隐藏所有其他信号，请右键点击希望示波器显示的信号名称。要显示所有信号，请按 **Esc**。

**注意**

图例仅显示前 20 个信号。您无法从图例查看或控制任何其他信号。

**可调：** 是

#### 依赖关系

要启用 **Legend**，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowLegend` |
| **类型：** `logical` |

### **Colorbar** — 显示或隐藏颜色条 按钮

选择 **Colorbar** 按钮后，频谱分析仪会显示颜色条。

**可调：** 是

#### 依赖关系

要启用 **Colorbar** 按钮，请在 **Scope** 选项卡中选择 **Spectrogram**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowColorbar` |
| **类型：** `logical` |

### **Layout** — 垂直或水平堆叠坐标轴 vertical layout (默认) | horizontal layout

通过在布局网格中选择适当的配置，垂直或水平堆叠坐标轴。

**可调：** 是

#### 依赖关系

要启用 **Layout**，请在 **Scope** 选项卡中选择 **Spectrum** 和 **Spectrogram**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AxesLayout` |
| **类型：** character vector or string scalar |

#### 共享

### **Copy to Clipboard** — 将显示内容发送到剪贴板 按钮

点击此按钮可将示波器显示内容复制到剪贴板。您可以通过在 **Copy to Clipboard** 下拉列表中选择 **Preserve Colors** 来保留显示中的颜色。

### **Preserve Colors** — 复制到剪贴板时保留颜色 `off` (默认) | `on`

当您使用 **Scope** 选项卡 > **Share** 部分中的 **Copy to Clipboard** 和 **Print** 选项将显示内容复制到剪贴板时，选择此参数可使示波器保留颜色。

要访问 **Preserve Colors**，请点击 **Copy to Clipboard** 的下拉箭头。

**可调：** 是

### **Print** — 打印显示内容 按钮

点击此按钮可将示波器显示内容保存为图像或 PDF，或打印显示内容。

### Estimation 选项卡

#### 域

### **Input Domain** — 输入信号的域 `Time` (默认) | `Frequency`

要可视化的输入信号的域。如果要可视化时域信号，示波器会根据 **Estimation Method** 参数中指定的算法将信号变换为频谱。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputDomain` |
| **类型：** character vector or string scalar |

### **Frequency (Hz)** — 频率向量 `Auto` (默认) | `Input port` | 单调递增向量

将决定显示 *x* 轴的频率向量设置为以下值之一：

- `Auto` — 示波器根据输入长度计算频率向量。有关详细信息，请参阅 Frequency Vector。
- `Input port` — 您在模块的 **Frequency** 输入端口指定频率向量。
- 自定义向量 — 您指定自定义向量作为频率向量。自定义向量的长度必须等于输入信号的帧大小。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Input Domain** 设置为 `Frequency`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyVectorSource`, `FrequencyVector` |
| **类型：** character vector, string scalar, `double` |

### **Input Unit** — 频率输入的单位 `dBm` (默认) | `dBuV` *(自 R2023b 起)* | `dBV` | `dBW` | `Vrms` | `Watts` | `None`

选择频域输入的单位。当您在 **Estimation** 选项卡的 **Spectrum Unit** 参数中选择不同的显示单位时，此参数使频谱分析仪能够缩放频率数据。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Input Domain** 设置为 `Frequency`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputUnits` |
| **类型：** character vector or string scalar |

#### 频率分辨率

### **Estimation Method** — 频谱估计方法 `Filter Bank` (默认) | `Welch`

将频谱估计方法选择为以下之一：

- `Filter Bank` — 使用分析滤波器组估计功率谱。与 Welch 方法相比，此方法具有更低的噪声底、更好的频率分辨率、更低的频谱泄漏，并且每次更新需要的样本更少。
- `Welch` — 使用平均修正周期图的 Welch 方法。

有关这些方法的更多详细信息，请参阅 Algorithms。

**可调：** 是

#### 依赖关系

要使用此参数，请将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Method` |
| **类型：** character vector or string scalar |

### **Resolution Method** — 频率分辨率方法 `RBW` (默认) | `Number of frequency bands` | `Window length`

*自 R2024a 起*

将频谱分析仪的频率分辨率方法指定为以下选项之一：

- `RBW` — **RBW (Hz)** 参数控制分析仪的频率分辨率（以 Hz 为单位）。
- `Number of frequency bands` — 仅当将 **Estimation Method** 设置为 `Filter bank` 时适用。**FFT Length** 参数控制频率分辨率。
- `Window length` — 仅当将 **Estimation Method** 设置为 `Welch` 时适用。**Window Length** 参数控制频率分辨率。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyResolutionMethod` |
| **类型：** character vector or string scalar |

### **Filter Sharpness** — 低通滤波器的锐度 `0.5` (默认) | [0,1] 范围内的非负标量

将原型低通滤波器的锐度指定为 [0,1] 范围内的实数非负标量。

提高滤波器锐度可减少频谱泄漏，并提供更准确的功率读数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Estimation Method** 设置为 `Filter bank`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FilterSharpness` |
| **类型：** `double` |

### **RBW (Hz)** — 分辨率带宽，以 Hz 为单位 `Auto` (默认) | `Input port` | 正标量

指定分辨率带宽，以 Hz 为单位。此参数定义示波器可以分辨的最小正频率。默认情况下，此参数设置为 `Auto`。在这种情况下，频谱分析仪会确定适当的值，以确保在指定频率跨度上有 1024 个 RBW 区间。

如果将此参数设置为 `Input port`，则可以通过模块上的输入端口指定 RBW 值。

如果将此参数设置为数值，则该值必须允许在指定频率跨度上至少有 2 个 RBW 区间。换句话说，总频率跨度与 RBW 的比值必须大于二：

spanRBW>2

要在状态栏上显示此属性，请点击状态栏中的 ⋮ 图标并选择 `RBW`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RBWSource`, `RBW` |
| **类型：** character vector, string scalar, `double` |

**可调：** 是

### **Window Length** — 窗长度 `1024` (默认) | 大于 2 的整数

*自 R2024a 起*

将窗长度指定为大于 2 的整数，以样本为单位。模块使用窗长度计算频谱估计。此参数控制频率分辨率。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Estimation Method** 为 `Welch`。
- **Resolution Method** 为 `Window Length`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `WindowLength` |
| **类型：**`double` |

### **FFT Length** — FFT 长度 `Auto` (默认) | `1024` | 正整数

*自 R2024a 起*

可以将 FFT 长度设置为以下选项之一：

- `Auto` — FFT 长度的值取决于频率分辨率方法的设置。当您设置：

  - **Resolution Method** 为 `RBW` 时，FFT 长度等于每次更新的样本数 *Nsamples*。有关 *Nsamples* 的更多详细信息，请参阅 Algorithms 部分。
  - **Resolution Method** 为 `Window length` 时，FFT 长度等于您在 **Window length** 参数中指定的值或 1024，以较大者为准。
  - **Resolution Method** 为 `Number of frequency bands` 时，FFT 长度等于输入帧大小（行数）。
- 正整数 — FFT 点数等于您在 `FFTLength` 属性中指定的值。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Estimation Method** 为 `Welch`。
- **Estimation Method** 为 `Filter bank` 且 **Resolution Method** 为 `Number of frequency bands`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FFTLengthSource`, `FFTLength` |
| **类型：**character vector or string scalar, `double` |

#### 平均

### **Averaging Method** — 平滑方法 `VBW` (默认) | `Exponential` | `Running`

将平滑方法指定为以下之一：

- `VBW` — 视频带宽方法。模块使用低通滤波器平滑迹线并降低噪声。使用 **VBW (Hz)** 参数指定视频带宽 (VBW) 值。
- `Exponential` — 样本的加权平均。模块通过对样本进行平均来计算平均值，并使用指数衰减遗忘因子进行加权。使用 **Forgetting Factor** 参数指定加权遗忘因子。
- `Running` — 最近 *Q* 个样本的运行平均值。使用 **Spectral Averages** 参数指定 *Q*。*(自 R2025a 起)*

有关平均方法的更多信息，请参阅 Averaging Method。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AveragingMethod` |
| **类型：** character vector or string scalar |

### **VBW (Hz)** — 视频带宽 `Auto` (默认) | `Input port` | 正标量

将视频带宽指定为以下之一：

- `Auto` — 频谱分析仪调整 VBW，使等效遗忘因子为 0.9。
- `Input port` — 您在模块的 **VBW** 输入端口指定频率向量。
- 正标量 — 您指定正标量。频谱分析仪使用此值调整 VBW。指定的值必须小于等于 **Sample Rate (Hz)**/2。

有关视频带宽方法的更多详细信息，请参阅 Averaging Method。

频谱分析仪在显示底部的状态栏中显示 VBW 值。要显示 VBW 值，请点击状态栏中的 ⋮ 图标并选择 `VBW`。

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- `Averaging Method` 为 `VBW`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VBWSource`, `VBW` |
| **类型：** `double` |

**可调：** 是

### **Forgetting Factor** — 加权平均方法的遗忘因子 `0.9` (默认) | [0,1] 范围内的标量

将指数加权平均方法的遗忘因子指定为 [0,1] 范围内的标量。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Averaging Method** 为 `Exponential`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ForgettingFactor` |
| **类型：** `double` |

### **Spectral Averages** — 频谱平均次数 `1` (默认) | 正整数

*自 R2025a 起*

将频谱平均次数 *Q* 指定为正整数。

频谱分析仪通过计算最近 *Q* 个功率谱估计的运行平均值来计算当前功率谱估计。

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Averaging Method** 为 `Running`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpectralAverages` |
| **类型：** `double` |

**数据类型：** `double`

#### 频率选项

### **Frequency Span** — 频率跨度模式 `Full` (默认) | `Span and Center Frequency` | `Start and Stop Frequencies`

将频率跨度模式指定为以下之一：

- `Full` — 频谱分析仪在整个 Nyquist Frequency Interval 上计算并绘制频谱。
- `Span and Center Frequency` — 频谱分析仪在 **Span (Hz)** 和 **Center Frequency (Hz)** 参数指定的区间上计算并绘制频谱。
- `Start and Stop Frequencies` — 频谱分析仪在 **Start Frequency (Hz)** 和 **Stop Frequency (Hz)** 参数指定的区间上计算并绘制频谱。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencySpan` |
| **类型：** character vector or string scalar |

### **Span (Hz)** — 计算频谱的频率跨度，以 Hz 为单位 `10e3` (默认) | 实数正标量

指定频谱分析仪计算并绘制频谱的频率跨度，以 Hz 为单位。由该参数和 **Center Frequency (Hz)** 参数定义的总跨度必须落在 Nyquist Frequency Interval 内。此参数定义频谱分析仪窗口中 Frequency 轴上显示的值范围。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Frequency Span** 为 `Span and Center Frequency`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Span` |
| **类型：** `double` |

### **Center Frequency (Hz)** — 频率跨度中心，以 Hz 为单位 `0` (默认) | 实数标量

指定频谱分析仪计算并绘制频谱的频率跨度中心，以 Hz 为单位。将此参数与 **Span (Hz)** 参数一起使用，以定义围绕中心频率的频率跨度。此参数定义频谱分析仪窗口中 Frequency 轴的中点。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Frequency Span** 为 `Span and Center Frequency`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CenterFrequency` |
| **类型：** `double` |

### **Start Frequency (Hz)** — 起始频率，以 Hz 为单位 `-5e3` (默认) | 标量

指定频谱分析仪计算并绘制频谱的频率区间起始频率，以 Hz 为单位。由该参数和 **Stop Frequency (Hz)** 参数定义的总跨度必须落在 Nyquist Frequency Interval 内。此参数定义频谱分析仪窗口中 Frequency 轴的最左侧值。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Frequency Span** 为 `Start and Stop Frequencies`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartFrequency` |
| **类型：** `double` |

### **Stop Frequency (Hz)** — 停止频率，以 Hz 为单位 `5e3` (默认) | 标量

指定频谱分析仪计算并绘制频谱的频率区间停止频率，以 Hz 为单位。由该参数和 **Start Frequency (Hz)** 参数定义的总跨度必须落在 Nyquist Frequency Interval 内。此参数定义频谱分析仪窗口中 Frequency 轴的最右侧值。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Frequency Span** 为 `Start and Stop Frequencies`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StopFrequency` |
| **类型：** `double` |

#### 窗选项

### **Window** — 加窗方法 `Hann` (默认) | `Blackman-Harris` | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular` | 自定义窗函数名称

指定应用于频谱的加窗方法。加窗用于控制频谱估计中旁瓣的影响。您指定的窗会影响达到分辨率带宽所需的窗长度以及每次更新所需的样本数。有关加窗的详细信息，请参阅 Windows。

您可以通过在 **Window** 参数中直接指定自定义窗函数名称来使用自己的频谱估计窗。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Estimation Method** 为 `Welch`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Window`, `CustomWindow` |
| **类型：** character vector or string scalar |

### **Attenuation (dB)** — 旁瓣衰减，以 dB 为单位 `60` (默认) | 大于等于 `45` 的标量

将旁瓣衰减指定为大于等于 `45` 的标量，以 dB 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Window** 设置为 `Chebyshev` 或 `Kaiser`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SidelobeAttenuation` |
| **类型：** `double` |

### **Overlap (%)** — 重叠百分比 `0` (默认) | [0 100) 范围内的标量

将前一个和当前缓冲数据段之间的重叠百分比指定为 [0 100) 范围内的标量。重叠会创建一个窗段，示波器使用该窗段计算频谱估计。该值必须大于等于零且小于 100。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Input Domain** 为 `Time`。
- **Estimation Method** 为 `Welch`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OverlapPercent` |
| **类型：** `double` |

### Measurements 选项卡

**注意**

要访问相位噪声测量设置，您必须拥有有效的 Mixed-Signal Blockset™ 许可证。

#### 通道

### **Channel** — 要获取测量的通道 `1` (默认) | 正整数

要获取测量的通道，指定为 [1 *N*] 范围内的正整数，其中 *N* 是输入通道数。

**可调：** 是

#### 依赖关系

要启用此参数，请通过示波器传递一些数据。

#### 程序化使用

请参阅 `MeasurementChannel`。

#### 光标

### **Data Cursors** — 启用光标测量 按钮

点击 **Data Cursors** 按钮以启用数据光标测量。每个光标沿信号跟踪一条垂直线。示波器在光标之间的框中显示两个光标处信号的 *x* 值和 *y* 值之差。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Snap to data** — 将光标捕捉到数据 `off` (默认) | `on`

选择此参数可将光标定位在信号数据点上。

**可调：** 是

#### 程序化使用

请参阅 `SnapToData`。

### **Lock cursor spacing** — 锁定光标间距 `off` (默认) | `on`

选择此参数可锁定两个光标之间的频率差。

**可调：** 是

#### 程序化使用

请参阅 `LockSpacing`。

#### 峰值

### **Peak Finder** — 启用峰值查找测量 按钮

点击 **Peak Finder** 按钮以启用峰值查找测量。每个最大值处会在绘图上出现一个箭头，并且示波器窗口底部会出现 Peaks 面板。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Num Peaks** — 要显示的最大峰值数 `3` (默认) | 小于 100 的正整数

将要显示的最大峰值数指定为小于 100 的正整数。

**可调：** 是

#### 程序化使用

请参阅 `NumPeaks`。

### **Min Height** — 示波器检测峰值的电平阈值 `-Inf` (默认) | 实数标量值

将示波器检测峰值的电平阈值指定为实数标量。

**可调：** 是

#### 程序化使用

请参阅 `MinHeight`。

### **Min Distance** — 相邻峰值之间的最小样本数 `1` (默认) | 正整数

将相邻峰值之间的最小样本数指定为正整数。

**可调：** 是

#### 程序化使用

请参阅 `MinDistance`。

### **Threshold** — 峰值高度与其相邻样本之间的最小差值 `0` (默认) | 非负标量

将峰值高度与其相邻样本之间的最小差值指定为非负标量。

**可调：** 是

#### 程序化使用

请参阅 `Threshold`。

### **Label Peaks** — 标记峰值 按钮

点击 **Label Peaks** 按钮以标记峰值。示波器会在绘图中的箭头上方显示标签（**P1**、**P2**、…）。

**可调：** 是

#### 程序化使用

请参阅 `LabelPeaks`。

#### 失真

### **Distortion** — 启用失真测量 按钮

点击 **Distortion** 按钮以启用失真测量。点击此按钮后，示波器窗口底部会出现 Distortion 面板。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Distortion Type** — 要显示的测量数据类型 `Harmonic` (默认) | `Intermodulation`

将要显示的测量数据类型指定为 `Harmonic` 或 `Intermodulation`。有关更多详细信息，请参阅 Distortion Measurements。

**可调：** 是

#### 程序化使用

请参阅 `Type`。

### **Num Harmonics** — 要测量的谐波数 `6` (默认) | 正整数

将要测量的谐波数指定为小于等于 99 的正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distortion Type** 设置为 `Harmonic`。

#### 程序化使用

请参阅 `NumHarmonics`。

### **Label Harmonics** — 标记谐波 `off` (默认) | `on`

选择此参数后，频谱分析仪会在频谱显示中为谐波添加数值标签。

**可调：** 是

#### 程序化使用

请参阅 `LabelValues`。

### **Label Frequencies** — 标记频率 `off` (默认) | `on`

选择此参数后，频谱分析仪会在频谱分析仪显示中为一阶互调产物和三阶频率添加数值标签。

**可调：** 是

#### 程序化使用

请参阅 `LabelValues`。

#### 相位噪声

### **Phase Noise** — 启用相位噪声测量 按钮

点击 **Phase Noise** 按钮以启用相位噪声测量。点击此按钮后，示波器窗口中会出现 Phase Noise 轴和 Phase Noise 面板。

**注意**

要访问相位噪声测量设置，您必须拥有有效的 Mixed-Signal Blockset 许可证。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Frequency Offsets (Hz)** — 频率偏移，以 Hz 为单位 [`10 100 1000`] (默认) | 具有单调递增值的向量

将示波器测量相位噪声时的频率偏移指定为具有单调递增值的数值向量，以 Hz 为单位。

**可调：** 是

#### 程序化使用

请参阅 `FrequencyOffset`。

### **Plot Target Phase Noise** — 绘制目标相位噪声曲线的选项 off (默认) | on

选择此参数可绘制目标相位噪声曲线。您可以在 **Target Phase Noise (dBc/Hz)** 参数中指定此曲线。

**可调：** 是

#### 程序化使用

请参阅 `PlotTargetPhaseNoise`。

### **Target Phase Noise (dBc/Hz)** — 目标相位噪声曲线，以 dBc/Hz 为单位 [`-300 -300 -300`] (默认) | 向量

将目标相位噪声曲线指定为与 **Frequency Offsets (Hz)** 向量长度相同的数值向量，以 dBc/Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请选择 **Plot Target Phase Noise** 参数。

#### 程序化使用

请参阅 `TargetPhaseNoise`。

### **Label Phase Noise** — 在绘图上标记测得相位噪声的选项 off (默认) | on

选择此参数可在绘图上标记测得的相位噪声。选择此参数后，频谱分析仪会在绘图上将测得的相位噪声值标记为 `SN1`、`SN2` 等。

**可调：** 是

#### 程序化使用

请参阅 `LabelPhaseNoise`。

### Spectrum 选项卡

**注意**

当您在 **Scope** 选项卡中选择 **Spectrum** 时，此选项卡会出现。

#### 迹线选项

### **Two-Sided Spectrum** — 启用双边频谱视图 `on` (默认) | `off`

选中此复选框可启用双边频谱视图。在此视图中，频谱分析仪会显示负频率和正频率。当输入信号为复值时，必须选择此参数。如果清除此复选框，频谱分析仪将显示仅包含正频率的单边频谱。在这种情况下，输入信号数据必须为实值。

清除此复选框时，频谱分析仪使用功率折叠。除 `0` 和 Nyquist 频率处外，*y* 轴值将是选择此参数时的两倍。单边功率谱密度 (PSD) 包含从 DC 到一半 Nyquist 速率的频率区间内信号的总功率。有关详细信息，请参阅 `pwelch`。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotAsTwoSidedSpectrum` |
| **类型：** `logical` |

### **Normal Trace** — 普通迹线视图 `on` (默认) | `off`

选中此复选框时，频谱分析仪会计算并绘制功率谱估计。频谱分析仪通过对多个频谱估计求平均来执行平滑操作，并且即使清除此参数，也会继续其频谱计算。

**可调：** 是

#### 依赖关系

要清除此复选框，请先选择 **Max-Hold Trace** 或 **Min-Hold Trace** 参数。

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotNormalTrace` |
| **类型：** `logical` |

### **Max-Hold Trace** — 最大保持迹线视图 `off` (默认) | `on`

选中此复选框可使频谱分析仪绘制所有估计的最大频谱值。频谱分析仪通过保留所有功率谱估计的最大值来计算每个频率 bin 处的最大保持频谱。清除此复选框时，频谱分析仪会重置其最大保持计算。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotMaxHoldTrace` |
| **类型：** `logical` |

### **Min-Hold Trace** — 最小保持迹线视图 `off` (默认) | `on`

选中此复选框可使频谱分析仪绘制所有估计的最小频谱值。频谱分析仪通过保留所有功率谱估计的最小值来计算每个频率 bin 处的最小保持频谱。清除此复选框时，频谱分析仪会重置其最小保持计算。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrum**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PlotMinHoldTrace` |
| **类型：** `logical` |

#### 刻度

### **Frequency Scale** — 频率轴刻度 `Linear` (默认) | `Log`

将显示频率的刻度指定为 `Linear` 或 `Log`。当频率跨度包含负频率值时，不能选择对数选项。

**可调：** 是

#### 依赖关系

要将 **Frequency Scale** 设置为 `Log`，请清除 **Spectrum** 或 **Spectrogram** 选项卡（如果启用）中 **Trace Options** 部分的 **Two-Sided Spectrum** 复选框。如果选中 **Two-Sided Spectrum** 复选框，则 **Frequency Scale** 参数设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyScale` |
| **类型：** character vector or string scalar |

### **Reference load (Ω)** — 参考负载，以 Ω 为单位 `1` (默认) | 正实数标量

指定 Spectrum Analyzer 用作计算功率值的参考负载，以欧姆为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请设置：

- **Spectrum** 类型为 `Power` 或 `Power Density`。
- **Spectrum Unit** 为除 `dBFS` 或 `dBFS/Hz` 以外的任何选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ReferenceLoad` |
| **类型：** `double` |

### **Spectrum Unit** — 频谱单位 `dBm` (默认) | `dBFS` | `dBV` | `dBuV` *(自 R2023b 起)* | `dBW` | `Vrms` | `Watts` | `dBm/Hz` | `dBW/Hz` | `dBFS/Hz` | `Watts/Hz` | `Auto`

将频谱分析仪显示功率值所用的单位指定为以下之一：

- `dBm`
- `dBFS`
- `dBuV` *(自 R2023b 起)*
- `dBV`
- `dBW`
- `Vrms`
- `Watts`
- `dBm/Hz`
- `dBW/Hz`
- `dBFS/Hz`
- `Watts/Hz`
- `Auto`

**可调：** 是

#### 依赖关系

可用单位取决于您在 **Scope** 选项卡中为 **Spectrum** 参数选择的值。

| Estimation 选项卡 > Input Domain 参数 | Scope 选项卡 > Spectrum 选项 | 可用单位 |
| --- | --- | --- |
| `Time` | `Power` | `dBm`, `dBW`, `dBFS`, `Watts` |
| `Power Density` | `dBm/Hz`, `dBW/Hz`,`dBFS/Hz`, `Watts/Hz` |
| `RMS` | `dBuV` *(自 R2023b 起)*, `dBV`, `Vrms` |
| `Frequency` | ― | `Auto`, `dBm`, `dBuV` *(自 R2023b 起)*, `dBV`, `dBW`, `Vrms`, `Watts` |

如果 **Input Domain** 参数设置为 `Frequency`，且 **Spectrum Unit** 参数设置为 `Auto`，则频谱分析仪假定频谱单位等于 **Estimation** 选项卡 > **Input Unit** 参数中指定的输入单位。如果 **Input Domain** 参数设置为 `Time`，且 **Spectrum Unit** 参数设置为 `Auto` 以外的任何选项，则频谱分析仪会将 **Input Unit** 参数中指定的单位转换为 **Spectrum Unit** 参数中指定的单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpectrumUnits` |
| **类型：** character vector or string scalar |

### **Full Scale** — dBFS 单位的满量程 `Auto` (默认) | 正实数标量

用于分贝满量程 (dBFS) 单位的满量程。默认情况下，频谱分析仪使用整个频谱量程。为 dBFS 满量程指定正实数标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 在 **Scope** 选项卡中，将频谱类型设置为 `Power` 或 `Power Density`。
- 在 **Estimation** 选项卡中，将 **Input Domain** 设置为 `Time`。
- 在 **Spectrum** 选项卡中，将 **Spectrum Unit** 设置为 `dBFS` 或 `dBFS/Hz`（当频谱类型设置为 `Power Density` 时）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FullScale` |
| **类型：** `double` |

### Spectrogram 选项卡

**注意**

当您在 **Scope** 选项卡中选择 **Spectrogram** 时，此选项卡会出现。

#### 通道

### **Channel** — 为其绘制频谱图的通道 `1` (默认) | 正整数的字符向量 | 正整数的字符串标量

选择频谱图设置适用的信号通道。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrogram**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpectrogramChannel` |
| **类型：** character vector, string scalar, `double` |

#### 时间选项

### **Time Resolution (s)** — 时间分辨率，以秒为单位 `Auto` (默认) | 正标量

时间分辨率是用于计算一条频谱图线的数据量，以秒为单位。最小可达到的分辨率是计算单个频谱估计所需的时间量。工具提示会显示给定当前频谱分析仪设置下的最小可达到分辨率。

当将 **RBW (Hz)** 和 **Time Resolution (s)** 设置为 `Auto` 时，频谱分析仪会调整 RBW 值，使一个频率跨度内有 1024 个 RBW 区间，并将时间分辨率设置为 1/`RBW`。

当将 **RBW (Hz)** 设置为 `Auto`，并将 **Time Resolution (s)** 设置为正标量时，时间分辨率成为主要控制项，RBW 设置为 1/**Time Resolution (s)** Hz。

当将 **RBW (Hz)** 设置为正标量，并将 **Time Resolution (s)** 设置为 `Auto` 时，RBW 成为主要控制项，时间分辨率设置为 1/**RBW (Hz)** s。

当将 **RBW (Hz)** 和 **Time Resolution (s)** 设置为正值时，时间分辨率必须大于等于由 1/**RBW (Hz)** 定义的最小可达到时间分辨率。多个频谱估计会组合成一条频谱图线，以获得所需的时间分辨率。对于不是 1/**RBW (Hz)** 整数倍的时间分辨率值，会使用插值。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrogram**，并在 **Estimation** 选项卡中将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TimeResolutionSource`, `TimeResolution` |
| **类型：** character vector, string scalar, `double` |

### **Time Span (s)** — 时间跨度，以秒为单位 `Auto` (默认) | 正标量

频谱分析仪显示频谱图的时间跨度，指定为正标量，以秒为单位。时间跨度是所需频谱线数与时间分辨率的乘积。当将此参数设置为 `Auto` 时，频谱图在任何给定时间显示 100 条频谱图线。否则，频谱图使用此参数中指定的时间长度。您指定的时间跨度必须至少比一次频谱更新所需样本数的持续时间大两倍。

**可调：** 是

#### 依赖关系

要启用此参数，请在 **Scope** 选项卡中选择 **Spectrogram**，并在 **Estimation** 选项卡中将 **Input Domain** 设置为 `Time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TimeSpanSource`, `TimeSpan` |
| **类型：** character vector, string scalar, `double` |

有关 `Two-Sided Spectrum` 的更多信息，请参阅 Spectrum Tab > Trace Options。

### Spectral Mask 选项卡

**注意**

当您在 **Scope** 选项卡中选择 **Spectrum**，并将 **Spectrum** 类型设置为 `Power` 或 `Power Density` 时，此选项卡会出现。

#### 视图

### **Upper Mask** — 启用上频谱掩码 按钮

选择 **Upper Mask** 可在频谱图中显示上掩码。频谱分析仪窗口底部会出现 **Spectral Mask** 面板，并显示掩码详细信息，例如掩码成功次数、掩码失败次数、导致掩码失败的通道等。

使用 **Upper Limits** 参数指定上掩码。如果整个频谱图都低于上掩码，则上掩码显示为绿色。在所有其他情况下，上掩码显示为红色。

**可调：** 是

#### 程序化使用

请参阅 `EnabledMasks`。

### **Lower Mask** — 启用下频谱掩码 按钮

选择 **Lower Mask** 可在频谱图中显示下掩码。频谱分析仪窗口底部会出现 **Spectral Mask** 面板，并显示掩码详细信息，例如掩码成功次数、掩码失败次数、导致掩码失败的通道等。

使用 **Lower Limits** 参数指定下掩码。如果整个频谱图都高于下掩码，则下掩码显示为绿色。在所有其他情况下，下掩码显示为红色。

**可调：** 是

#### 程序化使用

请参阅 `EnabledMasks`。

#### 配置

### **Upper Limits** — 上频谱掩码的限制 `Inf` (默认) | 标量 | 两列矩阵

将上频谱掩码的限制指定为标量或两列矩阵。

如果 `UpperMask` 是标量，则上限掩码对频谱分析仪中指定的所有频率使用相同的功率值。

如果指定矩阵，则第一列包含频率值 (Hz)，对应 *x* 轴值。第二列包含功率值，对应关联的 *y* 轴值。

要对功率和频率值应用偏移，请使用 **Reference Level (dBr)** 和 **Frequency Offset (Hz)** 参数。

**可调：** 是

#### 程序化使用

请参阅 `UpperMask`。

### **Lower Limits** — 下频谱掩码的限制 `-Inf` (默认) | 标量 | 两列矩阵

将下频谱掩码的限制指定为标量或两列矩阵。

如果 `LowerMask` 是标量，则下限掩码对频谱分析仪中指定的所有频率使用相同的功率值。

如果指定矩阵，则第一列包含频率值 (Hz)，对应 *x* 轴值。第二列包含功率值，对应关联的 *y* 轴值。

要对功率和频率值应用偏移，请使用 **Reference Level (dBr)** 和 **Frequency Offset (Hz)** 参数。

**可调：** 是

#### 程序化使用

请参阅 `LowerMask`。

### **Reference Level (dBr)** — 掩码功率值的参考电平 `0` (默认) | 实数标量 | `Spectrum peak`

将掩码功率值的参考电平指定为数值标量，或将其设置为 `Spectrum peak`。

当将 **Reference Level (dBr)** 设置为标量值时，频谱分析仪使用此值作为频谱分析仪上掩码和下掩码功率值（以 dBr 为单位）的参考。参考电平应与 **Spectrum** 选项卡中的 **Spectrum Unit** 参数具有相同单位。

当将 **Reference Level (dBr)** 设置为 `Spectrum peak` 时，频谱分析仪使用 **Spectral Mask** 选项卡中 **Channel** 当前频谱的峰值作为参考功率值。

**可调：** 是

#### 程序化使用

请参阅 `ReferenceLevel` 和 `CustomReferenceLevel`。

### **Channel** — 具有峰值频谱的输入通道 `1` (默认) | 整数

选择频谱分析仪用于确定掩码参考电平的输入通道。当将 **Reference Level (dBr)** 参数设置为 `Spectrum peak` 时，此通道中频谱的峰值将成为掩码参考电平。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Reference Level (dBr)** 设置为 `Spectrum peak`，并在示波器上显示一些数据。

#### 程序化使用

请参阅 `SelectedChannel`。

### **Frequency Offset (Hz)** — 频率偏移，以 Hz 为单位 `0` (默认) | 有限数值标量

将频率偏移指定为有限数值标量，以 Hz 为单位。使用此值，频谱分析仪会偏移 **Upper Mask** 和 **Lower Mask** 参数中的频率值。

**可调：** 是

#### 程序化使用

请参阅 `MaskFrequencyOffset`。

### Channel Measurements 选项卡

**注意**

当您在 **Scope** 选项卡中选择 **Spectrum** 时，此选项卡会出现。

#### 通道

### **Channel** — 用于计算占用带宽和相邻通道功率比的通道 `1` (默认) | 正整数

指定频谱分析仪计算并显示占用带宽和相邻通道功率比的通道，指定为 [1 *N*] 范围内的正整数，其中 *N* 是输入通道数。

**可调：** 是

#### 依赖关系

要启用此参数，请通过示波器传递数据。

#### 程序化使用

请参阅 `MeasurementChannel`。

#### 通道测量

### **Channel Measurements** — 启用通道测量 按钮

点击 **Channel Measurements** 以启用通道测量。

**可调：** 是

#### 程序化使用

请参阅 `Enabled`。

### **Type** — 要显示的测量数据类型 `Occupied BW` (默认) | `ACPR`

将要显示的测量数据类型指定为 `Occupied BW` 或 `ACPR`。

**可调：** 是

#### 程序化使用

请参阅 `Type`。

### **Occupied BW (%)** — 用于计算占用带宽的功率百分比 `99` (默认) | 正标量

将频谱分析仪计算占用带宽时使用的功率百分比指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Occupied BW`。

#### 程序化使用

请参阅 `PercentOccupiedBW`。

#### 频率选项

### **Frequency Span** — 频率跨度模式 `Span and Center Frequency` (默认) | `Start and Stop Frequencies`

将频率跨度模式指定为以下之一：

- `Span and Center Frequency` — 在 **Span (Hz)** 指定的频率范围内，并围绕 **Center Frequency (Hz)** 指定的频率值进行测量。
- `Start and Stop Frequencies` — 在频率范围 [**Start Frequency (Hz)**, **Stop Frequency (Hz)**] 内测量。

**可调：** 是

#### 程序化使用

请参阅 `FrequencySpan`。

### **Span (Hz)** — 频率跨度，以 Hz 为单位 `2000` (默认) | 正标量

将频谱分析仪计算通道测量的频率跨度指定为正标量，以 Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Frequency Span** 设置为 `Span and Center Frequency`。

#### 程序化使用

请参阅 `Span`。

### **Center Frequency (Hz)** — 跨度的中心频率，以 Hz 为单位 `0` (默认) | 实数标量

对象计算通道测量的跨度中心频率，指定为实数标量，以 Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Frequency Span** 设置为 `Span and Center Frequency`。

#### 程序化使用

请参阅 `CenterFrequency`。

### **Start Frequency (Hz)** — 起始频率，以 Hz 为单位 `-1000` (默认) | 实数标量

指定频谱分析仪计算通道测量的起始频率，以 Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Frequency Span** 设置为 `Start and Stop Frequencies`。

#### 程序化使用

请参阅 `StartFrequency`。

### **Stop Frequency (Hz)** — 停止频率，以 Hz 为单位 `1000` (默认) | 实数标量

指定频谱分析仪计算通道测量的停止频率，以 Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Frequency Span** 设置为 `Start and Stop Frequencies`。

#### 程序化使用

请参阅 `StopFrequency`。

#### 相邻通道

### **Num Pairs** — 相邻通道对数量 `2` (默认) | 范围 [`1`, `12`] 内的正整数

将相邻通道对数量指定为范围 [`1`, `12`] 内的正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`。

#### 程序化使用

请参阅 `NumOffsets`。

### **Offsets (Hz)** — ACPR 偏移，以 Hz 为单位 `[2000 3500]` (默认) | 向量

将相邻通道相对于主通道中心频率的频率指定为实数向量，其长度等于 **Num Pairs** 中指定的偏移对数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`。

#### 程序化使用

请参阅 `ACPROffsets`。

### **Adjacent BW (Hz)** — 相邻通道带宽，以 Hz 为单位 `1000` (默认) | 正标量

将相邻通道带宽指定为正标量，以 Hz 为单位。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`。

#### 程序化使用

请参阅 `AdjacentBW`。

### **Filter Shape** — 滤波器形状 `None` (默认) | `RRC` | `Gaussian`

将主通道和相邻通道的滤波器形状指定为 `None`、`RRC` 或 `Gaussian`。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`。

#### 程序化使用

请参阅 `FilterShape`。

### **Roll-off Factor** — 滚降因子 `0.5` (默认) | 范围 [`0`, `1`] 内的实数标量

将滚降因子指定为范围 [`0`, `1`] 内的实数标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`，并将 **Filter Shape** 设置为 `RRC`。

#### 程序化使用

请参阅 `FilterCoeff`。

### **BT Product** — BT 积 `0.5` (默认) | 范围 [`0`, `1`] 内的实数标量

将 BT 积指定为范围 [`0`, `1`] 内的实数标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `ACPR`，并将 **Filter Shape** 设置为 `Gaussian`。

#### 程序化使用

请参阅 `FilterCoeff`。

### 仅 Property Inspector

### **Channel Names** — 输入通道名称 `[]` (默认) | 字符向量 | 字符串 | 字符串或字符向量数组。

输入通道名称，指定为字符向量、字符串或数组。这些名称会出现在图例、**Settings** 和 **Measurements** 面板中。如果未指定名称，示波器会将通道标记为 `Channel 1`、`Channel 2` 等。

**示例：** ["A","B"]

#### 依赖关系

要查看通道名称，请在 **Scope** 选项卡中选择 **Legend**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ChannelNames` |
| **类型：** cell array of character vectors or string array |

### **Maximize Axes** — 最大化绘图大小 `Auto` (默认) | `Off` | `On`

- `Auto` — 如果未指定 **Title** 和 **Y-Label**，示波器会最大化所有绘图。
- `On` — 示波器最大化所有绘图，并隐藏 **Title** 和 **Y-label** 中的所有值。
- `Off` — 示波器不最大化绘图。

将鼠标悬停在 Spectrum Analyzer 上可看到最大化坐标轴按钮 。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaximizeAxes` |
| **类型：** character vector or string scalar |

### **Axes Scaling** — Y 轴缩放模式 `OnceAtStop` (默认) | `Manual` | `Auto` | `Updates`

- `OnceAtStop` — 仿真完成后缩放 *y* 轴。
- `Manual` — 使用 **Scale Y-axis Limits** 工具栏按钮手动缩放 *y* 轴范围。
- `Auto` — 在仿真期间和仿真之后缩放 *y* 轴范围。
- `Updates` — 在 Number of Updates 文本框中指定的时间步数（默认为 `100`）之后缩放 *y* 轴。每次运行仅缩放一次。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **模块参数：** `AxesScaling` |
| **类型：** character vector or string scalar |

### **Number of Updates** — 缩放前的更新次数 `100` (默认) | 整数

设置此属性以延迟自动缩放 y 轴。

**可调：** 是

#### 依赖关系

要启用此属性，请将 Axes Scaling 设置为 `Updates`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AxesScalingNumUpdates` |
| **类型：** character vector or string scalar |
| **值：** 标量 |

## 所属库

DSP System Toolbox / Sinks Audio Toolbox / Sinks DSP System Toolbox HDL Support / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可见性，但不会包含在生成的代码中。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。另请参阅 Generate HDL Code with Annotations or Comments (HDL Coder) 和 Integrate Custom HDL Code by Using DocBlock (HDL Coder)。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

此模块可用于生成 PLC 代码的系统中的仿真可见性，但不会包含在生成的代码中。

## 版本历史

**在 R2014b 中引入**

### R2025a：单独控制每条线的绘图类型

您现在可以单独控制每条线的绘图类型。要控制某条线的绘图类型，请选择该线并相应设置 **Plot Type** 参数。

### R2025a：Spectrum Analyzer 模块中的新相位噪声测量

您现在可以使用 Spectrum Analyzer 模块测量并绘制信号的相位噪声。

要启用 Spectrum Analyzer 窗口中的相位噪声测量，请点击示波器工具条上的 **Measurements** 选项卡，然后点击 **Phase Noise** 按钮。

**注意**

要访问相位噪声测量设置，您必须拥有有效的 Mixed-Signal Blockset 许可证。

### R2025a：支持运行平均方法

Spectrum Analyzer 模块现在支持运行平均方法来计算功率谱估计。要启用此模式，请将 **Estimation** 选项卡中的 **Averaging Method** 参数设置为 `Running`，并将 **Spectral Averages** 参数设置为正整数。

有关更多信息，请参阅 Algorithms 部分。

### R2024b：为任意数量的输入样本显示频谱数据并相应调整 RBW

以前，Spectrum Analyzer 模块对于给定 RBW 值需要最小样本数才能更新显示。从 R2024b 开始，此限制已移除。示波器现在可针对任意数量的输入样本更新其显示，并相应调整 RBW 值。

### R2024b：自动调整 RBW 以保持 1024 个样本

Spectrum Analyzer 模块现在可以自动调整分辨率带宽 (RBW)，以便无论选择哪种窗，都将每次频谱更新的样本数保持为 1024（*Nsamples* = 1024）。

要在 Spectrum Analyzer 模块中启用此模式，请设置：

- **Estimation Method** 为 `Welch`。
- **Resolution Method** 为 `RBW`。
- **RBW (Hz)** 为 `Auto`。

### R2024b：示波器 UI 中更高的显示精度

您现在可以使用示波器设置中 **Display and Labels** 下的 **Display Precision** 属性将显示精度提高到 15 位数字。此精度会影响示波器在其状态栏上显示的所有测量值和数据。

### R2024b：**Preserve Colors** 现在可在示波器工具条中使用

**Preserve colors for copy to clipboard** 属性已重命名为 **Preserve Colors**，现在可在 **Copy Display** 下的示波器工具条中使用。

### R2024a：**Analyzer** 选项卡已重命名为 **Scope** 选项卡

频谱分析仪中的 **Analyzer** 选项卡已重命名为 **Scope** 选项卡。

### R2024a：指定窗长度和 FFT 长度

您现在可以在某些条件下在频谱分析仪中指定窗长度和 FFT 长度。以下参数从 R2024a 开始可用：

- **Resolution Method**
- **Window Length**
- **FFT Length**

### R2023b：Spectrum Analyzer 支持 `dBuV` 单位

当您设置以下项时，可以将 **Spectrum Unit** 设置为 `dBuV`：

- **Input Domain** 为 `Time`，且 **Spectrum** 为 `RMS`。
- **Input Domain** 为 `Frequency`。

当您将 **Input Domain** 设置为 `Frequency` 时，可以将 **Input Unit** 设置为 `dBuV`。

### R2023a：Simulink 中响应性更好且具有工具条界面的 Spectrum Analyzer

在 R2023a 中，Spectrum Analyzer 模块响应性更好，其工具条界面经过改进，便于您访问频谱分析、估计和测量。您可以使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置并显示 Spectrum Analyzer 设置。

## 描述

显示频谱

Spectrum Analyzer 模块（此处称为示波器）显示频域信号以及时域信号的频谱。示波器显示频谱视图和频谱图视图。该模块算法使用滤波器组方法和平均修正周期图的 Welch 方法执行频谱估计。您可以自定义频谱分析仪显示，以显示所需的数据和测量信息。有关更多详细信息，请参阅 Algorithms。

Spectrum Analyzer 示波器快照，同时显示频谱和 Spectrogram。

您可以在以 `Normal` 或 `Accelerator` 仿真模式运行的模型中使用 Spectrum Analyzer 模块。您也可以在一定限制下在以 `Rapid Accelerator` 或 `External` 仿真模式运行的模型中使用 Spectrum Analyzer 模块。

您可以在所有子系统和条件子系统中使用 Spectrum Analyzer 模块。*条件子系统*包括使能子系统、触发子系统、使能和触发子系统以及函数调用子系统。有关更多信息，请参阅 Conditionally Executed Subsystems Overview (Simulink)。

### 测量

- 光标测量 — 使用垂直和水平光标测量信号值。
- 峰值查找测量 — 查找最大值并显示其出现的 *x* 轴值。
- 通道测量 — 测量占用带宽或相邻通道功率比 (ACPR)。
- 失真测量 — 测量谐波失真和互调失真。
- 频谱掩码 — 可视化频谱限制并将频谱值与规范值进行比较。

### 程序化控制

使用 `SpectrumAnalyzerBlockConfiguration` 对象从命令行配置并显示频谱分析仪设置。
