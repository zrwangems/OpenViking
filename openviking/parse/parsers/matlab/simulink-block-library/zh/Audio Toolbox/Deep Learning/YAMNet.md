---
type: simulink-block
title: 'YAMNet'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'yamnetblock'
documentation_source_path: 'ref/yamnetblock.html'
language: zh-CN
chinese_source: worker-translation
---

# YAMNet

## 端口

### 输入

### **features** — 梅尔频谱图 96×64 矩阵 | 96×64×1×*N* 数组

梅尔频谱图，指定为 96×64 矩阵或 96×64×1×*N* 数组，其中：

- `96` —— 表示每个梅尔频谱图中 25 ms 帧的数量
- `64` —— 表示覆盖 125 Hz 至 7.5 kHz 的梅尔频带数量
- *N* —— 通道数。

您可以使用 YAMNet Preprocess 模块生成梅尔频谱图。这些频谱图的维度为 96×64。

**数据类型：** `single` | `double`
### 输出

### **sound** — 预测的声音标签 枚举标量

预测的声音标签，以枚举标量形式返回。

**数据类型：** `enumerated`

### **scores** — 预测的激活值或分数 向量

每个支持的声音标签的预测激活值或分数值，以 1×521 向量形式返回，其中 521 是 YAMNet 中的类别数。

**数据类型：** `single`

### **labels** — 预测分数的类别标签 向量

预测分数的类别标签，以 1×521 向量形式返回。

**数据类型：** `enumerated`

## 参数

### **Mini-batch size** — 小批量大小 `128`（默认）| 正整数

用于预测的小批量大小，指定为正整数。较大的小批量大小需要更多内存，但可以加快预测速度。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Classification** — 选择输出声音分类 `on`（默认）| `off`

启用输出端口 **sound**，该端口输出分类的声音。

### **Predictions** — 输出所有分数和相关标签 `off`（默认）| `on`

启用输出端口 **scores** 和 **labels**，这些端口输出所有预测分数和相关类别标签。

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

**在 R2021b 中引入**

## 描述

YAMNet 声音分类网络

YAMNet 模块利用一个预训练的声音分类网络，该网络在 AudioSet 数据集上训练，用于根据 AudioSet 本体预测音频事件。
