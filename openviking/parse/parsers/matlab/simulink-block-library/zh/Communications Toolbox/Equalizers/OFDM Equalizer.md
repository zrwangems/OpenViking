---
type: simulink-block
title: 'OFDM Equalizer'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Equalizers'
documentation_page: 'ofdmequalizerblock'
documentation_source_path: 'ref/ofdmequalizerblock.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Equalizer

## 端口

### 输入

### **in** — 输入信号 3-D 数组 | 2-D 数组

输入信号，指定为接收 OFDM 符号的 3-D 或 2-D 数组。

- 如果 **Data format** 设置为
  `3-D`，则输入信号必须
  指定为
  *N*SC-by-*N*Symbols-by-*N*R
  数组。*N*SC
  表示 OFDM 子载波数，
  *N*Symbols
  表示 OFDM 符号数，*N*R 表示
  接收天线数。
- 如果 **Data format** 设置为
  `2-D`，则输入信号必须
  指定为
  *N*RE-by-*N*R
  数组。*N*RE
  表示 OFDM 子载波符号网格的不规则子集中的资源元素数。

**数据类型:** `double` | `single`
**复数支持:** Yes

### **hEst** — 信道估计 3-D 数组

信道估计，指定为 3-D 数组。

- 如果 **Data format** 设置为
  `3-D`，模块期望
  **hEst** 为
  *N*SC-by-*N*T-by-*N*R
  或
  (*N*SC×*N*Symbols)-by-*N*T-by-*N*R 数组。

  - 如果 **hEst** 为
    *N*SC-by-*N*T-by-*N*R
    数组，则输入信号
    `in` 中的所有 OFDM 符号
    都使用同一信道估计进行均衡。
    *N*SC
    表示 OFDM 子载波数，
    *N*T
    表示发射天线数，*N*R
    表示接收天线数。
  - 如果 **hEst** 为
    (*N*SC×*N*Symbols)-by-*N*T-by-*N*R
    数组，则输入信号
    `in` 中的每个 OFDM 符号
    都使用 **hEst** 中的对应条目进行均衡。
    *N*Symbols
    表示 OFDM 符号数。
- 如果 **Data format** 设置为
  `2-D`，模块期望
  **hEst** 为
  *N*RE-by-*N*T-by-*N*R
  数组。输入信号
  `in` 中的每个 OFDM 符号
  都使用 **hEst** 中的对应条目进行均衡。
  *N*RE 表示
  OFDM 子载波符号网格的不规则子集中的资源元素数。

**数据类型:** `double` | `single`
**复数支持:** Yes

### **noiseVar** — 噪声方差 0（默认） | 非负标量

用于最小均方误差 (MMSE) 均衡的噪声方差估计，指定为非负标量。

#### 依赖关系

仅当您将 **Noise variance source** 设置为 `Input port` 并且将 **Algorithm** 设置为 `Minimum mean squared error` 时，才使用噪声方差输入端口。

**数据类型:** `double` | `single`

### 输出

### **out** — 均衡后的符号 3-D 数组 | 2-D 数组

均衡后的符号，返回为 3-D 或 2-D 数组。

- 如果 **Data format** 设置为
  `3-D`，模块返回
  *N*SC-by-*N*Symbols-by-*N*T
  数组。*N*SC
  表示 OFDM 子载波数，
  *N*Symbols
  表示 OFDM 符号数，*N*T 表示
  发射天线数。
- 如果 **Data format** 设置为
  `2-D`，模块返回
  *N*RE-by-*N*T
  数组。*N*RE
  表示 OFDM 子载波符号网格的不规则子集中的资源元素数。

### **csi** — 软信道状态信息矩阵

软信道状态信息，返回为一个矩阵，其中
`size(csi,1) = size(hEst,1)` 且
`size(csi,2) = NT = size(hEst,2)`。
*N*T 表示发射天线数。

#### 依赖关系

要启用此输出端口，请选择 **Output soft channel state information** 参数。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Data format** — 信号格式 `3-D`（默认） | `2-D`

信号格式，指定为 `3-D` 或 `2-D`。

当此参数设置为 `3-D` 时，OFDM 子载波和 OFDM 符号在 **in** 和 **out** 的表示中使用两个独立维度。

- **in** 输入必须为
  *N*SC-by-*N*Symbols-by-*N*R
  数组。
- **out** 输出返回为
  *N*SC-by-*N*Symbols-by-*N*T
  数组。

当此参数设置为 `2-D` 时，OFDM 子载波和 OFDM 符号在 **in** 和 **out** 的表示中使用一个组合维度。

- **in** 输入必须为
  *N*RE-by-*N*R
  数组。
- **out** 输出返回为
  *N*RE-by-*N*T
  数组。

*N*SC 表示 OFDM 子载波数。*N*Symbols 表示符号数。*N*RE 表示 OFDM 子载波符号网格的不规则子集中的资源元素数。*N*T 表示发射天线数。*N*R 表示接收天线数。

### **Algorithm** — 均衡算法 `Minimum mean squared error`（默认） | `Zero-forcing`

均衡算法，指定为 `Minimum mean squared error` 或 `Zero-forcing`。

- 当此参数设置为 `Minimum mean squared error` 时，模块使用 MMSE 算法进行均衡。
- 当此参数设置为 `Zero-forcing` 时，模块使用 zero-forcing 算法进行均衡。当使用 zero-forcing 算法时，忽略 **noiseVar** 端口值。

### **Noise variance source** — 噪声方差的来源 `Input port`（默认） | `Property`

噪声方差的来源，指定为以下值之一：

- `Input port` — 指定此值可使用 **noiseVar** 输入端口指定用于 MMSE 均衡的噪声方差估计。
- `Property` — 指定此值可使用 **Noise variance** 参数指定用于 MMSE 均衡的噪声方差估计。

### **Noise variance** — 噪声方差 0（默认） | 非负标量

用于 MMSE 均衡的噪声方差估计，指定为非负标量。

#### 依赖关系

仅当您将 **Noise variance source** 设置为 `Property` 并将 **Algorithm** 设置为 `Minimum mean squared error` 时，才使用噪声方差设置。

### **Output soft channel state information** — 启用软信道状态信息输出 `off`（默认） | `on`

选择此参数以启用包含软信道状态信息的输出端口 **csi**。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Equalizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

均衡 OFDM 调制信号

OFDM Equalizer 模块执行频域均衡，以恢复通过信道传输的 OFDM 调制符号。

此图标显示启用了所有端口的模块。

显示可选端口的 OFDM Equalizer 模块。
