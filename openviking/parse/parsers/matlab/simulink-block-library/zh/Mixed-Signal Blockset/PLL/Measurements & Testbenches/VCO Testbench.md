---
type: simulink-block
title: 'VCO Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Measurements & Testbenches'
documentation_page: 'vcotestbench'
documentation_source_path: 'ref/vcotestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# VCO Testbench

## 端口
```yaml
ports:
- name: from vco
  summary: 输入信号标量
  direction: input
  data_types: double
- name: to vco
  summary: 输出信号标量
  direction: output
  data_types: double
```

### 输入

### **from vco** — 输入信号标量

输入信号，来自 VCO DUT 的输出。根据所选的 **Measurement** 选项，该输入信号用于计算相位噪声指标，或 VCO 的电压灵敏度和自由运行频率。

**数据类型：** `double`
### 输出

### **to vco** — 输出信号标量

输出信号，向 VCO DUT 的输入提供控制电压激励。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Measurement
  summary: 要测量的目标指标 Phase noise（默认）| Kvco and Fo
  group: ''
- name: Set stop time
  summary: 将推荐的最小仿真停止时间设置为模型停止时间按钮
  group: ''
- name: Plot measurement
  summary: 绘制测量结果按钮
  group: ''
- name: Export measurement results
  summary: 导出测量结果按钮
  group: ''
- name: Control voltage (V)
  summary: VCO 控制电压 2（默认）| 标量
  group: 激励
- name: Range of control voltage (V)
  summary: VCO 控制电压范围 [2 7]（默认）| 二元素行向量
  group: 激励
- name: Autofill setup parameters
  summary: 自动计算相位噪声测量的设置参数按钮
  group: 设置
- name: Resolution bandwidth (Hz)
  summary: 可分辨的最小正频率 30e3（默认）| 实正标量
  group: 设置
- name: No. of spectral averages
  summary: 频谱平均次数 8（默认）| 正整型标量
  group: 设置
- name: Hold-off time (s)
  summary: 延迟测量分析以避免瞬态 0（默认）
  group: 设置
- name: Autofill target metric
  summary: 自动填充目标相位噪声指标按钮
  group: 目标指标
- name: 相位噪声频率偏移向量 (Hz)
  summary: 相位噪声频率偏移向量 [30e3 100e3 1e6 3e6 10e6]（默认）| 实值向量
  group: 目标指标
- name: 相位噪声向量 (dBc/Hz)
  summary: 相位噪声向量 [-45 -55 -65 -75 -100]（默认）| 实值向量
  group: 目标指标
```

### **Measurement** — 要测量的目标指标 `Phase noise`（默认）| `Kvco and Fo`

确定正在测量两个给定目标指标中的哪一个。

选择 `Phase noise` 表示希望测试平台测量相位噪声并将其与目标相位噪声曲线进行比较。

选择 `Kvco and Fo` 表示希望测试平台使用一系列控制电压计算电压灵敏度（*K*vco）和静态频率（*F*o）。

#### 编程使用

- 使用 `get_param(gcb,'MeasureOptions')` 查看当前的 **Measurement** 选项。
- 使用 `set_param(gcb,'MeasureOptions',value)` 将 **Measurement** 设置为特定选项。

### **Set stop time** — 将推荐的最小仿真停止时间设置为模型停止时间按钮

点击以将 VCO Testbench 模块报告的 **Recommended min. simulation stop time (s)** 设置为模型停止时间。

#### 依赖关系

仅当选择 `Phase noise` 作为 **Measurement** 选项时，此按钮才可用。

### **Plot measurement** — 绘制测量结果按钮

根据 **Measurement** 选项绘制相关的 VCO 指标。

在 **Measurement** 中选择 `Phase noise` 会绘制 VCO 的相位噪声曲线。

在 **Measurement** 中选择 `Kvco and Fo` 会绘制 VCO 特性和 *K*vco。

### **Export measurement results** — 导出测量结果按钮

根据 **Measurement** 选项将相关的 VCO 指标导出到 Excel 文件。

在 **Measurement** 中选择 `Phase noise` 会导出 VCO 的相位噪声曲线。

在 **Measurement** 中选择 `Kvco and Fo` 会导出 VCO 特性和 *K*vco。

### 激励

### **Control voltage (V)** — VCO 控制电压 `2`（默认）| 标量

由 VCO Testbench 提供的控制电压，以 V 为单位的标量表示。在 **Control Voltage (V)** 中指定的值通过 **to vco** 端口流向 VCO 的输入。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **Measurement** 选项。

#### 编程使用

- 使用 `get_param(gcb,'ControlVoltage')` 查看当前的 **Control Voltage (V)** 值。
- 使用 `set_param(gcb,'ControlVoltage',value)` 将 **Control Voltage (V)** 设置为特定值。

**数据类型：** `double`

### **Range of control voltage (V)** — VCO 控制电压范围 `[2 7]`（默认）| 二元素行向量

由 VCO Testbench 提供的控制电压，以 V 为单位的二元素行向量表示。此参数指定控制电压的最小值和最大值，用于生成十个控制电压值点（包括所提供的值）。这十个控制电压值被发送到 VCO 输入以测量 *K*vco 和 *F*o。

#### 依赖关系

要启用此参数，请选择 `Kvco and Fo` 作为 **Measurement** 选项。

#### 编程使用

- 使用 `get_param(gcb,'ControlVoltageRange')` 查看当前的 **Range of control voltage (V)** 值。
- 使用 `set_param(gcb,'ControlVoltage',value)` 将 **Range of control voltage (V)** 设置为特定值。

**数据类型：** `double`

### 设置

### **Autofill setup parameters** — 自动计算相位噪声测量的设置参数按钮

点击此按钮可自动填充用于相位噪声测量的设置参数（
**Resolution bandwidth (Hz)** 和 **No. of
spectral averages**）。

如果 DUT 是来自 Mixed-Signal Blockset 的 VCO，则 VCO Testbench 模块用于相位
噪声测量的 `dsp.SpectrumEstimator`
System object™ 会根据 VCO 规格自动计算设置参数。

#### 依赖项

- 仅当 VCO DUT 是来自
  Mixed-Signal Blockset 的 VCO 模块时，此按钮才有效。

- 仅当选择
  `Phase noise` 作为
  **Measurement** 选项时，此按钮才可用。

### **Resolution bandwidth (Hz)** — 可分辨的最小正频率 `30e3`（默认）| 实正标量

可分辨的最小正频率，指定为实
正标量。**Resolution bandwidth (Hz)**
用于确定使用 Welch 方法进行频谱分析时的窗长度。有关详细信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**Resolution bandwidth (Hz)** 应
小于或等于最低偏移频率值。

如果 DUT 是来自 Mixed-Signal Blockset 库的 VCO 模块，您可以使用 **Autofill setup
parameters** 按钮自动计算
**Resolution bandwidth (Hz)**。

#### 依赖项

要启用此参数，请选择 `Phase
noise` 作为 **Measurement**
选项。

#### 程序化使用

- 使用 `get_param(gcb,'ResBandwidth')` 查看
  当前 **Resolution bandwidth (Hz)**
  值。
- 使用
  `set_param(gcb,'ResBandwidth',value)` 将
  **Resolution bandwidth (Hz)** 设置为
  特定值。

**数据类型：** `double`

### **No. of spectral averages** — 频谱平均次数 `8`（默认）| 正整型标量

频谱平均次数，指定为正整型标量。
VCO Testbench 模块内的 Phase Noise Measurement 子系统所使用的 `dsp.SpectrumEstimator`
System object 通过对 **No. of spectral averages** 指定的次数
进行平均，来计算当前功率
谱或功率密度谱估计。

如果 DUT 是来自 Mixed-Signal Blockset 库的 VCO 模块，您可以使用 **Autofill setup
parameters** 按钮自动计算频谱
平均次数。

#### 依赖项

要启用此参数，请选择 `Phase
noise` 作为 **Measurement**
选项。

#### 程序化使用

- 使用 `get_param(gcb,'SpectralAverages')`
  查看当前 **No. of spectral
  averages** 值。
- 使用
  `set_param(gcb,'SpectralAverages',value)`
  将 **No. of spectral averages** 设置为
  特定值。

**数据类型：** `double`

### **Hold-off time (s)** — 延迟测量分析以避免瞬态 `0`（默认）

保持期，指定为非负标量，单位为 s。
**Hold-off time** 将测量分析延迟
指定的时间量，以避免因瞬态而
损坏仿真结果。

#### 程序化使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看
  当前 **Hold-off time (s)**
  值。
- 使用
  `set_param(gcb,'HoldOffTime',value)` 将
  **Hold-off time (s)** 设置为特定
  值。

### 目标指标

### **Autofill target metric** — 自动填充目标相位噪声指标按钮

点击此按钮可根据 VCO 规格自动填充目标相位噪声
指标。

#### 依赖项

- 仅当 VCO DUT 是
  来自 Mixed-Signal Blockset 的
  VCO 模块时，此按钮才会有效。
- 仅当选择
  `Phase noise` 作为
  **Measurement** 选项时，此按钮才可用。

### **相位噪声频率偏移向量 (Hz)** — 相位噪声频率偏移向量 `[30e3 100e3 1e6 3e6 10e6]`（默认）| 实值向量

从数据手册中收集的、相对于载波频率的相位噪声频率偏移，指定为以 Hz 为单位的实值向量。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，您可以使用 **Autofill target metric** 按钮自动将 VCO 相位噪声频率偏移向量值传输到 VCO Testbench。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **Measurement** 选项。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseNoiseFreqOffset')` 查看当前的 **相位噪声频率偏移向量 (Hz)** 值。
- 使用 `set_param(gcb,'PhaseNoiseFreqOffset',value)` 将 **相位噪声频率偏移向量 (Hz)** 设置为特定值。

**数据类型：** `double`

### **相位噪声向量 (dBc/Hz)** — 相位噪声向量 `[-45 -55 -65 -75 -100]`（默认）| 实值向量

在以指定频率偏移为中心、相对于载波的 1 Hz 带宽内的相位噪声功率，从数据手册中收集，指定为以 dBc/Hz 为单位的实值向量。**相位噪声向量 (dBc/Hz)** 的元素对应于 **相位噪声频率偏移向量 (Hz)** 中的相对元素。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，您可以使用 **Autofill target metric** 按钮自动将 VCO 相位噪声向量值传输到测试台。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **Measurement** 选项。

#### 程序化使用

- 使用 `get_param(gcb,'PhaseNoiseVector')` 查看当前的 **相位噪声向量 (dBc/Hz)** 值。
- 使用 `set_param(gcb,'PhaseNoiseVector',value)` 将 **相位噪声向量 (dBc/Hz)** 设置为特定值。
## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

通过测量相位噪声指标或 VCO 特性来验证压控振荡器 (VCO)

VCO Testbench 模块通过测量两个目标指标之一来验证被测 VCO 设备 (DUT)：相位噪声，或电压灵敏度和静态频率。您可以使用该测试台来验证您自己实现的 VCO，也可以使用 Mixed-Signal Blockset™ 中的 VCO 模块。

VCO Testbench 模块从 **Stimulus** 选项卡生成激励（控制电压）来驱动被测设备 (DUT)。用于验证 DUT 的设置参数在 **Setup** 选项卡中定义，目标验证指标在 **Target Metric** 选项卡中定义。

要利用自动填充参数选项充分发挥 VCO 测试台的功能，请在 Simulink® 模型中仅使用两个模块：VCO DUT 和 VCO Testbench。
