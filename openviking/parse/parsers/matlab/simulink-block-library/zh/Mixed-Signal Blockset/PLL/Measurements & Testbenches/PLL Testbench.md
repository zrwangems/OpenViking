---
type: simulink-block
title: 'PLL Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'plltestbench'
documentation_source_path: 'ref/plltestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# PLL Testbench

## 端口
```yaml
ports:
- name: from pll
  summary: 输入时钟信号标量
  direction: input
  data_types: double
- name: to pll
  summary: 输出时钟信号标量
  direction: output
  data_types: double
```

### 输入

### **from pll** — 输入时钟信号标量

PLL Testbench 的输入时钟信号，指定为标量。**from pll** 端口连接到 PLL 系统的输出。

**数据类型：** `double`
### 输出

### **to pll** — 输出时钟信号标量

输出时钟信号，根据 **Signal type** 参数指定为正弦波或方波返回。**to pll** 端口处的信号为 PLL 系统提供激励。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Set stop time
  summary: 将推荐的最小仿真停止时间设为模型停止时间 按钮
  group: ''
- name: Plot phase noise profile
  summary: 绘制 PLL DUT 的相位噪声曲线 按钮
  group: ''
- name: Export measurement results
  summary: 仿真后导出测量结果 按钮
  group: ''
- name: Amplitude (V)
  summary: PLL 输入处激励信号的最大值 1（默认）| 实正标量
  group: 激励
- name: Frequency (Hz)
  summary: PLL 输入处激励信号的频率 30e6（默认）| 实正标量
  group: 激励
- name: Add phase noise
  summary: 添加相位噪声作为频率的函数 off（默认）| on
  group: 激励
- name: Phase noise frequency offset (Hz)
  summary: 相位噪声相对于载波频率的频率偏移 [500 1e3 10e3 100e3]（默认）| 实值向量
  group: 激励
  block_parameter: Foffset
  type: 字符向量
  values: 实值向量
- name: Phase noise level (dBc/Hz)
  summary: 指定频率偏移处相对于载波的相位噪声功率 [-115 -122 -142 -161]（默认）| 实值向量
  group: 激励
  block_parameter: PhaseNoise
  type: 字符向量
  values: 实值向量
- name: Estimate phase noise parameters
  summary: 自动估计相位噪声参数 on（默认）| off
  group: 激励
- name: Period jitter (S)
  summary: 周期抖动的标准差 4.8666e-15（默认）| 正实数标量
  group: 激励
  block_parameter: PeriodJitter
  type: 字符向量
  values: 正实数标量
  default: '4.8666e-15'
- name: Flicker corner frequency (Hz)
  summary: 闪烁噪声的转角频率 517103.8168（默认）| 标量
  group: 激励
  block_parameter: CornerFrequency
  type: 字符向量
  values: 标量
  default: '517103.8168'
- name: Plot fit
  summary: 绘制指定和期望的输出相位噪声密度 按钮
  group: 激励
- name: Frequency of operation
  summary: 测量 PLL DUT 的工作频率 on（默认）| off
  group: 设置
- name: Lock time
  summary: 测量 PLL DUT 的锁定时间 off（默认）| on
  group: 设置
- name: Target frequency of operation (Hz)
  summary: 用于计算锁定时间的 PLL DUT 目标工作频率 2.1e9（默认）| 实正标量
  group: 设置
- name: Error tolerance (Hz)
  summary: 锁定时间测量的误差容限 1e6（默认）| 实正标量
  group: 设置
- name: Phase noise
  summary: 测量 PLL DUT 的相位噪声水平 off（默认）| on
  group: 设置
- name: Resolution bandwidth (Hz)
  summary: 可分辨的最小正频率 200e3（默认）| 实正标量
  group: 设置
- name: No. of spectral averages
  summary: 频谱平均次数 4（默认）| 正整数标量
  group: 设置
- name: Hold off time (s)
  summary: 延迟测量分析以避免瞬态 0（默认）| 实非负标量
  group: 设置
- name: Frequency offset vector (Hz)
  summary: 相对于基频计算相位噪声的频率点 [300e3 1e6 3e6 10e6]（默认）| 实值向量
  group: 设置
- name: Frequency of operation
  summary: PLL 需要锁定的目标工作频率 2.1e9（默认）| 实正标量
  group: 目标指标
- name: Lock time (s)
  summary: PLL DUT 需要锁定的最大时间 3e-6（默认）| 实非负标量
  group: 目标指标
- name: 相位噪声 (dBc/Hz)
  summary: 与频率偏移向量 [-85,-125,-150,-180]（默认）对应的目标噪声功率 | 实值向量
  group: 目标指标
```

### **Set stop time** — 将推荐的最小仿真停止时间设为模型停止时间 按钮

点击以将 PLL Testbench 模块报告的 **Recommended min. simulation stop time (s)** 设置为模型停止时间。

#### 依赖关系

此按钮仅在 **Setup** 选项卡中选择了 **Phase noise** 测量选项时可用。

### **Plot phase noise profile** — 绘制 PLL DUT 的相位噪声曲线 按钮

点击以绘制 PLL 设备（DUT）的相位噪声曲线，并在仿真完成后将其与用户定义的相位噪声曲线进行比较。

#### 依赖关系

此按钮仅在 **Setup** 选项卡中选择了 **Phase noise** 测量选项时可用。

### **Export measurement results** — 仿真后导出测量结果 按钮

点击以在仿真完成后将测量结果导出为 Excel 电子表格（XLS）或逗号分隔值（CSV）。

### 激励

### **Amplitude (V)** — PLL 输入处激励信号的最大值 `1`（默认）| 实正标量

PLL 输入处激励信号的最大值，指定为实正标量。

#### 编程用法

- 使用 `get_param(gcb,'InputAmplitude')` 查看 **Amplitude (V)** 的当前值。
- 使用 `set_param(gcb,'InputAmplitude',value)` 将 **Amplitude (V)** 设置为特定值。

### **Frequency (Hz)** — PLL 输入处激励信号的频率 `30e6`（默认）| 实正标量

PLL 输入处激励信号的频率，指定为实正标量。

#### 编程用法

- 使用 `get_param(gcb,'Fo')` 查看 **Frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'Fo',value)` 将 **Frequency (Hz)** 设置为特定值。

### **Add phase noise** — 添加相位噪声作为频率的函数 off（默认）| on

选择以引入相位噪声作为频率的函数。默认情况下，此选项未选中。

### **Phase noise frequency offset (Hz)** — 相位噪声相对于载波频率的频率偏移 `[500 1e3 10e3 100e3]`（默认）| 实值向量

相位噪声相对于载波频率的频率偏移，指定为以 Hz 为单位的实值向量。

#### 依赖关系

要启用此参数，请在 **Stimulus** 选项卡中选择 **Add phase noise**。

#### 编程用法

|  |
| --- |
| **模块参数：** `Foffset` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[500 1e3 10e3 100e3]` |

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — 指定频率偏移处相对于载波的相位噪声功率 `[-115 -122 -142 -161]`（默认）| 实值向量

实值向量，指定以指定频率偏移为中心、相对于载波的 1 Hz 带宽内的相位噪声功率。该值以 dBc/Hz 为单位指定。

#### 依赖关系

要启用此参数，请在 **Stimulus** 选项卡中选择 **Add phase noise**。

#### 编程用法

|  |
| --- |
| **模块参数：** `PhaseNoise` |
| **类型：** 字符向量 |
| **值：** 实值向量 |
| **默认：** `[-115 -122 -142 -161]` |

**数据类型：** `double`

### **Estimate phase noise parameters** — 自动估计相位噪声参数 on（默认）| off

选择以自动估计相位噪声参数。默认情况下，此选项已选中。

您可以取消选择此选项以定义自定义周期抖动和闪烁拐角频率。

#### 依赖关系

要启用此参数，请在 **Stimulus** 选项卡中选择 **Add phase noise**。

**数据类型：** `double`

### **Period jitter (S)** — 周期抖动的标准差 `4.8666e-15`（默认）| 正实数标量

周期抖动的标准差，指定为以秒为单位的正实数标量。周期抖动是时钟信号的周期时间相对于理想周期的偏差。

要启用此参数，请在 **Stimulus** 选项卡中选择 **Add phase noise** 并取消选择 **Estimate phase noise parameters**。

#### 编程使用

|  |
| --- |
| **模块参数：** `PeriodJitter` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `4.8666e-15` |

**数据类型：** `double`

### **Flicker corner frequency (Hz)** — 闪烁噪声的转角频率 `517103.8168`（默认）| 标量

闪烁噪声的转角频率，指定为以赫兹为单位的标量。**Flicker corner frequency (Hz)** 定义为由于闪烁噪声导致相位噪声从 1/*f*2 过渡到 1/*f*3 的频率。在该频率处，周期抖动和闪烁噪声的频谱密度相等。

#### 依赖关系

要启用此参数，请在 **Stimulus** 选项卡中选择 **Add phase noise** 并取消选择 **Estimate phase noise parameters**。

#### 编程使用

|  |
| --- |
| **模块参数：** `CornerFrequency` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认值：** `517103.8168` |

**数据类型：** `double`

### **Plot fit** — 绘制指定和期望的输出相位噪声密度 按钮

点击以绘制指定的相位噪声密度和可实现的期望输出相位噪声密度。

### 设置

### **Frequency of operation** — 测量 PLL DUT 的工作频率 on（默认）| off

选择以测量 PLL DUT 的工作频率。默认情况下，此选项处于选中状态。

### **Lock time** — 测量 PLL DUT 的锁定时间 off（默认）| on

选择以使用用户指定的误差容限测量 PLL DUT 的锁定时间。默认情况下，此选项处于取消选中状态。

### **Target frequency of operation (Hz)** — 用于计算锁定时间的 PLL DUT 目标工作频率 `2.1e9`（默认）| 实正标量

用于计算 PLL 锁定时间的 PLL DUT 目标工作频率，指定为以 Hz 为单位的实正标量。

#### 依赖关系

要启用此参数，请在 **Setup** 选项卡中选择 **Lock time** 测量选项。

#### 编程使用

- 使用 `get_param(gcb,'ExpectedFreq')` 查看 **Target frequency of operation(Hz)** 的当前值。
- 使用 `set_param(gcb,'ExpectedFreq',value)` 将 **Target frequency of operation (Hz)** 设置为特定值。

### **Error tolerance (Hz)** — 锁定时间测量的误差容限 `1e6`（默认）| 实正标量

锁定时间测量的误差容限，指定为以 Hz 为单位的实正标量。

#### 依赖关系

要启用此参数，请在 **Setup** 选项卡中选择 **Lock time** 测量选项。

#### 编程使用

- 使用 `get_param(gcb,'FreqErrorTol')` 查看 **Error tolerance (Hz)** 的当前值。
- 使用 `set_param(gcb,'FreqErrorTol',value)` 将 **Error tolerance (Hz)** 设置为特定值。

### **Phase noise** — 测量 PLL DUT 的相位噪声水平 off（默认）| on

选择以在用户定义的频率偏移点处测量 PLL DUT 的相位噪声水平。默认情况下，此选项处于取消选中状态。

### **Resolution bandwidth (Hz)** — 可分辨的最小正频率 `200e3`（默认）| 实正标量

可分辨的最小正频率，指定为实正标量。**Resolution bandwidth (Hz)** 用于确定使用 Welch 方法进行频谱分析的窗口长度。有关详细信息，请参阅 Welch 平均修正周期图方法。

通常，**Resolution bandwidth (Hz)** 应小于或等于最低偏移频率值。

#### 依赖项

要启用此参数，请在 **Setup** 选项卡中选择 **Phase noise** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'ResBandwidth')` 查看 **Resolution bandwidth (Hz)** 的当前值。
- 使用 `set_param(gcb,'ResBandwidth',value)` 将 **Resolution bandwidth (Hz)** 设置为特定值。

### **No. of spectral averages** — 频谱平均次数 `4`（默认）| 正整数标量

频谱平均次数，指定为正整数标量。PLL Testbench 模块内部的 Phase Noise Measurement 子系统所使用的 `dsp.SpectrumEstimator` System object™ 通过对 **No. of spectral averages** 指定的次数进行平均来计算当前功率谱或功率密度谱估计。

#### 依赖项

要启用此参数，请在 **Setup** 选项卡中选择 **Phase noise** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'SpectralAverages')` 查看 **No. of spectral averages** 的当前值。
- 使用 `set_param(gcb,'SpectralAverages',value)` 将 **No. of spectral averages** 设置为特定值。

### **Hold off time (s)** — 延迟测量分析以避免瞬态 `0`（默认）| 实非负标量

将测量分析延迟指定的时间量以避免瞬态干扰，指定为以 s 为单位的实非负标量。

要启用此参数，请在 **Setup** 选项卡中选择 **Phase noise** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **Hold off time (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **Hold off time (s)** 设置为特定值。

### **Frequency offset vector (Hz)** — 相对于基频计算相位噪声的频率点 `[300e3 1e6 3e6 10e6]`（默认）| 实值向量

相对于基频计算相位噪声的频率点，指定为以 Hz 为单位的实值向量。这些值也会在 **Target Metrics** 选项卡中报告为 **Phase noise frequency offset (Hz)**。

要启用此参数，请在 **Setup** 选项卡中选择 **Phase noise** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'PhaseNoiseFreqOffset')` 查看 **Frequency offset vector (Hz)** 的当前值。
- 使用 `set_param(gcb,'PhaseNoiseFreqOffset',value)` 将 **Frequency offset vector (Hz)** 设置为特定值。

### 目标指标

### **Frequency of operation** — PLL 需要锁定的目标工作频率 `2.1e9`（默认）| 实正标量

PLL DUT 需要锁定的目标工作频率，指定为以 Hz 为单位的实正标量。

如果选择 **Lock time** 作为测量选项，则 **Frequency of operation** 从 **Target frequency of operation (Hz)** 参数报告。

#### 依赖项

要启用此参数，请在 **Setup** 选项卡中选择 **Frequency of operation** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'TargetFreq')` 查看 **Frequency of operation** 的当前值。
- 使用 `set_param(gcb,'TargetFreq',value)` 将 **Frequency of operation** 设置为特定值。

### **Lock time (s)** — PLL DUT 需要锁定的最大时间 `3e-6`（默认）| 实非负标量

PLL DUT 需要锁定的最大时间，指定为以 s 为单位的实非负标量。

#### 依赖项

要启用此参数，请在 **Setup** 选项卡中选择 **Lock time** 测量选项。

#### 编程用法

- 使用 `get_param(gcb,'TargetLockTime')` 查看 **Lock time** 的当前值。
- 使用 `set_param(gcb,'TargetLockTime',value)` 将 **Lock time** 设置为特定值。

### **相位噪声 (dBc/Hz)** — 与频率偏移向量 `[-85,-125,-150,-180]`（默认）对应的目标噪声功率 | 实值向量

以 **频率偏移向量 (Hz)** 参数指定的频率为中心、1 Hz 频率带宽内相对于载波的目标噪声功率电平，指定为以 dBc/Hz 为单位的实值向量。

#### 依赖关系

要启用此参数，请在 **Setup** 选项卡中选择 **Phase noise** 测量选项。

#### 程序化使用

- 使用 `get_param(gcb,'TargetPhaseNoiseVector')` 查看 **Phase noise** 的当前值。
- 使用 `set_param(gcb,'TargetPhaseNoiseVector',value)` 将 **Phase noise** 设置为特定值。
## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

通过测量工作频率、锁定时间和相位噪声来验证 PLL 系统

PLL Testbench 模块以时钟信号的形式向锁相环 (PLL) 系统提供输入激励。该测试台还通过将工作频率、锁定时间和相位噪声与目标指标进行比较来验证 PLL 系统的性能。

PLL Testbench 模块从 **Stimulus** 选项卡生成用于驱动被测设备 (DUT) 的激励。用于验证 DUT 的设置参数在 **Setup** 选项卡中定义，目标验证指标在 **Target Metric** 选项卡中定义。
