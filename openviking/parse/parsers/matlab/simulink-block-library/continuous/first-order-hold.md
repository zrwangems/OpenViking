---
type: simulink-block
title: 'First Order Hold'
family: continuous
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'firstorderhold'
---

# First Order Hold

Implement linearly extrapolated first order hold on input signal

## 中文

在输入信号上实现线性外插一阶保持

### 所属库

Simulink / Continuous

### 描述

First Order Hold 模块生成输入信号的连续分段线性逼近。使用 First Order Hold 模块将采样的离散信号转换为连续信号，而不触发求解器重置。

您也可以使用 First Order Hold 模块来打破模型中的代数环。

### 端口

#### 输入

#### **Port 1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为实标量、向量或矩阵。

**数据类型:** `double`
#### 输出

#### **Port 1** — 线性逼近的输出信号 标量 | 向量 | 矩阵

输入信号的分段线性逼近。

**数据类型:** `double`

### 参数

#### **初始输出** — 初始输出 `0` (默认) | 标量 | 向量

指定模块在仿真时间超过离散输入的第一个采样时间命中点之前生成的输出。

##### 依赖关系

- 此模块的初始输出不能为 `inf` 或 `NaN`。
- 不能在仿真运行时更改`运行到运行可调参数`。但是，在仿真开始之前更改此参数不会使得加速或快速加速重新生成代码。

##### 编程用法

|  |
| --- |
| **模块参数：**`InitialOutput` |
| **类型：**字符向量、字符串 |
| **值：**标量 | 向量 |
| **默认值：**`'0'` |

#### **输出算法** — 输出信号逼近方法 **缓慢(避免过冲)** (默认) | **快速（最小化误差）**

指定用于生成输出信号的逼近方法。慢速低通算法可避免输入信号过冲。快速高通算法可将逼近输出中的误差降至最低，但可能会使输入信号过冲。

##### 编程用法

|  |
| --- |
| **模块参数：**`OutputAlgorithm` |
| **类型：**字符向量、字符串 |
| **值**：`Slow (Avoid Overshoot)` | `Fast (Minimize Error)` |
| **默认值**：`'Slow (Avoid Overshoot)'` |

#### **相对外插误差超过以下值时重置** — 求解器重置的误差容限 `inf` (默认) | 非负实数标量

指定输出算法外插误差的容差级别。大于指定值的外插误差会导致 Simulink® 重置模型的求解器。

**提示**

当此参数设置为 `inf` 时，启用**允许连续输入**参数可能会导致仿真中的数值不准确。

##### 编程用法

|  |
| --- |
| **模块参数：**`ErrorTolerance` |
| **类型：**字符向量、字符串 |
| **值：**标量 |
| **默认值：**`'inf'` |

#### **允许连续输入** — 对连续信号应用保持 `off` (默认) | `on`

选择此参数将使模块能够接受连续信号作为输入。启用此参数会在输入和输出连续信号之间产生延迟。

**注意**

当使用此模块打破代数环时，请启用此参数。

##### 编程用法

|  |
| --- |
| **模块参数：**`AllowContinuousInput` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

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

不建议用于生产代码生成。

请考虑对模型进行离散化。

### 版本历史记录

**在 R2019b 中推出**

## Libraries

Simulink / Continuous

## Description

The First Order Hold block generates a continuous piecewise linear
approximation of the input signal. Use the First Order Hold block to
convert a sampled discrete signal to a continuous signal without triggering a solver
reset.

You can also use the First Order Hold block to break algebraic loops in
your model.

## Ports

### Input

### **Port 1** — Input signal scalar | vector | matrix

Input signal, specified as a real scalar, vector, or matrix.

**Data Types:** `double`
### Output

### **Port 1** — Linearly approximated output signal scalar | vector | matrix

Piecewise linear approximation of the input signal.

**Data Types:** `double`

## Parameters

### **Initial output** — Initial output `0` (default) | scalar | vector

Specify the output that the block generates until the simulation time exceeds the first sample
hit time of the discrete input.

#### Dependencies

- The initial output of this block cannot be `inf` or `NaN`.
- A `Run-to-run tunable parameter` cannot be changed during simulation run time. However, changing it before a simulation begins does not cause Accelerator or Rapid Accelerator to regenerate code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Output algorithm** — Output signal approximation technique `Slow (Avoid Overshoot)` (default) | `Fast (Minimize Error)`

Specify the approximation technique used to generate the output signal.
The slow, low pass algorithm avoids overshooting the input signal. The fast,
high pass algorithm minimizes error in the approximated output but can
overshoot the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputAlgorithm` |
| **Type:** character vector, string |
| **Values:** `Slow (Avoid Overshoot)`| `Fast (Minimize Error)` |
| **Default:** `'Slow (Avoid Overshoot)'` |

### **Reset if relative extrapolation error exceeds** — Error tolerance for solver reset `inf` (default) | non-negative real scalar

Specify the tolerance level for the extrapolation error of the output
algorithm. Extrapolation error greater than the specified value causes
Simulink® to reset the solver for the model.

**Tip**

Enabling the **Allow continuous input** parameter
when this parameter is set to `inf` can lead to
numerical inaccuracies in simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ErrorTolerance` |
| **Type:** character vector, string |
| **Values:** scalar |
| **Default:** `'inf'` |

### **Allow continuous input** — Apply hold on continuous signals `off` (default) | `on`

Select this parameter to enable the block to accept continuous signals as
input. Enabling this parameter creates a delay between the input and output
continuous signals.

**Note**

Enable this parameter when using this block to break an algebraic
loop.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowContinuousInput` |
| **Type:** character vector, string |
| **Values:** `'off'`| `'on'` |
| **Default:** `'off'` |

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

Not recommended for production code generation.

Consider discretizing your model.

## Version History

**Introduced in R2019b**
