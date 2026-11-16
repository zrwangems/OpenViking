---
type: simulink-block
title: 'CREPE'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Applications / Signal Processing, Audio, and Wireless / Audio Processing'
documentation_page: 'crepeblock'
documentation_source_path: '../audio/ref/crepeblock.html'
language: zh-CN
chinese_source: worker-translation
---

# CREPE

## 端口

### 输入

### **Port\_1** — 预处理后的音频输入向量 | 4-D 数组

网络的预处理输入，指定为 1024-by-1-by-1-by-*N*
数组，其中 *N* 是音频帧数。如果
输入只有一帧，则模块接受向量。

CREPE
Preprocess 模块接收音频信号并输出预处理后的帧。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 网络激活矩阵

CREPE 网络输出的网络激活，以
*N*-by-360 矩阵形式返回，其中 *N* 是
输入帧数。

CREPE
Postprocess 模块将这些网络激活转换为以 Hz 为单位的音高估计值。

**数据类型：** `single`

## 参数

### **模型容量** — 训练后的神经网络的大小 `Full`（默认值） | `Large` | `Medium` | `Small` | `Tiny`

模型容量，指定为 `Full`、
`Large`、`Medium`、
`Small` 或 `Tiny`。
较小的容量对应模型中较少的参数，从而加快计算速度，但会降低准确度。

### **小批量大小** — 小批量的大小 `128`（默认值） | 正整数

用于预测的小批量大小，指定为正
整数。较大的小批量大小需要更多内存，但可以加快预测速度。

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

- 要生成不依赖于第三方库的通用 C 代码，请在
  **Configuration Parameters** > **Code
  Generation** 常规类别中，将 **Language**
  参数设置为 `C`。
- 要生成 C++ 代码，请在 **Configuration Parameters** >
  **Code Generation** 常规类别中，将
  **Language** 参数设置为 `C++`。要
  指定代码生成的目标库，请在 **Code
  Generation** > **Interface** 类别中，设置
  **Target Library** 参数。将此参数设置为
  `None` 会生成不依赖于
  第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅支持代码生成的网络和层 (MATLAB Coder)。

## 版本历史

**R2023a 中推出**

## 描述

CREPE 深度音高估计神经网络

CREPE 模块利用预训练的卷积神经模型，从音频信号中估计
音高。此模块需要 Deep Learning Toolbox™。
