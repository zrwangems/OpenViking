---
type: simulink-block
title: 'Uniform Random Number'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'uniformrandomnumber'
---

# Uniform Random Number

Generate uniformly distributed random numbers

## 中文

生成均匀分布的随机数

### 所属库

Simulink / Sources

### 描述

Uniform Random Number 模块在您指定的间隔内生成均匀分布的随机数。要生成正态分布的随机数，请使用 Random Number 模块。两个模块都使用正态（高斯）随机数生成器（`'v4'`：`rng` 函数的传统 MATLAB® 4.0 生成器）。

您可以使用任何 Uniform Random Number 模块，利用相同的非负种子和参数生成可重复的序列。每次开始仿真时，种子都会重置为指定的值。

应避免对随机信号求积分，因为求解器积分针对的只能为相对平滑的信号。这种情况请改用 Band-Limited White Noise 模块。

此模块的数值参数在标量扩展后必须具有相同的维度。如果选中了**将向量参数解释为一维向量**复选框，而数值参数在标量扩展后是行或列向量，则模块将输出 1 维信号。如果清除**将向量参数解释为一维向量**复选框，模块将输出与参数具有相同维数的信号。

### 端口

#### 输出

#### **Port\_1** — 随机数输出信号 标量 | 向量

在您指定的间隔内生成均匀分布的随机数的输出信号。

**数据类型:** `double`

### 参数

#### **最小** — 最小间隔 `0` (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定间隔的最小值。

##### 编程用法

|  |
| --- |
| **模块参数**：`Minimum` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'-1'` |

#### **最大** — 最大间隔 `0` (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定间隔的最大值。

##### 编程用法

|  |
| --- |
| **模块参数**：`Maximum` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

#### **种子** — 随机数种子 `0` (默认) | 标量 | 向量 | 矩阵 | N 维数组

指定随机数生成器的起始种子。

种子必须为 0 或正整数。给定种子的输出可以重复。

##### 编程用法

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **采样时间** — 采样时间 `0.1` (默认) | 标量

指定采样时间间隔。有关详细信息，请参阅 指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.1'` |

#### **将向量参数解释为一维向量** — 将向量视为一维 `on` (默认) | `off`

如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，选中此复选框将输出长度为 `N` 的向量。

- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则选中此复选框时，模块将输出长度为 `N` 的向量。例如，模块将输出 `1-by-N` 维或 `N-by-1` 维矩阵。
- 如果**常量值**参数的计算结果为包含 `N` 个元素的行或列向量，则清除此复选框时，模块不输出长度为 `N` 的向量。

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
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Uniform Random Number block generates uniformly distributed random
numbers over an interval that you specify. To generate normally distributed random
numbers, use the Random Number block. Both blocks use the
Normal (Gaussian) random number generator (`'v4'`: legacy MATLAB® 4.0 generator of the `rng` function).

You can generate a repeatable sequence using any Uniform Random Number block
with the same nonnegative seed and parameters. The seed resets to the specified value
each time a simulation starts.

Avoid integrating a random signal, because solvers must integrate relatively smooth signals.
Instead, use the Band-Limited White Noise block.

The numeric parameters of this block must have the same dimensions
after scalar expansion. If you select the **Interpret vector parameters as 1-D** check box and the numeric parameters
are row or column vectors after scalar expansion, the block outputs
a 1-D signal. If you clear the **Interpret vector parameters as 1-D** check box, the block outputs a signal of the same dimensionality as the parameters.

## Ports

### Output

### **Port\_1** — Random number output signal scalar | vector

Output signal of generated uniformly distributed random numbers over
the interval you specify.

**Data Types:** `double`

## Parameters

### **Minimum** — Minimum interval `0` (default) | scalar | vector | matrix | N-D array

Specify the minimum of the interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Minimum` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'-1'` |

### **Maximum** — Maximum interval `0` (default) | scalar | vector | matrix | N-D array

Specify the maximum of the interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Maximum` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1'` |

### **Seed** — Random number seed `0` (default) | scalar | vector | matrix | N-D array

Specify the starting seed for the random number generator.

The seed must be 0 or a positive integer. Output is repeatable for a given
seed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Seed` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Sample time** — Sample time `0.1` (default) | scalar

Specify the time interval between samples. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.1'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if the
**Constant value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector. For example,
  the block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector.

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
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**
