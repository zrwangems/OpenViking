---
type: simulink-block
title: 'VGGish Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'vggishpreprocessblock'
documentation_source_path: 'ref/vggishpreprocessblock.html'
language: zh-CN
chinese_source: worker-translation
---

# VGGish Preprocess

## 端口

### 输入

### **Port\_1** — 声音数据列向量

声音数据，指定为单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 与 16e3 不同，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，该模块会抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — Mel 频谱图 96×64 矩阵

由输入音频信号生成的 Mel 频谱图，返回为 96×64 矩阵，其中：

- `96` –– 表示每个 Mel 频谱图中的 25 ms 帧数
- `64` –– 表示覆盖 125 Hz 至 7.5 kHz 的 Mel 频带数

连续 96×64 Mel 频谱图之间的重叠由 **Overlap percentage (%)** 参数的值确定。您可以将该 Mel 频谱图作为输入提供给 VGGish 预训练网络，或提供给接受与 VGGish 相同输入的网络。

**数据类型：** `single`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率，单位为 Hz `16e3`（默认值）| 正标量

输入信号的采样率，单位为 Hz，指定为正标量。

### **Overlap percentage (%)** — 连续 Mel 频谱图之间的重叠百分比 `50`（默认值）| [0 100)

将连续 Mel 频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

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

## 版本历史

**在 R2022a 中引入**

## 描述

为 VGGish 特征提取预处理音频

VGGish Preprocess 模块从音频输入生成 Mel 频谱图，然后您可以将其馈送到 VGGish 预训练网络，或馈送到接受与 VGGish 相同输入的网络。
