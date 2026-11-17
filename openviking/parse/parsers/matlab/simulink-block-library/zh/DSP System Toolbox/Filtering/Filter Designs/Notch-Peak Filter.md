---
type: simulink-block
title: 'Notch-Peak Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'notchpeakfilter'
documentation_source_path: 'ref/notchpeakfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Notch-Peak Filter

## 端口
```yaml
ports:
- name: Input
  summary: 输入信号 向量 | 矩阵
  direction: input
  data_types: single | double
- name: notch
  summary: 陷波滤波器输出 向量 | 矩阵
  direction: output
  data_types: single | double
- name: peak
  summary: 峰值滤波器输出 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。输入信号的每一列被视为一个单独通道。如果输入是二维信号，则第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则将其解释为单通道。

此模块支持可变大小输入，使您能够在仿真期间更改通道长度。要启用可变大小输入，请清除 **Inherit sample rate from input** 复选框。通道数必须保持不变。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **notch** — 陷波滤波器输出 向量 | 矩阵

陷波滤波器输出，以向量或矩阵形式返回。

**数据类型：** `single` | `double`
**复数支持：** 是

### **peak** — 峰值滤波器输出 向量 | 矩阵

峰值滤波器输出，以向量或矩阵形式返回。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter specification
  summary: 滤波器设计规格 Bandwidth and center frequency（默认）| Coefficients | Quality factor and center frequency
  group: ''
- name: Specify bandwidth from input port
  summary: 从输入端口指定 3 dB 带宽的选项 off（默认）| on
  group: ''
- name: 3 dB bandwidth
  summary: 3-dB 带宽 2205（默认）| 正标量
  group: ''
- name: Specify center frequency from input port
  summary: 从输入端口指定中心频率的选项 off（默认）| on
  group: ''
- name: Center frequency of notch or peak
  summary: 陷波或峰值中心频率 11025（默认）| 正标量
  group: ''
- name: Specify bandwidth coefficient from input port
  summary: 从输入端口指定带宽系数的选项 off（默认）| on
  group: ''
- name: Bandwidth coefficient
  summary: 带宽系数 0.72654（默认）| 范围 [−1 1] 内的实标量
  group: ''
- name: Specify center frequency coefficient from input port
  summary: 从输入端口指定中心频率系数的选项 off（默认）| on
  group: ''
- name: Center frequency coefficient
  summary: 中心频率系数 0（默认）| 范围 [−1 1] 内的实标量
  group: ''
- name: Specify quality factor from input port
  summary: 从输入端口指定品质因数的选项 off（默认）| on
  group: ''
- name: Quality factor
  summary: 陷波或峰值滤波器的品质因数 5（默认）| 正标量
  group: ''
- name: Filter output
  summary: 输出的滤波器响应 Notch and Peak（默认）| Notch | Peak
  group: ''
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: ''
- name: Input sample rate (Hz)
  summary: 输入的采样率 44100（默认）| 正标量
  group: ''
- name: View Filter Response
  summary: 查看滤波器响应按钮（默认）
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Filter specification** — 滤波器设计规格 `Bandwidth and center frequency`（默认）| `Coefficients` | `Quality factor and center frequency`

指定模块用于设计滤波器的参数或系数：

- `Bandwidth and center frequency`
  （默认）— 使用 **3 dB
  bandwidth** 和 **Center frequency of notch
  or peak** 设计滤波器。
- `Coefficients` — 使用
  **Bandwidth coefficient** 和
  **Center frequency coefficient** 设计滤波器。
- `Quality factor and center frequency`
  — 使用 **Quality
  factor** 和 **Center frequency of notch or
  peak** 设计滤波器。

### **Specify bandwidth from input port** — 从输入端口指定 3 dB 带宽的选项 `off`（默认）| `on`

当您选中此复选框时，3 dB 带宽通过
**BW** 端口输入。当您清除此复选框时，3 dB
带宽通过 **3 dB
bandwidth** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Bandwidth and center
frequency`。

### **3 dB bandwidth** — 3-dB 带宽 `2205`（默认）| 正标量

将滤波器的 3-dB 带宽指定为正标量，单位为 Hz
或归一化频率
单位 *(自 R2024a 起)*。

如果您将 **Sample rate
mode** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` —— 3-dB 带宽
  的值以 Hz 为单位，且必须小于输入信号采样率
  的一半。
- `Use normalized frequency (0 to 1)`
  —— 3-dB 带宽的值以归一化频率
  单位表示。该值必须是小于
  `1.0` 的正标量。

*(自 R2024a 起)*

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Bandwidth and center
frequency`，并清除 **Specify bandwidth
from input port** 参数。

### **Specify center frequency from input port** — 从输入端口指定中心频率的选项 `off`（默认）| `on`

当您选中此复选框时，中心频率通过
**Fc** 端口输入。当您清除此复选框时，中心
频率通过 **Center
frequency of notch or peak** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Bandwidth and center
frequency` 或 `Quality factor and center
frequency`。

### **Center frequency of notch or peak** — 陷波或峰值中心频率 `11025`（默认）| 正标量

将滤波器陷波和峰值的中心频率指定为正数值
标量，单位为 Hz 或归一化频率
单位 *(自 R2024a 起)*。

如果您将 **Sample rate
mode** 参数设置为：

- `Specify on dialog` 或
  `Inherit from input port` —— 中心频率
  的值以 Hz 为单位，且必须小于输入信号采样率
  的一半。
- `Use normalized frequency (0 to 1)`
  —— 中心频率的值以归一化频率
  单位表示。该值必须是小于
  `1.0` 的正标量。

*(自 R2024a 起)*

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Bandwidth and center
frequency` 或 `Quality factor and center
frequency`，并清除 **Specify center
frequency from input port** 参数。

### **Specify bandwidth coefficient from input port** — 从输入端口指定带宽系数的选项 `off`（默认）| `on`

当您选中此复选框时，带宽系数通过
端口 **BWCoeff** 输入。当您清除此复选框时，
带宽系数通过
**Bandwidth coefficient** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为
`Coefficients`。

### **Bandwidth coefficient** — 带宽系数 `0.72654`（默认）| 范围 [−`1` `1`] 内的实标量

将决定滤波器 3 dB 带宽的系数指定为
范围 [−`1`
`1`] 内的有限数值标量。

- `-1` 对应最大 3 dB
  带宽（输入信号采样率的四分之一）。
- `1` 对应最小带宽（0
  Hz，即全通滤波器）。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Coefficients`
并清除 **Specify bandwidth coefficient from input
port** 参数。

### **Specify center frequency coefficient from input port** — 从输入端口指定中心频率系数的选项 `off`（默认）| `on`

当您选中此复选框时，中心频率系数通过
**FcCoeff** 端口输入。当您清除此复选框时，
中心频率系数通过 **Center frequency coefficient**
参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为
`Coefficients`。

### **Center frequency coefficient** — 中心频率系数 `0`（默认）| 范围 [−`1` `1`] 内的实标量

将决定滤波器中心频率的系数指定为
范围 [−`1`
`1`] 内的有限数值标量。

- `-1` 对应最小中心
  频率（`0` Hz）。
- `1` 对应最大中心
  频率（输入信号采样率的一半）。

默认值 `0` 对应输入信号采样率的四分之一。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Coefficients`
并清除 **Specify center frequency coefficient from input
port** 参数。

### **Specify quality factor from input port** — 从输入端口指定品质因数的选项 `off`（默认）| `on`

当您选中此复选框时，品质因数通过
**Q** 端口输入。当您清除此复选框时，品质
因数通过 **Quality
factor** 参数在模块对话框中指定。

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Quality factor and center
frequency`。

### **Quality factor** — 陷波或峰值滤波器的品质因数 `5`（默认）| 正标量

将陷波和峰值滤波器的品质因数指定为实正标量。
品质因数定义为 **Center frequency of notch or
peak** / **3 dB bandwidth**。较高的品质
因数对应较窄的峰值或凹陷。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Filter
specification** 设置为 `Quality factor and center
frequency` 并清除 **Specify quality
factor from input port** 参数。

### **Filter output** — 输出的滤波器响应 `Notch and Peak`（默认）| `Notch` | `Peak`

将输出的响应指定为以下之一：

- `Notch and Peak` — 模块
  输出滤波器的陷波和峰值响应。
- `Notch` — 模块输出
  滤波器的陷波响应。
- `Peak` — 模块输出
  滤波器的峰值响应。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2024a 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)`
  —— 以归一化频率单位（0 到 1）指定通带边缘和阻带边缘
  频率。
- `Specify on dialog` —— 在模块对话框中通过
  **Input sample rate (Hz)**
  参数指定输入采样率。
- `Inherit from input port` ——
  模块从输入信号继承采样率。模块
  按 *N*/*Ts* 计算采样率，其中
  *N* 是输入信号的帧大小，
  *Ts* 是输入信号的采样时间。

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| 正标量

将输入信号的采样率指定为正标量
值。

#### 依赖关系

要启用此参数，请设置：

- **Filter specification** 为除
  `Coefficients` 之外的任何可接受
  值。
- **Sample
  rate mode** 为 `Specify on
  dialog`。*(自 R2024a 起)*

### **View Filter Response** — 查看滤波器响应按钮（默认）

点击此按钮将打开滤波器可视化工具，并显示陷波-峰值滤波器的幅值响应。该响应基于您在
模块对话框中选择的参数。要在可视化工具
运行时更新响应，请修改对话框中的参数并点击
**Apply**。

您可以从可视化工具的界面配置绘图设置和频率响应
测量。

在 **Scope** 选项卡上，您可以启用图例、指定同时绘制滤波器的幅值和相位响应、修改绘图设置、
生成用于重新创建绘图的脚本，甚至保存或共享
设置。在 **Measurements** 选项卡上，您可以启用数据
光标，并显示滤波器响应的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参阅
Configure Filter Visualizer。

#### 依赖关系

要启用此按钮，请勿从
输入端口指定任何滤波器规格。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用
  MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，该 C 代码将在
  后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续
  仿真。
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

## 版本历史

**在 R2015a 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为
`Interpreted execution`。通过此更改，模块默认使用
MATLAB 解释器进行仿真。

### R2023b：支持归一化频率

当您将 **Sample rate mode** 参数设置为
`Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到
1）指定 3 dB 带宽和中心频率。

## 描述

设计二阶可调陷波和峰值 IIR 滤波器

Notch-Peak Filter 模块使用指定的中心频率和 3 dB 带宽对输入信号的每个通道
随时间进行滤波。此模块提供
可调滤波器设计参数，使您能够在仿真运行时调整滤波器特性。
该模块根据模块对话框中设置的滤波器
参数设计滤波器。输出端口属性（如数据类型、
复数性和维度）与输入端口属性相同。
