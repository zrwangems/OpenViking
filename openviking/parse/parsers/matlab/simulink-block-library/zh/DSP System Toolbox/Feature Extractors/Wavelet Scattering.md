---
type: simulink-block
title: 'Wavelet Scattering'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Feature Extractors'
documentation_page: 'waveletscattering'
documentation_source_path: 'ref/waveletscattering.html'
language: zh-CN
chinese_source: worker-translation
---

# Wavelet Scattering

## 端口

### 输入

### **Input** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。该模块将矩阵中的每一列视为一个单独的通道。例如，该模块将 1×*Nchann* 行向量视为 *Nchann* 个单独的通道。

当输入数据类型为 `single` 时，该模块以单精度执行内部运算。输入数据类型决定了滤波器组中散射分解的精度。

输入帧长度不必与模块对话框中指定的信号长度匹配。该模块使用缓冲区以 **Signal length (samples)** 长度的帧向小波散射算法提供输入。如果输入帧大小与信号长度不匹配，该模块以多速率模式运行。

**数据类型：** `single` | `double`
### 输出

### **Output** — 输出信号 矩阵 | 三维数组

输出信号，以矩阵或三维数组形式返回。

对于列向量输入，输出维度为 *Npath*×*Nscat*，其中 *Npath* 是散射路径数，*Nscat* 是每条路径中的散射系数数量，即散射系数的分辨率。

对于矩阵输入，输出维度为 *Npath*×*Nscat*×*Nchann*，其中 *Nchann* 是输入中的列数。

**数据类型：** `single` | `double`

## 参数

### **Signal length (samples)** — 以采样点表示的信号长度 `1024`（默认）| 正整数 ≥ 16

将信号长度指定为以采样点表示的正整数 ≥ 16。

输入帧长度不必与信号长度匹配。该模块使用缓冲区以 **Signal length** 长度的帧向小波散射算法提供输入。如果输入帧大小与信号长度不匹配，该模块以多速率模式运行。

**数据类型：** `double`

### **Overlap length (Samples)** — 以采样点表示的重叠长度 `0`（默认）| 正整数

将信号连续帧之间的重叠（以采样点表示）指定为非负整数。

**数据类型：** `double`

### **Specify sample rate** — 指定采样率 off（默认）| on

使用 `Sample rate (Hz)` 参数在模块对话框上指定采样率。如果不选中此复选框，频率以周期/采样点为单位，奈奎斯特频率为 ½。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 采样率 `16e3`（默认）| 正标量

将采样率指定为以 Hz 表示的正标量。

#### 依赖关系

要启用此参数，请选中 **Specify sample rate** 参数。

**数据类型：** `double`

### **Invariance scale (samples)** — 以采样点表示的散射变换不变尺度 `512`（默认）| 正整数

将散射变换不变尺度指定为以采样点表示的正整数。不变尺度指定了散射变换的平移不变性。

如果不指定采样率，不变尺度以采样点为单位。如果指定采样率，不变尺度以秒为单位。

不变尺度不能超过信号长度。如果信号长度为 1000 个采样点且不指定采样率，不变尺度的最大值为 1000 个采样点。

#### 依赖关系

要启用此参数，请清除 **Specify sample rate** 参数。

**数据类型：** `double`

### **Invariance scale (s)** — 以秒表示的散射变换不变尺度 `0.032`（默认）| 正标量

将散射变换不变尺度指定为正标量。不变尺度指定了散射变换的平移不变性。

如果不指定采样率，不变尺度以采样点为单位。如果指定采样率，不变尺度以秒为单位。默认情况下，不变尺度为信号长度的一半。

不变尺度不能超过信号长度。如果信号长度为 1000 个采样点且指定采样率为 200 Hz，则不变尺度的最大值为 5。

#### 依赖关系

此参数仅在选中 **Specify sample rate** 参数时显示。

**数据类型：** `double`

### **Quality factors** — 散射滤波器组的品质因数 [`8`,`1`]（默认）| 正整数 | 单调递减正整数向量

将散射滤波器组的品质因数指定为正整数或单调递减正整数向量。滤波器组品质因数是每倍频程的小波滤波器数量。品质因数不能超过 32 且必须大于或等于 1。

默认情况下，该模块创建的小波散射网络有两个滤波器组。第一个滤波器组的品质因数为每倍频程八个小波，第二个滤波器组的品质因数为每倍频程一个小波。

**数据类型：** `double`

### **Reduce the number of scattering paths** — 优化散射变换 off（默认）| on

指定是否优化散射变换并减少散射路径数。

选中此参数时，算法基于带宽考虑减少要计算的散射路径数。散射变换排除不满足以下准则的二阶及更高阶散射路径：

第 (*i*+1) 个滤波器组中小波滤波器的中心频率减去 3-dB 带宽的 ½ 必须与第 *i* 个滤波器组中小波滤波器的 0 (DC) 加上 3-dB 带宽的 ½ 重叠。

如果不满足此准则，则排除高阶路径。对于大多数网络，选中 **Reduce the number of scattering paths** 参数可以显著减少散射路径数和散射变换的计算复杂度。

**数据类型：** `Boolean`

### **Oversampling factor** — 过采样因子 `0`（默认）| 非负整数 | `Inf`

将过采样因子指定为非负整数或 `Inf`。

过采样因子指定每个信号的散射系数数量以 log2 尺度增加的倍数。默认情况下，**Oversampling factor** 设置为 `0`，对应于对系数进行临界降采样。要获得完全非抽取的散射变换，请将 **Oversampling factor** 设置为 `Inf`。

将 **Oversampling factor** 设置为导致系数多于采样点的值等效于将 **Oversampling factor** 设置为 `Inf`。增加 **Oversampling factor** 会显著增加散射变换的计算复杂度和内存需求。

如果将 **Oversampling factor** 设置为 2，散射变换对每条散射路径返回的系数数量是临界采样数量的 `22` 倍。

**数据类型：** `double`

### **Boundary signal extension** — 信号延拓方法 `periodic`（默认）| `reflection`

将边界处应用的信号延拓方法指定为：

- `periodic` — 将信号周期延拓至长度 `2^ceil(log2(N))`，其中 *N* 是信号长度。
- `reflection` — 将信号反射延拓至长度 `2^ceil(log2(2N))`，其中 *N* 是信号长度。

信号被延拓以匹配小波滤波器的长度。滤波器长度为 2 的幂。

信号延拓方法用于内部运算。结果在返回之前被降采样回原始信号的尺度。

### 散射系数

### **Include zeroth-order coefficients** — 包含零阶系数 off（默认）| on

指定是否包含零阶系数。

**数据类型：** `Boolean`

### **Normalization** — 系数归一化 `none`（默认）| `parent`

将应用于散射系数的归一化类型指定为 `none` 或 `parent`。如果指定为 `parent`，阶数大于 0 的散射系数沿散射路径由其父系数归一化。

### **Transform** — 系数变换 `none`（默认）| `log`

将应用于散射系数的变换类型指定为 `none` 或 `log`。

## 所属库

DSP System Toolbox / Feature Extractors

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

如果动态内存分配关闭，此模块不支持代码生成。要打开动态内存分配，请在 MATLAB 命令提示符下运行此命令。

```
set_param(gcs,'MATLABDynamicMemAlloc','on')
```

## 版本历史

**在 R2022b 中引入**

## 描述

在 Simulink 中对小波散射网络建模

Wavelet Scattering 模块为 Simulink® 环境中的小波时间散射创建了一个框架。使用此模块从实值数据中提取低方差特征，然后将这些特征用于机器学习和深度学习应用。该模块使用预定义的小波滤波器计算尺度图，并对尺度图应用平均滤波器以进行特征提取。有关详细信息，请参阅 Wavelet Scattering (Wavelet Toolbox)。要在 MATLAB® 中执行小波散射，请使用 `waveletScattering` (Wavelet Toolbox) 函数。

Wavelet Scattering 模块需要 Wavelet Toolbox™。
