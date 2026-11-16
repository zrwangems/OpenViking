---
type: simulink-block
title: 'Multiband Combiner'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'multibandcombiner'
documentation_source_path: 'ref/multibandcombiner.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiband Combiner

## 端口

### 输入

### **In** — 输入信号 *N*samp×*N*chan 矩阵

输入信号，指定为 *N*samp×*N*chan 矩阵。*N*samp 是每通道的输入样本数，*N*chan 是通道数。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out** — 输出信号 *N*out×1 向量

输出信号，返回为与输入信号 `In` 具有相同数据类型的 *N*out×1 向量。*N*out 是输出样本数。**速率选项**参数指定单速率或多速率模式。有关详细信息，请参阅算法。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中选择**属性检查器**。

### **输入采样率 (Hz)** — 输入信号采样率 `1e6`（默认）| 正标量

输入信号采样率，以 Hz 为单位，指定为正标量。

### **频率偏移 (Hz)** — 频率偏移 `[0 1e6]`（默认）| 标量 | 1×*N*chan 向量

频率偏移，以 Hz 为单位，指定为以下选项之一。

- 标量 — 输入信号的每个通道都按此标量值进行频移。
- 1×*N*chan 向量 — 输入信号的每个通道都按此向量中的对应值进行频移。*N*chan 是输入信号 `In` 的通道数。

### **速率选项** — 处理速率的选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

处理速率的选项，指定为以下值之一。

- `Enforce single-rate processing` — 输出采样率必须是输入采样率的整数倍。输出中的行数大于或等于输入信号中的行数。输出帧率等于输入帧率。
- `Allow multirate processing` — 输出具有与输入相同的行数。输出帧率大于或等于输入帧率。

有关详细信息，请参阅算法部分。

### **输出采样率选项** — 输出采样率的选项 `Auto`（默认）| `Specify via property`

输出采样率的选项，指定为以下值之一。

- `Auto` — 模块对输入信号进行插值，以确保信号的最终采样率足以避免原始信号在频移以生成输出信号后其频率内容发生失真。
- `Specify via property` — 使用**输出采样率 (Hz)**参数指定输出采样率。

### **输出采样率 (Hz)** — 输出信号采样率 `3e6`（默认）| 正标量

输出信号采样率，以 Hz 为单位，指定为正标量。

#### 提示

为避免失真，请将此值指定为大于或等于自动计算的输出采样率。要确定自动计算的输出采样率，请先在**输出采样率选项**参数设置为 `Auto` 的情况下运行模块。

#### 依赖关系

要启用此参数，请将**输出采样率选项**参数设置为 `Specify via property`。

### **输出延迟 (samples)** — 输出延迟 只读：`36`（默认）| 正标量

此参数为只读。

输出延迟，以 samples 为单位，指定为正标量。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

对信号进行频移并合并

Multiband Combiner 模块对输入信号进行插值，将输入信号频移到指定的频带，然后将它们合并为单个信号。有关详细信息，请参阅算法部分。
