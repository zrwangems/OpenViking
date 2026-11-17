---
type: simulink-block
title: 'Resolver-to-Digital Converter'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Observers'
documentation_page: 'resolvertodigitalconverter'
documentation_source_path: 'ref/resolvertodigitalconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Resolver-to-Digital Converter

## 端口

### 输入

### **Vp** — 电压相位角标量

对应于电压相位角的 Simulink 信号。

**数据类型：** `single` | `double`

### **Vx** — `x` 轴电压标量

对应于 `x` 轴电压的 Simulink 信号。

**数据类型：** `single` | `double`

### **Vy** — `y` 轴电压标量

对应于 `y` 轴电压的 Simulink 信号。

**数据类型：** `single` | `double`
### 输出

### **Velocity** — 旋转速度标量

对应于旋转速度的 Simulink 信号。

**数据类型：** `single` | `double`

### **Angle** — 旋转角度标量

对应于旋转角度的 Simulink 信号。

**数据类型：** `single` | `double`

## 参数

### **极对数** — 所连接电机中的极对数 `4`（默认） | 正整数标量

所连接电机中的极对数。

### **锁相环比例增益** — PLL 比例增益 `15`（默认） | 正标量

锁相环滤波器的比例增益。此值决定 PLL 跟踪并锁定到相位角的积极程度。增大此值可更紧密地跟踪相位角的阶跃变化。

### **锁相环积分增益** — PLL 积分增益 `2.5e5`（默认） | 正标量

锁相环滤波器的积分增益。增大此值可提高相位角中稳态误差被消除的速率。此值还决定 PLL 跟踪并锁定到相位的积极程度。

### **初始位置 (rad)** — 初始相位角 `0` `rad`（默认） | 标量

相位角的初始估计值。如果输入信号是向量，请使用标量参数，或使用与输入信号大小相同的向量参数。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认） | 0 | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

对于继承的离散时间操作，请指定 `-1`。对于离散时间操作，请指定正整数。对于连续时间操作，请指定 `0`。

**注意**

如果此模块位于掩码子系统中，或位于允许在连续操作或离散操作之间切换的另一个变体子系统中，请提升采样时间参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅“提升掩码上的模块参数”。

## 所属库

Simscape / Electrical / Control / Observers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

旋转变压器-数字转换器

Resolver-to-Digital Converter 模块对一种变换器建模，该变换器将旋转轴的角位置或速度转换为电信号。旋转变压器-数字转换器通常用于恶劣、严苛的环境，例如纯电动汽车。

转换后的信号与轴角的正弦或余弦成正比。

旋转变压器传感器有一个转子绕组，其励磁正弦波以交流耦合方式连接到两个定子绕组。定子绕组（一个正弦线圈和一个余弦线圈）在机械上相位相差 90 度。当转子旋转时，转子位置角相对于定子绕组发生变化。然后必须对产生的幅度调制信号进行增益处理、解调 and 后处理，以提取角度和速度信息（[1] 和 [2]）。

### 方程

该模块使用锁相环 (PLL) 来提取旋转轴的角度和速度。PI 控制器使用的误差电压通过下式获得：

Ve=VyVpcos(Nθ)−VxVpsin(Nθ),

其中：

- `Vp` 是励磁电压。
- `Vx` 是旋转变压器次级绕组的 `x` 电压。
- `Vy` 是旋转变压器次级绕组的 `y` 电压。
- `N` 是旋转变压器的极对数。
- `θ` 是角度。

因此，速度通过下式获得：

ω=KpVe+Ki∫Ve,

并且使用下式由速度计算角度：

dθdt=ω.
