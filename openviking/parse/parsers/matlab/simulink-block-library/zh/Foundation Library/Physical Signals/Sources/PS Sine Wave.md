---
type: simulink-block
title: 'PS Sine Wave'
family: 'physical-signals'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'pssinewave'
documentation_source_path: 'ref/pssinewave.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Sine Wave

## 端口

### 输出

### **O** — 输出物理信号，类型由模块参数值和单位确定（物理信号）

输出物理信号。信号大小与 **Amplitude** 和 **Bias** 参数值的大小匹配。信号单位由 **Amplitude** 和 **Bias** 参数单位确定。

端口名称在模块图标中不可见，但你可以通过点击模块对话框的 **描述** 选项卡中的 **Source code** 链接，在底层源文件中看到此名称。

## 参数

### **Amplitude** — 正弦波幅值 `1 1`（默认） | scalar | vector | matrix

正弦波形的幅值。第一个编辑框表示参数值。你可以指定 scalar、vector 或 matrix。默认情况下，该值为 scalar，`1`。如果指定 vector 或 matrix，则 **Bias** 也必须为相同大小的 vector 或 matrix，或者为 scalar。

第二个组合框表示参数单位，它也决定输出信号的单位。默认情况下，单位为 `1`（无单位）。你可以从下拉列表中选择单位，或键入所需的单位名称，例如 `Pa`，或有效表达式，例如 `m^2`。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **Bias** — 添加到正弦波的常量 `0 1`（默认） | scalar | vector | matrix

正弦波形的偏置，即为生成输出而添加到正弦波的常量值。第一个编辑框表示参数值。你可以指定 scalar、vector 或 matrix。默认情况下，该值为 scalar，`0`。如果指定 vector 或 matrix，则 **Amplitude** 也必须为相同大小的 vector 或 matrix，或者为 scalar。

第二个组合框表示参数单位。指定的单位必须与 **Amplitude** 参数的单位可通约。默认情况下，单位为 `1`（无单位）。你可以从下拉列表中选择单位，或键入所需的单位名称，例如 `Pa`，或有效表达式，例如 `m^2`。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

### **Frequency specification** — 选择以 SI 单位还是角度单位指定频率 `Frequency (SI)`（默认） | `Angular`

选择是以 SI 系统单位（例如 Hz）还是角度单位（例如 rad/s）指定频率。底层模块方程会根据你的选择而变化，因为角度单位不需要 `2*pi` 转换因子。

### **Frequency (SI)** — 正弦波频率 `1 Hz`（默认） | scalar

正弦波的频率，以 SI 频率单位指定，例如 `Hz`、`kHz`、`MHz` 或 `GHz`。

#### 依赖关系

要启用此参数，请将 **Frequency specification** 设置为 `Frequency (SI)`。

### **Angular frequency** — 正弦波角频率 `1 rad/s`（默认） | scalar

正弦波的频率，以角频率单位指定，例如 `rad/s`、`deg/s` 或 `rpm`。

#### 依赖关系

要启用此参数，请将 **Frequency specification** 设置为 `Angular`。

### **Phase** — 正弦波相移 `0 rad`（默认） | scalar

正弦波的相移。

## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

生成正弦波物理信号，使用仿真时间作为时间源

PS Sine Wave 模块输出正弦波形，同时在如何指定正弦波频率方面提供灵活性。

在 SI 单位制中，频率的单位是赫兹（`Hz`），其定义为 `1/s`。但是，你也可以使用角速度单位，例如 `rad/s`、`deg/s` 和 `rpm`，来测量周期性过程的频率。这种方法与机械语境中将频率定义为每秒转数，或在电气语境中定义为每秒周期数是一致的，并且允许你在不需要 `2*pi` 转换因子的情况下编写与频率相关的方程。有关更多信息，请参阅角速度与频率的单位。

**Frequency specification** 参数让你选择指定正弦波频率的方法：

- 如果选择 `Frequency(SI)`，请以 `Hz` 或可直接转换为 Hz 的单位（例如 `kHz`、`MHz` 和 `GHz`）指定频率。此时底层模块方程为：

  O=amplitude⋅sin(2π⋅frequency\_si⋅time+phase)+bias

- 如果选择 `Angular`，请以 `rad/s`、`deg/s` 或 `rpm` 指定角频率。此时底层模块方程为：

  O=amplitude⋅sin(angular\_frequency⋅time+phase)+bias

其中

|  |  |
| --- | --- |
| *O* | 输出端口处的物理信号 |
| *amplitude* | **Amplitude** 参数值 |
| *frequency\_si* | **Frequency (SI)** 参数值 |
| *angular\_frequency* | **Angular frequency** 参数值 |
| *time* | 仿真时间 |
| *phase* | **Phase** 参数值 |
| *bias* | **Bias** 参数值 |

**Amplitude** 和 **Bias** 参数值决定输出信号是 scalar、vector 还是 matrix。如果其中一个参数是 vector 或 matrix，则另一个必须是相同大小的 vector 或 matrix，或者为 scalar。此时输出信号也是相同大小的 vector 或 matrix。

**Amplitude** 和 **Bias** 必须具有可通约的单位。输出端口处的单位由单位传播规则确定。如果这两个参数具有相同的单位，则输出信号单位也相同。如果参数单位不同，则输出信号的单位是与参数单位可通约的基本单位。有关更多信息，请参阅物理信号单位传播。
