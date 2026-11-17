---
type: simulink-block
title: 'Short-Time FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'shorttimefft'
documentation_source_path: 'ref/shorttimefft.html'
language: zh-CN
chinese_source: worker-translation
---

# Short-Time FFT

## 端口
```yaml
ports:
- name: x[n]
  summary: 输入信号 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: w[n]
  summary: 分析窗向量 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: X[nL,k]
  summary: 短时 FFT 输出 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **x[n]** — 输入信号 向量 | 矩阵

将时域输入信号指定为向量或矩阵。如果输入是矩阵，模块将每一列视为独立通道。输入可以是可变大小信号。也就是说，信号的帧大小可以在仿真运行期间变化。通道数必须保持不变。

如果输入是定点类型，它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **w[n]** — 分析窗向量 向量

将您的单通道分析窗连接到 **w[n]** 端口。对于 **Analysis window length** 参数，输入分析窗的长度 *W*。模块对输入信号进行缓冲，使其帧长度为 *W*。

如果窗向量是定点类型，它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **X[nL,k]** — 短时 FFT 输出 向量 | 矩阵

模块在此端口输出复值单通道或多通道短时 FFT。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Analysis window length
  summary: 分析窗长度 512（默认）| 大于 1 的正整数
  group: ''
- name: Overlap between consecutive windows (in samples)
  summary: 重叠长度 384（默认）| 非负整数
  group: ''
- name: FFT length
  summary: FFT 长度 1024（默认）| 大于或等于 2 的正整数
  group: ''
```

### **Analysis window length** — 分析窗长度 `512`（默认）| 大于 1 的正整数

将分析窗的帧长度指定为大于 1 的正整数。模块使用指定的窗长度和重叠长度将输入缓冲为重叠的窗段，然后将每个重叠段乘以窗。

### **Overlap between consecutive windows (in samples)** — 重叠长度 `384`（默认）| 非负整数

将输入信号每一帧中连续窗重叠的样本数指定为非负整数。窗重叠可减少数据边界处的伪影。

### **FFT length** — FFT 长度 `1024`（默认）| 大于或等于 2 的正整数

输入模块对输入信号进行填充的长度，为大于或等于 2 的正整数。在模块对信号进行缓冲和加窗后，它在计算 FFT 之前对信号进行零填充。此参数决定短时快速傅里叶变换输出的长度（行数）。FFT 长度必须大于或等于窗长度。
## 所属库

DSP System Toolbox / Transforms

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

- 生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。
- 当 FFT 长度不是 2 的幂时，从此模块生成的可执行文件依赖于 MATLAB® 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。

  当 FFT 长度是 2 的幂时，您可以从此模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用短时快速傅里叶变换 (STFT) 方法进行频谱的非参数估计

Short-Time FFT 模块计算频谱的非参数估计。该模块对输入信号进行缓冲、加窗和零填充。然后模块对信号进行 FFT，将其变换到频域。
