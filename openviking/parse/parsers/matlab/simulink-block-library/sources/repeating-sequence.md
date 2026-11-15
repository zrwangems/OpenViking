---
type: simulink-block
title: 'Repeating Sequence'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequence'
---

# Repeating Sequence

Generate arbitrarily shaped periodic signal

## 中文

生成任意形状的周期信号

### 所属库

Simulink / Sources

### 描述

Repeating Sequence 模块可以输出波形由**时间值**和**输出值**参数指定的周期性标量信号。**时间值**参数指定输出时间向量。**输出值**参数指定输出时间对应的信号振幅向量。这两个参数结合使用指定输出波形的重复间隔（信号周期）的各测量点确定的采样。

默认情况下，这两个参数都是 `[0 2]`。这些默认设置指定了从仿真开始每 `2` 秒重复一次，最大振幅为 `2` 的锯齿波形。

### 端口

#### 输出

#### **Port\_1** — 周期性输出信号 标量

输出由**时间值**和**输出值**参数指定的信号以创建周期性标量信号。

**数据类型:** `double`

### 参数

#### **时间值** — 输出时间的向量 `[0 2]` (默认) | 向量

严格单调递增时间值的向量。生成的波形的周期是此参数的最后一个值和第一个值之差。

##### 编程用法

|  |
| --- |
| **模块参数**：`rep_seq_t` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |

#### **输出值** — 输出值的向量 `[0 2]` (默认) | 向量

输出值的向量，用于指定输出波形。每个元素对应于**时间值**参数中的时间值。

##### 编程用法

|  |
| --- |
| **模块参数**：`rep_seq_y` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`[0 2]` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

考虑使用 Repeating Sequence Stair 或 Repeating Sequence Interpolated 模块进行代码生成。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Repeating Sequence block outputs a periodic scalar signal having a
waveform that you specify using the **Time values** and
**Output values** parameters. The **Time values**
parameter specifies a vector of output times. The **Output values**
parameter specifies a vector of signal amplitudes at the corresponding output times.
Together, the two parameters specify a sampling of the output waveform at points
measured from the beginning of the interval over which the waveform repeats (the period
of the signal).

By default, both parameters are `[0 2]`. These default settings specify a
sawtooth waveform that repeats every `2` seconds from the start of the
simulation and has a maximum amplitude of `2`.

## Ports

### Output

### **Port\_1** — Periodic output signal scalar

Output signal specified by the **Time values** and
**Output values** parameters to create a periodic
scalar signal.

**Data Types:** `double`

## Parameters

### **Time values** — Vector of output times `[0 2]` (default) | vector

Vector of strictly monotonically increasing time values. The period of the generated
waveform is the difference of the last and first values of this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rep_seq_t` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `[0 2]` |

### **Output values** — Vector of output values `[0 2]` (default) | vector

Vector of output values that specify the output waveform. Each element corresponds to the
time value in the **Time values**parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rep_seq_y` |
| **Type**: character vector |
| **Values**: vector |
| **Default**: `[0 2]` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

Consider using Repeating Sequence Stair or Repeating
Sequence Interpolated blocks for code generation.

## Version History

**Introduced before R2006a**
