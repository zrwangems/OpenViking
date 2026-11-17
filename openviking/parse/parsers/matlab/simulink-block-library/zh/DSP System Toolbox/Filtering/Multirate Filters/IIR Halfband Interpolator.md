---
type: simulink-block
title: 'IIR Halfband Interpolator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'iirhalfbandinterpolator'
documentation_source_path: 'ref/iirhalfbandinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# IIR Halfband Interpolator

## 端口
```yaml
ports:
- name: LP
  summary: 数据输入 列向量 | 矩阵
  direction: input
  data_types: single | double
- name: HP
  summary: 合成滤波器组的第二个输入 列向量 | 矩阵
  direction: input
  data_types: single | double
- name: coeffs1
  summary: 分支 1 全通多项式系数 *N*×1 向量 | *N*×2 矩阵
  direction: input
  data_types: single | double
- name: coeffs2
  summary: 分支 2 全通多项式系数 *N*×1 向量 | *N*×2 矩阵
  direction: input
  data_types: single | double
- name: Output
  summary: 插值器的输出 列向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **LP** — 数据输入 列向量 | 矩阵

将数据输入指定为向量或矩阵。如果输入信号是矩阵，该模块将矩阵的每一列视为独立通道。

当您选择 **Input highpass subband** 参数时，该模块充当半带合成滤波器组。此时该端口的输入是半带分析滤波器组的低通子带输出。

在选择 **Input highpass subband** 参数之前，该端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **HP** — 合成滤波器组的第二个输入 列向量 | 矩阵

将合成滤波器组的第二个输入指定为列向量或矩阵。该信号是半带分析滤波器组的高通子带输出。如果输入信号是矩阵，该模块将矩阵的每一列视为独立通道。

两个输入的大小、数据类型和复数特性必须相同。

#### 依赖关系

要启用该端口，请选择 **Input highpass subband** 参数。

**数据类型：** `single` | `double`
**复数支持：** 是

### **coeffs1** — 分支 1 全通多项式系数 *N*×`1` 向量 | *N*×`2` 矩阵

将第一个分支的全通多项式滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Minimum multiplier`
- 清除 **Make the first branch a pure delay** 参数
- 选择 **Specify coefficients from input port** 参数

**数据类型：** `single` | `double`

### **coeffs2** — 分支 2 全通多项式系数 *N*×`1` 向量 | *N*×`2` 矩阵

将第二个分支的全通多项式滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Minimum multiplier`
- 选择 **Specify coefficients from input port** 参数

**数据类型：** `single` | `double`
### 输出

### **Output** — 插值器的输出 列向量 | 矩阵

插值器的输出，以列向量或矩阵形式返回。插值器输出的行数是输入信号行数的两倍。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Filter specification
  summary: 滤波器设计参数 Transition width and stopband attenuation（默认）| Filter order and stopband attenuation | Filter order and
    transition width | Coefficients
  group: ''
- name: Transition width (Hz)
  summary: 过渡带宽 4.1e3（默认）| 正标量
  group: ''
- name: Filter order
  summary: IIR 半带滤波器的阶数 9（默认）| 正整数
  group: ''
- name: Stopband attenuation (dB)
  summary: 阻带中所需的最小衰减 80（默认）| 正实标量
  group: ''
- name: Design method
  summary: 设计方法 Elliptic（默认）| Quasi-linear phase
  group: ''
- name: Internal allpass structure
  summary: 系数模式下的滤波器结构 Minimum multiplier（默认）| Wave Digital Filter
  group: ''
- name: Make the first branch a pure delay
  summary: 使第一个分支为纯延迟 off（默认）| on
  group: ''
- name: Delay length in samples for branch 1
  summary: 延迟长度 1（默认）| 有限正标量
  group: ''
- name: Specify coefficients from input port
  summary: 从输入端口指定系数 off（默认）| on
  group: ''
- name: Branch 1 allpass polynomial coefficients
  summary: 第一个分支的全通多项式滤波器系数 [0.1284563; 0.7906755]（默认）| *N*×1 | *N*×2
  group: ''
- name: Branch 2 allpass polynomial coefficients
  summary: 第二个分支的全通多项式滤波器系数 [0.4295667]（默认）| *N*×1 | *N*×2
  group: ''
- name: Branch 1 Wave Digital coefficients
  summary: 第一个分支的波数字滤波器形式全通滤波器系数 [0.1284563; 0.7906755]（默认）| *N*×1 | *N*×2
  group: ''
- name: Branch 2 Wave Digital coefficients
  summary: 第二个分支的波数字滤波器形式全通滤波器系数 [0.4295667]（默认）| *N*×1 | *N*×2
  group: ''
- name: Last section of branch 2 is first order
  summary: 使第二个分支的最后一个节为一阶 off（默认）| on
  group: ''
- name: Input highpass subband
  summary: 输入高通子带 off（默认）| on
  group: ''
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: ''
- name: Input sample rate (Hz)
  summary: 输入信号的采样率 22050（默认）| 正实标量
  group: ''
- name: View Filter Response
  summary: 查看滤波器响应 按钮
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Filter specification** — 滤波器设计参数 `Transition width and stopband attenuation`（默认）| `Filter order and stopband attenuation` | `Filter order and transition width` | `Coefficients`

选择该模块用于设计 IIR 半带滤波器的参数。由于滤波器设计只有两个自由度，您只能指定三个参数中的两个：

- `Transition width and stopband attenuation`（默认）—— 使用 **Transition width (Hz)** 和 **Stopband attenuation (dB)** 设计滤波器。此设计为最小阶数设计。
- `Filter order and transition width` —— 使用 **Filter order** 和 **Transition width (Hz)** 设计滤波器。
- `Filter order and stopband attenuation` —— 使用 **Filter order** 和 **Stopband attenuation (dB)** 设计滤波器。
- `Coefficients` —— 使用启用的参数直接指定滤波器系数。

### **Transition width (Hz)** — 过渡带宽 `4.1e3`（默认）| 正标量

将 IIR 半带滤波器的过渡带宽指定为正标量，单位为 Hz 或归一化频率单位*（自 R2023b 起）*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 过渡带宽的值以 Hz 为单位，且必须小于输出采样率（2 × 输入采样率）的一半。
- `Use normalized frequency (0 to 1)` —— 过渡带宽的值以归一化频率单位表示。该值必须是小于 `1.0` 的正标量。

*（自 R2023b 起）*

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Transition width and stopband attenuation`。

### **Filter order** — IIR 半带滤波器的阶数 9（默认）| 正整数

将滤波器阶数指定为正整数。如果您将 **Design method** 设置为 `Elliptic`，则 **Filter order** 必须是大于 1 的奇整数。如果您将 **Design method** 设置为 `Quasi-linear phase`，则 **Filter order** 必须是 4 的倍数。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Filter order and stopband attenuation`。

### **Stopband attenuation (dB)** — 阻带中所需的最小衰减 80（默认）| 正实标量

将 IIR 半带滤波器阻带中所需的最小衰减指定为正实标量，单位为 dB。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Filter order and stopband attenuation` 或 `Transition width and stopband attenuation`。

### **Design method** — 设计方法 `Elliptic`（默认）| `Quasi-linear phase`

指定 IIR 半带滤波器的设计方法。

- `Elliptic`（默认）—— 滤波器具有非线性相位，使用的系数较少。
- `Quasi-linear phase` —— 多相滤波器结构的第一个分支是纯延迟，从而产生近似线性的相位响应。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为除 `Coefficients` 之外的任何选项。

### **Internal allpass structure** — 系数模式下的滤波器结构 `Minimum multiplier`（默认）| `Wave Digital Filter`

将内部全通滤波器实现结构指定为 `Minimum multiplier` 或 `Wave Digital Filter`。每种结构使用不同的系数集，分别存储在相应的系数属性中。默认值为 `Minimum multiplier`。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Coefficients`。

### **Make the first branch a pure delay** — 使第一个分支为纯延迟 `off`（默认）| `on`

当您选中此复选框时，多相滤波器结构的第一个分支变为纯延迟，**Branch 1 allpass polynomial coefficients** 和 **Branch 1 Wave Digital coefficients** 参数不再适用。

默认情况下，此复选框未选中。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Coefficients`。

### **Delay length in samples for branch 1** — 延迟长度 `1`（默认）| 有限正标量

将第一个分支延迟的长度指定为有限正标量。默认值为 `1`。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- 选择 **Make the first branch a pure delay** 参数

### **Specify coefficients from input port** — 从输入端口指定系数 `off`（默认）| `on`

当您选中此复选框时，可以通过输入端口 **coeffs1** 和 **coeffs2** 输入分支 1 全通多项式系数和分支 2 全通多项式系数。当您清除此复选框时，您可以在模块对话框中通过 **Branch 1 allpass polynomial coefficients** 和 **Branch 2 allpass polynomial coefficients** 参数指定系数。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Minimum multiplier`

### **Branch 1 allpass polynomial coefficients** — 第一个分支的全通多项式滤波器系数 `[0.1284563; 0.7906755]`（默认）| *N*×`1` | *N*×`2`

将第一个分支的全通多项式滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

该参数是可调的，即您可以在仿真期间更改其值。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Minimum multiplier`
- 清除 **Make the first branch a pure delay** 参数
- 清除 **Specify coefficients from input port** 参数

### **Branch 2 allpass polynomial coefficients** — 第二个分支的全通多项式滤波器系数 `[0.4295667]`（默认）| *N*×`1` | *N*×`2`

将第二个分支的全通多项式滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

该参数是可调的，即您可以在仿真期间更改其值。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Minimum multiplier`
- 清除 **Specify coefficients from input port** 参数

### **Branch 1 Wave Digital coefficients** — 第一个分支的波数字滤波器形式全通滤波器系数 `[0.1284563; 0.7906755]`（默认）| *N*×`1` | *N*×`2`

将第一个分支的波数字滤波器（WDF）形式全通滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

每个 WDF 系数的幅值不得大于 1。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Wave Digital Filter`
- 清除 **Make the first branch a pure delay** 参数

### **Branch 2 Wave Digital coefficients** — 第二个分支的波数字滤波器形式全通滤波器系数 `[0.4295667]`（默认）| *N*×`1` | *N*×`2`

将第二个分支的波数字滤波器（WDF）形式全通滤波器系数指定为 *N*×`1` 向量或 *N*×`2` 矩阵，表示 *N* 个一阶或二阶全通节。

每个 WDF 系数的幅值不得大于 1。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为 `Coefficients`
- **Internal allpass structure** 为 `Wave Digital Filter`

### **Last section of branch 2 is first order** — 使第二个分支的最后一个节为一阶 `off`（默认）| `on`

当您选中此复选框时，该模块将第二个分支的最后一个节视为一阶节。当第二个分支的系数为 *N*×`2` 矩阵时，该模块忽略矩阵最后一行的第二个元素。第二个分支的最后一个节随后变为一阶节。

当您清除此复选框时，该模块将第二个分支的最后一个节视为二阶节。当第二个分支的系数为 *N*×`1` 矩阵时，该模块忽略此参数。

默认情况下，此复选框未选中。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为 `Coefficients`。

### **Input highpass subband** — 输入高通子带 `off`（默认）| `on`

当您选中此复选框时，该模块充当合成滤波器组。该模块接受两个输入进行合成：低通和高通子带。当您清除此复选框时，该模块充当 IIR 半带插值器，并接受单个向量或矩阵作为输入。默认情况下，此复选框未选中。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2023b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定通带边缘和阻带边缘频率。
- `Specify on dialog` —— 在模块对话框中通过 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 该模块从输入信号继承采样率。

#### 依赖关系

要启用该参数，请将 **Filter specification** 设置为除 `Coefficients` 之外的任何值。

### **Input sample rate (Hz)** — 输入信号的采样率 22050（默认）| 正实标量

将输入信号的采样率指定为标量，单位为 Hz。

#### 依赖关系

要启用该参数，请设置：

- **Filter specification** 为除 `Coefficients` 之外的任何值。
- **Sample rate mode** 为 `Specify on dialog`。

*（自 R2023b 起）*

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮可打开滤波器可视化工具（FVTool），并显示 IIR Halfband Interpolator 的幅值和相位响应。响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数并点击 **Apply**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2023b：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到 1）指定过渡带宽。

## 描述

使用多相 IIR 半带滤波器对信号进行插值

IIR Halfband Interpolator 模块通过因子 2 对输入信号执行高效的多相插值。要设计半带滤波器，您可以使用椭圆设计或准线性相位设计。该模块使用这些设计方法计算滤波器系数。为了对输入进行滤波，该模块使用多相结构。多相结构中的全通滤波器采用最小乘法器形式。

椭圆设计引入非线性相位，并且使用比准线性设计更少的系数来创建滤波器。准线性相位设计以增加系数为代价克服了相位非线性。

或者，您可以直接指定滤波器系数，而不使用设计方法设计半带滤波器。当您选择此选项时，多相实现的两个分支中的全通滤波器可以采用最小乘法器形式或波数字形式。

您还可以使用该模块实现双频带滤波器组的合成部分，以从低通和高通子带合成信号。
