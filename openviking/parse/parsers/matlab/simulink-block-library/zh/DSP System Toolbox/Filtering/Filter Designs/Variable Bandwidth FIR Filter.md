---
type: simulink-block
title: 'Variable Bandwidth FIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'variablebandwidthfirfilter'
documentation_source_path: 'ref/variablebandwidthfirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Bandwidth FIR Filter

## 端口
```yaml
ports:
- name: x
  summary: 数据输入 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Fcut
  summary: 滤波器截止频率 正标量
  direction: input
  data_types: single | double
- name: Fc
  summary: 滤波器中心频率 正标量
  direction: input
  data_types: single | double
- name: BW
  summary: 滤波器带宽 正标量
  direction: input
  data_types: single | double
- name: Port_1
  summary: 滤波后的输出 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **x** — 数据输入 向量 | 矩阵

将数据输入指定为向量或矩阵。该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，则第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则该模块将其解释为单通道。

该模块接受可变大小输入信号，也就是说，您可以在仿真期间更改每个输入通道的大小，但不能更改通道数。

在选择以下参数之一之前，此端口未命名：

- **从输入端口指定截止频率**
- **从输入端口指定中心频率**
- **从输入端口指定带宽**

**数据类型：** `single` | `double`
**复数支持：** 是

### **Fcut** — 滤波器截止频率 正标量

将 FIR 滤波器的截止频率指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

#### 依赖关系

要启用此端口，请选择 **Specify cutoff frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Fc** — 滤波器中心频率 正标量

将 FIR 滤波器的中心频率指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

#### 依赖关系

要启用此端口，请选择 **Specify center frequency from input port** 参数。

**数据类型：** `single` | `double`

### **BW** — 滤波器带宽 正标量

将 FIR 滤波器的带宽指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

#### 依赖关系

要启用此端口，请选择 **Specify bandwidth from input port** 参数。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 滤波后的输出 向量 | 矩阵

滤波后的输出，以向量或矩阵形式返回。输出信号的大小、数据类型和复数性与输入信号匹配。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: FIR filter order
  summary: FIR 滤波器阶数 30（默认）| 正整数
  group: ''
- name: Filter type
  summary: 滤波器类型 Lowpass（默认）| Highpass | Bandpass | Bandstop
  group: ''
- name: Specify cutoff frequency from input port
  summary: 从输入端口指定截止频率 off（默认）| on
  group: ''
- name: Filter cutoff frequency
  summary: 滤波器截止频率 512（默认）| 正标量
  group: ''
- name: Specify center frequency from input port
  summary: 从输入端口指定中心频率 off（默认）| on
  group: ''
- name: Filter center frequency
  summary: 滤波器中心频率 44100/4（默认）| 正标量
  group: ''
- name: Specify bandwidth from input port
  summary: 从输入端口指定带宽 off（默认）| on
  group: ''
- name: Filter bandwidth
  summary: 滤波器带宽 7680（默认）| 正标量
  group: ''
- name: Window function
  summary: 窗函数 Hann（默认）| Hamming | Chebyshev | Kaiser
  group: ''
- name: Chebyshev window sidelobe attenuation (dB)
  summary: Chebyshev 窗旁瓣衰减 60（默认）| 正标量
  group: ''
- name: Kaiser window parameter
  summary: Kaiser 窗参数 0.5（默认）| 实标量
  group: ''
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: ''
- name: Input sample rate (Hz)
  summary: 输入采样率 44100（默认）| 正标量
  group: ''
- name: View Filter Response
  summary: 查看滤波器响应 按钮
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **FIR filter order** — FIR 滤波器阶数 `30`（默认）| 正整数

将 FIR 滤波器的阶数指定为正整数标量。

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

指定 FIR 滤波器的类型。您可以将此参数设置为：

- `Lowpass`
- `Highpass`
- `Bandpass`
- `Bandstop`

### **Specify cutoff frequency from input port** — 从输入端口指定截止频率 `off`（默认）| `on`

选中此复选框时，通过 **Fcut** 端口指定截止频率。清除此复选框时，在模块对话框中通过 **Filter cutoff frequency** 参数指定截止频率。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Lowpass` 或 `Highpass`。

### **Filter cutoff frequency** — 滤波器截止频率 512（默认）| 正标量

将 FIR 滤波器的截止频率指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 滤波器截止频率的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to 1)` —— 滤波器截止频率的值以归一化频率单位表示。该值必须是小于 `1.0` 的正标量。

*(自 R2023a 起)*

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Filter type** 设置为 `Lowpass` 或 `Highpass`。
- 清除 **Specify cutoff frequency from input port** 参数。

### **Specify center frequency from input port** — 从输入端口指定中心频率 `off`（默认）| `on`

选中此复选框时，通过 **Fc** 端口指定中心频率。清除此复选框时，在模块对话框中通过 **Filter center frequency** 参数指定中心频率。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Bandpass` 或 `Bandstop`。

### **Filter center frequency** — 滤波器中心频率 44100/4（默认）| 正标量

将 FIR 滤波器的中心频率指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 滤波器中心频率的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to 1)` —— 滤波器中心频率的值以归一化频率单位表示。该值必须是小于 `1.0` 的正标量。

*(自 R2023a 起)*

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Filter type** 设置为 `Bandpass` 或 `Bandstop`。
- 清除 **Specify center frequency from input port** 参数。

### **Specify bandwidth from input port** — 从输入端口指定带宽 `off`（默认）| `on`

选中此复选框时，通过 **BW** 端口指定滤波器带宽。清除此复选框时，在模块对话框中通过 **Filter bandwidth** 参数指定滤波器带宽。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Bandpass` 或 `Bandstop`。

### **Filter bandwidth** — 滤波器带宽 7680（默认）| 正标量

将 FIR 滤波器的带宽指定为以 Hz 或归一化频率单位表示的实正标量 *(自 R2023a 起)*。

如果将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 滤波器带宽的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to 1)` —— 滤波器带宽的值以归一化频率单位表示。该值必须是小于 `1.0` 的正标量。

*(自 R2023a 起)*

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Filter type** 设置为 `Bandpass` 或 `Bandstop`。
- 清除 **Specify bandwidth from input port** 参数。

### **Window function** — 窗函数 `Hann`（默认）| `Hamming` | `Chebyshev` | `Kaiser`

指定用于设计 FIR 滤波器的窗函数。您可以将此参数设置为：

- `Hann`
- `Hamming`
- `Chebyshev`
- `Kaiser`

### **Chebyshev window sidelobe attenuation (dB)** — Chebyshev 窗旁瓣衰减 60（默认）| 正标量

将 Chebyshev 窗的旁瓣衰减指定为实正标量。

#### 依赖关系

要启用此参数，请将 **Window function** 设置为 `Chebyshev`。

### **Kaiser window parameter** — Kaiser 窗参数 0.5（默认）| 实标量

将 Kaiser 窗参数指定为实标量。

#### 依赖关系

要启用此参数，请将 **Window function** 设置为 `Kaiser`。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2023a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定滤波器截止频率、中心频率和滤波器带宽。
- `Specify on dialog` —— 在模块对话框中通过 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 模块从输入信号继承采样率，即 *N* / *Ts*，其中 *N* 是输入信号的帧大小，*Ts* 是输入信号的采样时间。

### **Input sample rate (Hz)** — 输入采样率 44100（默认）| 正标量

将输入信号的采样率指定为以 Hz 表示的正标量。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*(自 R2023a 起)*

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮将打开滤波器可视化工具，并显示可变带宽 FIR 滤波器的幅值响应。该响应基于您在模块对话框中选择的参数。要在滤波器可视化工具运行时更新幅值响应，请修改对话框中的参数并点击 **Apply**。

您可以从可视化工具界面配置绘图设置和信号测量。

在滤波器可视化工具功能区的 **Scope** 选项卡上，**Configuration** 部分允许您修改绘图设置。在 **Measurements** 选项卡上，您可以测量信号统计量、放置数据光标，并显示所选信号的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参阅 Configure Filter Visualizer。

#### 依赖关系

要启用此按钮，请不要从输入端口指定任何滤波器规格。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Filtering / Filter Designs

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当输入信号的数据类型为 `single` 或 `double` 时，Variable Bandwidth FIR Filter 模块支持使用 Intel® AVX2 代码替换库进行 SIMD 代码生成。

SIMD 技术可显著提高生成代码的性能。有关更多信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2015a 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此变更，该模块默认使用 MATLAB 解释器进行仿真。

### R2023a：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，可以以归一化频率单位（0 到 1）指定滤波器截止频率、中心频率和滤波器带宽。

## 描述

设计可调带宽 FIR 滤波器

Variable Bandwidth FIR Filter 模块使用指定的 FIR 滤波器规格对输入信号的每个通道随时间进行滤波。该模块提供可调滤波器设计参数，使您能够在仿真运行时调整滤波器特性。

该模块根据模块对话框中指定的滤波器参数设计 FIR 滤波器。输出端口属性（如数据类型、复数性和维度）与输入端口属性相同。

该模块还支持 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
