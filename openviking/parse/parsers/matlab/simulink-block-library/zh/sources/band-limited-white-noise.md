---
type: simulink-block
title: 'Band-Limited White Noise'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'bandlimitedwhitenoise'
language: zh-CN
chinese_source: official
---

# Band-Limited White Noise

## 端口

### 输出

### **Port\_1** — 正态分布的随机数 标量 | 向量 | 矩阵 | N 维数组

正态分布的随机数，指定为标量、向量、矩阵或 N 维数组。

**数据类型:** `double`

## 参数

### **噪声功率** — 白噪声的 PSD 高度 `[0.1]` (默认) | 标量 | 向量 | 矩阵 | N 维数组

将白噪声的 PSD 高度指定为正值的标量、向量、矩阵或 N 维数组。

#### 编程用法

|  |
| --- |
| **模块参数**：`Cov` |
| **类型：**字符向量 |
| **值：**`scalar | vector | matrix | N-D array` |
| **默认值：**`'[0.1]'` |

### **采样时间** — 噪声的相关时间 `0.1` (默认) | 标量 | 向量

噪声的相关时间。有关详细信息，请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`Ts` |
| **类型：**字符向量 |
| **值：**`scalar | vector` |
| **默认值：**`'0.1'` |

### **种子** — 起始种子 `[23341]` (默认) | 标量 | 向量 | 矩阵 | N 维数组

将随机数生成器的起始种子指定为标量、向量、矩阵或 N 维数组。值必须是有限的正实数值。

#### 编程用法

|  |
| --- |
| **模块参数**：`seed` |
| **类型：**字符向量 |
| **值：**`scalar | vector | matrix | N-D array` |
| **默认值：**`'[23341]'` |

### **将向量参数解释为一维向量** — 将向量参数视为一维 `on` (默认) | `off`

当模块参数为向量时，选择此选项将输出一维数组。否则，将输出二维数组，其中一个维度为 `1`。有关详细信息，请参阅 确定源模块的输出维度。

#### 编程用法

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型：**字符向量 |
| **值：**`'on' | 'off'` |
| **默认值：**`'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不能在触发子系统层次结构中使用。

## 版本历史

**在 R2006a 之前推出**

## 描述

在连续系统中引入白噪声

Band-Limited White Noise 模块生成适合在连续系统或混合系统中使用的正态分布随机数。

### 白噪声仿真

从理论上讲，连续白噪声的相关时间为 0，功率谱密度 (PSD) 呈水平状态，总能量为无穷大。在实践中，物理系统永远不受白噪声干扰，尽管当噪声干扰的相关时间相对于系统的自然带宽非常小时，白噪声是很有用的理论逼近。

在 Simulink® 软件中，您可以使用相关时间比系统的最短时间常数小很多的随机序列来仿真白噪声的作用。Band-Limited White Noise 模块就生成这样的序列。噪声的相关时间是指模块的采样率。要进行准确的仿真，请使用比系统的最快动态小很多的相关时间。您可以通过指定以下方程来获得满意的结果：

tc≈11002πfmax,

其中 *fmax* 是以弧度/秒为单位的系统带宽。

### 与 Random Number 模块的比较

此模块与 Random Number 模块之间的主要区别在于，Band-Limited White Noise 模块以特定的采样率生成输出。此采样率与噪声的相关时间有关。

### 与 Averaging Power Spectral Density 模块一起使用

Band-Limited White Noise 模块指定双边频谱，其单位为赫兹。Averaging Power Spectral Density 模块指定单边频谱，其单位为每单位径向频率幅值的平方：mag^2/(rad/sec)。当您将 Band-Limited White Noise 模块的输出馈入 Averaging Power Spectral Density 模块时，平均 PSD 值比 Band-Limited White Noise 模块的**噪声功率**小 π 倍。这种差异是模块之间的单位转换造成的，即 1/(1/2)(2`π`) = 1/`π`，其中：

- 1/2 是从双边频谱转换为单边频谱的因子。
- 2`π` 是从赫兹转换为弧度/秒的因子。
