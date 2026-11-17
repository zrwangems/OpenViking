---
type: simulink-block
title: 'Band-Limited White Noise'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'bandlimitedwhitenoise'
documentation_source_path: 'slref/bandlimitedwhitenoise.html'
language: zh-CN
chinese_source: worker-translation
---

# Band-Limited White Noise

## 端口
```yaml
ports:
- name: Port_1
  summary: 正态分布随机数 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: double
```

### 输出

### **Port\_1** — 正态分布随机数 标量 | 向量 | 矩阵 | N 维数组

指定为正态分布的随机数，以标量、向量、矩阵或 N 维数组形式表示。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Noise power
  summary: 白噪声的 PSD 高度 [0.1]（默认）| 标量 | 向量 | 矩阵 | N 维数组
  group: ''
  block_parameter: Cov
  type: 字符向量
  values: scalar | vector | matrix | N-D array
  default: '''[0.1]'''
- name: Sample time
  summary: 噪声的相关时间 0.1（默认）| 标量 | 向量
  group: ''
  block_parameter: Ts
  type: 字符向量
  values: scalar | vector
  default: '''0.1'''
- name: Seed
  summary: 起始种子 [23341]（默认）| 标量 | 向量 | 矩阵 | N 维数组
  group: ''
  block_parameter: seed
  type: 字符向量
  values: scalar | vector | matrix | N-D array
  default: '''[23341]'''
- name: Interpret vector parameters as 1-D
  summary: 将向量参数视为一维 on（默认）| off
  group: ''
  block_parameter: VectorParams1D
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Noise power** — 白噪声的 PSD 高度 `[0.1]`（默认）| 标量 | 向量 | 矩阵 | N 维数组

将白噪声的 PSD 高度指定为正值的标量、向量、矩阵或 N 维数组。

#### 编程用法

|  |
| --- |
| **模块参数：** `Cov` |
| **类型：** 字符向量 |
| **值：** `scalar | vector | matrix | N-D array` |
| **默认值：** `'[0.1]'` |

### **Sample time** — 噪声的相关时间 `0.1`（默认）| 标量 | 向量

噪声的相关时间。有关详细信息，请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** 字符向量 |
| **值：** `scalar | vector` |
| **默认值：** `'0.1'` |

### **Seed** — 起始种子 `[23341]`（默认）| 标量 | 向量 | 矩阵 | N 维数组

将随机数生成器的起始种子指定为标量、向量、矩阵或 N 维数组。值必须为正的、实值的且有限的。

#### 编程用法

|  |
| --- |
| **模块参数：** `seed` |
| **类型：** 字符向量 |
| **值：** `scalar | vector | matrix | N-D array` |
| **默认值：** `'[23341]'` |

### **Interpret vector parameters as 1-D** — 将向量参数视为一维 `on`（默认）| `off`

选中此选项后，当模块参数为向量时，将输出一维数组。否则，输出二维数组，其中一个维度为 `1`。有关详细信息，请参阅确定源模块的输出维度。

#### 编程用法

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
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不能在触发子系统层次结构内使用。

## 版本历史

**在 R2006a 之前推出**

## 描述

将白噪声引入连续系统

Band-Limited White Noise 模块生成适合在连续或混合系统中使用的正态分布随机数。

### 白噪声的仿真

理论上，连续白噪声的相关时间为 0，功率谱密度 (PSD) 是平坦的，总能量为无穷大。在实践中，物理系统从不会受到白噪声的干扰，尽管当噪声干扰的相关时间相对于系统的自然带宽非常小时，白噪声是一种有用的理论近似。

在 Simulink® 软件中，您可以通过使用相关时间远小于系统最短时间常数的随机序列来仿真白噪声的影响。Band-Limited White Noise 模块产生这样的序列。噪声的相关时间是模块的采样率。为了获得准确的仿真，请使用远小于系统最快动态的相关时间。您可以通过指定以下内容获得良好的结果：

tc≈11002πfmax，

其中 *fmax* 是系统的带宽，单位为 rad/sec。

### 与 Random Number 模块的比较

此模块与 Random Number 模块的主要区别在于，Band-Limited White Noise 模块以特定的采样率产生输出。此采样率与噪声的相关时间有关。

### 与 Averaging Power Spectral Density 模块一起使用

Band-Limited White Noise 模块指定双边频谱，单位为 Hz。Averaging Power Spectral Density 模块指定单边频谱，单位为单位径向频率的幅度平方：mag^2/(rad/sec)。当您将 Band-Limited White Noise 模块的输出馈入 Averaging Power Spectral Density 模块时，平均 PSD 值比 Band-Limited White Noise 模块的 **Noise power** 小 π 倍。此差异是将一个模块的单位转换为另一个模块的单位的结果，1/(1/2)(2`π`) = 1/`π`，其中：

- 1/2 是从双边频谱转换为单边频谱的因子。
- 2`π` 是从 Hz 转换为 rad/sec 的因子。
