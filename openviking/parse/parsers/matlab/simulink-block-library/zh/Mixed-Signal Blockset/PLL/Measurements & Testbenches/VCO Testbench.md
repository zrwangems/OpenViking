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

### 输入

### **from vco** — 输入信号标量

输入信号，来自 VCO DUT 的输出。根据所选的 **测量** 选项，此输入信号用于计算相位噪声指标，或 VCO 的电压灵敏度和自由运行频率。

**数据类型：** `double`
### 输出

### **to vco** — 输出信号标量

输出信号，向 VCO DUT 的输入提供控制电压激励。

**数据类型：** `double`

## 参数

### **测量** — 要测量的目标指标 `Phase noise`（默认）| `Kvco and Fo`

确定正在测量两个给定目标指标中的哪一个。

如果希望测试平台测量相位噪声并将其与目标相位噪声曲线进行比较，请选择 `Phase noise`。

如果希望测试平台使用一系列控制电压计算电压灵敏度（*K*vco）和静态频率（*F*o），请选择 `Kvco and Fo`。

#### 编程使用

- 使用 `get_param(gcb,'MeasureOptions')` 查看当前 **测量** 选项。
- 使用 `set_param(gcb,'MeasureOptions',value)` 将 **测量** 设置为特定选项。

### **设置停止时间** — 将推荐的最小仿真停止时间设置为模型停止时间按钮

点击以将 VCO Testbench 模块报告的 **建议的最小仿真停止时间 (s)** 设置为模型停止时间。

#### 依赖关系

仅当选择 `Phase noise` 作为 **测量** 选项时，此按钮才可用。

### **绘制测量结果** — 绘制测量结果按钮

根据 **测量** 选项绘制相关的 VCO 指标。

在 **测量** 中选择 `Phase noise` 会绘制 VCO 的相位噪声曲线。

在 **测量** 中选择 `Kvco and Fo` 会绘制 VCO 特性和 *K*vco。

### **导出测量结果** — 导出测量结果按钮

根据 **测量** 选项将相关的 VCO 指标导出到 Excel 文件。

在 **测量** 中选择 `Phase noise` 会导出 VCO 的相位噪声曲线。

在 **测量** 中选择 `Kvco and Fo` 会导出 VCO 特性和 *K*vco。

### 激励

### **控制电压 (V)** — VCO 控制电压 `2`（默认）| 标量

VCO Testbench 提供的控制电压，以 V 为单位的标量表示。**控制电压 (V)** 中指定的值通过 **to vco** 端口流向 VCO 的输入。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'ControlVoltage')` 查看当前 **控制电压 (V)** 值。
- 使用 `set_param(gcb,'ControlVoltage',value)` 将 **控制电压 (V)** 设置为特定值。

**数据类型：** `double`

### **控制电压范围 (V)** — VCO 控制电压范围 `[2 7]`（默认）| 二元素行向量

VCO Testbench 提供的控制电压，以 V 为单位的二元素行向量表示。此参数指定控制电压的最小值和最大值，用于生成十个控制电压值点（包括提供的值）。这十个控制电压值被发送到 VCO 输入，以测量 *K*vco 和 *F*o。

#### 依赖关系

要启用此参数，请选择 `Kvco and Fo` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'ControlVoltageRange')` 查看当前 **控制电压范围 (V)** 值。
- 使用 `set_param(gcb,'ControlVoltage',value)` 将 **控制电压范围 (V)** 设置为特定值。

**数据类型：** `double`

### 设置

### **自动填充设置参数** — 自动计算相位噪声测量的设置参数按钮

点击此按钮可自动填充相位噪声测量的设置参数（**分辨率带宽 (Hz)** 和 **频谱平均次数**）。

如果 DUT 是 Mixed-Signal Blockset 中的 VCO，则 VCO Testbench 模块用于相位噪声测量的 `dsp.SpectrumEstimator` System object™ 会根据 VCO 规格自动计算设置参数。

#### 依赖关系

- 仅当 VCO DUT 是 Mixed-Signal Blockset 中的 VCO 模块时，此按钮才有效。

- 仅当选择 `Phase noise` 作为 **测量** 选项时，此按钮才可用。

### **分辨率带宽 (Hz)** — 可分辨的最小正频率 `30e3`（默认）| 正实数标量

可分辨的最小正频率，指定为正实数标量。**分辨率带宽 (Hz)** 用于确定使用 Welch 方法进行频谱分析的窗口长度。有关详细信息，请参阅 Welch's Method of Averaged Modified Periodograms。

通常，**分辨率带宽 (Hz)** 应小于或等于最低偏移频率值。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，则可以使用 **自动填充设置参数** 按钮自动计算 **分辨率带宽 (Hz)**。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'ResBandwidth')` 查看当前 **分辨率带宽 (Hz)** 值。
- 使用 `set_param(gcb,'ResBandwidth',value)` 将 **分辨率带宽 (Hz)** 设置为特定值。

**数据类型：** `double`

### **频谱平均次数** — 频谱平均次数 `8`（默认）| 正整数标量

频谱平均次数，指定为正整数标量。VCO Testbench 模块内的 Phase Noise Measurement 子系统使用的 `dsp.SpectrumEstimator` System object 通过对 **频谱平均次数** 指定的数量进行平均，计算当前功率谱或功率密度谱估计。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，则可以使用 **自动填充设置参数** 按钮自动计算频谱平均次数。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'SpectralAverages')` 查看当前 **频谱平均次数** 值。
- 使用 `set_param(gcb,'SpectralAverages',value)` 将 **频谱平均次数** 设置为特定值。

**数据类型：** `double`

### **抑制时间 (s)** — 延迟测量分析以避免瞬态 `0`（默认）

抑制期，指定为以 s 为单位的非负标量。**抑制时间** 将测量分析延迟指定的时间量，以避免瞬态导致仿真结果损坏。

#### 编程使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看当前 **抑制时间 (s)** 值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **抑制时间 (s)** 设置为特定值。

### 目标指标

### **自动填充目标指标** — 自动填充目标相位噪声指标按钮

点击此按钮可根据 VCO 规格自动填充目标相位噪声指标。

#### 依赖关系

- 仅当 VCO DUT 是 Mixed-Signal Blockset 中的 VCO 模块时，此按钮才有效。
- 仅当选择 `Phase noise` 作为 **测量** 选项时，此按钮才可用。

### **相位噪声频率偏移向量 (Hz)** — 相位噪声频率偏移向量 `[30e3 100e3 1e6 3e6 10e6]`（默认）| 实数值向量

从载波频率开始的相位噪声频率偏移，收集自数据手册，指定为以 Hz 为单位的实数值向量。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，则可以使用 **自动填充目标指标** 按钮将 VCO 的相位噪声频率偏移向量值自动传输到 VCO Testbench。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'PhaseNoiseFreqOffset')` 查看当前 **相位噪声频率偏移向量 (Hz)** 值。
- 使用 `set_param(gcb,'PhaseNoiseFreqOffset',value)` 将 **相位噪声频率偏移向量 (Hz)** 设置为特定值。

**数据类型：** `double`

### **相位噪声向量 (dBc/Hz)** — 相位噪声向量 `[-45 -55 -65 -75 -100]`（默认）| 实数值向量

在相对于载波的指定频率偏移处，1 Hz 带宽内的相位噪声功率，收集自数据手册，指定为以 dBc/Hz 为单位的实数值向量。**相位噪声向量 (dBc/Hz)** 的元素对应于 **相位噪声频率偏移向量 (Hz)** 中的相对元素。

如果 DUT 是 Mixed-Signal Blockset 库中的 VCO 模块，则可以使用 **自动填充目标指标** 按钮将 VCO 的相位噪声向量值自动传输到测试平台。

#### 依赖关系

要启用此参数，请选择 `Phase noise` 作为 **测量** 选项。

#### 编程使用

- 使用 `get_param(gcb,'PhaseNoiseVector')` 查看当前 **相位噪声向量 (dBc/Hz)** 值。
- 使用 `set_param(gcb,'PhaseNoiseVector',value)` 将 **相位噪声向量 (dBc/Hz)** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Measurements & Testbenches

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

通过测量相位噪声指标或 VCO 特性来验证压控振荡器 (VCO)

VCO Testbench 模块通过测量以下两个目标指标之一来验证 VCO 待测设备 (DUT)：相位噪声，或电压灵敏度和静态频率。您可以使用该测试平台验证自己实现的 VCO，也可以使用 Mixed-Signal Blockset™ 中的 VCO 模块。

VCO Testbench 模块从 **激励** 选项卡生成激励（控制电压）以驱动待测设备 (DUT)。用于验证 DUT 的设置参数在 **设置** 选项卡中定义，目标验证指标在 **目标指标** 选项卡中定义。

要充分利用 VCO 测试平台通过自动填充参数选项提供的功能，请在 Simulink® 模型中仅使用两个模块：VCO DUT 和 VCO Testbench。
