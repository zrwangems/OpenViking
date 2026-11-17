---
type: simulink-block
title: 'Uniform Random Number'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'uniformrandomnumber'
documentation_source_path: 'slref/uniformrandomnumber.html'
language: zh-CN
chinese_source: worker-translation
---

# Uniform Random Number

## 端口

### 输出

### **Port\_1** — 随机数输出信号 标量 | 向量

在您指定的区间上生成的均匀分布随机数的输出信号。

**数据类型：** `double`

## 参数

### **Minimum** — 最小间隔 `0`（默认）| 标量 | 向量 | 矩阵 | N 维数组

指定间隔的最小值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Minimum` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'-1'` |

### **Maximum** — 最大间隔 `0`（默认）| 标量 | 向量 | 矩阵 | N 维数组

指定间隔的最大值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Maximum` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'1'` |

### **Seed** — 随机数种子 `0`（默认）| 标量 | 向量 | 矩阵 | N 维数组

指定随机数生成器的起始种子。

种子必须为 0 或正整数。对于给定的种子，输出是可重复的。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Sample time** — 采样时间 `0.1`（默认）| 标量

指定采样之间的时间间隔。有关详细信息，请参阅指定采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.1'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Constant value** 参数求值为 `N` 元素的行或列向量，则选中此复选框以输出长度为 `N` 的向量。

- 当您选中此复选框时，如果 **Constant value** 参数求值为 `N` 元素的行或列向量，则模块输出长度为 `N` 的向量。例如，模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 当您清除此复选框时，如果 **Constant value** 参数求值为 `N` 元素的行或列向量，则模块不输出长度为 `N` 的向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VectorParams1D` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认值：** `'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成均匀分布的随机数

Uniform Random Number 模块在您指定的区间上生成均匀分布的随机数。要生成正态分布的随机数，请使用 Random Number 模块。这两个模块都使用 Normal (Gaussian) 随机数生成器（`'v4'`：`rng` 函数的旧版 MATLAB® 4.0 生成器）。

您可以使用任何具有相同非负种子和参数的 Uniform Random Number 模块生成可重复的序列。每次仿真开始时，种子都会重置为指定的值。

避免对随机信号进行积分，因为求解器必须积分相对平滑的信号。请改用 Band-Limited White Noise 模块。

此模块的数值参数在标量扩展后必须具有相同的维度。如果您选中 **Interpret vector parameters as 1-D** 复选框，并且数值参数在标量扩展后为行或列向量，则模块输出一维信号。如果您清除 **Interpret vector parameters as 1-D** 复选框，则模块输出的信号维度与参数相同。
