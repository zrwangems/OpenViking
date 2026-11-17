---
type: simulink-block
title: 'YAMNet Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'yamnetpreprocessblock'
documentation_source_path: 'ref/yamnetpreprocessblock.html'
language: zh-CN
chinese_source: worker-translation
---

# YAMNet Preprocess

## 端口
```yaml
ports:
- name: audioIn
  summary: 声音数据列向量
  direction: input
  data_types: single | double
- name: features
  summary: 可馈送到 YAMNet 预训练网络的梅尔频谱图 96×64 矩阵
  direction: output
  data_types: single
```

### 输入

### **audioIn** — 声音数据列向量

要分类的声音数据，指定为单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不等于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，该模块将抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **features** — 可馈送到 YAMNet 预训练网络的梅尔频谱图 96×64 矩阵

从 **audioIn** 生成的梅尔频谱图，以 96×64 矩阵形式返回，其中：

- `96` —— 表示每个梅尔频谱图中 25 ms 帧的数量
- `64` —— 表示跨越 125 Hz 到 7.5 kHz 的梅尔频带数量

连续 96×64 梅尔频谱图之间的重叠由 **Overlap percentage (%)** 参数的值决定。

每个 96×64 矩阵表示单个梅尔频谱图。有关此模块如何生成梅尔频谱图的更多详细信息，请参阅算法。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: 输入信号的采样率（以 Hz 为单位） 16e3（默认）| 正标量
  group: ''
- name: Overlap percentage (%)
  summary: 连续梅尔频谱图之间的重叠百分比 50（默认）| [0 100)
  group: ''
```

### **Sample rate of input signal (Hz)** — 输入信号的采样率（以 Hz 为单位） `16e3`（默认）| 正标量

输入信号的采样率（以 Hz 为单位），指定为正标量。

**数据类型：** `single` | `double`

### **Overlap percentage (%)** — 连续梅尔频谱图之间的重叠百分比 `50`（默认）| [0 100)

将连续梅尔频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

**数据类型：** `single` | `double`
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

**在 R2021b 中引入**

## 描述

为 YAMNet 分类预处理音频

YAMNet Preprocess 模块从音频输入生成梅尔频谱图，这些频谱图可以馈送到 YAMNet 预训练网络或接受与 YAMNet 相同输入的网络。
