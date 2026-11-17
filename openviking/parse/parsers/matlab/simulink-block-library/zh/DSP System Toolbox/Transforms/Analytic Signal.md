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
```yaml
ports:
- name: Input
  summary: 数据输入 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Output
  summary: 解析信号输出 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 数据输入 向量 | 矩阵

将数据输入 *u* 指定为大小为 *M*×*N* 的向量或矩阵。

**数据类型：** `single` | `double`
### 输出

### **Output** — 解析信号输出 向量 | 矩阵

解析信号输出 *y*，以向量或矩阵形式返回。

该模块计算每个通道的解析信号。每个通道输出的实部是该通道实数输入的副本。输出的虚部是输入的希尔伯特变换。在频域中，解析信号的傅里叶变换将原始信号的正频率内容加倍，同时将负频率置零并保留直流分量。

输出的尺寸和数据类型与输入相同。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter order (must be even)
  summary: 滤波器阶数 100（默认）| 偶数正整数
  group: ''
- name: Input processing
  summary: 处理输入信号的方法 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
```

### **Filter order (must be even)** — 滤波器阶数 `100`（默认）| 偶数正整数

将希尔伯特 FIR 滤波器的阶数指定为偶数正整数。该 FIR 滤波器计算实数输入信号的希尔伯特变换。当滤波器阶数较低时，模块使用等波纹 FIR 滤波器来计算希尔伯特变换。对于较高的滤波器阶数，如果等波纹设计失败，模块将改用 Kaiser 窗 FIR 滤波器。

### **Input processing** — 处理输入信号的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定模块应如何处理输入。

您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  — 模块执行基于帧的处理。在此模式下，模块将 *M*×*N*
  矩阵输入视为 *N* 个独立通道，每个通道包含
  *M* 个连续时间采样。模块对每个通道随时间计算解析信号。
- `Elements as channels (sample based)`
  — 模块执行基于采样的处理。在此模式下，模块将 *M*×*N*
  矩阵输入视为 *M*\**N*
  个独立通道，并对每个通道（矩阵元素）随时间计算解析信号。
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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

Analytic Signal 模块在以下条件下支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成：

- **Input processing** 设置为 `Columns as
  channels (frame based)`。
- 输入信号必须为实值。
- 输入信号的数据类型为 `single` 或
  `double`。

SIMD 技术显著提高了生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2006a 之前推出**

### R2025a：在较高滤波器阶数下支持 Kaiser 窗 FIR 滤波器

当您指定较高的滤波器阶数时，Analytic Signal 模块使用 Kaiser 窗 FIR 滤波器来计算希尔伯特变换，从而在较高阶数下实现更稳健的滤波器设计。

## 描述

计算离散时间输入的解析信号

Analytic Signal 模块计算实数输入 *u* 的每个通道对应的复数解析信号 *y*。

y=u+jH{u},

其中 j=−1，*H*{ } 表示希尔伯特变换。

该模块使用等波纹 FIR 滤波器或 Kaiser 窗 FIR 滤波器计算希尔伯特变换。当滤波器阶数较低时，模块使用等波纹 FIR 滤波器。对于较高的滤波器阶数，如果等波纹设计失败，模块将使用 Kaiser 窗 FIR 滤波器。

该模块支持 C/C++ 代码生成和 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
