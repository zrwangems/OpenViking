---
type: simulink-block
title: 'Variable-Frequency Second-Order Filter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'variablefrequencysecondorderfilter'
documentation_source_path: 'ref/variablefrequencysecondorderfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Frequency Second-Order Filter

## 端口

### 输入

### **u** — 滤波器输入标量

滤波器输入。

**数据类型：** `single` | `double`

### **fn** — 自然频率标量

自然频率。

**数据类型：** `single` | `double`

### 输出

### **y** — 滤波后的输出标量

滤波后的输出。

**数据类型：** `single` | `double`

## 参数

### 主要

### **Filter type** — 滤波器类型 `Low-pass`（默认） | `High-pass` | `Band-pass` | `Band-stop`

二阶滤波器的类型。

### **Initial natural frequency (Hz)** — 初始自然频率 `60`（默认） | 正标量

仿真开始时的自然频率，单位为 Hz。

### 初始条件

### **Damping factor** — 阻尼系数 `0.707`（默认） | 非负标量

滤波器的阻尼系数。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认） | `0` | 正标量

连续模块执行之间的时间。执行期间，模块生成输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Initial amplitude** — 初始幅值 `0`（默认） | 非负标量

仿真开始时的幅值。

### **Initial phase (rad)** — 初始相位 `0`（默认） | 非负标量

仿真开始时的相位，单位为 rad。

### **Initial frequency (Hz)** — 初始频率 `0`（默认） | 标量

仿真开始时的频率，单位为 Hz。

### **Initial bias** — 初始偏置 `0`（默认） | 非负标量

仿真开始时的偏置。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散时间或连续时间可变频率二阶滤波器

Variable-Frequency Second-Order Filter 模块实现四种不同类型的二阶滤波器，每种都具有外部频率输入。滤波器可用于衰减测量信号中的噪声。

该模块提供以下滤波器类型：

- Low pass — 仅允许频率低于截止频率 fc 的信号 f 通过。
- High pass — 仅允许频率高于截止频率 fc 的信号 f 通过。
- Band pass — 仅允许频率介于两个截止频率 fc1 和 fc2 之间的信号 f 通过。
- Band stop — 阻止频率介于两个截止频率 fc1 和 fc2 之间的信号 f 通过。

| 滤波器类型 | 频率范围，f | |
| --- | --- | --- |
| **Low-Pass** |  | f<fc |
| **High-Pass** |  | f>fc |
| **Band-Pass** |  | fc1<f<fc2 |
| **Band-Stop** |  | fc1<f<fc2 |

### 方程

滤波器的二阶导数状态方程为：

d2xdt2=u−2ζωndxdt−ωn2x

其中：

- *x* 是滤波器的内部状态。
- *u* 是滤波器输入。
- *ωn* 是滤波器的自然频率。
- *ζ* 是滤波器的阻尼系数。

对于每种滤波器类型，该表将模块输出 y(x)（作为滤波器内部状态的函数）映射到 *s* 域传递函数 G(s)。

| 滤波器类型 | 输出，y(x) | 传递函数，G(s) |
| --- | --- | --- |
| **Low-Pass** | ωn2x | ωn2s2+2ζωns+ωn2 |
| **High-Pass** | d2xdt2 | s2s2+2ζωns+ωn2 |
| **Band-Pass** | 2ζωndxdt | 2ζωnss2+2ζωns+ωn2 |
| **Band-Stop** | d2xdt2+x | s2+ωn2s2+2ζωns+ωn2 |

对于初始化：

x˙(0)=dxdt|t=0

u(0)=u1(0)+u2(0)

u1(0)=A0ejφ0

u2(0)=b0ejπ2

其中：

- x(0) 是滤波器的初始状态。
- u(0) 是滤波器的初始输入。
- u1(0) 是稳态初始输入的交流分量。
- A0 是初始幅值。
- φ0 是初始相位。
- u2(0) 是稳态初始输入的直流分量。
- b0 是初始偏置。

在 *s* 域中 s=jω0。因此，对于初始频率 ω0：

x˙(0)=Im(jω0u1(0)−ω02+jω02ζωn+ωn2).

x(0)=Im(x˙(0)ωn2jω0+u2(0))
