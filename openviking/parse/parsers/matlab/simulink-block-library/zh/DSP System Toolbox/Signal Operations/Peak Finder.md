---
type: simulink-block
title: 'Peak Finder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'peakfinder'
documentation_source_path: 'ref/peakfinder.html'
language: zh-CN
chinese_source: worker-translation
---

# Peak Finder

## 端口
```yaml
ports:
- name: Port_1
  summary: 数据输入 至少三行的列向量 | 至少三行的矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Cnt
  summary: 峰值数量 标量 | 行向量
  direction: output
  data_types: uint32
- name: Idx
  summary: 峰值索引 列向量 | 矩阵
  direction: output
  data_types: uint32
- name: Val
  summary: 峰值 列向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Pol
  summary: 峰值极性 列向量 | 矩阵
  direction: output
  data_types: Boolean
```

### 输入

### **Port\_1** — 数据输入 至少三行的列向量 | 至少三行的矩阵

Peak Finder 模块接受至少三行的实数值向量或矩阵输入。

**示例:** [`9 6 10 3 5 5 0 12`; `9 6 1 13 4 1 0
12`]'

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Cnt** — 峰值数量 标量 | 行向量

模块在输入信号中检测到的峰值数量，以标量或长度等于数据输入中通道数的行向量形式返回。

**示例:** [`4 3`]

**数据类型:** `uint32`

### **Idx** — 峰值索引 列向量 | 矩阵

输入信号中峰值的索引，以列向量或矩阵形式返回。峰值索引输出的大小与输入的大小相同。所有非零元素表示峰值索引。

如果将 **Index base** 设置为 `Zero`，模块输出从零开始的极值索引。如果将 **Index
base** 设置为 `One`，模块输出从一开始的极值索引。

**示例:** [`1 2 3 6 0 0 0 0 0 0`; `2 3 6 0 0 0 0 0 0
0`]'

#### 依赖

要启用此输出端口，请选择 **Output peak indices** 参数。

**数据类型:** `uint32`

### **Val** — 峰值 列向量 | 矩阵

输入信号中的峰值，以列向量或矩阵形式返回。

**示例:** [`6 10 3 0 0 0 0 0 0 0`; `1 13 0 0 0 0 0 0 0
0`]'

#### 依赖

要启用此输出端口，请选择 **Output peak values** 参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Pol** — 峰值极性 列向量 | 矩阵

输入信号中的峰值极性，以逻辑 1 和 0 的列向量或矩阵形式返回。如果信号值为极大值，模块在此端口输出 1。如果信号值为极小值，模块在此端口输出 0。

**示例:** [`0 1 0 0 0 0 0 0 0 0`; `0 1 0 0 0 0
0 0 0 0`]'

#### 依赖

要启用此端口，请选择 **Output peak
indices** 或 **Output peak values**，并将 **Peak type(s)** 参数设置为
`Maxima and Minima`。

**数据类型:** `Boolean`
## 参数
```yaml
parameters:
- name: Peak type(s)
  summary: 要识别的峰值类型 Maxima and Minima (默认) | Maxima | Minima
  group: ''
- name: Index base
  summary: 索引基准 Zero (默认) | One
  group: ''
- name: Output peak indices
  summary: 启用峰值索引输出 off (默认) | on
  group: ''
- name: Output peak values
  summary: 启用峰值输出 off (默认) | on
  group: ''
- name: Maximum number of peaks to find
  summary: 要识别的最大峰值数量 10 (默认) | 大于或等于 1 的整数
  group: ''
- name: Ignore peaks within threshold of neighboring values
  summary: 忽略低于阈值的峰值 off (默认) | on
  group: ''
- name: Threshold
  summary: 忽略峰值的阈值 0 (默认) | 正实数标量 | 向量
  group: ''
- name: Saturate on integer overflow
  summary: 溢出操作方式 off (默认) | on
  group: ''
```

### **Peak type(s)** — 要识别的峰值类型 `Maxima and Minima` (默认) | `Maxima` | `Minima`

指定要识别的峰值类型为以下之一：

- `Maxima` –– 如果选择
  **Ignore peaks within threshold of neighboring
  values**，当 (*current* – *previous*) > *threshold* 且 (*current* – *next*) >
  *threshold* 时，模块将当前值识别为极大值。在
  **Threshold** 参数中指定 *threshold*。如果不选择
  **Ignore peaks within threshold of neighboring
  values**，当当前值大于其两个相邻点时，模块将其识别为极大值。
- `Minima` –– 如果选择
  **Ignore peaks within threshold of neighboring
  values**，当 (*current* – *previous*) < –*threshold* 且 (*current* – *next*)
  < –*threshold* 时，模块将当前值识别为极小值。如果不
  选择 **Ignore peaks within threshold of neighboring
  values**，当当前值小于其两个相邻点时，模块将其识别为极小值。
- `Maxima and Minima` –– 模块
  识别极大值和极小值点。

### **Index base** — 索引基准 `Zero` (默认) | `One`

指定极值索引的基准为以下之一：

- `Zero` –– 第一个索引从
  0 开始。例如，考虑输入向量 [−1.5, 0.5, 0]。该向量的峰值为 0.5，该峰值的索引为 1。
- `One` –– 在此设置下，第一个
  索引从 1 开始。[−1.5, 0.5,
  0] 中峰值的索引为 2。

### **Output peak indices** — 启用峰值索引输出 `off` (默认) | `on`

如果希望模块在 **Idx** 端口输出极值索引，请选中此复选框。

### **Output peak values** — 启用峰值输出 `off` (默认) | `on`

如果希望模块在 **Val** 端口输出极值，请选择此参数。

### **Maximum number of peaks to find** — 要识别的最大峰值数量 `10` (默认) | 大于或等于 1 的整数

输入要在每个输入信号中查找的极值数量，为大于或等于 1 的整数。一旦找到最大数量的极值，模块将停止搜索输入信号中的极值。

### **Ignore peaks within threshold of neighboring values** — 忽略低于阈值的峰值 `off` (默认) | `on`

如果希望消除对幅度在相邻值指定阈值内的峰值的检测，请选择此参数。此功能允许模块通过关注高于指定阈值的值来忽略噪声。

清除此参数时，如果当前值大于（或小于）其两个相邻点，模块将当前值识别为峰值。选择此参数时，如果 (*current* – *previous*) > *threshold* 且 (*current* –
*next*) > *threshold*，模块将当前值识别为极大值。如果 (*current* – *previous*) < –*threshold* 且 (*current* –
*next*) < –*threshold*，模块将当前值识别为极小值。

### **Threshold** — 忽略峰值的阈值 `0` (默认) | 正实数标量 | 向量

指定忽略峰值的阈值，为大于或等于 0 的实数标量或所有元素均大于或等于 0 的向量。向量的长度必须等于通道数。

此属性将当前输入值识别为极大值（如果 (*current* – *previous*) > *threshold* 且
(*current* – *next*) > *threshold*）。当前值为极小值（如果 (*current* –
*previous*) < –*threshold* 且 (*current* – *next*) <
–*threshold*）。

#### 依赖

要启用此参数，请选择 **Ignore peaks within threshold of
neighboring values** 参数。

### **Saturate on integer overflow** — 溢出操作方式 `off` (默认) | `on`

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行回绕处理。有关
`saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

#### 依赖

要启用此参数，请选择 **Ignore peaks within threshold of
neighboring values** 参数。
## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

确定输入信号的每个值是局部极小值还是极大值

Peak Finder 模块统计实数值输入信号每一列中局部极值的数量。模块在
**Cnt** 端口输出局部极值的数量。您还可以配置模块输出极值索引、极值以及指示极值是极大值还是极小值的二进制值。要成为极值，一个点必须大于（或小于）其两个相邻点，因此模块在统计极值时不考虑端点。
