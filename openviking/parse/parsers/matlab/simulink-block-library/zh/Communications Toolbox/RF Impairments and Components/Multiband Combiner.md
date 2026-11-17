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
```yaml
ports:
- name: In
  summary: 输入信号 *N*samp-by-*N*chan 矩阵
  direction: input
  data_types: double | single
- name: Out
  summary: 输出信号 *N*out-by-1 向量
  direction: output
```

### 输入

### **In** — 输入信号 *N*samp-by-*N*chan 矩阵

输入信号，指定为
*N*samp-by-*N*chan
矩阵。*N*samp 是每个通道的输入样本数，
*N*chan 是通道数。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out** — 输出信号 *N*out-by-1 向量

输出信号，返回为与输入信号 `In` 数据类型相同的 *N*out-by-1
向量。
*N*out 是输出样本数。**Rate
options** 参数指定单速率或多速率模式。有关
更多信息，请参阅算法部分。
## 参数
```yaml
parameters:
- name: Input sample rate (Hz)
  summary: 输入信号采样率 1e6（默认）| 正标量
  group: ''
- name: Frequency offsets (Hz)
  summary: 频率偏移 [0 1e6]（默认）| 标量 | 1-by-*N*chan 向量
  group: ''
- name: Rate options
  summary: 处理速率选项 Enforce single-rate processing（默认）| Allow multirate processing
  group: ''
- name: Output sample rate options
  summary: 输出采样率选项 Auto（默认）| Specify via property
  group: ''
- name: Output sample rate (Hz)
  summary: 输出信号采样率 3e6（默认）| 正标量
  group: ''
- name: Output delay (samples)
  summary: 输出延迟 只读：36（默认）| 正标量
  group: ''
```

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Input sample rate (Hz)** — 输入信号采样率 `1e6`（默认）| 正标量

输入信号采样率，以 Hz 为单位，指定为正标量。

### **Frequency offsets (Hz)** — 频率偏移 `[0 1e6]`（默认）| 标量 | 1-by-*N*chan 向量

频率偏移，以 Hz 为单位，指定为以下选项之一。

- 标量 — 输入信号的每个通道按此标量值进行频率偏移。
- 1-by-*N*chan 向量 — 输入信号的每个通道按此向量中的对应值进行频率偏移。
  *N*chan 是输入信号 `In` 中的通道数。

### **Rate options** — 处理速率选项 `Enforce single-rate processing`（默认）| `Allow multirate processing`

处理速率选项，指定为以下值之一。

- `Enforce single-rate processing` — 输出采样率
  必须是输入采样率的整数倍。输出中的行数
  大于或等于输入信号中的行数。输出帧速率
  等于输入帧速率。
- `Allow multirate processing` — 输出的行数与输入相同。
  输出帧速率大于或等于输入
  帧速率。

有关更多信息，请参阅算法部分。

### **Output sample rate options** — 输出采样率选项 `Auto`（默认）| `Specify via property`

输出采样率选项，指定为以下值之一。

- `Auto` — 该模块对输入信号进行插值，以确保
  信号的最终采样率足以避免在信号经过频率偏移
  以产生输出信号后原始信号的频率内容发生
  失真。
- `Specify via property` — 使用 **Output sample rate
  (Hz)** 参数指定输出采样率。

### **Output sample rate (Hz)** — 输出信号采样率 `3e6`（默认）| 正标量

输出信号采样率，以 Hz 为单位，指定为正标量。

#### 提示

为避免失真，请将此值指定为大于或等于
自动计算的输出采样率。要确定自动计算的
输出采样率，请先将 **Output sample rate
options** 参数设置为 `Auto` 运行该模块。

#### 依赖关系

要启用此参数，请将 **Output sample rate
options** 参数设置为 `Specify via property`。

### **Output delay (samples)** — 输出延迟 只读：`36`（默认）| 正标量

此参数为只读。

输出延迟，以样本为单位，指定为正标量。
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

对信号进行频率偏移并合并

Multiband Combiner 模块对输入信号进行插值，将其偏移到指定的频带，
然后将其合并为单个信号。有关更多信息，请参阅算法部分。
