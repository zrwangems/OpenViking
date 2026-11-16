---
type: simulink-block
title: 'OpenL3 Embeddings'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'openl3embeddingsblock'
documentation_source_path: '../audio/ref/openl3embeddingsblock.html'
language: zh-CN
chinese_source: worker-translation
---

# OpenL3 Embeddings

## 端口

### 输入

### **Port\_1** — 声音数据列向量

声音数据，指定为单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 48e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不同于 48e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的整数倍。如果输入帧长度不满足此条件，该模块将抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 嵌入行向量

输出嵌入，以行向量形式返回，其长度由 **Embedding length** 参数指定。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率（以 Hz 为单位） `48e3`（默认值）| 正标量

输入信号的采样率（以 Hz 为单位），指定为正标量。

### **Overlap percentage (%)** — 连续频谱图之间的重叠百分比 `90`（默认值）| [0 100)

将连续频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

### **Spectrum type** — 频谱类型 `Mel (128 bands)`（默认值）| `Mel (256 bands)` | `Linear`

从音频生成并用作神经网络输入的频谱类型，指定为 `Mel (128 bands)`、`Mel (256 bands)` 或 `Linear`。

- `Mel (128 bands)` –– 神经网络接受由输入音频生成的、具有 128 个 mel 频带的 mel 频谱图。
- `Mel (256 bands)` –– 神经网络接受由输入音频生成的、具有 256 个 mel 频带的 mel 频谱图。
- `Linear` –– 神经网络接受由输入音频生成的正单边频谱图，其 FFT 长度为 257。

### **Content type** — 音频内容类型 `Environmental sounds`（默认值）| `Musical sounds`

神经网络训练所用的音频内容类型，指定为 `Environmental sounds` 或 `Musical sounds`。将此参数设置为 `Environmental sounds` 可使用在环境音频数据上预训练的神经网络，将其设置为 `Musical sounds` 可使用在音乐数据上预训练的网络。

### **Embedding length** — 输出嵌入长度 `512`（默认值）| `6144`

输出嵌入的长度，指定为 `512` 或 `6144`。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅支持代码生成的网络和层 (MATLAB Coder)。

## 版本历史

**在 R2022b 中推出**

## 描述

提取 OpenL3 嵌入

OpenL3 Embeddings 模块使用 OpenL3 从音频信号中提取特征嵌入。OpenL3 Embeddings 模块将必要的音频预处理与 OpenL3 网络推理相结合，并返回作为音频数据紧凑表示的特征嵌入。此模块需要 Deep Learning Toolbox™。
