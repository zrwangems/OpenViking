---
type: simulink-block
title: 'Band-Limited White Noise'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'bandlimitedwhitenoise'
---

# Band-Limited White Noise

Introduce white noise into continuous system

## 中文

在连续系统中引入白噪声

### 所属库

Simulink / Sources

### 描述

Band-Limited White Noise 模块生成适合在连续系统或混合系统中使用的正态分布随机数。

#### 白噪声仿真

从理论上讲，连续白噪声的相关时间为 0，功率谱密度 (PSD) 呈水平状态，总能量为无穷大。在实践中，物理系统永远不受白噪声干扰，尽管当噪声干扰的相关时间相对于系统的自然带宽非常小时，白噪声是很有用的理论逼近。

在 Simulink® 软件中，您可以使用相关时间比系统的最短时间常数小很多的随机序列来仿真白噪声的作用。Band-Limited White Noise 模块就生成这样的序列。噪声的相关时间是指模块的采样率。要进行准确的仿真，请使用比系统的最快动态小很多的相关时间。您可以通过指定以下方程来获得满意的结果：

tc≈11002πfmax,

其中 *fmax* 是以弧度/秒为单位的系统带宽。

#### 与 Random Number 模块的比较

此模块与 Random Number 模块之间的主要区别在于，Band-Limited White Noise 模块以特定的采样率生成输出。此采样率与噪声的相关时间有关。

#### 与 Averaging Power Spectral Density 模块一起使用

Band-Limited White Noise 模块指定双边频谱，其单位为赫兹。Averaging Power Spectral Density 模块指定单边频谱，其单位为每单位径向频率幅值的平方：mag^2/(rad/sec)。当您将 Band-Limited White Noise 模块的输出馈入 Averaging Power Spectral Density 模块时，平均 PSD 值比 Band-Limited White Noise 模块的**噪声功率**小 π 倍。这种差异是模块之间的单位转换造成的，即 1/(1/2)(2`π`) = 1/`π`，其中：

- 1/2 是从双边频谱转换为单边频谱的因子。
- 2`π` 是从赫兹转换为弧度/秒的因子。

### 端口

#### 输出

#### **Port\_1** — 正态分布的随机数 标量 | 向量 | 矩阵 | N 维数组

正态分布的随机数，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `double`

### 参数

#### **噪声功率** — 白噪声的 PSD 高度 `[0.1]` (默认) | 标量 | 向量 | 矩阵 | N 维数组

将白噪声的 PSD 高度指定为正值的标量、向量、矩阵或 N 维数组。

##### 编程用法

|  |
| --- |
| **模块参数**：`Cov` |
| **类型：**字符向量 |
| **值：**`scalar | vector | matrix | N-D array` |
| **默认值：**`'[0.1]'` |

#### **采样时间** — 噪声的相关时间 `0.1` (默认) | 标量 | 向量

噪声的相关时间。有关详细信息，请参阅指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`Ts` |
| **类型：**字符向量 |
| **值：**`scalar | vector` |
| **默认值：**`'0.1'` |

#### **种子** — 起始种子 `[23341]` (默认) | 标量 | 向量 | 矩阵 | N 维数组

将随机数生成器的起始种子指定为标量、向量、矩阵或 N 维数组。值必须是有限的正实数值。

##### 编程用法

|  |
| --- |
| **模块参数**：`seed` |
| **类型：**字符向量 |
| **值：**`scalar | vector | matrix | N-D array` |
| **默认值：**`'[23341]'` |

#### **将向量参数解释为一维向量** — 将向量参数视为一维 `on` (默认) | `off`

当模块参数为向量时，选择此选项将输出一维数组。否则，将输出二维数组，其中一个维度为 `1`。有关详细信息，请参阅 确定源模块的输出维度。

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

不能在触发子系统层次结构中使用。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sources

## Description

The Band-Limited White Noise block generates normally distributed
random numbers that are suitable for use in continuous or hybrid systems.

### Simulation of White Noise

Theoretically, continuous white noise has a correlation time of 0, a flat power
spectral density (PSD), and a total energy of infinity. In practice, physical
systems are never disturbed by white noise, although white noise is a useful
theoretical approximation when the noise disturbance has a correlation time that is
very small relative to the natural bandwidth of the system.

In Simulink® software, you can simulate the effect of white noise by using a random
sequence with a correlation time much smaller than the shortest time constant of the
system. The Band-Limited White Noise block produces such a sequence.
The correlation time of the noise is the sample rate of the block. For accurate
simulations, use a correlation time much smaller than the fastest dynamics of the
system. You can get good results by specifying

tc≈11002πfmax,

where *fmax* is the bandwidth of the
system in rad/sec.

### Comparison with the Random Number Block

The primary difference between this block and the Random Number
block is that the Band-Limited White Noise block produces output at a
specific sample rate. This rate is related to the correlation time of the
noise.

### Usage with the Averaging Power Spectral Density Block

The Band-Limited White Noise block specifies a two-sided spectrum, where the
units are Hz. The Averaging Power Spectral Density block specifies a
one-sided spectrum, where the units are the square of the magnitude per unit radial
frequency: mag^2/(rad/sec). When you feed the output of a Band-Limited White
Noise block into an Averaging Power Spectral Density block, the average
PSD value is π times smaller than the **Noise power** of the
Band-Limited White Noise block. This difference is the result of
converting the units of one block to the units of the other, 1/(1/2)(2`π`) = 1/`π`, where:

- 1/2 is the factor for converting from a two-sided to one-sided
  spectrum.
- 2`π` is the factor for converting from Hz to
  rad/sec.

## Ports

### Output

### **Port\_1** — Normally distributed random numbers scalar | vector | matrix | N-D array

Normally distributed random numbers specified as a scalar, vector,
matrix, or N-D array.

**Data Types:** `double`

## Parameters

### **Noise power** — Height of PSD of white noise `[0.1]` (default) | scalar | vector | matrix | N-D array

Specify the height of the PSD of the white noise as a scalar, vector,
matrix, or N-D array of positive values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Cov` |
| **Type:** character vector |
| **Values:** `scalar | vector | matrix | N-D array` |
| **Default:** `'[0.1]'` |

### **Sample time** — Correlation time of noise `0.1` (default) | scalar | vector

Correlation time of the noise. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Ts` |
| **Type:** character vector |
| **Values:** `scalar | vector` |
| **Default:** `'0.1'` |

### **Seed** — Starting seed `[23341]` (default) | scalar | vector | matrix | N-D array

Specify the starting seed for the random number generator as a scalar,
vector, matrix, or N-D array. Values must be positive, real-valued, and
finite.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `seed` |
| **Type:** character vector |
| **Values:** `scalar | vector | matrix | N-D array` |
| **Default:** `'[23341]'` |

### **Interpret vector parameters as 1-D** — Treat vector parameters as 1-D `on` (default) | `off`

Select to output a 1-D array when the block parameters are vectors.
Otherwise, output a 2-D array one of whose dimensions is
`1`. For more information, see Determine the Output Dimensions of Source Blocks.

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

Cannot use inside a triggered subsystem hierarchy.

## Version History

**Introduced before R2006a**
