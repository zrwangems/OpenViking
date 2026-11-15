---
type: simulink-block
title: 'Inverse Short-Time FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms and Spectral Analysis / Transforms / Fourier Transforms'
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

### **w[n]** — 分析窗向量

在 **w[n]** 端口指定分析窗。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **x[n]** — 逆短时 FFT 输出 向量 | 矩阵

该模块在 **x[n]** 端口输出逆短时 FFT 输出。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **分析窗长度** — 分析窗的长度 `512`（默认） | 大于 1 的正整数

将分析窗的长度输入为大于 1 的正整数。

### **连续 STFFT 帧之间的重叠（以采样点为单位）** — 重叠长度 `384`（默认） | 非负整数

将输入信号每一帧的重叠采样点数输入为非负整数。此值应与 Short-Time FFT 模块对话框中的 **连续窗之间的重叠（以采样点为单位）** 参数相同。

### **每个输出帧的采样点数** — 每个输出帧的采样点数 `512`（默认） | 正整数

将输出信号的所需帧大小输入为正整数。

### **输入为共轭对称** — 模块的输入为共轭对称 `on`（默认） | `off`

当模块的输入既是浮点又是共轭对称，并且您希望得到实值输出时，请选中此复选框。如果当输入不是共轭对称时选中此复选框，则模块的输出无效。此参数不能用于定点信号。

### **如果分析窗不支持完美信号重构则断言** — 如果分析窗不支持完美信号重构则报错 `off`（默认） | `on`

选中此复选框可在 Short-Time FFT 模块所使用的分析窗不支持完美信号重构时显示错误。

输入到 Short-time FFT 模块的时域信号无法完美重构。

为了确定信号是否可以完美重构，Inverse Short-time FFT 模块使用您在 **分析窗长度** 和 **重构误差容限** 参数中输入的值。

### **重构误差容限** — 原始信号的重构误差容限 `1e-4`（默认） | 实数标量

将原始信号重构中可接受的误差量输入为实数标量。

#### 依赖关系

要启用此参数，请选中 **如果分析窗不支持完美信号重构则断言** 复选框。

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

- 生成的代码在某些条件下依赖 `memcpy` 或
  `memset` 函数（`string.h`）。
- 当输入长度不是 2 的幂时，此模块生成的可执行文件依赖 MATLAB® 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一开发环境中重定位、解包并重新构建项目。有关更多详细信息，请参阅如何在 MATLAB 外部运行生成的可执行文件。

  当输入长度是 2 的幂时，您可以从该模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过执行逆短时快速傅里叶变换（FFT）恢复时域信号

Inverse Short-Time FFT 模块通过两步过程，从 Short-Time FFT 模块的频域输出重构时域信号。首先，该模块实现重叠相加算法。

x[n]=LW(0)∑p=−∞∞[1N∑k=0N−1X[pL,k]ej2πkn/N]

然后，该模块对信号重新缓冲，以重构时域信号。取决于 Short-Time FFT 模块所使用的分析窗，Inverse Short-Time FFT 模块可能会或可能不会实现时域信号的完美重构。
