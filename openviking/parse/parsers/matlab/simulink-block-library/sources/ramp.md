---
type: simulink-block
title: 'Ramp'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'ramp'
---

# Ramp

Generate constantly increasing or decreasing signal

## 中文

生成持续上升或下降的信号

### 所属库

Simulink / Sources

### 描述

Ramp 模块可生成从指定时间和值开始并以指定的速率发生变化的信号。此模块的**斜率**、**开始时间**和**初始输出**参数确定了输出信号的特征。进行标量扩展后，所有这些参数必须具有相同的维度。

### 端口

#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

产生的输出斜坡信号的特征由**斜率**、**开始时间**和**初始输出**参数确定。

**数据类型:** `double`

### 参数

#### **斜率** — 信号的斜率 1 (默认) | 标量 | 向量 | 矩阵

指定生成的信号的变化率。

##### 编程用法

|  |
| --- |
| **模块参数**：`slope` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'1'` |

#### **开始时间** — 输出的开始时间 0 (默认) | 标量

指定模块开始生成信号的时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`start` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

#### **初始输出** — 输出信号的初始值 0 (默认) | 标量 | 向量 | 矩阵

指定输出信号的初始值。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**斜率**、**开始时间**或**初始输出**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

- 如果**斜率**、**开始时间**或**初始输出**参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果**斜率**、**开始时间**或**初始输出**参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

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

不建议用于生产代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Ramp block generates a signal that starts at a specified time and value
and changes by a specified rate. The block's **Slope**, **Start
time**, and **Initial output** parameters determine the
characteristics of the output signal. All must have the same dimensions after scalar
expansion.

## Ports

### Output

### **Port\_1** — Output signal scalar | vector | matrix

Generated output ramp signal characterized by the **Slope**,
**Start time**, and **Initial
output** parameters.

**Data Types:** `double`

## Parameters

### **Slope** — Slope of signal 1 (default) | scalar | vector | matrix

Specify the rate of change of the generated signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `slope` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'1'` |

### **Start time** — Time output begins 0 (default) | scalar

Specify the time at which the block begins generating the signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `start` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Initial output** — Initial value of output signal 0 (default) | scalar | vector | matrix

Specify the initial value of the output signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if
the **Slope**, **Start time**, or
**Initial output** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of
  length `N` if the **Slope**,
  **Start time**, or **Initial
  output** parameter evaluates to an
  `N`-element row or column vector. For example, the
  block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector
  of length `N` if the **Slope**,
  **Start time**, or **Initial
  output** parameter evaluates to an
  `N`-element row or column vector.

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

Not recommended for production code.

## Version History

**Introduced before R2006a**
