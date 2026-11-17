---
type: simulink-block
title: 'CREPE'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'crepeblock'
documentation_source_path: 'ref/crepeblock.html'
language: zh-CN
chinese_source: worker-translation
---

# CREPE

## 端口
```yaml
ports:
- name: Port_1
  summary: 预处理后的音频输入向量 | 4-D 数组
  direction: input
  data_types: single | double
- name: Port_1
  summary: 网络激活矩阵
  direction: output
  data_types: single
```

### 输入

### **Port\_1** — 预处理后的音频输入向量 | 4-D 数组

网络的预处理输入，指定为 1024×1×1×*N* 数组，其中 *N* 是音频帧数。如果输入只有一帧，该模块接受向量。

CREPE Preprocess 模块接收音频信号并输出预处理后的帧。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 网络激活矩阵

CREPE 网络输出的网络激活，以 *N*×360 矩阵形式返回，其中 *N* 是输入帧数。

CREPE Postprocess 模块将这些网络激活转换为以 Hz 为单位的音高估计。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Model capacity
  summary: 训练神经网络的大小 Full（默认）| Large | Medium | Small | Tiny
  group: ''
- name: Mini-batch size
  summary: 小批量的大小 128（默认）| 正整数
  group: ''
```

### **Model capacity** — 训练神经网络的大小 `Full`（默认）| `Large` | `Medium` | `Small` | `Tiny`

模型容量，指定为 `Full`、`Large`、`Medium`、`Small` 或 `Tiny`。较小的尺寸对应模型中较少的参数，从而导致更快的计算速度但较低的准确度。

### **Mini-batch size** — 小批量的大小 `128`（默认）| 正整数

用于预测的小批量大小，指定为正整数。较大的小批量大小需要更多内存，但可以带来更快的预测速度。
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
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定代码生成的目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

## 版本历史

**在 R2023a 中引入**

## 描述

CREPE 深度音高估计神经网络

CREPE 模块利用预训练的卷积神经模型从音频信号中估计音高。该模块需要 Deep Learning Toolbox™。
