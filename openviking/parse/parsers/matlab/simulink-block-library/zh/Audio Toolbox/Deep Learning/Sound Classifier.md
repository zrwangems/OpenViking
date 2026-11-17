---
type: simulink-block
title: 'Sound Classifier'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'soundclassifier'
documentation_source_path: 'ref/soundclassifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Sound Classifier

## 端口

### 输入

### **audioIn** — 声音数据列向量

要分类的声音数据，指定为单通道信号（列向量）。如果 **Sample rate of input signal (Hz)** 为 16e3，则对输入帧长度没有限制。如果 **Sample rate of input signal (Hz)** 不同于 16e3，则输入帧长度必须是该模块执行的重采样操作的抽取因子的倍数。如果输入帧长度不满足此条件，该模块将抛出错误消息，其中包含有关抽取因子的信息。

**数据类型：** `single` | `double`
### 输出

### **sound** — 预测的声音标签枚举标量

预测的声音标签，以枚举标量形式返回。

**数据类型：** `enumerated`

### **scores** — 预测的激活值或分数向量

每个受支持声音标签的预测激活值或分数值，以 1×521 向量形式返回，其中 521 是 YAMNet 中的类别数。

**数据类型：** `single`

### **labels** — 预测分数的类别标签向量

预测分数的类别标签，以 1×521 向量形式返回。

**数据类型：** `enumerated`

## 参数

### **Sample rate of input signal (Hz)** — 输入信号的采样率（Hz） `16e3`（默认）| 正标量

以 Hz 为单位将输入信号的采样率指定为正标量。如果采样率不同于 16e3，则该模块会将信号重采样为 16e3，这是 YAMNet 支持的采样率。

**数据类型：** `single` | `double`

### **Overlap percentage (%)** — 连续梅尔频谱图之间的重叠百分比 `50`（默认）| [0 100)

将连续梅尔频谱图之间的重叠百分比指定为范围 [0 100) 内的标量。

**数据类型：** `single` | `double`

### **Classification** — 选择以输出声音分类 `on`（默认）| `off`

启用输出端口 **sound**，该端口输出分类后的声音。

### **Predictions** — 输出所有分数和相关标签 `off`（默认）| `on`

启用输出端口 **scores** 和 **labels**，它们输出所有预测分数和相关类别标签。

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
- 要生成 C++ 代码，请在 **Configuration Parameters** > **Code Generation** 常规类别中，将 **Language** 参数设置为 `C++`。要指定用于代码生成的目标库，请在 **Code Generation** > **Interface** 类别中，设置 **Target Library** 参数。将此参数设置为 `None` 会生成不依赖第三方库的通用 C++ 代码。
- 有关支持代码生成的网络和层的列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。

## 版本历史

**在 R2021b 中引入**

## 描述

对音频信号中的声音进行分类

Sound Classifier 模块使用 YAMNet 将音频段分类为 AudioSet 本体所描述的声音类别。Sound Classifier 模块结合了必要的音频预处理和 YAMNet 网络推理。该模块返回预测的声音标签、来自声音的预测分数以及预测分数的类别标签。
