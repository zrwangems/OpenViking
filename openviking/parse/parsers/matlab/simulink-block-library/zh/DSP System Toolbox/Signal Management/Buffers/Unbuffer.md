---
type: simulink-block
title: 'Unbuffer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'unbuffer'
documentation_source_path: 'ref/unbuffer.html'
language: zh-CN
chinese_source: worker-translation
---

# Unbuffer

## 端口
```yaml
ports:
- name: Input
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Output
  summary: 解缓冲后的信号 标量 | 行向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Input** — 输入信号 标量 | 向量 | 矩阵

指定要解缓冲的信号，可以是标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 解缓冲后的信号 标量 | 行向量

Unbuffer 模块将 *M*i×*N* 的输入解缓冲为 `1`×*N* 的输出。该模块按行对输入进行解缓冲，使每一矩阵行成为输出中独立的时间采样。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Initial conditions
  summary: 初始条件 0（默认） | 标量 | 向量 | 矩阵
  group: ''
```

### **Initial conditions** — 初始条件 `0`（默认） | 标量 | 向量 | 矩阵

在存在非零延迟的情况下，将模块的初始输出指定为以下之一：

- 标量，将重复用于每个通道的前 *M*i 个输出采样
- 长度为 *M*i 的向量，包含每个通道前 *M*i 个输出采样的值
- *M*i×*N* 的矩阵，包含 *N* 个通道中每个通道前 *M*i 个输出采样的值

**注意**

有关延迟和 Simulink® 任务模式的详细信息，请参阅 Excess Algorithmic Delay (Tasking Latency) 和 Time-Based Scheduling and Code Generation (Simulink Coder)。
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

Unbuffer 模块支持为 Simulink Real-Time™ 生成代码。为此目标生成的代码将并发执行。要生成此代码，请将模型的系统目标文件设置为 `speedgoat.tlc` 或 Simulink Real-Time 支持的任何其他目标文件。

要设置系统目标文件：

1. 在 Simulink 模型窗口中，在 **Modeling** 选项卡上，点击 **Model Settings**。
2. 在 Model Settings > **Code Generation** 窗格中，将 **System target file** 设置为 `speedgoat.tlc` 或 Simulink Real-Time 支持的任何其他目标文件。

## 版本历史

**在 R2006a 之前推出**

## 描述

将输入帧解缓冲为标量输出序列

Unbuffer 模块将 *M*i×*N* 的输入解缓冲为 `1`×*N* 的输出。该模块按行对输入进行解缓冲，使每一矩阵行成为输出中独立的时间采样。该模块接收输入的速率通常低于其产生输出的速率。

例如，考虑此图示。该模块仅每三个采样周期接收一次输入，但每个采样周期产生一次输出。要将输入重缓冲为更大或更小的帧大小，请使用 Buffer 模块。

该模块调整输出速率，使输入和输出处的*采样周期*相同，*T*so = *T*si。因此，对于帧大小为 *M*i、帧周期为 *T*fi 的输入，输出采样周期为 Tfi/*M*i，这表示速率比输入帧速率高 *M*i 倍。

在下图中，该模块对帧大小为三的四通道输入进行解缓冲。**Initial conditions** 参数设置为零，任务模式设置为多任务，因此前三个输出为零向量。
