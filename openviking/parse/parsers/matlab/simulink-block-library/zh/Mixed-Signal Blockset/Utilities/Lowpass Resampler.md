---
type: simulink-block
title: 'Lowpass Resampler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'lowpassresampler'
documentation_source_path: 'ref/lowpassresampler.html'
language: zh-CN
chinese_source: worker-translation
---

# Lowpass Resampler

## 端口
```yaml
ports:
- name: in
  summary: 离散时间输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: out
  summary: 连续时间输出信号 标量
  direction: output
  data_types: single | double
```

### 输入

### **in** — 离散时间输入信号 标量

离散时间输入信号，指定为固定步长或可变步长标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **out** — 连续时间输出信号 标量

连续时间输出信号，返回为固定步长或可变步长标量。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Inherit output rise/fall time
  summary: 从固定步长输入采样时间继承输出上升/下降时间 on（默认）| off
  group: ''
- name: Output rise/fall time
  summary: 20%−80% 输出上升/下降时间 1e-10（默认）| 正实数标量
  group: ''
  block_parameter: OutputRiseFall
  type: 字符向量
  values: 正实数标量
- name: Number of samples of delay
  summary: 固定步长操作的传播延迟采样数 1（默认）| 正实数标量
  group: ''
  block_parameter: NDelay
  type: 字符向量
  values: 正实数标量
- name: Output sample time
  summary: 输出采样时间的类型 Inherited（默认）| Fixed step discrete | Variable step discrete
  group: ''
  block_parameter: OutputTsType
  type: 字符向量
  values: Fixed step discrete | Variable step discrete
- name: Samples out per rise/fall time
  summary: 单个输出上升/下降时间内的输出采样数 5（默认）| 正实数标量
  group: ''
  block_parameter: OutputTsRatio
  type: 字符向量
  values: 正实数标量
- name: Enable large buffer
  summary: 启用额外缓冲区采样 on（默认）| off
  group: ''
- name: 额外缓冲区采样数
  summary: 用于支持采样延迟的额外缓冲区采样数 10（默认）| 正实数标量
  group: ''
  block_parameter: NBuffer
  type: 字符向量
  values: 正实数标量
```

### **Inherit output rise/fall time** — 从固定步长输入采样时间继承输出上升/下降时间 on（默认）| off

选择以从固定步长输入采样时间继承输出上升/下降时间。

**注意**

在可变步长输入的情况下，没有可继承的上升/下降时间。

### **Output rise/fall time** — 20%−80% 输出上升/下降时间 `1e-10`（默认）| 正实数标量

20%−80% 输出上升/下降时间，指定为正实数标量。

#### 依赖

要启用此参数，请取消选择 **Inherit output rise/fall time** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputRiseFall` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1e-10` |

### **Number of samples of delay** — 固定步长操作的传播延迟采样数 `1`（默认）| 正实数标量

固定步长操作的传播延迟采样数，指定为正实数标量。

如果 Lowpass Resampler 模块在固定步长模式下继承 **Output rise/fall time**，则重采样器转换延迟由 *NDelay*·*τ* 给出，其中 *NDelay* 是 **Number of samples of delay** 参数，*τ* 是继承的输入采样间隔。

在可变步长输入模式下，当 *NDelay* 等于 1 时，重采样器转换延迟由 0.6*τv* 给出；当 *NDelay* 大于 1 时，由 (*NDelay*-0.5)·*τv* 给出。*τv* 是 **Output rise/fall time** 参数的 5/3 倍。

转换延迟与带外数值伪影的抑制之间存在权衡，较大的延迟在带内产生更好的保真度，并在带外产生更大的抑制。

**注意**

如果需要抗混叠滤波器抑制，请将 **Number of samples of delay** 设置为 5 或更高。

#### 依赖

要启用此参数，请取消选择 **Inherit output rise/fall time** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `NDelay` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `1` |

### **Output sample time** — 输出采样时间的类型 `Inherited`（默认）| `Fixed step discrete` | `Variable step discrete`

下游模块要使用的输出采样时间的类型，指定为固定步长离散或可变步长离散。输出采样率必须高于输入采样率。有关详细信息，请参阅 Variable Step Sampling Scheme。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputTsType` |
| **类型：** 字符向量 |
| **值：** `Fixed step discrete` | `Variable step discrete` |
| **默认：** `Inherited` |

### **Samples out per rise/fall time** — 单个输出上升/下降时间内的输出采样数 `5`（默认）| 正实数标量

单个输出上升/下降时间内的输出采样数，指定为正实数标量。

#### 依赖

要启用此参数，请在 **Output sample time** 参数中选择 `Fixed step discrete` 或 `Variable step discrete` 选项。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputTsRatio` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `5` |

### **Enable large buffer** — 启用额外缓冲区采样 on（默认）| off

选择以启用额外缓冲区采样。此选项默认启用。

### **额外缓冲区采样数** — 用于支持采样延迟的额外缓冲区采样数 `10`（默认）| 正实数标量

支持延迟采样数所需的额外缓冲区采样数，指定为正实数标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `10` |
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

### R2022a：在 R2022a 中更新

Lowpass Resampler 可以定义自己的输出采样时间。

### R2021a：在 R2021a 中引入

用于更改信号的采样时间。

## 描述

将信号从一个采样时间转换为另一个采样时间

Lowpass Resampler 模块将其输入端的定步离散或变步离散采样时间转换为输出端的不同采样时间。为了计算输出采样值，该模块使用低通滤波插值算法。该算法相对于输出上升/下降时间最小化输出端的频率混叠。

如果输出上升/下降时间继承自定步离散输入，则截止频率为输入的奈奎斯特频率。否则，截止频率为与采样间隔相关联的奈奎斯特频率，该采样间隔通过将指定的 20%−80% 输出上升/下降时间缩放为 0%−100% 上升/下降时间的值而获得。
