---
type: simulink-block
title: '2-D IFFT'
family: 'transforms'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2difft'
documentation_source_path: 'ref/2difft.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D IFFT

## 端口

### 输入

### **Port\_1** — 输入数据向量 | 矩阵

输入数据，指定为强度值的向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出数据向量 | 矩阵

输出数据，包含输入的 2-D IFFT，以向量或矩阵形式返回。
输出的大小和数据类型与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

## 参数

### 主

### **FFT implementation** — FFT 实现 `Auto` (default) | `Radix-2` | `FFTW`

指定用于计算 FFT 的实现类型，为以下选项之一：

- `FFTW` — 选择此选项以支持任意长度的输入信号。该模块将使用 `FFTW` 实现生成的代码限制为能够运行 MATLAB® 的主机。
- `Radix-2` — 选择此选项以支持位反转处理、定点数据和浮点数据，或使用 Simulink Coder 生成可移植的 C 代码。输入矩阵的维度 *M* 和 *N* 必须为 2 的幂。要处理其他输入大小，请使用 Image Pad 模块将这些维度填充或截断为 2 的幂，或者如果可能，选择 `FFTW` 实现。有关 `Radix-2` 模式所用算法的详细信息，请参阅 Radix-2 Implementation。
- `Auto` — 选择此选项让模块选择 FFT 实现。对于非 2 的幂变换长度，该模块将生成的代码限制为 MATLAB 主机。

### **Input is in bit-reversed order** — 位反转输入 `off` (default) | `on`

指定模块的输入是位反转顺序还是线性顺序。
当以位反转顺序指定输入时，选择此参数。否则，清除此参数。如果未正确设置此参数，该模块将产生无效输出。有关输入位反转顺序的详细信息，请参阅 Bit-Reversed Order。

#### 依赖关系

要启用此参数，请将 **FFT implementation** 参数设置为 `Auto` 或 `Radix-2`。

### **Input is conjugate symmetric** — 共轭对称输入 `on` (default) | `off`

选择此参数以指定模块输入是共轭对称的，并且您希望输出为实值。否则，清除此参数。

当输入实值数据时，2-D FFT 模块产生共轭对称输出。对共轭对称输入矩阵执行 2-D IFFT 会产生实值输出。因此，如果 2-D IFFT 模块的输入是共轭对称的，并且您选择此参数，则该模块产生实值输出。选择此参数后，该模块会优化其计算方法。对于定点，不能选择此参数。

如果指定共轭对称输入数据但未选择此参数，则该模块输出带有小虚部的复值数据。如果对非共轭对称的输入数据选择此参数，则该模块输出无效数据。

### **Divide output by product of FFT length in each input dimension** — 缩放输出数据 `on` (default) | `off`

选择此参数以计算缩放后的 IFFT，它会将输出除以 FFT 输入维度长度之积，如下式所示。

f(x,y)=1MN∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN,

其中 0≤x≤M−1 且 0≤y≤N−1。

当清除此参数时，该模块计算未缩放的 IFFT 版本，如下式所示。

f(x,y)=∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off` (default) | `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法说明和限制：

- 当以下条件适用时，从此模块生成的可执行文件依赖 MATLAB 附带的预构建动态库文件（`.dll` 文件）：

  - **FFT implementation** 设置为 `FFTW`。
  - **Inherit FFT length from input dimensions** 已清除，并且输入矩阵的每个维度的长度都是 2 的幂。

  使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重定位、解包并重新构建项目。
- 当输入矩阵的每个维度的长度都是 2 的幂时，您可以从此模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算二维逆快速傅里叶变换（IFFT）

2-D IFFT 模块使用快速傅里叶变换（FFT）算法计算二维输入矩阵的离散傅里叶逆变换（IDFT）。M×N 输入矩阵 *F*(*m*, *n*) 的二维 IDFT *f*(*x*, *y*) 的公式为：

f(x,y)=1MN∑m=0M−1∑n=0N−1F(m,n)ej2πmxMej2πnyN,

其中 0≤x≤M−1 且 0≤y≤N−1。

该模块支持基于 FFTW 库的 FFT 实现以及基于一组 Radix-2 算法的实现。您可以手动选择其中一种实现，也可以让模块自动选择一种实现。
