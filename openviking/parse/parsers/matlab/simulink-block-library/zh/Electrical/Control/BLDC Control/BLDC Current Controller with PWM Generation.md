---
type: simulink-block
title: 'BLDC Current Controller with PWM Generation'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control'
documentation_page: 'bldccurrentcontrollerwithpwmgeneration'
documentation_source_path: 'ref/bldccurrentcontrollerwithpwmgeneration.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC Current Controller with PWM Generation

## 端口

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **Is** — 测得电流标量

实际电流。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### **Hall** — 霍尔传感器向量

霍尔传感器数据。

**数据类型：** `single` | `double`

### **Direction** — 电机方向标量

电机旋转方向。

**数据类型：** `single` | `double`

### 输出

### **G** — 门极脉冲向量

决定所连接模块中开关行为的脉冲波形。

**数据类型：** `single` | `double`

## 参数

### 控制参数

### **比例增益** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益，*Kp*。

### **积分增益** — 积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益，*Ki*。

### **抗饱和增益** — 抗饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗饱和增益，*Kaw*。

### **采样时间(-1 表示继承)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续可变步长模型中，请使用正标量显式指定采样时间。

#### 依赖关系

如果您将 **采样时间(-1 表示继承)** 设置为 `-1` 并选择 **启用零对消** 选项，则 **离散化采样时间** 参数将可见。

### **离散化采样时间** — 用于离散化的采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，以 s 为单位。零对消需要离散化。

#### 依赖关系

仅当满足以下两个条件时，此参数才可见：

- **采样时间** 设置为 `-1`。
- **启用零对消** 已选择。

### **启用零对消** — 前馈零对消 off（默认）| on

在前馈路径上使用零对消的选项。

#### 依赖关系

如果您选择 **启用零对消** 选项并将 **采样时间(-1 表示继承)** 设置为 `-1`，则 **离散化采样时间** 参数将可见。

### PWM 发生器

### **载波计数器** — 载波计数器模型 `Up`（默认）| `Down` | `Up-Down`

使用载波计数器策略更改 PWM 输出的初始行为：

- Up 计数器 — PWM 输出从导通状态开始时开始。
- Down 计数器 — PWM 输出从关断状态开始时开始。
- Up-down 计数器 — PWM 输出从导通状态中间开始。

### **定时器周期 (s)** — PWM 定时器周期 `0.001`（默认）| 正标量

脉冲宽度调制定时器周期，*Tper*，以秒为单位。

### **基本采样时间 (s)** — PWM 生成的采样时间 `0.0001`（默认）| 正标量

连续 PWM 发生器执行之间的时间，以 s 为单位。在执行期间，模块产生 PWM 输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

为确保生成的 PWM 信号具有足够分辨率，请设置基本采样时间，使得 0<Ts\_pwm≤10Tper，其中：

- *Ts\_pwm* 是 **基本采样时间 (s)**。
- *Tper* 是 **定时器周期 (s)**。

## 所属库

Simscape / Electrical / Control / BLDC Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带脉冲宽度调制生成的离散时间无刷直流电机电流 PI 控制器

BLDC Current Controller with PWM Generation 模块生成脉冲宽度调制 (PWM) 信号并控制无刷直流电机中的电流。该控制器使用此算法。

### 方程

BLDC Current Controller with PWM Generation 通过使用以下方程实现比例积分 (PI) 电流控制，为 BLDC 模块产生占空比

D=(Kp+KiTszz−1)(Is\_ref−Is)

其中：

- *D* 是占空比。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是时间周期。
- *Is\_ref* 是参考电流。
- *Is* 是测得电流。
- *Gzc* 是零对消多项式。

PI 控制算法的闭环传递函数会产生一个零点，可使用前馈路径中的零对消模块将其对消。离散时间中的零对消传递函数为：

GZC(z)=TsKiKpz+(Ts−KpKiKpKi).

该模块通过将占空比与换相信号相乘来获得三相的控制信号。得到的三路控制信号在区间 [-1, 1] 上归一化。

当控制信号的值大于载波计数器值时，PWM 发生器输出 1。否则，PWM 发生器输出 0。
