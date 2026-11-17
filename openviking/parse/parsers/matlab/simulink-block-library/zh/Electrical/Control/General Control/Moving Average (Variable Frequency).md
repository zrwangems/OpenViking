---
type: simulink-block
title: 'Moving Average (Variable Frequency)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'movingaveragevariablefrequency'
documentation_source_path: 'ref/movingaveragevariablefrequency.html'
language: zh-CN
chinese_source: worker-translation
---

# Moving Average (Variable Frequency)

## 端口
```yaml
ports:
- name: u
  summary: 滑动平均输入 标量 | 向量
  direction: input
  data_types: single | double
- name: f
  summary: 频率，Hz 标量 | 向量
  direction: input
  data_types: single | double
- name: Mean
  summary: 滑动平均输出 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 滑动平均输入 标量 | 向量

滑动平均输入，指定为标量或向量。

**数据类型：** `single` | `double`

### **f** — 频率，Hz 标量 | 向量

频率，以 Hz 为单位指定为标量或向量。

**数据类型：** `single` | `double`
### 输出

### **Mean** — 滑动平均输出 标量 | 向量

输入信号的滑动平均值，以标量或向量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Initial frequency (Hz)
  summary: 初始信号频率 60（默认）| 正标量 | 含正值的向量
  group: ''
- name: Minimum frequency (Hz)
  summary: 最小信号频率 30（默认）| 正标量 | 含正值的向量
  group: ''
- name: Initial value
  summary: 初始输入信号值 0（默认）| 标量
  group: ''
- name: Buffer size
  summary: 缓冲区大小 8192（默认）| 标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: ''
```

### **Initial frequency (Hz)** — 初始信号频率 `60`（默认）| 正标量 | 含正值的向量

信号的初始频率，以 Hz 为单位。如果使用向量指定初始频率，则该向量必须与输入向量的维度匹配。

### **Minimum frequency (Hz)** — 最小信号频率 `30`（默认）| 正标量 | 含正值的向量

信号的最小频率，以 Hz 为单位。如果使用向量指定最小频率，则该向量必须与输入向量的维度匹配。

### **Initial value** — 初始输入信号值 `0`（默认）| 标量

输入信号的初始值。

### **Buffer size** — 缓冲区大小 `8192`（默认）| 标量

缓冲区的大小。

#### 依赖关系

要启用此参数，请将 **Sample time (-1 for inherited)** 设置为 `0`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

变频滑动平均值计算

Moving Average (Variable Frequency) 模块计算变频输入信号的滑动平均值。使用此模块可滤除较高频率的信号分量并平滑含噪信号。

### 方程

该模块基于滑动时间窗口计算滑动平均值。连续时间的滑动平均值等于

u¯=1T0∫t0t0+T0u(t)dt,

其中：

- *u(t)* 是输入信号。
- *T0* 等于 1f。
- *f* 是信号的基频。
- *t0* 是时间窗口内积分的初始时间。

离散时间的滑动平均值等于：

u¯(k)=1T0∑i=0n−1u(k−i)。

**注意**

如果将此模块用于连续时间操作，并将 **Sample time (-1 for inherited)** 参数设置为 `0`，则还应指定 **Buffer size** 参数的值，以确保其覆盖滑动时间窗口。

### 假设和限制

- 输出在时间区间 `[0, T0]` 内使用初始条件进行初始化。
- 如果将此模块用于离散时间操作，并将 **Sample time (-1 for inherited)** 参数设置为 `-1`，则最大可变整数延迟设置为 4096 个采样。要将最大可变整数延迟计算为最小频率和采样时间的函数，请将 **Sample time (-1 for inherited)** 参数设置为正值。
