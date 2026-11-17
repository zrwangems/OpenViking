---
type: simulink-block
title: 'Deep Pitch Estimator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'deeppitchestimator'
documentation_source_path: 'ref/deeppitchestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Pitch Estimator

## 端口

### 输入

### **Port\_1** — 音频输入向量

音频输入，指定为单通道信号（向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不等于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，该模块将生成一条错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 估计的基频列向量

以 Hz 为单位的估计基频，返回为 *N*×1 向量，其中 *N* 是由 **Number of buffered pitch estimations** 指定的音高估计数量。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率（Hz） `16e3`（默认）| 正标量

输入信号的采样率（Hz），指定为正标量。

### **Overlap percentage (%)** — 连续帧之间的重叠百分比 `85`（默认）| [0, 100)

将连续输入帧之间的重叠百分比指定为范围 [0, 100) 内的标量。

### **Number of buffered pitch estimations** — 输出中的音高估计数量 `1`（默认）| 正整数

输出中的音高估计数量，指定为正整数。

较高的值允许该模块通过并行处理多个音频帧来提高计算效率。但是，这也会增加延迟，因为该模块会缓冲指定数量的音高估计，然后才返回它们。

### **Confidence threshold** — 音高置信度阈值 `0.5`（默认）| 范围 [0, 1) 内的标量

音高置信度阈值，指定为范围 [0, 1) 内的标量。在后处理中，该模块会抑制网络置信度低于阈值的基频。

**注意**

如果网络输出的最大值小于置信度阈值，该模块将返回 `NaN`。

### **Model capacity** — 训练神经网络的大小 `Full`（默认）| `Large` | `Medium` | `Small` | `Tiny`

模型容量，指定为 `Full`、`Large`、`Medium`、`Small` 或 `Tiny`。较小的尺寸对应于模型中较少的参数，从而导致计算更快但精度更低。

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
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 将生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

## 版本历史

**在 R2023a 中引入**

## 描述

使用 CREPE 深度学习神经网络估计音高

Deep Pitch Estimator 模块使用 CREPE 预训练神经网络从音频信号中估计音高。该模块结合必要的音频预处理、网络推理和网络输出后处理，以 Hz 为单位返回音高估计。此模块需要 Deep Learning Toolbox™。
