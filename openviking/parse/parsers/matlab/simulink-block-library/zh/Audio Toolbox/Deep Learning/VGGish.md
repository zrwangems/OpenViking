---
type: simulink-block
title: 'VGGish'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'vggishblock'
documentation_source_path: 'ref/vggishblock.html'
language: zh-CN
chinese_source: worker-translation
---

# VGGish

## 端口

### 输入

### **Port\_1** — Mel 频谱图 96-by-64 矩阵 | 96-by-64-by-1-by-*N* 数组

Mel 频谱图，指定为 96-by-64 矩阵或 96-by-64-by-1-by-*N* 数组，其中：

- `96` –– 表示每个 Mel 频谱图中 25 ms 帧的数量
- `64` –– 表示覆盖 125 Hz 至 7.5 kHz 的 Mel 频带数量
- *N* –– 表示 Mel 频谱图的数量。

您可以使用 VGGish Preprocess 模块生成 Mel 频谱图。所有频谱图的维度均为 96-by-64。

**数据类型：** `single` | `double`

### 输出

### **Port\_1** — 嵌入 *N*-by-128 矩阵

VGGish 特征嵌入，以 *N*-by-128 矩阵形式返回，其中 *N* 是输入中 Mel 频谱图的数量。特征嵌入是音频数据的紧凑表示。

**数据类型：** `single`

## 参数

### **Mini-batch size** — 小批量大小 `128`（默认）| 正整数

预测时使用的小批量大小，指定为正整数。较大的小批量大小需要更多内存，但可以加快预测速度。

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

使用注意事项和限制：

- 要生成不依赖于第三方库的通用 C 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖于第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

## 版本历史

**在 R2022a 中推出**

## 描述

VGGish 嵌入提取网络

VGGish 模块利用在 AudioSet 数据集上训练的预训练卷积神经网络，从音频信号中提取特征嵌入。
