---
type: simulink-block
title: 'Moving Average'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'movingaverage'
documentation_source_path: 'ref/movingaverage.html'
language: zh-CN
chinese_source: worker-translation
---

# Moving Average

## 端口

### 输入

### **u** — 移动平均输入 标量 | 向量

输入信号。

**数据类型：** `single` | `double`
### 输出

### **Mean** — 移动平均输出 标量 | 向量

输入信号的移动平均值。

**数据类型：** `single` | `double`

## 参数

### **Fundamental frequency (Hz)** — 信号基频 `60`（默认）| 正标量 | 具有正值的向量

信号的基频，以 Hz 为单位。如果使用向量指定基频，则该向量必须与输入向量维度匹配。

### **Initial value** — 输入信号初始值 `0`（默认）| 标量

输入信号的初始值。

### **Buffer size** — 缓冲区大小 `8192`（默认）| 标量

缓冲区的大小。

#### 依赖关系

要启用此参数，请将 **Sample time (-1 for inherited)** 设置为 `0`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，该模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

移动平均值计算

Moving Average 模块计算输入信号的移动平均值。使用此模块可滤除较高频率的信号分量并平滑含噪信号。

### 方程

该模块基于移动时间窗口计算移动平均值。连续时间的移动平均值等于

u¯=1T0∫t0t0+T0u(t)dt,

其中：

- *u(t)* 是输入信号。
- *T0* 等于 1f。
- *f* 是信号的基频。
- *t0* 是时间窗口中积分的初始时间。

离散时间的移动平均值等于：

u¯(k)=1T0∑i=0n−1u(k−i).

**注意**

如果将此模块用于连续时间操作，并将 **Sample time (-1 for inherited)** 参数设置为 `0`，则还应指定 **Buffer size** 参数的值，以确保其覆盖移动时间窗口。

### 假设

该模块在时间区间 `[0, T0]` 内使用初始条件初始化输出。
