---
type: simulink-block
title: 'PI Controller with Integral Anti-Windup (Discrete or Continuous)'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'picontrollerwithintegralantiwindupdiscreteorcontinuous'
documentation_source_path: 'ref/picontrollerwithintegralantiwindupdiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# PI Controller with Integral Anti-Windup (Discrete or Continuous)

## 端口

### 输入

### **e** — 误差信号标量

误差信号，*e(k)*，由参考信号 *r(k)* 与测量信号 *y(k)* 之间的差获得。

**数据类型：** `single` | `double`

### **Reset** — 积分器增益复位标量

积分器的外部复位（上升沿）信号。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制信号标量

控制信号，*u(k)*。

**数据类型：** `single` | `double`

## 参数

### **比例增益** — *Kp* `1`（默认）| 正标量

PI 控制器的比例增益，*Kp*。

### **积分增益** — *Ki* `1`（默认）| 正标量

PI 控制器的积分增益，*Ki*。

### **饱和上限** — *B* `5`（默认）| 大于 **饱和下限** 参数值的标量

PI 控制器输出的上限，*B*。

### **饱和下限** — *A* `-5`（默认）| 标量

PI 控制器输出的下限，*A*。

### **积分器初始条件** — 积分器初始值 `0`（默认）| 标量

仿真开始时刻的积分器值。

### **采样时间（继承时为 -1）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关更多信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关更多信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：支持连续时间仿真

PI Controller with Integral Anti-Windup (Discrete or Continuous) 模块现在支持连续时间仿真。对于连续时间操作，将 **采样时间（继承时为 -1）** 参数设置为 `0`。

## 描述

离散时间或连续时间 PI 控制，带积分抗饱和

The PI Controller with Integral Anti-Windup (Discrete or Continuous) 模块实现带内部抗饱和的离散时间或连续时间 PI 控制。此图显示带内部抗饱和的控制器的等效电路。

### 方程

该模块使用后向欧拉离散化方法计算控制信号：

u(k)=sat(Kpe(k)+sat(KiTszz−1e(k),A,B),A,B),

sat(x,A,B)=min(max(x,A),B),

其中：

- *u* 是控制信号。
- *Kp* 是比例增益系数。
- *e* 是误差信号。
- *Ki* 是积分增益系数。
- *Ts* 是采样周期。
- *A* 是饱和的下限。
- *B* 是饱和的上限。
