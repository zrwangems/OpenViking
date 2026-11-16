---
type: simulink-block
title: 'Analytic Signal'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'analyticsignal'
documentation_source_path: 'ref/analyticsignal.html'
language: zh-CN
chinese_source: worker-translation
---

# Analytic Signal

## 端口

### Input

### **Input** — 数据输入向量 | 矩阵

将数据输入 *u* 指定为大小为 *M*×*N* 的向量或矩阵。

**数据类型：** `single` | `double`
### Output

### **Output** — 解析信号输出向量 | 矩阵

解析信号输出 *y*，以向量或矩阵形式返回。

该模块为每个通道计算解析信号。每个通道输出的实部是该通道实数输入的副本。输出的虚部是输入的 Hilbert 变换。在频域中，解析信号的 Fourier 变换会将原始信号的正频率内容加倍，同时将负频率置零并保留 DC 分量。

输出与输入具有相同的大小和数据类型。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

### **滤波器阶数（必须为偶数）** — 滤波器阶数 `100`（默认） | 偶数正整数

将 Hilbert FIR 滤波器的阶数指定为偶数正整数。该 FIR 滤波器计算实数输入信号的 Hilbert 变换。当滤波器阶数较低时，该模块使用等波纹 FIR 滤波器来计算 Hilbert 变换。对于较高的滤波器阶数，如果等波纹设计失败，则该模块改用 Kaiser 窗 FIR 滤波器。

### **输入处理** — 处理输入信号的方法 `Columns as channels (frame based)`（默认） | `Elements as channels (sample based)`

指定该模块应如何处理输入。

您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  — 该模块执行基于帧的处理。在此模式下，
  该模块将 *M*×*N*
  矩阵输入视为 *N* 个独立通道，其中包含
  *M* 个顺序时间样本。该模块
  随时间计算每个通道的解析信号。
- `Elements as channels (sample based)`
  — 该模块执行基于样本的处理。在此模式下，
  该模块将 *M*×*N*
  矩阵输入视为 *M*\**N*
  个独立通道，并随时间计算每个
  通道（矩阵元素）的解析信号。

## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

在这些条件下，Analytic Signal 模块支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成：

- **输入处理** 设置为 `Columns as channels (frame based)`。
- 输入信号必须为实值。
- 输入信号的数据类型为 `single` 或 `double`。

SIMD 技术可显著提高生成代码的性能。有关详细信息，请参阅 SIMD 代码生成。要从该模块生成 SIMD 代码，请参阅使用 Intel AVX2 代码替换库从 Simulink 模块生成 SIMD 代码。

## 版本历史

**在 R2006a 之前引入**

### R2025a：在更高滤波器阶数下支持 Kaiser 窗 FIR 滤波器

当您指定更高的滤波器阶数时，Analytic Signal 模块使用 Kaiser 窗 FIR 滤波器来计算 Hilbert 变换，从而在更高阶数下获得更稳健的滤波器设计。

## 描述

计算离散时间输入的解析信号

Analytic Signal 模块为实数输入 *u* 的每个通道计算复数解析信号 *y*。

y=u+jH{u},

其中 j=−1，*H*{ } 表示 Hilbert 变换。

该模块使用等波纹 FIR 滤波器或 Kaiser 窗 FIR 滤波器计算 Hilbert 变换。当滤波器阶数较低时，该模块使用等波纹 FIR 滤波器。对于较高的滤波器阶数，如果等波纹设计失败，则该模块使用 Kaiser 窗 FIR 滤波器。

该模块支持 C/C++ 代码生成和 SIMD 代码生成。有关详细信息，请参阅代码生成。
