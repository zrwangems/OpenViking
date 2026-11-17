---
type: simulink-block
title: 'OpenL3 Preprocess'
family: 'deep-learning'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'openl3preprocessblock'
documentation_source_path: 'ref/openl3preprocessblock.html'
language: zh-CN
chinese_source: worker-translation
---

# OpenL3 Preprocess

## 端口

### 输入

### **Port\_1** — 声音数据列向量

声音数据，指定为一个单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 48e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不同于 48e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，模块将抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`

### 输出

### **Port\_1** — 频谱图矩阵

由输入音频生成的频谱图，返回为矩阵，其大小取决于 **Spectrum type** 参数的值。

- `Mel (128 bands)` –– 该模块返回大小为 128×199 的 mel 频谱图，其中 128 是 mel 频带的数量，199 是时间跳数。
- `Mel (256 bands)` –– 该模块返回大小为 256×199 的 mel 频谱图，其中 256 是 mel 频带的数量，199 是时间跳数。
- `Linear` –– 该模块返回大小为 257×197 的正单边频谱图，其中 257 是 FFT 长度，197 是时间跳数。

您可以将此频谱图用作 OpenL3 模块的输入，该模块具有相同的 **Spectrum type**。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率，以 Hz 为单位 `48e3` （默认值） | 正标量

输入信号的采样率，以 Hz 为单位，指定为正标量。

### **Overlap percentage (%)** — 连续频谱图之间的重叠百分比 `90` （默认值） | [0 100)

将连续频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

### **Spectrum type** — 频谱类型 `Mel (128 bands)` （默认值） | `Mel (256 bands)` | `Linear`

由输入音频生成的频谱类型，指定为 `Mel (128 bands)`、`Mel (256 bands)` 或 `Linear`。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

为 OpenL3 嵌入提取预处理音频

OpenL3 Preprocess 模块从音频输入生成频谱图。然后，您可以将这些频谱图馈送到 OpenL3 预训练网络，或馈送到接受与 OpenL3 相同输入的网络。
