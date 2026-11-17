---
type: simulink-block
title: 'Random Number'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'SNG'
documentation_page: 'randomnumber'
documentation_source_path: '../simulink/slref/randomnumber.html'
language: zh-CN
chinese_source: worker-translation
---

# Random Number

## 端口

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，即生成的服从正态高斯分布的随机数。对于给定的种子，输出是可重复的。

**数据类型：** `double`

## 参数

### **Mean** — 随机数的均值 `0`（默认）| 标量 | 数组

指定所生成随机数的均值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Mean` |
| **类型**：字符向量 |
| **值**：标量 | 数组 |
| **默认值**：`'0'` |

### **Variance** — 随机数的方差 `1`（默认）| 标量 | 数组

指定随机数的方差。

#### 编程使用

|  |
| --- |
| **模块参数**：`Variance` |
| **类型**：字符向量 |
| **值**：标量 | 数组 |
| **默认值**：`'1'` |

### **Seed** — 起始种子 `0`（默认）| 正整数 | 标量 | 数组

指定随机数生成器的起始种子。

对于给定的种子，所生成数字的输出是可重复的。

#### 编程使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：字符向量 |
| **值**：标量 | 数组 |
| **默认值**：`'0'` |

### **Sample time** — 间隔之间的时间 `0.1`（默认）| `integer`

指定采样之间的时间间隔。默认值为 `0.1`，与 Band-Limited White Noise 模块的默认采样时间一致。有关更多信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.1'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Mean**、**Variance** 和 **Seed** 参数求值为 `N` 元素的行向量或列向量，则选中此复选框以输出长度为 `N` 的向量。

- 选中此复选框时，如果 **Mean**、**Variance** 和 **Seed** 参数求值为 `N` 元素的行向量或列向量，则模块输出长度为 `N` 的向量。例如，模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 清除此复选框时，如果 **Mean**、**Variance** 和 **Seed** 参数求值为 `N` 元素的行向量或列向量，则模块不输出长度为 `N` 的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：字符向量 |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成正态分布的随机数

Random Number 模块生成正态分布的随机数。要生成均匀分布的随机数，请使用 Uniform Random Number 模块。这两个模块都使用 Normal (Gaussian) 随机数生成器（`'v4'`：`rng` 函数的旧版 MATLAB® 4.0 生成器）。

您可以使用任何具有相同非负种子和参数的 Random Number 模块生成可重复的序列。每次仿真开始时，种子都会重置为指定的值。默认情况下，该模块生成的序列均值为 0，方差为 1。要生成具有相同均值和方差的随机数向量，请将 **Seed** 参数指定为向量。

避免对随机信号进行积分，因为求解器必须对相对平滑的信号进行积分。请改用 Band-Limited White Noise 模块。

此模块的数值参数在标量扩展后必须具有相同的维度。如果选中 **Interpret vector parameters as 1-D** 复选框，并且数值参数在标量扩展后为行向量或列向量，则模块输出一维信号。如果清除 **Interpret vector parameters as 1-D** 复选框，则模块输出的信号维度与参数相同。
