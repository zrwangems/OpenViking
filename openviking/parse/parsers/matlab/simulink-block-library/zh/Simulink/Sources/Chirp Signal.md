---
type: simulink-block
title: 'Chirp Signal'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'chirpsignal'
documentation_source_path: 'slref/chirpsignal.html'
language: zh-CN
chinese_source: worker-translation
---

# Chirp Signal

## 端口

### 输出

### **Port\_1** — Chirp 信号 标量 | 向量 | 矩阵 | N 维数组

频率随时间线性增加的 sine wave。Chirp 信号可以是标量、向量、矩阵或 N 维数组。

**数据类型：** `double`

## 参数

### **Initial frequency** — 初始频率 (Hz) `0.1`（默认）| 标量 | 向量 | 矩阵 | N 维数组

信号的初始频率，指定为标量、向量、矩阵或 N 维数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`f1` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'0.1'` |

### **Target time** — 目标时间（秒） `100`（默认）| 标量 | 向量 | 矩阵 | N 维数组

频率达到 **Frequency at target time** 参数值的时间，以秒为单位。将 **Target time** 指定为标量、向量、矩阵或 N 维数组。达到目标时间后，频率继续以相同速率变化。

#### 编程使用

|  |
| --- |
| **模块参数**：`T` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'100'` |

### **Frequency at target time** — 频率 (Hz) `1`（默认）| 标量 | 向量 | 矩阵 | N 维数组

信号在目标时间的频率，以 Hz 为单位，指定为标量、向量、矩阵或 N 维数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`f2` |
| **类型**：character vector |
| **值**：scalar | vector | matrix | N-D array |
| **默认值**：`'1'` |

### **Interpret vector parameters as 1-D** — 将向量参数视为一维 `on`（默认）| `off`

选中此复选框时，为 **Initial frequency**、**Target time** 和 **Frequency at target time** 参数指定的任何列或行矩阵值都会生成向量输出，其元素为行或列的元素。有关详细信息，请参阅 Determine the Output Dimensions of Source Blocks。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：character vector |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然该代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐步演变为适合生产代码。因此，适合生产代码的模块仍然适合。

## 版本历史

**在 R2006a 之前推出**

## 描述

生成频率递增的 sine wave

Chirp Signal 模块生成一个 sine wave，其频率随时间线性增加。您可以使用此模块对非线性系统进行频谱分析。该模块生成标量或向量输出。

参数 **Initial frequency**、**Target time** 和 **Frequency at target time** 决定模块的输出。您可以将这些变量中的任意一个或全部指定为标量或数组。所有指定为数组的参数必须具有相同的维度。该模块会将标量参数扩展为与数组参数具有相同的维度。除非您选中 **Interpret vector parameters as 1-D** 复选框，否则模块输出与参数具有相同的维度。如果您选中此复选框，并且参数是行向量或列向量，则该模块输出向量（一维数组）信号。
