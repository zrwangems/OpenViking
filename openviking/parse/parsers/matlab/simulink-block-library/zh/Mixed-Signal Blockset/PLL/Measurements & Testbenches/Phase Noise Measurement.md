---
type: simulink-block
title: 'Phase Noise Measurement'
family: 'pll'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'phasenoisemeasurement'
documentation_source_path: 'ref/phasenoisemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Noise Measurement

## 端口

### 输入

### **sig** — 输入信号标量

输入到 Phase Noise Measurement 模块的时域信号，指定为标量。

**数据类型：** `double`

## 参数

### **分辨率带宽 (Hz)** — 可分辨的最小正频率 `30e3`（默认） | 正实数标量

可分辨的最小正频率，指定为正实数标量。**分辨率带宽 (Hz)** 用于确定使用 Welch 方法进行频谱分析时的窗长度。有关详细信息，请参阅 Welch 平均修正周期图法。

通常，**分辨率带宽 (Hz)** 应小于最低偏移频率值。

#### 程序化使用

- 使用 `get_param(gcb,'ResBandwidth')` 查看 **分辨率带宽 (Hz)** 的当前值。
- 使用 `set_param(gcb,'ResBandwidth',value)` 将 **分辨率带宽 (Hz)** 设置为特定值。

### **频谱平均次数** — 频谱平均次数 `4`（默认） | 正整数标量

频谱平均次数，指定为正整数标量。Phase Noise Measurement 模块使用的 `dsp.SpectrumEstimator` System object™ 通过对 **频谱平均次数** 指定的次数求平均，来计算当前功率谱或功率密度谱估计。

#### 程序化使用

- 使用 `get_param(gcb,'SpectralAverages')` 查看 **频谱平均次数** 的当前值。
- 使用 `set_param(gcb,'SpectralAverages',value)` 将 **频谱平均次数** 设置为特定值。

### **保持关闭时间 (s)** — 延迟测量分析以避免瞬态 `0`（默认） | 实数非负标量

将测量分析延迟指定的时间量，以避免瞬态造成破坏，指定为以 s 为单位的实数非负标量。

#### 程序化使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **保持关闭时间 (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **保持关闭时间 (s)** 设置为特定值。

### **频率偏移向量 (Hz)** — 相对于基频计算相位噪声的频率点 `[30e3 100e3 1e6 3e6 10e6]`（默认） | 实数值向量

相对于基频的频率点，在这些频率点处计算相位噪声，指定为以 Hz 为单位的实数值向量。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseNoiseFreqOffset')` 查看 **频率偏移向量 (Hz)** 的当前值。
- 使用 `set_param(gcb,'PhaseNoiseFreqOffset',value)` 将 **频率偏移向量 (Hz)** 设置为特定值。

### **指定目标** — 指定目标相位噪声向量 off（默认） | on

为给定频率偏移向量指定目标相位噪声向量。默认情况下，此选项未选中

### **相位噪声向量 (dBc/Hz)** — 给定频率偏移向量的目标相位噪声曲线 `[-300 -300 -300 -300 -300]`（默认） | 实数值向量

给定频率偏移向量的目标相位噪声曲线，指定为以 dBc/Hz 为单位的实数值向量。**相位噪声向量 (dBc/Hz)** 是以相对于载波的指定频率偏移为中心、1 Hz 带宽内的相位噪声功率。

#### 依赖关系

要启用此参数，请选择 **指定目标** 参数。

#### 程序化使用

- 使用 `get_param(gcb,'TargetPhaseNoise')` 查看 **相位噪声向量 (dBc/Hz)** 的当前值。
- 使用 `set_param(gcb,'TargetPhaseNoise',value)` 将 **相位噪声向量 (dBc/Hz)** 设置为特定值。

### **设置停止时间** — 将推荐的最小仿真停止时间设置为模型停止时间的按钮

单击以将 Phase Noise Measurement 模块报告的 **推荐的最小仿真停止时间 (s)** 设置为模型停止时间。

### **绘制相位噪声** — 绘制输入信号相位噪声曲线的按钮

单击以绘制输入信号的测量相位噪声曲线。如果选择了 **指定目标** 选项，还会叠加目标相位噪声曲线。您可以在仿真期间随时绘制相位噪声曲线。

### **导出测量结果** — 仿真后导出测量结果的按钮

仿真完成后，单击以将测量结果导出到 Excel 电子表格 (XLS) 或导出为逗号分隔值 (CSV)。

## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

计算特定频率偏移向量处的相位噪声

Phase Noise Measurement 模块测量并绘制时域信号的相位噪声曲线。它还会在模块图标上显示指定频率偏移向量的相位噪声值。
