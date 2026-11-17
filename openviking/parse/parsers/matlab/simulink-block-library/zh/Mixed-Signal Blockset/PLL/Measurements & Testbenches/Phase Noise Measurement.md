---
type: simulink-block
title: 'Phase Noise Measurement'
family: 'msblks'
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
```yaml
ports:
- name: sig
  summary: 输入信号 标量
  direction: input
  data_types: double
```

### 输入

### **sig** — 输入信号 标量

输入到 Phase Noise Measurement 模块的输入时域信号，指定为标量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Resolution bandwidth (Hz)
  summary: 可分辨的最小正频率 30e3（默认）| 实正标量
  group: ''
- name: No. of spectral averages
  summary: 频谱平均次数 4（默认）| 正整型标量
  group: ''
- name: Hold off time (s)
  summary: 延迟测量分析以避免瞬态 0（默认）| 实非负标量
  group: ''
- name: Frequency offset vector (Hz)
  summary: 相对于基频计算相位噪声的频率点 [30e3 100e3 1e6 3e6 10e6]（默认）| 实值向量
  group: ''
- name: Specify target
  summary: 指定目标相位噪声向量 off（默认）| on
  group: ''
- name: Phase noise vector (dBc/Hz)
  summary: 给定频率偏移向量的目标相位噪声曲线 [-300 -300 -300 -300 -300]（默认）| 实值向量
  group: ''
- name: Set stop time
  summary: 将推荐的最小仿真停止时间设置为模型停止时间 按钮
  group: ''
- name: 绘制相位噪声
  summary: 绘制输入信号相位噪声曲线按钮
  group: ''
- name: 导出测量结果
  summary: 仿真后导出测量结果按钮
  group: ''
```

### **Resolution bandwidth (Hz)** — 可分辨的最小正频率 `30e3`（默认）| 实正标量

可分辨的最小正频率，指定为实正标量。**Resolution bandwidth (Hz)** 用于确定使用 Welch 方法进行频谱分析的窗长。有关详细信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**Resolution bandwidth (Hz)** 应小于最低偏移频率值。

#### 编程使用

- 使用 `get_param(gcb,'ResBandwidth')` 查看 **Resolution bandwidth (Hz)** 的当前值。
- 使用 `set_param(gcb,'ResBandwidth',value)` 将 **Resolution bandwidth (Hz)** 设置为特定值。

### **No. of spectral averages** — 频谱平均次数 `4`（默认）| 正整型标量

频谱平均次数，指定为正整型标量。Phase Noise Measurement 模块使用的 `dsp.SpectrumEstimator` System object™ 通过对 **No. of spectral averages** 指定的次数进行平均来计算当前功率谱或功率密度谱估计。

#### 编程使用

- 使用 `get_param(gcb,'SpectralAverages')` 查看 **No. of spectral averages** 的当前值。
- 使用 `set_param(gcb,'SpectralAverages',value)` 将 **No. of spectral averages** 设置为特定值。

### **Hold off time (s)** — 延迟测量分析以避免瞬态 `0`（默认）| 实非负标量

将测量分析延迟指定的时间量以避免瞬态污染，指定为以 s 为单位的实非负标量。

#### 编程使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **Hold off time (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **Hold off time (s)** 设置为特定值。

### **Frequency offset vector (Hz)** — 相对于基频计算相位噪声的频率点 `[30e3 100e3 1e6 3e6 10e6]`（默认）| 实值向量

相对于基频计算相位噪声的频率点，指定为以 Hz 为单位的实值向量。

#### 编程使用

- 使用 `get_param(gcb,'PhaseNoiseFreqOffset')` 查看 **Frequency offset vector (Hz)** 的当前值。
- 使用 `set_param(gcb,'PhaseNoiseFreqOffset',value)` 将 **Frequency offset vector (Hz)** 设置为特定值。

### **Specify target** — 指定目标相位噪声向量 off（默认）| on

为给定频率偏移向量指定目标相位噪声向量。默认情况下，此选项未选中

### **Phase noise vector (dBc/Hz)** — 给定频率偏移向量的目标相位噪声曲线 `[-300 -300 -300 -300 -300]`（默认）| 实值向量

给定频率偏移向量的目标相位噪声曲线，指定为以 dBc/Hz 为单位的实值向量。**Phase noise vector (dBc/Hz)** 是以相对于载波的指定频率偏移为中心的 1 Hz 带宽内的相位噪声功率。

#### 依赖关系

要启用此参数，请选择 **Specify target** 参数。

#### 编程使用

- 使用 `get_param(gcb,'TargetPhaseNoise')` 查看 **Phase noise vector (dBc/Hz)** 的当前值。
- 使用 `set_param(gcb,'TargetPhaseNoise',value)` 将 **Phase noise vector (dBc/Hz)** 设置为特定值。

### **Set stop time** — 将推荐的最小仿真停止时间设置为模型停止时间 按钮

点击以将 Phase Noise Measurement 模块报告的 **Recommended min. simulation stop time (s)** 设置为模型停止时间。

### **绘制相位噪声** — 绘制输入信号相位噪声曲线按钮

点击以绘制输入信号的实测相位噪声曲线。如果选择了 **指定目标** 选项，目标相位噪声曲线也会叠加显示。您可以在仿真过程中的任意时刻绘制相位噪声曲线。

### **导出测量结果** — 仿真后导出测量结果按钮

仿真完成后，点击可将测量结果导出为 Excel 电子表格 (XLS) 或逗号分隔值 (CSV) 文件。
## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

计算特定频率偏移向量处的相位噪声

Phase Noise Measurement 模块测量并绘制时域信号的相位噪声曲线。它还会在模块图标上显示指定频率偏移向量对应的相位噪声值。
