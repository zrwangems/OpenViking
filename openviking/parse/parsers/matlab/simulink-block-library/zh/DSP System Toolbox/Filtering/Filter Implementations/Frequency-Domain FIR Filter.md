---
type: simulink-block
title: 'Frequency-Domain FIR Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'frequencydomainfirfilter'
documentation_source_path: 'ref/frequencydomainfirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Frequency-Domain FIR Filter

## 端口
```yaml
ports:
- name: x
  summary: 数据输入 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Num
  summary: 时域 FIR 滤波器系数 行向量 | 矩阵 *(自 R2024a 起)*
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: NumFFT
  summary: 频域 FIR 滤波器系数 行向量 | 矩阵 | 三维数组 *(自 R2024a 起)*
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: output
  summary: 滤波后的输出 向量 | 矩阵 | 三维数组 *(自 R2024a 起)*
  direction: input
  data_types: single | double
- name: latency
  summary: 滤波器延迟 正整数
  direction: input
  data_types: uint32
```

### 输入

### **x** — 数据输入 向量 | 矩阵

数据输入，指定为大小为 *L*×*T* 的向量或矩阵。此模块支持可变大小输入信号，也就是说，即使在调用算法之后，您也可以更改输入帧大小（行数）。但是，通道数（列数）必须保持不变。

在您选择 **Specify coefficients from input port** 参数之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Num** — 时域 FIR 滤波器系数 行向量 | 矩阵 *(自 R2024a 起)*

将时域 FIR 滤波器系数指定为大小为 *F*×*NumLen* 的行向量（单个滤波器）或矩阵（多个滤波器）*(自 R2024a 起)*，其中 *F* 是滤波器数量，*NumLen* 是滤波器长度。如果 *F* 大于 1，则其值必须是输入通道数（列数）*T* 与您通过 **Number of propagation paths** 参数指定的路径数 *P* 的乘积的倍数。乘数因子决定输出通道数 *R*，等于 *F*/(*T* × *P*)。

系数值可以在仿真期间更改，但分子的大小必须保持不变。

#### 依赖关系

要启用此端口，请将 **Numerator domain** 设置为 `Time`，并选择 **Specify coefficients from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **NumFFT** — 频域 FIR 滤波器系数 行向量 | 矩阵 | 三维数组 *(自 R2024a 起)*

将频域 FIR 滤波器系数指定为行向量、矩阵或三维数组 *(自 R2024a 起)*。

当您清除 **Partition numerator to reduce latency** 参数时，此端口输入的系数可以是行向量或大小为 *F*×*FFTLength* 的矩阵。FFT 长度等于向量输入的长度。如果 *F* 大于 1（多个滤波器）*(自 R2024a 起)*，则其值必须是输入通道数（列数）*T* 与您通过 **Number of propagation paths** 参数指定的路径数 *P* 的乘积的倍数。乘数因子决定输出通道数 *R*，等于 *F*/(*T* × *P*)。

当您选择 **Partition numerator to reduce latency** 参数时，**Frequency response** 必须是大小为 2*PL*×*N* 的矩阵以表示单个滤波器，或大小为 2*PL*×*N*×*F* 的三维数组 *(自 R2024a 起)* 以表示多个滤波器，其中 *PL* 是分区大小，*N* 是分区数，*F* 是滤波器数量。

#### 依赖关系

要启用此端口，请将 **Numerator domain** 设置为 `Frequency`，并选择 **Specify frequency response from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是
### 输出参数

### **output** — 滤波后的输出 向量 | 矩阵 | 三维数组 *(自 R2024a 起)*

滤波后的输出，返回为向量、矩阵或三维数组 *(自 R2024a 起)*。

当滤波器数量 *F* 大于 1 且您选择 **Sum filtered output contributions from all input channels** 参数时，模块将每个输入通道的滤波输出相加，生成 *L*×*R* 输出矩阵，其中 *L* 是输入帧大小（输入行数），*R* 是输出通道数。*R* 等于 *F*/(*T* x *P*)，其中 *F* 是滤波器数量，*T* 是输入通道数，*P* 是您在 **Number of propagation paths** 参数中指定的值。*(自 R2024a 起)*

当您清除 **Sum filtered output contributions from all input channels** 参数时，模块不会对所有输入通道的滤波输出贡献求和。输出是 *L*×*R*×*T* 数组。`output(:,j,k)` 指的是第 *k* 个输入通道对第 *j* 个输出通道的输出。例如，`output(:,3,2)` 表示第二个输入通道在第三个输出通道上的输出。*(自 R2024a 起)*

有关对象如何计算输出的更多信息，请参阅算法。

输出的数据类型和复/实性与输入信号相同。

在您选择 **Output filter latency** 参数并点击 **Apply** 之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **latency** — 滤波器延迟 正整数

滤波器延迟，返回为标量。此延迟是重叠相加法和重叠保留法固有的，不包括滤波器的群延迟。此端口仅在您选择 **Output filter latency** 复选框时出现。

在您选择 **Output filter latency** 复选框并点击 **Apply** 之前，此端口未命名。

**数据类型：** `uint32`
## 参数
```yaml
parameters:
- name: Frequency-domain filter method
  summary: 频域滤波方法 Overlap-save（默认）| Overlap-add
  group: ''
- name: Numerator domain
  summary: 分子域 Time（默认）| Frequency
  group: ''
- name: Specify coefficients from input port
  summary: 指定时域 FIR 滤波器系数的标志 off（默认）| on
  group: ''
- name: Filter coefficients
  summary: 时域 FIR 滤波器系数 fir1(100,0.3)（默认）| 行向量 | 矩阵 *(自 R2024a 起)*
  group: ''
- name: Specify frequency response from input port
  summary: 指定频域滤波器系数的标志 off（默认）| on
  group: ''
- name: Frequency response
  summary: 滤波器的频率响应 fft(fir1(100,0.3),202)（默认）| 行向量 | 矩阵 | 三维数组 *(自 R2024a 起)*
  group: ''
- name: Number of propagation paths
  summary: 每个输入通道和输出通道对之间的传播路径数 1（默认）| 正整数
  group: ''
- name: Sum filtered output contributions from all input channels
  summary: 对所有输入通道的滤波输出贡献求和的选项 true（默认）| false
  group: ''
- name: Partition numerator to reduce latency
  summary: 对分子进行分区以减少延迟的选项 off（默认）| on
  group: ''
- name: Numerator partition length
  summary: 分子的分区长度 32（默认）| 正整数
  group: ''
- name: Time-domain numerator length
  summary: 时域分子长度 101（默认）| 正整数
  group: ''
- name: Inherit FFT length from numerator length
  summary: 从分子长度继承 FFT 长度的标志 on（默认）| off
  group: ''
- name: FFT length
  summary: FFT 长度 1024（默认）| 正整数
  group: ''
- name: Filter is real
  summary: 指定滤波器是否为实数的标志 true（默认）| false
  group: ''
- name: Output filter latency
  summary: 输出滤波器延迟的标志 'off'（默认）| 'on'
  group: ''
- name: View Filter Response
  summary: 可视化频率响应 button
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Frequency-domain filter method** — 频域滤波方法 `Overlap-save`（默认）| `Overlap-add`

将频域滤波方法指定为 `Overlap-save` 或 `Overlap-add`。有关这两种方法的更多详细信息，请参阅算法。

### **Numerator domain** — 分子域 `Time`（默认）| `Frequency`

将滤波器系数的域指定为以下之一：

- `Time` —— 在 **Filter coefficients** 参数中或通过 **Num** 输入端口指定时域滤波器系数。
- `Frequency` —— 在 **Frequency response** 参数中或通过 **NumFFT** 输入端口指定滤波器的频率响应。

### **Specify coefficients from input port** — 指定时域 FIR 滤波器系数的标志 `off`（默认）| `on`

当您选择此复选框时，时域 FIR 滤波器系数通过端口 **Num** 输入。当您清除此复选框时，系数通过 **Filter coefficients** 参数在模块对话框中指定。

要查看滤波器响应，请清除此复选框，在模块对话框中指定系数，然后点击 **View Filter Response** 按钮。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Time`。

### **Filter coefficients** — 时域 FIR 滤波器系数 `fir1(100,0.3)`（默认）| 行向量 | 矩阵 *(自 R2024a 起)*

将时域 FIR 滤波器系数指定为大小为 *F*×*NumLen* 的行向量（单个滤波器）或矩阵（多个滤波器）*(自 R2024a 起)*，其中 *F* 是滤波器数量，*NumLen* 是滤波器长度。如果 *F* 大于 1，则其值必须是输入通道数（列数）*T* 与您通过 **Number of propagation paths** 参数指定的路径数 *P* 的乘积的倍数。乘数因子决定输出通道数 *R*，等于 *F*/(*T* × *P*)。

系数值可以在仿真期间更改，但分子的大小必须保持不变。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Time`，并清除 **Specify coefficients from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是

### **Specify frequency response from input port** — 指定频域滤波器系数的标志 off（默认）| on

当您选择此复选框时，频域 FIR 滤波器系数通过端口 **NumFFT** 输入。当您清除此复选框时，系数通过 **Frequency response** 参数在模块对话框中指定。

要查看滤波器响应，请清除此复选框，在模块对话框中指定频率响应，然后点击 **View Filter Response** 按钮。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Frequency`。

### **Frequency response** — 滤波器的频率响应 `fft(fir1(100,0.3),202)`（默认）| 行向量 | 矩阵 | 三维数组 *(自 R2024a 起)*

将滤波器的频率响应指定为行向量、矩阵或三维数组 *(自 R2024a 起)*。

当您清除 **Partition numerator to reduce latency** 参数时，**Frequency response** 可以是行向量或大小为 *F*×*FFTLength* 的矩阵。FFT 长度等于 **Frequency response** 向量的长度。如果 *F* 大于 1（多个滤波器）*(自 R2024a 起)*，则其值必须是输入通道数（列数）*T* 与您通过 **Number of propagation paths** 参数指定的路径数 *P* 的乘积的倍数。乘数因子决定输出通道数 *R*，等于 *F*/(*T* × *P*)。

当您选择 **Partition numerator to reduce latency** 参数时，**Frequency response** 必须是大小为 2*PL*×*N* 的矩阵以表示单个滤波器，或大小为 2*PL*×*N*×*F* 的三维数组 *(自 R2024a 起)* 以表示多个滤波器，其中 *PL* 是分区大小，*N* 是分区数，*F* 是滤波器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Frequency`，并清除 **Specify frequency response from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**复数支持：** 是

### **Number of propagation paths** — 每个输入通道和输出通道对之间的传播路径数 `1`（默认）| 正整数

*自 R2024a 起*

将每个输入通道和输出通道对之间的传播路径数 *P* 指定为正整数。每条路径由唯一的滤波器表示。当您将路径数指定为大于 `1` 时，滤波器对多径传播进行建模。算法对每个输入通道和输出通道对之间所有路径的滤波输出贡献求和。

有关示例，请参阅 Filter Input Signal Using 1-by-2 SIMO System。

#### 依赖关系

要启用此参数，滤波器数量 *F* 必须大于 1。

**数据类型：** `single` | `double`

### **Sum filtered output contributions from all input channels** — 对所有输入通道的滤波输出贡献求和的选项 `true`（默认）| `false`

*自 R2024a 起*

选择此复选框以对所有输入通道的滤波输出贡献求和。当您选择此复选框时，模块将每个输入通道的滤波输出相加，生成 *L*×*R* 输出矩阵，其中 *L* 是输入帧大小（输入行数），*R* 是输出通道数。*R* 等于 *F*/(*T* x *P*)，其中 *F* 是滤波器数量，*T* 是输入通道数，*P* 是您通过 **Number of propagation paths** 参数指定的值。

当您清除此参数时，模块不会对所有输入通道的滤波输出贡献求和。输出是 *L*×*R*×*T* 数组。

有关模块如何基于此参数的值计算输出的更多信息，请参阅 Modeling MIMO System with Multiple Propagation Paths。

#### 依赖关系

要启用此属性，滤波器数量 *F* 必须大于 1。

### **Partition numerator to reduce latency** — 对分子进行分区以减少延迟的选项 `off`（默认）| `on`

选择此参数以对分子进行分区以减少延迟。当您选择此参数时，模块将分子划分为由 **Numerator partition length** 参数指定长度的段。滤波器对每个分区执行重叠保留法或重叠相加法，并组合部分结果以形成整体输出。此选项将延迟降低到分区长度。

当您清除此参数时，滤波器使用传统的重叠保留法或重叠相加法。此情况下的延迟为 FFT 长度 – *NumLen* + 1，其中 *NumLen* 是滤波器长度。有关滤波器长度的更多信息，请参阅 **Filter coefficients** 参数。

### **Numerator partition length** — 分子的分区长度 `32`（默认）| 正整数

将分子的分区长度 *PL* 指定为小于或等于分子长度的正整数。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Time`，并选择 **Partition numerator to reduce latency** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Time-domain numerator length** — 时域分子长度 `101`（默认）| 正整数

将时域分子长度指定为正整数。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Frequency`，并清除 **Partition numerator to reduce latency** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Inherit FFT length from numerator length** — 从分子长度继承 FFT 长度的标志 on（默认）| off

当您选择此复选框时，FFT 长度等于分子长度的两倍。当您清除此复选框时，您通过 **FFT length** 参数指定 FFT 长度。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Time`，并清除 **Partition numerator to reduce latency** 参数。

### **FFT length** — FFT 长度 `1024`（默认）| 正整数

您指定的 FFT 长度必须大于或等于您在 **Filter coefficients** 参数中指定的分子长度。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Time`，并清除 **Partition numerator to reduce latency** 和 **Inherit FFT length from numerator length** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter is real** — 指定滤波器是否为实数的标志 `true`（默认）| `false`

选择此参数以指定滤波器系数全部为实数。

#### 依赖关系

要启用此参数，请将 **Numerator domain** 设置为 `Frequency`。

### **Output filter latency** — 输出滤波器延迟的标志 `'off'`（默认）| `'on'`

当您选择此复选框并点击 **Apply** 时，模块通过 **latency** 端口输出滤波器延迟。

### **View Filter Response** — 可视化频率响应 `button`

点击此按钮将打开滤波器可视化工具，并显示频域 FIR 滤波器的幅值响应。响应基于您在模块对话框中选择的参数。要在可视化工具运行时更新响应，请修改对话框中的参数并点击 **Apply**。

您可以从可视化工具的界面配置绘图设置和频率响应测量。

在 **Scope** 选项卡上，您可以启用图例、指定绘制滤波器的幅值和相位响应、修改绘图设置、生成用于重新创建绘图的脚本，甚至保存或共享设置。在 **Measurements** 选项卡上，您可以启用数据光标，并显示滤波器响应的峰值。

有关滤波器可视化工具界面及其工具的更多详细信息，请参阅 Configure Filter Visualizer。

#### 依赖关系

要启用此按钮，请清除 **Specify coefficients from input port** 和 **Specify frequency response from input port** 参数。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Filtering / Filter Implementations

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

**在 R2017b 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

### R2024a：支持多个滤波器

您可以通过在时域和频域中指定多个滤波器来对 MIMO 系统建模。您还可以为每个输入和输出对之间指定多条路径。

## 描述

在频域中对输入信号进行滤波

Frequency-Domain FIR Filter 模块实现基于频域快速傅里叶变换 (FFT) 的滤波，以对流式输入信号进行滤波。在时域中，滤波操作涉及输入与有限脉冲响应 (FIR) 滤波器脉冲响应之间的卷积。在频域中，滤波操作涉及输入的傅里叶变换与脉冲响应的傅里叶变换的乘积。随着脉冲响应变得更长，频域滤波比时域滤波更高效。您可以通过将 **Numerator domain** 设置为 `Frequency`，直接在频域中指定滤波器系数。

此模块使用重叠保留法和重叠相加法来执行频域滤波。对于脉冲响应长度较长的滤波器，这两种方法固有的延迟可能很大。为了减轻此延迟，Frequency-Domain FIR Filter 模块将脉冲响应划分为较短的块，并在这些较短的块上实现重叠保留法和重叠相加法。要划分脉冲响应，请选中 **Partition numerator to reduce latency** 复选框。有关这两种方法以及通过脉冲响应划分来减少延迟的更多详细信息，请参阅算法。

Frequency-Domain FIR Filter 模块可以通过在时域和频域中支持多个滤波器，对单输入多输出 (SIMO) 和多输入多输出 (MIMO) 系统建模。有关展示如何对此类系统建模的示例，请参阅 Filter Input Signal Using 1-by-2 SIMO System 和 Filter Input Signal Using 3-by-2 MIMO System。您还可以使用 **Number of propagation paths** 参数为每个输入通道和输出通道对之间指定多条路径。有关对 MIMO 系统建模的更多信息，请参阅 Modeling MIMO System with Multiple Propagation Paths。*（自 R2024a 起）*
