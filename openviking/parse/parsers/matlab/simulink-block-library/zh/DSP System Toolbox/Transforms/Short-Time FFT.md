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

### 输入

### **x[n]** — 输入信号 向量 | 矩阵

将时域输入信号指定为向量或矩阵。如果输入为矩阵，
模块将每一列视为独立通道。输入可以是
可变大小信号。也就是说，信号的帧大小可以
在仿真运行期间变化。通道数必须保持
不变。

如果输入为定点，则它必须为有符号整数或
具有 2 的幂斜率和零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **w[n]** — 分析窗向量 向量

将您的单通道分析窗连接到 **w[n]** 端口。对于
**分析窗长度** 参数，请输入
分析窗的长度 *W*。模块对
输入信号进行缓冲，使其帧长度为
*W*。

如果窗向量为定点，则它必须为
有符号整数或具有 2 的幂斜率和零偏置的有符号定点
值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **X[nL,k]** — 短时 FFT 输出 向量 | 矩阵

模块在此端口输出复值的单通道或多通道短时 FFT。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### **分析窗长度** — 分析窗的长度 `512`（默认值）| 大于 1 的正整数

将分析窗的帧长度指定为大于 1 的正整数。模块使用指定的
窗长度和重叠长度将输入缓冲为重叠的窗段，然后将每个重叠
段乘以窗。

### **连续窗之间的重叠（以 samples 为单位）** — 重叠长度 `384`（默认值）| 非负整数

将连续窗在每个输入信号帧中重叠的 samples 数量指定为非负整数。窗重叠可减少
数据边界处的伪影。

### **FFT 长度** — FFT 长度 `1024`（默认值）| 大于或等于 2 的正整数

输入模块对输入信号填充到的长度，指定为大于或等于 2 的正整数。
在模块对信号进行缓冲和加窗后，
它在计算 FFT 之前对信号进行零填充。此参数确定
短时快速傅里叶变换输出的长度（行数）。
FFT 长度必须大于或等于窗长度。

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

- 在某些条件下，生成的代码依赖于 `memcpy` 或
  `memset` 函数 (`string.h`)。
- 当 FFT 长度不是 2 的幂时，从此模块生成的可执行文件
  依赖于 MATLAB® 中包含的预构建动态库文件（`.dll`
  文件）。使用 `packNGo` 函数将
  从此模块生成的代码及所有相关文件打包到压缩
  zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的其他开发环境中重新定位、解包并重建您的
  项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。

  当 FFT 长度是 2 的幂时，您可以从此模块生成独立的 C 和
  C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用短时快速傅里叶变换 (STFT) 方法的频谱非参数估计

Short-Time FFT 模块计算频谱的非参数估计。该模块
对输入信号进行缓冲、加窗和零填充。然后，该模块对
信号进行 FFT，将其变换到频域。
