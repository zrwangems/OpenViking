---
type: simulink-block
title: 'PI Controller (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Controllers'
documentation_page: 'picontrollerdiscreteorcontinuous'
documentation_source_path: 'ref/picontrollerdiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# PI Controller (Discrete or Continuous)

## 端口

### 输入

### **e** — 误差信号标量

误差信号 *e(k)*，由参考信号 *r(k)* 与测量信号 *y(k)* 之差得到。

**数据类型：** `single` | `double`

### **du** — 控制信号饱和标量

*du(k)*，即饱和控制信号 *u^sat(k)* 与未饱和控制信号 *u(k)* 之间的差值。如果 *du(k)* 为零，则禁用抗饱和。

描述

**数据类型：** `single` | `double`

### **Reset** — 积分器增益复位标量

积分器的外部复位（上升沿）信号。

**数据类型：** `single` | `double`

### 输出

### **u** — 控制信号标量

控制信号 *u(k)*。

**数据类型：** `single` | `double`

## 参数

### **比例增益** — *Kp* `1` (默认) | 正标量

PI 控制器的比例增益 *Kp*。

### **积分增益** — *Ki* `1` (默认) | 正标量

PI 控制器的积分增益 *Ki*。

### **抗饱和增益** — *Kaw* `1` (默认) | 正标量

PI 控制器的抗饱和增益 *Kaw*。

### **积分器初始条件** — 积分器初始值 `0` (默认) | 标量

仿真开始时的积分器值。

### **采样时间（-1 表示 inherited）** — 模块采样时间 `-1` (默认) | `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于 inherited 离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的封装子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：支持连续时间仿真

PI Controller (Discrete or Continuous) 模块现在支持连续时间仿真。对于连续时间操作，将 **采样时间（-1 表示 inherited）** 参数设置为 `0`。

## 描述

带外部抗饱和输入的离散时间或连续时间 PI 控制器

Discrete PI Controller 模块实现带外部抗饱和输入的离散时间或连续时间 PI 控制。

此图展示了带外部抗饱和输入的控制器等效电路。

### 方程

PI Controller (Discrete or Continuous) 模块使用后向欧拉离散化方法计算控制信号：

u(k)=[Kp+(Ki+du(k)Kaw)Tszz−1]e(k),

其中

- *u* 是控制信号。
- *Kp* 是比例增益系数。
- *Ki* 是积分增益系数。
- *Kaw* 是抗饱和增益系数。
- *Ts* 是采样周期。
- *e* 是误差信号。

为防止过度超调，模块可以使用反算实现外部抗饱和机制。它输入 *du(k)*，即饱和控制信号 *usat(k)* 与计算得到的未饱和控制信号 *u(k)* 之间的差值。然后，它将差值乘以抗饱和系数，并将来自积分增益的放大信号相加。
