---
type: simulink-block
title: 'VGGish Embeddings'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'vggishembeddingsblock'
documentation_source_path: 'ref/vggishembeddingsblock.html'
language: zh-CN
chinese_source: worker-translation
---

# VGGish Embeddings

## 端口

### 输入

### **Port\_1** — 声音数据列向量

声音数据，指定为单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不等于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，模块将抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 长度为 128 的嵌入行向量

VGGish 特征嵌入，以长度为 128 的行向量形式返回。特征嵌入是音频数据的紧凑表示。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率（Hz） `16e3`（默认）| 正标量

输入信号的采样率（Hz），指定为正标量。

### **Overlap percentage (%)** — 连续梅尔频谱图之间的重叠百分比 `50`（默认）| [0 100)

将连续梅尔频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

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

- 要生成不依赖第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 将生成不依赖第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

## 版本历史

**在 R2022a 中引入**

## 描述

提取 VGGish 嵌入

VGGish Embeddings 模块使用 VGGish 从音频片段中提取特征嵌入。VGGish Embeddings 模块结合了必要的音频预处理和 VGGish 网络推理，并返回特征嵌入，这些嵌入是音频数据的紧凑表示。
