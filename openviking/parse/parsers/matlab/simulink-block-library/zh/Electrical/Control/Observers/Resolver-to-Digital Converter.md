---
type: simulink-block
title: 'Resolver-to-Digital Converter'
family: 'sps'
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

### **Number of pole pairs** — 所连接电机的极对数 `4`（默认）| 正标量整数

所连接电机的极对数。

### **Phase-looked loop proportional gain** — PLL 比例增益 `15`（默认）| 正标量

锁相环滤波器的比例增益。该值决定 PLL 跟踪并锁定相位角的激进程度。增大该值可更紧密地跟踪相位角的阶跃变化。

### **Phase-looked loop integral gain** — PLL 积分增益 `2.5e5`（默认）| 正标量

锁相环滤波器的积分增益。增大该值可提高消除相位角稳态误差的速率。该值还决定 PLL 跟踪并锁定相位的激进程度。

### **Initial position (rad)** — 初始相位角 `0` `rad`（默认）| 标量

相位角的初始估计值。如果输入信号为向量，请使用标量参数或与输入信号大小相同的向量参数。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 0 | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请指定 `-1`。对于离散时间操作，请指定正整数。对于连续时间操作，请指定 `0`。

**注意**

如果此模块位于掩码子系统或允许在连续操作或离散操作之间切换的其他变体子系统中，请提升采样时间参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Observers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

旋变数字转换器

Resolver-to-Digital Converter 模块对一种换能器进行建模，该换能器将旋转轴的角位置或速度转换为电信号。旋变数字转换器通常用于恶劣、坚固的环境中，例如纯电动汽车。

转换后的信号与轴角的正弦或余弦成正比。

旋变传感器有一个转子绕组，其励磁正弦波通过交流耦合到两个定子绕组。定子绕组（一个正弦线圈和一个余弦线圈）在机械上相位相差 90 度。当转子旋转时，转子位置角相对于定子绕组发生变化。随后必须对产生的幅度调制信号进行增益、解调和后处理，以提取角度和速度信息（[1] 和 [2]）。

### 方程

该模块使用锁相环（PLL）提取旋转轴的角度和速度。PI 控制器使用的误差电压为：

Ve=VyVpcos(Nθ)−VxVpsin(Nθ),

其中：

- `Vp` 是励磁电压。
- `Vx` 是旋变次级绕组的 `x` 电压。
- `Vy` 是旋变次级绕组的 `y` 电压。
- `N` 是旋变的极对数。
- `θ` 是角度。

因此，速度由下式获得：

ω=KpVe+Ki∫Ve,

角度则使用速度通过下式计算：

dθdt=ω。
