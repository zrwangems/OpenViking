---
type: simulink-block
title: '2-D FFT'
family: 'transforms'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: '2dfft'
documentation_source_path: 'ref/2dfft.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D FFT

## 端口

### 输入

### **Port\_1** — 输入数据向量 | 矩阵

输入数据，指定为强度值向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — 输出数据向量 | 矩阵

输出数据，包含输入的 2-D FFT，以向量或矩阵形式返回。输出的大小和数据类型与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

## 参数

### 主

### **FFT 实现** — FFT 实现 `Auto`（默认） | `Radix-2` | `FFTW`

指定用于计算 FFT 的实现类型，为以下选项之一：

- `FFTW` — 选择此选项以支持任意长度输入信号。该模块将使用 `FFTW` 实现生成的代码限制为能够运行 MATLAB® 的主机计算机。
- `Radix-2` — 选择此选项以支持位反转处理、定点数据和浮点数据，或使用 Simulink Coder 生成可移植 C 代码。输入矩阵的维度 *M* 和 *N* 必须是 2 的幂。要处理其他输入大小，请使用 Image Pad 模块将这些维度填充或截断为 2 的幂，或者如果可能，选择 `FFTW` 实现。有关 `Radix-2` 模式所用算法的详细信息，请参阅 Radix-2 Implementation。
- `Auto` — 选择此选项让模块选择 FFT 实现。对于非 2 的幂变换长度，该模块将生成的代码限制为 MATLAB 主机计算机。

### **以位反转顺序输出** — 位反转输出 `off`（默认） | `on`

选择此参数可使输出数据相对于输入数据的顺序为位反转顺序。如果清除此参数，输出数据相对于输入数据的顺序呈现为线性顺序。有关输出的位反转顺序的详细信息，请参阅 Bit-Reversed Order。

#### 依赖关系

要启用此参数，请将 **FFT 实现** 参数设置为 `Auto` 或 `Radix-2`。

### **按 FFT 长度缩放结果** — 缩放输出数据 `off`（默认） | `on`

选择此参数时，模块会将输出除以 FFT 长度。当您希望 FFT 的输出保持与输入相同的幅度范围时，此选项很有用。这在处理定点数据类型时特别有用。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **锁定数据类型设置以防止定点工具更改** — 数据类型覆盖 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

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

使用说明和限制：

- 当这些条件适用时，从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）：

  - **FFT 实现** 设置为 `FFTW`。
  - **从输入维度继承 FFT 长度** 被清除，并且输入矩阵每个维度的长度为 2 的幂。

  使用 `packNGo` 函数将从该模块生成的代码及所有相关文件打包到压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的其他开发环境中重新定位、解包并重建您的项目。
- 当输入矩阵每个维度的长度为 2 的幂时，您可以从该模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算二维快速傅里叶变换（FFT）

2-D FFT 模块使用快速傅里叶变换（FFT）算法计算二维输入矩阵的离散傅里叶变换（DFT）。对于 *M*×*N* 输入矩阵 *f*(*x*, *y*) 的二维 DFT *F*(*m*, *n*)，其方程为：

F(m,n)=∑x=0M−1∑y=0N−1f(x,y)e−j2πmxMe−j2πnyN

其中 0≤m≤M−1 且 0≤n≤N−1。

该模块支持基于 FFTW 库的 FFT 实现，以及基于一组 Radix-2 算法的实现。您可以手动选择其中一种实现，或让该模块自动选择一种实现。
