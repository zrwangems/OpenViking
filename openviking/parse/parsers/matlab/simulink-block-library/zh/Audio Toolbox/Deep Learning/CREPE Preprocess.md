---
type: simulink-block
title: 'CREPE Preprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'crepepreprocessblock'
documentation_source_path: 'ref/crepepreprocessblock.html'
language: zh-CN
chinese_source: worker-translation
---

# CREPE Preprocess

## 端口
```yaml
ports:
- name: Port_1
  summary: 音频输入向量
  direction: input
  data_types: single | double
- name: Port_1
  summary: 预处理后的音频帧 4 维数组
  direction: output
  data_types: single
```

### 输入

### **Port\_1** — 音频输入向量

音频输入，指定为单通道信号（向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不等于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，该模块将生成一条错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 预处理后的音频帧 4 维数组

用于 CREPE 神经网络的预处理音频帧，返回为 1024×1×1×*N* 数组，其中 *N* 是由 **Number of output frames** 指定的生成帧数。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: 输入信号的采样率（Hz） 16e3（默认）| 正标量
  group: ''
- name: Overlap percentage (%)
  summary: 连续帧之间的重叠百分比 85（默认）| [0, 100)
  group: ''
- name: Number of output frames
  summary: 生成的帧数 1（默认）| 正整数
  group: ''
```

### **Sample rate of input signal (Hz)** — 输入信号的采样率（Hz） `16e3`（默认）| 正标量

输入信号的采样率（Hz），指定为正标量。

### **Overlap percentage (%)** — 连续帧之间的重叠百分比 `85`（默认）| [0, 100)

将连续帧之间的重叠百分比指定为范围 [0, 100) 内的标量。

### **Number of output frames** — 生成的帧数 `1`（默认）| 正整数

输出中生成的帧数，指定为正整数。
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

**在 R2023a 中引入**

## 描述

为 CREPE 深度音高估计预处理音频

CREPE Preprocess 模块从输入音频信号生成帧，您可以将其馈送到 CREPE 预训练网络或接受与 CREPE 相同输入的网络。
