---
type: simulink-block
title: 'Deep Pitch Estimator'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'deeppitchestimator'
documentation_source_path: '../audio/ref/deeppitchestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Pitch Estimator

## 端口

### 输入

### **Port\_1** — 音频输入向量

音频输入，指定为单通道信号（向量）。如果 **输入信号的采样率 (Hz)** 为 16e3，则输入帧长度没有限制。如果 **输入信号的采样率 (Hz)** 不等于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，模块将生成错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`

### 输出

### **Port\_1** — 估计的基频列向量

以 Hz 为单位的估计基频，返回为 *N*×1 向量，其中 *N* 是由 **缓冲的音高估计数** 指定的音高估计数。

**数据类型：** `single`

## 参数

### **输入信号的采样率 (Hz)** — 输入信号的采样率，单位为 Hz `16e3`（默认值）| 正标量

输入信号的采样率，单位为 Hz，指定为正标量。

### **重叠百分比 (%)** — 连续帧之间的重叠百分比 `85`（默认值）| [0, 100)

将连续输入帧之间的重叠百分比指定为范围 [0, 100) 内的标量。

### **缓冲的音高估计数** — 输出中的音高估计数 `1`（默认值）| 正整数

输出中的音高估计数，指定为正整数。

较高的值允许模块通过并行处理多个音频帧来提高计算效率。但是，由于模块在返回指定数量的音高估计之前会缓冲这些估计，因此它也会增加延迟。

### **置信度阈值** — 音高置信度阈值 `0.5`（默认值）| [0, 1) 范围内的标量

音高置信度阈值，指定为范围 [0, 1) 内的标量。在后处理中，模块会抑制网络置信度低于该阈值的基频。

**注意**

如果网络输出的最大值小于置信度阈值，模块将返回 `NaN`。

### **模型容量** — 训练后的神经网络的大小 `Full`（默认值）| `Large` | `Medium` | `Small` | `Tiny`

模型容量，指定为 `Full`、`Large`、`Medium`、`Small` 或 `Tiny`。较小的尺寸对应于模型中较少的参数，从而计算更快，但精度更低。

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

- 要生成不依赖第三方库的通用 C 代码，请在 **配置参数** > **代码生成** 常规类别中，将 **语言** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **配置参数** > **代码生成** 常规类别中，将 **语言** 参数设置为 `C++`。要为代码生成指定目标库，请在 **代码生成** > **接口** 类别中，设置 **目标库** 参数。将此参数设置为 `None` 会生成不依赖第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅支持代码生成的网络和层 (MATLAB Coder)。

## 版本历史

**在 R2023a 中引入**

## 描述

使用 CREPE 深度学习神经网络估计音高

Deep Pitch Estimator 模块使用 CREPE 预训练神经网络从音频信号中估计音高。该模块组合了必要的音频预处理、网络推理以及网络输出的后处理，以返回以 Hz 为单位的音高估计。此模块需要 Deep Learning Toolbox™。
