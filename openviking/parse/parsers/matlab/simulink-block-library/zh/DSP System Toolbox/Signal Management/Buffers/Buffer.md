---
type: simulink-block
title: 'Buffer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'buffer'
documentation_source_path: 'ref/buffer.html'
language: zh-CN
chinese_source: worker-translation
---

# Buffer

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要缓冲单通道信号，输入标量或列向量。要缓冲多通道信号，输入行向量或矩阵。要缓冲单通道信号，输入大小为 *Mi*×1 的标量或列向量，其中 *Mi* 是输入帧大小。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 向量 | 矩阵

缓冲后的输入信号，以向量或矩阵形式返回。

当输入为单通道信号时：

- 1×1（标量）— 输出为 *Mo*×1 向量。
- *Mi*×1（列向量）— 输出为 *Mo*×1 向量。

其中

- *Mi* — 输入帧大小
- *Mo* — **Output buffer size** 参数的值

输入帧周期为 *Mi* · *Tsi*，其中 *Tsi* 是输入采样周期。输出帧周期为 (Mo−L)Tsi，其中 *L* 是 **Buffer overlap** 参数的值，*T*si 是输入采样周期。当您将 **Buffer overlap** 参数设置为 *M*o – 1 时，输出帧周期等于输入采样周期。

当输入为多通道信号时：

- 1×*N* — 输出为 *Mo*×*N* 矩阵。
- *Mi*×*N* — 输出为 *Mo*×*N* 矩阵。

其中

- *N* — 信号中的通道数
- *Mi* — 输入帧周期
- *M*o 是 **Output buffer size** 参数的值，可以大于或小于输入帧大小 *Mi*。该模块独立缓冲 *N* 个输入通道中的每一个。

输入帧周期为 *Mi* · *Tsi*。输出帧周期为 (Mo−L)Tsi，当 **Buffer overlap** 为 Mo−1 时，该值等于序列采样周期。因此，输出采样周期 *Tso* 与输入采样周期 *Tsi* 的关系为

Tso=(Mo−L)TsiMi

输出的数据类型和复数性与输入相同

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Output buffer size (per channel)
  summary: 缓冲区大小 64（默认）| 正整数
  group: ''
- name: Buffer overlap
  summary: 缓冲区重叠 0（默认）| 整数
  group: ''
- name: Initial conditions
  summary: 初始输出 0（默认）| 标量 | 向量 | 矩阵
  group: ''
```

### **Output buffer size (per channel)** — 缓冲区大小 `64`（默认）| 正整数

指定要从每个通道缓冲到输出帧中的连续采样数 *Mo*。

**数据类型：** `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Buffer overlap** — 缓冲区重叠 `0`（默认）| 整数

指定采样数 *L*，它指定每个连续输出帧中的重叠量或欠重叠量。

要重叠缓冲区中的数据，请指定 *L* 的值在 0≤L<Mo 范围内，其中 *Mo* 是 **Output buffer size** 参数的值。该模块从当前输出中取 *L* 个采样（行），并在下一个输出中重复它们。在重叠的情况下，该模块在将缓冲数据传播到输出之前获取 Mo−L 个*新*输入采样。

当 L<0 时，您正在以欠重叠方式缓冲信号。该模块在缓冲区填满后丢弃 *L* 个输入采样，并以周期 (Mo−L)Tsi 输出缓冲区，该周期比零重叠情况下更长。

输出帧周期为 (Mo−L)Tsi，当 **Buffer overlap** 为 Mo−1 时，该值等于输入序列采样周期 *Tsi*。

**数据类型：** `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Initial conditions** — 初始输出 `0`（默认）| 标量 | 向量 | 矩阵

在非零延迟的情况下，将模块的初始输出值指定为标量、向量或矩阵。

对于除零任务延迟中列出的情况之外的所有单任务操作情况，Buffer 模块的缓冲区被初始化为 **Initial conditions** 参数指定的值。该模块从该缓冲区读取以生成前 *D* 个输出采样，其中

D={Mo+L(L≥0)Mo(L<0)

**Initial conditions** 参数的维度取决于 **Buffer overlap** *L* 以及输入是单通道还是多通道：

- 当 L≠0 时，**Initial conditions** 参数必须是标量。
- 当 L=0 时，**Initial conditions** 参数可以是标量，也可以是满足以下任一约束的向量：

  - 对于单通道输入，如果 *Mi* 为 1，**Initial conditions** 参数可以是长度为 *Mo* 的向量；如果 *Mo* 为 1，则可以是长度为 *Mi* 的向量。
  - 对于多通道输入，如果 *Mi* 为 1，**Initial conditions** 参数可以是长度为 *Mo* \* *N* 的向量；如果 *Mo* 为 1，则可以是长度为 *Mi* \* *N* 的向量。

对于所有多任务操作，使用 `rebuffer_delay` 函数来计算 Buffer 模块在给定缓冲区大小和缓冲区重叠组合下引入的精确采样延迟。

对于任意帧大小之间的一般缓冲，**Initial conditions** 参数必须是标量，然后该标量会在初始输出的所有元素中重复。然而，在输入为 1×*N* 行向量且模块输出为 *Mo*×*N* 矩阵的特殊情况下，**Initial conditions** 可以是：

- 一个 *Mo*×*N* 矩阵
- 一个长度为 *Mo* 的向量，在初始输出的所有列中重复
- 一个标量，在初始输出的所有元素中重复

在输出为 1×*N* 行向量的特殊情况下（这是对 *Mi*×*N* 矩阵进行解缓冲的结果），**Initial conditions** 可以是：

- 一个包含 *Mi* 个采样的向量，在前 *Mi* 个采样时间期间为每个通道依次输出
- 一个标量，在初始输出的所有元素中重复

有关延迟和 Simulink® 任务模式的更多信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 所属库

DSP System Toolbox / Signal Management / Buffers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Buffer 模块支持 Simulink Real-Time™ 的代码生成。为此目标生成的代码是并发执行的。要生成此代码，请将模型的系统目标文件设置为 `speedgoat.tlc` 或 Simulink Real-Time 支持的任何其他目标文件。Buffer 模块还需要满足某些条件。

要设置系统目标文件：

1. 在 Simulink 模型窗口中，在 **Modeling** 选项卡中，点击 **Model Settings**。
2. 在 Model Settings > **Code Generation** 窗格中，将 **System target file** 设置为 `speedgoat.tlc` 或 Simulink Real-Time 支持的任何其他目标文件。

此外，Buffer 模块必须满足以下条件：

- 输出与输入缓冲区大小之间的比率必须是纯整数，即 1/*N* 或 *N*/1。诸如 3/12、1/7、7/1 或 2/4 等比率都是有效的比率。在 Buffer 模块中，您可以使用 **Output buffer size (per channel)** 参数指定适当的输出缓冲区大小。
- 帧之间不应有重叠。在 Buffer 模块中，将 **Buffer overlap** 参数设置为 `0`。

## 版本历史

**在 R2006a 之前推出**

## 描述

将输入序列缓冲为更小或更大的帧大小

Buffer 模块始终执行基于帧的处理。该模块重新分配输入每一列中的数据，以产生具有不同帧大小的输出。将信号缓冲为更大的帧大小会产生帧速率比输入*更慢*的输出。例如，考虑以下标量输入的图示。

将信号缓冲为更小的帧大小会产生帧速率比输入*更快*的输出。例如，考虑以下标量输出的图示。

该模块协调非重叠缓冲区的输出*帧大小*和*帧速率*，使得信号在输入和输出处的采样周期相同：*Tso* = *Tsi*。

当模块输入和输出速率相同时，该模块支持触发子系统。
