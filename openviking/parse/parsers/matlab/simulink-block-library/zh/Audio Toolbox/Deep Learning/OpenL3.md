---
type: simulink-block
title: 'OpenL3'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'openl3block'
documentation_source_path: 'ref/openl3block.html'
language: zh-CN
chinese_source: worker-translation
---

# OpenL3

## 端口

### 输入

### **Port\_1** — 频谱图矩阵 | 4 维数组

从音频生成的频谱图，指定为 *N*-by-*M* 矩阵或 *N*-by-*M*-by-1-by-*K* 数组。*K* 表示频谱图的数量，*N*-by-*M* 是频谱图的大小，具体取决于 **Spectrum type** 参数的值。

- `Mel (128 bands)` –– 网络接受大小为 128-by-199 的 mel 频谱图，其中 128 是 mel 频带数，199 是时间跳数。
- `Mel (256 bands)` –– 网络接受大小为 256-by-199 的 mel 频谱图，其中 256 是 mel 频带数，199 是时间跳数。
- `Linear` –– 网络接受大小为 257-by-197 的正单边频谱图，其中 257 是 FFT 长度，197 是时间跳数。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 嵌入矩阵

输出嵌入，以 *K*-by-*L* 矩阵的形式返回，其中 *K* 是输入频谱图的数量，*L* 由 **Embedding length** 参数指定。

**数据类型：** `single`

## 参数

### **Spectrum type** — 频谱类型 `Mel (128 bands)` (默认) | `Mel (256 bands)` | `Linear`

从音频生成并用作神经网络输入的频谱类型，指定为 `Mel (128 bands)`、`Mel (256 bands)` 或 `Linear`。此参数指定网络输入 Port\_1 的大小。

### **Content type** — 音频内容类型 `Environmental sounds` (默认) | `Musical sounds`

神经网络训练所用的音频内容类型，指定为 `Environmental sounds` 或 `Musical sounds`。将此参数设置为 `Environmental sounds` 可使用基于环境音频数据预训练的神经网络，将其设置为 `Musical sounds` 可使用基于音乐数据预训练的网络。

### **Embedding length** — 输出嵌入长度 `512` (默认) | `6144`

输出嵌入的长度，指定为 `512` 或 `6144`。

### **Mini-batch size** — 小批量大小 `128` (默认) | 正整数

用于预测的小批量的大小，指定为正整数。较大的小批量需要更多内存，但可以加快预测速度。

## 所属库

Audio Toolbox / Deep Learning

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用注意事项和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 的常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 的常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中设置 **Target Library** 参数。将此参数设置为 `None` 可生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅“支持代码生成的网络和层 (MATLAB Coder)”。

## 版本历史

**在 R2022b 中推出**

## 描述

OpenL3 嵌入提取网络

OpenL3 模块利用预训练的卷积神经网络，从音频信号中提取特征嵌入。这些嵌入是强大的音频表示，可用于分类等任务。此模块需要 Deep Learning Toolbox™。
