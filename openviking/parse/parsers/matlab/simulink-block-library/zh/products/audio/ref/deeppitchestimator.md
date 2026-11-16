---
type: simulink-block
title: 'Deep Pitch Estimator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Pretrained Models / CREPE'
documentation_page: 'deeppitchestimator'
documentation_source_path: 'ref/deeppitchestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Pitch Estimator

## 端口

### 输入

### **Port\_1** — 音频输入向量

音频输入，指定为单通道信号（向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不同于 16e3，则输入帧长度必须是模块执行的重采样操作的抽取因子的整数倍。如果输入帧长度不满足此条件，模块将生成一条错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 估计的基频列向量

估计的基频，以 Hz 为单位，返回为 *N*×1 向量，其中 *N* 是由 **Number of buffered pitch estimations** 指定的音高估计数量。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率，单位为 Hz `16e3` (默认) | 正标量

输入信号的采样率，以 Hz 为单位，指定为正标量。

### **Overlap percentage (%)** — 连续帧之间的重叠百分比 `85` (默认) | [0, 100)

将连续输入帧之间的重叠百分比指定为 [0, 100) 范围内的标量。

### **Number of buffered pitch estimations** — 输出中的音高估计数量 `1` (默认) | 正整数

输出中的音高估计数量，指定为正整数。

较大的值允许模块通过并行处理多个音频帧来提高计算效率。但是，这也会增加延迟，因为模块会先缓冲指定数量的音高估计值，然后再返回这些估计值。

### **Confidence threshold** — 音高置信度阈值 `0.5` (默认) | [0, 1) 范围内的标量

音高置信度阈值，指定为 [0, 1) 范围内的标量。在后处理中，模块会抑制网络置信度低于该阈值的基频。

**注意**

如果网络输出的最大值小于置信度阈值，模块将返回 `NaN`。

### **Model capacity** — 经过训练的神经网络的大小 `Full` (默认) | `Large` | `Medium` | `Small` | `Tiny`

模型容量，指定为 `Full`、`Large`、`Medium`、`Small` 或 `Tiny`。较小的模型大小对应模型中较少的参数，因此计算速度更快，但精度较低。

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

使用说明和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在
  **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language**
  参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** >
  **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅代码生成支持的网络和层 (MATLAB Coder)。

## 版本历史

**在 R2023a 中推出**

## 描述

使用 CREPE 深度学习神经网络估计音高

Deep Pitch Estimator 模块使用 CREPE 预训练神经网络来估计音频信号的音高。该模块将必要的音频预处理、网络推理和网络输出后处理相结合，返回以 Hz 为单位的音高估计值。此模块需要 Deep Learning Toolbox™。
