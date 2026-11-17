---
type: simulink-block
title: 'Magnitude FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'magnitudefft'
documentation_source_path: 'ref/magnitudefft.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnitude FFT

## 端口

### 输入

### **Input** — 输入向量 | 矩阵

将输入 *u* 指定为大小为 *M*×*N* 的向量或矩阵。

该模块将 *M*×*N* 矩阵输入视为来自 *N* 个独立通道的 *M* 个顺序时间采样。

Magnitude FFT 模块支持实数和复数浮点输入。该模块还支持 `Magnitude` 和 `Magnitude squared` 模式下的实数定点输入，以及 `Magnitude squared` 模式下的复数定点输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 幅度 FFT 输出向量 | 矩阵

幅度 FFT 输出，以向量或矩阵形式返回。

该模块为 *N* 个独立通道中的每一个计算单独的估计值，并生成 *Nfft*×*N* 矩阵输出。输出矩阵的每一列包含对应输入列在 [0,*Fs*) 范围内 *Nfft* 个等间隔频率点处的功率谱密度估计，其中 *Fs* 表示信号的采样率。

当您将 **Output** 参数设置为 `Magnitude squared` 时，*M*×*N* 输入 *u* 的模块输出等效于：

```
y = abs(fft(u,nfft)).^2	% M ≤ nfft
```

当您将 **Output** 参数设置为 `Magnitude` 时，输入 *u* 的模块输出等效于：

```
y = abs(fft(u,nfft)) 	  % M ≤ nfft
```

当 *M* > *Nfft* 时，该模块在计算 FFT 之前使用上述方程之一将输入环绕为 *Nfft*：

```
y(:,k) = datawrap(u(:,k),nfft)  % 1 ≤ k ≤ N
```

当 *M* > *Nfft* 时，该模块也可以截断输入：

```
y(:,k) = abs(fft(u,nfft)) 	% 1 ≤ k ≤ N
```

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### **Output** — 输出类型 `Magnitude squared`（默认）| `Magnitude`

指定该模块计算输入信号的幅度 FFT 还是幅度平方 FFT。有关该模块如何基于此设置计算输出的更多详细信息，请参阅 **Output** 端口描述。

### **FFT implementation** — FFT 实现 `Auto`（默认）| `Radix-2` | `FFTW`

将此参数设置为以下值之一：

- `Auto` —— 使用此选项让模块选择 FFT 实现。对于不是 2 的幂的变换长度，该模块将生成的代码限制在 MATLAB® 主机计算机上。
- `Radix-2` —— 将此选项用于位反转处理、定点或浮点数据，或使用 Simulink® Coder™ 生成可移植的 C 代码。输入矩阵的第一维 *M* 必须是 2 的幂。要处理其他输入大小，请使用 Pad 模块将维度填充或截断为 2 的幂，或者如果可能的话选择 `FFTW` 算法。
- `FFTW` —— 使用此选项支持任意长度的输入信号。该模块将使用 FFTW 实现生成的代码限制在 MATLAB 主机计算机上。

### **Inherit FFT length from input dimensions** — 从输入帧大小继承 FFT 长度 `off`（默认）| `on`

选择此参数以使用输入帧大小作为执行 FFT 的数据点数。当您选中此复选框时，输入帧大小必须是 2 的幂。当您不选中此复选框时，**FFT length** 参数指定数据点数。

### **FFT length** — FFT 长度 `256`（默认）| 正整数

输入执行 FFT 的数据点数 *Nfft*。当 *Nfft* 大于输入帧大小时，该模块根据需要将每一帧用零填充。当 *Nfft* 小于输入帧大小时，该模块根据需要环绕每一帧。

当您将 **FFT implementation** 参数设置为 `Radix-2` 时，此值必须是 2 的幂。

#### 依赖关系

要启用此参数，请清除 **Inherit FFT length from input dimensions** 参数。

### **Wrap input data when FFT length is shorter than input length** — 选择环绕或截断输入 `on`（默认）| `off`

根据 **FFT length** 选择环绕或截断输入。

当您选择此参数且 **FFT length** 短于输入长度时，在 FFT 操作之前会进行模长数据环绕。当您清除此参数时，该模块在 FFT 操作之前将输入数据截断为 FFT 长度。

## 所属库

DSP System Toolbox / Estimation / Power Spectrum Estimation DSP System Toolbox / Transforms / Power Spectrum Estimation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。
- 当以下条件适用时，从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）：

  - 您将 **FFT implementation** 设置为 `FFTW`。
  - 您清除 **Inherit FFT length from input dimensions** 参数并将 **FFT length** 设置为不是 2 的幂的值。

  使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的其他开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。
- 当 FFT 长度是 2 的幂时，您可以从该模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用周期图方法计算频谱的非参数估计

Magnitude FFT 模块使用周期图方法计算频谱的非参数估计。
