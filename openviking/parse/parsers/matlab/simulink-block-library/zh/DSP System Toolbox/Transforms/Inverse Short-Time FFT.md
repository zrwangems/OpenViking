---
type: simulink-block
title: 'Inverse Short-Time FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'inverseshorttimefft'
documentation_source_path: 'ref/inverseshorttimefft.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Short-Time FFT

## 端口

### 输入

### **X[nL,k]** — 频域输入信号 无向向量 | 列向量 | 矩阵

将频域输入信号指定为向量或矩阵。FFT 长度等于 **x[nL,k]** 端口处输入的行数。因此，输入行数必须大于或等于窗长度。

**数据类型：** `single` | `double`
**复数支持：** 是

### **w[n]** — 分析窗 向量

在 **w[n]** 端口指定分析窗。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **x[n]** — 逆短时 FFT 输出 向量 | 矩阵

模块在 **x[n]** 端口输出逆短时 FFT 结果。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **Analysis window length** — 分析窗长度 `512`（默认）| 大于 1 的正整数

输入分析窗长度，为大于 1 的正整数。

### **Overlap between consecutive STFFT frames (in samples)** — 重叠长度 `384`（默认）| 非负整数

输入输入信号每帧重叠的样本数，为非负整数。此值应与 Short-Time FFT 模块对话框中的 **Overlap between consecutive windows (in samples)** 参数相同。

### **Samples per output frame** — 每个输出帧的样本数 `512`（默认）| 正整数

输入输出信号的期望帧大小，为正整数。

### **Input is conjugate symmetric** — 模块输入为共轭对称 `on`（默认）| `off`

当模块输入为浮点且共轭对称，并且您希望输出为实值时，选中此复选框。如果输入不是共轭对称时选中此复选框，则模块的输出无效。此参数不能用于定点信号。

### **Assert if analysis window does not support perfect signal reconstruction** — 分析窗不支持完美信号重建时出错 `off`（默认）| `on`

选中此复选框可在 Short-Time FFT 模块使用的分析窗不支持完美信号重建时显示错误。

输入到 Short-time FFT 模块的时域信号无法完美重建。

为确定信号是否可以完美重建，Inverse Short-time FFT 模块使用您在 **Analysis window length** 和 **Reconstruction error tolerance** 参数中输入的值。

### **Reconstruction error tolerance** — 原始信号的重建误差容限 `1e-4`（默认）| 实标量

输入原始信号重建中可接受的误差量，为实标量。

#### 依赖

要启用此参数，请选中 **Assert if analysis window does not support perfect signal reconstruction** 复选框。

## 所属库

DSP System Toolbox / Transforms / Matrix Operations

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

使用说明和限制：

- 生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。
- 当输入长度不是 2 的幂时，从此模块生成的可执行文件依赖于 MATLAB® 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩的 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅如何在 MATLAB 外部运行生成的可执行文件。

  当输入长度是 2 的幂时，您可以从此模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过执行逆短时快速傅里叶变换（FFT）恢复时域信号

逆短时 FFT 模块使用两步过程从短时 FFT 模块的频域输出重建时域信号。首先，该模块实现重叠相加算法。

x[n]=LW(0)∑p=−∞∞[1N∑k=0N−1X[pL,k]ej2πkn/N]

然后，该模块对信号进行重新缓冲，以重建时域信号。根据短时 FFT 模块所使用的分析窗，逆短时 FFT 模块可能会或可能不会实现时域信号的完美重建。
