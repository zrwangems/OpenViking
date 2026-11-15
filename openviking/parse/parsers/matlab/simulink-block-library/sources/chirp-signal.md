---
type: simulink-block
title: 'Chirp Signal'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'chirpsignal'
---

# Chirp Signal

Generate sine wave with increasing frequency

## 中文

生成频率不断增加的正弦波

### 所属库

Simulink / Sources

### 描述

Chirp Signal 模块生成频率随时间按线性速率增加的正弦波。您可以使用此模块对非线性系统进行频谱分析。模块生成标量或向量输出。

参数**初始频率**、**目标时间**和**目标时间的频率**决定模块的输出。您可以将任何或所有这些变量指定为标量或数组。指定为数组的所有参数都必须具有相同的维度。模块会扩展标量参数，使其与数组参数具有相同的维度。模块输出与参数具有相同的维度，除非您选中了**将向量参数解释为一维向量**复选框。如果选中此复选框且参数为行或列向量，则模块将输出向量（一维数组）信号。

### 端口

#### 输出

#### **Port\_1** — 啁啾信号 标量 | 向量 | 矩阵 | N 维数组

频率随时间按线性速率增加的正弦波。啁啾信号可以是标量、向量、矩阵或 N 维数组。

**数据类型:** `double`

### 参数

#### **初始频率** — 初始频率(Hz) `0.1` (默认) | 标量 | 向量 | 矩阵 | N 维数组

信号的初始频率，指定为标量、向量、矩阵或 N 维数组。

##### 编程用法

|  |
| --- |
| **模块参数**：`f1` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'0.1'` |

#### **目标时间** — 目标时间（秒） `100` (默认) | 标量 | 向量 | 矩阵 | N 维数组

频率达到**目标时间的频率**参数值的时间（以秒为单位）。您可以将**目标时间**指定为标量、向量、矩阵或 N 维数组。达到目标时间后，频率继续以相同的速率变化。

##### 编程用法

|  |
| --- |
| **模块参数**：`T` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'100'` |

#### **目标时间的频率** — 频率(Hz) `1` (默认) | 标量 | 向量 | 矩阵 | N 维数组

信号在目标时间的频率（以 Hz 为单位），指定为标量、向量、矩阵或 N 维数组。

##### 编程用法

|  |
| --- |
| **模块参数**：`f2` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 | N 维数组 |
| **默认值：**`'1'` |

#### **将向量参数解释为一维向量** — 将向量参数视为一维 `on` (默认) | `off`

如果选中此复选框，**初始频率**、**目标时间**和**目标时间的频率**参数的任何列或行矩阵值将生成一个向量输出，其元素为该行或列的元素。有关详细信息，请参阅 确定源模块的输出维度。

##### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

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

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含动态分配和释放内存、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Chirp Signal block generates a sine wave whose frequency increases at a
linear rate with time. You can use this block for spectral analysis of nonlinear
systems. The block generates a scalar or vector output.

The parameters, **Initial frequency**, **Target time**, and **Frequency at target time**,
determine the block's output. You can specify any or all of these
variables as scalars or arrays. All the parameters specified as arrays
must have the same dimensions. The block expands scalar parameters
to have the same dimensions as the array parameters. The block output
has the same dimensions as the parameters unless you select the **Interpret vector parameters as 1-D** check box. If you select this check box and the parameters are row or column vectors, the block outputs a vector (1-D array) signal.

## Ports

### Output

### **Port\_1** — Chirp signal scalar | vector | matrix | N-D array

Sine wave whose frequency increases at a linear rate with time. The chirp signal can be
a scalar, vector, matrix, or N-D array.

**Data Types:** `double`

## Parameters

### **Initial frequency** — Initial frequency (Hz) `0.1` (default) | scalar | vector | matrix | N-D array

The initial frequency of the signal, specified as a scalar, vector,
matrix, or N-D array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `f1` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'0.1'` |

### **Target time** — Target time (seconds) `100` (default) | scalar | vector | matrix | N-D array

Time, in seconds, at which the frequency reaches the **Frequency
at target time** parameter value. You specify the
**Target time** as a scalar, vector, matrix, or N-D
array. After the target time is reached, the frequency continues to change
at the same rate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `T` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'100'` |

### **Frequency at target time** — Frequency (Hz) `1` (default) | scalar | vector | matrix | N-D array

Frequency, in Hz, of the signal at the target time, specified as a scalar, vector,
matrix, or N-D array.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `f2` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'1'` |

### **Interpret vector parameters as 1-D** — Treat vector parameters as 1-D `on` (default) | `off`

When you select this check box, any column or row matrix values you
specify for the **Initial frequency**, **Target
time**, and **Frequency at target time**
parameters result in a vector output whose elements are the elements of the
row or column. For more information, see Determine the Output Dimensions of Source Blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

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

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

## Version History

**Introduced before R2006a**
